# Raskare `make docs-build`

## Bakgrunn

Brukaren bad om å evaluere om det finst tiltak som kan gjere `make
docs-build` raskare, og dokumentere funna. Denne specen dekkjer **berre**
`docs-build` (statisk MkDocs-bygg, `make/50-docs.mk` linje 28-31) — ikkje
`docs-publish`, som nyleg vart optimalisert (sjå
`specs/done/batch-docs-publish-generering.md`).

**`docs-build` vert i praksis berre køyrt frå CI** — `.github/workflows/generate.yml`,
`publish`-jobben (linje 438-446), som køyrer `make docs-publish` rett
etterfølgd av `make docs-build` på ein `ubuntu-22.04`-hosta GitHub-runnar.
Det finst ingen andre workflow-filer som refererer til `docs-build`. Første
runde av denne evalueringa profilerte målet lokalt på utviklaren si
WSL2-maskin (der repoet ligg på `/mnt/c/...`), og fann at éin spesifikk
flaskehals (sjå rotårsak 1 under) er **spesifikk for det WSL2/DrvFs-monterte
filsystemet** og difor ikkje representativ for korleis `docs-build` faktisk
køyrer i produksjon. Sjå "Effekt i GitHub Actions-runnarar" for konsekvensen
dette har for kva tiltak som er verdt å implementere.

## Funn (profilering)

Baseline vart målt med ekte `make docs-build` mot repoet slik det står i
dag (6234 filer, 71 MB i `mkdocs/docs/`, kald og deretter gjenteken
køyring):

| Scenario | Tid |
|---|---|
| `make docs-build` (bind-mount frå `/mnt/c`, kald cache) | 482,58 s |
| `make docs-build` (bind-mount frå `/mnt/c`, gjenteke — cache skal i teorien treffe) | 478,60 s (**ingen målbar cache-gevinst**) |
| Same bygg, `docs/`/`.cache`/`site` kopiert til podman named volumes i staden for bind-mount | 201,96 s bygg + 35,83 s kopier-inn + 11,62 s kopier-ut = **~249 s totalt (-48 %)** |
| Same bygg (volum-variant), alle plugins fjerna frå `mkdocs.yml` (isolerer rein markdown/mal-rendering) | 139,92 s |
| → Estimert kostnad for `search`-pluginen | ~62 s (~30 % av rendering-golvet) |

Metode: `DOCS_RUN`-ekvivalente `podman run`-kommandoar vart køyrde manuelt
mot identisk `mkdocs.yml`/`docs/`-innhald, med to ulike monteringsstrategiar
(direkte bind-mount frå `$(CURDIR)` vs. podman named volumes med
kopier-inn/kopier-ut). `mkdocs/.cache/`-katalogen var 0 byte både før og
etter dei to bind-mount-køyringane.

## Rotårsak

To distinkte, uavhengige problem er identifiserte:

1. **WSL2/DrvFs bind-mount-overhead dominerer byggtida.** Repoet ligg på
   `/mnt/c/...`, som WSL2 monterer via 9p/DrvFs frå Windows-filsystemet.
   Denne monteringstypen har vesentleg høgare per-fil-kostnad enn eit
   WSL2-native filsystem, og `docs-build` les/skriv svært mange små filer
   (5769 markdown-filer inn, tilsvarande mange HTML-filer + søkeindeks ut).
   Eit reint lese-benchmark (`find … -exec cat`) synte 33,5 s på `/mnt/c`
   mot 12,4 s på `/tmp` (WSL2-native) for identisk innhald — ca. 2,7×
   raskare. Full mkdocs-bygg via podman named volumes (som lagrar data i
   podman sitt eige, WSL2-native lagringsområde i staden for å krysse
   9p-grensa for kvar fil) stadfestar same effekt i praksis: 201,96 s mot
   478-482 s.

