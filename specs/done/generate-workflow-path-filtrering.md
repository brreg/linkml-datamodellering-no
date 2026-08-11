# Presiser path-filtrering i generate.yml

## Bakgrunn

Commit a299364 (`feat(analyse-iri-resolution)`) trigga ei full køyring av
`generate.yml` (alle domene) sjølv om ingen av endringane påverkar noko
`generate`-jobben faktisk brukar (`make domain-<domain>`, `make docs-publish`,
`make docs-build`). To ting matcha det eksisterande, breie `paths:`-filteret:

- `Makefile` fekk lagt til éi `include make/91-modell-analyse.mk`-linje —
  matcha det bokstavelege `Makefile`-elementet i filteret
- To nye analyse-script (`check-iri-resolution.py`, `find-similar-names.py`)
  hamna under `src/assets/scripts/**` — matcha det breie script-filteret

Begge desse er berre brukte av `modell-analyse.yml` (vekentleg, informativ
rapport — ikkje del av generate/publish-pipelinen).

Motsett hol oppdaga under gransking: `make/**` (t.d.
`make/20-domain-targets.mk`, `make/50-docs.mk` — filer som *styrer* domene-
generering og docs-publisering) er **ikkje** i `paths:`-lista i det heile, så
ei reell endring der ville **ikkje** trigge ein rebuild. Cache-nøkkelen for
"infra" i `generate`-jobben har same hol: `hashFiles(...)`-lista manglar
`make/**`, så sjølv om vi legg `make/**` til trigger-filteret, kan ein
cache-hit likevel servere utdaterte artefakt dersom berre eit
`make/*.mk`-generatormål endrar seg.

## Steg

1. Legg `make/**` til `paths:`-filteret i `generate.yml` (steg-triggeret) —
   generatormål i `make/*.mk` styrer faktisk `make domain-*` og
   `make docs-publish`/`docs-build`
2. Legg negative glob-mønster (`!...`) til same `paths:`-liste for filer som
   verifisert **ikkje** er i kallgrafen til generate.yml sine make-mål:
   - `!src/assets/scripts/makefile/check-iri-resolution.py`
   - `!src/assets/scripts/makefile/find-similar-names.py`
   - `!src/assets/scripts/migreringsscript/**`
   - `!src/assets/scripts/scaffolding/**`
   - `!src/assets/scripts/pr-linkml-interactive.bash`
   - `!make/91-modell-analyse.mk`
3. Utvid "infra"-cache-nøkkelen i `generate`-jobben (`hashFiles(...)` for
   `cache-generated`-steget) til å inkludere `make/**`, slik at ei ekte
   endring i eit generatormål ikkje vert maskert av ein falsk cache-hit
4. Køyr `actionlint` mot `generate.yml` (podman, jf. CLAUDE.md § "Actionlint
   etter CI-endring")
5. Oppdater spec med `## Utført` og flytt til `specs/done/`

## Merknad om avgrensing

GitHub Actions sine `paths:`-filter er fil-nivå, ikkje linje-nivå. Ei
framtidig endring i `Makefile` som berre legg til éi urelatert `include`-linje
(t.d. for eit nytt analyse-mål) vil framleis trigge `generate.yml`, sidan
heile `Makefile` framleis må stå i filteret (han *er* reelt relevant for
generering elles). Dette er ein aksepta avgrensing i GitHub Actions, ikkje
noko denne endringa kan løyse fullt ut.

## Utført

1. `make/**` lagt til `paths:`-filteret i `generate.yml`, med `!make/91-modell-analyse.mk` ekskludert
2. Negative glob-mønster lagt til for `check-iri-resolution.py`, `find-similar-names.py`, `migreringsscript/**`, `scaffolding/**`, `pr-linkml-interactive.bash`
3. `make/**` lagt til "infra"-cache-nøkkelen (`hashFiles(...)`) i `generate`-jobben
4. `actionlint` køyrt mot `generate.yml` — ingen `[expression]`/syntaksfeil, kun 4 pre-eksisterande `[shellcheck]`-funn (urelaterte til denne endringa)
