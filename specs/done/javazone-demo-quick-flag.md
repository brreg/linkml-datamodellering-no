# Plan: `QUICK`-flagg for JavaZone-demoscriptet

## Bakgrunn

`src/assets/scripts/demo/javazone-demo-script.sh` (sjå
[javazone-demo-plan.md](javazone-demo-plan.md) og
[javazone-demo-auto-innsetjing.md](javazone-demo-auto-innsetjing.md) for
full kontekst) køyrer i dag alltid gjennom heile 14-stegs-sekvensen frå
botnen: steg 1 (`make help`), steg 2 (`check-prereqs`), steg 3
(`make new-modell`) og steg 4a-4c (scripta innsetjing av seks klassar,
atten slots og éin enum-blokk i `$SCHEMA`, kvar med si eiga
`Trykk Enter → sjå diff`-pause).

Brukaren ønskjer eit nytt `QUICK=<true|false>`-flagg, **default `true`**,
som hoppar over steg 1-4 heilt (ingen prompt, ingen "boxes"-overskrifter,
ingen diff-visingar for desse stega) og i staden **genererer
`javazonetalk-schema.yaml` direkte** i nøyaktig den tilstanden fila skal
vere i etter steg 4 — altså identisk sluttinnhald som om steg 1-4 var
køyrde interaktivt, berre utan presentasjonsstoppa. Scriptet held så fram
frå steg 5 (validering) som normalt.

Bruksmønsteret dette dekkjer: rask, gjenteken øving/verifisering av steg
5-14 (validering, funn-retting, analyse, artefaktgenerering) utan å måtte
klikke seg gjennom fire kjende, uendra innleiingssteg kvar gong — medan
`QUICK=false` framleis gjev den fulle, presentasjonsklare demoen slik ho
er i dag.

## Design

### Kva "steg 1-4" konkret er

| Steg | Kommando/handling | Notat |
|---|---|---|
| 1 | `make help \| less -R` | Reint informativt |
| 2 | `bash check-prereqs.bash` | Miljøsjekk |
| 3 | `make new-modell DOMAIN=$DOMAIN NAME=$NAME` | Scaffoldar `$SCHEMA` |
| 4a | Set inn 6 klassar før `slots:`-linja | `do_insert "slots:" "$classes_content"` |
| 4b | Set inn 18 slots før `$TRAILING_MARKER` | `do_insert "$TRAILING_MARKER" "$slots_content"` |
| 4c | Set inn `enums:`-blokk før `$TRAILING_MARKER` | `do_insert "$TRAILING_MARKER" "$enums_content"` |

Steg 5 (`make mcp-linkml-valider-modell`) og alt etter er **uendra** i
begge modus — `QUICK` styrer berre korleis `$SCHEMA` kjem fram til den
tilstanden steg 5 forventar.

### Teknisk tilnærming — gjenbruk, ikkje duplisering

`classes_content`/`slots_content`/`enums_content` (dei tre heredoc-ane i
dagens steg 4a-4c) og innsetjingsfunksjonen `insert_before_line` finst
alt (sjå `javazone-demo-auto-innsetjing.md`). Løysinga er difor **ikkje**
å skrive ein separat, ferdig `javazonetalk-schema.yaml`-fil, men å:

1. Hoiste dei tre heredoc-tildelingane (`classes_content`, `slots_content`,
   `enums_content`) til **før** steg 1-4-blokka, slik at både den
   interaktive og den stille vegen brukar nøyaktig same shell-variablar —
   éin kjelde for innhaldet (same DRY-grunngjeving som alt gjeld for
   steg 5/7-visinga vs. innsetjinga, jf. auto-innsetjing-specen).
2. Vikle heile steg 1-4-blokka (dagens linjer ca. 362-563) i
   `if [ "$QUICK" = "false" ]; then … else … fi` — `false`-greina er
   **uendra kopi** av dagens kode (same `step`/`print_heading`/`do_insert`-
   kall, same forklarande `cat <<EOF`-tekstar), `true`-greina køyrer dei
   same underliggjande operasjonane (`make new-modell` +
   `insert_before_line` × 3) **utan** `step()`/`prompt_enter`/`show_diff`.

