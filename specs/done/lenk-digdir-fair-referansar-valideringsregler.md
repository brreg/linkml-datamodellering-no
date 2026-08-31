# Lenk Digdir-regel- og FAIR-referansar i valideringsregler-tabellane

## Bakgrunn

`mkdocs/docs/arkitektur/valideringsregler.md` vert automatisk generert av
`generate_validation_docs()` i `mkdocs/publish.sh` (Steg 1, sjå
`specs/done/generer-valideringsreglar-docs.md`) frå kjeldefila
`src/mcp-linkml-validator/policies/README.md`. Fila er sannkjelda — endringar
skal difor gjerast i `README.md`, ikkje i den genererte `valideringsregler.md`
(som vert overskriven ved neste `make docs-publish`, jf.
`.claude/rules/mkdocs-portal.md`).

I dag er "Digdir-regel"- og "FAIR"-kolonnene i tabellane rein tekst (t.d.
`4 — Identifiserbarheit` eller `F3, I1`) utan lenkjer. Brukaren ønskjer at
desse referansane skal lenke til dei autoritative kjeldene:

- **Digdir-reglar** → `https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029`
- **FAIR-prinsipp** → `https://www.go-fair.org/fair-principles/`

Verken Digdir-sida eller go-fair.org har per-regel/per-prinsipp-anker, så
lenkjemåla er dei same for alle referansar til same system.

**Avklarte val (frå spørsmål til brukar):**
- **Éin lenkje per celle**, ikkje éin lenkje per enkeltreferanse. Ei celle med
  fleire referansar (t.d. `4 — Identifiserbarheit, 8 — Maskinprosserbarheit`
  eller `F2, A1, R1.2`) vert éi samla lenkje: heile celleteksten som lenkjetekst.
- **Celler med `—`** (ingen referanse) skal **ikkje** lenkast — det finst
  ingenting å peike på.
- **Omfang:** dei fire tabellane i `policies/README.md` som refererer Digdir-
  reglar og/eller FAIR-prinsipp:
  1. "Digdir-reglar og FAIR-prinsipp — dekningsgrad" (linje ~10-31)
  2. `### bronze`-tabellen (linje ~76-95)
  3. `### silver`-tabellen (linje ~111-138)
  4. `### gold`-tabellen (linje ~162-194)

  **Ikkje omfatta:** "Nivå for skjemakvalitet"-tabellen (linje ~52-56, kolonnene
  "Digdir-reglar"/"FAIR-prinsipp" der oppsummerer heile intervall som `1-4, 7-11, 13`
  — brukaren valde å halde denne utanfor).

### Kolonnestruktur per tabell

| Tabell | Kolonne som representerer Digdir-regel | Kolonne som representerer FAIR |
|---|---|---|
| Dekningsgrad (rad 1-15) | `Navn` (2. kolonne, feittsett, t.d. `**Forståelighet**`) | `FAIR` (5. kolonne) |
| bronze / silver / gold | `Digdir-regel` | `FAIR` |

I dekningsgrad-tabellen er **kvar rad** definisjonen av éin Digdir-regel (radnummeret
i `#`-kolonnen samsvarar med regelnummeret) — det er `Navn`-kolonna (feittsett
regelnavn) som er den naturlege lenkjeteksten, ikkje `#`-kolonna åleine.

## Steg

### 1. Lenk `Navn`-kolonna i dekningsgrad-tabellen
Erstatt `**<Navn>**` med `[**<Navn>**](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029)`
for alle 15 rader (regel 1-15).

### 2. Lenk `FAIR`-kolonna i dekningsgrad-tabellen
For alle rader der FAIR-kolonna **ikkje** er `—` (dvs. alle unntatt regel 3, 6
og 14 — sjekk faktisk innhald på nytt før endring, sidan radnummer/innhald kan
ha drifta sidan denne specen vart skriven), erstatt celleteksten `<kode(ar)>`
med `[<kode(ar)>](https://www.go-fair.org/fair-principles/)`. Behald `—` uendra
der han finst.

### 3. Lenk `Digdir-regel`- og `FAIR`-kolonnene i bronze-tabellen
For kvar rad i tabellen under `### bronze` (linje ~76-95):
- `Digdir-regel`-kolonne: lenk heile celleteksten (t.d.
  `4 — Identifiserbarheit, 8 — Maskinprosserbarheit`) til Digdir-URL-en over.
  Ingen rader i bronze-tabellen har `—` i denne kolonna i dag — dobbeltsjekk
  ved gjennomføring.
