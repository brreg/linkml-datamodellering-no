# Publiser artefakt-generering.md og arkitektur-oversikt.md i mkdocs-portalen

## Bakgrunn

`specs/backlog/artefakt-generering.md` og `specs/backlog/arkitektur-oversikt.md`
er to orienteringsskisser (same sjanger — "korleis heng repoet saman", ikkje
endringsplanar) som begge skal publiserast i GitHub Pages-portalen. Første
runde av denne specen vurderte berre `artefakt-generering.md`; brukaren har no
bede om at `arkitektur-oversikt.md` takast med i same løp, **og** om ei
vurdering av om seks mkdocs-sider (`arkitektur-oversikt.md`,
`artefakt-generering.md`, `readme-tabellgenerering.md`,
`publisering-oversikt.md`, `modellmanifest-generering.md`, `monitorering.md`)
bør gjennomgåast samla for å unngå gjentakingar, gruppere relatert innhald, og
betre filnamn/overskrifter/oppbygging pedagogisk for nye brukarar.

Konklusjon på begge spørsmåla: **ja** — plasseringsvurderinga frå runde 1 gjeld
uendra for `arkitektur-oversikt.md` (same NAV-plassering, same grunngjeving),
og gjennomgangen under viser konkrete, dokumenterbare funn som gjer at ein
konsolideringsrunde er verdt kostnaden, ikkje berre eit teoretisk DRY-poeng.

## Del 1: Plassering — same konklusjon som for artefakt-generering.md

Dei tre alternativa frå runde 1 (NAV under "Rettleiingar" / lenkje frå
"Om dette repoet" / lenkje frå README.md) er allereie vurderte generelt for
denne typen intern-arkitektur-dokumentasjon — grunngjevinga er identisk for
`arkitektur-oversikt.md`: sida høyrer heime blant dei andre teknisk orienterte
Rettleiingar-sidene, ikkje i `om.md` (anna register: kontakt/lisens/attribusjon)
og ikkje i README.md (framside, ikkje ein lenkjeindeks til Rettleiingar-sidene).
Sjå historikken i Del 2 for kvifor dette spørsmålet faktisk **alt har blitt
svart** ein gong før, med same konklusjon.

## Del 2: Viktig funn — namnet "arkitektur-oversikt.md" har vore brukt i portalen før

`mkdocs/docs/arkitektur-oversikt.md` **fanst allereie éin gong**, og historikken
er relevant for korleis den nye fila bør handterast:

1. `specs/done/konsolidering-arkitektur-docs.md` (2026-06-29) slo saman
   `mkdocs/docs/arkitektur-oversikt.md` og `mkdocs/docs/publiseringsflyt-oversikt.md`
   til éi fil for å fjerne duplisering.
2. `specs/done/readme-oppdatering.md` (tiltak 10) **omdøypte** den samanslåtte
   fila frå `arkitektur-oversikt.md` til `publisering-oversikt.md` — sitat:
   *"Omdøyp arkitektur-oversikt.md til publisering-oversikt.md ... for å spegle
   faktisk innhald"*. Det er difor `mkdocs/docs/publisering-oversikt.md` som i
   dag er den historiske etterkomaren av det gamle `arkitektur-oversikt.md`
   (H1 i fila er framleis "# Publiseringsflyt").

Den **nye** `specs/backlog/arkitektur-oversikt.md` er ikkje same fil kome
tilbake — ho er vesentleg breiare (MCP-serverar, GHCR, bootstrap for eksterne
repo, KUDAF/dataplattform-konsumentar) enn det gamle, publiseringsfokuserte
innhaldet. Namnekollisjonen er difor **ikkje eit problem** (det gamle namnet
er ledig), men ho forklarer kvifor `publisering-oversikt.md` og den nye
`arkitektur-oversikt.md` overlappar så mykje innhaldsmessig — dei er
i praksis søskenfiler frå same opphavlege idé, som har utvikla seg i kvar
sin retning. Dette er hovudfunnet som gjer konsolideringsspørsmålet i Del 3
konkret, ikkje berre teoretisk.

## Del 3: Bør dei seks filene gjennomgåast samla? Ja — konkrete funn

### 3.1 Innhaldsklynger som dukkar opp i fleire filer

