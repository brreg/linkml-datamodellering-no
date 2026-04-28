

# Slot: dekningsomrade 


_Geografisk dekningsområde._





URI: [dct:spatial](http://purl.org/dc/terms/spatial)
Alias: dekningsomrade

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasettserie](Datasettserie.md) | Ei serie av relaterte datasett publisert separat men med felles metadata |  yes  |
| [Datasett](Datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  yes  |
| [Katalog](Katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre kata... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Begrep](Begrep.md) |
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
description: Geografisk dekningsområde.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dct:spatial
alias: dekningsomrade
domain_of:
- Datasett
- Datasettserie
- Katalog
range: Begrep
multivalued: true

```
</details>