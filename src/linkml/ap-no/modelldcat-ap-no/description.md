ModelDCAT-AP-NO er den norske applikasjonsprofilen for beskriving av informasjonsmodellar i DCAT-format, modellert i LinkML.

Profilen dekkjer metadata for informasjonsmodellar og modellelement — tilpassa krava i [ModelDCAT-AP-NO-spesifikasjonen](https://data.norge.no/specification/modelldcat-ap-no) frå Digitaliseringsdirektoratet.

**Typisk brukar:** Offentlege verksemder som skal publisere informasjonsmodellar til [Felles modellkatalog](https://data.norge.no/informationmodels), og utviklarar som implementerer ModelDCAT-AP-NO-kompatible system.


**Skjemastruktur:** Profilen er delt i tre sjølvstendige modellar som følgjer spesifikasjonen sin eigen struktur:
- `modelldcat-ap-no` (dette skjemaet) — hovudskjema, importerer dei to andre
- [`modelldcat-katalog`](../modelldcat-katalog/index.md) — `Informasjonsmodell` og `Katalog`-klassane
- [`modelldcat-modell`](../modelldcat-modell/index.md) — alle modellelement-klassane (`Objekttype`, `Egenskap` o.fl.)

**Avvik frå spesifikasjonen:** Sjå `specs/done/avvik-modelldcat-ap-no.md` for dokumenterte avvik og grunngjevingar.
