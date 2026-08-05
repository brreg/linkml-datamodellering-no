# Konsistens mellom bronze-, silver- og gold-tabellane i policies/README.md

## Bakgrunn

Evaluering av dei tre tabellane under `## Kvalitetspolicyer` i
`src/mcp-linkml-validator/policies/README.md` (bronze: linje 68-86, silver:
102-127, gold: 143-152) avdekte fire avvik i format og innhald:

1. **Ulikt kolonnetal.** Bronze har 4 kolonnar (`Sjekk | Alvor | Digdir-regel | FAIR`).
   Silver og gold har 5 (+ `Skildring`).
2. **Ulikt Digdir-regel-format.** Bronze og silver sine livssyklus-/instansrader
   brukar `N — Namn` (t.d. `4 — Identifiserbarheit`). Gold og silver sine
   klasse-slot-rader brukar berre tal (`4`, `1, 2, 10`).
3. **Gold-tabellen er ufullstendig.** Innleiingsteksten («Alle brot gir `error`
   — også dei som er åtvarslane på bronse») lovar at gold dekkjer alle bronse-
   sjekkane, men berre 8 av bronse sine 17 sjekkar har eiga rad i gold.
   Dette gjer m.a. at «Nivå for skjemakvalitet»-tabellen (linje 56) sin
   påstand om at gold dekkjer FAIR A2 ikkje har støtte i gold-detaljtabellen.
4. **Feil «oppgradert»-påstand.** Gold-rada for `schema.id er HTTP(S)-URI`
   (linje 145) seier «arva frå bronse, oppgradert til error» — men denne
   sjekken er **allereie** `error` i bronse (linje 71), så det er ingenting
   å oppgradere.

## Avklarte val (frå brukardialog)

- **Digdir-regel-format:** Standardiser på `N — Namn` overalt (meir informativt).
- **Gold-fullstendigheit:** Legg til alle manglande bronse-sjekkar som eigne
  gold-rader (realiser innleiingsteksten sin påstand bokstaveleg).
- **Silver klasse-slot-presisjon:** **Ikkje** endra — behald dagens klasse-
  nivå-verdiar duplisert per utflata slot-rad (unngår å dikte opp ny per-slot-
  mapping utan kjeldegrunnlag).
- **Silver instans-alvor:** **Ikkje** splitt i fleire rader — behald
  fleirverdi-alvor (`error/warning/info`) som éi rad, sidan alvoret er reelt
  dynamisk og ikkje tre uavhengige sjekkar.

**Eksplisitt utanfor scope:** Toppseksjonane «Digdir-reglar og FAIR-prinsipp
— dekningsgrad» (linje 10-31) og «Nivå for skjemakvalitet» (linje 50-56) har
eigne, pre-eksisterande avvik (t.d. manglar regel 6 — Modularitet — frå
silver/gold sine regel-lister sjølv om begge arvar han frå bronse). Dette er
ikkje del av denne spec-en — berre dei tre `## Kvalitetspolicyer`-tabellane
vert endra.

## Relevante filer

- `src/mcp-linkml-validator/policies/README.md` — einaste fila som skal endrast

## Steg

### 1. Legg til Skildring-kolonne i bronze-tabellen

Erstatt bronze-tabellen (linje 68-86) med:

```markdown
| Sjekk | Alvor | Digdir-regel | FAIR | Skildring |
|---|---|---|---|---|
| `schema.id` til stades | error | 4 — Identifiserbarheit | F1 | Persistent identifikator for skjemaet |
| `schema.id` er HTTP(S)-URI | error | 4 — Identifiserbarheit | F1 | Sikrar at identifikatoren er ein oppløyseleg URI |
| `schema.name` til stades | error | 1 — Forståelighet | — | Maskinlesbart namn for skjemaet |
| `schema.title` til stades | error | 1 — Forståelighet, 2 — Meiningsfullheit | F2 | Menneskelesbar tittel |
| `schema.default_prefix` til stades | error | 4 — Identifiserbarheit | — | Standardnamnerom for lokale identifikatorar |
| `schema.default_prefix` er absolutt HTTPS-URI med avsluttande `/` | error | 4 — Identifiserbarheit | — | Sikrar korrekt URI-konstruksjon for lokale ressursar |
| `schema.description` til stades | warning | 1 — Forståelighet | F2 | Fritekstskildring av skjemaet sitt føremål |
| `schema.version` til stades | warning | 9 — Datering | F4 | Versjonsnummer for sporbarheit |
| `schema.license` til stades | warning | 7 — Tilgjengeleggjering | R1.1 | Lisens for gjenbruk av skjemaet |
| Skjema har ikkje fleire enn 50 klasser (unntatt `tree_root`) | warning | 6 — Modularitet | — | Handterleg mengde modellelement per modul |
| Alle klassenamn startar med stor bokstav (PascalCase) | warning | 3 — Navne- og skrivekonvensjoner | — | Konsistent namngjevingskonvensjon for klasser |
| Alle slotnamn er snake_case (berre `a-z`, `0-9`, `_` — **ikkje bindestreker**) | warning | 3 — Navne- og skrivekonvensjoner | — | Konsistent namngjevingskonvensjon for eigenskapar |
| Alle klasser (unntatt `tree_root`) har `class_uri` | warning | 4 — Identifiserbarheit, 8 — Maskinprosserbarheit | F3, I1 | Mappar klassen til RDF-vokabular |
| Alle globale slots har `slot_uri` | warning | 4 — Identifiserbarheit, 8 — Maskinprosserbarheit | I1 | Mappar eigenskapen til RDF-vokabular |
| Alle klasser (unntatt `tree_root`) har identifikator-slot | warning | 4 — Identifiserbarheit | F1 | Sikrar at instansar av klassen kan identifiserast unikt |
| Alle klasser (unntatt `tree_root`) har `annotations.begrepsidentifikator` | warning | 13 — Begreper | A2 | Koplar modellelement til fagomgrep i begrepskatalog |
| Slots med kontrollerte vokabular har korrekte annotations | warning | 8 — Maskinprosserbarheit | I1 | Sikrar maskinlesbar dokumentasjon av vokabularkrav |
```

