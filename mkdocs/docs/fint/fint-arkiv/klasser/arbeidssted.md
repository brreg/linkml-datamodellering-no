

# Slot: arbeidssted 


_Referanse til Organisasjonselement som er arbeidstakarens arbeidsstad._





URI: [ark:arbeidssted](https://schema.fintlabs.no/arkiv/arbeidssted)
Alias: arbeidssted

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Personalmappe](personalmappe.md) | Saksmappe med opplysningar om ein arbeidstakars arbeidsforhold |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](uriorcurie.md) |
| Domain Of | [Personalmappe](personalmappe.md) |
| Slot URI | [ark:arbeidssted](https://schema.fintlabs.no/arkiv/arbeidssted) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Personalmappe](personalmappe.md) |








## In Subsets


* [Obligatorisk](obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:arbeidssted |
| native | https://schema.fintlabs.no/arkiv/:arbeidssted |




## LinkML Source

<details>
```yaml
name: arbeidssted
description: Referanse til Organisasjonselement som er arbeidstakarens arbeidsstad.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:arbeidssted
alias: arbeidssted
owner: Personalmappe
domain_of:
- Personalmappe
range: uriorcurie
required: true

```
</details>