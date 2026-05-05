

# Slot: rettighet 


_Rettigheiter knytt til identiteten._





URI: [res:rettighet](https://schema.fintlabs.no/ressurs/rettighet)
Alias: rettighet

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Identitet](identitet.md) | Identitet som identifiserer innehavaren av rettigheiter i organisasjonen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Rettighet](rettighet.md) |
| Domain Of | [Identitet](identitet.md) |
| Slot URI | [res:rettighet](https://schema.fintlabs.no/ressurs/rettighet) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Identitet](identitet.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | res:rettighet |
| native | https://schema.fintlabs.no/ressurs/:rettighet |




## LinkML Source

<details>
```yaml
name: rettighet
description: Rettigheiter knytt til identiteten.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
slot_uri: res:rettighet
alias: rettighet
owner: Identitet
domain_of:
- Identitet
range: Rettighet
multivalued: true

```
</details>