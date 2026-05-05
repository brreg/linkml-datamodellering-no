

# Slot: arbeidsforhold 


_Referanse til Arbeidsforhold i Administrasjon-domenet._





URI: [utd:arbeidsforhold](https://schema.fintlabs.no/utdanning/arbeidsforhold)
Alias: arbeidsforhold

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Undervisningsforhold](undervisningsforhold.md) | Eit tilhøve mellom ein skoleressurs og undervisningsaktivitetar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](uriorcurie.md) |
| Domain Of | [Undervisningsforhold](undervisningsforhold.md) |
| Slot URI | [utd:arbeidsforhold](https://schema.fintlabs.no/utdanning/arbeidsforhold) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Undervisningsforhold](undervisningsforhold.md) |








## In Subsets


* [Obligatorisk](obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:arbeidsforhold |
| native | https://schema.fintlabs.no/utdanning/:arbeidsforhold |




## LinkML Source

<details>
```yaml
name: arbeidsforhold
description: Referanse til Arbeidsforhold i Administrasjon-domenet.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:arbeidsforhold
alias: arbeidsforhold
owner: Undervisningsforhold
domain_of:
- Undervisningsforhold
range: uriorcurie
required: true

```
</details>