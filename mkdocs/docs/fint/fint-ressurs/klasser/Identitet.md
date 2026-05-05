

# Slot: identitet 


_Identitetar knytt til rettigheta._





URI: [res:identitet](https://schema.fintlabs.no/ressurs/identitet)
Alias: identitet

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Rettighet](rettighet.md) | Ei namngitt rettighet |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identitet](identitet.md) |
| Domain Of | [Rettighet](rettighet.md) |
| Slot URI | [res:identitet](https://schema.fintlabs.no/ressurs/identitet) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Rettighet](rettighet.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | res:identitet |
| native | https://schema.fintlabs.no/ressurs/:identitet |




## LinkML Source

<details>
```yaml
name: identitet
description: Identitetar knytt til rettigheta.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
slot_uri: res:identitet
alias: identitet
owner: Rettighet
domain_of:
- Rettighet
range: Identitet
multivalued: true

```
</details>