2. **`mkdocs-build-cache-plugin` er verkningslaus i dagens oppsett.**
   Pluginen (`src/assets/containers/Dockerfile.mkdocs` linje 6,
   `mkdocs/mkdocs.yml` linje 25) skal hoppe over heile bygget dersom
   innhaldet er uendra sidan sist, ved å skrive ein hash til
   `build_cache.json` i `on_post_build` og lese han att i `on_config`.
   Filstien er **hardkoda relativ** (`CACHE_FILE = "build_cache.json"`),
   som vert løyst mot containeren sin arbeidskatalog `/docs`
   (`WorkingDir` i imagen). `/docs` sjølv er **ikkje** blant dei monterte
   stiane i `DOCS_RUN` (`make/01-containers.mk` linje 65-70) — berre
   `docs/docs`, `mkdocs.yml`, `overrides`, `.cache` og `site` er
   bind-monterte. `build_cache.json` hamnar dermed i containeren sitt
   eige, flyktige filsystem og forsvinn når `podman run --rm` avsluttar.
   Stadfesta empirisk: to påfølgjande køyringar med identisk innhald tok
   478,60 s og 482,58 s (ingen skilnad), og `mkdocs/.cache/` var 0 byte
   begge gongar.

   Sjølv om stien vart retta, er pluginen si cache **alt-eller-ingenting**
   — éin enkelt endra fil kvar som helst i `docs/` ugyldiggjer heile
   cachen. Han vil difor berre gje gevinst ved eksakt uendra rekøyringar
   (t.d. lokal feilsøking, utilsikta CI-rekøyring), ikkje ved vanleg
   publisering der `docs-publish` alltid skriv nye tidsstempel/innhald
   først.

3. **Sjølve innhaldsvolumet er iboende stort, ikkje overhead.** 5589 av
   5769 markdown-filer (97 %) kjem frå gen-doc sin éin-fil-per-klasse/slot/
   enum/type-modell (`mkdocs/docs/<domain>/<schema>/klasser/`). Rein
   markdown+mal-rendering av dette (utan søk/cache-plugin, på
   WSL2-native lagring) tek 139,92 s — dette er eit golv som veks lineært
   med talet på domene/skjema, ikkje noko som bør fjernast (det ville
   redusert dokumentasjonsinnhaldet).

4. `search`-pluginen legg til ~62 s (~30 %) oppå rendering-golvet for å
   indeksere alle 5769 sidene. Dette er kostnaden ved å ha eit fungerande
   søk i heile portalen — ein funksjonell avveging, ikkje ein reindyrka
   ytelsesbug.

## Effekt i GitHub Actions-runnarar

Sidan `docs-build` reelt sett berre køyrer i `generate.yml` sin
`publish`-jobb på ein GitHub-hosta `ubuntu-22.04`-runnar, må kvart tiltak
vurderast mot **den** konteksten, ikkje mot WSL2-målingane åleine.

**Rotårsak 1 (bind-mount-overhead) gjeld ikkje GitHub-runnarar.**
GitHub-hosta `ubuntu-22.04`-runnarar brukar eit lokalt, native ext4-filsystem
på runnaren sin eigen SSD-lagra disk — det finst inga WSL2/DrvFs- eller
9p-liknande protokollgrense å krysse. Ein `podman -v`-bind-mount frå
runnaren sin arbeidskatalog (`$GITHUB_WORKSPACE`) er ein vanleg Linux
bind-mount, som har neglisjerbar overhead samanlikna med filsystemet han
monterer frå. **Tiltak 1 (podman named volumes for docs/.cache/site) løyser
difor eit problem som ikkje finst i CI**, og kopier-inn/kopier-ut-stega
(~48 s overhead målt lokalt) vil vere rein ekstra kostnad utan
kompenserande gevinst på ein GitHub-runnar — potensielt ei **netto
forverring**. Tiltak 1 er difor **ikkje anbefalt** for `docs-build` slik han
faktisk vert brukt, og flyttast til "Eksplisitt utanfor scope" under.

