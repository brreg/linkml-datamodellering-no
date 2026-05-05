

# Slot: virksomhetsId 


_Intern unik identifikator i økonomisystemet._





URI: [fint:virksomhetsId](https://schema.fintlabs.no/virksomhetsId)
Alias: virksomhetsId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Virksomhet](virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identifikator](identifikator.md) |
| Domain Of | [Virksomhet](virksomhet.md) |
| Slot URI | [fint:virksomhetsId](https://schema.fintlabs.no/virksomhetsId) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Virksomhet](virksomhet.md) |








## In Subsets


* [Obligatorisk](obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:virksomhetsId |
| native | https://schema.fintlabs.no/utdanning/:virksomhetsId |




## LinkML Source

<details>
```yaml
name: virksomhetsId
description: Intern unik identifikator i økonomisystemet.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: fint:virksomhetsId
alias: virksomhetsId
owner: Virksomhet
domain_of:
- Virksomhet
range: Identifikator
required: true
inlined: true

```
</details>