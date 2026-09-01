# Splitt brreg-felles-adresse i geografisk og digital adresse

## Bakgrunn

`src/linkml/felles/brreg-felles-adresse/brreg-felles-adresse-schema.yaml`
inneheld i dag to uavhengige klassehierarki i eitt skjema:

- **Geografisk adressehierarki:** `GeografiskAdresse` (abstrakt,
  `class_uri: locn:Address`) med subklassane `Postboksadresse`,
  `Stedsadresse`, `Vegadresse`, `Matrikkeladresse`, `InternasjonalAdresse`,
  pluss støtteklassane `Poststed`, `Kommune`, `Fylke`, `Matrikkelnummer`
  og `Adressenummer` (frå Strukturtypekatalog_v1) som berre desse bruker.
- **Digitalt adressehierarki:** `DigitalAdresse` (abstrakt) med
  subklassane `IPAdresse`, `EPostadresse`, `Nettadresse`, `Meldingsboks`,
  `Mobiltelefonnummer`, `Telefonnummer`.

Dei to hierarkia deler berre to trivielle slots (`id`, `type`) og har
elles ingen kryssreferansar mellom seg. `brreg-felles-aktoer` importerer
i dag heile `brreg-felles-adresse-schema` for å bruke **begge**
hierarkia (`range: GeografiskAdresse` og `range: DigitalAdresse` på
høvesvis `adresse`/`digital_adresse`-slots, sjå linje 176/181 i
`brreg-felles-aktoer-schema.yaml`).

**Ønska sluttilstand** (avklart med brukar):

- Splitt i to sjølvstendige skjema: **`brreg-felles-geografisk-adresse`**
  og **`brreg-felles-digital-adresse`**.
- Dei fem strukturtypeklassane (Poststed, Kommune, Fylke,
  Matrikkelnummer, Adressenummer) følgjer med til
  `brreg-felles-geografisk-adresse`, sidan dei i dag berre er brukt av
  `GeografiskAdresse`-hierarkiet.
- Den gamle `brreg-felles-adresse`-katalogen **fjernast heilt** — reint
  brot, ingen deprecated overgangsperiode (modellen er PoC/v0.1.0 og
  berre brukt internt i repoet).
- `brreg-felles-aktoer` oppdaterast til å importere **begge** dei nye
  skjemaa i staden for det eine gamle.

## Steg

1. **Opprett `src/linkml/felles/brreg-felles-geografisk-adresse/`** via
   `make new-modell DOMAIN=felles NAME=brreg-felles-geografisk-adresse`,
   deretter fyll `brreg-felles-geografisk-adresse-schema.yaml` med:
   - `id`/`default_prefix`: `https://data.norge.no/felles/brreg-felles-geografisk-adresse`
   - `prefixes.brreg_felles_geografisk_adresse`: same URI + `/`
   - `imports`: `linkml:types`, `../brreg-felles-typer/brreg-felles-typer-schema` (uendra — typane som er i bruk, t.d. `Postboksnummer`, `Bruksenhetsnummer`, `Landkode`, `PrefiksMedNasjonalKode`, `NasjonaltNummer`, `Postnummer`, `Kommunenummer`, `Fylkesnummer`, `Husnummer`, `Husbokstav`, ligg alle i `brreg-felles-typer`)
   - Klasser: `GeografiskAdresse`, `Postboksadresse`, `Stedsadresse`,
     `Vegadresse`, `Matrikkeladresse`, `InternasjonalAdresse`,
     `Poststed`, `Kommune`, `Fylke`, `Matrikkelnummer`, `Adressenummer`
     — kopiert uendra frå det gamle skjemaet (klasse- og slotdefinisjonar
     er allereie isolerte til denne gruppa, ingen refaktorering av
     feltnamn/typar).
   - Slots: alle slots brukt av klassene over (`id`, `br_adresse_id`,
     `co_navn`, `type`, `postboksnummer`, `anleggsnavn`, `poststed`,
     `kommune`, `stedsnavn`, `vegadresse_id`, `bruksenhetsnummer`,
     `adressenavn`, `kort_adressenavn`, `adressenummer`,
     `adressetilleggsnavn`, `fylke`, `matrikkeladresse_id`,
     `matrikkelnummer`, `undernummer`, `adressenummer_tekst`, `bygning`,
     `etasjenummer`, `boenhet`, `postboks`, `postkode`,
     `by_eller_stedsnavn`, `region`, `distrikt_eller_bydel`, `landkode`,
     `fri_adressetekst`, `adresseidentifikator`, `navn`, `postnummer`,
     `kommunenummer`, `kommunenavn`, `fylkesnummer`, `fylkesnavn`,
     `gaardsnummer`, `bruksnummer`, `festenummer`, `seksjonsnummer`,
     `nummer`, `bokstav`) — `slot_uri`-prefiks endra frå
     `brreg_felles_adresse:` til `brreg_felles_geografisk_adresse:`.
   - `class_uri` for `GeografiskAdresse` er uendra (`locn:Address`);
     alle andre `class_uri` endrar prefiks til
     `brreg_felles_geografisk_adresse:`.
   - Skildringskommentaren (`description:`) og fil-header-kommentaren
     oppdaterast til å berre nemne det geografiske hierarkiet + dei fem
     strukturtypeklassane (fjern all omtale av `DigitalAdresse` og
     "Aksesspunkt"-unntaket, som ikkje gjeld denne modellen lenger).
   - `title`: `BRREG felles geografisk adresse`.

