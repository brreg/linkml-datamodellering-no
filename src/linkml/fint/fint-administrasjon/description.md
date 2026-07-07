LinkML-modell av FINT Administrasjon-API, konvertert frå FINT sin Java-baserte modell.

Modellen definerer `Personalressurs`, `Arbeidsforhold`, `Fullmakt`, `Organisasjonselement` og andre HR-relaterte klasser for integrasjon med FINT Administrasjon-tenester.

**Typisk brukar:** Kommunar og fylkeskommunar som brukar FINT Administrasjon-API for personaldata og organisasjonsstruktur.

**Nøkkelklasser:** `Personalressurs`, `Arbeidsforhold`, `Fullmakt`, `Organisasjonselement`, `Lonn`, `Fastlonn`, `Variabelonn`.

**Relasjon til andre modellar i dette repoet:**
- Importerer `fint-common` for felles typar og basisklassar
- Ingen AP-NO-profiler importerte — FINT-modellane er uavhengige av AP-NO
