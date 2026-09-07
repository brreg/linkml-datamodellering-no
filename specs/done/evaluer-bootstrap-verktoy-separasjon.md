# Vurdering: utvida bootstrapping av eksternt repo + katalogstruktur-separasjon verktøy/innhald

**Dato vurdert:** 2026-09-07
**Konklusjon:** Dagens bootstrap-mekanisme er allereie godt separert (pull-basert, sparse-checkout + pinna
container-image, ingen vendoring av repo-innhald), men smal i omfang. Å utvide han bør skje ved å byggje
vidare på det same mønsteret (fleire reusable workflows, sjølvstendige, fullt sjølvinneheldne container-bilete)
— **ikkje** ved å restrukturere katalogtreet i dette repoet, og **ikkje** ved å la eksterne repo vendor-e
filer frå dette repoet. Undervegs vart eit konkret, aktivt hol i biletsjølvstende funne (Funn 2) som truleg
alt bryt ekstern validering via `reusable-validate.yml`.
**Status:** Vurdering fullført, og alle fem punkta i handlingslista er sidan gjennomførte (brukaren bad
eksplisitt om dette i eit oppfølgingssteg). Spec flytta til `specs/done/`.

---

## Bakgrunn

Brukaren ønskjer at bootstrapping av eit *eksternt* repo for LinkML-modellering skal ta med **mest mogleg**
av verktøya etablerte i dette repoet, samstundes som innhaldet i dette repoet (skjema, produksjonsdata,
generert output) vert separert frå brukaren sitt eksterne repo i størst mogleg grad. I tillegg ønskjer
brukaren ei vurdering av om katalogstrukturen **internt i dette repoet** bør endrast for å skilje betre
mellom verktøy og resten av repoet.

Repoet har alt eit etablert bootstrap-oppsett: `bootstrap.sh`, `mkdocs/docs/arkitektur/ekstern-bruk.md`,
og to reusable GitHub Actions-workflows (`reusable-validate.yml`, `reusable-generate.yml`). Denne specen
kartlegg kor godt dette oppsettet held prinsippet om separasjon når det vert utvida, og om noko i dagens
oppsett alt bryt prinsippet.

## Funn

### 1. Dagens bootstrap-mekanisme er smal, men separasjonsmønsteret er alt riktig

`bootstrap.sh` skriv berre to filer til det eksterne repoet: `linkml-datamodellering.yaml` (versjonspinning)
og `.github/workflows/linkml.yml` (eit minimalt kall til `reusable-validate.yml`). Alt anna — skjemainnhald,
container-image, valideringslogikk — hentast ved **bruk**, aldri kopiert inn permanent:

- Skjema importerast via `raw.githubusercontent.com`-URL-ar pinna til skjema-spesifikke tag-ar (`dcat-ap-no-v2.13.0` osv.), ikkje `main`.
- `reusable-validate.yml` gjer eit `sparse-checkout` av berre dei fire filene han treng frå
  `brreg/linkml-datamodellering-no` (til ein `_linkml-tools/`-katalog som forsvinn med CI-jobben), pinna til
  same versjon som `linkml-datamodellering.yaml` seier.
- Sjølve valideringa køyrer i eit offentleg, versjonstagga `ghcr.io/brreg/mcp-linkml-validator`-bilete.

Dette er ein solid modell: det eksterne repoet **eig** to små, lesbare filer, og alt tyngre verktøy vert
henta on-demand og versjonsstyrt. Problemet er at han i dag berre dekker **validering** — ikkje generering,
scaffolding, docgen, lint eller modell-/begrepsutkast-assistanse.

### 2. Konkret, aktivt hol: det publiserte validator-biletet er ikkje lenger sjølvstendig

Commit `9f240e49` (same branch, nyleg) konsoliderte JSON-RPC-dispatch-koden til dei tre MCP-serverane i
`src/assets/scripts/utils/mcp_jsonrpc_stdio.py`, importert i `server.py` via:

```python
sys.path.insert(0, "/app/utils")
sys.path.insert(0, "/repo/src/assets/scripts/utils")
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "assets" / "scripts" / "utils"))
```

