# Docs-only-endring i make/*.mk trigga cache-miss og full rekjøring av alle matrix:generate-jobbar

## Bakgrunn

Commit `0fac7453` (`feat(mkdocs): tidtak docs-build individuelt, behald som
separat make-kall frå docs-publish`) endra kun `make/50-docs.mk` og
`mkdocs/publish.sh` — filer som utelukkande styrer `make docs-publish`/
`make docs-build` (mkdocs-portalen), og som ikkje er i kallgrafen til
`make domain-<domain>` (domenegenereringa). Likevel førte commiten til at
**alle** `generate`-matrix-jobbane (éin per domene) køyrde på nytt frå botnen
i staden for å hente frå cache — sjølv om ingen skjemainnhald var endra.

**Rotårsak, verifisert:** `generate`-jobben i `.github/workflows/generate.yml`
(linje ~172-177) cachar genererte artefakt per domene med denne nøkkelen:

```yaml
key: v4-generated-${{ matrix.domain }}-${{ hashFiles(format('src/linkml/{0}/**', matrix.domain)) }}-infra-${{ hashFiles('src/assets/containers/Dockerfile.linkml', 'src/assets/containers/Dockerfile.avrotize', 'src/assets/containers/Dockerfile.asyncapi-cli-minimal', 'src/assets/scripts/**', 'src/assets/templates/**', 'make/**', 'Makefile') }}
```

`make/**` inngår ublokka i "infra"-delen av nøkkelen — **for alle domene**.
Denne breie `make/**`-inkluderinga vart lagt til i
`specs/done/generate-workflow-path-filtrering.md` for å løyse eit anna,
motsett problem (ei reell endring i eit generatormål vart *ikkje* fanga opp
av cache-nøkkelen). Den endringa la derimot ikkje inn nokon eksklusjon for
`.mk`-filer som **ikkje** er i kallgrafen til `make domain-<domain>` — i
motsetnad til `paths:`-triggeret på steg-nivå (same fil, linje ~29), som
allereie har eit presedens for slike eksklusjonar
(`!make/91-modell-analyse.mk`).

**Verifisert med grep at desse filene ikkje er i kallgrafen til
`make domain-<domain>`** (ingen referansar frå `make/20-domain-targets.mk`,
`make/10-generator-macros.mk`, `make/11-generator-targets.mk`,
`make/00-settings.mk`, `make/01-containers.mk`, `make/02-schema-discovery.mk`,
`make/03-output.mk`, `make/30-instances.mk`, `make/40-validation.mk` til
noko mål/variabel definert i desse filene):

- `make/50-docs.mk` — `docs-serve`/`docs-build`/`docs-publish` (mkdocs-portal)
- `make/60-mcp.mk` — MCP-validator-mål (`mcp-linkml-*`)
- `make/70-scaffolding.mk` — `new-modell`/`new-begrepskatalog` o.l.
- `make/90-tools.mk` — `gource-*`, `check-prereqs`
- `make/91-modell-analyse.mk` — alt ekskludert (presedens)

**Ikkje verifisert, treng vidare gransking før implementering:**

- `make/80-images.mk` (`build-docker-linkml` m.fl.) — desse måla vert ikkje
  kalla direkte av `generate`-jobben (som brukar `./.github/actions/
  pull-images` mot GHCR, ikkje `make build-docker-*`), men Dockerfile-inn-
  haldet dei byggjer frå er alt eksplisitt i cache-nøkkelen separat
  (`Dockerfile.linkml` osv.) — usikkert om sjølve `.mk`-recipe-teksten har
  nokon reell påverknad utover det. Bør avklarast før eksklusjon.

**Observert biverknad i same commit (separat, ikkje denne spec sitt
hovudfokus):** commiten inneheldt òg endringar i `mkdocs/docs/referanse/
index.md` (sletta) og `.claude/settings.local.json` — filer som ikkje var
del av den tilsikta endringa. `mkdocs/docs/referanse/` er lista i
`.gitignore`, men fila var frå før spora i git (før ignore-regelen vart
lagt til), så lokale `make docs-publish`/`make docs-build`-køyringar
etterlet endringar som vart fanga opp av ei etterfølgjande brei
`git add`. Dette peikar på eit separat, mindre ryddeproblem (bør
`git rm --cached` desse spora-men-ignorerte filene?) — ikkje del av denne
spec-en sitt mål, men verdt ein eigen, seinare spec om det gjentek seg.

## Mål

- Ei endring som **kun** rører `.mk`-filer utanfor kallgrafen til
  `make domain-<domain>` (verifisert over) skal **ikkje** invalidere
  per-domene-cachen i `generate`-jobben, og skal difor **ikkje** trigge
  full rekjøring av `matrix:generate` for noko domene.
- Ingen endring i cache-oppførsel for reelle generatormål-endringar
  (`make/00-settings.mk`, `make/01-containers.mk`,
  `make/02-schema-discovery.mk`, `make/03-output.mk`,
  `make/10-generator-macros.mk`, `make/11-generator-targets.mk`,
  `make/20-domain-targets.mk`, `make/30-instances.mk`,
  `make/40-validation.mk`, `Makefile`) — desse skal framleis invalidere
  cachen slik dei gjer i dag.

## Steg

1. Avklar `make/80-images.mk` sin status (sjå "Ikkje verifisert" over) —
   les gjennom `.github/actions/pull-images/action.yml` og
   `make/10-generator-macros.mk`/`make/11-generator-targets.mk` for å
   stadfeste om nokon reell køyretidsbruk av `make/80-images.mk` sine mål
   skjer i `generate`-jobben, eller om images.json+Dockerfile-hash åleine
   er tilstrekkeleg.