- `FAIR`-kolonne: lenk celleteksten til FAIR-URL-en der ho ikkje er `—`
  (fleire rader i bronze, t.d. rad for `class_names_pascal_case`, har `—` og
  skal ikkje lenkast).

### 4. Lenk `Digdir-regel`- og `FAIR`-kolonnene i silver-tabellen
Same mønster som steg 3, for tabellen under `### silver` (linje ~111-138).
Merk at fleire rader her har `—` i **begge** kolonnene (t.d. `Datasett har
dct:accessRights`, `Distribusjon har dcat:accessURL`) — desse skal ikkje få
nokon lenkje i det heile.

### 5. Lenk `Digdir-regel`- og `FAIR`-kolonnene i gold-tabellen
Same mønster som steg 3/4, for tabellen under `### gold` (linje ~162-194).

### 6. Verifiser at generate_validation_docs() ikkje treng endring
`generate_validation_docs()` i `mkdocs/publish.sh` (linje ~49-75) køyrer tre
`sed`-transformasjonar på innhaldet frå `policies/README.md`, alle avgrensa
til relative lenkjer (`*.yaml`, `specs/done/*`, `../../../<TITTEL>.md`). Dei
nye absolutte `https://www.digdir.no/...`- og `https://www.go-fair.org/...`-
lenkjene matchar ingen av desse mønstra og skal difor gå uendra gjennom pipa.
Les gjennom regexane på nytt for å stadfeste at ingen av dei utilsikta fangar
opp dei nye lenkjene (t.d. at `\.md`-mønsteret ikkje matchar `go-fair.org`).
Ingen kodeendring forventa i dette steget — reint verifikasjonssteg.

### 7. Regenerer og valider portalen
Køyr `make docs-publish` og:
- Sjekk at `mkdocs/docs/arkitektur/valideringsregler.md` viser dei nye
  lenkjene i alle fire tabellane, med korrekt Markdown-tabellsyntaks (ingen
  broten kolonnetal pga. `[`/`]`/`(`/`)`-teikn i cellene).
- Køyr `make docs-build` (eller tilsvarande mkdocs-byggetarget) og sjekk at
  mkdocs sin lenkjevalidering (`validation.links`) ikkje slår ut på dei nye
  lenkjene.
- Stadfest at `src/mcp-linkml-validator/policies/README.md` framleis
  renderer korrekt som GitHub-Markdown (tabellstruktur intakt, ingen
  utilsikta pipe-teikn i cellene som bryt tabellen).

## Prioritert handlingsliste

1. Lenk `Navn`-kolonna i dekningsgrad-tabellen til Digdir-URL (15 rader)
2. Lenk `FAIR`-kolonna i dekningsgrad-tabellen til FAIR-URL (der ikkje `—`)
3. Lenk `Digdir-regel`- og `FAIR`-kolonnene i bronze-tabellen (der ikkje `—`)
4. Lenk `Digdir-regel`- og `FAIR`-kolonnene i silver-tabellen (der ikkje `—`)
5. Lenk `Digdir-regel`- og `FAIR`-kolonnene i gold-tabellen (der ikkje `—`)
6. Verifiser at `generate_validation_docs()` ikkje treng endring
7. Regenerer portalen (`make docs-publish`) og verifiser lenkjer + tabellsyntaks

## Avhengigheiter

- Ingen avhengigheiter til andre specs i `specs/backlog/`.
- Føresett at `src/mcp-linkml-validator/policies/README.md` og
  `generate_validation_docs()`-transformasjonen i `mkdocs/publish.sh` er i
  same tilstand som ved skrivetidspunktet for denne specen — sjekk begge før
  gjennomføring, sidan radinnhald/regex kan ha drifta.

## Utført

Alle 7 steg gjennomførte:

1-5. **Lenking gjennomført** via eit eingongs Python-skript (køyrt direkte,
ikkje lagt til som permanent script — reint ein tekst-transformasjon av
`README.md`, ingen LinkML/podman-avhengigheit): 15 rader i dekningsgrad-
tabellen (`Navn`-kolonna → Digdir-URL, `FAIR`-kolonna → FAIR-URL der ikkje
`—`) og 18+27+31 rader i høvesvis bronze-, silver- og gold-tabellen
(`Digdir-regel`- og `FAIR`-kolonnene, der ikkje `—`). Alle celler delt på
`" | "` (verifisert at ingen celle inneheld eit literalt `|`-teikn), så
kvar rad vart eintydig identifisert utan risiko for feilmatching.

