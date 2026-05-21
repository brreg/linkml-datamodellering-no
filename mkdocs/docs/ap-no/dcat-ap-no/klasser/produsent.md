

# Slot: produsent 


_Aktøren som primært har skapt ressursen._





URI: [dct:creator](http://purl.org/dc/terms/creator)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  no  |
| [Katalog](katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre kata... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Aktor](aktor.md) |
| Domain Of | [Datasett](datasett.md), [Katalog](katalog.md) |
| Slot URI | [dct:creator](http://purl.org/dc/terms/creator) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:creator |
| native | https://data.norge.no/linkml/dcat-ap-no/produsent |




## LinkML Source

<details>
```yaml
name: produsent
description: Aktøren som primært har skapt ressursen.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dct:creator
domain_of:
- Datasett
- Katalog
range: Aktor

```
</details>