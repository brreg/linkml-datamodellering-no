

# Slot: brukertype 


_For kva brukertypar denne lisensen er gyldig._





URI: [res:brukertype](https://schema.fintlabs.no/ressurs/brukertype)
Alias: brukertype

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Applikasjonsressurs](Applikasjonsressurs.md) | Informasjon om kor ein applikasjon kan nyttast (lisensressurs) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Brukertype](Brukertype.md) |
| Domain Of | [Applikasjonsressurs](Applikasjonsressurs.md) |
| Slot URI | [res:brukertype](https://schema.fintlabs.no/ressurs/brukertype) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Applikasjonsressurs](Applikasjonsressurs.md) |








## In Subsets


* [Obligatorisk](Obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | res:brukertype |
| native | https://schema.fintlabs.no/ressurs/:brukertype |




## LinkML Source

<details>
```yaml
name: brukertype
description: For kva brukertypar denne lisensen er gyldig.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
slot_uri: res:brukertype
alias: brukertype
owner: Applikasjonsressurs
domain_of:
- Applikasjonsressurs
range: Brukertype
required: true
multivalued: true

```
</details>