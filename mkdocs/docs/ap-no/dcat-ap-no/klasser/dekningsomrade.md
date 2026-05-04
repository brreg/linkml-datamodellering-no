

# Slot: dekningsomrade 


_Geografisk dekningsområde (dct:spatial)._





URI: [dct:spatial](http://purl.org/dc/terms/spatial)
Alias: dekningsomrade

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Katalog](Katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre kata... |  yes  |
| [Datasett](Datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  yes  |
| [Datasettserie](Datasettserie.md) | Ei serie av relaterte datasett publisert separat men med felles metadata |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Konsept](Konsept.md) |
| Domain Of | [Datasett](Datasett.md), [Datasettserie](Datasettserie.md), [Katalog](Katalog.md) |
| Slot URI | [dct:spatial](http://purl.org/dc/terms/spatial) |

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
| self | dct:spatial |
| native | https://data.norge.no/linkml/dcat-ap-no/dekningsomrade |




## LinkML Source

<details>
```yaml
name: dekningsomrade
description: Geografisk dekningsområde (dct:spatial).
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dct:spatial
alias: dekningsomrade
domain_of:
- Datasett
- Datasettserie
- Katalog
range: Konsept
multivalued: true

```
</details>