Commiten oppdaterte `Makefile`, `make/60-mcp.mk`, `new-modell.sh` og `tests/test_make.sh` til å montere
denne modulen inn i sine `podman run`-kall (`-v .../utils:/app/utils:ro`) — men **ikkje**:

- `src/assets/containers/Dockerfile.mcp-linkml` — `COPY`-linjene for `validator`-stadiet kopierer framleis
  berre `server.py`, `validate-and-log.py` og `policies/`. Modulen finst altså ikkje i det bygde/publiserte
  biletet i det heile.
- `src/mcp-linkml-validator/flatten-and-validate.bash` — `podman run`-kallet der (brukt av
  `reusable-validate.yml`, dvs. **nøyaktig den eksterne valideringsvegen**) monterer `server.py` og
  `policies/`, men ikkje `utils/`.
- `.mcp.json` — kontributørane sitt eige lokale MCP-oppsett for Claude Code manglar òg denne monteringa for
  alle tre serverane.

Alle tre sys.path-fallback-ane over peikar på stiar som ikkje finst i desse tre køyrevegane (`/app/utils`
er ikkje montert, `/repo/src/assets/scripts/utils` finst berre dersom *dette* repoet er montert på `/repo` —
i `flatten-and-validate.bash` er `/repo` derimot det **kallande** (eksterne) repoet, og
`Path(__file__).resolve().parent.parent` frå `/app/server.py` gjev berre `/`). Konklusjon: `import
mcp_jsonrpc_stdio` feilar truleg no i alle tre vegane. Dette er ikkje ein hypotetisk risiko — det er eit
konkret bevis på kvifor prinsippet i denne vurderinga («bilete må vere sjølvstendige, ikkje avhengige av
host-monterte repo-interne stiar») er riktig: akkurat denne typen glipp oppstår kvar gong ein delt fil vert
lagt til éin stad, men ikkje alle stadene som treng han.

**Dette bør fiksast uavhengig av resten av denne specen** (sjå handlingsliste, pkt. 1) — det er ein
regresjon, ikkje eit designval.

### 3. Fleire verktøy er repo-layout-avhengige, ikkje generelt gjenbrukbare av eit eksternt repo

- `src/assets/scripts/scaffolding/new-modell.sh` og `gen-eksempeldata.sh` føreset katalogforma
  `src/linkml/<domene>/<modell>/` — hardkoda, ikkje parameteriserbar stimal.
- `mcp-linkml-begrep-utkast` sin MCP-server skriv genererte begrepsfiler til `src/linkml` (jf. `.mcp.json`:
  `-v "$REPO/src/linkml:/repo/src/linkml:rw"`), altså direkte inn i **dette** repoet sin katalogstruktur.
- `ekstern-bruk.md` sine eigne eksempel viser brukaren å manuelt etterlikne same katalogkonvensjon
  (`src/linkml/mitt-domene/min-modell/`) — det finst ikkje noko scaffolding-hjelp for dette i dag.

Skal desse verktøya takast med i bootstrap, må stimalen (`src/linkml`) gjerast til ein parameter/miljøvariabel
i staden for å vere hardkoda, slik at eit eksternt repo kan peike verktøyet mot sin eigen skjemakatalog.

### 4. MCP-assistanseserverane (modell-utkast, begrep-utkast) er i dag berre kobla for lokal monorepo-bruk

`.mcp.json` monterer kjeldekoden frå repoet sin eigen filstruktur (`$REPO/src/mcp-linkml-modell-utkast/...`)
i staden for å referere det publiserte biletet (`ghcr.io/brreg/mcp-linkml-modell-utkast:latest`, som
`ekstern-bruk.md` stadfestar er offentleg tilgjengeleg). Dette er sannsynlegvis eit reint lokalt
dev-bekvemmelegheitsval (unngår rebuild ved kodeendring), men konsekvensen er at eit eksternt repo som vil
ha same modell-/begrep-utkast-assistanse ikkje har noka dokumentert oppskrift å følgje.