Fotnotane rett under tabellen (`snake_case`-format, Kontrollerte vokabular) er uendra.

### 2. Legg namn til Digdir-regel i silver sine klasse-slot-rader

I silver-tabellen (linje 102-127), oppdater Digdir-regel-kolonnen for
klasse-slot-radene (Katalog/Katalogpost/Datasett/Distribusjon/Datatjeneste/Aktør)
frå tal-berre til `N — Namn`:

| Noverande verdi | Ny verdi |
|---|---|
| `1, 2, 10` | `1 — Forståelighet, 2 — Meiningsfullheit, 10 — Ansvar` |
| `9` | `9 — Datering` |
| `1` (Aktør) | `1 — Forståelighet` |
| `—` (Distribusjon, container) | uendra |

Livssyklus- og instansradene har alt `N — Namn`-format — uendra.

### 3. Legg namn til Digdir-regel i gold-tabellen og fyll ut manglande rader

Erstatt heile gold-tabellen (linje 143-152) med ei fullstendig tabell som
følgjer bronze sitt radrekkefølgje (17 rader arva/oppgraderte frå bronse) +
gold sine 3 eigne tilleggssjekkar (20 rader totalt). Rader merkte **(ny)**
finst ikkje i dagens gold-tabell:

```markdown
| Sjekk | Alvor | Digdir-regel | FAIR | Skildring |
|---|---|---|---|---|
| `schema.id` til stades | error | 4 — Identifiserbarheit | F1 | Persistent identifikator for skjemaet — arva frå bronse (allereie error) |
| `schema.id` er HTTP(S)-URI | error | 4 — Identifiserbarheit | F1 | Sikrar at identifikatoren er ein oppløyseleg URI — arva frå bronse (allereie error) |
| `schema.name` til stades | error | 1 — Forståelighet | — | Maskinlesbart namn for skjemaet — arva frå bronse (allereie error) |
| `schema.title` til stades | error | 1 — Forståelighet, 2 — Meiningsfullheit | F2 | Tittel er del av rike metadata som gjer ressursen søkbar — arva frå bronse (allereie error) |
| `schema.default_prefix` til stades | error | 4 — Identifiserbarheit | — | Standardnamnerom for lokale identifikatorar — arva frå bronse (allereie error) |
| `schema.default_prefix` er absolutt HTTPS-URI med avsluttande `/` | error | 4 — Identifiserbarheit | — | Sikrar korrekt URI-konstruksjon — arva frå bronse (allereie error) |
| `schema.description` til stades | error | 1 — Forståelighet | F2 | Fritekstskildring av skjemaet sitt føremål — arva frå bronse, oppgradert til error |
| `schema.version` til stades | error | 9 — Datering | F4 | Versjonering støttar katalogregistrering og sporbarheit — arva frå bronse, oppgradert til error |
| `schema.license` til stades | error | 7 — Tilgjengeleggjering | R1.1 | Lisens for gjenbruk av skjemaet — arva frå bronse, oppgradert til error |
| Skjema har ikkje fleire enn 50 klasser (unntatt `tree_root`) | error | 6 — Modularitet | — | Handterleg mengde modellelement per modul — arva frå bronse, oppgradert til error |
| Alle klassenamn startar med stor bokstav (PascalCase) | error | 3 — Navne- og skrivekonvensjoner | — | Konsistent namngjevingskonvensjon for klasser — arva frå bronse, oppgradert til error |
| Alle slotnamn er snake_case | error | 3 — Navne- og skrivekonvensjoner | — | Konsistent namngjevingskonvensjon for eigenskapar — arva frå bronse, oppgradert til error |
| Alle klasser (unntatt `tree_root`) har `class_uri` | error | 4 — Identifiserbarheit, 8 — Maskinprosserbarheit | F3, I1 | Mappar klassen til RDF-vokabular — arva frå bronse, oppgradert til error |
| Alle globale slots har `slot_uri` | error | 4 — Identifiserbarheit, 8 — Maskinprosserbarheit | I1 | Mappar eigenskapen til RDF-vokabular — arva frå bronse, oppgradert til error |
| Alle klasser (unntatt `tree_root`) har identifikator-slot | error | 4 — Identifiserbarheit | F1 | Sikrar at instansar av klassen kan identifiserast unikt — arva frå bronse, oppgradert til error |
| Alle klasser (unntatt `tree_root`) har `annotations.begrepsidentifikator` | error | 13 — Begreper | A2 | Koplar modellelement til fagomgrep i begrepskatalog — arva frå bronse, oppgradert til error |
| Slots med kontrollerte vokabular har korrekte annotations | error | 8 — Maskinprosserbarheit | I1 | Sikrar maskinlesbar dokumentasjon av vokabularkrav — arva frå bronse, oppgradert til error |
| Skjemaet deklarerer minst eitt standard vokabularprefiks (`dct`, `dcat`, `skos`, `prov`, `rdf`, `rdfs`, `owl`, `foaf`, `xsd`) | error | 8 — Maskinprosserbarheit | I2 | Standardvokabular sikrar interoperabilitet på tvers av system |
| Skjemaet har ein slot med `dct:license` | error | 7 — Tilgjengeleggjering | R1.1 | Lisensinformasjon er føresetnad for gjenbruk — arva frå bronse, oppgradert til error |
| Skjemaet har ein slot for proveniens (`prov:wasAttributedTo`, `prov:wasGeneratedBy`, `dct:creator`, `dct:publisher` eller `dct:contributor`) | error | 10 — Ansvar | R1.2 | Proveniens er viktig for tillit til og gjenbruk av data |
```