| Klynge | Finst i | Vurdering |
|---|---|---|
| **"Pull, ikkje push"-prinsippet** | `CLAUDE.md` (kanonisk), `arkitektur-oversikt.md` (kort forklaringsboks), `publisering-oversikt.md` (full tabell + "Kvifor?"-avsnitt), `monitorering.md` ("Avgrensingar"-seksjonen seier same ting med andre ord) | 4 stader. `publisering-oversikt.md` har den fyldigaste forklaringa — dei andre tre bør lenkje dit i staden for å omskrive prinsippet |
| **Private/eksterne konsumentar** (KUDAF, private datakatalogar, dataplattformer, API-gateway) | `arkitektur-oversikt.md` Del 2 (`Konsumenter`-subgraph + forklaringspunkt) og `publisering-oversikt.md` ("Private system som kan høste") | Same tre konsument-kategoriar skildra to gonger med ulikt detaljnivå. `arkitektur-oversikt.md` gir diagrammet/oversikta, `publisering-oversikt.md` gir formatdetaljar (`.ttl`/`.json`/`.proto` per konsumenttype). Bør delast tydeleg: arkitektur-oversikt.md peikar *at* dette skjer, publisering-oversikt.md forklarar *korleis* |
| **"Kvar genererte filer endar"** (generated/ → GitHub Pages → GitHub Releases) | `publisering-oversikt.md` (eiga seksjon), `arkitektur-oversikt.md` ("Publiserte pull-punkt"-node i diagrammet), `artefakt-generering.md` (implisitt, per-artefakt-tabellen) | 3 stader, ulikt detaljnivå. `publisering-oversikt.md` er den einaste med reelt tekstleg forklaring — behald der, lenk frå dei andre to |
| **CI-workflow-skildringar** (`generate.yml`, `validate.yml`, `release-please.yml`, `release.yml`) | `arkitektur-oversikt.md` (diagram-nodar), `artefakt-generering.md` § 5 "CI-orkestrering", `monitorering.md` (fulle tabellar + "Kva viser loggane") | `monitorering.md` er tydeleg mest detaljert/autoritativ her (loggtolking, feilsøking). `artefakt-generering.md` § 5 bør korte ned til rekkjefølgje + lenkje til `monitorering.md` for detaljar |
| **Manifest-generering (ModelDCAT-AP-NO)** | `modellmanifest-generering.md` (fullstendig), `artefakt-generering.md` § 3.6 (kortversjon av same 6 kjelder + same tabellstruktur) | § 3.6 dupliserer strukturen (ikkje berre viser til han). Bør kortast til 3-4 linjer + lenkje |

### 3.2 To konkrete, uavhengige funn (ikkje berre "stil"-vurdering)

1. **Bokstaveleg intern duplikasjon i éi og same fil.** I
   `publisering-oversikt.md` skildrar seksjonen **"Dataflyt: frå YAML til
   data.norge.no"** (to Mermaid sequence-diagram, linje 249-289) nøyaktig dei
   same fem-seks stega som seksjonen **"Workflow: frå commit til synleg på
   data.norge.no"** rett under (linje 292-339, bash-kommandoar +
   nummerert liste). Same informasjon, to notasjonsformer, ingen kryssvising
   mellom dei. Dette bør slåast saman til éin gjennomgang (diagram **eller**
   trinnvis liste, ikkje begge) — reint vedlikehaldsproblem, uavhengig av
   dei to nye sidene.
2. **`readme-tabellgenerering.md` er publisert, men manglar i NAV-menyen.**
   Fila ligg i `mkdocs/docs/` og er bygd av `publish.sh`, men står **ikkje**
   i `nav:`-heredoc-blokka i `publish.sh` (verifisert ved å lese heile
   blokka). Einaste inngang til sida i dag er éi lenkje frå README.md/hovud-
   `index.md` (linje 349). Ein brukar som navigerer via menyen til venstre
   (den vanlege måten å utforske Rettleiingar-sider på) finn henne aldri.
   Dette er ei uavhengig, lågkost retting (éi nav-linje) som bør gjerast
   same runde, sidan spørsmålet uansett gjeld korleis desse seks sidene
   heng saman i menyen.

