LinkML-modell av Nasjonale grunndata - Virksomhet, modellert som ein domenemodell for verksemdsdata frå Enhetsregisteret.

Modellen definerer `Virksomhet` med `Underenhet` og `Hovudeining`, roller, adresser og klassifikasjonar (`Naeringskode`, `Organisasjonsform`).

**Typisk brukar:** Offentlege verksemder som arbeider med verksemdsdata frå Brønnøysundregistrene sitt Enhetsregister, og utviklare som implementerer virksomhet-API-ar baserte på Nasjonale grunndata.

**Nøkkelklasser:** `Virksomhet`, `Underenhet`, `Hovudeining`, `Naeringskode`, `Organisasjonsform`, `Adresse`.

**Relasjon til andre modellar i dette repoet:**
- Importerer `linkml:types` direkte — ingen AP-NO-profiler
- `oreg/enhetsregisteret-bvrinn` er ein relatert, meir detaljert modell av same domene
