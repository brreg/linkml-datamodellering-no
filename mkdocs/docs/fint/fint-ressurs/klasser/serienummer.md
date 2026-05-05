

# Slot: serienummer 


_Unikt serienummer frå einingsprodusentens._





URI: [res:serienummer](https://schema.fintlabs.no/ressurs/serienummer)
Alias: serienummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DigitalEnhet](digitalenhet.md) | Ei digital eining som t |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [DigitalEnhet](digitalenhet.md) |
| Slot URI | [res:serienummer](https://schema.fintlabs.no/ressurs/serienummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [DigitalEnhet](digitalenhet.md) |








## In Subsets


* [Obligatorisk](obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | res:serienummer |
| native | https://schema.fintlabs.no/ressurs/:serienummer |




## LinkML Source

<details>
```yaml
name: serienummer
description: Unikt serienummer frå einingsprodusentens.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
slot_uri: res:serienummer
alias: serienummer
owner: DigitalEnhet
domain_of:
- DigitalEnhet
range: string
required: true

```
</details>