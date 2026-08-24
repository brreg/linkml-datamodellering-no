# Kort ned `generate.yml`-køyretid til under 5 minutt

## Bakgrunn

Brukaren bad om å evaluere om det finst tiltak som kan korte ned
totaltida for `.github/workflows/generate.yml`. Siste køyring
(`databaseId 32716167174`, 2026-08-24, `workflow_dispatch`) tok **6 min
20 s** (10:19:05 → 10:25:25). Målet er å kome under **5 min (300 s)** —
altså minst **-80 s**.

Fleire tidlegare specar har alt optimalisert delar av denne pipelinen:
`specs/done/effektiviser-generate-workflow-koyretid.md` (batching av
generator-kall per domene), `specs/done/splitt-validering-modellanalyse-eigen-jobb.md`
og `specs/done/effektiviser-modellanalyse-koyretid.md` (eigne parallelle
jobbar for validering/modellanalyse), og `specs/done/raskare-docs-build.md`
(djup profilering av `make docs-build`). Denne specen byggjer vidare på
desse — særleg `raskare-docs-build.md`, som konkluderte at CI-golvet for
`docs-build` (~154 s) i hovudsak er irreduserbart utan funksjonelle
avvegingar (fjerne/snevre inn søk, redusere sidetal).

## Målt tidsfordeling (køyring 32716167174)

Henta frå `gh run view <id> --json jobs` og `gh run view <id> --log`
(steg-tidsstempel for `publish`-jobben).

| Fase | Tid | Del av total |
|---|---|---|
| **Pre-publish** (checkout-source → ensure-images → generate/valider-og-analyser-matrise, kritisk sti `generate / oreg`) | 123 s | 32 % |
| **`publish`-jobb, total** | 256 s | 67 % |
| ↳ Oppsett (nedlast `source`+artefakt-merge+modellanalyse-artefakt, GHCR-login, image-pull) | ~23 s | 6 % |
| ↳ `make docs-publish` (Steg 1-3, innhaldsgenerering) | 32 s | 8 % |
| ↳ **`make docs-build` (sjølve mkdocs-bygget)** | **154 s** | **40 % av HEILE workflowen** |
| ↳ Konfigurer + last opp Pages-artefakt | 10 s | 3 % |
| ↳ Deploy til GitHub Pages (forsøk 1, vellukka) | 33 s | 8 % |

`docs-build` åleine er den klart største enkeltposten — større enn heile
pre-publish-fasen. `generate / oreg` (9 skjema) er den lengste
domene-jobben i matrisa (~90 s, mot 30-60 s for andre domene), sjølv om
`ap-no` har fleire `build.yaml` (10) og er ~30 s raskare — talet på
genererte format/generator-kall ser ut til å styre meir enn talet på
skjema.

## Kva `raskare-docs-build.md` alt fann (og kvifor det avgrensar handlingsrommet)

- `mkdocs-build-cache-plugin` vart fjerna fordi han **aldri traff cache**:
  han hasha heile `docs_dir`-**output**, og `mkdocs/publish.sh` skriv eit
  ferskt "Portalen vart sist bygd: …"-tidsstempel inn i portalen **kvar
  einaste køyring** — cache-ID-en endra seg difor alltid.
- Rein markdown/mal-rendering (utan søk/cache-plugin) er eit golv på
  ~140 s lokalt (WSL2-native fs), driven av dei ~5589 auto-genererte
  klasse/slot/enum/type-sidene (97 % av alle sider).
- `search`-pluginen legg til ~30 % (~46 s ekstrapolert til CI-tal) oppå
  golvet, for å indeksere alle sidene.
- Podman named volumes (løyser WSL2/9p-overhead) er **irrelevant i CI** —
  GitHub-runnarane brukar native ext4, ingen monteringsgrense å krysse.

Konklusjonen då var at vidare reduksjon av `docs-build` krev anten å
redusere innhald eller svekke søk — begge funksjonelle avvegingar utanfor
scope. **Brukaren har no eksplisitt stadfesta at søk-innsnevring** (tiltak
4 under) **framleis skal stå som "vurdert/avvist"**, ikkje eit aktivt
forslag — same konklusjon som før.

## Ny innsikt: cache på INPUT i staden for OUTPUT