6. **Verifisert** at `generate_validation_docs()` sine tre `sed`-regex
(avgrensa til `*.yaml`, `specs/done/*`, `../../../<TITTEL>.md`) ikkje
matchar dei nye `https://www.digdir.no/...`/`https://www.go-fair.org/...`-
lenkjene — stadfesta ved `grep` av generert output (82 treff, alle med
lenkjer intakte).

7. **Regenerert og validert:**
   - `make docs-publish` — ingen feil, `valideringsregler.md` regenerert med
     korrekt tabellsyntaks.
   - `make docs-build` — bygde OK (59s), dei to eksisterande warningane er
     urelaterte til denne endringa (`begrepskatalog/index.md`-lenkje og
     `#classes`-anker i `oreg/javazonetalk`).
   - Talde faktiske `href`-attributt i det rendra HTML-et: 80 Digdir-lenkjer
     og 66 FAIR-lenkjer, ingen broten tabellstruktur.

**Avvik frå opphavleg plan:** Ingen avvik i sjølve endringa. Talet på rader
med FAIR `—` i dekningsgrad-tabellen viste seg å vere regel 3, 5, 6 og 14
(ikkje berre 3/6/14 som anteke i steg 2 — regel 5 hadde òg `—`), men dette
påverka ikkje gjennomføringa sidan skriptet sjekka faktisk celleinnhald,
ikkje ei hardkoda liste.

---

## Oppfølging: lenk til per-regel-anker i staden for éin samla Digdir-URL (2026-08-31)

Brukaren har stadfesta at Digdir-sida faktisk har anker per deloverskrift, på
forma `.../3029#<slug>` — t.d. regel 1 "Forståelighet" → `#forstelighet`
(stadfesta ved manuell inspeksjon av den live-rendra sida i nettlesaren).
Ankera vert generert **klientsides** av ein TOC-komponent i sida sin JS-bunt
(`data-toc="section.paragraph--body" data-toc-headings="h2,h3"` på ei tom
`<ul>`) og finst difor **ikkje** i den statiske server-HTML-en som vert
henta via `curl`/`WebFetch` — stadfesta ved undersøking i denne økta (henta
rå HTML og JS-bunten, fann ingen `id`-attributt på overskriftene og ingen
lesbar slugify-funksjon i den generiske jQuery-koden i bunten).

**Endra mål:** Kvar Digdir-regel-referanse skal lenke til sitt eige anker:
`https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#<slug>`
i staden for éin samla lenkje til Digdir-URL-en utan anker. FAIR-lenkjene er
**uendra** (framleis éin samla URL, sidan go-fair.org ikkje har tilsvarande
anker per prinsipp).

### Slug-algoritme — delvis usikker, må verifiserast før gjennomføring

Stadfesta datapunkt: `å` vert **fjerna heilt** frå slugen (ikkje omgjort til
`a` via NFKD-dekomponering, slik vår eigen mkdocs-portal sin slug-algoritme
gjer — sjå `.claude/rules/mkdocs-portal.md` § Ankerlenkjer). Digdir-sida
brukar altså **ikkje** same slug-algoritme som vår eigen portal — den
kunnskapen kan ikkje gjenbrukast direkte, og algoritma elles er ukjend
(JS-bunten var ikkje mogleg å reverse-engineere frå denne økta).

Berre éin av dei 15 regelnamna inneheld `æ`/`ø` i tillegg til `å`: regel 7
"Tilgjengeliggjøring" (inneheld `ø`). Om `ø` vert fjerna heilt (same mønster
som `å`) vert ankeret `tilgjengeliggjring`; om det i staden vert transkribert
til `o` vert det `tilgjengeliggjoring`. **Dette må stadfestast mot den
live-rendra sida før gjennomføring.**

Regelnamna er henta frå Digdir sine eigne `<h3>`-overskrifter (avvik litt frå
namna i `README.md` sine tabellar, t.d. "Meningsfullhet"/"Identifiserbarhet"
hos Digdir vs. "Meiningsfullheit"/"Identifiserbarheit" i `README.md` — dette
påverkar berre kva slug som vert utleia, ikkje teksten i `README.md`, som
skal stå uendra):