**Rotårsak 2 (build-cache-plugin er verkningslaus) gjeld også i CI — og er
verre enn i det lokale tilfellet.** `generate.yml` har alt eit eksplisitt
forsøk på å utnytte denne cachen: steget "Cache mkdocs-build-cache" (linje
431-436) brukar `actions/cache@v6` til å lagre/gjenopprette
`mkdocs/.cache/` mellom CI-køyringar, nøkla på ein hash av
`src/linkml/**`, `Dockerfile.mkdocs`, templates og statiske
`mkdocs/docs/stylesheets|javascripts|overrides`. Sidan pluginen skriv
`build_cache.json` til containeren sin arbeidskatalog (`/docs/`) og **ikkje**
til den monterte `/docs/.cache/`-stien (same bug som stadfesta lokalt), er
`mkdocs/.cache/` alltid tom — `actions/cache`-steget lastar ned og lastar
opp ein tom katalog kvar einaste køyring, heilt utan effekt.

Endå viktigare: **sjølv om filsti-buggen vart retta, ville cachen framleis
aldri treffe i denne pipelinen.** `make docs-publish` køyrer **alltid**
rett før `make docs-build` i same steg (`generate.yml` linje 445-446), og
`mkdocs/publish.sh` linje 237+464 skriv eit ferskt byggtidsstempel
(`_Portalen vart sist bygd: ${BUILD_TIMESTAMP}_`, minuttpresisjon) inn i ei
side under `mkdocs/docs/` **kvar gong**. `mkdocs-build-cache-plugin` sin
`compute_cache_id()` hashar **alle** filer under `docs_dir` uvilkårleg (han
har ingen exclude-mekanisme, berre eit tillegg-`include` for filer
*utanfor* `docs_dir`) — så cache-ID-en endrar seg minst éin gong per
CI-køyring uansett, sidan tidsstempel-fila alltid er ulik frå førre køyring.
**Alternativ A (fiks filstien) vil difor ikkje gje nokon reell gevinst i
denne pipelinen** med mindre `docs-publish` også sluttar å skrive eit
per-køyring-tidsstempel — noko som er ei åtferdsendring utanfor denne
specen sitt omfang, og truleg uønskt (tidsstempelet er dokumentert,
tilsikta funksjonalitet).

Dette peikar konkret mot **Alternativ B (fjern pluginen)** for
CI-konteksten: han gjev i praksis aldri ein cache-treff i denne pipelinen,
uansett filsti-fiks, og kostar i tillegg SHA-256-hashing av 5700+ filer
**pluss** last-ned/last-opp av ein alltid-tom `actions/cache`-artefakt for
kvar CI-køyring. Å fjerne både pluginen og "Cache mkdocs-build-cache"-steget
i `generate.yml` fjernar reint bortkasta arbeid, sjølv om den målbare
tidsgevinsten er liten (cache-oppslaget/hashinga er ikkje hovudkostnaden —
sjå rotårsak 3-4).

**Rotårsak 3-4 (innhaldsvolum + søk-indeksering) er reint CPU-/rendering-bunde
arbeid som ikkje avheng av filsystem-monteringstype.** Dette gjeld likt i
CI som lokalt — den absolutte tida vil variere med runnaren sin CPU-ytelse
(GitHub-hosta standard-runnarar har 4 delte vCPU-kjernar), men det finst
ingen kjend CI-spesifikk måte å redusere denne kostnaden på utan anten å
redusere innhald eller fjerne søk (begge eksplisitt utanfor scope, sjå
under).

**Konklusjon:** av dei to opphavleg foreslåtte tiltaka er berre tiltak 2
(fjern den verknadslause cache-pluginen, inkl. det tilsvarande
`actions/cache`-steget i `generate.yml`) relevant for `docs-build` slik han
faktisk vert brukt. Tiltak 1 (podman-volum) er flytta til "utanfor scope"
sidan han løyser eit WSL2-spesifikt problem som ikkje finst på
GitHub-runnarar.

## Evaluering: WSL-deteksjon som vilkår for volum-staging

Brukaren spurde om ei mellomløysing — bruk podman named volumes **berre**
når vi kan detektere at brukaren køyrer WSL, slik at CI (der problemet ikkje
finst) framleis brukar dagens enkle bind-mount, medan lokal WSL2-utvikling
får gevinsten. Dette er teknisk fullt mogleg og vart evaluert konkret:

