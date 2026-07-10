# Legg til "Generator"-kolonne i README-tabellane

## Bakgrunn

README.md har to hovudtabellar som dokumenterer genererte artefakter:
1. **Genererte artefakter** — oversikt over alle artefaktformat som kan genererast frå LinkML-skjema
2. **Genererte modellkatalogar** — oversikt over organisasjonskatalogane

COMMANDS.md inneheld detaljert dokumentasjon av kvar einskild generator (`make gen-jsonld-context`, `make gen-shacl` osv.).

Det finst ikkje nokon direkte lenking mellom README-tabellane og COMMANDS.md-dokumentasjonen. Brukarar må manuelt søkje opp riktig generator-kommando i COMMANDS.md.

## Mål

Leggje til ei "Generator"-kolonne i begge tabellane som lenker til den einskilde generatoren sin dokumentasjon i COMMANDS.md.

## Steg

1. **Les gjeldande struktur**
   - README.md tabellane (Genererte artefakter, Genererte modellkatalogar)
   - COMMANDS.md generatorseksjonar

2. **Map artefakt → generator**
   - Identifiser riktig `make gen-*` kommando for kvar artefakt
   - Map modellkatalog-generering til `make gen-modellkatalog-instance`
   - Modellmetadata (`metadata/<skjema>-manifest.yaml`) mappar til `make gen-informasjonsmodell-instance`

3. **Oppdater "Genererte artefakter"-tabellen**
   - Legg til ny kolonne "Generator" som kolonne 2 (etter "Artefakt", før "Fil")
   - Kvar rad får markdown-lenke til `COMMANDS.md#<generator-anchor>`
   - Rekkjefølgje: `| Artefakt | Generator | Fil | Brukstilfelle | W3C semantisk | manifest.yaml flag |`

4. **Oppdater "Genererte modellkatalogar"-tabellen**
   - Legg til ny kolonne "Generator" som siste kolonne
   - Rekkjefølgje: `| Modellkatalog | Organisasjon | Skildring | Generator |`
   - Alle radene får same lenke: `[`make gen-modellkatalog-instance`](COMMANDS.md#vedlikehald)`

5. **Verifiser lenkar**
   - Sjekk at alle anker-referansar peikar til eksisterande seksjonsheadings i COMMANDS.md
   - COMMANDS.md-anker generert automatisk: lowercase, mellomrom → bindestreke, `:` fjerna

## Mapping artefakt → generator

| Artefakt | `make`-kommando | COMMANDS.md-anker |
|---|---|---|
| Modellmetadata ihht ModellDCAT-AP-NO | `make gen-informasjonsmodell-instance` | `#vedlikehald` |
| JSON-LD kontekst | `make gen-jsonld-context` | `#enkeltartefakter` |
| SHACL shapes | `make gen-shacl` | `#enkeltartefakter` |
| OWL ontologi | `make gen-owl` | `#enkeltartefakter` |
| RDF/Turtle skjema | `make gen-rdf` | `#enkeltartefakter` |
| Eksempel-RDF | `make convert-rdf` | `#enkeltartefakter` |
| Python-klassar | `make gen-python` | `#enkeltartefakter` |
| JSON Schema | `make gen-jsonschema` | `#enkeltartefakter` |
| XSD-skjema | `make gen-xsd` | `#enkeltartefakter` |
| Protobuf-skjema | `make gen-proto` | `#enkeltartefakter` |
| AsyncAPI-spec | `make gen-asyncapi` | `#enkeltartefakter` |
| OpenAPI-spec | `make gen-openapi` | `#enkeltartefakter` |
| ER-diagram | `make gen-erdiagram` | `#enkeltartefakter` |
| Klasse-diagram | `make gen-plantuml` | `#enkeltartefakter` |
| HTML-dokumentasjon | `make gen-docs` | `#enkeltartefakter` |
| DQV-målingar | `make gen-dqv-measurements` | `#enkeltartefakter` |
| ModelDCAT-element | `make gen-modelldcat-elements` | `#enkeltartefakter` |

## Handlingsliste

- [x] Les README.md sin "Genererte artefakter"-tabell
- [x] Oppdater "Genererte artefakter"-tabellen med ny "Generator"-kolonne
- [x] Oppdater "Genererte modellkatalogar"-tabellen med ny "Generator"-kolonne
- [x] Verifiser at lenkar mappar korrekt til COMMANDS.md
- [x] Generer commit-melding

## Utført

Begge tabellane i README.md er no oppdaterte med "Generator"-kolonne:

**Genererte artefakter:**
- Ny kolonne "Generator" som kolonne 2 (mellom "Artefakt" og "Fil")
- Kvar rad lenker til riktig generator i COMMANDS.md
- 17 radene med korrekt mapping til `#enkeltartefakter` eller `#vedlikehald`

**Genererte modellkatalogar:**
- Ny kolonne "Generator" som siste kolonne
- Alle 6 radene lenker til `gen-modellkatalog-instance` i COMMANDS.md

**src/assets/scripts/generate-readme-tables.sh:**
- `generate_artifacts_table()` ny funksjon for å generere "Genererte artefakter"-tabellen
- `generate_modellkatalog_table()` oppdatert med ny "Generator"-kolonne
- Genererer lenkjer til `COMMANDS.md#enkeltartefakter` og `COMMANDS.md#vedlikehald`
- Hovudlogikk oppdatert med `IN_ARTIFACTS_TABLE` og handtering av `<!-- AUTO-GENERATED: ARTIFACTS TABLE -->`

**README.md:**
- Lagt til `<!-- BEGIN/END AUTO-GENERATED: ARTIFACTS TABLE -->` markørar rundt artefakt-tabellen
- Tabellen kan no regenererast med scriptet

Alle anker-referansar (`#enkeltartefakter`, `#vedlikehald`) mappar korrekt til eksisterande seksjonsheadings i COMMANDS.md.
