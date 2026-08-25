# Plan: Scripta innsetjing + diffvising i steg 5/7 av JavaZone-demoen

## Bakgrunn

`src/assets/scripts/demo/javazone-demo-script.sh` (sjå
[javazone-demo-plan.md](javazone-demo-plan.md) for full bakgrunn om
demoen) legg i dag opp til at brukaren **manuelt** kopierer YAML-tekst frå
terminalen (fem `cat <<EOF`-blokkar, fordelt på steg 5 og steg 7) inn i
`${SCHEMA}` med ein tekstredigerar, midt i ein tidspressa presentasjon:

- **Steg 5** (tre separate lim-inn-pausar): seks klassar under `classes:`,
  atten slots under `slots:`, éin `enums:`-blokk til slutt i fila.
- **Steg 7** (to separate lim-inn-pausar): erstatt `Foredrag:`/`Sesjon:`
  (limt inn i steg 5) med versjonar som har
  `annotations.begrepsidentifikator`; erstatt `har_foredrag:`/`tid_start:`
  med versjonar som har `slot_uri`.

Dette er sårbart for kopieringsfeil (feil innrykk, utelatne linjer,
skrivefeil) midt i sjølve presentasjonen — nett den typen feil som er
vanskelegast å oppdage og rette live, med publikum til stades. Brukaren
har bede om ei evaluering av om innsetjinga kan **scriptast** (fjerne
copy-paste-steget heilt) og om resultatet i staden kan **visast som ein
diff** på skjermen, som eit synleg, sjølvforklarande steg i demoen.

**Avklart med brukaren før denne spesifikasjonen vart skriven:**

1. **Pausestruktur:** behald dagens per-del Enter-pausar (éin pause per
   `cat`-blokk) — kvar del vert no `Enter → scriptet set inn → diff vert
   vist → Enter for å halde fram`, i staden for `Enter → (brukar limer inn
   sjølv) → Enter`. Presentasjonstempoet er dermed uendra.
2. **Teknisk metode:** rein tekstinnsetjing på kjende ankerlinjer (t.d.
   rett etter `classes:`) via awk/heredoc — **ikkje** ein YAML-parsande
   avhengigheit (t.d. Python/ruamel.yaml i ny container). Grunngjeving:
   innhaldet og målplasseringa er statisk kjend (scriptet sitt eige,
   ferdigskrivne innhald — ikkje brukargenerert eller variabelt), så ei
   YAML-medviten løysing løyser eit problem som ikkje finst her, og legg
   til ei ny containeravhengigheit berre for demo-scriptet.

## Evaluering

**Kan vi scripte kopieringa? Ja**, av følgjande grunnar:

- Alle fem tekstblokkane er **statiske og kjende på førehand** (dei er
  ferdig verifiserte i [javazone-demo-plan.md](javazone-demo-plan.md)) —
  scriptet treng ikkje tolke eller validere vilkårleg brukarinnhald, berre
  setje inn sin eigen, ferdigskrivne tekst på eit kjent punkt.
- Ankerpunkta er eintydige i eit nyoppretta `new-modell`-skjema:
  `classes:`, `slots:` og filslutt (for `enums:`) finst éin gong kvar som
  toppnivå-nøklar. Steg 7 sine erstattingar er enda enklare: dei bytter ut
  **eksakt den teksten scriptet sjølv sette inn i steg 5** (ikkje
  brukarskriven tekst), så ei rein strengerstatting av kjend gamal → kjend
  ny blokk er trygg og deterministisk.
- `git diff --no-index` gjev gratis, fargelagt, lettlest diffvising utan
  ny avhengigheit — git er alt ein føresetnad for å arbeide i dette
  repoet (same status som bash/make, ikkje eit verktøy CLAUDE.md sin
  "ingen lokale avhengigheiter"-regel siktar til — den regelen gjeld
  LinkML-verktøykjeda som elles hadde kravd `pip install linkml` e.l.).
  Same "trykk 'q' for å lukke less"-mønster som `run_help`/`run_validate`
  kan gjenbrukast (`| less -R -F -X`).

