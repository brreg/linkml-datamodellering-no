

# Slot: filstorrelse 


_Filstørrelse i bytes._





URI: [dcat:byteSize](http://www.w3.org/ns/dcat#byteSize)
Alias: filstorrelse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Distribusjon](distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NonNegativeInteger](nonnegativeinteger.md) |
| Domain Of | [Distribusjon](distribusjon.md) |
| Slot URI | [dcat:byteSize](http://www.w3.org/ns/dcat#byteSize) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:byteSize |
| native | samtbuskole:filstorrelse |




## LinkML Source

<details>
```yaml
name: filstorrelse
description: Filstørrelse i bytes.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
slot_uri: dcat:byteSize
alias: filstorrelse
domain_of:
- Distribusjon
range: NonNegativeInteger

```
</details>