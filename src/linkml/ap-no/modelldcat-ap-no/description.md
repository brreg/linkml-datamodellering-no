ModelDCAT-AP-NO er den norske applikasjonsprofilen for beskriving av informasjonsmodellar i DCAT-format, modellert i LinkML.

Profilen definerer korleis informasjonsmodellar og modellelement skal beskrivas med metadata — etter krava i [ModelDCAT-AP-NO-spesifikasjonen](https://data.norge.no/specification/modelldcat-ap-no) frå Digitaliseringsdirektoratet.

**Typisk brukar:** Offentlege verksemder som skal publisere informasjonsmodellar til [Felles modellkatalog](https://data.norge.no/informationmodels), og utviklare som implementerer ModelDCAT-AP-NO-kompatible system.

**Nøkkelklasser:** `Informasjonsmodell`, `Katalog`, `Objekttype`, `Datatype`, `Kodeliste`, `Egenskap` og subklassar av `Modellelement`.

**Skjemastruktur:** Profilen er delt i tre filer for å unngå sirkular import:
- `modelldcat-ap-no-schema.yaml` — hovudskjema, importerer dei to andre
- `modelldcat-katalog-schema.yaml` — `Informasjonsmodell` og `Katalog`-klassane
- `modelldcat-modell-schema.yaml` — alle modellelement-klassane (`Objekttype`, `Egenskap` o.fl.)

**Avvik frå spesifikasjonen:** Sjå `specs/done/avvik-modelldcat-ap-no.md` for dokumenterte avvik og grunngjevingar.