**Pedagogisk gevinst, ikkje berre risikoreduksjon:** ein synleg diff er i
seg sjølv eit poeng å vise fram — publikum ser presist kva som vart lagt
til, i staden for å sjå ein presentatør lime inn tekst dei alt har lest på
skjermen. Diffen fungerer dessutan som ei kvittering på at innsetjinga
faktisk trefte rett stad i fila.

**Vurderte risikoar:**

| Risiko | Vurdering |
|---|---|
| Ankerlinje `classes:`/`slots:` finst fleire gonger | Ikkje eit problem i eit ferskt `new-modell`-skjema (stadfest med `grep -c` i implementeringssteget under, som ein eingongssjekk) |
| `git diff --no-index` krev git-binær lokalt | Alt ein rimeleg føresetnad — repoet er eit git-repo, brukaren har git installert for å i det heile arbeide med koden |
| Steg 7-erstattinga finn ikkje att teksten frå steg 5 | Kan ikkje lenger skje: før var det brukaren som skreiv inn (variabelt), no er det scriptet sjølv som skreiv presis den same teksten i steg 5 — strengerstattinga er dermed deterministisk |
| Duplisering av tekstinnhald (både vist til brukar og brukt til innsetjing) | Løys ved å la éin shell-variabel/heredoc vere kjelda for **både** visinga og innsetjinga (same DRY-prinsipp som elles i CLAUDE.md) |

## Plan — nummererte steg

1. **Lag ein felles insert-funksjon** `insert_after_line SCHEMA ANKERLINJE INNHALD` (awk-basert: finn fyrste linje som matchar ankeret, set inn `INNHALD` rett etter). Brukast til steg 5 sine `classes:`- og `slots:`-innsetjingar.
2. **Lag ein append-funksjon** `append_to_file SCHEMA INNHALD` for `enums:`-blokka (heilt nytt toppnivå-felt til slutt i fila).
3. **Lag ein `show_diff FØR ETTER`-funksjon**: `git diff --no-index --color=always -- "$FØR" "$ETTER" | less -R -F -X`, med same `(trykk 'q' for å lukke less …)`-hint som `run_help`/`run_validate`.
4. **Refaktorer steg 5**: for kvar av dei tre `cat <<EOF`-blokkane — ta kopi av `$SCHEMA` (`cp` til ein tempfil i `$TMPDIR`), køyr innsetjinga via steg 1/2 sine funksjonar, vis diff via steg 3, behald eksisterande `prompt_enter`-pause mellom kvar del. Same tekstinnhald skal brukast **både** til det som (framleis) vert vist i terminalen og det som vert sett inn i fila — unngå å duplisere teksten i to ulike variablar.
5. **Refaktorer steg 7**: for kvar av dei to erstattingane — finn og byt ut den eksakte gamle blokka (frå steg 5) med den nye (annotert) versjonen, t.d. via ein `replace_block SCHEMA GAMMAL NY`-funksjon (`awk`/`perl -0777 -pe` for fleirlinje-erstatting), vis diff, behald `prompt_enter`-pausane.
6. **Oppdater kommentarane** i scriptet: linje 9-10 (`# Steg utan kommando (steg 5) er reine pausar for live-redigering.`) er ikkje lenger presist og må justerast til å skildre den nye "scriptet set inn + viser diff"-flyten.
7. **Oppdater [javazone-demo-plan.md](javazone-demo-plan.md)**: seksjonane "Ferdig kopierbar klassedefinisjon (steg 5)" og "Steg 9 (nytt): Adresser funn frå valideringa" skildrar i dag manuell lim-inn — legg til ei kort kryssreferanse til denne specen i staden for å skrive om heile skildringa (DRY, jf. CLAUDE.md).
8. **Test heile scriptet end-to-end**, same offline-sjekkliste-mønster som elles i `javazone-demo-plan.md` — verifiser at diffane faktisk viser dei rette endringane, at `less -R`-pipinga fungerer identisk til `run_help`/`run_validate`, og at det ferdig-redigerte skjemaet framleis validerer likt som før (steg 6/8 uendra).

## Handlingsliste