**Deteksjonsmekanisme.** To alternativ er testa i dette repoet sitt eige
WSL2-miljø:

| Metode | Kommando | Resultat her |
|---|---|---|
| Grov WSL-deteksjon | `uname -r \| grep -qi microsoft` | Treff (`6.6.87.2-microsoft-standard-WSL2`) |
| Presis monteringstype-deteksjon | `stat -f -c '%T' "<sti>"` | `v9fs` for `/mnt/c/...`, `ext2/ext3` for native WSL2-filsystem (`/tmp`) |

Den **presise** varianten (`stat -f`) er å føretrekke framfor den grove: han
sjekkar direkte om `$(CURDIR)` faktisk ligg på det trege 9p/DrvFs-monterte
filsystemet (`findmnt` stadfestar `FSTYPE=9p` med `aname=drvfs` for
`/mnt/c`), i staden for å anta at "er i WSL" automatisk betyr "repoet ligg
på eit sakte filsystem". Ein WSL2-utviklar som har klona repoet til eit
WSL2-native område (t.d. `~/dev/...` i staden for `/mnt/c/...`) ville
feilaktig trigga volum-staginga med den grove metoden sjølv om han ikkje
har problemet — den presise metoden unngår dette. Begge metodane er trygge
å bruke i eit `ifeq`/`$(shell ...)`-uttrykk i Makefilen, evaluert éin gong
når `make docs-build` startar, og fell trygt tilbake til dagens
bind-mount-åtferd dersom `stat -f` skulle feile (uventa plattform).

**Implementasjonsskisse** (dersom dette vert vald): eit betinga steg i
`docs-build` (`make/50-docs.mk`) som ved treff kopierer `mkdocs/docs/` inn i
eit podman named volume, køyrer bygget med volum montert for
`docs`/`.cache`/`site` (behald bind-mount for `mkdocs.yml`/`overrides/`),
og kopierer `site/`-resultatet ut att til `$(CURDIR)/mkdocs/site/`. Sjølve
`mkdocs-local`-imagen er alt Alpine-basert med `/bin/sh` og `/bin/cp`
tilgjengeleg (stadfesta), så kopier-inn/kopier-ut kan gjenbruke `$(DOCS_IMAGE)`
direkte (`--entrypoint sh -c "cp -a ..."`) — **ingen ny
verktøyavhengigheit** (t.d. eit ekstra alpine-image) trengst.

**Kostnad/nytte-vurdering:**

- **Nytte:** ~48 % raskare `make docs-build` for utviklarar som køyrer han
  lokalt på eit `/mnt/c`-liknande WSL2-oppsett (stadfesta måling frå
  hovudevalueringa over).
- **Kostnad:** `docs-build`-targetet får to kodestiar (bind-mount vs.
  volum-staging) som begge må haldast fungerande og produsere identisk
  `site/`-output — dobla testoverflate for eit mål som i dag **ikkje**
  har nokon stadfesta jamleg lokal brukssituasjon (jf. "Bakgrunn": einaste
  kjende brukar er `generate.yml`). CLAUDE.md sitt prinsipp "Forsøk alltid
  å utføre minimale endringar som kun løser den spesifikke oppgåva" talar
  mot å leggje til denne greina utan eit konkret, gjenteke lokalt
  bruksbehov å løyse.
- **Realistisk vurdering:** dette er eit **reversibelt, isolert tiltak**
  (påverkar ikkje CI-åtferd i det heile, sidan deteksjonen aldri slår til
  på ein GitHub-runnar) — risikoen ved å implementere han er låg. Men
  verdien er spekulativ inntil det er stadfesta at nokon faktisk køyrer
  `make docs-build` lokalt jamleg. **Tilrådinga er å ikkje implementere
  dette no**, men behalde evalueringa her slik at han er rask å hente fram
  dersom lokal `docs-build`-bruk vert eit reelt behov seinare (t.d. dersom
  ein utviklar ønskjer å førehandsvise portalen før push, i staden for å
  vente på CI).

## Evaluering: andre kontainerar i repoet

