

# Slot: verdi 


_Karakterverdiar i denne skalaen._





URI: [utd:verdi](https://schema.fintlabs.no/utdanning/verdi)
Alias: verdi

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Karakterskala](Karakterskala.md) | Skala for karaktersetjing (t |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Karakterverdi](Karakterverdi.md) |
| Domain Of | [Karakterskala](Karakterskala.md) |
| Slot URI | [utd:verdi](https://schema.fintlabs.no/utdanning/verdi) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Karakterskala](Karakterskala.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:verdi |
| native | https://schema.fintlabs.no/utdanning/:verdi |




## LinkML Source

<details>
```yaml
name: verdi
description: Karakterverdiar i denne skalaen.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:verdi
alias: verdi
owner: Karakterskala
domain_of:
- Karakterskala
range: Karakterverdi
multivalued: true

```
</details>