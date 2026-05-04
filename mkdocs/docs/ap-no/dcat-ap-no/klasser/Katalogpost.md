

# Slot: katalogpost 


_Katalogpostar i katalogen._





URI: [dcat:record](http://www.w3.org/ns/dcat#record)
Alias: katalogpost

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Katalog](Katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre kata... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Katalogpost](Katalogpost.md) |
| Domain Of | [Katalog](Katalog.md) |
| Slot URI | [dcat:record](http://www.w3.org/ns/dcat#record) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:record |
| native | https://data.norge.no/linkml/dcat-ap-no/katalogpost |




## LinkML Source

<details>
```yaml
name: katalogpost
description: Katalogpostar i katalogen.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dcat:record
alias: katalogpost
domain_of:
- Katalog
range: Katalogpost
multivalued: true

```
</details>