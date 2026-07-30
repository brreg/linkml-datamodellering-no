#!/usr/bin/env bash
# Migrer description og see_also i skjema frå hardkoda verdiar til skjemafiler
# Brukar hardkoda verdiar frå generate-readme-tables.sh som kjelde

set -euo pipefail

# Hardkoda skildringar (frå generate-readme-tables.sh)
declare -A DESCRIPTIONS=(
  ["fair-metadata"]="**FAIR**-metadataoverbygning (**FAIR**-prinsippa)"
  ["common-ap-no"]="Felles slot-definisjonar for alle AP-NO-profilar"
  ["cpsv-ap-no"]="Offentlege tenester og hendingar"
  ["dcat-ap-no"]="Datakatalogar og datasett"
  ["dqv-ap-no"]="Datakvalitet"
  ["modelldcat-ap-no"]="Informasjonsmodellar"
  ["skos-ap-no"]="Omgrepsamlingar"
  ["xkos-ap-no"]="Utvida klassifikasjon"
  ["fint-common"]="Felles klassar for FINT"
  ["fint-administrasjon"]="Lønn, arbeidsforhold, organisasjon"
  ["fint-arkiv"]="Sak, journal, dokument"
  ["fint-okonomi"]="Økonomi og rekneskap"
  ["fint-personvern"]="Personvernmeldingar"
  ["fint-ressurs"]="Ressursar"
  ["fint-utdanning"]="Utdanning og skule"
  ["ngr-adresse"]="Adresse"
  ["ngr-eiendom"]="Fast eigedom, matrikkeleining og bygning"
  ["ngr-person"]="Person, identifikasjon og familierelasjonar"
  ["ngr-virksomhet"]="Verksemder, roller og organisasjonsstruktur"
  ["enhetsregisteret-bvrinn"]="Berettigede, verger, rettighetshavere i næring (BVRiNN)"
  ["register-over-aksjeeiere"]="Aksjeeigarar og eigedelar"
  ["samt-bu"]="Skular og barnehagar"
  ["referanse"]="Enkel eksempelmodell for å demonstrere gyldig LinkML-struktur"
)

# Hardkoda dokumentasjonslenkjer (frå generate-readme-tables.sh)
declare -A DOC_LINKS=(
  ["fair-metadata"]="https://www.go-fair.org/fair-principles/"
  ["cpsv-ap-no"]="https://data.norge.no/specification/cpsv-ap-no"
  ["dcat-ap-no"]="https://data.norge.no/specification/dcat-ap-no"
  ["dqv-ap-no"]="https://data.norge.no/specification/dqv-ap-no"
  ["modelldcat-ap-no"]="https://data.norge.no/specification/modelldcat-ap-no"
  ["skos-ap-no"]="https://data.norge.no/specification/skos-ap-no-begrep"
  ["xkos-ap-no"]="https://data.norge.no/specification/xkos-ap-no"
  ["fint-administrasjon"]="https://informasjonsmodell.felleskomponent.no/docs/package_administrasjon?v=v4.0.20"
  ["fint-arkiv"]="https://informasjonsmodell.felleskomponent.no/docs/package_arkiv?v=v4.0.20"
  ["fint-okonomi"]="https://informasjonsmodell.felleskomponent.no/docs/package_okonomi?v=v4.0.20"
  ["fint-personvern"]="https://informasjonsmodell.felleskomponent.no/docs/package_personvern?v=v4.0.20"
  ["fint-ressurs"]="https://informasjonsmodell.felleskomponent.no/docs/package_ressurs?v=v4.0.20"
  ["fint-utdanning"]="https://informasjonsmodell.felleskomponent.no/docs/package_utdanning?v=v4.0.20"
  ["ngr-adresse"]="https://informasjonsforvaltning.github.io/nasjonale-grunndata/#Adresse"
  ["ngr-eiendom"]="https://informasjonsforvaltning.github.io/nasjonale-grunndata/#Temaomr%C3%A5deEiendom"
  ["ngr-person"]="https://informasjonsforvaltning.github.io/nasjonale-grunndata/#Person"
  ["ngr-virksomhet"]="https://informasjonsforvaltning.github.io/nasjonale-grunndata/#Virksomhet"
  ["samt-bu"]="https://docs.samt-bu.no/om/"
)

MODE="${1:-}"