### 3.3 Kva bør IKKJE endrast

`modellmanifest-generering.md`, `monitorering.md` (utanom kryssleenking) og
`readme-tabellgenerering.md` (utanom nav-oppføringa) treng ikkje
innhaldsendringar — dei er allereie sjølvstendige, veldokumenterte sider med
lite intern overlapp med kvarandre. Konsolideringsarbeidet gjeld primært
`arkitektur-oversikt.md` ↔ `publisering-oversikt.md` (størst overlapp) og
korte ned dupliserte forklaringar i `artefakt-generering.md`.

## Del 4: Filnamn, overskrifter og pedagogisk oppbygging

### 4.1 Namnekonsistens

| Fil | Filnamn-mønster | H1 | Nav-label | Vurdering |
|---|---|---|---|---|
| `artefakt-generering.md` (ny) | `<ting>-generering.md` | "Artefaktgenerering — kjelder og pipeline" | (ny) | Konsistent med mønsteret under |
| `modellmanifest-generering.md` | `<ting>-generering.md` | "Modellmanifest-generering" | "Generering av modellmanifest" | OK |
| `readme-tabellgenerering.md` | `<ting>-generering.md` | "README-tabellgenerering" | *(manglar — sjå § 3.2)* | Namn OK, manglar berre nav-oppføring |
| `arkitektur-oversikt.md` (ny) | `<ting>-oversikt.md` | "Arkitekturoversikt" | (ny) | OK, men merk kollisjon med historisk namn (Del 2) — ingen handling naudsynt, berre kontekst |
| `publisering-oversikt.md` | `<ting>-oversikt.md` (filnamn) vs. `<ting>flyt` (H1) | "Publiseringsflyt" | "Publiseringsflyt" | **Filnamnet matchar ikkje H1/nav-label.** Historisk arva frå omdøyping i `readme-oppdatering.md` (Del 2) som prioriterte å matche *innhald*, men ikkje fullførte namnebyte på fila. Bør helst heite `publiseringsflyt.md` for indre konsistens — **valfri opprydding**, sjå åtvaring under |
| `monitorering.md` | eittordsnamn | "Monitorering av automasjon" | "Monitorering av automasjon" | OK |

**Åtvaring om å omdøype `publisering-oversikt.md`:** GitHub Pages-URL-en
(`.../publisering-oversikt/`) er offentleg og kan vere bokmerkt eller lenkja
til utanfrå (portalen peikar alltid til siste `main`, jf. CLAUDE.md, så det
finst ingen versjonert URL å ta omsyn til — men eksterne lenkjer til *denne*
sida ville likevel brekke). Dette er lågare risiko enn t.d. eit skjema-URI,
men bør vere eit medvite val, ikkje ei sidegevinst av denne oppryddinga.
**Anbefaling: la filnamnet vere som det er** med mindre brukaren eksplisitt
ønskjer omdøyping — namneavviket er kosmetisk, ikkje forvirrande nok til å
rettferdiggjere brotne lenkjer.

### 4.2 Manglar gruppering i NAV — pedagogisk forslag (større omfang, valfritt)

I dag er alle 16 (snart 18) Rettleiingar-sider éi flat liste. Ein ny brukar
kan ikkje sjå at t.d. `ny-domenemodell.md` er ein annan type side
("kom i gang") enn `artefakt-generering.md` ("intern pipeline-referanse") før
dei klikkar seg inn. MkDocs Material støttar nesta nav-grupper
(`- Gruppenamn: [...]`), som `publish.sh` sin `nav:`-heredoc **ikkje** nyttar
i dag for Rettleiingar-seksjonen (kun for domenemodellane, steg 4 i
`publish.sh`).

**Forslag til gruppering** (kun ei omorganisering av eksisterande sider —
ingen nye filer):