Dette sikrar at eit `QUICK=true`-køyr og eit `QUICK=false`-køyr med same
`DOMAIN`/`NAME` gjev **byte-for-byte identisk** `$SCHEMA` etter steg 4 —
same innhald, berre ulik presentasjon undervegs.

### Design-val (antakingar — juster om ønskt)

1. **Eksisterande "finst frå før"-oppryddingsspørsmålet (linje 65-72)
   vert ikkje endra.** Det køyrer alltid, uavhengig av `QUICK`, sidan
   `make new-modell` uansett feilar dersom katalogen finst frå før — dette
   er ikkje eit av "steg 1-4", men eit tryggingssteg før dei.
2. **`check-prereqs` (steg 2) hoppar heilt over i `QUICK=true`,** ikkje
   berre stille i bakgrunnen. Grunngjeving: `QUICK` er meint for raske,
   gjentekne øvingskøyringar der miljøet alt er stadfesta klart (t.d.
   rett etter ei `QUICK=false`-køyring same økt) — og feilar miljøet
   likevel, vil `make new-modell` (som kallar podman) feile synleg med
   ein tydeleg feilmelding uansett. Ønskjer brukaren miljøsjekk likevel,
   er `make check-prereqs` éin kommando unna, frittståande frå
   demoscriptet.
3. **`QUICK=true` skriv éi kort statuslinje** (kva som skjer + at steg
   5 er neste), ikkje full stille — konsistent med
   "Ingen stille feil"-prinsippet i CLAUDE.md og gjev likevel eit synleg
   spor i terminalen om noko skulle feile midtvegs.
4. **Feil i `make new-modell`/innsetjinga under `QUICK=true` er ikkje-
   fatale** (same filosofi som elles i scriptet — "Ikkje 'set -e'"):
   feilen vert vist med `${CLR_ERR}`, scriptet held fram til steg 5, som
   då truleg også feilar synleg (t.d. fordi `$SCHEMA` manglar) — brukaren
   ser tydeleg kva som gjekk gale, i staden for at scriptet krasjar midt i
   ei presentasjonsøving.
5. **Demoklokka (`DEMO_START`, linje 331) vert ikkje flytta.** I
   `QUICK=true` tel klokka dermed frå rett før steg 5 (den einaste
   praktiske forskjellen er at "steg 1" tilskodaren opplever no er det
   som i dag er steg 5) — ønskt åtferd, sidan klokka sitt føremål er å
   halde presentasjonstida, og den stille genereringa ikkje er ein del av
   presentasjonen.

## Nummererte steg

1. **Legg til `QUICK`-parsing** i argument-loopen (linje ~26-38): ny
   variabel `QUICK="true"` (default), nytt `QUICK=*`-case som validerer
   verdien er nøyaktig `true` eller `false` (elles ei tydeleg feilmelding
   og exit 1 — same mønster som det eksisterande "ukjent argument"-caset).

2. **Oppdater bruksdokumentasjonen i toppkommentaren** (linje 5-8): legg
   til `[QUICK=<true|false>]` i køyreeksempelet og forklar default +
   åtferd (skip steg 1-4, `$SCHEMA` genererast direkte i tilstanden etter
   steg 4).

3. **Hoist dei tre heredoc-innhaldsvariablane** (`classes_content`,
   `slots_content`, `enums_content`) til rett før steg 1-4-blokka, slik
   at begge greinene i steg 4 kan bruke dei utan duplisering. Sjølve
   YAML-innhaldet i heredoc-ane er **uendra**.

4. **Vikle steg 1-4 i `if [ "$QUICK" = "false" ]; then … fi`** med
   dagens kode uendra i denne greina (steg 1, 2, 3, 4a, 4b, 4c — same
   `step`/`print_heading`/`cat <<EOF`-forklaringar/`do_insert`-kall som i
   dag).

