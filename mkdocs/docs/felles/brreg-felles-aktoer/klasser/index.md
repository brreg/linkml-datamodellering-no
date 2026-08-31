# BRREG felles aktør

## Modellmetadata

> Modellmetadata viser sentrale metadata for modellen, inkludert versjon, status, lisens, identifikatorar og avhengigheiter. Verdiane er henta direkte frå skjemaet.

| Felt | Verdi |
| --- | --- |
| Name | brreg-felles-aktoer |
| Title | BRREG felles aktør |
| Description | Gjenbrukbare aktørklassar (Aktør, Virksomhet, Person, Rolle m.fl.) utleia frå Brønnøysundregistrene (BR) sin interne BRReferansemodell_v3 (MagicDraw/XMI), pakken "Aktør", pluss dei aktør-relaterte komplekstypane frå Strukturtypekatalog_v1 (Personnavn, Personidentifikator, Virksomhetsidentifikator) som aktørklassane er avhengige av. Importerer brreg-felles-adresse for GeografiskAdresse/DigitalAdresse. Sjå specs/done/felles-typar-enhetsregisteret-fra-br-katalogar.md for bakgrunn, metode og avklaringane denne modellen byggjer på. |
| Schema URI | [https://data.norge.no/felles/brreg-felles-aktoer](https://data.norge.no/felles/brreg-felles-aktoer) |
| Versjon | 0.1.0 |
| Lisens | [https://data.norge.no/nlod/no/2.0](https://data.norge.no/nlod/no/2.0) |
| Utgiver | [https://data.norge.no/organizations/974760673](https://data.norge.no/organizations/974760673) |
| Status | [http://purl.org/adms/status/UnderDevelopment](http://purl.org/adms/status/UnderDevelopment) |
| Endringsdato | 2026-08-31 |
| Utgivelsesdato | 2026-08-31 |
| Imports | `linkml:types`<br>`../brreg-felles-adresse/brreg-felles-adresse-schema` |


### Classes (10)

> Classes viser klasser som er definerte lokalt i brreg-felles-aktoer modellen. 
> Klasser frå importerte modellar er ikkje inkluderte i teljinga, men kan vere refererte frå lokale klasser og kan inngå i valideringsresultat og diagram.  
> Klasser grupperes i Obligatorisk, Anbefalt, Valgfri og Andre (uklassifisert).

#### Andre (10)

| Class | Description |
| --- | --- |
| [Aktoer](aktoer.md) | Ein aktør — person eller verksemd. Abstrakt basisklasse for Virksomhet og Person. |
| [Kontaktinformasjon](kontaktinformasjon.md) | Kontaktinformasjon (digital og/eller geografisk adresse) for ein aktør. |
| [Person](person.md) | Ein fysisk person. |
| [Personidentifikator](personidentifikator.md) | Ein identifikator for ein person, med ein type som seier kva slag identifikator det er. |
| [Personnavn](personnavn.md) | Fullt namn på ein person, delt opp i for-, mellom- og etternamn. |
| [Relasjon](relasjon.md) | Ein relasjon mellom to aktørar. |
| [Rolle](rolle.md) | Ei rolle ein aktør har overfor ein annan aktør (t.d. styreleiar, revisor). |
| [Rolletypegruppe](rolletypegruppe.md) | Ei gruppering av rolletypar (t.d. "styre"). |
| [Virksomhet](virksomhet.md) | Ei verksemd registrert i Einingsregisteret. |
| [Virksomhetsidentifikator](virksomhetsidentifikator.md) | Ein identifikator for ei verksemd, med ein type som seier kva slag identifikator det er. |

### Slots (27)

> Slots viser **eigenskapar** som er definert i eller brukt av lokale klasser i modellen.  
> Eigenskapar grupperes i "Verdiar" som inneheld data, og "Refransar" som refererer til andre klasser.  
> *Defined in* kolonna angir kildeskjemaet for eigenskapen.
#### Verdiar (14)

| Slot | Description | Defined in |
| --- | --- | --- |
| [br_person_id](br_person_id.md) | BR sin interne identifikator for personen. | [https://data.norge.no/felles/brreg-felles-aktoer](https://data.norge.no/felles/brreg-felles-aktoer) |
| [etternavn](etternavn.md) | Etternamnet til personen. | [https://data.norge.no/felles/brreg-felles-aktoer](https://data.norge.no/felles/brreg-felles-aktoer) |
| [foedsel_eller_d_nummer](foedsel_eller_d_nummer.md) | Fødselsnummeret eller D-nummeret til personen. | [https://data.norge.no/felles/brreg-felles-aktoer](https://data.norge.no/felles/brreg-felles-aktoer) |
| [fornavn](fornavn.md) | Fornamnet til personen. | [https://data.norge.no/felles/brreg-felles-aktoer](https://data.norge.no/felles/brreg-felles-aktoer) |
| [id](id.md) | URI-identifikator for ressursen. | [https://data.norge.no/felles/brreg-felles-adresse](https://data.norge.no/felles/brreg-felles-adresse) |
| [identifikator](identifikator.md) | Generisk identifikator (form varierer per samanheng — brukt både for digitale adresser og, via brreg-felles-aktoer, for aktørar generelt). | [https://data.norge.no/felles/brreg-felles-adresse](https://data.norge.no/felles/brreg-felles-adresse) |
| [mellomnavn](mellomnavn.md) | Mellomnamnet til personen, dersom personen har det. | [https://data.norge.no/felles/brreg-felles-aktoer](https://data.norge.no/felles/brreg-felles-aktoer) |
| [organisasjonsnummer](organisasjonsnummer.md) | Organisasjonsnummeret til verksemda. | [https://data.norge.no/felles/brreg-felles-aktoer](https://data.norge.no/felles/brreg-felles-aktoer) |
| [personstatus](personstatus.md) | Statusen til personen. | [https://data.norge.no/felles/brreg-felles-aktoer](https://data.norge.no/felles/brreg-felles-aktoer) |
| [statsborgerskap](statsborgerskap.md) | Statsborgarskapet til personen. | [https://data.norge.no/felles/brreg-felles-aktoer](https://data.norge.no/felles/brreg-felles-aktoer) |
| [type](type.md) | Diskriminator for kva slag adresse dette er. | [https://data.norge.no/felles/brreg-felles-adresse](https://data.norge.no/felles/brreg-felles-adresse) |
| [verdi](verdi.md) | Verdien til identifikatoren. | [https://data.norge.no/felles/brreg-felles-aktoer](https://data.norge.no/felles/brreg-felles-aktoer) |
| [virksomhetsnavn](virksomhetsnavn.md) | Namnet på verksemda. | [https://data.norge.no/felles/brreg-felles-aktoer](https://data.norge.no/felles/brreg-felles-aktoer) |
| [virksomhetsstatus](virksomhetsstatus.md) | Statusen til verksemda. | [https://data.norge.no/felles/brreg-felles-aktoer](https://data.norge.no/felles/brreg-felles-aktoer) |

#### Referansar (11)

| Slot | Description | Defined in |
| --- | --- | --- |
| [aktoer](aktoer.md) | Aktøren relasjonen gjeld. | [https://data.norge.no/felles/brreg-felles-aktoer](https://data.norge.no/felles/brreg-felles-aktoer) |
| [digital_adresse](digital_adresse.md) | Digital adresse knytt til aktøren/rolla. | [https://data.norge.no/felles/brreg-felles-aktoer](https://data.norge.no/felles/brreg-felles-aktoer) |
| [geografisk_adresse](geografisk_adresse.md) | Geografisk adresse knytt til aktøren/rolla. | [https://data.norge.no/felles/brreg-felles-aktoer](https://data.norge.no/felles/brreg-felles-aktoer) |
| [kontaktinformasjon](kontaktinformasjon.md) | Kontaktinformasjon for aktøren/rolla. | [https://data.norge.no/felles/brreg-felles-aktoer](https://data.norge.no/felles/brreg-felles-aktoer) |
| [personidentifikator](personidentifikator.md) | Identifikatoren for personen. | [https://data.norge.no/felles/brreg-felles-aktoer](https://data.norge.no/felles/brreg-felles-aktoer) |
| [personnavn](personnavn.md) | Namnet på personen. | [https://data.norge.no/felles/brreg-felles-aktoer](https://data.norge.no/felles/brreg-felles-aktoer) |
| [relasjon](relasjon.md) | Relasjonar aktøren har til andre aktørar. | [https://data.norge.no/felles/brreg-felles-aktoer](https://data.norge.no/felles/brreg-felles-aktoer) |
| [rolle](rolle.md) | Roller aktøren har. | [https://data.norge.no/felles/brreg-felles-aktoer](https://data.norge.no/felles/brreg-felles-aktoer) |
| [rolleinnehaver](rolleinnehaver.md) | Aktøren som innehar rolla. | [https://data.norge.no/felles/brreg-felles-aktoer](https://data.norge.no/felles/brreg-felles-aktoer) |
| [rolletypegruppe](rolletypegruppe.md) | Rolletypegruppa rolla høyrer til. | [https://data.norge.no/felles/brreg-felles-aktoer](https://data.norge.no/felles/brreg-felles-aktoer) |
| [virksomhetsidentifikator](virksomhetsidentifikator.md) | Identifikatoren for verksemda. | [https://data.norge.no/felles/brreg-felles-aktoer](https://data.norge.no/felles/brreg-felles-aktoer) |

#### Kodar (2)

| Slot | Description | Defined in |
| --- | --- | --- |
| [personidentifikator_type](personidentifikator_type.md) | Kva slag personidentifikator dette er. | [https://data.norge.no/felles/brreg-felles-aktoer](https://data.norge.no/felles/brreg-felles-aktoer) |
| [virksomhetsidentifikator_type](virksomhetsidentifikator_type.md) | Kva slag verksemdsidentifikator dette er. | [https://data.norge.no/felles/brreg-felles-aktoer](https://data.norge.no/felles/brreg-felles-aktoer) |


### Enumerations (2)

> Enumerations viser kontrollerte **verdiområder** som er definert i eller brukt lokalt i modellen.  
> *Defined in* kolonna angir kildeskjemaet for verdiområdet.


| Enumeration | Description | Defined in |
| --- | --- | --- |
| [PersonidentifikatorType](personidentifikatortype.md) | Kva slag personidentifikator ein Personidentifikator inneheld. | [https://data.norge.no/felles/brreg-felles-aktoer](https://data.norge.no/felles/brreg-felles-aktoer) |
| [VirksomhetsidentifikatorType](virksomhetsidentifikatortype.md) | Kva slag verksemdsidentifikator ein Virksomhetsidentifikator inneheld. | [https://data.norge.no/felles/brreg-felles-aktoer](https://data.norge.no/felles/brreg-felles-aktoer) |


### Types (9)

> Types viser primitive **verdiformat** som datoar, URI-ar, språkstrengar og andre grunnleggjande datatypar som er definert i eller brukt i modellen.  
> *Defined in* kolonna angir kildeskjemaet for verdiformatet.

| Type | URI | Description | Defined in |
| --- | --- | --- | --- |
| BRPersonId | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | BR sin interne identifikator for ein person. | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Foedselsnummer | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Norsk fødselsnummer eller D-nummer (11 sifer). | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Landkode | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Kode for land. | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Organisasjonsnummer | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Organisasjonsnummer for ei norsk verksemd (9 sifer), jf. Einingsregisteret. | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| PersonstatusType | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Kode for status på ein person i BR sine register. | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| string | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | A character string | [linkml:types](https://github.com/linkml/linkml-model/blob/main/linkml_model/model/schema/types.yaml) |
| uriorcurie | [xsd:anyURI](https://www.w3.org/TR/xmlschema11-2/#anyURI) | a URI or a CURIE | [linkml:types](https://github.com/linkml/linkml-model/blob/main/linkml_model/model/schema/types.yaml) |
| Virksomhetsnavn | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Namnet på ei verksemd, slik det er registrert i Einingsregisteret. | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Virksomhetsstatus | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Kode for status på ei verksemd (t.d. aktiv, konkurs, oppløyst). | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
### Subsets (0)

> Subsets viser **klassifiseringar** av klasser og slots som blir brukt i modellen. For AP-NO-modellar vil dette typisk vere Obligatorisk, Anbefalt og Valgfri.  
> *Defined in* kolonna angir kildeskjemaet for klassifiseringa.

*Ingen subsets definert lokalt eller brukt i denne modellen.*
