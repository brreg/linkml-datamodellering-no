

# Slot: utgiver 


_Aktøren som er ansvarleg for å tilgjengeleggjere ressursen._





URI: [dct:publisher](http://purl.org/dc/terms/publisher)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  yes  |
| [Datasettserie](datasettserie.md) | Ei serie av relaterte datasett publisert separat men med felles metadata |  yes  |
| [Datatjeneste](datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  yes  |
| [Katalog](katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre kata... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Aktor](aktor.md) |
| Domain Of | [Datasett](datasett.md), [Datasettserie](datasettserie.md), [Datatjeneste](datatjeneste.md), [Katalog](katalog.md) |
| Slot URI | [dct:publisher](http://purl.org/dc/terms/publisher) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:publisher |
| native | https://data.norge.no/ap-no/dcat-ap-no/utgiver |




## LinkML Source

<details>
```yaml
name: utgiver
description: Aktøren som er ansvarleg for å tilgjengeleggjere ressursen.
from_schema: https://data.norge.no/ap-no/dcat-ap-no
rank: 1000
slot_uri: dct:publisher
domain_of:
- Datasett
- Datasettserie
- Datatjeneste
- Katalog
range: Aktor

```
</details>