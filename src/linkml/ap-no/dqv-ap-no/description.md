DQV-AP-NO er den norske applikasjonsprofilen av [DQV](https://www.w3.org/TR/vocab-dqv/) (Data Quality Vocabulary), tilpassa norsk offentleg sektor og modellert i LinkML.

Profilen dekkjer metadata for datakvalitet, inkludert kvalitetsmerknadar, kvalitetsmålingar, kvalitetsdimensjonar og kvalitetsmål — tilpassa krava i [DQV-AP-NO-spesifikasjonen](https://informasjonsforvaltning.github.io/dqv-ap-no/) frå Digitaliseringsdirektoratet.

**Typisk brukar:** Offentlege verksemder som skal annotere datasett med datakvalitetsinformasjon i [Felles datakatalog](https://data.norge.no), og utviklarar som implementerer DQV-AP-NO-kompatible system.


**Skjemastruktur:** Profilen er delt i to sjølvstendige modellar for å unngå sirkulær import:
- `dqv-ap-no` (dette skjemaet) — narrowar `har_maal.range` til `KatalogisertRessurs`
- [`dqv-core`](../dqv-core/index.md) — kjerneklasser utan DCAT-avhengigheit, importert av både `dqv-ap-no` og `dcat-ap-no`

**Avvik frå spesifikasjonen:** Sjå `specs/done/avvik-dqv-ap-no.md` for dokumenterte avvik og grunngjevingar.
