

# Slot: sjekksumverdi 


_Sjekksumverdi som heksadesimal streng._





URI: [spdx:checksumValue](http://spdx.org/rdf/terms#checksumValue)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sjekksum](sjekksum.md) | Ein sjekksum for ein distribusjon |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Sjekksum](sjekksum.md) |
| Slot URI | [spdx:checksumValue](http://spdx.org/rdf/terms#checksumValue) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | spdx:checksumValue |
| native | https://data.norge.no/linkml/dcat-ap-no/sjekksumverdi |




## LinkML Source

<details>
```yaml
name: sjekksumverdi
description: Sjekksumverdi som heksadesimal streng.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: spdx:checksumValue
domain_of:
- Sjekksum
range: string

```
</details>