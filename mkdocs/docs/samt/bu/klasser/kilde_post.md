

# Slot: kilde_post 


_Kjelde for katalogposten (ekstern oppføring)._





URI: [dct:source](http://purl.org/dc/terms/source)
Alias: kilde_post

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Katalogpost](katalogpost.md) | Ein katalogpost som beskriv ein ressurs i katalogen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](uri.md) |
| Domain Of | [Katalogpost](katalogpost.md) |
| Slot URI | [dct:source](http://purl.org/dc/terms/source) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:source |
| native | samtbuskole:kilde_post |




## LinkML Source

<details>
```yaml
name: kilde_post
description: Kjelde for katalogposten (ekstern oppføring).
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
slot_uri: dct:source
alias: kilde_post
domain_of:
- Katalogpost
range: uri

```
</details>