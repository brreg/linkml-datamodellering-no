# Plan: Omdøyp `modelkatalog` → `modellkatalog`

## Bakgrunn

«Modelkatalog» er feil norsk — «modellkatalog» (dobbel-l) er korrekt. Endringa
gjeld domenenamnet, skjemanamnet og alle norske vocabulary-termar avleia av ordet.

---

## Nivå 1 — Domene og stiar

Reint organisatorisk. Ingen semantiske konsekvensar.

| Fil | Endring |
|---|---|
| `src/linkml/modelkatalog/` | `git mv` → `src/linkml/modellkatalog/` |
| `.github/workflows/generate.yml` | `modelkatalog` → `modellkatalog` i domain-matrise |
| `.github/workflows/validate.yml` | Same |
| `mkdocs/publish.sh` | `modelkatalog)` → `modellkatalog)` og label |
| `README.md` | Domenetabell |
| `mkdocs/docs/index.md` | Domenetabell |
| `mkdocs/docs/publisering-modell.md` | Sti-referansar (`src/linkml/modelkatalog/…`) |
| `src/mcp-linkml-validator/README.md` | Sti-eksempel |
| `specs/domenenamn-begrep-modell.md` | Tilrådingstekst |

---

## Nivå 2 — Skjemanamn

`brreg-modelkatalog` → `brreg-modellkatalog`. Inkluderer endring av schema-id URI.

Skjemaet er ikkje eksternt registrert i Felles Datakatalog enno, so URI-endringa
er utan praktiske konsekvensar.

| Fil / felt | Endring |
|---|---|
| `brreg-modelkatalog/` (katalog) | `git mv` → `brreg-modellkatalog/` |
| `brreg-modelkatalog-schema.yaml` | `git mv` → `brreg-modellkatalog-schema.yaml` |
| `brreg-modelkatalog-eksempel.yaml` | `git mv` → `brreg-modellkatalog-eksempel.yaml` |
| Schema `name:` | `brreg-modelkatalog` → `brreg-modellkatalog` |
| Schema `id:` | `https://data.norge.no/linkml/brreg-modelkatalog` → `…/brreg-modellkatalog` |
| Schema `default_prefix:` | Same |
| `published-uris.lock` | Header-kommentar |
| Alle sti-referansar til `brreg-modelkatalog` | Oppdaterast som følgje av filflyttingane |

---

## Nivå 3 — Norske vocabulary-termar

Endrar klasse- og slot-namn som er avleia av det feilstava `modelkatalog`.

⚠️ Klasse- og slotnamn i `modelldcat-ap-no-schema.yaml` vert brukt av alle
skjema som importerer profilen. Endringa krev at `brreg-modellkatalog-schema.yaml`
og eventuelle andre importerande skjema oppdaterer sine `range:`- og slot-referansar.

| Fil | Endring |
|---|---|
| `src/linkml/ap-no/modelldcat-ap-no/modelldcat-ap-no-schema.yaml` | Klasse `Modelkatalog` → `Modellkatalog` |
| Same | Slot `modelkatalogar` → `modellkatalogar` |
| Same | Fritekstbeskrivingar som inneheld «modelkatalog» → «modellkatalog» |
| `brreg-modellkatalog-schema.yaml` | `range: Modelkatalog` → `Modellkatalog` |
| Same | Attributt `modelkatalogar:` → `modellkatalogar:` |
| `src/mcp-linkml-validator/policies/felles-datakatalog.yaml` | Regelnamn `container_har_modelkatalog`, `modelkatalog_har_*` → `modellkatalog_*` |
| Same | Fritekst som inneheld «modelkatalog» → «modellkatalog» |
| `brreg-modellkatalog-eksempel.yaml` | YAML-nøkkel `modelkatalogar:` → `modellkatalogar:` |
| `src/linkml/ap-no/modelldcat-ap-no/examples/modelldcat-ap-no-eksempel.yaml` | Same |
| `tests/fixtures/modelldcat-ap-no-fixture.yaml` | Same |
| `src/mcp-linkml-validator/README.md` | Regelnamntabell |
| `specs/oppdater-validator-readme.md` | Regelnamntabell |

---

## Rekkjefølgje

1. Nivå 1: `git mv src/linkml/modelkatalog → src/linkml/modellkatalog`, oppdater konfig og docs
2. Nivå 2: `git mv` for skjema og eksempel, oppdater schema-felt
3. Nivå 3: Oppdater AP-NO-profil, policy og alle avhengige filer

Alle tre nivåa kan utførast i same arbeidsøkt i denne rekkjefølgja.