5. **Legg til `else`-greina** (`QUICK=true`) med:
   - Éi kort statuslinje (`${CLR_DBG}`) som seier at steg 1-4 vert hoppa
     over og `$SCHEMA` vert generert direkte.
   - `make new-modell DOMAIN="$DOMAIN" NAME="$NAME"`, feil vert vist
     (`${CLR_ERR}`), ikkje `exit`.
   - Tre `insert_before_line`-kall (klasser → `"slots:"`, slots →
     `"$TRAILING_MARKER"`, enums → `"$TRAILING_MARKER"`) — same rekkjefølgje
     og same ankerlinjer som `do_insert`-kalla i `false`-greina, berre
     utan `prompt_enter`/`show_diff`. Kvart kall sin eigen feilhandtering
     (`insert_before_line` skriv alt ein tydeleg `${CLR_ERR}`-feilmelding
     til stderr ved manglande ankerlinje — ingen ekstra logging naudsynt
     her for å oppfylle "ingen stille feil").
   - Ei avsluttande `${CLR_OK}`-linje: "Ferdig — held fram frå steg 5."

6. **Oppdater `specs/backlog/javazone-demo-plan.md`**: legg til
   `QUICK=<true|false>`-argumentet i køyreeksempelet
   (`bash src/assets/scripts/demo/javazone-demo-script.sh …`) med ei kort
   forklaring og kryssreferanse til denne specen — same
   kryssreferanse-mønster som specen alt brukar for
   `javazone-demo-auto-innsetjing.md` (DRY, ikkje dupliser skildringa).

7. **Verifiser**:
   - `bash -n src/assets/scripts/demo/javazone-demo-script.sh` (syntakssjekk).
   - Køyr scriptet med `QUICK=true` (default) frå repo-rota, stadfest at
     det hoppar rett til steg 5 sitt "Trykk Enter"-prompt og at
     `src/linkml/oreg/javazonetalk/javazonetalk-schema.yaml` då alt
     inneheld dei seks klassane, atten slotsa og enum-blokka.
   - `diff` det resulterande skjemaet mot eit skjema generert med
     `QUICK=false` (same `DOMAIN`/`NAME`, gjennomført steg 1-4
     interaktivt) — skal vere identisk.
   - Stadfest at steg 5-14 oppfører seg identisk i begge modus (same
     valideringsfunn som dokumentert i `javazone-demo-plan.md`, "Steg 9").
   - Rydd opp testkøyringane (`rm -rf src/linkml/oreg/javazonetalk
     generated/oreg/javazonetalk`) mellom kvart forsøk, same som scriptet
     sjølv spør om ved gjenbruk av `DOMAIN`/`NAME`.
   - `podman info` fungerer i dette miljøet (stadfesta) — i motsetnad til
     verktøymiljøet `javazone-demo-auto-innsetjing.md` vart skriven i, bør
     ei fullverdig live-køyring difor vere mogleg å gjennomføre no, ikkje
     berre statisk verifisering.

## Handlingsliste

| # | Tiltak | Fil | Type |
|---|---|---|---|
| 1 | `QUICK`-argumentparsing + validering | `javazone-demo-script.sh` | Ny funksjonalitet |
| 2 | Oppdater toppkommentar (bruk/default) | `javazone-demo-script.sh` | Dokumentasjon |
| 3 | Hoist `classes_content`/`slots_content`/`enums_content` | `javazone-demo-script.sh` | Refaktorering (DRY) |
| 4 | `if QUICK=false … fi` rundt eksisterande steg 1-4 | `javazone-demo-script.sh` | Refaktorering |
| 5 | Ny `else`-grein: stille `make new-modell` + 3× `insert_before_line` | `javazone-demo-script.sh` | Ny funksjonalitet |
| 6 | Nemn `QUICK` i køyreeksempelet | `specs/backlog/javazone-demo-plan.md` | Dokumentasjon |
| 7 | Syntakssjekk + live-verifisering (begge modus, diff mot kvarandre) | — | Verifisering |

