FINT-domenet inneheld LinkML-modellar konverterte frå FINT (Felles Integrasjonsplattform for Norske Kommunar/fylkeskommunar) sin Java-baserte API-modell, og dekkjer integrasjonar for fylkeskommunar og kommunar.

`fint-common` er basislaget med felles konsept (identifikatorar, periodar, adresser, kontaktinformasjon) som dei andre FINT-modellane byggjer på: `fint-administrasjon` (HR og organisasjonsstruktur), `fint-arkiv` (Noark 5-basert sakshandsaming), `fint-okonomi` (fakturahandsaming og innkjøp), `fint-personvern` (GDPR-dokumentasjon), `fint-ressurs` (tilgangsstyring) og `fint-utdanning` (elevdata og undervisningsorganisering).

FINT-modellane arvar `camelCase`-navngjeving frå FINT API-spesifikasjonen — eit bevisst avvik frå repoet sin elles `snake_case`-konvensjon for slotnavn.

**Typisk brukar:** Kommunar og fylkeskommunar som brukar FINT-API-a, og utviklarar som implementerer FINT-baserte integrasjonar.
