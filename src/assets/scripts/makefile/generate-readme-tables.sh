#!/usr/bin/env bash
# Genererer domene-tabell, skjema-tabell og modellkatalog-tabell for README.md
# Køyr: ./scripts/generate-readme-tables.sh [README-fil]
# Output: Oppdatert README-fil med auto-genererte tabellar

set -euo pipefail
trap 'echo "ERROR in ${BASH_SOURCE[0]}:${LINENO} — command: ${BASH_COMMAND}" >&2; exit 1' ERR

README="${1:-README.md}"

if [[ ! -f "$README" ]]; then
  echo "❌ Feil: $README finst ikkje"
  exit 1
fi

echo "🔧 Genererer auto-genererte tabellar for $README..."

# Katalog for støttescripts
SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)

# Opprett temp-fil
TEMP_README=$(mktemp)

# --- Funksjon: Generer skjema-tabell ---
generate_schema_table() {
  echo "| Domene | Skjema | Skildring | Dokumentasjon"
  echo "|---|---|---|---|"

  # Domene-rekkefølgje (same som i domene-tabellen)
  DOMAIN_ORDER=("fair" "ap-no" "referanse" "ngr" "oreg" "fint" "samt")

  # Bygg assosiativ array: domain -> liste av skjema-filer
  declare -A DOMAIN_SCHEMAS

  while IFS= read -r schema_file; do
    domain=$(echo "$schema_file" | cut -d'/' -f3)

    # Hopp over modellkatalog og begrepskatalog (handterast separat)
    [[ "$domain" == "modellkatalog" ]] && continue
    [[ "$domain" == "begrepskatalog" ]] && continue

    schema_dir=$(dirname "$schema_file")
    schema_name=$(basename "$schema_dir")
    schema_basename=$(basename "$schema_file" "-schema.yaml")

    # Berre inkluder hovudskjema (der filnamn matcher katalognamn)
    # t.d. modelldcat-ap-no/modelldcat-ap-no-schema.yaml (OK)
    # men ikkje modelldcat-ap-no/modelldcat-katalog-schema.yaml (hopp over)
    [[ "$schema_basename" != "$schema_name" ]] && continue

    # Legg til skjema i domenet sin liste
    if [[ -z "${DOMAIN_SCHEMAS[$domain]:-}" ]]; then
      DOMAIN_SCHEMAS[$domain]="$schema_file"
    else
      DOMAIN_SCHEMAS[$domain]="${DOMAIN_SCHEMAS[$domain]}"$'\n'"$schema_file"
    fi
  done < <(find src/linkml -name "*-schema.yaml" -type f | sort)

  # Iterer gjennom domene i riktig rekkefølgje
  for domain in "${DOMAIN_ORDER[@]}"; do
    # Hopp over domene utan skjema
    [[ -z "${DOMAIN_SCHEMAS[$domain]:-}" ]] && continue

    # Iterer gjennom skjema i dette domenet
    while IFS= read -r schema_file; do
      [[ -z "$schema_file" ]] && continue

      schema_dir=$(dirname "$schema_file")
      schema_name=$(basename "$schema_dir")

      # Hent description frå skjemafil (dynamisk via Python-script)
      description=$(python3 src/assets/scripts/makefile/extract-schema-metadata.py "$schema_file" description)

      # Hent see_also frå skjemafil (første URI via Python-script)
      see_also_uri=$(python3 src/assets/scripts/makefile/extract-schema-metadata.py "$schema_file" see_also)

      # Format dokumentasjonslenkje dersom see_also finst
      if [[ -n "$see_also_uri" ]]; then
        # Ekstraher domenenamn frå URI (t.d. data.norge.no, www.go-fair.org)
        doc_domain=$(echo "$see_also_uri" | sed -E 's|https?://([^/]+).*|\1|')
        doc_link="[$doc_domain]($see_also_uri)"
      else
        doc_link=""
      fi

      # Konverter src/linkml/<domain>/<modell>/ til <domain>/<modell>/ for GitHub Pages
      ghpages_schema_link="${schema_dir#src/linkml/}"

      echo "| [$domain]($domain/) | [$schema_name]($ghpages_schema_link/) | $description | $doc_link"
    done <<< "${DOMAIN_SCHEMAS[$domain]}"
  done
}

# --- Funksjon: Generer begrepskatalog-tabell ---
generate_begrepskatalog_table() {
  echo "| Domene | Begrepskatalog | Organisasjon | Skildring | Generator |"
  echo "|---|---|---|---|---|"

  local extractor="$SCRIPT_DIR/extract-schema-metadata.py"

  # Finn alle begrepskatalogar
  while IFS= read -r schema_file; do
    schema_dir=$(dirname "$schema_file")
    schema_name=$(basename "$schema_dir")

    # Hent title frå skjema, ekstraher organisasjonsnamn (før " - Begrepskatalog")
    title=$("$extractor" "$schema_file" title)
    # Fjern " - Begrepskatalog" og alt etter det (inkl. eventuelle parentesar)
    org=$(echo "$title" | sed 's/ - Begrepskatalog.*//')

    # Fallback dersom title manglar eller ikkje følgjer mønsteret
    if [[ -z "$org" || "$org" == "$title" ]]; then
      org="Ukjend"
    fi

    # Lenk begrepskatalog-domenet til dokumentasjonsportalen
    domain_link="https://brreg.github.io/linkml-datamodellering-no/begrepskatalog/"

    # Konverter src/linkml/begrepskatalog/<katalog>/ til begrepskatalog/<katalog>/ for GitHub Pages
    ghpages_link="${schema_dir#src/linkml/}"

    echo "| [begrepskatalog]($domain_link) | [$schema_name]($ghpages_link/) | $org | Begrepskatalog for $org sine begrep | [\`gen-begrepskatalog-instance\`](COMMANDS.md#vedlikehald) |"
  done < <(find src/linkml/begrepskatalog -name "*-schema.yaml" -type f | sort)
}

