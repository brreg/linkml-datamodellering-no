Modellkatalog for KS Digital sine informasjonsmodellar, basert på ModelDCAT-AP-NO.

Katalogen inneheld metadata om KS Digital sine LinkML-modellar, publiserte til [Felles modellkatalog](https://data.norge.no/informationmodels).

**Typisk brukar:** KS Digital sine modelladministratorar og eksterne brukarar som søkjer etter informasjonsmodellar frå KS.

**Nøkkelklasser:** `ModellkatalogContainer` (containerklasse) — alle andre klasser (`Informasjonsmodell`, `Objekttype`, `Egenskap` m.fl.) er importerte frå `modelldcat-ap-no`.

**Relasjon til andre modellar i dette repoet:**
- Importerer `modelldcat-ap-no` for alle ModelDCAT-AP-NO-klasser
- CI genererer `Informasjonsmodell`-instansar for alle KS Digital-skjema og legg dei til i denne katalogen