2. **Opprett `src/linkml/felles/brreg-felles-digital-adresse/`** via
   `make new-modell DOMAIN=felles NAME=brreg-felles-digital-adresse`,
   deretter fyll skjemaet med:
   - `id`/`default_prefix`: `https://data.norge.no/felles/brreg-felles-digital-adresse`
   - `prefixes.brreg_felles_digital_adresse`: same URI + `/`
   - `imports`: `linkml:types`, `../brreg-felles-typer/brreg-felles-typer-schema`
     (for typane brukt i telefonnummer-slots)
   - Klasser: `DigitalAdresse`, `IPAdresse`, `EPostadresse`,
     `Nettadresse`, `Meldingsboks`, `Mobiltelefonnummer`,
     `Telefonnummer` — kopiert uendra.
   - Slots: `id`, `identifikator`, `type`, `ip_nummer`, `domenenavn`,
     `brukernavn`, `protokoll`, `filsti`, `meldingsbokstype`,
     `prefiks_med_nasjonal_kode`, `nasjonalt_nummer` — `slot_uri`-prefiks
     endra til `brreg_felles_digital_adresse:`. `id` og `type` vert
     **duplisert** frå geografisk-adresse-skjemaet (identisk, trivielt
     innhald) — same mønster som at kvart FELLES-skjema alt definerer
     sin eigen lokale `id`-slot (jf. `brreg-felles-tid`,
     `brreg-felles-typer`), ikkje delt via import.
   - Behald kommentaren om at BR sin `Nettadresse`-undertype
     "Aksesspunkt" er medvite utelaten (sirkularitet mot
     `brreg-felles-aktoer` sin `Virksomhet`) — denne gjeld framleis for
     `Nettadresse` i dette skjemaet.
   - `title`: `BRREG felles digital adresse`.

3. **Oppdater `src/linkml/felles/brreg-felles-aktoer/brreg-felles-aktoer-schema.yaml`:**
   - Byt ut importlinja
     `../brreg-felles-adresse/brreg-felles-adresse-schema` med **to**
     imports:
     `../brreg-felles-geografisk-adresse/brreg-felles-geografisk-adresse-schema`
     og
     `../brreg-felles-digital-adresse/brreg-felles-digital-adresse-schema`.
   - `range: GeografiskAdresse` (linje ~176) og `range: DigitalAdresse`
     (linje ~181) er uendra (klassenamna er identiske i dei nye
     skjemaa).
   - Oppdater `description:`-referansen "Importerer brreg-felles-adresse
     for GeografiskAdresse/DigitalAdresse" til å nemne dei to nye
     skjemaa.

4. **Fjern gamal katalog:**
   `rm -rf src/linkml/felles/brreg-felles-adresse/` (skjema, build.yaml,
   description.md, metadata/, validation/ — alt CI-generert innhald
   vert regenerert for dei nye modellane i steg 6).

