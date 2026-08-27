# Verifiser Vurdering-kolonnen i Pilar 1/2/3-tabellane i standardetterleving.md

## Bakgrunn

Brukaren ønskjer at alle radene i "Pilar 1 — Veiledere", "Pilar 2 — Standarder
og spesifikasjoner" og "Pilar 3 — Informasjonsmodellar" i
`mkdocs/docs/arkitektur/standardetterleving.md` vert gjennomgått, slik at
"Vurdering"-kolonnen konsekvent gir god informasjon om **både** kva som er i
henhold til rammeverket **og** kva som eventuelt er gap — ikkje berre eit
uspesifisert "Utført."/"I hovudsak utført."

**Avgrensing:** "Kjerneprinsipp"-tabellen (linje 59-67) er ikkje del av dei tre
pilar-tabellane og er difor ikkje i scope for denne gjennomgangen, med mindre
gjennomgangen avdekkjer noko som direkte påverkar henvisningar til han.

## Framgangsmåte

1. For kvar rad: identifiser kjeldespec (`specs/done/avvik-*.md` eller
   tilsvarande) som ligg til grunn for statusvurderinga.
2. Verifiser kjeldespecen sin sluttstatus mot faktisk repo-tilstand i dag
   (skjemafiler, manifest, validator-policy) — kjeldespecane kan vere fleire
   månadar gamle og kan ha vorte utdaterte (jf. `avvik-prinsipper-informasjonsmodeller.md`
   som synte fire lukka gap sidan juni).
3. Vurder om noverande "Vurdering"-tekst i `standardetterleving.md` er
   informativ nok: seier ho konkret kva som ER i henhold (ikkje berre "utført"),
   og listar ho eventuelle attverande gap eksplisitt (ikkje berre "i hovudsak")?
4. Der teksten er for vag eller kjeldespecen har endra seg: skriv om cella med
   konkrete punkt, i same stil som already gjort for "Ni designprinsipper"-rada
   (sjå `specs/done/detaljer-ni-designprinsipper-gap.md`).
5. Oppdater "Attverande gap"-tabellen (linje 70-79) dersom nye konkrete gap vert
   avdekt som ikkje alt er lista der.

## Rader i scope

**Pilar 1 — Veiledere (7 rader):** Orden i eget hus, Modenhetsmodell,
Tilgjengeliggjøring av åpne data, Beskrivelse av kvalitet på datasett,
Internkontroll i praksis, Veileder for informasjonsmodellar (ModellDCAT-AP-NO),
Veileder for høsting og deling av språkdata.

**Pilar 2 — Standarder og spesifikasjoner (12 rader):** DCAT-AP-NO, SKOS-AP-NO
Begrep, Termlosen, Forvaltningsstandard for begrepsharmonisering, TBX-AP-NO,
Retningslinjer ved tilgjengeliggjøring, DQV-AP-NO, ModelDCAT-AP-NO, Los,
Standarder for URI-peikarar, XKOS-AP-NO, CPSV-AP-NO.

**Pilar 3 — Informasjonsmodellar (4 rader):** Ni designprinsipper (allereie
verifisert og oppdatert, sjå `specs/done/detaljer-ni-designprinsipper-gap.md`),
Felles modelleringsregler, Person og Enhet, Adresse.

## Utført

Alle 23 rader i Pilar 1/2/3-tabellane vart verifisert mot kjeldespec **og**
faktisk repo-tilstand (fire parallelle gjennomgangar). Funn og rettingar:

**Rader utan endring (kjeldespec framleis dekkjande, teksten alt informativ):**
Orden i eget hus, Modenhetsmodell, Internkontroll, Veileder for språkdata,
Forvaltningsstandard begrepsharmonisering, TBX-AP-NO, ModelDCAT-AP-NO,
Los, Person og Enhet.

**Tillegg (etter brukarønske om meir detalj):** Termlosen-rada vart i etterkant
utvida frå "I hovudsak utført." til konkret å namngje TL1-TL3 (relasjontype →
Konsept, `kjelde_tekst`, dei tre samsvarsprediketa) og det utsette TL4-punktet
(SHACL-regex for definisjonskvalitet, kryssreferert til SK5 Forslag B i
avvik-skos-ap-no.md). Verifisert direkte mot `skos-ap-no-schema.yaml` (line 179-533).

**Rader oppdatert — meir presis "kva er i henhold / kva er gap"-tekst:**
Tilgjengeliggjøring av åpne data, Veileder for informasjonsmodellar (ModellDCAT-AP-NO),
DCAT-AP-NO, SKOS-AP-NO Begrep, Retningslinjer tilgjengeliggjøring, DQV-AP-NO,
XKOS-AP-NO, CPSV-AP-NO, Felles modelleringsregler, Adresse.

**Faktafeil retta:** "Standarder for URI-peikarar" sa "2 av 5 tiltak attståande" —
kjeldespecen viser faktisk 6 punkt der 4 er opne. Retta til å namngje alle fire.

**Ny funksjonsfeil avdekt (ikkje berre eit dokumentasjonsgap):** "Beskrivelse av
kvalitet på datasett" gjekk frå ✅ til 🟡. `gen-dqv-measurements.py` ser etter
nøkkelen `data_policy` i `build.yaml`, medan alle datamanifest i dag brukar
`validation_policy` — scriptet er difor eit stille no-op, og
`brreg-begrepskatalog.yaml` har mista alle kvalitetsmålingar. Lagt til som gap 7
(høg prioritet) i "Attverande gap"-tabellen; sjølve bugfixen er ikkje utført
som del av denne specen (utanfor scope — dette var ein dokumentasjonsgjennomgang).

**Attverande gap-tabellen:** gap 1 (URI-peikarar) og gap 3 (Adresse `class_uri`)
omskrivne for å reflektere faktisk noverande tilstand (class_uri er no lagt til,
men peikar til lokalt `ngr:`-prefiks i staden for standard geometrivokabular).
Gap 5 (begrepsidentifikator) fekk oppdatert kjeldereferanse (også Felles
modelleringsregler regel 13, ikkje berre Ni designprinsipper). Ny gap 7 lagt til.

**Ikkje utført (utanfor scope):** sjølve bugfixen for `gen-dqv-measurements.py`
er ikkje applikert — brukaren bad om ein dokumentasjonsgjennomgang, ikkje ein
kodeendring. Anbefaling: opprett eigen spec (t.d. `fiks-dqv-measurements-data-policy-nokkel.md`)
for retting av nøkkelnamn-mismatchen.