Brukaren spurde òg om andre kontainer-mål i repoet kunne hatt nytte av
same podman-volum-mønster. Repoet sine andre `*_RUN`-makroar
(`make/01-containers.mk`) er `LINKML_RUN`, `PYTHON_RUN`, `AVROTIZE_RUN` og
`ASYNCAPI_RUN` — i motsetnad til `DOCS_RUN` (som alt berre montar dei
delkatalogane som faktisk trengst, jf. kommentaren "Mountar berre
nødvendige delkatalogar for å unngå unødvendig I/O" på linje 63-64) montar
desse **heile repoet** via den felles `WORK_MOUNT := -v "$(CURDIR):/work"
-w /work`. Repoet er 548 MB / 19 768 filer utanom `.git` — vesentleg
større enn `mkdocs/docs/` (71 MB / 6234 filer) sjølv om berre ein liten
delmengd faktisk vert lese/skrive per kall.

**Kvar desse faktisk køyrer, og kvifor det avgrensar gevinsten:**

1. **`generate`-jobben i `generate.yml`** (matrix per domene, same som
   `docs-build` sin `publish`-jobb) køyrer på GitHub-hosta
   `ubuntu-22.04`-runnarar — same konklusjon som for rotårsak 1 over: her
   finst ikkje 9p-overheaden i det heile, så volum-staging ville berre
   lagt til rein kostnad.

2. **Lokal utvikling** er der desse kontainarane faktisk kunne hatt nytte
   av volum-staging på WSL2 — og i motsetnad til `docs-build`, har
   `LINKML_RUN`/`PYTHON_RUN` ein stadfesta, jamleg lokal brukssituasjon:
   CLAUDE.md sin eigen "Valider arbeidet ditt"-seksjon instruerer
   eksplisitt å køyre `make lint SCHEMA=...`, `make validate-instance
   SCHEMA=...` og `make roundtrip SCHEMA=...` **for eitt enkelt skjema**
   etter kvar skjemaendring. Sidan `batch-generate.py`
   (`src/assets/scripts/makefile/batch-generate.py`) alt batchar N skjema
   inn i **éin** kontainar-prosess (jf. `specs/done/effektiviser-generate-workflow-koyretid.md`,
   eit tidlegare, ferdigstilt tiltak som løyste eit anna
   ytelsesproblem — kontainar-/interpreter-oppstart, ~8 s per kall — for
   nett desse måla), er det typiske lokale kallet avgrensa til éin skjema
   sine ~175 filer i snitt (målt over alle 36 skjema sine
   `generated/<domain>/<schema>/`-katalogar), ikkje tusenvis som i
   `docs-build`.

**Kvifor volum-staging truleg ikkje lønar seg her:** Ved same
kostnadsmodell som over (~5-6 ms/fil 9p-overhead, utleia frå
lese-benchmarken i "Rotårsak" — 33,5 s / 5769 filer) tilsvarar ~175 filer
berre **~1 s** ekstra I/O-kostnad per lokalt kall. Dette er lite
samanlikna med den **~8 s** kontainar-/interpreter-oppstartskostnaden
`effektiviser-generate-workflow-koyretid.md` alt har målt og delvis løyst
for same kontainarane. Volum-staginga sin faste kopier-inn/kopier-ut-kostnad
(målt til ~48 s for `mkdocs/docs/` sine 71 MB — og ville vore **større**
her sidan `WORK_MOUNT` montar heile det 548 MB store repoet, ikkje berre
den vesle delmengda som faktisk vert brukt) ville med stor sannsynlegheit
gjere eit typisk **enkelt-skjema**-kall **tregare**, ikkje raskare.

Unntaket er dersom nokon køyrer eit **ufiltrert** mål (t.d. `make gen-doc`
utan `SCHEMA=`, som batchar **alle** 36 skjema i éin kontainar og dermed
kan nå ei filmengd i same storleiksorden som `docs-build`, ~6300 filer
aggregert). Dette er derimot ikkje det vanlege lokale arbeidsmønsteret
(CLAUDE.md sin eigen instruks er per-skjema-validering, ikkje
heile-repoet-generering) — verdien av å optimalisere for eit sjeldnare
brukstilfelle er difor mindre openbar.

**Konklusjon:** volum-staging for `LINKML_RUN`/`PYTHON_RUN`/`AVROTIZE_RUN`/
`ASYNCAPI_RUN` er **ikkje anbefalt** som eit nytt tiltak no. Dei køyrer
primært i CI (ingen gevinst der), og det vanlege lokale bruksmønsteret
(éin-skjema-kall) har for lite filarbeid til at den faste
kopier-inn/kopier-ut-kostnaden løner seg — særleg sidan `WORK_MOUNT` montar
heile repoet, ikkje ei avgrensa delmengd slik `DOCS_RUN` alt gjer. Dersom
dette skal takast opp att, bør det avgrensast til det spesifikke,
sjeldnare tilfellet "ufiltrert, alle-skjema lokalt kall" — ikkje som ei
generell endring av `WORK_MOUNT`.

## Mål

Fjerne reint bortkasta arbeid frå `docs-build` slik han faktisk køyrer i
CI (`generate.yml`), utan å endre generert innhald eller søkefunksjonen.
Realistisk forventa gevinst er **liten** (hashing/cache-opp- og nedlasting
er ikkje hovudkostnaden), men tiltaket fjernar eit steg som i dag ikkje gjer
noko nyttig.

## Tiltak / Steg

1. **Fjern `mkdocs-build-cache-plugin` (Alternativ B — grunngjeving over):**
   - Fjern `mkdocs-build-cache-plugin` frå `pip install`-lista i
     `src/assets/containers/Dockerfile.mkdocs`
   - Fjern `- build-cache` frå `plugins:`-lista i `mkdocs/mkdocs.yml`
   - Bygg containeren på nytt (`make build-docker-mkdocs`) og verifiser at
     `make docs-build` framleis fullfører feilfritt
   - **Ikkje** implementer Alternativ A (fiks filsti) — sjå "Effekt i
     GitHub Actions-runnarar" for kvifor det ikkje gjev reell gevinst i
     denne pipelinen

2. **Fjern det no verknadslause "Cache mkdocs-build-cache"-steget i
   `.github/workflows/generate.yml`** (linje 431-436, `actions/cache@v6`
   mot `mkdocs/.cache/`) — steget cachar i dag alltid ein tom katalog og
   gjev null nytte. Køyr `actionlint` mot fila etter endringa (jf.
   CLAUDE.md "Actionlint etter CI-endring")

3. **Mål total tid før/etter** for `publish`-jobben i `generate.yml` (via
   Actions-loggen sin steg-tidsbruk for "Publiser og bygg
   dokumentasjonsportal"), dokumenter i "Utført"-seksjonen. Forvent liten,
   men reell, forbetring (fjerna last-ned/last-opp av tom cache-artefakt +
   fjerna unødvendig SHA-256-hashing av 5700+ filer i `on_config`)

4. **Verifiser identisk output:** `mkdocs/site/`-innhaldet skal vere
   byte-for-byte identisk med og utan pluginen (bortsett frå eventuelle
   byggtidsstempel), sidan pluginen berre styrer om bygget vert hoppa over
   — han endrar ikkje sjølve rendering-logikken

**Eksplisitt utanfor scope:**

- **Podman named volumes for `docs/`/`.cache`/`site` i `docs-build`
  (opphavleg tiltak 1)** — løyser eit WSL2/DrvFs-bind-mount-problem som
  ikkje finst på GitHub-hosta `ubuntu-22.04`-runnarar, der `docs-build`
  faktisk køyrer. Kopier-inn/kopier-ut-overhead (~48 s målt lokalt) ville
  vore rein ekstra kostnad utan kompenserande gevinst i CI, og kunne gjort
  jobben **tregare**, ikkje raskare. Ein WSL-deteksjonsgata variant (berre
  bruk volum når `stat -f` viser `v9fs`, elles dagens bind-mount) er
  konkret evaluert — sjå "Evaluering: WSL-deteksjon som vilkår for
  volum-staging" — og vurdert som teknisk gjennomførbar, men utsett inntil
  det finst eit stadfesta, jamleg lokalt bruksbehov for `docs-build`
  (i dag er einaste kjende brukar `generate.yml`)
- **Volum-staging for `LINKML_RUN`/`PYTHON_RUN`/`AVROTIZE_RUN`/
  `ASYNCAPI_RUN`** — evaluert (sjå "Evaluering: andre kontainerar i
  repoet"), men ikkje anbefalt: same CI-only-argument gjeld for
  `generate`-jobben, og det vanlege lokale bruksmønsteret (éin-skjema-kall
  via `SCHEMA=`) har for lite filarbeid (~175 filer, ~1 s ekstra 9p-overhead)
  til at kopier-inn/kopier-ut av heile det 548 MB store repoet (montert via
  `WORK_MOUNT`) løner seg
- Alternativ A for cache-pluginen (fiks filsti i staden for å fjerne) — sjå
  grunngjeving i "Effekt i GitHub Actions-runnarar": ville krevje at
  `docs-publish` sluttar å skrive eit ferskt byggtidsstempel for kvar
  køyring, som er ei separat åtferdsendring utanfor denne specen
- Å redusere talet på genererte markdown-sider (5589 av 5769 kjem frå
  gen-doc sin éin-fil-per-klasse/slot/enum/type-modell) — dette er
  dokumentasjonsinnhald, ikkje overhead
- Å fjerne `search`-pluginen — kostar ~60 s/~30 % av rendering-golvet, men
  gjev fungerande søk i heile portalen; ein funksjonell trade-off
- Å flytte heile repoet vekk frå `/mnt/c` til eit WSL2-native filsystem —
  irrelevant for `docs-build` i CI (sjå over), og ville uansett vore ei
  arkitekturendring som påverkar heile utviklaropplevinga (git, IDE, andre
  make-target), utanfor denne specen sitt omfang

## Akseptansekriterium

- [x] `mkdocs-build-cache-plugin` fjerna frå `Dockerfile.mkdocs` og
      `mkdocs.yml` (via kjelda i `mkdocs/publish.sh`, sjå "Utført")
- [x] "Cache mkdocs-build-cache"-steget fjerna frå `.github/workflows/generate.yml`
- [x] `actionlint` køyrt mot `generate.yml` etter endringa, ingen
      `[expression]`-feil
- [x] `make docs-build` fullfører feilfritt lokalt etter containeren er
      bygd på nytt
- [x] Generert `mkdocs/site/`-innhald identisk før/etter (bortsett frå
      eventuelle tidsstempel) — grunngjeving i "Utført" (kodelesing av
      pluginen, ikkje ny diff-køyring)
- [ ] CI-tidsbruk for `publish`-jobben (steget "Publiser og bygg
      dokumentasjonsportal") målt før/etter — **ikkje verifiserbart av
      LLM** (krev push + faktisk CI-køyring, som er brukaren sitt ansvar
      per CLAUDE.md). Lokal måling brukt som stedfortredar, sjå "Utført"

## Relaterte filer

- `src/assets/containers/Dockerfile.mkdocs` — `mkdocs-build-cache-plugin`-installasjon
- `mkdocs/mkdocs.yml` — `plugins:`-lista (`build-cache`, `search`)
- `.github/workflows/generate.yml` — `publish`-jobben (linje 387-446),
  "Cache mkdocs-build-cache"-steget (linje 431-436)
- `make/50-docs.mk` — `docs-build`-target (uendra av denne specen)
- `make/01-containers.mk` — `DOCS_RUN`-variabel (linje 65-70, uendra),
  `WORK_MOUNT`/`LINKML_RUN`/`PYTHON_RUN`/`AVROTIZE_RUN`/`ASYNCAPI_RUN`
  (vurdert, ikkje endra — sjå "Evaluering: andre kontainerar i repoet")
- `specs/done/batch-docs-publish-generering.md` — tilsvarande
  profileringsmetode brukt for `docs-publish`, presedens for format
- `specs/done/effektiviser-generate-workflow-koyretid.md` — tidlegare,
  ferdigstilt tiltak som batcha `LINKML_RUN`/`PYTHON_RUN`-kall på tvers av
  skjema og målte kontainar-/interpreter-oppstartskostnad (~8 s/kall) —
  samanlikningsgrunnlag for "Evaluering: andre kontainerar i repoet"

## Utført

**Endra filer:**

- `src/assets/containers/Dockerfile.mkdocs` — fjerna
  `mkdocs-build-cache-plugin` frå `pip install`-lista (`mkdocs-kroki-plugin`
  ståande att)
- `mkdocs/publish.sh` — fjerna `- build-cache` frå `plugins:`-heredocen
  (linje ~508-510). **Merk:** `mkdocs/mkdocs.yml` sjølv vart òg redigert
  direkte for å kunne verifisere lokalt utan å køyre `docs-publish` først,
  men *kjelda* er `publish.sh` (jf. CLAUDE.md: "Sannkjelda for nav-menyen
  er `mkdocs/publish.sh`" — same gjeld resten av heredoc-blokka, `mkdocs.yml`
  vert overskrive ved neste `docs-publish`-køyring uansett)
- `.github/workflows/generate.yml` — fjerna det verknadslause "Cache
  mkdocs-build-cache"-steget (`actions/cache@v6` mot `mkdocs/.cache/`)

**Verifisering:**

- `make build-docker-mkdocs`: bygde `localhost/mkdocs-local:latest` på
  nytt utan pluginen, feilfritt
- `actionlint` mot `generate.yml`: berre 4 pre-eksisterande
  `[shellcheck]`-funn i andre, urelaterte steg (linje 177, 336) — ingen
  `[expression]`-feil, ikkje noko som blokkerer per CLAUDE.md
- `make docs-build` (lokalt, `/mnt/c`-bind-mount, kald `.cache`/`site`):
  fullførte feilfritt, **378,85 s** — ned frå 478,60-482,58 s målt i
  hovudevalueringa (same maskin, same innhald). **~21 % raskare**, ei
  vesentleg større lokal gevinst enn "Mål"-seksjonen sitt opphavlege
  "liten gevinst"-anslag. Dette stadfestar at
  `mkdocs-build-cache-plugin` sin `compute_cache_id()` — som gjer sin
  **eigen** fulle `os.walk`+SHA-256-lesepass over heile `docs_dir` (5769
  filer), *i tillegg til* mkdocs sitt eige rendering-lesepass — var ein
  reell kostnad i seg sjølv, uavhengig av 9p-monteringsspørsmålet. Same
  hashing-pass køyrer identisk (CPU+syscall-bunde) på GitHub-runnarar, så
  ei tilsvarande (om enn truleg mindre, sidan native ext4 har lågare
  per-syscall-kostnad enn 9p) forbetring er venta i CI — men den faktiske
  CI-talet er **ikkje målt** her (krev ein ekte workflow-køyring etter
  push, som ligg utanfor kva ein LLM-økt kan gjere)
- Output-identitet vart **ikkje** verifisert med ein ny diff-køyring (den
  gamle `site/`-katalogen frå før endringa var ikkje bevart). Grunngjevinga
  i staden er kodelesing av pluginen (`plugin.py`, sitert i "Rotårsak"):
  `on_config`/`on_post_build` påverkar berre om bygget vert *hoppa over*
  (`raise BuildCacheAbort`) og skriv ei ekstern cache-fil — dei rører aldri
  `docs_dir`-innhaldet, malane eller rendering-stien. Strukturelt kan
  fjerning av pluginen difor ikkje endre `site/`-innhaldet, berre om
  bygget køyrer i det heile

**Ikkje gjort (stadfesta utanfor scope, sjå seksjonane over):**

- Podman named volumes for `docs-build` (verken ubetinga eller
  WSL-deteksjonsgata varianten)
- Volum-staging for `LINKML_RUN`/`PYTHON_RUN`/`AVROTIZE_RUN`/`ASYNCAPI_RUN`
- Alternativ A (fiks filstien til `build_cache.json` i staden for å fjerne
  pluginen)