`generate.yml` sin `on.push.paths`-filter dekkjer **ikkje**
`.github/workflows/**` — endringar i sjølve workflow-fila (som denne
økta sine `perf(generate.yml)`-commitar) triggar difor aldri denne
workflowen via push. Køyringar som testar CI-orkestrering (slik denne
evalueringa gjeld) startar via `workflow_dispatch`, og har **null
reell endring** i generert dokumentasjonsinnhald — likevel betaler dei
heile `docs-publish`+`docs-build`-kostnaden (186 s) kvar gong.

Grunnen `mkdocs-build-cache-plugin` aldri traff, var at han hasha
**resultatet** (`docs_dir`), som alltid inneheld eit ferskt tidsstempel.
Dei faktiske **inndataa** som avgjer det renderte innhaldet —
`generated/<domain>/**` (alle domene, etter merge), `mkdocs/publish.sh`,
`src/assets/templates/docgen/**`, `mkdocs/docs/{stylesheets,javascripts,overrides}`
og `src/assets/scripts/**` — inneheld **ikkje** noko tidsstempel. Ein
`actions/cache`-nøkkel bygd på desse inndataa (i staden for på output)
vil difor **treffe** for køyringar der ingenting av dette har endra seg,
og bomme korrekt for køyringar med reelle skjema-/malendringar.

## Tiltak

1. **Legg til site-cache i `publish`-jobben** (`actions/cache@v6`,
   `path: mkdocs/site/`), nøkla på ein kombinert hash av:
   - `generated/**` (etter `merge-generated-artifacts`-steget, alle domene)
   - `generated/modell-analyse-tvers-domene/**`
   - `mkdocs/publish.sh`
   - `src/assets/templates/docgen/**`
   - `mkdocs/docs/stylesheets/**`, `mkdocs/docs/javascripts/**`, `mkdocs/docs/overrides/**`
   - `src/assets/containers/Dockerfile.mkdocs`

   Plasser cache-steget **etter** nedlasting/samanslåing av
   generate-artefakta (treng dei ferdige for å hashe), men **før**
   "Publiser og bygg dokumentasjonsportal". Legg `if:
   steps.cache-site.outputs.cache-hit != 'true'` på sjølve
   docs-publish/docs-build-steget. Ved treff: hopp rett til "Konfigurer
   GitHub Pages" → "Last opp Pages-artefakt" → deploy, med den
   gjenoppretta `mkdocs/site/`.

   **Godkjend avveging (jf. brukarsvar):** ved cache-treff viser
   portalen sitt "sist bygd"-tidsstempel tidspunktet for det opphavlege
   (cacha) bygget, ikkje denne køyringa — akseptert som korrekt
   åtferd (tidsstempelet skal reflektere når *innhaldet* sist vart
   bygd, ikkje når CI sist køyrde).

   **Forventa gevinst:** ~186 s (nesten heile `docs-publish`+
   `docs-build`) på køyringar med uendra generert innhald (typisk
   CI-/workflow-tuning-iterasjonar, `workflow_dispatch`-rekøyringar,
   reine `.github/workflows/**`-endringar testa manuelt). **Null gevinst**
   på køyringar med reelle skjema-/malendringar, sidan desse per
   definisjon endrar `generated/**` og dermed cache-nøkkelen.

2. **Undersøk kvifor `generate / oreg` er lengste domene-jobb** (~90 s,
   kritisk sti i pre-publish-fasen). Domenet har 9 `build.yaml` (færre
   enn `ap-no` sine 10, som er ~30 s raskare) — talet på
   genererte format/generator-flagg per skjema ser ut til å vege meir enn
   talet på skjema. Profiler kva `gen-*`-steg som dominerer for oreg
   (t.d. via `LOGLVL=DEBUG`/`timed_run`-utskrift i
   `generate-domain`-actionen), og vurder om domenet kan delast i to
   matrise-einingar for betre balansering. Meir uviss gevinst enn tiltak
   1 (anslag 20-40 s), krev eiga profilering før konkret forslag.

3. **Fjern ubrukt `mkdocs-kroki-plugin`** frå
   `src/assets/containers/Dockerfile.mkdocs` — installert via `pip`, men
   ikkje referert i `mkdocs.yml` sin `plugins:`-liste eller nokon annan
   stad i `mkdocs/` (verifisert med `grep -rn kroki mkdocs/`). Reint
   DRY-/vedlikehaldstiltak (fjernar daud avhengigheit), ikkje ei reell
   tidsgevinst i normale køyringar sidan `mkdocs-local`-imaget vanlegvis
   vert pulla ferdigbygd frå GHCR (`ensure-images`-jobben cacha på
   image-tag) — gjev berre gevinst ved faktiske image-rebuild.

