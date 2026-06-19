SKOS-AP-NO er den norske applikasjonsprofilen av [SKOS](https://www.w3.org/TR/skos-reference/) for omgrep (begrep), modellert i LinkML.

Profilen definerer korleis omgrep, omgrepssystem og definisjonar skal beskrivas med metadata — etter krava i [SKOS-AP-NO-Begrep-spesifikasjonen](https://informasjonsforvaltning.github.io/skos-ap-no-begrep/) frå Digitaliseringsdirektoratet.

**Typisk brukar:** Offentlege verksemder som skal publisere omgrepskatalogar til [Felles begrepskatalog](https://data.norge.no/concepts), og utviklare som implementerer SKOS-AP-NO-kompatible system.

**Nøkkelklasser:** `Begrep`, `Definisjon`, `BegrepSamling`, `AssosiativRelasjon`, `GenericRelasjon`, `PartitivRelasjon`.

**Relasjon til andre modellar i dette repoet:**
- `common-ap-no` er basislaget — felles typar og prefiks vert importerte derifrå
- `brreg-begrepskatalog` er eit konkret døme på ein omgrepskatalog som importerer dette skjemaet direkte utan eigne klasser
- `xkos-ap-no` er eit tilgrensande skjema for klassifikasjonar (ikkje omgrep)

**Avvik frå spesifikasjonen:** Sjå `specs/backlog/avvik-skos-ap-no.md` for dokumenterte avvik og grunngjevingar.