5. **Oppdater statisk dokumentasjon som nemner `brreg-felles-adresse`
   ved namn:**
   - `src/linkml/felles/description.md`: byt éin rad
     (`brreg-felles-adresse`) med to
     (`brreg-felles-geografisk-adresse`, `brreg-felles-digital-adresse`)
     i modell-/importrekkjefølgje-lista.
   - `mkdocs/docs/arkitektur/importhierarki.md` § FELLES-hierarki:
     oppdater ASCII-treet og reglane til å reflektere den nye,
     bortgreina strukturen, t.d.:
     ```
     linkml:types
         └── brreg-felles-typer-schema
             ├── brreg-felles-tid-schema
             ├── brreg-felles-geografisk-adresse-schema
             │   └── brreg-felles-aktoer-schema
             └── brreg-felles-digital-adresse-schema
                 └── brreg-felles-aktoer-schema
     ```
     (`brreg-felles-aktoer-schema` har to foreldre — vurder om
     ASCII-tre-formatet i `parse-dependency-tree.py` handterer eit
     multi-parent-node korrekt, eller om treet må forenklast/kommenterast
     manuelt for lesbarheit — sjå Merknad under.)

6. **Regenerer og valider:**
   - `make lint SCHEMA=src/linkml/felles/brreg-felles-geografisk-adresse/brreg-felles-geografisk-adresse-schema.yaml`
   - `make lint SCHEMA=src/linkml/felles/brreg-felles-digital-adresse/brreg-felles-digital-adresse-schema.yaml`
   - `make lint SCHEMA=src/linkml/felles/brreg-felles-aktoer/brreg-felles-aktoer-schema.yaml`
   - `make roundtrip SCHEMA=...` for alle tre.
   - `make domain-felles` (regenererer alle FELLES-artefakt, inkl. dei
     to nye modellane sine `metadata/`- og `validation/`-filer).
   - `make docs-publish` (README-tabellar + mkdocs-portal, inkl.
     `mkdocs/docs/felles/index.md`-modell-liste).

7. **Kryssjekk avhengige OREG-modellar:** ingen `enhetsregisteret-*`
   importerer `brreg-felles-adresse` i dag (verifisert:
   `enhetsregisteret-bvrinnfelles` importerer berre
   `brreg-felles-typer`), så ingen OREG-endringar er nødvendige — berre
   dobbeltsjekk med
   `grep -rl brreg-felles-adresse src/linkml/oreg/` før avslutning for å
   fange opp evt. framtidige importar lagt til sidan denne specen vart
   skriven.

## Merknad — multi-parent i importhierarki-ASCII-treet

`brreg-felles-aktoer-schema` vil etter splitten importere to søsken-noder
(`brreg-felles-geografisk-adresse-schema` og
`brreg-felles-digital-adresse-schema`) i staden for éin enkelt
foreldrenode. `parse_tree_lines()`/`build_subtree()` i
`parse-dependency-tree.py` bygger treet frå eit `{parent: [children]}`-oppslag
og har ikkje eksplisitt handtert multi-parent-noder tidlegare i repoet
(alle eksisterande hierarki er reine tre, ikkje DAG). Verifiser under
steg 6 at avhengigheitstreet på `brreg-felles-aktoer`-sida (og på
`enhetsregisteret-bvrinnfelles`-sida, viss han seinare importerer
aktør-modellen) vert teikna fornuftig og ikkje dupliserer/utelet
noder — juster ASCII-treet i `importhierarki.md` eller
scriptet om nødvendig.

## Handlingsliste

- [x] Steg 1: Opprett `brreg-felles-geografisk-adresse`
- [x] Steg 2: Opprett `brreg-felles-digital-adresse`
- [x] Steg 3: Oppdater `brreg-felles-aktoer` sine imports
- [x] Steg 4: Fjern gamal `brreg-felles-adresse`-katalog
- [x] Steg 5: Oppdater `felles/description.md` og `importhierarki.md`
- [x] Steg 6: Regenerer og valider (lint, roundtrip, domain-felles, docs-publish)
- [x] Steg 7: Kryssjekk OREG-avhengigheiter

## Utført

Alle steg gjennomførte som spesifisert, med éin nødvendig justering
oppdaga under steg 6 (sjå «Avvik» under).

**Avvik frå opphavleg plan — namnekollisjon på `id`/`type`:**