**Eksplisitt vurdert og avvist (jf. brukarsvar):**

4. **Snevre inn `search`-pluginen sitt indekseringsomfang** (ekskluder
   dei ~5500 auto-genererte per-klasse/-slot/-enum/-type-sidene frå
   fulltekstindeksen, behald berre modell-/domeneoversiktssider).
   Estimert gevinst: ~30 % av `docs-build` (~46 s i CI). **Ikkje teke med
   som aktivt forslag** — søk er ein funksjonell verdi for heile portalen,
   ikkje reindyrka overhead, same konklusjon som i
   `specs/done/raskare-docs-build.md` sitt tilsvarande (meir drastiske)
   forslag om å fjerne søk heilt. Står att som eit alternativ dersom
   tiltak 1-3 ikkje er nok til å nå <5 min for køyringar med reelt
   innhaldsendring.

**Eksplisitt utanfor scope:**

5. **Sharding av sjølve mkdocs-bygget** (parallelle delbygg av `site/`
   per domene-gruppe, slått saman før deploy) — kunne i teorien kutte
   store delar av dei 154 s, men krev fleire separate
   mkdocs-prosjekt/-konfigurasjonar, handtering av kryssdomene-lenkjer og
   ein samla søkeindeks på tvers av shards. Vurdert som for høg
   kompleksitet/risiko i forhold til gevinst for denne specen — kan takast
   opp som eiga spec dersom tiltak 1 ikkje gjev nok i praksis.
6. Podman named volumes for `docs-build` og volum-staging for
   `LINKML_RUN`/`PYTHON_RUN`/`AVROTIZE_RUN`/`ASYNCAPI_RUN` — alt vurdert
   og avvist i `specs/done/raskare-docs-build.md` (løyser eit
   WSL2/9p-problem som ikkje finst på GitHub-hosta runnarar).

## Realistisk forventa resultat

- **Køyringar med uendra generert innhald** (CI-/workflow-tuning, som
  denne økta): tiltak 1 kan i praksis bringe totaltida ned mot
  ~**140-160 s** (pre-publish 123 s + minimal publish-overhead ~20-30 s)
  — godt under 5 min.
- **Køyringar med reell skjema-/malendring**: tiltak 1 gjev null gevinst
  (cache bommar korrekt). Med tiltak 2+3 realistisk anslag **~330-350 s**
  — framleis over 5 min-målet. Å kome under 5 min for **alle** køyringar
  (inkludert reelle innhaldsendringar) krev truleg tiltak 4
  (søk-innsnevring) eller ein meir djuptgåande arkitekturendring (tiltak
  5) — begge eksplisitt sett på vent inntil tiltak 1-3 er implementerte
  og målte i praksis.

## Akseptansekriterium

