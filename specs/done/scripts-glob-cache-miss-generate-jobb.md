# Plan: Innsnevr `src/assets/scripts/**`-glob i generate-jobben sin cache-nøkkel

**Kortnavn:** `scripts-glob-cache-miss-generate-jobb`
**Dato:** 2026-08-27

---

## Bakgrunn

I siste `generate`-workflow-køyring (commit `5705cef1`,
`fix(check-prereqs): endrer podman installasjonsguide`) las
`valider-og-analyser`-jobben frå cache for alle domene, mens
`generate`-matrisejobben **ikkje** gjorde det — sjølv om commiten ikkje
endra noko som skulle trigge regenerering av skjema-artefakt.

**Rotårsak, verifisert:** Commiten endra kun to filer:

- `src/assets/scripts/demo/javazone-demo-script.sh`
- `src/assets/scripts/makefile/check-prereqs.bash`

`generate`-jobben sin cache-nøkkel (`.github/workflows/generate.yml`,
"Cache genererte artefakter"-steget, linje ~499) inkluderer det **breie**
mønsteret `'src/assets/scripts/**'` i "infra"-delen av `hashFiles(...)`.
Dette globet fangar **alle** filer under `src/assets/scripts/`, uavhengig
av om dei faktisk er i kallgrafen til `make domain-<domain>`. Begge dei
endra filene er verifisert **utanfor** denne kallgrafen:

- `check-prereqs.bash` er berre referert frå `make/90-tools.mk` sitt
  `check-prereqs`-mål (grep-verifisert: `make/90-tools.mk:74`) —
  `make/90-tools.mk` er alt dokumentert som utanfor kallgrafen til
  `make domain-<domain>` i `specs/done/docs-only-endring-cache-miss-alle-domene.md`.
  `check-prereqs`-målet vert heller aldri kalla av `generate`-jobben eller
  `./.github/actions/generate-domain`.
- `javazone-demo-script.sh` ligg under `src/assets/scripts/demo/` — eit
  demo-skript utan referanse frå noko `make/*.mk`-mål i
  generator-kallgrafen.

`valider-og-analyser`-jobben sin cache-nøkkel (linje ~271) listar i staden
eksplisitte enkeltfiler under `src/assets/scripts/makefile/` og
`src/assets/scripts/utils/` — han fekk difor korrekt `cache-hit: true`,
sidan ingen av desse eksplisitte filene vart endra.

Dette er **same feilklasse** som `specs/done/docs-only-endring-cache-miss-alle-domene.md`
fiksa for `'make/**'` i same cache-nøkkel (erstatta med ei eksplisitt liste
over dei ni `.mk`-filene som **er** i kallgrafen) — men den fiksen dekte
ikkje `'src/assets/scripts/**'`-globet, som framleis er breitt og har no
vist seg å gi same type unødvendig full rekjøring av **alle**
`matrix:generate`-jobbar.

**Verifisert med grep — faktisk kallgraf til `make domain-<domain>`
(via `make/10-generator-macros.mk`, `make/20-domain-targets.mk`,
`make/30-instances.mk`, `make/40-validation.mk`, `.github/actions/generate-domain/action.yml`)
brukar utelukkande filer under:**

- `src/assets/scripts/makefile/*.py` og `*.sh` (batch-generate.py,
  batch-generate-instances.py, run-domain-pipeline.sh,
  batch-render-plantuml.sh, batch-gen-xsd.sh, batch-asyncapi-validate.sh,
  batch-lint.py, batch-linkml-validate.py, check-import-duplicates.py,
  detect-validation-policy.py, run-schema-validation.py,
  save-validation-log.py, run-validation.sh, filter_container.awk m.fl.)
- `src/assets/scripts/scaffolding/resolve-catalog-slug.sh` (eitt enkelt
  skript, brukt av `make/30-instances.mk`)

**Ikkje verifisert enno, treng vidare gransking før implementering:**