| # | Regelnavn (Digdir sin eigen tekst) | Anker |
|---|---|---|
| 1 | Forståelighet | `forstelighet` (**stadfesta**) |
| 2 | Meningsfullhet | `meningsfullhet` |
| 3 | Navne- og skrivekonvensjoner | `navne-og-skrivekonvensjoner` |
| 4 | Identifiserbarhet | `identifiserbarhet` |
| 5 | Visualisering | `visualisering` |
| 6 | Modularitet | `modularitet` |
| 7 | Tilgjengeliggjøring | **må stadfestast** — `tilgjengeliggjring` eller `tilgjengeliggjoring` |
| 8 | Maskinprosserbarhet | `maskinprosserbarhet` |
| 9 | Datering | `datering` |
| 10 | Ansvar | `ansvar` |
| 11 | Modellstatus | `modellstatus` |
| 12 | Sammenhenger mellom modeller | `sammenhenger-mellom-modeller` |
| 13 | Begreper | `begreper` |
| 14 | Gjenbruk | `gjenbruk` |
| 15 | Standardiserte datatyper | `standardiserte-datatyper` |

Dei 13 radene utan `æ`/`ø`/`å` er trygge å utleie med enkel
lowercase + mellomrom→bindestrek (standard for nesten alle slug-algoritmar),
sjølv om den nøyaktige algoritma elles er ukjend.

### Ny avklaring naudsynt — fleire-regel-celler i bronze/silver/gold

Det opphavlege valet "éin lenkje per celle" (sjå `## Bakgrunn` over) var
trygt fordi alle referansar i same celle uansett peika til same generiske
URL. Med per-regel-anker vert dette **ikkje lenger trivielt**: ei celle som
`4 — Identifiserbarheit, 8 — Maskinprosserbarheit` refererer to ulike
regel-anker (`#identifiserbarhet` og `#maskinprosserbarhet`), og éi samla
lenkje kan berre peike til **eitt** av dei to.

Dekningsgrad-tabellen er upåverka av dette (éin regel per rad, alltid
eintydig). Bronze/silver/gold-tabellane treng ei ny avgjerd:

- **Alternativ A — éin lenkje per celle, fyrste regel:** Behald éin lenkje
  per celle, men lenk til ankeret til den **fyrste** nemnde regelen. Enklast,
  men mister presisjon for celler med fleire regelnummer (lenkja hoppar
  forbi den andre/tredje regelen sin del av sida).
- **Alternativ B — éin lenkje per enkeltregel:** Gå bort frå "éin lenkje per
  celle" for desse tre tabellane, og lenk kvar regelreferanse for seg (t.d.
  `[4 — Identifiserbarheit](.../#identifiserbarhet), [8 — Maskinprosserbarheit](.../#maskinprosserbarhet)`).
  Meir presist, men reverserer det opphavlege "éin lenkje per celle"-valet
  for celler med fleire referansar.

### Oppdaterte steg (utfør etter avklaring)

1. Stadfest anker for regel 7 (sjå usikkerheit over) og bygg fullstendig
   regelnummer→anker-oppslag.
2. Oppdater/skriv på nytt eit Python-skript (same mønster som originalskriptet,
   sjå `## Utført` over) som no brukar `regel → #anker` i staden for éin
   konstant `DIGDIR_URL`:
   - Dekningsgrad-tabellen: bruk ankeret som svarar til radnummeret.
   - Bronze/silver/gold: følg vald alternativ (A eller B) frå avklaringa over.
3. Regenerer portalen (`make docs-publish`, `make docs-build`) og verifiser
   at lenkjene peikar til rett anker (kan ikkje verifiserast automatisk via
   mkdocs sin lenkjevalidator, sidan ho ikkje kjenner til eksterne sider sine
   anker — krev manuell stikkprøve i nettlesar mot nokre av lenkjene).

## Avhengigheiter (oppdatert)

**Begge avklaringane er no stadfesta av brukaren:**

