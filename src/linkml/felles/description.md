FELLES-domenet inneheld gjenbrukbare felleskomponentar utleia frå Brønnøysundregistrene (BR) sine interne referansemodellar (BRReferansemodell_v3, Strukturtypekatalog_v1, Løsningstypekatalog_v1), meint for import inn i andre domenemodellar — først og fremst OREG-modellane for Enhetsregisteret.

Domenet inneheld fem modellar: `brreg-felles-typer` (gjenbrukbare primitivtypar), `brreg-felles-tid` (tidsperiode-klassar), `brreg-felles-geografisk-adresse` (geografisk adresse), `brreg-felles-digital-adresse` (digital adresse) og `brreg-felles-aktoer` (Aktør, Virksomhet, Person, Rolle m.fl.). Importrekkjefølgja følgjer denne lista — kvar modell kan importere dei føregåande, men ikkje omvendt.

**Typisk brukar:** Modellerarar i Brønnøysundregistrene som treng felles adresse-, aktør-, tids- eller typedefinisjonar i eigne domenemodellar, i staden for å redefinere dei lokalt i kvart skjema.
