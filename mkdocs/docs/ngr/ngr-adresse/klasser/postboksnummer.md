

# Slot: postboksnummer 


_Postboksnummer (heiltal)._





URI: [ngr:postboksnummer](https://data.norge.no/vocabulary/ngr-adresse#postboksnummer)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Postboks](postboks.md) | Ei postboks registrert i Postboksregisteret |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:integer](http://www.w3.org/2001/XMLSchema#integer) |
| Domain Of | [Postboks](postboks.md) |
| Slot URI | [ngr:postboksnummer](https://data.norge.no/vocabulary/ngr-adresse#postboksnummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngr:postboksnummer |
| native | https://data.norge.no/ngr/ngr-adresse/postboksnummer |




## LinkML Source

<details>
```yaml
name: postboksnummer
description: Postboksnummer (heiltal).
from_schema: https://data.norge.no/ngr/ngr-adresse
rank: 1000
slot_uri: ngr:postboksnummer
domain_of:
- Postboks
range: integer

```
</details>