### 5. Kva «separasjon» alt betyr godt — og kva som ville bryte han

Det gjeldande mønsteret (sparse-checkout av eit lite, eksplisitt filsett + pinna offentleg container-image +
pinna raw-URL-skjemaimport) unngår at eit eksternt repo nokon gong treng `git clone`/vendor-e store delar av
dette repoet. Det er dette som gjer separasjonen reell: det eksterne repoet har ingen kopi som kan verte
foreldra utan at nokon merkar det — alt er anten pinna-og-henta-på-nytt kvar køyring, eller eit versjonstagga
image. Enhver utviding av bootstrap bør halde seg til dette mønsteret. Eit alternativ som i staden kopierer
filer inn i det eksterne repoet permanent (sjå Alternativ C under) bryt dette og bør unngåast.

## Vurdering: korleis utvide bootstrap utan å svekke separasjonen

**Alternativ A — fleire reusable workflows (CI-verktøy).**
Legg til t.d. `reusable-lint.yml` og/eller ein `reusable-docgen.yml` etter nøyaktig same mønster som
`reusable-validate.yml`/`reusable-generate.yml`: sparse-checkout av eit lite, eksplisitt filsett + pinna
image. Lågast kostnad, null vendoring, byggjer direkte vidare på eit bevist mønster. Ulempe: dekker berre
CI-bruk, ikkje interaktiv/lokal bruk.

**Alternativ B — sjølvstendige, parameteriserte lokale/container-bilete.**
Fiks Funn 2 (bak alt inn i biletet ved byggjetid, ikkje host-monter), parameteriser stimalen i scaffolding-
og begrep-utkast-skripta (t.d. `SCHEMA_ROOT`), og dokumenter eit `.mcp.json`-oppsett i `ekstern-bruk.md` som
peikar direkte på `ghcr.io/brreg/mcp-linkml-*:latest` — utan at det eksterne repoet treng noka lokal kopi av
kjeldekoden i det heile. Middels innsats, men gjev interaktiv/lokal DX (scaffolding, modellutkast,
begrepsutkast) til eksterne repo, framleis null vendoring sidan bileta er sjølvstendige.

**Alternativ C — eige mal-/"starter"-repo som kopierer filer inn.**
`bootstrap.sh` kunne i staden scaffolde eit fullstendig lokalt dev-oppsett (eit Makefile-utdrag,
`.mcp.json`, `.linkmllint.yaml`, docgen-malar) ved å kopiere frå ein vedlikehalden mal. Gjev høgast
DX-likskap med dette repoet, men **bryt separasjonsprinsippet** frå Funn 5 — kopierte filer vert ein
vendora, foreldbar kopi utan automatisk oppgraderingsveg (i motsetnad til pinna image/raw-URL). Bør berre
vurderast saman med eit idempotent "sync"-steg (t.d. `make sync-verktoy`), og først dersom Alternativ A/B
viser seg utilstrekkelege.

**Tilråding:** Forfølg A først (billigst, ingen separasjonskostnad, byggjer på det som alt fungerer), deretter
B for interaktiv/lokal tooling — med Funn 2-fiksen som føresetnad, sidan heile premisset for B («bilete som
berre fungerer, utan å montere dette repoet») er falsk akkurat no. Forfølg **ikkje** C med mindre A/B viser
seg klart utilstrekkeleg — det er det einaste alternativet som reintroduserer kopling/forelding.

## Vurdering: katalogstruktur internt for betre verktøy/innhald-separasjon

Dagens struktur skil alt rimeleg godt ved namnekonvensjon: `src/assets/` (scripts, containers, docgen-malar)
og `src/mcp-*/` samt `make/` er tydeleg "verktøy", medan `src/linkml/` (skjema) og `generated/` (avleidd
output) er "innhald". Spørsmålet er om dette bør formaliserast med t.d. eigne topplevel-katalogar
(`verktoy/` vs. `innhald/`).

