

# Slot: leder 


_Referanse til Personalressurs som er arbeidstakarens leiar._





URI: [ark:leder](https://schema.fintlabs.no/arkiv/leder)
Alias: leder

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Personalmappe](Personalmappe.md) | Saksmappe med opplysningar om ein arbeidstakars arbeidsforhold |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Personalmappe](Personalmappe.md) |
| Slot URI | [ark:leder](https://schema.fintlabs.no/arkiv/leder) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Personalmappe](Personalmappe.md) |








## In Subsets


* [Obligatorisk](Obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:leder |
| native | https://schema.fintlabs.no/arkiv/:leder |




## LinkML Source

<details>
```yaml
name: leder
description: Referanse til Personalressurs som er arbeidstakarens leiar.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:leder
alias: leder
owner: Personalmappe
domain_of:
- Personalmappe
range: uriorcurie
required: true

```
</details>