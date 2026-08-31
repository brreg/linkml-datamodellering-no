

# Slot: type 


_Diskriminator for kva slag adresse dette er._





URI: [brreg_felles_adresse:type](https://data.norge.no/felles/brreg-felles-adresse/type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeografiskAdresse](geografiskadresse.md) | Ei geografisk adresse. Abstrakt basisklasse for dei konkrete adressetypane under. |  yes  |
| [DigitalAdresse](digitaladresse.md) | Ei digital adresse. Abstrakt basisklasse for dei konkrete digitale adressetypane under. |  yes  |
| [Rolle](rolle.md) | Ei rolle ein aktør har overfor ein annan aktør (t.d. styreleiar, revisor). |  no  |
| [Rolletypegruppe](rolletypegruppe.md) | Ei gruppering av rolletypar (t.d. "styre"). |  no  |
| [Relasjon](relasjon.md) | Ein relasjon mellom to aktørar. |  no  |
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
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [GeografiskAdresse](geografiskadresse.md), [DigitalAdresse](digitaladresse.md), [Rolle](rolle.md), [Rolletypegruppe](rolletypegruppe.md), [Relasjon](relasjon.md) |
| Slot URI | [brreg_felles_adresse:type](https://data.norge.no/felles/brreg-felles-adresse/type) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/felles/brreg-felles-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | brreg_felles_adresse:type |
| native | https://data.norge.no/felles/brreg-felles-adresse/type |




## LinkML Source

<details>
```yaml
name: type
description: Diskriminator for kva slag adresse dette er.
from_schema: https://data.norge.no/felles/brreg-felles-adresse
slot_uri: brreg_felles_adresse:type
domain_of:
- GeografiskAdresse
- DigitalAdresse
- Rolle
- Rolletypegruppe
- Relasjon
range: string

```
</details>