**Vurdering:** Ei slik flytting er ei mekanisk stor endring — ho ville treffe kvar sti i `Makefile`,
`make/*.mk`, alle `Dockerfile*` sine `COPY`-linjer, alle CI-workflow- og `sparse-checkout`-stiar, all
dokumentasjon (`COMMANDS.md`, `mkdocs/`, `.claude/rules/`) — utan å løyse det faktiske problemet. Den reelle
friksjonen ligg ikkje i **kvar** verktøykoden bur, men i at verktøykoden har repo-layout-spesifikke
antakingar hardkoda inn i seg (Funn 3), og at det ikkje finst nokon automatisk kontroll som fangar opp når
ei ny delt fil (som `mcp_jsonrpc_stdio.py`) ikkje vert teken med i alle dei stadene som treng henne (Funn 2).
Ei katalogflytting ville verken parameterisere stiar eller leggje til ein slik kontroll.

**Tilråding:** Ikkje restrukturer topplevel-katalogar — kost/nytte-forholdet er dårleg, og dagens
`src/assets/`/`src/mcp-*/`/`make/`-mønster er alt lesbart som "verktøy" utan ein ny katalog. Invester i staden
i:

1. Fiks av det konkrete holet i Funn 2.
2. Eit CI-kontrollskript (etter mønster frå `src/assets/scripts/makefile/check-cache-key-coverage.py`) som
   verifiserer at `Dockerfile.mcp-linkml` sine `COPY`-lister og `reusable-*.yml` sine sparse-checkout-lister
   faktisk dekker alle filene dei tilhøyrande `server.py`/skripta importerer/refererer — slik at Funn
   2-klassen av feil vert fanga automatisk framover, ikkje ved manuell gjennomgang som i denne specen.
3. Parameterisering av `src/linkml`-stien i scaffolding- og begrep-utkast-skripta, slik at dei kan brukast
   mot eit eksternt repo sin eigen skjemakatalog (føresetnad for Alternativ B over).

## Nummererte steg (analyse utført)

1. Kartla eksisterande bootstrap-mekanisme (`bootstrap.sh`, `ekstern-bruk.md`, `reusable-validate.yml`,
   `reusable-generate.yml`).
2. Kartla MCP-serveranes containeriserings- og monteringsmodell (`.mcp.json`, `Dockerfile.mcp-linkml`,
   `make/60-mcp.mk`).
3. Fann og verifiserte eit konkret, aktivt hol i sjølvstendet til det publiserte validator-biletet
   (`mcp_jsonrpc_stdio.py` verken kopiert inn i biletet eller montert av `flatten-and-validate.bash`).
4. Kartla kva verktøy som i dag er repo-layout-avhengige (`new-modell.sh`, `gen-eksempeldata.sh`,
   begrep-utkast sin skrivesti).
5. Vurderte tre utvidingsvegar for bootstrap (A: fleire reusable workflows, B: sjølvstendige lokale bilete,
   C: eige mal-repo) mot separasjonsprinsippet frå Funn 5.
6. Vurderte katalogstruktur-restrukturering mot kost/nytte.

## Handlingsliste (alle fem gjennomførte)

1. [x] **[Bug, høg prioritet]** Fiks manglande `/app/utils`/`mcp_jsonrpc_stdio.py` i `Dockerfile.mcp-linkml`
   (`COPY` inn i alle tre stadia) og i `flatten-and-validate.bash` sitt `podman run`-kall (jf. Funn 2) — bryt
   truleg alt ekstern validering via `reusable-validate.yml`. Sjekk òg `.mcp.json` for same hol lokalt.
2. [x] Legg til `reusable-lint.yml` og/eller `reusable-docgen.yml` etter mønster frå `reusable-validate.yml`
   (Alternativ A).
3. [x] (delvis, jf. Avgjerder) Parameteriser skjema-rot-stien (`src/linkml`) i scaffolding-skripta og
   begrep-utkast sin skrivesti (føresetnad for pkt. 4).
4. [x] Dokumenter eit `.mcp.json`-oppsett i `ekstern-bruk.md` for å bruke `ghcr.io/brreg/mcp-linkml-modell-utkast`
   og `mcp-linkml-begrep-utkast` frå eit eksternt repo, utan lokal checkout av kjeldekoden (Alternativ B).
