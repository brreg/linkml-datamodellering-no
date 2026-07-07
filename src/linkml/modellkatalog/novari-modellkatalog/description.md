Modellkatalog for Novari sine informasjonsmodellar, basert på ModelDCAT-AP-NO.

Katalogen inneheld metadata om Novari sine LinkML-modellar, publiserte til [Felles modellkatalog](https://data.norge.no/informationmodels).

**Typisk brukar:** Novari sine modelladministratorar og eksterne brukarar som søkjer etter informasjonsmodellar frå Novari.

**Nøkkelklasser:** `ModellkatalogContainer` (containerklasse) — alle andre klasser (`Informasjonsmodell`, `Objekttype`, `Egenskap` m.fl.) er importerte frå `modelldcat-ap-no`.

**Relasjon til andre modellar i dette repoet:**
- Importerer `modelldcat-ap-no` for alle ModelDCAT-AP-NO-klasser
- CI genererer `Informasjonsmodell`-instansar for alle Novari-skjema og legg dei til i denne katalogen
