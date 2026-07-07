LinkML-modell av FINT Økonomi-API, konvertert frå FINT sin Java-baserte modell.

Modellen definerer `Faktura`, `Ordre`, `Oppdrag`, `Kontering` og andre økonomimodul-klasser for integrasjon med FINT Økonomi-tenester.

**Typisk brukar:** Kommunar og fylkeskommunar som brukar FINT Økonomi-API for fakturahandsaming, innkjøp og regnskap.

**Nøkkelklasser:** `Faktura`, `Ordre`, `Oppdrag`, `Kontering`, `Leverandor`, `Kunde`.

**Relasjon til andre modellar i dette repoet:**
- Importerer `fint-common` for felles typar og basisklassar
- Ingen AP-NO-profiler importerte — FINT-modellane er uavhengige av AP-NO