- [x] `insert_before_line`-funksjon (awk-basert)
- [x] `block_end_line` + `replace_block`-funksjonar (indentasjonsbasert blokkgrense — sjå avvik under)
- [x] `show_diff`-funksjon (`git diff --no-index --color=always | less -R -F -X`)
- [x] Refaktorer steg 5 (tre lim-inn-pausar → tre insert+diff-sekvensar)
- [x] Refaktorer steg 7 (to lim-inn-pausar → to replace+diff-sekvensar)
- [x] Oppdater kommentar i toppen av `javazone-demo-script.sh` (linje 9-10)
- [x] Kryssreferanse frå `javazone-demo-plan.md` til denne specen
- [x] Funksjonstest av innsetjings-/erstattingslogikken mot ein realistisk fixture (verifiserer YAML-gyldigheit, riktige ankerpunkt, riktig blokkerstatting)
- [ ] **Attverande:** full live offline-øvingskøyring av heile scriptet på brukaren si eiga maskin (sjå "Avvik/notat" under — kunne ikkje fullførast i dette verktøymiljøet)

## Avvik frå opphavleg plan

1. **`insert_after_line` vart `insert_before_line`, og `append_to_file` vart aldri laga.**
   Ved gjennomgang av det faktiske filoppsettet frå `new-modell.sh` og
   ein reell tidlegare demo-køyring (`src/linkml/oreg/javazonetalk/javazonetalk-schema.yaml`,
   sjå git-historikk) synte det seg at brukaren sitt opphavlege manuelle
   lim-inn-punkt var **slutten** av `classes:`-/`slots:`-seksjonane
   (rett før neste toppnivåfelt), ikkje rett etter `classes:`-/`slots:`-
   linjene sjølve. Éin funksjon, `insert_before_line SCHEMA ANKERLINJE
   INNHALD`, dekkjer alle tre steg-5-innsetjingane ved å bruke to stabile
   tekstankrar: den bokstavelege `slots:`-linja (klassar) og den
   bokstavelege, alltid-tilstadeverande sluttkommentaren
   `# TODO: Gi stub-klassen eit meir meiningsfullt navn.` frå
   `new-modell.sh` (slots og enums — begge sett inn rett før same
   ankerlinje, som naturleg gjev rett rekkjefølgje sidan ankerlinja sin
   posisjon flyttar seg nedover for kvar innsetjing). Enklare og meir
   robust enn den opphavleg føreslåtte insert-etter/append-kombinasjonen.
2. **`replace_block` brukar indentasjonsbasert blokkgrense, ikkje
   linjenummer-sporing frå innsetjinga.** I staden for å hugse kva
   linjenummer steg 5 sette inn på, finn `block_end_line` blokkgrensa
   dynamisk: frå nøkkellinja (t.d. `  Foredrag:`) og framover til neste
   linje med same 2-mellomrom-innrykk (neste klasse/slot-nøkkel) eller
   eit nytt 0-innrykk toppnivåfelt. Robust mot at anna kode har endra
   fila mellom steg 5 og 7, og krev ingen tilstand å bere mellom stega.
3. **Full live offline-øvingskøyring kunne ikkje fullførast i dette
   verktøymiljøet** — `podman` her manglar fungerande rootless-oppsett
   (`newuidmap: write to uid_map failed: Operation not permitted`, same
   feil som `make check-prereqs` sjølv rapporterer), så `make new-modell`
   kunne aldri generere ei fil å teste innsetjinga mot. I staden vart
   innsetjings-/erstattingslogikken verifisert ved å (a) hente
   ankerstrategien direkte frå det faktiske, tidlegare genererte
   `javazonetalk-schema.yaml` i git-historikken (stadfestar kvar ekte
   `new-modell`-output legg lim-inn-punkta), (b) byggje ein realistisk
   fixture med same struktur, og (c) køyre funksjonane **ordrett henta ut
   av den ferdigskrivne `javazone-demo-script.sh`** (ikkje ein separat
   kopi) mot fixturen — stadfesta gyldig YAML med alle seks klassar,
   atten slots, enum-blokka og begge annoterte erstattingane på plass.
   Kravet i handlingslista sitt punkt 8
   (`javazone-demo-plan.md` sin offline-sjekkliste: full live-øving,
   fråkopla nett) står att som brukaren sitt eige steg før demo-dagen —
   uendra frå det opphavlege kravet i `javazone-demo-plan.md`.