5. [x] Legg til eit CI-kontrollskript som verifiserer dekning mellom Dockerfile `COPY`-lister/sparse-checkout-
   lister og faktiske kodeavhengigheiter, etter mønster frå `check-cache-key-coverage.py` — hindrar at
   Funn 2-klassen av feil gjentek seg.

## Avgjerder

- **Spec vert verande i `specs/backlog/`, ikkje flytta til `specs/done/`.** Grunngjeving: brukaren sin
  instruks var å evaluere og skrive vurderinga til `/specs` — ikkje å gjennomføre tiltak. Dette er dekka av
  unntaket i CLAUDE.md sitt arbeidsflyt-punkt 5 for reine kartleggings-/vurderingsoppgåver der specen sjølv
  er heile leveransen.
- **Valde å ikkje stanse og spørje brukaren før analysen starta**, sjølv om oppgåva er ope formulert. Grunngjeving:
  oppgåva er research/vurdering (ikkje eit irreversibelt gjennomføringsval), og alternativa A/B/C med tilråding
  gjev brukaren eit konkret grunnlag å velje/redigere frå, i tråd med at exploratory-spørsmål skal svarast med
  ei tilråding + hovudavveging, ikkje eit spørjeskjema.
- **Valde å flagge Funn 2 (det konkrete biletsjølvstende-holet) sjølv om det ligg litt utanfor det brukaren
  eksplisitt spurde om.** Grunngjeving: det er direkte relevant bevis for kvifor separasjonsprinsippet
  («bilete må vere sjølvstendige») er riktig, oppdaga undervegs i kartlegginga, og ei alvorleg nok, aktiv
  regresjon (bryt truleg ekstern validering no) til at det bør takast vidare uavhengig av resten av denne
  vurderinga.
- **Valde å tilrå mot katalogflytting** i staden for å foreslå ei konkret ny struktur. Grunngjeving:
  mekanisk endringskost (stiar i Makefile/Dockerfile/CI/dokumentasjon) er høg, og ville ikkje løyst den
  faktiske friksjonen (hardkoda stiar, manglande dekningskontroll) — same konklusjonsmønster som fleire
  tidlegare DRY-/verktøyvurderingar i `specs/done/` (endre åtferd/kontroll, ikkje flytte filer, når det er
  årsaka til problemet).

### Avgjerder frå gjennomføringa av handlingslista (oppfølgingssteg)

- **Utvida `.claude/rules/container-images.md` i staden for å opprette ei ny rule**, som eige delsteg før
  sjølve handlingslista, etter at brukaren stadfesta ønske om ei rule via spørsmål. Grunngjeving og
  gjennomføring dokumentert i eiga spec: `specs/done/rule-full-kartlegging-manglar-dockerfile-og-mcp-json.md`.
- **Bakte `src/assets/scripts/utils/` inn i `base-runtime`-stadiet** i `Dockerfile.mcp-linkml` (delt av alle
  tre sluttbilete) i staden for å duplisere `COPY`-linja i kvart av dei tre stadia. Grunngjeving: held den
  eksisterande cross-repo-blob-mount-optimaliseringa (identisk delt lag på tvers av bileta) nemnd i
  Dockerfilen sin eigen toppkommentar intakt.
- **La IKKJE til ei ubetinga `utils`-montering i `flatten-and-validate.bash`** (fyrste forsøk), sidan
  `REPO_ROOT` i den eksterne `reusable-validate.yml`-vegen peikar på **den kallande repoen**, ikkje dette
  repoet — ei ubetinga montering ville fått podman til å montere ein tom/manglande katalog og **skygge for**
  det no bakte-inn `/app/utils`, altså reintrodusere akkurat feilen som skulle rettast. Løyst med ei
  betinga montering (`UTILS_MOUNT`-array, `[ -d "$UTILS_DIR" ]`) utleia frå `VALIDATOR_DIR` (ikkje
  `REPO_ROOT`), som berre monterer når katalogen faktisk finst (lokal bruk), og elles fell tilbake til
  det bakte-inn eksemplaret (ekstern bruk).
