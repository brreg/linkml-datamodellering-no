# Vegkart: Tilgjengeleggjering og ekstraverdi frå LinkML-modellane

Seks delar i gjennomføringsrekkefølge. Kvar del er sjølvstendig og kan leverast separat.
Dei strategiske prioriteringane bak rekkefølga er forklart i kvar overskrift.

---

## Del 1 — README med rask oppstart

**Mål:** Éin fil som gir alle nødvendige opplysningar for å kome i gang.

**Ferdig når:** Ein ny utviklar kan lese README og køyre sin første validering utan å slå opp i andre filer.

### 1.1 — Røtter og omfang
Skriv `README.md` i repo-rota med:
- Kva repoet er (éin setning)
- Føresetnadar: podman, WSL2, GNU make
- Tre eksempelkommandoar med forventa output:
  ```bash
  make mcp-validate SCHEMA=src/linkml/oreg/register-over-aksjeeiere/register-over-aksjeeiere-schema.yaml
  make linkml-gen-generate SCHEMA=/tmp/mitt-skjema.json FORMAT=json-schema
  make docs-serve
  ```
- Peik til `CLAUDE.md` for modelleringsprinsippa
- Peik til `docs/ny-domenemodell.md` for steg-for-steg-rettleiing

### 1.2 — Domene- og skjemaoversikt
Legg til seksjon i README med tabell over alle domene og kva skjema dei inneheld (auto-generert frå `src/linkml/`-struktur om mogleg).

---

## Del 2 — Rename og nytt API for mcp-linkml-generator

**Mål:** Rename `mcp-json2linkml` til `mcp-linkml-generator` og innfør eit framtidsretta
`inputFormat` + `inputContent`-API som gjer serveren klar for fleire inputformat.

**Ferdig når:** Alle eksisterande testar er grøne under nytt namn, og `generate_linkml` med
`inputFormat: "json-schema"` og `inputFormat: "empty"` fungerer.

> Denne delen er ein føresetnad for Del 3.

### 2.1 — Rename server og katalog
Rename `src/mcp-json2linkml/` → `src/mcp-linkml-generator/` og oppdater alle referansar:

| Fil | Endring |
|---|---|
| `Makefile` | `JSON2LINKML_*` → `LINKML_GEN_*`, image `mcp-json2linkml` → `mcp-linkml-generator` |
| `.mcp.json` | Nøkkel `json2linkml` → `linkml-generator`, monteringsstigar |
| `tests/test_mcp_json2linkml.py` | Rename til `test_mcp_linkml_generator.py` |
| `tests/test-mcp-json2linkml.json` | Rename til `test-mcp-linkml-generator.json` |

### 2.2 — Nytt API: `inputFormat` + `inputContent`
Erstatt `generate_linkml_from_json_schema`-verktøyet med `generate_linkml`:

| Parameter | Type | Påkravd | Default |
|---|---|---|---|
| `inputFormat` | string | ja | — |
| `inputContent` | string | nei | `""` |
| `schemaId` | string | nei | `"https://example.org/schema"` |
| `schemaName` | string | nei | `"schema"` |
| `schemaTitle` | string | nei | `""` |
| `profile` | string | nei | `"default"` |
| `validate` | boolean | nei | `true` |

Gyldige verdiar for `inputFormat` i denne delen: `"json-schema"` og `"empty"`.
`"turtle"` kjem i Del 6.

Oppdater `server.py`, `converter.py` og alle testar tilsvarande.

### 2.3 — Legg til `empty`-format
Legg til `_convert_empty(schema_name, profile) → (yaml_str, warnings)` i `converter.py`.
Returnerer eit skjema med éin stub-klasse og containerklasse, utan eigenskapar.
Brukt av scaffolding-skriptet (Del 3) og eliminerer behovet for ein statisk mal der.

---

## Del 3 — Scaffolding-kommando for ny modell

**Mål:** `make new-model NAME=<namn> DOMAIN=<domene>` oppretter riktig filstruktur og boilerplate.

**Ferdig når:** Kommandoen produserer eit gyldig skjema som passerer `make mcp-validate ... POLICY=bronze` utan manuell redigering.

> Avheng av Del 2 (rename + `empty`-format).

### 3.1 — Shell-skript for katalogoppsett
Lag `src/assets/scripts/new-model.sh` som:
- Tek `NAME` og `DOMAIN` som argument
- Oppretter `src/linkml/<domain>/<name>/`
- Oppretter `examples/<domain>/`
- Feil med tydeleg melding om katalogen allereie finst

### 3.2 — Skjema-mal via mcp-linkml-generator
Skriptet kallar `mcp-linkml-generator` med `inputFormat: "empty"` for å generere boilerplate,
og gjer deretter to justeringar:
1. Byter `schemaId` til riktig URI basert på namnekonvensjonane i repoet
   (t.d. `https://data.norge.no/<domain>/<name>`)
