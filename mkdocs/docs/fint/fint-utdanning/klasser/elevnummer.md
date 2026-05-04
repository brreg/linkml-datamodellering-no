

# Slot: elevnummer 


_Skulens interne elevnummer._





URI: [utd:elevnummer](https://schema.fintlabs.no/utdanning/elevnummer)
Alias: elevnummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Elev](Elev.md) | Ein elev registrert i skulesystemet |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identifikator](Identifikator.md) |
| Domain Of | [Elev](Elev.md) |
| Slot URI | [utd:elevnummer](https://schema.fintlabs.no/utdanning/elevnummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Elev](Elev.md) |








## In Subsets


* [Obligatorisk](Obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:elevnummer |
| native | https://schema.fintlabs.no/utdanning/:elevnummer |




## LinkML Source

<details>
```yaml
name: elevnummer
description: Skulens interne elevnummer.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:elevnummer
alias: elevnummer
owner: Elev
domain_of:
- Elev
range: Identifikator
inlined: true

```
</details>