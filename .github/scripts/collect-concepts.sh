#!/usr/bin/env bash
# Samlar alle begrep frå begrepssamlingar og genererer begrepskatalog per organisasjon.
#
# For kvar organisasjon:
#  1. Finn alle begrepssamlingar med aggregation.organization = <org-nr>
#  2. Samle alle begrep-YAML-filer frå begrepssamling-<namn>/begrep/*.yaml
#  3. Generer aggregert begrepskatalog.yaml i begrepskatalog/<org>-begrepskatalog/data/<org>-begrepskatalog/
#
# Køyrast av CI før generatorfasen.

set -euo pipefail

REPO_ROOT="${REPO_ROOT:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}"
SRC_DIR="${REPO_ROOT}/src/linkml"
BEGREPSKATALOG_DIR="${SRC_DIR}/begrepskatalog"

# Fargar for utskrift
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

log_info() {
    echo -e "${GREEN}[collect-concepts]${NC} $*"
}

log_warn() {
    echo -e "${YELLOW}[collect-concepts]${NC} $*"
}

log_error() {
    echo -e "${RED}[collect-concepts]${NC} $*" >&2
}

# Finn alle begrepssamlingar med aggregation-metadata
find_begrepssamlingar() {
    find "${SRC_DIR}" -type f -name "build.yaml" -path "*/begrepssamling-*/build.yaml" | sort
}

# Hent aggregation.organization frå build.yaml
get_organization() {
    local build_yaml="$1"
    yq eval '.aggregation.organization // ""' "${build_yaml}" 2>/dev/null || echo ""
}

# Hent aggregation.catalog_name frå build.yaml
get_catalog_name() {
    local build_yaml="$1"
    yq eval '.aggregation.catalog_name // ""' "${build_yaml}" 2>/dev/null || echo ""
}

# Samle alle begrep frå ei begrepssamling
collect_begrep_from_samling() {
    local samling_dir="$1"
    local begrep_dir="${samling_dir}/begrep"

    if [[ ! -d "${begrep_dir}" ]]; then
        log_warn "Hoppar over ${samling_dir} — manglar begrep/-mappe"
        return
    fi

    find "${begrep_dir}" -type f -name "*.yaml" | sort
}

# Generer begrepskatalog.yaml for ein organisasjon
generate_begrepskatalog() {
    local org_nr="$1"
    local catalog_name="$2"
    shift 2
    local begrepssamlingar=("$@")

    if [[ -z "${catalog_name}" ]]; then
        log_error "Manglar catalog_name for organisasjon ${org_nr}"
        return 1
    fi

    local catalog_dir="${BEGREPSKATALOG_DIR}/${catalog_name}/data/${catalog_name}"
    local catalog_file="${catalog_dir}/${catalog_name}.yaml"

    log_info "Genererer ${catalog_name}.yaml for organisasjon ${org_nr}"

    # Opprett katalogmappe
    mkdir -p "${catalog_dir}"

    # Skriv header
    cat > "${catalog_file}" <<EOF
# Generert av CI frå collect-concepts.sh — ikkje rediger manuelt
# Samlar alle begrep frå begrepssamlingane til organisasjon ${org_nr}

begrep:
EOF

    # Samle alle begrep-filer frå alle begrepssamlingane
    local begrep_count=0
    for samling_dir in "${begrepssamlingar[@]}"; do
        local samling_name
        samling_name="$(basename "${samling_dir}")"
        log_info "  Samlar begrep frå ${samling_name}"

        while IFS= read -r begrep_file; do
            if [[ -z "${begrep_file}" ]]; then
                continue
            fi

            # Les YAML-innhald og legg til som list-element
            # Indenter heile objektet med 2 mellomrom (list-element) + 2 for feltnamn
            echo "  - $(head -1 "${begrep_file}")" >> "${catalog_file}"
            tail -n +2 "${begrep_file}" | sed 's/^/    /' >> "${catalog_file}"
            echo "" >> "${catalog_file}"
            ((begrep_count++))
        done < <(collect_begrep_from_samling "${samling_dir}")
    done

    log_info "✓ Genererte ${catalog_file} med ${begrep_count} begrep"
}

# Hovudlogikk
main() {
    log_info "Startar aggregering av begrep til begrepskatalogar"

    # Sjekk at yq er installert
    if ! command -v yq &> /dev/null; then
        log_error "yq er ikkje installert — kan ikkje parse YAML"
        exit 1
    fi

    # Finn alle begrepssamlingar og grupper per organisasjon
    declare -A org_samlings  # org_nr -> liste av samling_dir

    while IFS= read -r build_yaml; do
        if [[ -z "${build_yaml}" ]]; then
            continue
        fi

        local org_nr
        org_nr="$(get_organization "${build_yaml}")"

        if [[ -z "${org_nr}" ]]; then
            log_warn "Hoppar over $(dirname "${build_yaml}") — manglar aggregation.organization"
            continue
        fi

        local catalog_name
        catalog_name="$(get_catalog_name "${build_yaml}")"

        if [[ -z "${catalog_name}" ]]; then
            log_warn "Hoppar over $(dirname "${build_yaml}") — manglar aggregation.catalog_name"
            continue
        fi

        local samling_dir
        samling_dir="$(dirname "${build_yaml}")"

        # Legg til i org_samlings-array
        if [[ -z "${org_samlings[${org_nr}]:-}" ]]; then
            org_samlings["${org_nr}"]="${samling_dir}|${catalog_name}"
        else
            org_samlings["${org_nr}"]+=" ${samling_dir}|${catalog_name}"
        fi
    done < <(find_begrepssamlingar)

    # Generer begrepskatalog per organisasjon
    for org_nr in "${!org_samlings[@]}"; do
        # Split samling_dir og catalog_name (første element har catalog_name)
        local samlings_str="${org_samlings[${org_nr}]}"
        local first_entry
        first_entry="$(echo "${samlings_str}" | awk '{print $1}')"
        local catalog_name
        catalog_name="$(echo "${first_entry}" | cut -d'|' -f2)"

        # Ekstraker berre samling_dir (fjern catalog_name)
        local samling_dirs=()
        for entry in ${samlings_str}; do
            samling_dirs+=("$(echo "${entry}" | cut -d'|' -f1)")
        done

        generate_begrepskatalog "${org_nr}" "${catalog_name}" "${samling_dirs[@]}"
    done

    log_info "✓ Ferdig med aggregering av begrepskatalogar"
}

main "$@"