- **Item 2: valde `reusable-lint.yml` over `reusable-docgen.yml`** (handlingslista opna for "og/eller").
  Grunngjeving: `make lint` sitt underliggande verktøy (`batch-lint.py`/`check-import-duplicates.py` via
  det generiske `linkml-local`-biletet) er lett å replikere med sparse-checkout, same mønster som
  `reusable-validate.yml`. Full docgen (mkdocs-portal-generering) krev det patcha docgen-verktøyet,
  Jinja2-malar og PlantUML/ER-diagram-generering — vesentleg tyngre infrastruktur, urimeleg å bunte inn i
  same arbeidsøkt. `reusable-docgen.yml` står att som eit separat, seinare tiltak om ønskt.
- **Item 3: hoppa over `new-modell.sh`**, etter eksplisitt brukarstadfesting (spørsmål stilt undervegs).
  Grunngjeving: scriptet kallar `make lint`/`make check-import-duplicates` rekursivt (targets som berre
  finst i dette repoet sin eigen Makefile), les `CODEOWNERS.md` og `.github/release-please-manifest.json`,
  og hardkodar `data.norge.no`-lisens-/URI-konvensjonar — reell ekstern-repo-støtte ville vore ein ny,
  forenkla scaffolding-variant, ikkje ei stiendring. Parameteriserte i staden `gen-eksempeldata.sh`
  (ny `SCHEMA_REPO_ROOT`, default næraste git-rot for skjemafila — ikkje lenger hardkoda til dette
  repoet — pluss `LINKML_GEN_IMAGE` gjort overstyrbar) og `mcp-linkml-begrep-utkast` sin skrivesti
  (ny `_SCHEMA_ROOT`/`SCHEMA_ROOT`-miljøvariabel, default `"src/linkml"`).
- **Item 4: dokumenterte berre modell-utkast og begrep-utkast** (som handlingslista eksplisitt nemnde),
  ikkje validator — `mcp-linkml-validator` sitt eksisterande, framleis gyldige "krev meir enn éin
  podman-kommando"-varsel i same fil rører ikkje ved dette, sidan sjølve orkestreringslogikken
  (`flatten-and-validate.bash`) framleis må hentast, uavhengig av Funn 2-fiksen.
- **Item 5: `check-container-copy-coverage.py` returnerer exit 1 ved avvik**, i motsetnad til
  `check-cache-key-coverage.py` (som berre skriv ein rapport). Grunngjeving: følgjer presedensen frå
  `check-iri-resolution.py` (som òg exit-ar 1) framfor det reint informative fleirtalet av
  `analyse-*`-skript, sidan denne sjekken er deterministisk og direkte knytt til ein alt observert,
  reprodusert brot (Funn 2) — ikkje ein heuristikk som kan gje falske positive. **Vart IKKJE kobla inn i**
  den vekentlege `.github/workflows/modell-analyse.yml`-rapporten, i tråd med presedensen frå
  `analyse-cache-key-konsistens`/`analyse-scaffold-todo-alder` (begge finst som make-target utan å vere
  kobla inn i workflowen) — tilgjengeleg via `make analyse-container-copy-konsistens` for manuell/ad hoc
  bruk. Verifisert med reell reproduksjon i begge retningar: (a) mot den faktisk retta Dockerfilen/
  `reusable-lint.yml` (rapporterer null avvik), og (b) mot midlertidig reverterte versjonar av begge
  (fangar alle tre Dockerfile-stadia og begge `reusable-lint.yml`-scripta presist).

## Utført

