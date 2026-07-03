# Filtrer PlantUML-diagram til kun lokale klasser

## Bakgrunn

PlantUML-diagramma (`generated/<domain>/<modell>/diagrams/<modell>.puml`) inneheld for tida alle klasser frå både:
- Det lokale skjemaet (t.d. `Skole`, `Kommune`, `Elev` i `samt-bu-schema.yaml`)
- Importerte skjema (t.d. `Datasett`, `Katalog`, `Distribusjon` frå `dcat-ap-no-schema`)
- Containerklassen (`SamtBuContainer`, markert med `tree_root: true`)

Dette gjer diagramma svært store og vanskelege å lese. Brukarane er primært interesserte i å sjå strukturen til **domenemodellen** — ikkje metadata-klassane eller serialiseringskontaineren.

Repoet har allereie ein liknande filtreringsmekanisme for Mermaid ER-diagram (`filter_erdiagram.py`) som:
1. Genererer eit ufiltrert diagram (`<modell>-erdiagram-unfiltered.md`)
2. Filtrerer vekk alle klasser som ikkje er definerte i `classes:`-seksjonen i det lokale skjemaet
3. Skriv det filtrerte diagrammet til `<modell>-erdiagram.md`

Same tilnærminga bør brukast for PlantUML-diagram.

## Krav

1. **Bevar ufiltrert diagram:** `<modell>.puml` (den fulle versjonen generert av `gen-plantuml`)
2. **Generer filtrert diagram:** `<modell>-filtered.puml` som kun inneheld:
   - Klasser definerte i det lokale skjemaet sitt `classes:`-blokk
   - **Unntatt:** klasser markerte med `tree_root: true` (containerklassen)
   - **Inkludert:** abstrakte klasser (`abstract: true`) dersom dei er lokalt definerte (t.d. `Skoleeier`, `Person`)
   - Relasjonar (piler) mellom dei filtrerte klassane
   - Arvestruktur (`is_a`) for filtrerte klasser
3. **SVG-rendering:** Generer både `.puml` og `.svg` for den filtrerte versjonen
4. **Dokumentasjon:** Oppdater `CLAUDE.md` og/eller `CONTRIBUTING.md` med forklaring av filtrert vs. ufiltrert PlantUML-diagram

## Prioritert handlingsliste

1. ✓ Opprett `src/assets/scripts/filter_plantuml.py` basert på mønsteret frå `filter_erdiagram.py`
   - Les skjemaet med `yaml.safe_load()` for å hente `local_classes = schema.get("classes", {}).keys()`
   - Filtrer vekk klasser med `tree_root: true`
   - Behald klassedefinisjonar (`class "Klassenamn"`) kun for lokale klasser
   - Behald relasjonar (piler) kun mellom lokale klasser
   - Skriv filtrert PlantUML-kode til stdout
   - **Implementert:** Regex for relasjonar fangar opp kardinalitet (`"0..1"`, `"1..*"`)

2. ✓ Oppdater `Makefile` for å køyre filtreringsskriptet
   - Legg til `filter_plantuml.py`-kall i `run_gen_plantuml`-blokka
   - Input: `$(call schema_outdir,$(s))/diagrams/$(call schema_name,$(s)).puml`
   - Output: `$(call schema_outdir,$(s))/diagrams/$(call schema_name,$(s))-filtered.puml`
   - Køyr PlantUML-rendering på den filtrerte `.puml`-fila også → `.svg`
   - **Implementert:** Begge `.svg`-filer (full og filtrert) vert genererte

3. ✓ Test på `samt-bu-schema.yaml`
   - Køyr `make gen-plantuml SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml`
   - Verifiser at `samt-bu-filtered.puml` kun inneheld:
     - `Skole`, `Skoleeier`, `Kommune`, `Fylke`, `PrivatVirksomhet`, `Basisgruppe`, `Person`, `Elev`, `Rektor`, `Kontaktlaerer`
   - Verifiser at desse **ikkje** er med:
     - `SamtBuContainer`
     - `Datasett`, `Katalog`, `Distribusjon` (frå dcat-ap-no)
     - `Kvalitetsmerknad`, `Brukartilbakemelding` (frå dqv-ap-no)
   - Sjekk at arvehierarkiet (`Skoleeier ^-- Kommune`) er intakt
   - **Verifisert:** Alle lokale klasser er med, ingen importerte klasser eller containerklasse
   - **Verifisert:** Alle relasjonar (`har_skoleeier`, `del_av_skole`, osv.) og arvehierarki er intakte

