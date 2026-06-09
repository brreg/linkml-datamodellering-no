# Fix: fint-eksempeldata brukar inline-objekt i relasjonsslots

## Bakgrunn

`test_roundtrip_json` hoppar over `fint-administrasjon`, `fint-okonomi`,
`fint-personvern` og `fint-utdanning` fordi `linkml-convert` feiler med:

```
ValueError: [{'id': 'finta:...', ...}] is not a valid URI or CURIE
```

## Rot-årsak

Eksempeldatafilene har full inline-objekt i relasjonsslots mellom domaineklassar,
t.d.:

```yaml
# fint-administrasjon-eksempel.yaml — Personalressurs
personalressursar:
  - id: finta:personalressurs/p12345
    ...
    arbeidsforhold:               # ← dette er ein relasjon til Arbeidsforhold
      - id: finta:arbeidsforhold/af-p12345-1
        stillingsnummer: "1001"   # ← men innhaldet er eit fullt objekt
        ...
```

`arbeidsforhold`-sloten har `range: Arbeidsforhold`, og `Arbeidsforhold`
har `id: identifier: true`. Utan `inlined: true` på sloten forventar
`linkml-convert` URI-referansar, ikkje fulle objekt. Resultatet er at
`linkml-convert` prøver å tolke heile dict-listen som ein URI og feiler.

**fint-ressurs** løyser dette riktig: relasjonsslots brukar berre URI:

```yaml
# fint-ressurs-eksempel.yaml — Applikasjonsressurs
applikasjonsressursar:
  - id: finta:applikasjonsressurs/hr-portal-ansatt
    applikasjon: finta:applikasjon/hr-portal   # ← berre URI
    brukertype:
      - finta:brukertype/ansatt                # ← berre URI-liste
```

Dei fulle objekta (`Applikasjon`, `Brukertype`) ligg som eigne oppføringar
i container-listene, og relasjonane brukar URI-referansar.

## Løysing

Omstrukturér eksempeldatafilene for dei fire skjemaa slik at:

1. Fulle domaineobjekt ligg berre i container-attributtane (toppnivå i fila).
2. Relasjonsslots inne i eit domaineobjekt brukar URI-referansar (string eller
   liste av strings), ikkje inline-objekt.

Mønsteret frå `fint-ressurs` er referansen.

## Prioritert tiltaksliste

| # | Tiltak | Prioritet |
|---|---|---|
| 1 | `fint-administrasjon-eksempel.yaml`: flytt inline-`Arbeidsforhold`-objekt frå `Personalressurs.arbeidsforhold` til container-nivå; bytt ut med URI-referansar | Høg |
| 2 | `fint-administrasjon-eksempel.yaml`: gjer same for andre relasjonsslots (t.d. `Arbeidsforhold.personalressurs`, `Personalressurs.leder`, `Fullmakt.personalressurs`) | Høg |
| 3 | `fint-okonomi-eksempel.yaml`: same omstrukturering for relasjonsslots mellom `Faktura`, `Fakturagrunnlag`, `Fakturautsteder`, `Leverandor` | Høg |
| 4 | `fint-personvern-eksempel.yaml`: same for `Behandling.behandlingsgrunnlag`, `Behandling.tjeneste`, `Samtykke.person` | Høg |
| 5 | `fint-utdanning-eksempel.yaml`: same for relasjonane mellom `Elev`, `Skole`, `Undervisningsforhold`, `Personalressurs` | Høg |
| 6 | Køyr `make test` for alle fire skjema og verifiser `roundtrip-json` passerer | Høg |
| 7 | Fjern dei fire skjemaa frå skip-lista i `test_roundtrip_json` i `tests/test_make.sh` | Høg |

## Implementasjonsdetalj

Etter omstrukturering bør eksempelfila sjå slik ut (skjematisk):

```yaml
# Container-nivå: fulle objekt
personalressursar:
  - id: finta:personalressurs/p12345
    ansattnummer:
      identifikatorverdi: "P12345"
    arbeidsforhold:
      - finta:arbeidsforhold/af-p12345-1    # ← berre URI

arbeidsforhold:
  - id: finta:arbeidsforhold/af-p12345-1
    stillingsnummer: "1001"
    stillingstittel: "Rådgiver IKT"
    personalressurs: finta:personalressurs/p12345  # ← tilbake-referanse som URI
    ...
```

Sjekk `fint-ressurs-eksempel.yaml` for fleire eksempel på riktig mønster.

## Utført

Alle tiltak gjennomførte. `make test` passerer 17/17 for alle fire skjema inkludert `roundtrip-json` og `roundtrip-ttl`.

### Faktisk rot-årsak (avvik frå spec)

Spec-en antok at feilen låg i eksempeldatafilene (inline-objekt i relasjonsslots). Etter nærmare analyse var det faktisk **schemafiler** som hadde feilen: container-klassane brukte `slot_usage:` for å setje `multivalued: true` og `inlined_as_list: true`, men `slot_usage:` overstyrer ikkje `attributes:` — berre globale slots. Resultatet var at Python-klassane som vart genererte frå skjemaet hadde container-attributtane som enkle URI-referansar, ikkje som multivalued inline-lister.

Eksempeldatafilene var allereie korrekte.

### Endringar per skjema

- **`fint-administrasjon-schema.yaml`**: flytta `multivalued: true` og `inlined_as_list: true` frå `slot_usage:` til `attributes:` direkte for 15 attributtar (`arbeidsforhold`, `fastlonn`, `fasttillegg`, `fravaer`, `organisasjonselement`, `variabellonn`, `anlegg`, `ansvar`, `diverse`, `formaal`, `lopenummer`, `objekt`, `prosjekt`, `kjonn`, `fylke`). Lagt til `range: Kjonn` og `range: Fylke` på dei to som mangla range. Fjerna heile `slot_usage:`-seksjonen frå containeren.
- **`fint-okonomi-schema.yaml`**: same fix for `fakturagrunnlag`. Fjerna `slot_usage:`-seksjonen.
- **`fint-personvern-schema.yaml`**: same fix for `behandlingsgrunnlag`. Fjerna `slot_usage:`-seksjonen.
- **`fint-utdanning-schema.yaml`**: same fix for 31 attributtar. Fjerna heile `slot_usage:`-seksjonen frå containeren.
- **`tests/test_make.sh`**: fjerna dei fire skjemaa frå skip-listene i `test_roundtrip_json` og `test_roundtrip_ttl`.
