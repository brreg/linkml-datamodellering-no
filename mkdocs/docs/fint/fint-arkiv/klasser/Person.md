

# Slot: person 


_Referanse til Person i Administrasjon-domenet._





URI: [ark:person](https://schema.fintlabs.no/arkiv/person)
Alias: person

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
| Slot URI | [ark:person](https://schema.fintlabs.no/arkiv/person) |

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
| self | ark:person |
| native | https://schema.fintlabs.no/arkiv/:person |




## LinkML Source

<details>
```yaml
name: person
description: Referanse til Person i Administrasjon-domenet.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:person
alias: person
owner: Personalmappe
domain_of:
- Personalmappe
range: uriorcurie
required: true

```
</details>