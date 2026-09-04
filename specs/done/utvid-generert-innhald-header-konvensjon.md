# Utvid header/felt-konvensjon for generert innhald

## Bakgrunn

Brukaren opplever at LLM-en av og til ikkje har oversikt over kva innhald
som er generert (kopiert frå andre filer eller produsert av script) versus
hand-forfatta. Vurdert som eiga rule/skill, men forkasta til fordel for å
gjere proveniens ein del av **sjølve fila** — synleg uansett kva fil som
vert opna, uavhengig av om noka rule er lasta. Brukaren valde denne
tilnærminga eksplisitt ("gå for header/felt-konvensjonen").

Eiga gransking av repoet avdekte at ein slik konvensjon **delvis alt
finst**, men er brukt inkonsekvent:

- **Fullt generert YAML** — `utils/yaml_io.py::write_yaml()` skriv alt ein
  `# Generert av CI frå <script> — ikkje rediger manuelt`-header. Brukt av
  `generate-informasjonsmodell.py` (→ `metadata/*-manifest.yaml`) og
  `collect-concepts.py` (→ begrepskatalog-aggregering). **Ingen endring
  nødvendig her.**
- **Hybrid `schema.yaml`** (dato/versjon/policy vert script-oppdatert, resten
  er hand-forfatta) — `add-schema-header-comments.py` set alt inn ein
  forklarande header ("version, endringsdato og utgivelsesdato vert
  automatisk oppdatert av CI"). **Ingen endring nødvendig her.**
- **Gap 1 — `validation/<version>/<policy>.json`:** heilt generert av
  `utils/validation_log.py::write_validation_log()` (brukt av
  `save-validation-log.py` og `run-validation.sh`), men ingen
  proveniens-felt i det heile — JSON kan ikkje ha kommentarar.
- **Gap 2 — `src/linkml/modellkatalog/<org>/data/<org>/<org>.yaml`:**
  skriven av **to ulike script** (`update-modellkatalog.py`,
  `gen-modelldcat-elements.py`) med rein `yaml.dump()` — ingen av dei brukar
  `write_yaml()` eller nokon header. Fila er **hybrid**:
  `update-modellkatalog.py` legg sjølv til stub-oppføringar som "treng
  manuell utfylling av TODO-felt" — ein blank "ikkje rediger
  manuelt"-header ville difor vore misvisande.
- **Gap 3 — `kvalitetsmaalingar:`-blokka** i produksjonsdatafiler
  (`src/linkml/<domain>/<modell>/data/<katalog>/<katalog>.yaml`), sett inn
  av `gen-dqv-measurements.py::process_datafile()` via målretta
  tekstinnsetting (ikkje full YAML-dump): ingen markør skil den
  script-vedlikehaldne blokka frå resten av den hand-kuraterte
  produksjonsdatafila.

## Steg

1. `utils/validation_log.py::write_validation_log()` — legg til eit
   `"_generated_by"`-felt i JSON-objektet (peikar til `validation_log.py`
   og dei to kallande skripta).
2. `update-modellkatalog.py` og `gen-modelldcat-elements.py` — legg til ein
   kort, hybrid-forklarande header (to linjer, same stil som
   `add-schema-header-comments.py`) rett før `yaml.dump()`-kallet i kvar av
   dei to skripta.
3. `gen-dqv-measurements.py::process_datafile()` — legg til ei
   kommentarlinje rett over `kvalitetsmaalingar:`-blokka når han vert sett
   inn/oppdatert.
4. Verifiser at ingen eksisterande forbrukar (`generate-validation-md.py`,
   `linkml validate`) feilar av dei nye felta/kommentarane.

## Prioritert handlingsliste

| # | Steg | Fil | Merknad |
|---|---|---|---|
| 1 | `_generated_by`-felt i valideringslogg-JSON | `src/assets/scripts/utils/validation_log.py` | |
| 2 | Hybrid-header i modellkatalog-skrivarar | `src/assets/scripts/makefile/update-modellkatalog.py`, `.../gen-modelldcat-elements.py` | To skrivepunkt, same header-tekst |
| 3 | Kommentarlinje over `kvalitetsmaalingar:`-blokk | `src/assets/scripts/makefile/gen-dqv-measurements.py` | |
| 4 | Verifiser ingen brot hos forbrukarar | — | `make lint`/relevant validering |

## Avgjerder

- **Konsoliderte ikkje `update-modellkatalog.py` og
  `gen-modelldcat-elements.py` sine skrivepunkt til éin delt writer**, sjølv
  om dei skriv same filtype med duplisert `yaml.dump()`-logikk (parallelt
  mønster til BUG-16). Grunngjeving: CLAUDE.md krev eksplisitt
  brukargodkjenning for DRY-konsolidering av fungerande kode, og det er
  utanfor denne specen sitt avgrensa mål (proveniens-markering, ikkje
  refaktorering). Header lagt til separat på begge skrivepunkt i staden.
- **Brukte IKKJE `write_yaml()`** (som gir ein blank "ikkje rediger
  manuelt"-header) for modellkatalog-fila. Grunngjeving:
  `update-modellkatalog.py` sitt eige loggoutput seier at nye
  stub-oppføringar "treng manuell utfylling av TODO-felt" — ein "ikkje
  rediger"-header ville motsagt denne dokumenterte arbeidsflyten. Skreiv i
  staden ein eigen, hybrid-forklarande header, same mønster som
  `add-schema-header-comments.py` alt brukar for `schema.yaml`.
- **JSON-feltnamn valt til `_generated_by`** (understrek-prefiks).
  Grunngjeving: signaliserer eit metadata-/ikkje-forretningsfelt, og
  `generate-validation-md.py` (einaste kjende forbrukar) itererer ikkje
  strengt over nøklar — trygt å leggje til utan å bryte eksisterande
  parsing.
- **`gen-dqv-measurements.py` sin tekstinnsettingslogikk kravde ei
  idempotens-retting utover det opphavleg planlagde steget.** Ei naiv
  "prepend kommentar før `kvalitetsmaalingar:`"-implementering ville
  duplisert markøren for kvar køyring, sidan `find_top_level_block()` sin
  regex berre matchar sjølve nøkkellinja, ikkje ei føregåande
  kommentarlinje. Løyst ved å utvide blokkgrensa bakover forbi ein
  eksisterande `DQV_MARKER` før erstatting. Verifisert med ein
  to-køyrings-simulering (`ast.parse` + manuell `find_top_level_block`-test)
  — ingen duplisering.

## Utført

- `src/assets/scripts/utils/validation_log.py`: `"_generated_by"`-felt lagt
  til i `build_validation_log_entry()`.
- `src/assets/scripts/makefile/gen-dqv-measurements.py`: `DQV_MARKER`-konstant
  innført, sett inn idempotent over `kvalitetsmaalingar:`-blokka.
- `src/assets/scripts/makefile/update-modellkatalog.py`,
  `.../gen-modelldcat-elements.py`: hybrid-forklarande header lagt til før
  `yaml.dump()`.
- Verifisert: alle fire filer `ast.parse`-ar korrekt (syntaks OK), og
  DQV-markør-logikken er idempotent over to simulerte køyringar.