- Om nokon av `makefile/*.py`-skripta importerer moduler frå
  `src/assets/scripts/utils/` (slik `find-unused-local-definitions.py`
  gjorde i `valider-og-analyser`-jobben sitt tilsvarande arbeid, jf.
  `specs/backlog/cache-valider-og-analyser-modellanalyse.md` sitt
  "Status"-avsnitt — der vart eit reelt hòl funne i etterkant av fyrste
  utkast). Må sjekkast eksplisitt med grep før ei eksklusjonsliste vert
  endeleg.
- `src/assets/scripts/container/**` — brukt av Dockerfile-bygga (allereie
  dekt separat via `Dockerfile.*`-hashane i same nøkkel) eller direkte i
  kallgrafen? Avklar før eksklusjon.

## Mål

- Ei endring som **kun** rører filer under `src/assets/scripts/` utanfor
  den faktiske kallgrafen til `make domain-<domain>` (t.d.
  `src/assets/scripts/demo/**`, `check-prereqs.bash`,
  `src/assets/scripts/migreringsscript/**`, `src/assets/scripts/scaffolding/**`
  utanom `resolve-catalog-slug.sh`) skal **ikkje** invalidere
  per-domene-cachen i `generate`-jobben.
- Ingen endring i cache-oppførsel for reelle generatorskript-endringar
  (alt under `src/assets/scripts/makefile/` som faktisk er i kallgrafen,
  pluss `resolve-catalog-slug.sh`) — desse skal framleis invalidere cachen
  slik dei gjer i dag.

## Steg

1. Grep-verifiser fullstendig kallgraf frå `make domain-<domain>` til
   `src/assets/scripts/**` (byggje vidare på lista i "Bakgrunn" over),
   inkludert eventuelle transitive Python-importar frå `utils/`-mappa.
   Avklar dei to "ikkje verifisert"-punkta over.
2. I `.github/workflows/generate.yml`, "Cache genererte artefakter
   (${{ matrix.domain }})"-steget: erstatt `'src/assets/scripts/**'` med
   anten (a) ei eksplisitt liste over relevante fil-/undermappe-glob
   (t.d. `'src/assets/scripts/makefile/**'` +
   `'src/assets/scripts/scaffolding/resolve-catalog-slug.sh'` + evt.
   `'src/assets/scripts/utils/**'` dersom steg 1 stadfestar reell bruk),
   same positiv-liste-tilnærming som vart valt for `make/**` i
   `specs/done/docs-only-endring-cache-miss-alle-domene.md`.
3. Oppdater kommentaren over cache-steget til å forklare den nye,
   innsnevra lista og kvifor `demo/`, `migreringsscript/`, og
   (heile eller delar av) `scaffolding/` er medvite utelatne.
4. Test lokalt/i CI: gjer ei rein endring i t.d.
   `src/assets/scripts/demo/javazone-demo-script.sh` eller
   `check-prereqs.bash`, stadfest `cache-hit: true` for alle domene i
   `generate`-matrisa i neste køyring.
5. Test at ei reell endring i eit skript i kallgrafen (t.d.
   `batch-generate.py`) framleis gir `cache-hit: false`.
6. `actionlint` mot `generate.yml` (podman, jf. CLAUDE.md § «Actionlint
   etter CI-endring»).
7. Oppdater spec med `## Utført` og flytt til `specs/done/`.

## Utanfor scope

- Det kjende, separate avviket kring transitiv import på tvers av domene
  (`src/linkml/<domain>/**`-scoping) — dekt av
  `specs/done/cache-valider-og-analyser-modellanalyse.md`, ikkje denne
  specen.
- Endringar i cache-nøklane til `valider-og-analyser` eller
  `modellanalyse-tvers-domene` — dei brukar alt eksplisitte fil-lister og
  er ikkje ramma av dette funnet.

## Relaterte filer

- `.github/workflows/generate.yml` — cache-nøkkelen i `generate`-jobben
  (linje ~477-499)
- `specs/done/docs-only-endring-cache-miss-alle-domene.md` — presedens for
  same feilklasse (`make/**`-globet), metode gjenbrukt her
- `specs/done/cache-valider-og-analyser-modellanalyse.md` — separat spec
  om caching i dei to andre jobbane i same workflow
- `make/90-tools.mk` — `check-prereqs`-målet, verifisert utanfor
  `make domain-<domain>`-kallgrafen

