# Plan: List slotnamn per klasse i `analyse-similar-classes-*`-rapporten

## Bakgrunn

`make analyse-similar-classes-domain`/`analyse-similar-classes-all` viser
i dag berre klassenamn + kva skjema dei kjem frå — ikkje noko om **innhaldet**
i klassane. To klassar kan ha likt namn utan å ha likt innhald (falskt
positivt), eller ulikt namn men samanfallande slots (verdt å undersøke
likevel, men det er utanfor dette skriptet sitt namnebaserte føremål).
Brukaren vil ha slotnamna til kvar identifisert klasse med i rapporten,
slik at ein visuelt kan vurdere om eit namnetreff òg er eit reelt
strukturelt duplikat.

## Kartlegging

Klassar refererer slots på to måtar i dette repoet (jf. CLAUDE.md §
«Slots, ikke attributes»): vanlege domeneklassar via `classes.<X>.slots:`
(liste av slotnamn), containerklassar via `classes.<X>.attributes:`
(dict). Begge må hentast for fullstendig dekning.

Fordeling av slot-tal per klasse (målt over alle 484 klassar med minst
eitt slot): median 4, 90-persentil 11, maks 66 (venteleg ein
containerklasse). Dei fleste rader vert difor korte, men nokre få
(containerklassar) kan verte svært lange utan ei avgrensing.

## Plan

`find-similar-names.py`:
- Ny hjelpefunksjon `class_slot_names(defn) -> list[str]`: kombinerer
  `slots:`-lista og `attributes:`-nøklane, sortert, dupliserte fjerna.
- `load_entries()` for `--kind class`: returnerer no `(namn, slotnamn-liste)`
  i staden for `(namn, None)`.
- Klasse-rapporten sin tabell utvidast med to nye kolonnar, `Slots A` og
  `Slots B`, kommaseparerte og backtick-omslutta. For å halde tabellen
  lesbar: trunker til 12 slotnamn med eit `… (+N til)`-suffiks dersom
  lista er lengre.
- Ny tabellform for klasse-rapporten:
  `| Likskap | Namn A | Slots A | Skjema A | Namn B | Slots B | Skjema B |`
  (slot-rapporten er uendra frå [[modell-analyse-domain-datatype-help]]:
  `| Likskap | Namn A | Type A | Skjema A | Namn B | Type B | Skjema B |`)

**Utanfor omfang (ikkje bedt om, ikkje del av dette tiltaket):** ei
automatisk utrekna «felles slots»/overlapp-kolonne. Brukaren bad
spesifikt om å **liste** slotnamna, ikkje om ei berekna samanlikning —
med begge listene synlege kan brukaren sjølv vurdere overlappet visuelt.
Kan leggjast til seinare som eige, avgrensa tiltak dersom ønskt.

## Filer som vert påverka

- `src/assets/scripts/makefile/find-similar-names.py`

## Handlingsliste

1. [x] Legg til `class_slot_names()`-hjelpefunksjon
2. [x] Oppdater `load_entries()` for `--kind class` til å returnere
   slotnamn-liste i staden for `None`
3. [x] Utvid klasse-rapporten sin tabell med `Slots A`/`Slots B`-kolonnar,
   med 12-element trunkering
4. [x] Verifiser med ein reell køyring (`make analyse-similar-classes-all`)
   at slot-listene vert viste korrekt, inkl. eit tilfelle med
   trunkering (ei stor containerklasse) om det finst eitt i treffa

## Utført

`class_slot_names()` kombinerer `slots:`-lista og `attributes:`-nøklane,
sortert/deduplisert. `load_entries()` for `--kind class` returnerer no
`(namn, slotnamn-liste)`. Klasse-tabellen utvida med `Slots A`/`Slots B`,
kommaseparert, backtick-omslutta, trunkert til 12 element med
`… (+N til)`. Slot-rapporten (Type-kolonnar frå
[[modell-analyse-domain-datatype-help]]) er uendra.

**Verifisert med reelle køyringar** — funna stadfestar direkte nytteverdien:
- `Bruksenhetsnummer` (ngr-adresse/ngr-eiendom): identiske slot-lister —
  eit reelt strukturelt duplikat, ikkje berre namnesamantreff
- `Aktivitet` (fint-administrasjon vs. ngr-virksomhet/oreg): `(ingen)`
  slots i fint-administrasjon-varianten mot rike lister i dei andre —
  tydeleg IKKJE same innhald trass identisk namn
- `Begrep`/`Datasett` (skos-ap-no/dcat-ap-no): trunkering fungerer korrekt
  (`… (+27 til)`, `… (+31 til)`) for klassar med mange slots
- `make analyse-similar-classes-domain DOMAIN=ngr` og
  `make analyse-similar-slots-domain DOMAIN=oreg`: begge rapporttypar
  fungerer korrekt saman med det eksisterande `DOMAIN=`-filteret
