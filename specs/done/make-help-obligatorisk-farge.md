# Plan: Eigen farge for obligatoriske vs. valfrie argument

## Bakgrunn

`make help` viser i dag argumenta til kvart target som éitt farga
uttrykk (`CLR_WARN`, gul) uavhengig av om det er obligatorisk
(`(ARG=<verdi>)`) eller valfritt (`[ARG=<verdi>]`) — skiljet er berre
synleg via parentes/hakeparentes-teiknet, ikkje farge. Brukaren ønskjer
eigen farge på obligatoriske argument: **grønt for obligatoriske,
gult framleis for valfrie.**

For target med fleire etterfølgjande grupper (t.d.
`remove-modell (DOMAIN=<domene> NAME=<namn>) [CONFIRM=1]`) må kvar gruppe
fargeleggjast individuelt basert på sin eigen parentes/hakeparentes-type —
ikkje heile argument-uttrykket samla, sidan det kan blande obligatorisk og
valfritt i same target.

## Tiltak

`src/assets/scripts/makefile/help.sh`:
- Legg til `CLR_OK=$'\033[0;32m'` (grøn, matchar `CLR_OK` i
  `make/00-settings.mk`)
- I ekstraheringsløkka: fargelegg kvar gruppe individuelt idet ho vert
  peila av — `CLR_OK` for parentes-grupper (`(...)`), `CLR_WARN` for
  hakeparentes-grupper (`[...]`) — før ho vert sett saman til det endelege
  `argexpr`-uttrykket. Dette gjer at `argexpr` alt inneheld embedda
  fargekodar, og `printf`-linja som skriv ut `make <target> <argexpr>`
  treng ikkje lenger pakke heile uttrykket i éin ytre farge.

`Makefile`: oppdater `Konvensjon:`-forklaringslinja i `help:`-targetet
([[make-help-argumentkonvensjon-forklaring]]) til å bruke same fargepar —
`(ARG=<verdi>)`-eksempelet i grønt, `[ARG=<verdi>]`-eksempelet framleis i
gult — slik at legenda faktisk matchar det lista under viser.

## Handlingsliste

1. [x] `help.sh`: legg til `CLR_OK`, fargelegg kvar argumentgruppe
   individuelt i ekstraheringsløkka
2. [x] `help.sh`: forenkla `printf`-linjene (argexpr er no ferdig-farga)
3. [x] `Makefile`: oppdater `Konvensjon:`-linja til grønt for obligatorisk
4. [x] Verifiser med `make help`: eittgruppe-target (`roundtrip`,
   `new-modell`), fleiregruppe-target (`remove-modell`,
   `mcp-linkml-valider-modell`, som blandar obligatorisk `SCHEMA` og
   valfri `[POLICY=...]` inni same parentes)

## Utført

`help.sh`: `CLR_OK` lagt til, kvar avslutta argumentgruppe vert no farga
individuelt idet ho vert peila av — grøn (`CLR_OK`) for parentes-grupper,
gul (`CLR_WARN`) for hakeparentes-grupper — før samanslåing til `argexpr`.
`printf`-linjene forenkla sidan `argexpr` alt inneheld embedda fargekodar.
`Makefile` sin `Konvensjon:`-linje oppdatert til å bruke same fargepar.

Verifisert med `make help`:
- `new-modell (DOMAIN=<domene> NAME=<namn>)` — heile grøn (éin
  obligatorisk gruppe)
- `remove-modell (DOMAIN=<domene> NAME=<namn>) [CONFIRM=1]` — grøn gruppe
  + gul gruppe, korrekt skilt
- `mcp-linkml-valider-modell (SCHEMA=<sti> [POLICY=<bronze|silver|gold>])`
  — heile den ytre parentesen (inkl. nøsta `[POLICY=...]`) vert grøn, sidan
  fargelegginga skjer på gruppe-nivå (ytre delimiter), ikkje token-nivå —
  medvite avgrensing, dokumentert i `help.sh` sin toppkommentar
