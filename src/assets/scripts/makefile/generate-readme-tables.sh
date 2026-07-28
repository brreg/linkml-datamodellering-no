#!/usr/bin/env bash
# Genererer domene-tabell, skjema-tabell og modellkatalog-tabell for README.md
# Køyr: ./scripts/generate-readme-tables.sh [README-fil]
# Output: Oppdatert README-fil med auto-genererte tabellar

set -euo pipefail

README="${1:-README.md}"

if [[ ! -f "$README" ]]; then
  echo "❌ Feil: $README finst ikkje"
  exit 1
fi

echo "🔧 Genererer auto-genererte tabellar for $README..."

# Opprett temp-fil
TEMP_README=$(mktemp)

# --- Funksjon: Generer domene-tabell ---
generate_domain_table() {
  echo "| Domene | Skildring | Dokumentasjon |"
  echo "|---|---|---|"

  # Hardkoda domene-skildringar (manuelt kurert)
  # Domenenamn lenker til <domain>/ for GitHub Pages-kompatibilitet
  cat <<'EOF'
| [fair](fair/) | **FAIR**-metadataoverbygning — **F**indable, **A**ccessible, **I**nteroperable, **R**eusable. Kan importerast av alle domenemodeller. | [FAIR principles](https://www.go-fair.org/fair-principles/)
| [ap-no](ap-no/) | Norske W3C-applikasjonsprofiler — DCAT, SKOS, CPSV, DQV m.fl. Importerast av domenemodeller. | [RDF-baserte maskinlesbare ressurser](https://data.norge.no/showroom/overview)
| [referanse](referanse/) | Enkle eksempel på gyldige LinkML-modellar (referanseimplementasjonar) |
| [ngr](ngr/) | Nasjonale grunndata — adresse, eigedom, person og verksemd. | [Nasjonale grunndata](https://informasjonsforvaltning.github.io/nasjonale-grunndata/#OmNasjonaleGrunndata)
| [oreg](oreg/) | Offentlege register. |
| [fint](fint/) | FINT felleskomponent — integrasjonsmodellar for fylkeskommunal sektor. | [FINT informasjonsmodell](https://informasjonsmodell.felleskomponent.no/docs?v=v4.0.20)
| [samt](samt/) | SAMT — integrasjonsmodellar for kommunesektoren. | [SAMT-prosjektet](https://docs.samt-bu.no/om/)
| [begrepskatalog](begrepskatalog/) | Begrepskatalog etter SKOS-AP-NO-Begrep. Instansdatafiler vert automatisk konverterte til SKOS/RDF for publisering til Felles Begrepskatalog. | [SKOS-AP-NO-Begrep](https://data.norge.no/specification/skos-ap-no-begrep)
| [modellkatalog](modellkatalog/) | Modellkatalog for informasjonsmodellar etter ModelDCAT-AP-NO for publisering til Felles Datakatalog. | [ModelDCAT-AP-NO](https://data.norge.no/specification/modelldcat-ap-no)
EOF
}

# --- Funksjon: Generer skjema-tabell ---
generate_schema_table() {
  echo "| Domene | Skjema | Skildring | Dokumentasjon"
  echo "|---|---|---|---|"

  # Hardkoda skildringar for spesielle skjema
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

  # Hardkoda dokumentasjonslenkjer
  declare -A DOC_LINKS=(
    ["fair-metadata"]="[www.go-fair.org/fair-principles/](https://www.go-fair.org/fair-principles/)"
    ["cpsv-ap-no"]="[data.norge.no/specification/cpsv-ap-no](https://data.norge.no/specification/cpsv-ap-no)"
    ["dcat-ap-no"]="[data.norge.no/specification/dcat-ap-no](https://data.norge.no/specification/dcat-ap-no)"
    ["dqv-ap-no"]="[data.norge.no/specification/dqv-ap-no](https://data.norge.no/specification/dqv-ap-no)"
    ["modelldcat-ap-no"]="[data.norge.no/specification/modelldcat-ap-no](https://data.norge.no/specification/modelldcat-ap-no)"
    ["skos-ap-no"]="[data.norge.no/specification/skos-ap-no-begrep](https://data.norge.no/specification/skos-ap-no-begrep)"
    ["xkos-ap-no"]="[data.norge.no/specification/xkos-ap-no](https://data.norge.no/specification/xkos-ap-no)"
    ["fint-administrasjon"]="[informasjonsmodell.felleskomponent.no/docs/package_administrasjon?v=v4.0.20](https://informasjonsmodell.felleskomponent.no/docs/package_administrasjon?v=v4.0.20)"
    ["fint-arkiv"]="[informasjonsmodell.felleskomponent.no/docs/package_arkiv?v=v4.0.20](https://informasjonsmodell.felleskomponent.no/docs/package_arkiv?v=v4.0.20)"
    ["fint-okonomi"]="[informasjonsmodell.felleskomponent.no/docs/package_okonomi?v=v4.0.20](https://informasjonsmodell.felleskomponent.no/docs/package_okonomi?v=v4.0.20)"
    ["fint-personvern"]="[informasjonsmodell.felleskomponent.no/docs/package_personvern?v=v4.0.20](https://informasjonsmodell.felleskomponent.no/docs/package_personvern?v=v4.0.20)"
    ["fint-ressurs"]="[informasjonsmodell.felleskomponent.no/docs/package_ressurs?v=v4.0.20](https://informasjonsmodell.felleskomponent.no/docs/package_ressurs?v=v4.0.20)"
    ["fint-utdanning"]="[informasjonsmodell.felleskomponent.no/docs/package_utdanning?v=v4.0.20](https://informasjonsmodell.felleskomponent.no/docs/package_utdanning?v=v4.0.20)"
    ["ngr-adresse"]="[informasjonsforvaltning.github.io/nasjonale-grunndata/#Adresse](https://informasjonsforvaltning.github.io/nasjonale-grunndata/#Adresse)"
    ["ngr-eiendom"]="[informasjonsforvaltning.github.io/nasjonale-grunndata/#Temaomr%C3%A5deEiendom](https://informasjonsforvaltning.github.io/nasjonale-grunndata/#Temaomr%C3%A5deEiendom)"
    ["ngr-person"]="[informasjonsforvaltning.github.io/nasjonale-grunndata/#Person](https://informasjonsforvaltning.github.io/nasjonale-grunndata/#Person)"
    ["ngr-virksomhet"]="[informasjonsforvaltning.github.io/nasjonale-grunndata/#Virksomhet](https://informasjonsforvaltning.github.io/nasjonale-grunndata/#Virksomhet)"
    ["samt-bu"]="[docs.samt-bu.no/om/](https://docs.samt-bu.no/om/)"
  )

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

      # Hent skildring
      description="${DESCRIPTIONS[$schema_name]:-}"

      # Hent dokumentasjonslenkje
      doc_link="${DOC_LINKS[$schema_name]:-}"

      # Konverter src/linkml/<domain>/<modell>/ til <domain>/<modell>/ for GitHub Pages
      ghpages_schema_link="${schema_dir#src/linkml/}"

      echo "| [$domain]($domain/) | [$schema_name]($ghpages_schema_link/) | $description | $doc_link"
    done <<< "${DOMAIN_SCHEMAS[$domain]}"
  done
}

# --- Funksjon: Generer artefakt-tabell ---
generate_artifacts_table() {
  echo "| Artefakt | Fil | Brukstilfelle | W3C semantisk | manifest.yaml flag | Generator |"
  echo "|---|---|---|---|---|---|"

  # Hardkoda artefakt-skildringar (manuelt kurert)
  cat <<'EOF'
| Modellmetadata ihht ModellDCAT-AP-NO | `metadata/<skjema>-manifest.yaml` | ModelDCAT-AP-NO metadata for publisering til Felles Datakatalog | — | — | [`gen-informasjonsmodell-instance`](COMMANDS.md#vedlikehald) |
| JSON-LD kontekst | `<skjema>-context.jsonld` | Mapping frå JSON til RDF — brukast saman med API | ✓ | `jsonld_context` | [`gen-jsonld-context`](COMMANDS.md#enkeltartefakter) |
| SHACL shapes | `<skjema>-shapes.ttl` | Validering av RDF-data mot skjema i triple stores | ✓ | `shacl` | [`gen-shacl`](COMMANDS.md#enkeltartefakter) |
| OWL ontologi | `<skjema>-ontology.ttl` | Maskinlesbar ontologi for semantiske verktøy | ✓ | `owl` | [`gen-owl`](COMMANDS.md#enkeltartefakter) |
| RDF/Turtle skjema | `<skjema>-schema.ttl` | Fullstendig RDF-representasjon av skjemaet | ✓ | `rdf` | [`gen-rdf`](COMMANDS.md#enkeltartefakter) |
| Eksempel-RDF | `<skjema>-eksempel.ttl` | Konkret RDF-instans for testing og dokumentasjon | ✓ | `example_rdf` | [`convert-rdf`](COMMANDS.md#enkeltartefakter) |
| Python-klassar | `<skjema>-model.py` | Direkte bruk i Python-applikasjonar via LinkML | — | `python` | [`gen-python`](COMMANDS.md#enkeltartefakter) |
| JSON Schema | `<skjema>-schema.json` | Validering av JSON-data i applikasjonar og RESTful integrasjon | — | `json_schema` | [`gen-jsonschema`](COMMANDS.md#enkeltartefakter) |
| XSD-skjema | `<skjema>-schema.xsd` | XML Schema for XML-basert integrasjon | — | `xsd` | [`gen-xsd`](COMMANDS.md#enkeltartefakter) |
| Protobuf-skjema | `<skjema>-schema.proto` | gRPC og Protocol Buffers-integrasjon | — | `protobuf` | [`gen-proto`](COMMANDS.md#enkeltartefakter) |
| AsyncAPI-spec | `<skjema>-asyncapi.yaml` | Asynkron meldingsutveksling (event-driven API) | — | `asyncapi` | [`gen-asyncapi`](COMMANDS.md#enkeltartefakter) |
| OpenAPI-spec | `<skjema>-openapi.yaml` | RESTful API-dokumentasjon (OpenAPI 3.1) | — | `openapi` | [`gen-openapi`](COMMANDS.md#enkeltartefakter) |
| ER-diagram | `<skjema>-erdiagram.md` | Visuell oversikt over klasser og relasjonar (Mermaid) | — | `erdiagram` | [`gen-erdiagram`](COMMANDS.md#enkeltartefakter) |
| Klasse-diagram | `diagrams/<skjema>.puml` + `.svg` | Klassediagram for presentasjon og dokumentasjon (PlantUML) | — | `plantuml` | [`gen-plantuml`](COMMANDS.md#enkeltartefakter) |
| HTML-dokumentasjon | `docs/` | Menneskelesleg referansedokumentasjon basert på markdown | — | `docs` | [`gen-docs`](COMMANDS.md#enkeltartefakter) |
| DQV-målingar | `dqv-measurements.ttl` | Datakvalitetsmålingar (kun datakatalog-modellar) | ✓ | — | [`gen-dqv-measurements`](COMMANDS.md#enkeltartefakter) |
| ModelDCAT-element | `modelldcat-elements.ttl` | Modellkatalog-element (kun modellkatalog-modellar) | ✓ | — | [`gen-modelldcat-elements`](COMMANDS.md#enkeltartefakter) |
EOF
}

# --- Funksjon: Generer begrepskatalog-tabell ---
generate_begrepskatalog_table() {
  echo "| Domene | Begrepskatalog | Organisasjon | Skildring | Generator |"
  echo "|---|---|---|---|---|"

  # Hardkoda organisasjonsnamn og skildringar
  declare -A ORGS=(
    ["brreg-begrepskatalog"]="Brønnøysundregistra"
  )

  # Finn alle begrepskatalogar
  while IFS= read -r schema_file; do
    schema_dir=$(dirname "$schema_file")
    schema_name=$(basename "$schema_dir")

    org="${ORGS[$schema_name]:-Ukjend}"

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

  # Hardkoda organisasjonsnamn og skildringar
  declare -A ORGS=(
    ["brreg-modellkatalog"]="Brønnøysundregistra"
    ["digdir-modellkatalog"]="Digitaliseringsdirektoratet"
    ["kartverket-modellkatalog"]="Kartverket"
    ["ksdigital-modellkatalog"]="KS Digital"
    ["novari-modellkatalog"]="Novari"
    ["skatteetaten-modellkatalog"]="Skatteetaten"
  )

  # Finn alle modellkatalogar
  while IFS= read -r schema_file; do
    schema_dir=$(dirname "$schema_file")
    schema_name=$(basename "$schema_dir")

    org="${ORGS[$schema_name]:-Ukjend}"

    # Lenk modellkatalog-domenet til dokumentasjonsportalen
    domain_link="https://brreg.github.io/linkml-datamodellering-no/modellkatalog/"

    # Konverter src/linkml/modellkatalog/<katalog>/ til modellkatalog/<katalog>/ for GitHub Pages
    ghpages_link="${schema_dir#src/linkml/}"

    echo "| [modellkatalog]($domain_link) | [$schema_name]($ghpages_link/) | $org | Modellkatalog for $org sine informasjonsmodellar | [\`gen-modellkatalog-instance\`](COMMANDS.md#vedlikehald) |"
  done < <(find src/linkml/modellkatalog -name "*-schema.yaml" -type f | sort)
}

# --- Hovudlogikk: Bygg ny README med auto-genererte seksjoner ---

IN_DOMAIN_TABLE=false
IN_SCHEMA_TABLE=false
IN_ARTIFACTS_TABLE=false
IN_BEGREPSKATALOG_TABLE=false
IN_MODELLKATALOG_TABLE=false

while IFS= read -r line; do
  # Domene-tabell
  if [[ "$line" == "<!-- BEGIN AUTO-GENERATED: DOMAIN TABLE -->" ]]; then
    IN_DOMAIN_TABLE=true
    echo "$line" >> "$TEMP_README"
    generate_domain_table >> "$TEMP_README"
    continue
  elif [[ "$line" == "<!-- END AUTO-GENERATED: DOMAIN TABLE -->" ]]; then
    IN_DOMAIN_TABLE=false
    echo "$line" >> "$TEMP_README"
    continue
  elif $IN_DOMAIN_TABLE; then
    continue  # Hopp over eksisterande innhald
  fi

  # Skjema-tabell
  if [[ "$line" == "<!-- BEGIN AUTO-GENERATED: SCHEMA TABLE -->" ]]; then
    IN_SCHEMA_TABLE=true
    echo "$line" >> "$TEMP_README"
    generate_schema_table >> "$TEMP_README"
    continue
  elif [[ "$line" == "<!-- END AUTO-GENERATED: SCHEMA TABLE -->" ]]; then
    IN_SCHEMA_TABLE=false
    echo "$line" >> "$TEMP_README"
    continue
  elif $IN_SCHEMA_TABLE; then
    continue  # Hopp over eksisterande innhald
  fi

  # Artefakt-tabell
  if [[ "$line" == "<!-- BEGIN AUTO-GENERATED: ARTIFACTS TABLE -->" ]]; then
    IN_ARTIFACTS_TABLE=true
    echo "$line" >> "$TEMP_README"
    generate_artifacts_table >> "$TEMP_README"
    continue
  elif [[ "$line" == "<!-- END AUTO-GENERATED: ARTIFACTS TABLE -->" ]]; then
    IN_ARTIFACTS_TABLE=false
    echo "$line" >> "$TEMP_README"
    continue
  elif $IN_ARTIFACTS_TABLE; then
    continue  # Hopp over eksisterande innhald
  fi

  # Begrepskatalog-tabell
  if [[ "$line" == "<!-- BEGIN AUTO-GENERATED: BEGREPSKATALOG TABLE -->" ]]; then
    IN_BEGREPSKATALOG_TABLE=true
    echo "$line" >> "$TEMP_README"
    generate_begrepskatalog_table >> "$TEMP_README"
    continue
  elif [[ "$line" == "<!-- END AUTO-GENERATED: BEGREPSKATALOG TABLE -->" ]]; then
    IN_BEGREPSKATALOG_TABLE=false
    echo "$line" >> "$TEMP_README"
    continue
  elif $IN_BEGREPSKATALOG_TABLE; then
    continue  # Hopp over eksisterande innhald
  fi

  # Modellkatalog-tabell
  if [[ "$line" == "<!-- BEGIN AUTO-GENERATED: MODELLKATALOG TABLE -->" ]]; then
    IN_MODELLKATALOG_TABLE=true
    echo "$line" >> "$TEMP_README"
    generate_modellkatalog_table >> "$TEMP_README"
    continue
  elif [[ "$line" == "<!-- END AUTO-GENERATED: MODELLKATALOG TABLE -->" ]]; then
    IN_MODELLKATALOG_TABLE=false
    echo "$line" >> "$TEMP_README"
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
