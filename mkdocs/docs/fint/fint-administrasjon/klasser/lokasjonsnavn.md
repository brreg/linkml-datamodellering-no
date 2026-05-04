

# Slot: lokasjonsnavn 


_Namn som beskriv ein arbeidslokasjon._





URI: [adm:lokasjonsnavn](https://schema.fintlabs.no/administrasjon/lokasjonsnavn)
Alias: lokasjonsnavn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Arbeidslokasjon](Arbeidslokasjon.md) | Fysisk lokasjon der ein tilsett har sitt arbeidsstad |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Arbeidslokasjon](Arbeidslokasjon.md) |
| Slot URI | [adm:lokasjonsnavn](https://schema.fintlabs.no/administrasjon/lokasjonsnavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Arbeidslokasjon](Arbeidslokasjon.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:lokasjonsnavn |
| native | https://schema.fintlabs.no/administrasjon/:lokasjonsnavn |




## LinkML Source

<details>
```yaml
name: lokasjonsnavn
description: Namn som beskriv ein arbeidslokasjon.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:lokasjonsnavn
alias: lokasjonsnavn
owner: Arbeidslokasjon
domain_of:
- Arbeidslokasjon
range: string

```
</details>