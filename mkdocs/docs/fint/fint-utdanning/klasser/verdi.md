

# Slot: verdi 


_Karakterverdiar i denne skalaen._





URI: [utd:verdi](https://schema.fintlabs.no/utdanning/verdi)
Alias: verdi

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Karakterskala](karakterskala.md) | Skala for karaktersetjing (t |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Karakterverdi](karakterverdi.md) |
| Domain Of | [Karakterskala](karakterskala.md) |
| Slot URI | [utd:verdi](https://schema.fintlabs.no/utdanning/verdi) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Karakterskala](karakterskala.md) |








## In Subsets


* [Valgfri](valgfri.md)






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