```yaml
- Rettleiingar:
    - index.md
    - Kom i gang:
        - Bli modelleigar: ny-org.md
        - Ny domenemodell: ny-domenemodell.md
        - Ny begrepskatalog: ny-begrepsmodell.md
        - Byggmanifest: build-config.md
        - Kommandooversikt: kommandoar.md
    - Arkitektur og publisering:
        - Arkitekturoversikt: arkitektur-oversikt.md
        - Importhierarki: importhierarki.md
        - Valideringsreglar: valideringsregler.md
        - AP-NO arkitektur og avvik: ap-no-arkitektur.md
        - Bruk frå eksternt repo: ekstern-bruk.md
        - Publiseringsflyt: publisering-oversikt.md
        - Publiser til Felles Begrepskatalog: publisering-begrep.md
        - Publiser til Felles Datakatalog: publisering-modell.md
    - Korleis artefaktar vert generert:
        - Artefaktgenerering — kjelder og pipeline: artefakt-generering.md
        - Generering av modell-dokumentasjon: index-md-struktur.md
        - Generering av modellmanifest: modellmanifest-generering.md
        - README-tabellgenerering: readme-tabellgenerering.md
    - Monitorering av automasjon: monitorering.md
    - Om dette repoet: om.md
```

Dette er **eit større tiltak** enn det brukaren opphavleg spurte om (flytter
også eksisterande sider, ikkje berre dei to nye), og er difor markert som
valfri Fase 3 i handlingslista — ikkje noko som gjerast implisitt saman med
publiseringa av dei to nye sidene.

## Anbefaling (samla)

1. Flytt begge filene til NAV under "Rettleiingar" —
   `specs/backlog/artefakt-generering.md` → `mkdocs/docs/artefakt-generering.md`
   og `specs/backlog/arkitektur-oversikt.md` → `mkdocs/docs/arkitektur-oversikt.md`
   (§ "Flytting av backlog-filene" under — krev oppdaterte kryssreferansar i
   to `bugs/*.md`-filer, sjå same seksjon)
2. Gjer den låge-risiko nav-fiksen for `readme-tabellgenerering.md` samstundes
   — same runde, uavhengig funn, éin linje
3. Rett den interne duplikasjonen i `publisering-oversikt.md` (§ 3.2 punkt 1)
   og kort ned dei mest openbare gjentakingane (§ 3.1-tabellen) — moderat
   omfang, gjer portalen meir stringent utan å skrive om heile sider
4. **Ikkje** gjer den fulle nav-grupperinga (§ 4.2) eller filnamn-oppryddinga
   av `publisering-oversikt.md` (§ 4.1) i same runde — begge er gyldige,
   men større/meir synlege endringar som brukaren bør ta eit eksplisitt val
   om, ikkje noko som skjer som ein bieffekt av å publisere to nye sider

## Flytting av backlog-filene: kva må oppdaterast