2. Legg til domene-spesifikk import etter `linkml:types`
   (t.d. `- dcat-ap-no` for oreg-domenet)

### 3.3 — Makefile-integrasjon
```makefile
# Bruk: make new-model NAME=<namn> DOMAIN=<domene>
new-model:
    @test -n "$(NAME)" && test -n "$(DOMAIN)" || \
      (echo "Bruk: make new-model NAME=<namn> DOMAIN=<domene>"; exit 1)
    bash src/assets/scripts/new-model.sh "$(NAME)" "$(DOMAIN)"
```

### 3.4 — Eksempelfil
Skriptet skriv òg `examples/<domain>/<name>-eksempel.yaml` med éin minimal instans som samsvarar med stub-klassen.

---

## Del 4 — CI/CD som validerer og publiserer automatisk

**Mål:** Kvar push til `main` validerer alle skjema og publiserer oppdatert dokumentasjonsportal.

**Ferdig når:** GitHub Actions køyrer grønt på `main`, og MkDocs-portalen er tilgjengeleg på GitHub Pages.

### 4.1 — Valideringsworkflow
Opprett `.github/workflows/validate.yml`:
- Triggar på push til `main` og pull requests
- Køyrer `make mcp-validate` for kvart skjema i `src/linkml/` mot bronze-policy
- Rapporterer feil som GitHub-annotasjonar på PR

### 4.2 — Artefakt-genereringsworkflow
Opprett `.github/workflows/generate.yml`:
- Triggar på push til `main`
- Køyrer `make gen-shacl gen-jsonschema gen-jsonld gen-python` for alle skjema
- Lastar opp genererte artefaktar som workflow-artefaktar (og/eller commit tilbake til `generated/`-branch)

### 4.3 — Dokumentasjonspublisering
Utvid `.github/workflows/generate.yml` med:
- `make publish` (kopier genererte docs til `mkdocs/docs/`)
- `make docs-build`
- Deploy til GitHub Pages med `actions/deploy-pages`

---

## Del 5 — Realistiske eksempeldatasett for alle modeller

**Mål:** Kvart skjema har eit gjennomarbeid, realistisk eksempel som dokumenterer bruk og fungerer som integrasjonstest.

**Ferdig når:** Alle eksempel passerer `validate_schema.bash` og gir meiningsfull RDF ved `make convert-rdf`.

### 5.1 — Inventar og gap-analyse
Køyr eit skript som listar alle skjema i `src/linkml/` og sjekkar om tilsvarande eksempel finst i `examples/`. Rapporter kva som manglar.

### 5.2 — Eksempel per manglande skjema
For kvart skjema utan eksempel:
- Bruk `mcp-linkml-generator` som utgangspunkt for å forstå strukturen
- Skriv eit eksempel med minst 2–3 instansar og realistiske (ikkje berre `dummy`) verdiar
- Verifiser med `validate_schema.bash`

### 5.3 — Eksempel som CI-testar
Legg til eit steg i `.github/workflows/validate.yml` som køyrer `validate_schema.bash` for kvart skjema/eksempel-par automatisk.

---

## Del 6 — RDF/OWL som inputformat i mcp-linkml-generator

**Mål:** Konvertere OWL/Turtle og DCAT-AP RDF/XML til LinkML-utkast.

**Ferdig når:** `generate_linkml` med `inputFormat: "turtle"` produserer eit gyldig LinkML-utkast frå ei Turtle-fil med ein DCAT-AP-klasse.

### 6.1 — RDF-konvertering
Legg til `rdflib` i `requirements.txt`.
Lag `src/mcp-linkml-generator/rdf_converter.py` med:
```python
def convert_from_rdf(rdf_content: str, rdf_format: str, profile: dict) -> tuple[str, list[str]]:
    """Konverterer RDF/OWL til LinkML-utkast. rdf_format: 'turtle'|'xml'|'json-ld'"""
```
Strategien:
- `owl:Class` → LinkML-klasse
- `owl:ObjectProperty` / `owl:DatatypeProperty` → slot med range
- `rdfs:label` → klasse- og slot-namn
- `rdfs:comment` → description
- `rdfs:domain` / `rdfs:range` → slot_usage per klasse

Legg til `TestRDFConversion` i testfila:
- Enkel OWL-klasse i Turtle → korrekt LinkML-klasse
- `owl:ObjectProperty` med domain/range → slot med riktig range

### 6.2 — Oppdater smoke-test og dokumentasjon
- Legg til `"turtle"` i lista over gyldige `inputFormat`-verdiar i `server.py`
- Legg til ein Turtle-basert testmelding i `tests/test-mcp-linkml-generator.json`
- Køyr `make linkml-gen-smoke` og `make linkml-gen-test-converter`
- Oppdater `docs/json2linkml.md` med merknad om at planen er realisert og erstatta av dette vegkartet
