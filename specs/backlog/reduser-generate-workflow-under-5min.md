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

2. **`generate / oreg` profilert (køyring 32716167174).** Henta direkte frå
   CI-jobbloggane (`gh api .../actions/jobs/<id>/logs`) for alle 9
   `generate / <domain>`-jobbar, inkludert `run-domain-pipeline.sh` sitt
   eige `print_pipeline_summary()`-steg-for-steg-oppsett (Fase 1/2/3, sjå
   `src/assets/scripts/makefile/run-domain-pipeline.sh`).

   **Jobb-nivå-breakdown, `oreg` (91 s total) mot `ap-no` (62 s total,
   nest-tregaste av dei "normale" domena):**

   | Delsteg | `oreg` | `ap-no` | Diff |
   |---|---|---|---|
   | download-artifact + oppsett | ~4 s | ~4 s | ~0 |
   | pull-images (parallelt) | 8,3 s | 7,4 s | +0,9 s |
   | **`generate-domain` (run-domain-pipeline.sh)** | **62,25 s** | **40,4 s** | **+21,9 s** |
   | upload-artifact (`generated-oreg`) | 10,2 s | 4,1 s | +6,1 s |

   `generate-domain`-steget (sjølve genereringspipelinen) og
   `upload-artifact` (meir output å laste opp) står for heile
   differansen — nedlasting/pull-images er identisk mellom domena.

   **Internt i `generate-domain` (Fase 1, 12 parallelle batch-kall på same
   runner), `oreg` mot `ap-no`:**

   | Steg | `oreg` | `ap-no` | `fint` (7 skjema, tregaste "normale" domene) |
   |---|---|---|---|
   | merge (validate) | **58,96 s** | 36,61 s | 40,19 s |
   | docs | **60,13 s** | 38,85 s | 45,59 s |
   | python | **58,87 s** | 8,21 s | 10,71 s |
   | plantuml | **55,33 s** | 36,59 s | 42,08 s |
   | owl | 51,25 s | 32,36 s | 35,22 s |
   | jsonld-context | 47,76 s | 8,17 s | 10,20 s |
   | proto | 43,04 s | 6,44 s | 10,15 s |
   | shacl | 43,06 s | 30,00 s | 10,10 s |
   | graphql | 41,88 s | 6,33 s | 10,68 s |
   | rdf | 37,43 s | 30,15 s | 34,93 s |
   | json-schema | 36,32 s | 6,23 s | 26,53 s |
   | Fase 2: openapi | 21,08 s | 3,85 s | 6,91 s |

   **To samverkande rotårsaker:**

   a) **Fleire aktive generatorar per skjema.** Samanlikna
      `generators:`-blokka i alle `build.yaml` på tvers av domene: 8 av
      `oreg` sine 9 skjema har 13 av 15 generatorar aktiverte
      (`jsonld_context`, `shacl`, `python`, `json_schema`, `owl`, `rdf`,
      `protobuf`, `example_rdf`, `openapi`, `graphql`, `erdiagram`,
      `docs`, `plantuml` — berre `xsd`/`asyncapi` av). `ap-no` sine 10
      skjema har typisk berre 6-7 aktive (`shacl`, `owl`, `rdf`,
      `erdiagram`, `docs`, `plantuml`) — resten (`python`,
      `json_schema`, `jsonld_context`, `protobuf`, `graphql`, `openapi`
      m.fl.) er av. Dette forklarar kvifor steg som `python`,
      `jsonld-context`, `proto` og `graphql` er 4-8× tregare for `oreg`
      enn `ap-no` (reelt generatorarbeid mot reint nær-augeblikkeleg
      containeroppstart-golv når generatoren er av for alle skjema i
      domenet).
   b) **Iboende skjemakompleksitet, uavhengig av generatorflagg.**
      `merge`-steget (`make validate`, ei rein LinkML-importvalidering
      som køyrer **uansett** kva generatorar som er aktiverte) er
      `oreg` sitt klart tregaste Fase 1-steg (58,96 s) — høgare enn
      **alle** andre domene, sjølv `ap-no` med fleire skjema (10 mot 8
      aktive i `oreg`). Dette peikar på at sjølve skjemaa i `oreg`
      (Brønnøysundregistera sine sentrale registermodellar —
      `enhetsregisteret-bvr*`-familien, `register-over-aksjeeiere`) er
      individuelt større/meir komplekse (fleire klasser/slots/importar)
      enn typiske AP-NO-profilskjema, ikkje berre at fleire
      generatorflagg er sette.
   c) **Ingen throttling av dei 12 parallelle Fase 1-batch-kalla.**
      `run-domain-pipeline.sh` startar alle 12 steg samstundes som
      bakgrunnsprosessar på éin GitHub-hosta runnar (typisk 4 delte
      vCPU). Sidan `oreg` har reelt arbeid i **nesten alle** 12 steg
      (mot `ap-no`, der 5-6 steg er nær-augeblikkelege no-op-kall), gjev
      dette **CPU-metting**: alle steg for `oreg` tek 36-60 s kvar,
      sjølv `merge` (generatorflagg-uavhengig) — eit teikn på at steg
      konkurrerer om avgrensa CPU-kapasitet i staden for å køyre reelt
      parallelt.

   **Konkret forslag (ikkje implementert):** Del `oreg` sine 9
   `build.yaml` i to matrise-einingar (t.d. basert på faktisk
   generator-arbeidsmengd, ikkje berre skjematal — flytt dei 4-5
   tyngste `enhetsregisteret-bvr*`-skjemaa til ei eiga gruppe). Kvar
   gruppe får då sin **eigen** GitHub-runnar (eigne 4 vCPU) i staden for
   å dele éin, som bør redusere CPU-mettinga frå (c) og bringe kvar
   halvdel ned mot `fint`/`modellkatalog`-nivå (~45-55 s pipeline +
   ~15-20 s oppsett/upload ≈ 60-75 s per gruppe, køyrde parallelt).
   **Estimert gevinst: ~20-30 s** på kritisk sti (pre-publish-fasen sitt
   lengste domene ville då vore `fint`/`modellkatalog` i staden for
   `oreg`).

   **Kompleksitet/kostnad, ikkje vurdert som verdt det no:** ei slik
   deling krev å utvide `discover-domains`-actionen (som i dag
   returnerer éin liste med domenenamn brukt identisk av **både**
   `generate`- og `valider-og-analyser`-matrisene, cache-nøklane i
   `generate`-jobben, `merge-generated-artifacts`, OG
   `mkdocs/publish.sh` sin nav-genereringslogikk som forventar éin
   mkdocs-sidekatalog per domene) til å støtte eit "sub-domene"-omgrep
   som framleis produserer éin samla `generated/oreg/`-katalog og éi
   samla `mkdocs/docs/oreg/`-sidegruppe etter samanslåing. Dette er ei
   djupare, meir invasiv arkitekturendring enn tiltak 1/3 — påverkar eit
   grunnleggjande, fleire-stader-brukt konsept (domene = matrise-eining =
   cache-eining = nav-eining), ikkje eit isolert steg. Tilrådinga er å
   **ikkje** implementere dette no, men behalde denne profileringa slik
   at forslaget er klart til å hentast fram dersom tiltak 1 åleine ikkje
   er nok i praksis (særleg for køyringar med reelt innhaldsendring, der
   tiltak 1 sin site-cache ikkje hjelper — sjå "Realistisk forventa
   resultat").

   **Beslekta, separat gjennomført tiltak (ikkje del av denne specen):**
   Rotårsak (a) over (fleire aktive generatorar per skjema) er sidan
   redusert direkte for dei 7 `enhetsregisteret-*`-modellane — talet på
   aktive generatorar for desse er kutta frå 13 til 8
   (`json_schema`, `xsd`, `erdiagram`, `docs`, `plantuml`, `owl`, `shacl`,
   `rdf`), etter eksplisitt brukarinstruks, ikkje som ei direkte
   oppfølging av splittingsforslaget. Sjå commit-historikken for
   `src/linkml/oreg/enhetsregisteret-*/build.yaml` — dette reduserer
   truleg noko av gapet mot `ap-no`/`fint` for Fase 1-steg som `python`,
   `jsonld-context`, `proto`, `graphql` og `openapi` (no av for desse
   7 modellane), men er ikkje målt i CI enno.

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
  (cache bommar korrekt). Med tiltak 3 (implementert) og tiltak 2 (profilert,
  **ikkje** implementert — sjå kompleksitetsvurderinga over) realistisk
  anslag **~305-330 s** dersom tiltak 2 seinare vert implementert, elles
  uendra ~330-350 s. Framleis over/nær 5 min-målet. Å kome trygt under
  5 min for **alle** køyringar (inkludert reelle innhaldsendringar) krev
  truleg tiltak 4 (søk-innsnevring) eller ein meir djuptgåande
  arkitekturendring (tiltak 5) — begge eksplisitt sett på vent.

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
- [x] Tiltak 2: profilering av `generate / oreg` dokumentert (CI-jobbloggar
      for alle 9 domene, Fase 1/2-steg-for-steg), konkret splittingsforslag
      og kompleksitetsvurdering skriven — **sjølve splittinga ikkje
      implementert**, tilrådd venta til tiltak 1 er målt i praksis
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

## Utført (delvis — tiltak 1, 2 (profilering), 3)

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

**Tiltak 2 (profilering av `generate / oreg`):**
- Henta CI-jobbloggane for alle 9 `generate / <domain>`-jobbar frå
  køyring 32716167174 (`gh api repos/{owner}/{repo}/actions/jobs/<id>/logs`
  — `gh run view --log` returnerte tomt for matrisejobbar, truleg pga.
  loggstorleik/paginering) og trekte ut `run-domain-pipeline.sh` sin
  `print_pipeline_summary()`-blokk (Fase 1/2-steg-for-steg-tid) for kvar.
- Kryssjekka `generators:`-blokka i alle `build.yaml` på tvers av alle 9
  domene (`grep -A20 "^generators:"`) for å stadfeste at `oreg` har
  vesentleg fleire aktive generatorar per skjema enn andre domene.
- Identifiserte tre samverkande rotårsaker (fleire aktive generatorar,
  iboende skjemakompleksitet stadfesta via det generatorflagg-uavhengige
  `merge`/`validate`-steget, og CPU-metting frå 12 throttling-lause
  parallelle batch-kall) — sjå fullt utfylt "Tiltak 2" over.
- Skreiv eit konkret, men **ikkje implementert**, forslag (del `oreg` i to
  matrise-einingar) med eit eksplisitt kompleksitets-/kostnadsresonnement
  (`discover-domains` er brukt som sannkjelde av 4+ andre delar av
  pipelinen — `generate`- og `valider-og-analyser`-matrisene, cache-nøklar,
  `merge-generated-artifacts`, mkdocs nav-generering — så ei splitting
  krev å utvide dette konseptet, ikkje berre leggje til éin jobb).
- **Ikkje implementert:** sjølve splittinga av `oreg`-domenet. Tilrådd
  venta til tiltak 1 sin faktiske CI-gevinst er stadfesta (sjå
  "Realistisk forventa resultat").

**Attverande (ikkje implementert):**
- Tiltak 2 (sjølve splittinga av `generate / oreg`) — profilert og
  konkretisert, men medvite venta (sjå over).
- CI-tidsbruk før/etter for tiltak 1 — krev ei faktisk workflow-køyring.

Specen vert verande i `specs/backlog/` til tiltak 2 er vurdert/utført og
CI-tidsbruken for tiltak 1 er stadfesta.