## Opne spørsmål til brukaren

Design-vala i lista over («Design-val (antakingar)») er rimelege
standardval, men er ikkje eksplisitt stadfesta av brukaren enno —
spesielt punkt 2 (heilt hoppe over `check-prereqs`, ikkje berre køyre han
stille) og punkt 4 (ikkje-fatal feilhandtering i `QUICK=true`). Sei frå
dersom nokon av desse skal vere annleis før steg 1-7 vert gjennomførte.

---

## Utført

Alle steg (1-7) er gjennomførte 2026-09-01, med dei dokumenterte
design-vala uendra (ingen tilbakemelding kravde justering):

- **Steg 1**: `QUICK`-argumentparsing lagt til (default `"true"`),
  validerer verdien er nøyaktig `true`/`false`.
- **Steg 2**: Toppkommentaren oppdatert med `QUICK`-bruk/default/åtferd.
- **Steg 3**: `classes_content`/`slots_content`/`enums_content` hoista
  til rett før steg 1-4-blokka (identisk YAML-innhald, berre flytta —
  gjort programmatisk via eit Python-restruktureringsskript for å unngå
  transkripsjonsfeil i så stort ein flytt).
- **Steg 4**: Steg 1-4 vikla i `if [ "$QUICK" = "false" ]; then … fi`,
  uendra kode i denne greina.
- **Steg 5**: `else`-grein lagt til — statuslinjer, stille
  `make new-modell`, tre `insert_before_line`-kall, avsluttande
  `${CLR_OK}`-kvittering.
- **Steg 6**: `specs/backlog/javazone-demo-plan.md` sitt køyreeksempel
  utvida med `QUICK=false`-varianten og ei kort forklaring +
  kryssreferanse til denne specen.
- **Steg 7 — verifisert live**:
  - `bash -n` syntakssjekk: OK.
  - Full live-køyring med `QUICK=true DOMAIN=oreg NAME=quicktest` (< /dev/null,
    timeout 90s): hoppa korrekt over steg 1-4, viste
    `QUICK=true — hoppar over steg 1-4 …`, køyrde `make new-modell` +
    innsetjingane, gjekk rett til "5. Valider skjemaet", og heldt fram
    gjennom steg 6-13 (fekk tidsavbrot under steg 13, forventa —
    testen trong berre stadfeste at QUICK-greina og overgangen til
    steg 5 fungerer).
  - Full live-køyring med `QUICK=false DOMAIN=oreg NAME=quicktest2`
    (same vilkår): gjennomførte steg 1-4 interaktivt (ikkje-fatalt
    tomt `/dev/null`-stdin let alle `read`/`less`-kall passere gjennom).
  - `diff` av dei to resulterande skjemafilene (etter å ha normalisert
    `quicktest2` → `quicktest` i namnereferansane) synte **ingen
    skilnad** utover den forventa stub-klasse-namngjevinga avleidd av
    `NAME` sjølv (`Quicktest`/`Quicktest2`) — stadfestar at `QUICK=true`
    og `QUICK=false` gjev byte-for-byte identisk sluttinnhald for dei
    seks klassane, atten slotsa og enum-blokka.
  - Testartefakta (`src/linkml/oreg/quicktest*`,
    `generated/oreg/quicktest*`) rydda opp etter verifiseringa. Den
    faktiske `src/linkml/oreg/javazonetalk`-katalogen (med
    førehandseksisterande, ikkje-relaterte lokale endringar) vart ikkje
    rørt.
  - `podman info` fungerte i dette miljøet gjennom heile testen —
    fullverdig live-verifisering var difor mogleg, i motsetnad til
    avgrensinga nemnd i `javazone-demo-auto-innsetjing.md`.

Ingen avvik frå planen.
