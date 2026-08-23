# oreg-skjema: retta generering-feil i CI (domain-oreg)

## Bakgrunn

CI-jobben `Generer alle artefakter for oreg` (`.github/workflows/generate.yml`,
`make domain-oreg`) feila etter commit `64387d86` («feat(oreg): scaffold seks
nye enhetsregisteret-domenemodellar frå JSON Schema»). Seks generatorsteg
(`python`, `jsonld-context`, `proto`, `graphql`, `plantuml`,
`convert-instance-rdf`) feila for fleire av dei nye skjema.

To distinkte feilklassar vart identifiserte ved reproduksjon lokalt
(`make gen-python|gen-jsonld-context|gen-proto|gen-graphql|gen-plantuml|convert-instance-rdf DOMAIN=oreg`):

### 1. Namnekollisjon mellom lokale slots/klassar og importerte AP-NO-slots/klassar

Fire nye skjema importerer `dcat-ap-no-schema` (som igjen importerer
`common-ap-no-schema`), men definerer lokale `slots:`/`classes:` med **same
namn** som eit allereie importert element, men med **anna URI**:

| Skjema | Lokalt namn | Kolliderer med | Import-kjelde |
|---|---|---|---|
| enhetsregisteret-bvrbekreftelse | slot `beskrivelse` | slot `beskrivelse` (`dct:description`) | common-ap-no |
| enhetsregisteret-bvrfriv | slot `versjon` | slot `versjon` (`dcat:version`) | dcat-ap-no |
| enhetsregisteret-bvrinnfelles | slot `beskrivelse` | slot `beskrivelse` (`dct:description`) | common-ap-no |
| enhetsregisteret-bvrinnfelles | slot `versjon` | slot `versjon` (`dcat:version`) | dcat-ap-no |
| enhetsregisteret-bvrinnfelles | klasse `Kontaktopplysning` | klasse `Kontaktopplysning` (`vcard:Kind`) | dcat-ap-no |

LinkML sitt import-hierarki mergar alle namn til éin namneromstabell —
to element med same namn men ulik URI gir feilen
`Conflicting URIs (<uri-a>, <uri-b>) for item: <namn>` i alle generatorar
som byggjer eit forent skjema (python, proto, graphql, jsonld-context,
plantuml, linkml-convert). Feilen stoppar heile generatorsteget for det
skjemaet, ikkje berre det kolliderande elementet.

Alle fem kollisjonane er **semantisk ulike** frå AP-NO-omgrepet dei
kolliderer med (t.d. `versjon` i FRIV-innrapportering er eit
meldingsversjonsnummer, ikkje ein ressursversjon som `dcat:version`) —
attgjenbruk av det importerte elementet var difor ikkje rett løysing.

Skjemaa har alt eit etablert mønster for akkurat dette: slottet
`kontaktinformasjon` er i alle ni oreg-skjema prefikset med modellnamnet
(`enhetsregisteret_bvrfriv_kontaktinformasjon` osv.) nettopp for å unngå
kollisjon med eit generisk importert namn. Fiksen følgjer same mønster.

### 2. Placeholder-verdien `dummy` i eksempeldata er ikkje gyldig for typa slotten har

Scaffold-eksempla (generert av mcp-linkml-modell-utkast) fyller obligatoriske
og andre felt med bokstaveleg `dummy` som placeholder (jf. kommentaren øvst i
kvar `*-eksempel.yaml`). Dette er greitt for felt med `range: string`, men
`linkml-convert`/RDF-serialisering feilar hardt når `dummy` står i felt med:

- **Enum-range** (`Unknown <Enum> enumeration code: dummy`)
- **Numerisk range** (`float`/`integer`-baserte typar — `could not convert
  string to float: 'dummy'`)
- **Dato/dato-tid-range** (`xsd:date`/`xsd:dateTime` — rdflib kastar
  `ValueError: Invalid isoformat string: 'dummy'` /
  `XSD Date string must contain at least two dashes`)
- **Klassereferanse-range** (ikkje-inlina slot som peikar på ein identifiserbar
  klasse — treng ein gyldig CURIE-referanse, ikkje ein fritekst-streng).
  Feilen frå `linkml-convert` sin CURIE-ekspandering er misvisande formulert:
  `Unknown CURIE prefix: @base`.

