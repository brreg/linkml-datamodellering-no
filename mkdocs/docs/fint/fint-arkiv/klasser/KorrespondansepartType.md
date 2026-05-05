

# Slot: korrespondanseparttype 


_Type korrespondansepart._





URI: [ark:korrespondanseparttype](https://schema.fintlabs.no/arkiv/korrespondanseparttype)
Alias: korrespondanseparttype

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Korrespondansepart](korrespondansepart.md) | Verksemd eller person som arkivskapar mottek eller sender arkivdokument til |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [KorrespondansepartType](korrespondanseparttype.md) |
| Domain Of | [Korrespondansepart](korrespondansepart.md) |
| Slot URI | [ark:korrespondanseparttype](https://schema.fintlabs.no/arkiv/korrespondanseparttype) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Korrespondansepart](korrespondansepart.md) |








## In Subsets


* [Obligatorisk](obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:korrespondanseparttype |
| native | https://schema.fintlabs.no/arkiv/:korrespondanseparttype |




## LinkML Source

<details>
```yaml
name: korrespondanseparttype
description: Type korrespondansepart.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:korrespondanseparttype
alias: korrespondanseparttype
owner: Korrespondansepart
domain_of:
- Korrespondansepart
range: KorrespondansepartType
required: true

```
</details>