Vurderinga er gjennomført ved gjennomgang av: `bootstrap.sh`, `mkdocs/docs/arkitektur/ekstern-bruk.md`,
`.github/workflows/reusable-validate.yml`, `.github/workflows/reusable-generate.yml`, `.mcp.json`,
`src/assets/containers/Dockerfile.mcp-linkml`, `src/assets/containers/Dockerfile.linkml`, `make/60-mcp.mk`,
`make/70-scaffolding.mk`, `src/mcp-linkml-validator/server.py`, `src/mcp-linkml-validator/flatten-and-validate.bash`,
`src/mcp-linkml-modell-utkast/` og `SCOPE.md`. Funn 2 vart verifisert ved å lese `sys.path.insert`-linjene i
`server.py` opp mot faktiske `COPY`- og `-v`-monteringar i både Dockerfile og alle tre køyrevegane
(`make/60-mcp.mk`, `flatten-and-validate.bash`, `.mcp.json`), og stadfeste at ingen av dei tre stiane
`sys.path` prøver, finst i nokon av desse køyrevegane. Ingen kodeendringar er gjort — dette er ei rein
kartleggings-/vurderingsoppgåve, i tråd med unntaket i CLAUDE.md sitt arbeidsflytpunkt 5.

### Gjennomføring av handlingslista (oppfølgingssteg)

Alle fem punkta i handlingslista er gjennomførte:

1. **Bug-fiks (Funn 2):** `src/assets/scripts/utils/` bakt inn i `base-runtime`-stadiet i
   `Dockerfile.mcp-linkml`; betinga `utils`-montering lagt til i `flatten-and-validate.bash`; `utils`-montering
   lagt til for alle tre serverane i `.mcp.json`. Verifisert med reell `podman build`+`podman run` for alle
   tre bileta (ingen ekstra `-v`-montering, simulerer ekstern/publisert bruk) — alle svarar korrekt på
   `initialize` no. `make mcp-linkml-valider-modell-smoke`, `make mcp-linkml-modell-utkast-smoke`,
   `make mcp-linkml-begrep-utkast-smoke`, `make mcp-linkml-valider-modell-test` (47 testar) og
   `make mcp-linkml-modell-utkast-test` (51 testar) køyrde alle grønt etter endringane.
2. **`reusable-lint.yml`:** ny fil, sparse-checkout av `.linkmllint.yaml`/`batch-lint.py`/
   `check-import-duplicates.py`/`utils/`, køyrer mot `ghcr.io/brreg/linkml-local`. `actionlint` køyrd reint.
   Underliggande kommandoar smoke-testa direkte mot repoet sitt eige `linkml-local`-bilete (`✓ No problems
   found` / `✓ Ingen import-kollisjonar funne`).
3. **Parameterisering:** `gen-eksempeldata.sh` fekk `SCHEMA_REPO_ROOT` (default: næraste git-rot for
   skjemafila) og overstyrbar `LINKML_GEN_IMAGE`; testa uendra mot eit skjema i dette repoet (framleis
   fungerer identisk). `mcp-linkml-begrep-utkast/server.py` fekk `_SCHEMA_ROOT`/`SCHEMA_ROOT`-miljøvariabel
   (default `"src/linkml"`) i staden for hardkoda sti, inkl. i verktøybeskrivinga. `new-modell.sh` eksplisitt
   ikkje endra (sjå Avgjerder).
4. **Dokumentasjon:** nytt avsnitt «2 — Modell-/begrepsutkast-assistanse via MCP» i `ekstern-bruk.md`
   med `.mcp.json`-oppskrift for begge serverane direkte mot GHCR-bileta (stadfesta publiserte via
   `.github/workflows/release.yml`), pluss eit nytt «Lint»-underavsnitt for `reusable-lint.yml`. JSON-en i
   koden er syntakssjekka.
5. **`check-container-copy-coverage.py`:** ny, kobla inn som `make analyse-container-copy-konsistens`
   (`make/91-modell-analyse.mk`, dokumentert i `COMMANDS.md`, kryssreferert frå den utvida sjekklista i
   `.claude/rules/container-images.md`). Verifisert i begge retningar: rapporterer null avvik mot den retta
   koden, og fangar presist alle tre Dockerfile-stadia + begge `reusable-lint.yml`-scripta når endringane
   vart midlertidig reverterte for testing.

Alle endra Python-/bash-filer er syntakssjekka (`py_compile`/`bash -n`), alle endra `.github/workflows/*.yml`
er køyrde gjennom `actionlint` (reint), og `.mcp.json` er verifisert som gyldig JSON.