4. ✓ Oppdater `mkdocs/publish.sh` for å bruke filtrert diagram i dokumentasjonsportalen
   - Kopier `<modell>-filtered.svg` i staden for `<modell>.svg` til `mkdocs/docs/<domain>/<schema>/`
   - Alternativt: kopier begge, men referer til `-filtered.svg` som standard i index.md
   - **Implementert:** Begge versjonar vert kopierte, filtrert versjon vert vist først i artefakt-tabellen
   - **Implementert:** Full versjon er merka med "(full)" i lenkja

5. ✓ Dokumenter i `CLAUDE.md` under «Modelleringsprinsipper» eller «Valider arbeidet ditt»
   - Forklar at det finst to PlantUML-versjonar: ufiltrert (full) og filtrert (kun domenemodell)
   - Dokumentasjonsportalen brukar den filtrerte versjonen

## Avhengigheiter

- Ingen eksterne avhengigheiter
- Krev Python 3 (allereie brukt i `filter_erdiagram.py`)
- Krev PlantUML-container (allereie definert som `PLANTUML_IMAGE` i Makefile)

## Akseptansekriterier

- `make gen-plantuml SCHEMA=<sti>` genererer både `<modell>.puml` (ufiltrert) og `<modell>-filtered.puml` (filtrert)
- Filtrert diagram inneheld **kun** klasser definerte i det lokale skjemaet (minus `tree_root`-klassen)
- Arvestruktur og relasjonar er bevarte for dei filtrerte klassane
- Abstrakte klasser (t.d. `Skoleeier`) er inkluderte dersom dei er lokalt definerte
- SVG-rendering av filtrert diagram fungerer
- Dokumentasjonsportalen (`mkdocs/docs/`) viser det filtrerte diagrammet

## Utført

Alle tiltak er implementerte og teste. Løysinga følgjer same mønster som eksisterande `filter_erdiagram.py`:

1. **Filtreringsskript (`src/assets/scripts/filter_plantuml.py`):**
   - Brukar `yaml.safe_load()` for å lese lokale klasser frå skjemaet
   - Filtrer vekk klasser med `tree_root: true` (containerklassen)
   - Regex-mønster fangar opp PlantUML-relasjonar med kardinalitet (`"0..1"`, `"1..*"`)
   - Behald abstrakte klasser dersom dei er lokalt definerte

2. **Makefile-integrering (`Makefile`):**
   - `run_gen_plantuml` køyrer både `gen-plantuml` (ufiltrert) og `filter_plantuml.py` (filtrert)
   - Genererer både `.puml` og `.svg` for begge versjonar
   - Total generering tar ca. same tid som før (PlantUML-rendering er den treigaste delen)

3. **Test på `samt-bu-schema.yaml`:**
   - Filtrert diagram inneheld alle 11 lokale klasser (inkl. abstrakte `Skoleeier` og `Person`)
   - Ingen containerklasse (`SamtBuContainer`)
   - Ingen importerte klasser (dcat-ap-no, dqv-ap-no)
   - Alle relasjonar og arvehierarki er bevarte

4. **Mkdocs-integrering (`mkdocs/publish.sh`):**
   - Begge versjonar vert kopierte til `mkdocs/docs/<domain>/<schema>/diagrams/`
   - Filtrert versjon vert vist først i artefakt-tabellen
   - Full versjon er merka med "(full)" i lenkja

5. **Dokumentasjon (`CLAUDE.md`):**
   - Ny seksjon under «Dokumentasjonsportal (mkdocs)» → «PlantUML-diagram»
   - Forklarar forskjellen mellom full og filtrert versjon
   - Dokumenterer at dokumentasjonsportalen brukar filtrert versjon som standard