- [x] Tiltak 1: site-cache lagt til i `publish`-jobben, `actionlint`
      køyrt mot `generate.yml` etter endringa (jf. CLAUDE.md "Actionlint
      etter CI-endring")
- [ ] Tiltak 1: verifisert at cache-treff faktisk hoppar over
      docs-publish/docs-build (via CI-logg etter ei uendra-innhald-rekøyring)
      — **krev faktisk CI-køyring**, ikkje verifisert enno
- [ ] Tiltak 1: verifisert at cache-bom framleis produserer korrekt
      `mkdocs/site/`-innhald (via CI-logg etter ei innhaldsendrande køyring)
      — **krev faktisk CI-køyring**, ikkje verifisert enno
- [ ] Tiltak 2: profilering av `generate / oreg` dokumentert, med
      konkret vidare forslag (eller grunngjeving for kvifor ingen
      splitting er verdt det) — **ikkje implementert enno**
- [x] Tiltak 3: `mkdocs-kroki-plugin` fjerna, `make build-docker-mkdocs`
      verifiserer feilfri rebuild
- [ ] CI-tidsbruk før/etter målt og dokumentert i "Utført" — **krev
      faktisk CI-køyring** (brukaren sitt ansvar per CLAUDE.md, LLM kan
      ikkje verifisere sjølv)

## Relaterte filer

- `.github/workflows/generate.yml` — `publish`-jobben (site-cache-steg,
  tiltak 1), `generate`-matrisa (tiltak 2)
- `src/assets/containers/Dockerfile.mkdocs` — fjern `mkdocs-kroki-plugin`
  (tiltak 3)
- `mkdocs/publish.sh` — kjelde for tidsstempel-linja som gjorde
  output-basert cache verknadslaus (uendra av denne specen, berre årsak
  til kvifor input-basert cache er nødvendig)
- `specs/done/raskare-docs-build.md` — føregåande djup profilering av
  `docs-build`, grunngjeving for kvifor søk-/innhaldsreduksjon er avvist
- `specs/done/effektiviser-generate-workflow-koyretid.md` — tidlegare
  batching av generator-kall i `generate`-matrisa
- `specs/done/splitt-validering-modellanalyse-eigen-jobb.md`,
  `specs/done/effektiviser-modellanalyse-koyretid.md` — tidlegare
  jobb-splitting/parallellisering same workflow

## Utført (delvis — tiltak 1 og 3)

**Tiltak 1 (site-cache):**
- `.github/workflows/generate.yml`, `publish`-jobben: lagt til steget
  "Cache bygd site (mkdocs/site/)" (`actions/cache@v6`, `id: cache-site`)
  rett etter dei to artefakt-nedlastingssteg som byggjer `generated/`.
  Nøkkelen hashar `generated/**`, `mkdocs/publish.sh`, `mkdocs/lib/**`,
  `mkdocs/docs/**`, `mkdocs/overrides/**`,
  `src/assets/containers/Dockerfile.mkdocs`, `README.md`,
  `src/assets/scripts/makefile/generate-readme-tables.sh` og
  `src/mcp-linkml-validator/policies/README.md` — kartlagt ved å lese
  `mkdocs/publish.sh` sine faktiske filavhengigheiter (m.a.
  `mkdocs/lib/scripts/collect-schema-metadata.py`,
  `generate-readme-tables.sh` + `README.md` → `index.md`), ikkje berre
  det opphavlege specforslaget (som mangla `mkdocs/lib/**` og README-kjeda).
  `mkdocs/mkdocs.yml` og resten av `mkdocs/docs/<domain>/` er medvite
  UTELATNE frå nøkkelen — dei er gitignora/genererte av `docs-publish`
  sjølv og finst ikkje i arbeidskatalogen før steget køyrer.
- Steget "Oppgrader crun" flytta til etter cache-steget (var før
  `merge-generated-artifacts`, som ikkje treng podman/crun) og gjeve
  `if: steps.cache-site.outputs.cache-hit != 'true'`, saman med "Logg inn
  på GHCR", "Last mkdocs-local og python-pytest frå GHCR" og "Publiser og
  bygg dokumentasjonsportal" — alle fire hoppar no over ved cache-treff.
  "Konfigurer GitHub Pages", "Last opp Pages-artefakt" og
  deploy-stega køyrer uendra (bruker den gjenoppretta eller nybygde
  `mkdocs/site/`).
- `actionlint` (via podman, `docker.io/rhysd/actionlint:latest`) køyrt mot
  `generate.yml`: ingen `[expression]`-funn.
- **Ikkje verifisert:** faktisk cache-treff/-bom-åtferd i CI (krev ekte
  workflow-køyring, brukaren sitt ansvar per CLAUDE.md).

**Tiltak 3 (fjern ubrukt kroki-plugin):**
- `src/assets/containers/Dockerfile.mkdocs`: fjerna `RUN pip install
  mkdocs-kroki-plugin`-steget (ikkje referert i `mkdocs.yml` eller nokon
  `mkdocs/`-fil, stadfesta med grep).
- `make build-docker-mkdocs` køyrt lokalt (sandbox-nettverk deaktivert for
  denne eine kommandoen, sidan podman-pull krev tilgang til `docker.io`
  utanfor standard-allowlista): bygde `localhost/mkdocs-local:latest` på
  nytt, feilfritt.

**Attverande (ikkje implementert):**
- Tiltak 2 (profilering/splitting av `generate / oreg`) — ikkje starta.
- CI-tidsbruk før/etter for tiltak 1 — krev ei faktisk workflow-køyring.

Specen vert verande i `specs/backlog/` til tiltak 2 er vurdert/utført og
CI-tidsbruken for tiltak 1 er stadfesta.
