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
    ["brreg-begrepskatalog"]="Begrepskatalog for Brønnøysundregistrene"
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
  DOMAIN_ORDER=("fair" "ap-no" "referanse" "ngr" "oreg" "fint" "samt" "begrepskatalog")

  # Bygg assosiativ array: domain -> liste av skjema-filer
  declare -A DOMAIN_SCHEMAS

  while IFS= read -r schema_file; do
    domain=$(echo "$schema_file" | cut -d'/' -f3)

    # Hopp over modellkatalog (handterast separat)
    [[ "$domain" == "modellkatalog" ]] && continue

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
  echo "| Artefakt | Generator | Fil | Brukstilfelle | W3C semantisk | manifest.yaml flag |"
  echo "|---|---|---|---|---|---|"

  # Hardkoda artefakt-skildringar (manuelt kurert)
  cat <<'EOF'
| Modellmetadata ihht ModellDCAT-AP-NO | [`gen-informasjonsmodell-instance`](COMMANDS.md#vedlikehald) | `metadata/<skjema>-manifest.yaml` | ModelDCAT-AP-NO metadata for publisering til Felles Datakatalog | — | — |
| JSON-LD kontekst | [`gen-jsonld-context`](COMMANDS.md#enkeltartefakter) | `<skjema>-context.jsonld` | Mapping frå JSON til RDF — brukast saman med API | ✓ | `jsonld_context` |
| SHACL shapes | [`gen-shacl`](COMMANDS.md#enkeltartefakter) | `<skjema>-shapes.ttl` | Validering av RDF-data mot skjema i triple stores | ✓ | `shacl` |
| OWL ontologi | [`gen-owl`](COMMANDS.md#enkeltartefakter) | `<skjema>-ontology.ttl` | Maskinlesbar ontologi for semantiske verktøy | ✓ | `owl` |
| RDF/Turtle skjema | [`gen-rdf`](COMMANDS.md#enkeltartefakter) | `<skjema>-schema.ttl` | Fullstendig RDF-representasjon av skjemaet | ✓ | `rdf` |
| Eksempel-RDF | [`convert-rdf`](COMMANDS.md#enkeltartefakter) | `<skjema>-eksempel.ttl` | Konkret RDF-instans for testing og dokumentasjon | ✓ | `example_rdf` |
| Python-klassar | [`gen-python`](COMMANDS.md#enkeltartefakter) | `<skjema>-model.py` | Direkte bruk i Python-applikasjonar via LinkML | — | `python` |
| JSON Schema | [`gen-jsonschema`](COMMANDS.md#enkeltartefakter) | `<skjema>-schema.json` | Validering av JSON-data i applikasjonar og RESTful integrasjon | — | `json_schema` |
| XSD-skjema | [`gen-xsd`](COMMANDS.md#enkeltartefakter) | `<skjema>-schema.xsd` | XML Schema for XML-basert integrasjon | — | `xsd` |
| Protobuf-skjema | [`gen-proto`](COMMANDS.md#enkeltartefakter) | `<skjema>-schema.proto` | gRPC og Protocol Buffers-integrasjon | — | `protobuf` |
| AsyncAPI-spec | [`gen-asyncapi`](COMMANDS.md#enkeltartefakter) | `<skjema>-asyncapi.yaml` | Asynkron meldingsutveksling (event-driven API) | — | `asyncapi` |
| OpenAPI-spec | [`gen-openapi`](COMMANDS.md#enkeltartefakter) | `<skjema>-openapi.yaml` | RESTful API-dokumentasjon (OpenAPI 3.1) | — | `openapi` |
| ER-diagram | [`gen-erdiagram`](COMMANDS.md#enkeltartefakter) | `<skjema>-erdiagram.md` | Visuell oversikt over klasser og relasjonar (Mermaid) | — | `erdiagram` |
| Klasse-diagram | [`gen-plantuml`](COMMANDS.md#enkeltartefakter) | `diagrams/<skjema>.puml` + `.svg` | Klassediagram for presentasjon og dokumentasjon (PlantUML) | — | `plantuml` |
| HTML-dokumentasjon | [`gen-docs`](COMMANDS.md#enkeltartefakter) | `docs/` | Menneskelesleg referansedokumentasjon basert på markdown | — | `docs` |
| DQV-målingar | [`gen-dqv-measurements`](COMMANDS.md#enkeltartefakter) | `dqv-measurements.ttl` | Datakvalitetsmålingar (kun datakatalog-modellar) | ✓ | — |
| ModelDCAT-element | [`gen-modelldcat-elements`](COMMANDS.md#enkeltartefakter) | `modelldcat-elements.ttl` | Modellkatalog-element (kun modellkatalog-modellar) | ✓ | — |
EOF
}

# --- Funksjon: Generer modellkatalog-tabell ---
generate_modellkatalog_table() {
  echo "| Modellkatalog | Organisasjon | Skildring | Generator |"
  echo "|---|---|---|---|"

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

    # Konverter src/linkml/modellkatalog/<katalog>/ til modellkatalog/<katalog>/ for GitHub Pages
    ghpages_link="${schema_dir#src/linkml/}"

    echo "| [$schema_name]($ghpages_link/) | $org | Modellkatalog for $org sine informasjonsmodellar | [\`gen-modellkatalog-instance\`](COMMANDS.md#vedlikehald) |"
  done < <(find src/linkml/modellkatalog -name "*-schema.yaml" -type f | sort)
}

# --- Hovudlogikk: Bygg ny README med auto-genererte seksjoner ---

IN_DOMAIN_TABLE=false
IN_SCHEMA_TABLE=false
IN_ARTIFACTS_TABLE=false
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
