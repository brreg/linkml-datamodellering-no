

# Slot: postboksanleggsnavn 


_Namn på postboksanlegget (t.d. bedriftsnamn, institusjon)._





URI: [ngr:postboksanleggsnavn](https://data.norge.no/vocabulary/ngr-adresse#postboksanleggsnavn)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Postboksadresse](postboksadresse.md) | Ei postboksadresse registrert i Postboksregisteret (Posten Norge) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Postboksadresse](postboksadresse.md) |
| Slot URI | [ngr:postboksanleggsnavn](https://data.norge.no/vocabulary/ngr-adresse#postboksanleggsnavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngr:postboksanleggsnavn |
| native | https://data.norge.no/ngr/ngr-adresse/postboksanleggsnavn |




## LinkML Source

<details>
```yaml
name: postboksanleggsnavn
description: Namn på postboksanlegget (t.d. bedriftsnamn, institusjon).
from_schema: https://data.norge.no/ngr/ngr-adresse
rank: 1000
slot_uri: ngr:postboksanleggsnavn
domain_of:
- Postboksadresse
range: string

```
</details>