**Brukaren har bestemt at dei to filene skal flyttast** frå
`specs/backlog/` til `mkdocs/docs/`, ikkje kopierast (som runde 1-2 av denne
specen la opp til). Det finst difor ikkje lenger to versjonar å halde
synkroniserte — DRY-spørsmålet frå tidlegare versjonar av specen ("manuell
kopi vs. automatisert kopiering i `publish.sh`") **fell bort**.

Flyttinga krev likevel at éin kjend avgrensing vert handtert eksplisitt, ikkje
oversett:

`specs/backlog/artefakt-generering.md` er eit kryssreferansemål med faste
§-nummer frå to filer, begge med filstien skriven direkte i teksten (t.d.
*"sjå `specs/backlog/artefakt-generering.md` § 5"*):

- `bugs/informasjonsmodell-instance-stale-metadata-sti.md` (§ 5, § 3.6)
- `bugs/valideringslogg-json-inkonsistent-skjema.md` (§ 3.5)

Dersom fila flyttast utan at desse to referansane vert oppdaterte, peikar dei
på ein filsti som ikkje lenger finst. **Krav ved flytting (ikkje valfritt):**

1. Behald §-nummereringa uendra i `mkdocs/docs/artefakt-generering.md` —
   nummera (§ 3.5, § 3.6, § 5 osv.) er sjølve ankeret referansane brukar,
   ikkje berre filstien i seg sjølv
2. Oppdater filstien i begge `bugs/*.md`-filene frå
   `specs/backlog/artefakt-generering.md` til
   `mkdocs/docs/artefakt-generering.md` (3 førekomstar totalt: 2 i
   `informasjonsmodell-instance-stale-metadata-sti.md`, 1 i
   `valideringslogg-json-inkonsistent-skjema.md`)

`specs/backlog/arkitektur-oversikt.md` har **ingen** slike harde §-referansar
frå `bugs/*.md` (verifisert med grep) — einaste kryssreferanse til fila er
den mjuke sjanger-tilvisinga i `artefakt-generering.md` si eiga innleiing
("same sjanger som..."), som uansett strippast bort ved flytting (§ under).
Denne fila kan flyttast utan følgjefeil andre stader.

Innhaldstilpassinga som var planlagd for kopiane i tidlegare versjonar av
specen, gjeld like fullt for dei flytta filene:

- **`artefakt-generering.md`:** behald §-nummereringa (sjå krav over), fjern
  spec-konvensjons-innleiinga (linje 1-9), legg til
  `!!! note "Beskrivelse"`, kort ned § 5 (CI-orkestrering — **ikkje** § 3.5,
  som er "Validering" og skal stå urørt, sjå retting under) og § 3.6
  (manifest) til korte peikarar mot `monitorering.md` og
  `modellmanifest-generering.md` (§ 3.1-tabellen)
- **`arkitektur-oversikt.md`:** fjern spec-konvensjons-innleiinga (linje 3-6),
  legg til `!!! note "Beskrivelse"`, legg til eksplisitt lenkje til
  `publisering-oversikt.md` i "Nasjonale katalogar"-forklaringspunktet
  (i staden for å la "Konsumenter"-skildringa stå som ei sjølvstendig
  gjentaking av same innhald)

**Korleis flytte, ved utføring:** vanleg filsystem-`mv`, **ikkje** `git mv` —
CLAUDE.md sitt forbod mot at LLM utfører versjonskontroll-endrande
git-kommandoar (`git add`/`commit`/`push`/`stash` "eller andre
git-kommandoar som endrar versjonskontroll-tilstand") gjeld likt for
`git mv`. Brukaren stagar/committar flyttinga sjølv — `git add` fangar opp
endringa som ei rename dersom innhaldet framleis er tilstrekkeleg likt etter
tilpassinga, elles som delete+add. Begge er greitt; det er brukaren sitt val.

## Funn frå konsolideringsgjennomgang (Anbefaling punkt 3, utført)

Utført isolert frå Fase 1 (dei to nye sidene er framleis ikkje publiserte —
`mkdocs/docs/artefakt-generering.md` og `mkdocs/docs/arkitektur-oversikt.md`
finst ikkje enno). Konsolideringsarbeidet vart difor avgrensa til det som
faktisk kunne rettast blant dei fire **allereie publiserte** sidene.

### 1. Slått saman "Dataflyt"- og "Workflow"-seksjonane i `publisering-oversikt.md`

Bekrefta funnet frå § 3.2 punkt 1: dei to seksjonane (linje 249-339 i
opphavleg versjon) skildra nøyaktig same fem-seks steg to gonger — éin gong
som to Mermaid sequence-diagram, éin gong som nummerert bash-gjennomgang —
utan kryssvising mellom dei, og med "Tidsbruk"-opplysningar spreidd og
delvis inkonsistente (`3-5 minutt` vs. `~3-5 minutt`, `minutt til dagar` vs.
`Varierer — frå minutt til dagar`).

**Endring:** Slått saman til éin seksjon **"Frå commit til synleg på
data.norge.no"** som held begge presentasjonsforma (diagram *og*
kommandolinje), men som no eksplisitt er strukturert som to komplementære
visningar av det **same** stegsettet i staden for to uavhengige
gjennomgangar. Nummereringa i kommandolinje-delen (1-5) er justert til å
matche diagramma sine "steg 1-4"/"steg 5-6"-nemningar. Ingen ekstern fil
lenkja til dei gamle overskrift-ankera (`#dataflyt-fra-yaml-til...`,
`#workflow-fra-commit-til...` — verifisert med grep før endring), så
samanslåinga braut ingen lenkjer.

**Fil:** `mkdocs/docs/publisering-oversikt.md`

### 2. Kryssleenkja "Pull, ikkje push"-forklaringa frå `monitorering.md`

Det opphavlege funnet i § 3.1-tabellen ("monitorering.md sin
Avgrensingar-seksjon seier same ting med andre ord") viste seg å vere meir
nyansert ved nærare lesing: `monitorering.md` har alt ei lenkje til
`publisering-oversikt.md` i botn-seksjonen "Sjå òg", så det er ikkje ei
reint udokumentert duplisering. Problemet er at lenkja står **langt unna**
sjølve "Avgrensingar"-seksjonen (nedst på sida), så ein lesar som møter
utsegna "repoet kan ikkje overvake ekstern hausting" midt i sida får ikkje
forklart **kvifor** før dei eventuelt scroller heilt ned.

**Endring:** Lagt til éi innleiingssetning øvst i "Avgrensingar"-seksjonen
som peikar direkte til "Pull, ikkje push"-prinsippet i
`publisering-oversikt.md`, i staden for å la lesaren støyte på konsekvensen
utan kontekst om årsaka.

**Fil:** `mkdocs/docs/monitorering.md`

### 3. Ikkje utført — avhengig av Fase 1

Desse radene frå § 3.1-tabellen kunne **ikkje** konsoliderast no, sidan dei
involverer sider som ikkje er publiserte enno:

- **Private/eksterne konsumentar** (`arkitektur-oversikt.md` sitt
  Konsumenter-diagram vs. `publisering-oversikt.md` sin "Private system
  som kan høste"-seksjon) — ingen endring gjort, `publisering-oversikt.md`
  sin versjon står som han er
- **"Kvar genererte filer endar"** — same status, ingen publisert motpart
  å kryssleenkje mot enno
- **CI-workflow-skildringar** (`artefakt-generering.md` § 5 skal kortast
  ned når fila vert tilpassa for portalen, jf. "Flytting av
  backlog-filene" over) — uendra
- **Manifest-generering** (`artefakt-generering.md` § 3.6 skal kortast ned
  til peikar mot `modellmanifest-generering.md`) — uendra,
  `modellmanifest-generering.md` sjølv treng ingen endring

Desse fire punkta bør handterast som del av Fase 1 (når dei to nye sidene
faktisk vert flytta/tilpassa/publiserte), ikkje som eit eige steg — sjølve
tilpassings-instruksen for kortare § 3.5/§ 3.6 og eksplisitt lenkje frå
arkitektur-oversikt.md ligg alt i "Flytting av backlog-filene"-seksjonen
over.

## Funn frå utføring av Fase 1 og 2

Fase 1 (tiltak 1-4) og Fase 2 (tiltak 5-7) er no utførte i sin heilskap.

**Feil oppdaga og retta undervegs:** teksten i "Flytting av
backlog-filene" (og opphavleg "Viktig avgrensing") sa feilaktig "kort ned
§ 3.5 (CI-orkestrering)". § 3.5 i `artefakt-generering.md` er **Validering**
(`validation/<versjon>/<policy>.json`) — ho er sjølve grunnlaget for
BUG-12-referansen frå `bugs/valideringslogg-json-inkonsistent-skjema.md` og
inneheld unikt innhald (ingen annan side dekkjer dei tre valideringslogg-
skrivevegane eller `validation_log.py`-konsolideringa). Ho skal difor
**ikkje** kortast ned. CI-orkestrering er faktisk **§ 5** (eit eige
toppnivå-avsnitt, ikkje eit underavsnitt av § 3). Retta i teksten over —
utføringa brukte den korrekte § 5, ikkje § 3.5.

**§ 3.6 og § 5 korta ned som planlagt**, med lenkjer til høvesvis
`modellmanifest-generering.md` og `monitorering.md`. §-numra sjølve
(3.5, 3.6, 5) er identiske med før flyttinga, så kryssreferansane frå
`bugs/*.md` peikar framleis til meiningsfulle avsnitt.

**Punkt 7 (kryssleenking) er no fullført**, ikkje berre delvis: sidan dei to
nye sidene faktisk finst, kunne dei resterande fire radene frå § 3.1-tabellen
løysast:
- "Publiserte pull-punkt" og "Nasjonale katalogar" i `arkitektur-oversikt.md`
  peikar no eksplisitt til `publisering-oversikt.md` for detaljar
- "Konsumentar"-bolken i `arkitektur-oversikt.md` er korta ned — dei tre
  tidlegare separate underpunkta for private datakatalogar/dataplattformer/
  API-gateway (som gjentok formatdetaljane frå `publisering-oversikt.md`
  sin "Private system som kan høste") er slått saman til éitt punkt med
  lenkje dit. KUDAF-forklaringa (unikt innhald) står urørt
- `artefakt-generering.md` § 5 peikar til `monitorering.md` for
  `validate.yml`-detaljar (logglagring, PR-oppretting), og behalde sjølv
  den unike `ensure-images`/container-detaljen som ikkje står i
  `monitorering.md`
- `artefakt-generering.md` § 3.6 peikar til `modellmanifest-generering.md`
  for feltkjelde-tabellen

Begge nye sidene har òg fått eigne "Sjå òg"-seksjonar som lenkjer til
kvarandre og til dei tre eksisterande overlappande sidene.

**`mkdocs/mkdocs.yml`** (den genererte fila, ikkje berre `publish.sh` sin
mal) vart òg oppdatert direkte, sjølv om han normalt vert regenerert av
`make docs-publish` — slik at lokal `mkdocs serve` mot noverande
repo-tilstand viser dei nye sidene utan at heile genererings-pipelinen må
køyrast først. Neste `make docs-publish` vil regenerere han likt uansett.

**Verifisert (oppfølgande økt):** `generated/` synte seg alt å vere fullt
bygd for alle 9 domene med naudsynte podman-images tilgjengelege lokalt, så
`make docs-publish && make docs-build` vart faktisk køyrt. `docs-build`
(statisk mkdocs-bygg via container) fullførte med exit code 0 og null
WARNING/ERROR-linjer — ingen av dei eksisterande INFO-nivå
lenkje-åtvaringane (om domenekryssreferansar utan `index.md`-suffiks,
pre-eksisterande og urelatert til denne specen) nemner nokon av dei nye
eller endra filene. `docs-serve` (interaktiv, blokkerande server) vart
ikkje køyrt — unødvendig når `docs-build` alt validerer at heile portalen
byggjer feilfritt.

## Funn frå Fase 3-utføring (etter eksplisitt brukarval)

Brukaren vart spurd eksplisitt om dei to Fase 3-tiltaka (§ "Anbefaling"
punkt 4 sa desse ikkje skulle gjerast som ein bieffekt):

- **Tiltak 8 (nesta NAV-gruppering): JA** — implementert i
  `mkdocs/publish.sh` sin `nav:`-heredoc nøyaktig som skissert i § 4.2
  (gruppene "Kom i gang" / "Arkitektur og publisering" / "Korleis
  artefaktar vert generert", pluss `monitorering.md` og `om.md` som
  ugrupperte toppnivå-oppføringar). Verifisert med `make docs-publish`
  (mkdocs.yml regenerert med korrekt nesta struktur) og `make docs-build`
  (bygg feilfritt med den nye nav-strukturen)
- **Tiltak 9 (omdøyp `publisering-oversikt.md`): NEI** — brukaren valde å
  behalde filnamnet, i tråd med anbefalinga i § 4.1 (lenkjerisiko for den
  offentlege GitHub Pages-URL-en oppvegde ikkje den kosmetiske gevinsten)

## Handlingsliste

**Fase 1 — flytt dei to nye sidene (kjernen i oppgåva):**

- [x] 1. Flytt `specs/backlog/artefakt-generering.md` →
      `mkdocs/docs/artefakt-generering.md` (filsystem-`mv`, ikkje `git mv`)
      og tilpass innhaldet for portalen — **utført**
- [x] 2. Flytt `specs/backlog/arkitektur-oversikt.md` →
      `mkdocs/docs/arkitektur-oversikt.md` (filsystem-`mv`, ikkje `git mv`)
      og tilpass innhaldet for portalen — **utført**
- [x] 3. Oppdater filstig-referansane i
      `bugs/informasjonsmodell-instance-stale-metadata-sti.md` (§ 5, § 3.6)
      og `bugs/valideringslogg-json-inkonsistent-skjema.md` (§ 3.5) —
      **utført**, verifisert med grep (null treff på gamal sti)
- [x] 4. Legg til begge i `mkdocs/publish.sh` sin `nav:`-heredoc — **utført**,
      same endring spegla i `mkdocs/mkdocs.yml` direkte (sjå "Funn" over)

**Fase 2 — låg-risiko oppryddingar same runde:**

- [x] 5. Legg til `readme-tabellgenerering.md` i `nav:`-heredoc — **utført**
- [x] 6. Slå saman "Dataflyt"- og "Workflow"-seksjonane i
      `publisering-oversikt.md` — **utført** (frå tidlegare økt)
- [x] 7. Kryssleenk dei seks sidene der § 3.1-tabellen peikar på overlapp —
      **fullført** (sjå "Funn" over for dei fire attverande punkta)

**Fase 3 — valfritt, større omfang (krev eksplisitt brukarval, sjå § 4.2):**

- [x] 8. Nesta NAV-gruppering av Rettleiingar-seksjonen ("Kom i gang" /
      "Arkitektur og publisering" / "Korleis artefaktar vert generert") —
      **utført** etter eksplisitt "ja" frå brukaren. Verifisert med
      `make docs-publish` (mkdocs.yml regenerert med korrekt nesta struktur)
      og `make docs-build` (feilfritt bygg, null nye WARNING/ERROR, alle tre
      gruppenamn stadfesta i `mkdocs/site/index.html`)
- [x] 9. Vurder omdøyping av `publisering-oversikt.md` → `publiseringsflyt.md`
      for filnamn/H1/nav-konsistens (§ 4.1) — **vurdert og avvist** etter
      eksplisitt "nei" frå brukaren (lenkjerisiko for offentleg URL vog
      tyngre enn kosmetisk gevinst). Filnamnet står uendra

**Verifisering:**

- [x] 10. `make docs-publish && make docs-build` — **utført**: `generated/`
      var alt bygd (9 domene, alle podman-images tilgjengelege lokalt), så
      `docs-publish` var raskt (~3 min). `docs-build` (statisk mkdocs-bygg,
      428s) fullførte med exit code 0, **null** WARNING/ERROR-linjer, og
      ingen av dei INFO-nivå lenkje-åtvaringane (alle pre-eksisterande,
      om domenekryssreferansar utan `index.md`-suffiks) nemner nokon av dei
      nye/endra filene. Begge nye sidene stadfesta til stades i
      `mkdocs/site/` med korrekt nav-tittel. `docs-serve` (interaktiv,
      blokkerande server) vart ikkje køyrt — unødvendig når `docs-build`
      alt validerer at heile sida byggjer feilfritt
- [x] 11. `grep -rn "specs/backlog/artefakt-generering.md" bugs/` — **null
      treff, stadfesta**

## Utført (2026-08-07)

Alle 11 tiltak i handlingslista er fullførte, inkludert begge Fase
3-tiltaka (utført etter eksplisitt brukarval — sjå "Funn frå
Fase 3-utføring"). Endra/nye/sletta filer:

- **Nye:** `mkdocs/docs/artefakt-generering.md`, `mkdocs/docs/arkitektur-oversikt.md`
- **Sletta:** `specs/backlog/artefakt-generering.md`, `specs/backlog/arkitektur-oversikt.md` (flytta, ikkje kopierte)
- **Endra:** `mkdocs/publish.sh` (nav-heredoc: nye sider, `readme-tabellgenerering.md` lagt til, nesta gruppering), `mkdocs/docs/publisering-oversikt.md` (slått saman duplisert seksjon), `mkdocs/docs/monitorering.md` (kryssleenkje til "Pull, ikkje push"), `bugs/informasjonsmodell-instance-stale-metadata-sti.md` og `bugs/valideringslogg-json-inkonsistent-skjema.md` (oppdatert filsti-referanse)
- **Regenerert av `make docs-publish`** (ikkje manuelt redigert): `mkdocs/mkdocs.yml` (gitignora), `mkdocs/docs/referanse/referansemodell/index.md` (inkidental retting av eit stale make-target-namn i eit kodeeksempel, urelatert til denne specen si kjerne)

Verifisert med `make docs-publish && make docs-build` (to gonger — før og
etter Fase 3-nav-endringa): begge køyringar fullførte med exit code 0 og
null WARNING/ERROR-linjer.
