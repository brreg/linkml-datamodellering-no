

# Slot: tidsrom 


_Tidsperiode ressursen dekkar._





URI: [dct:temporal](http://purl.org/dc/terms/temporal)
Alias: tidsrom

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Katalog](Katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre kata... |  no  |
| [Datasett](Datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  yes  |
| [Datasettserie](Datasettserie.md) | Ei serie av relaterte datasett publisert separat men med felles metadata |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Tidsrom](Tidsrom.md) |
| Domain Of | [Datasett](Datasett.md), [Datasettserie](Datasettserie.md), [Katalog](Katalog.md) |
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
alias: tidsrom
domain_of:
- Datasett
- Datasettserie
- Katalog
range: Tidsrom
multivalued: true

```
</details>