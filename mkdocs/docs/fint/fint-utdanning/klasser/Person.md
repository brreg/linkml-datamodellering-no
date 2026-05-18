

# Slot: person 


_Referanse til Person i Administrasjon-domenet._





URI: [fint:person](https://schema.fintlabs.no/person)
Alias: person

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtUngdom](otungdom.md) | Eit ungdomsobjekt i oppfølgingstenesta (OT) |  yes  |
| [Laerling](laerling.md) | Ein lærling i yrkesopplæring |  yes  |
| [Elev](elev.md) | Ein elev registrert i skulesystemet |  yes  |
| [Skoleressurs](skoleressurs.md) | Ein lærar eller anna tilsett ved ein skule |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Person](person.md) |
| Domain Of | [Elev](elev.md), [Skoleressurs](skoleressurs.md), [Laerling](laerling.md), [OtUngdom](otungdom.md) |
| Slot URI | [fint:person](https://schema.fintlabs.no/person) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:person |
| native | https://schema.fintlabs.no/:person |




## LinkML Source

<details>
```yaml
name: person
description: Referanse til Person i Administrasjon-domenet.
from_schema: https://data.norge.no/linkml/fint-common
slot_uri: fint:person
alias: person
domain_of:
- Elev
- Skoleressurs
- Laerling
- OtUngdom
range: Person

```
</details>