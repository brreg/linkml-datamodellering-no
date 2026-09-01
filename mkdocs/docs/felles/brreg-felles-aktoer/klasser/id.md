

# Slot: id 


_URI-identifikator for ressursen._





URI: [https://data.norge.no/felles/brreg-felles-geografisk-adresse/id](https://data.norge.no/felles/brreg-felles-geografisk-adresse/id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeografiskAdresse](geografiskadresse.md) | Ei geografisk adresse. Abstrakt basisklasse for dei konkrete adressetypane under. |  no  |
| [Poststed](poststed.md) | Eit poststed knytt til eit postnummer. |  no  |
| [Kommune](kommune.md) | Ein norsk kommune. |  no  |
| [Fylke](fylke.md) | Eit norsk fylke. |  no  |
| [Matrikkelnummer](matrikkelnummer.md) | Eit matrikkelnummer (gårds-, bruks-, feste- og seksjonsnummer). |  no  |
| [Adressenummer](adressenummer.md) | Adressenummeret (husnummer og eventuell husbokstav) i ei vegadresse. |  no  |
| [Aktoer](aktoer.md) | Ein aktør — person eller verksemd. Abstrakt basisklasse for Virksomhet og Person. |  no  |
| [Kontaktinformasjon](kontaktinformasjon.md) | Kontaktinformasjon (digital og/eller geografisk adresse) for ein aktør. |  no  |
| [Rolle](rolle.md) | Ei rolle ein aktør har overfor ein annan aktør (t.d. styreleiar, revisor). |  no  |
| [Rolletypegruppe](rolletypegruppe.md) | Ei gruppering av rolletypar (t.d. "styre"). |  no  |
| [Relasjon](relasjon.md) | Ein relasjon mellom to aktørar. |  no  |
| [Personnavn](personnavn.md) | Fullt namn på ein person, delt opp i for-, mellom- og etternamn. |  no  |
| [Personidentifikator](personidentifikator.md) | Ein identifikator for ein person, med ein type som seier kva slag identifikator det er. |  no  |
| [Virksomhetsidentifikator](virksomhetsidentifikator.md) | Ein identifikator for ei verksemd, med ein type som seier kva slag identifikator det er. |  no  |
| [Postboksadresse](postboksadresse.md) | Ei postboksadresse. |  no  |
| [Stedsadresse](stedsadresse.md) | Ei stadfesta adresse utan vegadresse (t.d. i utmark). |  no  |
| [Vegadresse](vegadresse.md) | Ei vegadresse (adressenavn + adressenummer). |  no  |
| [Matrikkeladresse](matrikkeladresse.md) | Ei matrikkeladresse (knytt til eit matrikkelnummer). |  no  |
| [InternasjonalAdresse](internasjonaladresse.md) | Ei adresse i eit anna land enn Noreg, i fri form. |  no  |
| [Virksomhet](virksomhet.md) | Ei verksemd registrert i Einingsregisteret. |  no  |
| [Person](person.md) | Ein fysisk person. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain Of | [GeografiskAdresse](geografiskadresse.md), [Poststed](poststed.md), [Kommune](kommune.md), [Fylke](fylke.md), [Matrikkelnummer](matrikkelnummer.md), [Adressenummer](adressenummer.md), [Aktoer](aktoer.md), [Kontaktinformasjon](kontaktinformasjon.md), [Rolle](rolle.md), [Rolletypegruppe](rolletypegruppe.md), [Relasjon](relasjon.md), [Personnavn](personnavn.md), [Personidentifikator](personidentifikator.md), [Virksomhetsidentifikator](virksomhetsidentifikator.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/felles/brreg-felles-geografisk-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/felles/brreg-felles-geografisk-adresse/id |
| native | https://data.norge.no/felles/brreg-felles-geografisk-adresse/id |




## LinkML Source

<details>
```yaml
name: id
description: URI-identifikator for ressursen.
from_schema: https://data.norge.no/felles/brreg-felles-geografisk-adresse
identifier: true
domain_of:
- GeografiskAdresse
- Poststed
- Kommune
- Fylke
- Matrikkelnummer
- Adressenummer
- Aktoer
- Kontaktinformasjon
- Rolle
- Rolletypegruppe
- Relasjon
- Personnavn
- Personidentifikator
- Virksomhetsidentifikator
range: uriorcurie
required: true

```
</details>