2. I `.github/workflows/generate.yml`, "Cache genererte artefakter
   (${{ matrix.domain }})"-steget (~linje 172-177): erstatt
   `hashFiles(..., 'make/**', ...)` med eksplisitte per-fil/glob-referansar
   til dei `.mk`-filene som **er** i kallgrafen (jf. "Mål"), i staden for
   det brei `make/**`-mønsteret — ELLER, dersom `hashFiles()` sin
   negative-glob-støtte tillet det reint, behald `make/**` men legg til
   eksplisitte eksklusjonar for filene stadfesta over (same idé som
   `!make/91-modell-analyse.mk` i `paths:`-triggeret, men `hashFiles()`
   støttar ikkje `!`-negering på same måte som `paths:` — må difor
   truleg vere ei positiv liste over relevante filer/glob i staden for
   ei eksklusjonsliste).
3. Oppdater kommentaren over cache-steget (og evt. i
   `specs/done/generate-workflow-path-filtrering.md` sitt "Merknad om
   avgrensing") til å referere denne presiseringa.
4. Test lokalt/i CI: gjer ei rein `make/50-docs.mk`-endring (t.d. eit
   kommentartillegg), stadfest at cache-steget rapporterer
   `cache-hit: true` for alle domene i neste `generate`-køyring, og at
   ingen `matrix:generate`-jobb køyrer det tunge genererings-/
   valideringsarbeidet.
5. Test at ei reell endring i t.d. `make/20-domain-targets.mk` framleis gir
   `cache-hit: false` (cache framleis fungerer for reelle
   generatormål-endringar).
6. `actionlint` mot `generate.yml` (podman, jf. CLAUDE.md § «Actionlint
   etter CI-endring»).
7. Oppdater spec med `## Utført` og flytt til `specs/done/`.

## Utanfor scope

- Oppryddinga av spora-men-gitignora `mkdocs/docs/`-filer (jf. "Observert
  biverknad" over) — eiga, seinare vurdering.
- `make/80-images.mk` sin eksklusjon vert **ikkje** gjort automatisk som
  del av denne spec-en før steg 1 er avklara — inntil då vert han verande
  i "infra"-hashen som i dag (trygt val, unngår falske cache-hit dersom
  han faktisk er relevant).

## Utført

1. **`make/80-images.mk` avklart:** `.github/actions/pull-images/action.yml`
   fell tilbake til `make "$make_target"` (t.d. `build-docker-linkml`) når
   ein GHCR-pull feilar — desse måla er difor reelt i kallgrafen (om enn
   berre på feil-fallback-stien) og er **behaldne** i infra-hashen.
2. Cache-nøkkelen i `.github/workflows/generate.yml` sitt
   "Cache genererte artefakter"-steg bytt frå breie `'make/**'` til ei
   eksplisitt liste over dei ni `.mk`-filene stadfesta i kallgrafen til
   `make domain-<domain>`: `00-settings.mk`, `01-containers.mk`,
   `02-schema-discovery.mk`, `03-output.mk`, `10-generator-macros.mk`,
   `11-generator-targets.mk`, `20-domain-targets.mk`, `30-instances.mk`,
   `40-validation.mk`, `80-images.mk`. Vald positiv-liste-tilnærming (ikkje
   `make/**` + negerte glob) sidan `hashFiles()` sin negasjonsstøtte ikkje
   var verifisert — ei eksplisitt liste er uansett meir lesbar/auditerbar
   for framtidige endringar.
3. Kommentar lagt til rett over cache-steget som forklarar kvifor listinga
   er eksplisitt, kva som er medvite utelate (`50-docs.mk`, `60-mcp.mk`,
   `70-scaffolding.mk`, `90-tools.mk`, `91-modell-analyse.mk`) og kvifor
   `80-images.mk` er med.
4. **Ikkje utført (krev reell CI-køyring, som eg ikkje kan trigge —
   ingen push-tilgang):** steg 4 og 5 sin live-verifisering av
   `cache-hit: true`/`false`-utfall i faktisk `generate`-jobb-køyring.
   Koden er grep-verifisert korrekt (sjå "Bakgrunn"), men den funksjonelle
   GitHub Actions-cache-oppførselen bør stadfestast av brukaren på neste
   push som (a) berre rører t.d. `make/50-docs.mk` — forvent `cache-hit`
   for alle domene — og (b) rører t.d. `make/20-domain-targets.mk` —
   forvent framleis full rekjøring.
5. `actionlint` køyrt mot `generate.yml` — ingen `[expression]`/syntaksfeil,
   same fire pre-eksisterande `[shellcheck]`-funn som før (urelaterte,
   linjenummer forskyvne av dei nye kommentarlinjene).
6. `python3 -c "import yaml; yaml.safe_load(...)"` — YAML framleis gyldig.

## Relaterte filer

- `.github/workflows/generate.yml` — cache-nøkkelen i `generate`-jobben
- `specs/done/generate-workflow-path-filtrering.md` — presedens for
  `paths:`-eksklusjonsmønster (`!make/91-modell-analyse.mk`) og
  opphavet til den breie `make/**`-inkluderinga i infra-hashen
- `make/50-docs.mk`, `make/60-mcp.mk`, `make/70-scaffolding.mk`,
  `make/90-tools.mk` — verifisert utanfor kallgrafen til
  `make domain-<domain>`