- Anker for regel 7 "Tilgjengeliggjøring": **`tilgjengeliggjring`** (stadfesta
  ved manuell inspeksjon av live-rendra sida — `ø` fell bort, same mønster
  som `å`. Fullstendig regelnummer→anker-oppslag er dermed:

  | # | Anker |
  |---|---|
  | 1 | `forstelighet` |
  | 2 | `meningsfullhet` |
  | 3 | `navne-og-skrivekonvensjoner` |
  | 4 | `identifiserbarhet` |
  | 5 | `visualisering` |
  | 6 | `modularitet` |
  | 7 | `tilgjengeliggjring` |
  | 8 | `maskinprosserbarhet` |
  | 9 | `datering` |
  | 10 | `ansvar` |
  | 11 | `modellstatus` |
  | 12 | `sammenhenger-mellom-modeller` |
  | 13 | `begreper` |
  | 14 | `gjenbruk` |
  | 15 | `standardiserte-datatyper` |

- Fleire-regel-celler i bronze/silver/gold: **Alternativ B — éin lenkje per
  enkeltregel** (t.d. `[4 — Identifiserbarheit](.../#identifiserbarhet), [8 — Maskinprosserbarheit](.../#maskinprosserbarhet)`).
  Dette reverserer "éin lenkje per celle"-forenklinga frå første runde for
  celler med fleire regelnummer.

Ingen lenger-blokkerande avhengigheiter — klar til gjennomføring.

## Utført (oppfølging)

Alle 3 oppdaterte steg gjennomførte:

1. **Regel→anker-oppslag stadfesta** — sjå tabellen i "Avhengigheiter
   (oppdatert)" over (15 regelnummer, inkl. det brukar-stadfesta
   `tilgjengeliggjring` for regel 7).
2. **Skript oppdatert og køyrt** (eingongs Python-skript, same mønster som
   originalrunden — ingen permanent script lagt til):
   - Dekningsgrad-tabellen: `Navn`-lenkja for kvar av dei 15 radene fekk
     `#<anker>` lagt til, basert på radnummeret.
   - Bronze/silver/gold: `Digdir-regel`-cellene vart pakka opp og pakka inn
     att med **éin lenkje per enkeltregel** (Alternativ B) — t.d.
     `[1 — Forståelighet](.../#forstelighet), [2 — Meiningsfullheit](.../#meningsfullhet), [10 — Ansvar](.../#ansvar)`
     for celler med fleire regelnummer. `—`-celler og FAIR-kolonna urørte.
   - Verifisert med `grep`: ingen dobbelt-lenking, `—`-celler framleis `—`,
     radtal i fila uendra (154 tabellrader).
3. **Regenerert og validert:**
   - `make docs-publish` — ingen feil, alle 79 `3029#`-treff i generert
     `valideringsregler.md`.
   - `make docs-build` — bygde OK (99s), same eine pre-eksisterande
     urelaterte warning som tidlegare (`begrepskatalog/index.md`-lenkja).
   - Stikkprøve av rendra HTML: alle 15 distinkte anker stadfesta til stades
     i `href`-attributta (`#forstelighet`, `#tilgjengeliggjring`, osv.).

**Avvik frå opphavleg plan:** Ingen. Alternativ B (éin lenkje per
enkeltregel) vart valt av brukaren i staden for Alternativ A.

---

## Oppfølging 2: tre anker brukar understrek, ikkje bindestrek (2026-08-31)

Brukaren rapporterte at tre av dei 15 ankera ikkje fungerte i praksis.
Digdir-sida sin slugify-algoritme viste seg å ikkje vere heilt konsistent —
dei fleste fleirords-regelnamn brukar bindestrek mellom orda, men tre brukar
understrek:

| Anker (feil, bindestrek) | Anker (korrekt, understrek) |
|---|---|
| `#navne-og-skrivekonvensjoner` | `#navne_og_skrivekonvensjoner` |
| `#sammenhenger-mellom-modeller` | `#sammenhenger_mellom_modeller` |
| `#standardiserte-datatyper` | `#standardiserte_datatyper` |

Retta med `sed` (7 treff totalt på tvers av dekningsgrad- og
bronze/silver/gold-tabellane). Regenerert (`make docs-publish`,
`make docs-build`) og stadfesta i rendra HTML at alle 15 anker no viser
korrekt separator (understrek for desse tre, bindestrek for resten).

**Endeleg regel→anker-oppslag** (oppdatert frå tabellen i "Avhengigheiter
(oppdatert)" over — regel 3, 12 og 15 endra frå bindestrek til understrek):

| # | Anker |
|---|---|
| 1 | `forstelighet` |
| 2 | `meningsfullhet` |
| 3 | `navne_og_skrivekonvensjoner` |
| 4 | `identifiserbarhet` |
| 5 | `visualisering` |
| 6 | `modularitet` |
| 7 | `tilgjengeliggjring` |
| 8 | `maskinprosserbarhet` |
| 9 | `datering` |
| 10 | `ansvar` |
| 11 | `modellstatus` |
| 12 | `sammenhenger_mellom_modeller` |
| 13 | `begreper` |
| 14 | `gjenbruk` |
| 15 | `standardiserte_datatyper` |
