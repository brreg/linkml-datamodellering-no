# BRREG felles tid

## Modellmetadata

> Modellmetadata viser sentrale metadata for modellen, inkludert versjon, status, lisens, identifikatorar og avhengigheiter. Verdiane er henta direkte frå skjemaet.

| Felt | Verdi |
| --- | --- |
| Name | brreg-felles-tid |
| Title | BRREG felles tid |
| Description | Gjenbrukbare tidsperiode-klassar utleia frå Brønnøysundregistrene (BR) sin interne Strukturtypekatalog_v1 (MagicDraw/XMI), pakken "Komplekstyper" (Tidsperiode, TidsperiodeDatoKlokkeslett). Sjå specs/done/felles-typar-enhetsregisteret-fra-br-katalogar.md for bakgrunn, metode og avklaringane denne modellen byggjer på. |
| Schema URI | [https://data.norge.no/felles/brreg-felles-tid](https://data.norge.no/felles/brreg-felles-tid) |
| Versjon | 0.1.0 |
| Lisens | [https://data.norge.no/nlod/no/2.0](https://data.norge.no/nlod/no/2.0) |
| Utgiver | [https://data.norge.no/organizations/974760673](https://data.norge.no/organizations/974760673) |
| Status | [http://purl.org/adms/status/UnderDevelopment](http://purl.org/adms/status/UnderDevelopment) |
| Endringsdato | 2026-08-31 |
| Utgivelsesdato | 2026-08-31 |
| Imports | `linkml:types`<br>`../brreg-felles-typer/brreg-felles-typer-schema` |


### Classes (2)

> Classes viser klasser som er definerte lokalt i brreg-felles-tid modellen. 
> Klasser frå importerte modellar er ikkje inkluderte i teljinga, men kan vere refererte frå lokale klasser og kan inngå i valideringsresultat og diagram.  
> Klasser grupperes i Obligatorisk, Anbefalt, Valgfri og Andre (uklassifisert).

#### Andre (2)

| Class | Description |
| --- | --- |
| [Tidsperiode](tidsperiode.md) | Ei tidsperiode avgrensa av ein frå- og til-dato. |
| [TidsperiodeDatoKlokkeslett](tidsperiodedatoklokkeslett.md) | Ei tidsperiode avgrensa av frå- og til-tidspunkt (dato og klokkeslett). |

### Slots (5)

> Slots viser **eigenskapar** som er definert i eller brukt av lokale klasser i modellen.  
> Eigenskapar grupperes i "Verdiar" som inneheld data, og "Refransar" som refererer til andre klasser.  
> *Defined in* kolonna angir kildeskjemaet for eigenskapen.
#### Verdiar (5)

| Slot | Description | Defined in |
| --- | --- | --- |
| [fra](fra.md) | Start-tidspunktet (dato og klokkeslett) for tidsperioden. | [https://data.norge.no/felles/brreg-felles-tid](https://data.norge.no/felles/brreg-felles-tid) |
| [fra_dato](fra_dato.md) | Startdatoen for tidsperioden. | [https://data.norge.no/felles/brreg-felles-tid](https://data.norge.no/felles/brreg-felles-tid) |
| [id](id.md) | URI-identifikator for ressursen. | [https://data.norge.no/felles/brreg-felles-tid](https://data.norge.no/felles/brreg-felles-tid) |
| [til](til.md) | Slutt-tidspunktet (dato og klokkeslett) for tidsperioden. | [https://data.norge.no/felles/brreg-felles-tid](https://data.norge.no/felles/brreg-felles-tid) |
| [til_dato](til_dato.md) | Sluttdatoen for tidsperioden. | [https://data.norge.no/felles/brreg-felles-tid](https://data.norge.no/felles/brreg-felles-tid) |


### Enumerations (0)

> Enumerations viser kontrollerte **verdiområder** som er definert i eller brukt lokalt i modellen.  
> *Defined in* kolonna angir kildeskjemaet for verdiområdet.


*Ingen enumerations definert lokalt eller brukt i denne modellen.*


### Types (3)

> Types viser primitive **verdiformat** som datoar, URI-ar, språkstrengar og andre grunnleggjande datatypar som er definert i eller brukt i modellen.  
> *Defined in* kolonna angir kildeskjemaet for verdiformatet.

| Type | URI | Description | Defined in |
| --- | --- | --- | --- |
| date | [xsd:date](https://www.w3.org/TR/xmlschema11-2/#date) | a date (year, month and day) in an idealized calendar | [linkml:types](https://github.com/linkml/linkml-model/blob/main/linkml_model/model/schema/types.yaml) |
| DateTime | [xsd:dateTime](https://www.w3.org/TR/xmlschema11-2/#dateTime) | Dato og klokkeslett (xsd:dateTime). | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| uriorcurie | [xsd:anyURI](https://www.w3.org/TR/xmlschema11-2/#anyURI) | a URI or a CURIE | [linkml:types](https://github.com/linkml/linkml-model/blob/main/linkml_model/model/schema/types.yaml) |
### Subsets (0)

> Subsets viser **klassifiseringar** av klasser og slots som blir brukt i modellen. For AP-NO-modellar vil dette typisk vere Obligatorisk, Anbefalt og Valgfri.  
> *Defined in* kolonna angir kildeskjemaet for klassifiseringa.

*Ingen subsets definert lokalt eller brukt i denne modellen.*