Merk: dei tre siste radene (standard vokabularprefiks, `dct:license`-slot,
proveniens-slot) er identiske med dagens gold-tabell, berre med `N — Namn`
på Digdir-regel-kolonnen.

### 4. Visuell kontroll

Les gjennom dei tre oppdaterte tabellane og stadfest at:
- Bronze har 17 rader, alle med utfylt Skildring-kolonne
- Silver sine klasse-slot-rader har `N — Namn`-format på Digdir-regel
- Gold har 20 rader (17 arva/oppgraderte frå bronse + 3 gold-eigne), alle
  med `N — Namn`-format
- Ingen av dei tre tabellane har rader med feil «oppgradert»-påstand for
  sjekkar som alt var `error` i bronse
- `make lint`/eksisterande CI-sjekkar for README.md (om nokon) framleis passerer

## Handlingsliste

- [x] Legg til Skildring-kolonne i bronze-tabellen (steg 1)
- [x] Legg namn til Digdir-regel i silver sine klasse-slot-rader (steg 2)
- [x] Legg namn til Digdir-regel og fyll ut manglande rader i gold-tabellen (steg 3)
- [x] Visuell kontroll av alle tre tabellar (steg 4)

## Utført

Alle fire steg gjennomførte utan avvik frå planen:

1. Bronze-tabellen fekk Skildring-kolonne — 17 rader, alle utfylte.
2. Silver sine 17 klasse-slot-rader fekk `N — Namn`-format på Digdir-regel
   (t.d. `1, 2, 10` → `1 — Forståelighet, 2 — Meiningsfullheit, 10 — Ansvar`).
3. Gold-tabellen utvida frå 8 til 20 rader — alle 17 bronse-sjekkane er no
   representerte (12 nye rader), med korrekt skilje mellom «allereie error i
   bronse» og «oppgradert frå warning til error». Alle rader brukar
   `N — Namn`-format.
4. Visuell kontroll stadfesta radtal, kolonneformat og at ingen rader har
   feilaktige «oppgradert»-påstandar.

## Utkast til commit-melding

```
docs(mcp-linkml-validator): gjer bronze/silver/gold-tabellane konsistente i policies/README.md
  - src/mcp-linkml-validator/policies/README.md:
    - bronze: legg til Skildring-kolonne (17 rader)
    - silver: namngjev Digdir-regel i klasse-slot-radene
    - gold: utvid frå 8 til 20 rader (alle bronse-sjekkar representerte),
      namngjev Digdir-regel, fjern feilaktig «oppgradert»-påstand for
      schema.id-sjekken
  - specs/backlog/bronze-silver-gold-tabell-konsistens.md: flytta til specs/done/
```
