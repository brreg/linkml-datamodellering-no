

# Slot: applikasjon 


_Applikasjonen denne ressursen (lisensen) er knytt til._





URI: [res:applikasjon](https://schema.fintlabs.no/ressurs/applikasjon)
Alias: applikasjon

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Applikasjonsressurs](Applikasjonsressurs.md) | Informasjon om kor ein applikasjon kan nyttast (lisensressurs) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Applikasjon](Applikasjon.md) |
| Domain Of | [Applikasjonsressurs](Applikasjonsressurs.md) |
| Slot URI | [res:applikasjon](https://schema.fintlabs.no/ressurs/applikasjon) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
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
| self | res:applikasjon |
| native | https://schema.fintlabs.no/ressurs/:applikasjon |




## LinkML Source

<details>
```yaml
name: applikasjon
description: Applikasjonen denne ressursen (lisensen) er knytt til.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
slot_uri: res:applikasjon
alias: applikasjon
owner: Applikasjonsressurs
domain_of:
- Applikasjonsressurs
range: Applikasjon
required: true

```
</details>