## Utført (2026-08-27)

1. **Kallgraf grep-verifisert** (steg 1) — begge "ikkje verifisert"-punkta
   i Bakgrunn avklarte:
   - `src/assets/scripts/utils/**` **er** i kallgrafen: fleire
     `makefile/*.py`-skript importerer transitivt frå `utils/`
     (`linkml_relative_import_patch.py` i batch-generate.py/batch-lint.py/
     batch-linkml-validate.py/check-import-duplicates.py;
     `utils.schema_meta`/`utils.release_helpers`/`utils.validation_log` i
     detect-validation-policy.py/run-schema-validation.py/
     save-validation-log.py/run-validation.sh; `utils.codeowners` i
     `scaffolding/resolve-catalog-slug.sh`). Lagt til i cache-nøkkelen.
   - `src/assets/scripts/container/**` er **ikkje** i kallgrafen til
     `make domain-<domain>` — einaste fila (`asyncapi-validate.js`) vert
     kun kopiert inn via `COPY` i `Dockerfile.asyncapi-cli-minimal`, som
     alt får ny image-tag frå `compute-image-tags`-action uavhengig av
     denne cache-nøkkelen. Medvite utelaten.
   - `scaffolding/` er kun i kallgrafen via `resolve-catalog-slug.sh`
     (brukt av `make/30-instances.mk`) — dei fire andre skripta der
     (`new-modell.sh`, `new-modellkatalog.sh`, `new-begrepssamling.sh`,
     `remove-modell.sh`) er scaffolding-verktøy utanfor kallgrafen.
   - `demo/` og `migreringsscript/` stadfesta framleis heilt utanfor
     kallgrafen (ingen treff i generator-`.mk`-filene).
2. **Cache-nøkkelen innsnevra** i `.github/workflows/generate.yml`
   ("Cache genererte artefakter"-steget): `'src/assets/scripts/**'`
   erstatta med `'src/assets/scripts/makefile/**'`,
   `'src/assets/scripts/scaffolding/resolve-catalog-slug.sh'` og
   `'src/assets/scripts/utils/**'`.
3. **Kommentar oppdatert** rett over cache-steget — forklarar den nye,
   innsnevra lista og kva som er medvite utelate (`demo/`,
   `migreringsscript/`, resten av `scaffolding/`, `container/`).
4. `actionlint` køyrt mot `generate.yml` — ingen funn, exit code 0.
   `python3 -c "import yaml; yaml.safe_load(...)"` — YAML framleis gyldig.
5. **Ikkje utført (krev reell CI-køyring, som LLM ikkje kan trigge —
   inga push-tilgang):** steg 4 og 5 sin live-verifisering av
   `cache-hit: true`/`false`-utfall i faktisk `generate`-jobb-køyring.
   Koden er grep-verifisert korrekt (sjå punkt 1), men brukar bør
   stadfeste på neste push som (a) berre rører t.d.
   `src/assets/scripts/demo/**` eller `check-prereqs.bash` — forvent
   `cache-hit: true` for alle domene i `generate`-matrisa — og (b) rører
   t.d. eit skript i `makefile/`- eller `utils/`-kallgrafen — forvent
   framleis `cache-hit: false`.

Specen kan flyttast til `specs/done/` når brukar har stadfesta CI-åtferda
i punkt 5, eller no dersom brukar ønskjer å arkivere med denne
avgrensinga dokumentert (jf. presedens i
`specs/done/docs-only-endring-cache-miss-alle-domene.md`, der same type
attståande live-verifisering vart arkivert med tilsvarande merknad).

**Stadfesta av brukar 2026-09-04** (jf.
`specs/done/evaluering-gjentakande-monster-backlog.md`, P6): CI-åtferda i
punkt 5 er stadfesta. Merk: same feilklasse (breitt glob for
`src/assets/scripts/**`) vart uavhengig funne att i
`lenkje-og-mermaid-sjekk.yml` (retta same dag, sjå P3 i
`evaluering-gjentakande-monster-backlog.md`) — denne fila sin fiks dekte
altså berre `generate.yml`, ikkje alle stader same nøkkel vert brukt.
Flytta til `specs/done/`.
