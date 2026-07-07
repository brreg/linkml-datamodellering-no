common-ap-no er basislaget for alle norske applikasjonsprofiler (AP-NO) i dette repoet, modellert i LinkML.

Skjemaet definerer felles typar, enum-ar og prefiks som vert gjenbrukt på tvers av DCAT-AP-NO, SKOS-AP-NO, ModelDCAT-AP-NO, CPSV-AP-NO og XKOS-AP-NO.

**Typisk brukar:** Utviklare som arbeidar med AP-NO-profilane — skjemaet vert ikkje brukt direkte, berre importert.

**Nøkkeltypar:** `LangString` (rdf:langString), `DateOrDateTimeOrYear` (dato med ulik presisjon), `XHTML` (XHTML-formatert tekst).

**Nøkkelenum:** `AdmsStatus` (ADMS status-URI-ar), `PublisherType` (utgjevartype), `DcatMediaType` (IANA mediatypar).

**Relasjon til andre modellar i dette repoet:**
- Alle AP-NO-profilar importerer `common-ap-no` direkte
- Domenemodellane (`ngr-*`, `oreg-*`, `samt-bu`) importerer AP-NO-profilar, ikkje `common-ap-no` direkte
