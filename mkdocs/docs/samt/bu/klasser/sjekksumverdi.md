

# Slot: sjekksumverdi 


_Sjekksumverdi som heksadesimal streng._





URI: [spdx:checksumValue](http://spdx.org/rdf/terms#checksumValue)
Alias: sjekksumverdi

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sjekksum](sjekksum.md) | Ein sjekksum for ein distribusjon |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Sjekksum](sjekksum.md) |
| Slot URI | [spdx:checksumValue](http://spdx.org/rdf/terms#checksumValue) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | spdx:checksumValue |
| native | samtbuskole:sjekksumverdi |




## LinkML Source

<details>
```yaml
name: sjekksumverdi
description: Sjekksumverdi som heksadesimal streng.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
slot_uri: spdx:checksumValue
alias: sjekksumverdi
domain_of:
- Sjekksum
range: string

```
</details>