Alle refererte målklassar hadde alt nøyaktig éin eksempel-instans i sin
respektive container-bøtte, så feilen vart retta ved å peike `dummy`-referansane
til den eksisterande instansen sin `id`, ikkje ved å oppfinne nye instansar.

## Tiltak

1. **Fjern namnekollisjonar** — prefiks kvart lokalt kolliderande slot/klasse-namn
   med modellnamnet (same mønster som `<modell>_kontaktinformasjon`), i
   `slots:`-lista, `slot_usage:`, den globale slot-/klasse-definisjonen, og
   alle `range:`-referansar til klassen:
   - `enhetsregisteret-bvrbekreftelse-schema.yaml`: `beskrivelse` →
     `enhetsregisteret_bvrbekreftelse_beskrivelse`
   - `enhetsregisteret-bvrfriv-schema.yaml`: `versjon` →
     `enhetsregisteret_bvrfriv_versjon` (+ eksempeldata)
   - `enhetsregisteret-bvrinnfelles-schema.yaml`: `beskrivelse` →
     `enhetsregisteret_bvrinnfelles_beskrivelse`, `versjon` →
     `enhetsregisteret_bvrinnfelles_versjon`, klasse `Kontaktopplysning` →
     `EnhetsregisteretBvrinnfellesKontaktopplysning` (+ eksempeldata)
2. **Rett `dummy`-placeholder i eksempeldata** der verdien ikkje er gyldig for
   slotten sin `range`:
   - Enum-felt → første gyldige `permissible_values`-kode
     (`typeBekreftelse`, `maalformForTilbakemelding`)
   - Numeriske felt (`BeloepFriDesimal`→float, `AntallAksjer`→int) → `0`/`0.0`
   - Dato/dato-tid-felt (`Dato`, `DatoKlokkeslett`) → `2024-01-01` /
     `2024-01-01T00:00:00` (same konvensjon som kommentaren i fila alt nemner)
   - Klassereferanse-felt → CURIE til den eksisterande eksempel-instansen i
     riktig container-bøtte (t.d. `innsender: dummy` →
     `innsender: enhetsregisteret_bvrettersendingavvedlegg:eksempel-2`)
   - Berørte filer: `enhetsregisteret-bvrbekreftelse-eksempel.yaml`,
     `enhetsregisteret-bvrettersendingavvedlegg-eksempel.yaml`,
     `enhetsregisteret-bvrfriv-eksempel.yaml`,
     `enhetsregisteret-bvrinnfelles-eksempel.yaml`,
     `enhetsregisteret-bvrstiftelsesdokument-eksempel.yaml`,
     `enhetsregisteret-frivilligorganisasjonapi-eksempel.yaml`
3. **Verifiser** — køyr `make domain-oreg` og stadfest 0 feil (alle 16
   generatorsteg OK), samt ein systematisk Python-sjekk av at ingen
   `slots:`/`classes:` i oreg-skjema kolliderer med importerte
   common-ap-no/dcat-ap-no-namn, og at ingen `dummy`-verdiar står att i felt
   med enum-, numerisk-, dato- eller klassereferanse-range.

## Utført

Alle tre steg gjennomførte 2026-08-23. `make domain-oreg` køyrer no reint:
**16 OK, 0 feil** (var 6 feilande grupper av 12 før fiksen). Verifisert med
full lokal køyring av `gen-python`, `gen-jsonld-context`, `gen-proto`,
`gen-graphql`, `gen-plantuml`, `convert-instance-rdf` og heile
`domain-oreg`-pipelinen.

Genererte biprodukt frå lokal verifiseringskøyring (`metadata/*.yaml` for dei
seks skjemaa, samt versjons-/datooppdateringar i `enhetsregisteret-bvrinn`,
`javazonetalk` og `register-over-aksjeeiere` sine manifest — skjema eg ikkje
endra) vart reverterte/fjerna, sidan dei ikkje høyrer til denne fiksen og CI
regenererer dei korrekt ved neste køyring.

Ingen endring i `.github/workflows/*.yml` — `actionlint`-steget er difor ikkje
aktuelt for denne fiksen.
