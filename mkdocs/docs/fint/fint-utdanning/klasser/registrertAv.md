

# Slot: registrertAv 


_Skoleressurs som registrerte fråværet._





URI: [utd:registrertAv](https://schema.fintlabs.no/utdanning/registrertAv)
Alias: registrertAv

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fraversregistrering](fraversregistrering.md) | Ei enkelt fråversregistrering for ein elev |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Skoleressurs](skoleressurs.md) |
| Domain Of | [Fraversregistrering](fraversregistrering.md) |
| Slot URI | [utd:registrertAv](https://schema.fintlabs.no/utdanning/registrertAv) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Fraversregistrering](fraversregistrering.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:registrertAv |
| native | https://schema.fintlabs.no/utdanning/:registrertAv |




## LinkML Source

<details>
```yaml
name: registrertAv
description: Skoleressurs som registrerte fråværet.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:registrertAv
alias: registrertAv
owner: Fraversregistrering
domain_of:
- Fraversregistrering
range: Skoleressurs

```
</details>