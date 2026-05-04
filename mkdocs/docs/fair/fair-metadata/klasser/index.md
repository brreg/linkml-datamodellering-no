# FAIR Metadata Overbygning

FAIR metadata-overbygning som utfyllar norske applikasjonsprofilar for å sikre maskin-aksjonerbar FAIR-konformitet i tråd med FAIR-prinsippa (Findable, Accessible, Interoperable, Reusable).


URI: https://data.norge.no/linkml/fair-metadata

Name: fair-metadata



## Classes

| Class | Description |
| --- | --- |
| [FAIRMetadata](FAIRMetadata.md) | Maskin-aksjonerbar metadata som beskriver ein digital ressurs i tråd med FAIR... |
| [Gjenbruksmetadata](Gjenbruksmetadata.md) | Metadata som støttar gjenbruk av ressursen (FAIR R1 |
| [Katalogregistrering](Katalogregistrering.md) | Dokumenterer registrering i søkbar katalog (FAIR F4) |
| [Proveniensmetadata](Proveniensmetadata.md) | Metadata om opphav og endringshistorie (FAIR R1 |
| [Tilgangsmetadata](Tilgangsmetadata.md) | Metadata for tilgang, autentisering og tilgjengelegheit (FAIR A1/A2) |



## Slots

| Slot | Description |
| --- | --- |
| [ansvarlegAktoer](ansvarlegAktoer.md) | Organisasjon eller aktør som er ansvarleg for ressursen, som URI (FAIR R1 |
| [autentiseringPaakrevd](autentiseringPaakrevd.md) | Om autentisering eller autorisasjon er nødvendig (FAIR A1 |
| [beskrivelse](beskrivelse.md) | URI til ressursen som denne metadata-posten beskriver (FAIR F3) |
| [bruksavgrensingar](bruksavgrensingar.md) | Eventuelle juridiske eller praktiske bruksavgrensingar (FAIR R1 |
| [endringsdato](endringsdato.md) | Sist endra dato (FAIR R1 |
| [generertAvAktivitet](generertAvAktivitet.md) | Aktivitet som har generert ressursen (FAIR R1 |
| [gjenbruksmetadata](gjenbruksmetadata.md) | Metadata som støttar gjenbruk av ressursen (FAIR R1 |
| [id](id.md) | Persistent URI-identifikator for metadata-posten (FAIR F1) |
| [katalogOppfoeringURL](katalogOppfoeringURL.md) | Direkte URL til oppføringa i katalogen (FAIR F4) |
| [katalogregistrering](katalogregistrering.md) | Dokumenterer registrering i søkbar katalog (FAIR F4) |
| [lisens](lisens.md) | Brukslisens for ressursen som URI (FAIR R1 |
| [metadataPersistens](metadataPersistens.md) | Metadata er tilgjengeleg sjølv om sjølve ressursen ikkje lenger er tilgjengel... |
| [opprettingsdato](opprettingsdato.md) | Dato ressursen blei oppretta (FAIR R1 |
| [proveniensmetadata](proveniensmetadata.md) | Metadata om opphav og endringshistorie (FAIR R1 |
| [registreringsdato](registreringsdato.md) | Dato for katalogregistrering (FAIR F4) |
| [registrertIKatalog](registrertIKatalog.md) | URI til katalogen der metadata er registrert (FAIR F4) |
| [ressursIdentifikator](ressursIdentifikator.md) | Global og persistent identifikator for ressursen (FAIR F1) |
| [ressurstype](ressurstype.md) | Type digital ressurs, t |
| [standardoverensstemming](standardoverensstemming.md) | Standardar eller profilar ressursen følgjer, t |
| [tilgangsmetadata](tilgangsmetadata.md) | Metadata for tilgang og tilgjengelegheit (FAIR A1/A2) |
| [tilgangsprotokoll](tilgangsprotokoll.md) | Kommunikasjonsprotokoll, t |
| [tilgangsrettar](tilgangsrettar.md) | Tilgangsnivå som URI, t |
| [tilgangsURL](tilgangsURL.md) | URL for maskinell tilgang til ressurs eller metadata (FAIR A1) |
| [vokabular](vokabular.md) | Kontrollerte vokabular eller ontologiar som ressursen brukar (FAIR I2) |


## Enumerations

| Enumeration | Description |
| --- | --- |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
| [Accessible](Accessible.md) | Eigenskapar knytt til FAIR A-prinsippa (Accessible) |
| [Findable](Findable.md) | Eigenskapar knytt til FAIR F-prinsippa (Findable) |
| [Interoperable](Interoperable.md) | Eigenskapar knytt til FAIR I-prinsippa (Interoperable) |
| [Reusable](Reusable.md) | Eigenskapar knytt til FAIR R-prinsippa (Reusable) |
