# Referansemodell

## Modellmetadata

> Denne oversikta viser sentrale metadata for modellen, inkludert versjon, status, lisens, identifikatorar og avhengigheiter. Verdiane er henta direkte frå skjemaet.

| Felt | Verdi |
| --- | --- |
| Name | referansemodell-schema |
| Title | Referansemodell |
| Description | Enkel eksempelmodell for å demonstrere gyldig LinkML-struktur |
| Schema URI | [https://data.norge.no/linkml/referansemodell](https://data.norge.no/linkml/referansemodell) |
| Versjon | 1.3.0 |
| Lisens | [https://data.norge.no/nlod/no/2.0](https://data.norge.no/nlod/no/2.0) |
| Utgjevar | [https://data.norge.no/organizations/974760673](https://data.norge.no/organizations/974760673) |
| Status | [http://purl.org/adms/status/UnderDevelopment](http://purl.org/adms/status/UnderDevelopment) |
| Endringsdato | 2026-07-30 |
| Utgivelsesdato | 2026-07-09 |
| Imports | linkml:types<br>../../ap-no/dcat-ap-no/dcat-ap-no-schema |


## Classes (1)

> Denne oversikta viser berre klassar som er definerte lokalt i referansemodell-schema. Klassar frå importerte modellar er ikkje inkluderte i teljinga, men kan vere refererte frå lokale klassar og kan inngå i valideringsresultat og diagram.

### Obligatorisk (1)

| Class | Description |
| --- | --- |
| [Ressurs](ressurs.md) | Ein generisk ressurs med tittel, skildring og utgjevar. |

## Slots (4)

> Denne oversikta viser eigenskapar som er definert i eller brukt av lokale klassar i modellen. Nokre eigenskapar kan vere importerte frå andre skjema sjølv om dei blir brukte lokalt.
### Verdiar (4)

| Slot | Description | Defined in | Usage |
| --- | --- | --- | --- |
| [beskrivelse](beskrivelse.md) | Fritekstbeskrivelse av ressursen (dct:description). | [https://data.norge.no/ap-no/common-ap-no](https://data.norge.no/ap-no/common-ap-no) | ✅ Brukt lokalt |
| [id](id.md) | URI-identifikator for ressursen. | [https://data.norge.no/ap-no/common-ap-no](https://data.norge.no/ap-no/common-ap-no) | ✅ Brukt lokalt |
| [tittel](tittel.md) | Namn/tittel på ressursen (dct:title). | [https://data.norge.no/ap-no/common-ap-no](https://data.norge.no/ap-no/common-ap-no) | ✅ Brukt lokalt |
| [utgjevar](utgjevar.md) | Organisasjon ansvarleg for ressursen (referert med URI). | [https://data.norge.no/linkml/referansemodell](https://data.norge.no/linkml/referansemodell) | ✅ Brukt lokalt |


## Enumerations (0)

> Denne oversikta viser kontrollerte verdiområde som er definert i eller brukt lokalt i modellen. Importerte enumerasjonar blir dokumenterte separat der det er relevant.


*Ingen enumerations definert lokalt eller brukt i denne modellen.*


## Types (2)

> Denne oversikta viser primitive verdiformat som datoar, URI-ar, språkstrengar og andre grunnleggjande datatypar som er definert i eller brukt i modellen. Mange av desse kjem frå LinkML eller importerte schema.

| Type | URI | Description | Defined in | Usage |
| --- | --- | --- | --- | --- |
| LangString | [rdf:langString](rdf:langString) | Språktagget streng (rdf:langString). | [https://data.norge.no/ap-no/common-ap-no](https://data.norge.no/ap-no/common-ap-no) | ✅ Brukt lokalt |
| uriorcurie | [xsd:anyURI](https://www.w3.org/TR/xmlschema11-2/#anyURI) | a URI or a CURIE | [linkml:types](https://github.com/linkml/linkml-model/blob/main/linkml_model/model/schema/types.yaml) | ✅ Brukt lokalt |
## Subsets (2)

> Denne oversikta viser klassifiseringar av klasser og slots som blir brukt i modellen. For AP-NO-modellar vil dette typisk vere Obligatorisk, Anbefalt og Valgfri.

| Subset | Description | Defined in | Usage |
| --- | --- | --- | --- |
| [Anbefalt](anbefalt.md) | Anbefalte eigenskapar i ein AP-NO-profil. | [https://data.norge.no/ap-no/common-ap-no](https://data.norge.no/ap-no/common-ap-no) | ✅ Brukt lokalt |
| [Obligatorisk](obligatorisk.md) | Obligatoriske eigenskapar i ein AP-NO-profil. | [https://data.norge.no/ap-no/common-ap-no](https://data.norge.no/ap-no/common-ap-no) | ✅ Brukt lokalt |