# --- Funksjon: Generer modellkatalog-tabell ---
generate_modellkatalog_table() {
  echo "| Domene | Modellkatalog | Organisasjon | Skildring | Generator |"
  echo "|---|---|---|---|---|"

  local extractor="$SCRIPT_DIR/extract-schema-metadata.py"

  # Finn alle modellkatalogar
  while IFS= read -r schema_file; do
    schema_dir=$(dirname "$schema_file")
    schema_name=$(basename "$schema_dir")

    # Hent title frå skjema, ekstraher organisasjonsnamn (før " - Modellkatalog")
    title=$("$extractor" "$schema_file" title)
    # Fjern " - Modellkatalog" og alt etter det (inkl. eventuelle parentesar)
    org=$(echo "$title" | sed 's/ - Modellkatalog.*//')

    # Fallback dersom title manglar eller ikkje følgjer mønsteret
    if [[ -z "$org" || "$org" == "$title" ]]; then
      org="Ukjend"
    fi

    # Lenk modellkatalog-domenet til dokumentasjonsportalen
    domain_link="https://brreg.github.io/linkml-datamodellering-no/modellkatalog/"

    # Konverter src/linkml/modellkatalog/<katalog>/ til modellkatalog/<katalog>/ for GitHub Pages
    ghpages_link="${schema_dir#src/linkml/}"

    echo "| [modellkatalog]($domain_link) | [$schema_name]($ghpages_link/) | $org | Modellkatalog for $org sine informasjonsmodellar | [\`gen-modellkatalog-instance\`](COMMANDS.md#vedlikehald) |"
  done < <(find src/linkml/modellkatalog -name "*-schema.yaml" -type f | sort)
}

# --- Hovudlogikk: Bygg ny README med auto-genererte seksjoner ---

IN_SCHEMA_TABLE=false
IN_BEGREPSKATALOG_TABLE=false
IN_MODELLKATALOG_TABLE=false

while IFS= read -r line; do
  # Skjema-tabell
  if [[ "$line" =~ ^\<\!--\ BEGIN\ AUTO-GENERATED:.*SCHEMA\ TABLE ]]; then
    IN_SCHEMA_TABLE=true
    echo "<!-- BEGIN AUTO-GENERATED: src/assets/scripts/makefile/generate-readme-tables.sh generate_schema_table -->" >> "$TEMP_README"
    generate_schema_table >> "$TEMP_README"
    continue
  elif [[ "$line" =~ ^\<\!--\ END\ AUTO-GENERATED:.*SCHEMA\ TABLE ]]; then
    IN_SCHEMA_TABLE=false
    echo "<!-- END AUTO-GENERATED: src/assets/scripts/makefile/generate-readme-tables.sh generate_schema_table -->" >> "$TEMP_README"
    continue
  elif $IN_SCHEMA_TABLE; then
    continue  # Hopp over eksisterande innhald
  fi

  # Begrepskatalog-tabell
  if [[ "$line" =~ ^\<\!--\ BEGIN\ AUTO-GENERATED:.*BEGREPSKATALOG\ TABLE ]]; then
    IN_BEGREPSKATALOG_TABLE=true
    echo "<!-- BEGIN AUTO-GENERATED: src/assets/scripts/makefile/generate-readme-tables.sh generate_begrepskatalog_table -->" >> "$TEMP_README"
    generate_begrepskatalog_table >> "$TEMP_README"
    continue
  elif [[ "$line" =~ ^\<\!--\ END\ AUTO-GENERATED:.*BEGREPSKATALOG\ TABLE ]]; then
    IN_BEGREPSKATALOG_TABLE=false
    echo "<!-- END AUTO-GENERATED: src/assets/scripts/makefile/generate-readme-tables.sh generate_begrepskatalog_table -->" >> "$TEMP_README"
    continue
  elif $IN_BEGREPSKATALOG_TABLE; then
    continue  # Hopp over eksisterande innhald
  fi

  # Modellkatalog-tabell
  if [[ "$line" =~ ^\<\!--\ BEGIN\ AUTO-GENERATED:.*MODELLKATALOG\ TABLE ]]; then
    IN_MODELLKATALOG_TABLE=true
    echo "<!-- BEGIN AUTO-GENERATED: src/assets/scripts/makefile/generate-readme-tables.sh generate_modellkatalog_table -->" >> "$TEMP_README"
    generate_modellkatalog_table >> "$TEMP_README"
    continue
  elif [[ "$line" =~ ^\<\!--\ END\ AUTO-GENERATED:.*MODELLKATALOG\ TABLE ]]; then
    IN_MODELLKATALOG_TABLE=false
    echo "<!-- END AUTO-GENERATED: src/assets/scripts/makefile/generate-readme-tables.sh generate_modellkatalog_table -->" >> "$TEMP_README"
    continue
  elif $IN_MODELLKATALOG_TABLE; then
    continue  # Hopp over eksisterande innhald
  fi

  # Behald alle andre linjer
  echo "$line" >> "$TEMP_README"
done < "$README"

# Erstatt original med oppdatert versjon
mv "$TEMP_README" "$README"

echo "✅ $README er oppdatert med auto-genererte tabellar"
