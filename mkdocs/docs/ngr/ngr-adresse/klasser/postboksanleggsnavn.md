

# Slot: postboksanleggsnavn 


_Namn på postboksanlegget (t.d. bedriftsnamn, institusjon)._





URI: [ngr:postboksanleggsnavn](https://data.norge.no/vocabulary/ngr-adresse#postboksanleggsnavn)
Alias: postboksanleggsnavn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Postboksadresse](Postboksadresse.md) | Ei postboksadresse registrert i Postboksregisteret (Posten Norge) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Postboksadresse](Postboksadresse.md) |
| Slot URI | [ngr:postboksanleggsnavn](https://data.norge.no/vocabulary/ngr-adresse#postboksanleggsnavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngr:postboksanleggsnavn |
| native | https://data.norge.no/linkml/ngr-adresse/postboksanleggsnavn |




## LinkML Source

<details>
```yaml
name: postboksanleggsnavn
description: Namn på postboksanlegget (t.d. bedriftsnamn, institusjon).
from_schema: https://data.norge.no/linkml/ngr-adresse
rank: 1000
slot_uri: ngr:postboksanleggsnavn
alias: postboksanleggsnavn
domain_of:
- Postboksadresse
range: string

```
</details>