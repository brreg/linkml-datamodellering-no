LinkML-modell av Enhetsregisteret (BVRINN — Brønnøysundregistrene Virksomheter og Næringsdata), proof-of-concept for registerdatamodellering.

Modellen definerer `Enhet`, `Underenhet`, `Hovudeining`, `Organisasjonsform`, `Naeringskode` og andre eigenskapar for norske verksemder registrerte i Enhetsregisteret.

**Typisk brukar:** Utviklare som arbeider med Enhetsregister-data frå Brønnøysundregistrene, og som ønskjer å eksperimentere med LinkML-basert registermodellering.

**Nøkkelklasser:** `Enhet`, `Underenhet`, `Hovudeining`, `Organisasjonsform`, `Naeringskode`, `Adresse`.

**Relasjon til andre modellar i dette repoet:**
- Importerer `linkml:types` direkte — ingen AP-NO-profiler
- `ngr-virksomhet` er ein relatert, meir generisk modell basert på Nasjonale grunndata