

# Slot: postboksnummer 


_Postboksnummer (heiltal)._





URI: [ngr:postboksnummer](https://data.norge.no/vocabulary/ngr-adresse#postboksnummer)
Alias: postboksnummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Postboks](Postboks.md) | Ei postboks registrert i Postboksregisteret |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [Postboks](Postboks.md) |
| Slot URI | [ngr:postboksnummer](https://data.norge.no/vocabulary/ngr-adresse#postboksnummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngr:postboksnummer |
| native | https://data.norge.no/linkml/ngr-adresse/postboksnummer |




## LinkML Source

<details>
```yaml
name: postboksnummer
description: Postboksnummer (heiltal).
from_schema: https://data.norge.no/linkml/ngr-adresse
rank: 1000
slot_uri: ngr:postboksnummer
alias: postboksnummer
domain_of:
- Postboks
range: integer

```
</details>