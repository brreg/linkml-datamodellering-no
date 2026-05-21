

# Slot: tidsrom 


_Tidsperiode ressursen dekkar._





URI: [dct:temporal](http://purl.org/dc/terms/temporal)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  yes  |
| [Datasettserie](datasettserie.md) | Ei serie av relaterte datasett publisert separat men med felles metadata |  yes  |
| [Katalog](katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre kata... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Tidsrom](tidsrom.md) |
| Domain Of | [Datasett](datasett.md), [Datasettserie](datasettserie.md), [Katalog](katalog.md) |
| Slot URI | [dct:temporal](http://purl.org/dc/terms/temporal) |

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
| self | dct:temporal |
| native | https://data.norge.no/linkml/dcat-ap-no/tidsrom |




## LinkML Source

<details>
```yaml
name: tidsrom
description: Tidsperiode ressursen dekkar.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dct:temporal
domain_of:
- Datasett
- Datasettserie
- Katalog
range: Tidsrom
multivalued: true

```
</details>