Steg 2 sin plan om å duplisere `id`/`type` identisk (med same globale
slotnavn) i `brreg-felles-digital-adresse` viste seg å bryte
`make check-import-duplicates`/`make domain-felles` (`gen-rdf`, `gen-owl`,
`gen-shacl`, `gen-plantuml` m.fl.) med feilen
`Conflicting URIs (...digital-adresse, ...geografisk-adresse) for item: id`.
Årsak: LinkML sin `SchemaLoader`/`mergeutils.merge_dicts()` tillet ikkje at
to søsken-skjema uavhengig definerer eit globalt element med same **namn**
når eit tredje skjema (her: `brreg-felles-aktoer`) importerer begge —
uavhengig av om `slot_uri` er lik. Dette gjaldt både for `id`
(identifikator-sloten) og `type` (diskriminator-sloten).

**Løysing:** I `brreg-felles-digital-adresse-schema.yaml` er dei to
globale slota omdøypte til `digital_adresse_id` og `digital_adresse_type`
(unike namn i importgrafen), med `alias: id` / `alias: type` sett på kvar
— LinkML sin offisielle mekanisme for å presentere eit slot under eit anna
namn i klassane som brukar det. `digital_adresse_id` har i tillegg fått
eksplisitt `slot_uri: brreg_felles_digital_adresse:id` (parallelt med at
`digital_adresse_type` alt hadde `slot_uri: ...type`), slik at RDF/SHACL-
predikatet vert `...:id`/`...:type` — konsistent med korleis
`brreg-felles-geografisk-adresse` sine tilsvarande slot (utan eksplisitt
`slot_uri`, men same auto-avleiing) ser ut. Verifisert empirisk: generert
JSON Schema for `DigitalAdresse` har framleis property-namn `id`/`type`
(ikkje `digital_adresse_id`/`digital_adresse_type`), og SHACL-shapes brukar
`brreg_felles_digital_adresse:id`/`:type` som `sh:path` — identisk
ytre kontrakt som før splitten, berre den interne globale slot-identiteten
er endra.

`brreg-felles-geografisk-adresse` sine `id`/`type`-slot er **uendra** frå
planen (framleis rein `id`/`type`, ingen alias nødvendig — kollisjonen
oppstod berre for den sida som måtte omdøypast for å bli unik).

**Andre mindre justeringar utover opphavleg spec-tekst:**
- `examples/`-katalogane som `make new-modell` genererte automatisk for
  begge nye modellane er sletta — ingen andre FELLES-modellar
  (`brreg-felles-tid`, `-typer`, `-aktoer`, gamle `-adresse`) har
  `examples/`, sidan dei manglar `tree_root`-containerklasse og ikkje er
  meint å instansierast åleine.
- `build.yaml` for begge nye modellane er behalde slik `make new-modell`
  scaffolda dei (gjeldande mal med fleire generatorar aktiverte), i staden
  for å kopiere den eldre, meir avgrensa `build.yaml`-forma til det gamle
  `brreg-felles-adresse`.
- Ein attverande kommentarreferanse til det gamle namnet
  `brreg-felles-adresse` i `brreg-felles-aktoer-schema.yaml` (linje ~45,
  grunngjevingskommentar for `identifikator`-feltet) er retta til å peike
  til `brreg-felles-digital-adresse` i staden.
- Stale lokale byggoutput frå det gamle `brreg-felles-adresse`
  (`generated/felles/brreg-felles-adresse/` og
  `mkdocs/docs/felles/brreg-felles-adresse/`) er sletta manuelt, sidan
  `make docs-publish` elles ville republisert dei uendra (dei vert ikkje
  automatisk rydda av `domain-felles`/`docs-publish` når eit skjema fjernast
  frå `src/linkml/`, berre når heile domenet forsvinn).

**Validert:** `make lint` og `make roundtrip` for alle tre skjema, samt
`make domain-felles` (17 OK, 0 feil) og `make docs-publish` — alle grøne.
(Éin transient nettverksfeil, `<urlopen error [Errno -3] Try again>`, dukka
opp sporadisk på ulike, usamanhengande skjema mellom køyringar — stadfesta
som eit ustabilt DNS-oppslag i denne sandkasseomgjevnaden, ikkje ein reell
skjemafeil, sidan isolert `make gen-rdf` for kvart skjema alltid lukkast.)
