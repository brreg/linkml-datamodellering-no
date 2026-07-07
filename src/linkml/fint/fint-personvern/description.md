LinkML-modell av FINT Personvern-API, konvertert frå FINT sin Java-baserte modell.

Modellen definerer `Behandling`, `Personopplysning`, `Rettslig grunnlag` og andre personvernrelaterte klasser for integrasjon med FINT Personvern-tenester (GDPR-støtte).

**Typisk brukar:** Kommunar og fylkeskommunar som brukar FINT Personvern-API for å dokumentere behandling av personopplysningar.

**Nøkkelklasser:** `Behandling`, `Personopplysning`, `RettsligGrunnlag`, `Behandlingsgrunnlag`, `Samtykke`.

**Relasjon til andre modellar i dette repoet:**
- Importerer `fint-common` for felles typar og basisklassar
- Ingen AP-NO-profiler importerte — FINT-modellane er uavhengige av AP-NO