if [[ "$MODE" == "--schema" ]]; then
  SCHEMA_NAME="${2:-}"
  if [[ -z "$SCHEMA_NAME" ]]; then
    echo "❌ Bruk: $0 --schema <skjema-namn>"
    exit 1
  fi
  # Prøv først <domain>/<schema>/<schema>-schema.yaml, deretter <domain>/<schema>-schema.yaml (for referanse)
  SCHEMA_FILE=$(find src/linkml -name "$SCHEMA_NAME-schema.yaml" -type f | grep -v begrepskatalog | grep -v modellkatalog | head -1)
  if [[ -z "$SCHEMA_FILE" ]]; then
    echo "❌ Fann ikkje skjema: $SCHEMA_NAME"
    exit 1
  fi
  SCHEMAS=("$SCHEMA_FILE")
elif [[ "$MODE" == "--all" ]]; then
  # Finn alle skjema (ekskluder begrepskatalog og modellkatalog)
  mapfile -t SCHEMAS < <(find src/linkml -name "*-schema.yaml" -type f | \
    grep -v begrepskatalog | \
    grep -v modellkatalog | \
    grep -v -E '(dqv-core|modelldcat-katalog|modelldcat-modell)-schema.yaml' | \
    sort)
else
  echo "Bruk:"
  echo "  $0 --schema <skjema-namn>   # Migrer eitt skjema"
  echo "  $0 --all                      # Migrer alle skjema"
  exit 0
fi

# Python-script for å oppdatere YAML trygt
PYTHON_SCRIPT=$(cat <<'PYTHON_EOF'
import sys
import re
from pathlib import Path

schema_file = sys.argv[1]
new_description = sys.argv[2]
new_see_also = sys.argv[3] if len(sys.argv) > 3 else None

with open(schema_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Erstatt description (både einlinjes og multiline)
# Finn description-blokk (kan vere einlinjes eller multiline med >- eller >)
# Multiline-blokk sluttar når vi finn ein linje som startar med bokstav (nytt felt) eller når indenteringa sluttar
desc_pattern = r'^description:.*?(?=\n[a-z_]+:)'
desc_match = re.search(desc_pattern, content, re.MULTILINE | re.DOTALL)

if desc_match:
    old_desc = desc_match.group(0).rstrip()
    content = content.replace(old_desc, f'description: {new_description}', 1)
else:
    # Legg til description etter title
    title_pattern = r'^title:.*$'
    content = re.sub(title_pattern, lambda m: m.group(0) + f'\ndescription: {new_description}', content, count=1, flags=re.MULTILINE)

# Legg til see_also dersom den ikkje finst (toppnivå, ikkje som slot) og vi har ein URI
if new_see_also and new_see_also != "NONE":
    # Sjekk om toppnivå see_also allereie finst (^see_also: på starten av ei linje)
    if not re.search(r'^see_also:', content, re.MULTILINE):
        # Strategi: Legg til see_also etter license, men FØR annotations
        license_pattern = r'^license:.*$'
        license_match = re.search(license_pattern, content, re.MULTILINE)

        if license_match:
            # Legg til rett etter license-linja
            insert_pos = license_match.end()
            content = content[:insert_pos] + f'\nsee_also:\n  - {new_see_also}' + content[insert_pos:]
        else:
            # Dersom license manglar: legg til etter description
            desc_pattern = r'^description:.*?(?=\n[a-z_]+:)'
            desc_match = re.search(desc_pattern, content, re.MULTILINE | re.DOTALL)
            if desc_match:
                insert_pos = desc_match.end()
                content = content[:insert_pos] + f'\nsee_also:\n  - {new_see_also}' + content[insert_pos:]

with open(schema_file, 'w', encoding='utf-8') as f:
    f.write(content)
PYTHON_EOF
)

# Lagre Python-script til temp-fil
TEMP_PYTHON="/tmp/migrate-schema-metadata.py"
echo "$PYTHON_SCRIPT" > "$TEMP_PYTHON"

# Migrer kvart skjema
for schema_file in "${SCHEMAS[@]}"; do
  [[ ! -f "$schema_file" ]] && continue

  schema_name=$(basename "$(dirname "$schema_file")")

  # Hent nye verdiar
  new_desc="${DESCRIPTIONS[$schema_name]:-}"
  new_see_also="${DOC_LINKS[$schema_name]:-NONE}"

  if [[ -z "$new_desc" ]]; then
    echo "⚠️  Hoppar over $schema_name (manglar hardkoda description)"
    continue
  fi

  echo "🔧 Oppdaterer $schema_name..."
  echo "   description: $new_desc"
  [[ "$new_see_also" != "NONE" ]] && echo "   see_also: $new_see_also"

  # Køyr Python-script
  python3 "$TEMP_PYTHON" "$schema_file" "$new_desc" "$new_see_also"
done

echo "✅ Migreringa er fullført"
