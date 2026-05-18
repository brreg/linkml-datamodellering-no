

# Slot: person 


_Referanse til Person i Administrasjon-domenet._





URI: [fint:person](https://schema.fintlabs.no/person)
Alias: person

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Personalressurs](personalressurs.md) | Arbeidstakar eller oppdragstakar i organisasjonen |  yes  |
| [Elev](elev.md) | Ein elev registrert i skulesystemet |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Person](person.md) |
| Domain Of | [Elev](elev.md), [Personalressurs](personalressurs.md) |
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
- Personalressurs
range: Person

```
</details>