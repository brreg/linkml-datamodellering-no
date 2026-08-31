

# Slot: id 


_URI-identifikator for ressursen._





URI: [https://data.norge.no/felles/brreg-felles-adresse/id](https://data.norge.no/felles/brreg-felles-adresse/id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeografiskAdresse](geografiskadresse.md) | Ei geografisk adresse. Abstrakt basisklasse for dei konkrete adressetypane under. |  no  |
| [DigitalAdresse](digitaladresse.md) | Ei digital adresse. Abstrakt basisklasse for dei konkrete digitale adressetypane under. |  no  |
| [Poststed](poststed.md) | Eit poststed knytt til eit postnummer. |  no  |
| [Kommune](kommune.md) | Ein norsk kommune. |  no  |
| [Fylke](fylke.md) | Eit norsk fylke. |  no  |
| [Matrikkelnummer](matrikkelnummer.md) | Eit matrikkelnummer (gårds-, bruks-, feste- og seksjonsnummer). |  no  |
| [Adressenummer](adressenummer.md) | Adressenummeret (husnummer og eventuell husbokstav) i ei vegadresse. |  no  |
| [Postboksadresse](postboksadresse.md) | Ei postboksadresse. |  no  |
| [Stedsadresse](stedsadresse.md) | Ei stadfesta adresse utan vegadresse (t.d. i utmark). |  no  |
| [Vegadresse](vegadresse.md) | Ei vegadresse (adressenavn + adressenummer). |  no  |
| [Matrikkeladresse](matrikkeladresse.md) | Ei matrikkeladresse (knytt til eit matrikkelnummer). |  no  |
| [InternasjonalAdresse](internasjonaladresse.md) | Ei adresse i eit anna land enn Noreg, i fri form. |  no  |
| [IPAdresse](ipadresse.md) | Ei IP-adresse. |  no  |
| [EPostadresse](epostadresse.md) | Ei e-postadresse, delt opp i brukarnamn og domenenavn. |  no  |
| [Nettadresse](nettadresse.md) | Ei nettadresse (protokoll, domenenavn og filsti). |  no  |
| [Meldingsboks](meldingsboks.md) | Ei digital meldingsboks (t.d. Altinn). |  no  |
| [Mobiltelefonnummer](mobiltelefonnummer.md) | Eit mobiltelefonnummer. |  no  |
| [Telefonnummer](telefonnummer.md) | Eit fasttelefonnummer. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain Of | [GeografiskAdresse](geografiskadresse.md), [DigitalAdresse](digitaladresse.md), [Poststed](poststed.md), [Kommune](kommune.md), [Fylke](fylke.md), [Matrikkelnummer](matrikkelnummer.md), [Adressenummer](adressenummer.md) |

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


* from schema: https://data.norge.no/felles/brreg-felles-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/felles/brreg-felles-adresse/id |
| native | https://data.norge.no/felles/brreg-felles-adresse/id |




## LinkML Source

<details>
```yaml
name: id
description: URI-identifikator for ressursen.
from_schema: https://data.norge.no/felles/brreg-felles-adresse
identifier: true
domain_of:
- GeografiskAdresse
- DigitalAdresse
- Poststed
- Kommune
- Fylke
- Matrikkelnummer
- Adressenummer
range: uriorcurie
required: true

```
</details>