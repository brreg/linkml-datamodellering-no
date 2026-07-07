LinkML-modell av FINT Utdanning-API, konvertert frå FINT sin Java-baserte modell.

Modellen definerer `Elev`, `Skole`, `Basisgruppe`, `Undervisningsforhold` og andre utdanningsrelaterte klasser for integrasjon med FINT Utdanning-tenester.

**Typisk brukar:** Kommunar, fylkeskommunar og skolar som brukar FINT Utdanning-API for elevdata og organisering av undervisning.

**Nøkkelklasser:** `Elev`, `Skole`, `Basisgruppe`, `Undervisningsforhold`, `Fag`, `Vurdering`, `Fravar`.

**Relasjon til andre modellar i dette repoet:**
- Importerer `fint-common` for felles typar og basisklassar
- Ingen AP-NO-profiler importerte — FINT-modellane er uavhengige av AP-NO
