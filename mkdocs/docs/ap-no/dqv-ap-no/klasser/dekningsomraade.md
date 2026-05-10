

# Slot: dekningsomraade 


_Geografisk dekningsområde (dct:spatial)._





URI: [dct:spatial](http://purl.org/dc/terms/spatial)
Alias: dekningsomraade

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasettserie](datasettserie.md) | Ei serie av relaterte datasett publisert separat men med felles metadata |  yes  |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  yes  |
| [Katalog](katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre kata... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Konsept](konsept.md) |
| Domain Of | [Datasett](datasett.md), [Datasettserie](datasettserie.md), [Katalog](katalog.md) |
| Slot URI | [dct:spatial](http://purl.org/dc/terms/spatial) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/common-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:spatial |
| native | https://data.norge.no/linkml/common-ap-no/dekningsomraade |




## LinkML Source

<details>
```yaml
name: dekningsomraade
description: Geografisk dekningsområde (dct:spatial).
from_schema: https://data.norge.no/linkml/common-ap-no
slot_uri: dct:spatial
alias: dekningsomraade
domain_of:
- Datasett
- Datasettserie
- Katalog
range: Konsept
multivalued: true

```
</details>