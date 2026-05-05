

# Slot: tiltak 


_Skildrar kva tiltak som skal utførast på eigedommen._





URI: [ark:tiltak](https://schema.fintlabs.no/arkiv/tiltak)
Alias: tiltak

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DispensasjonAutomatiskFredaKulturminne](dispensasjonautomatiskfredakulturminne.md) | Sak om søknad om dispensasjon for tiltak på automatisk freda kulturminne |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [DispensasjonAutomatiskFredaKulturminne](dispensasjonautomatiskfredakulturminne.md) |
| Slot URI | [ark:tiltak](https://schema.fintlabs.no/arkiv/tiltak) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [DispensasjonAutomatiskFredaKulturminne](dispensasjonautomatiskfredakulturminne.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:tiltak |
| native | https://schema.fintlabs.no/arkiv/:tiltak |




## LinkML Source

<details>
```yaml
name: tiltak
description: Skildrar kva tiltak som skal utførast på eigedommen.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:tiltak
alias: tiltak
owner: DispensasjonAutomatiskFredaKulturminne
domain_of:
- DispensasjonAutomatiskFredaKulturminne
range: string

```
</details>