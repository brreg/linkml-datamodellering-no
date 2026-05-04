

# Slot: organisasjonsenhet 


_Referanse til Organisasjonselement grupperinga er tilknytt._





URI: [res:organisasjonsenhet](https://schema.fintlabs.no/ressurs/organisasjonsenhet)
Alias: organisasjonsenhet

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Enhetsgruppe](Enhetsgruppe.md) | Ei gruppering av einsarta digitale einingar (t |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Enhetsgruppe](Enhetsgruppe.md) |
| Slot URI | [res:organisasjonsenhet](https://schema.fintlabs.no/ressurs/organisasjonsenhet) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Enhetsgruppe](Enhetsgruppe.md) |








## In Subsets


* [Obligatorisk](Obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | res:organisasjonsenhet |
| native | https://schema.fintlabs.no/ressurs/:organisasjonsenhet |




## LinkML Source

<details>
```yaml
name: organisasjonsenhet
description: Referanse til Organisasjonselement grupperinga er tilknytt.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
slot_uri: res:organisasjonsenhet
alias: organisasjonsenhet
owner: Enhetsgruppe
domain_of:
- Enhetsgruppe
range: uriorcurie
required: true

```
</details>