

# Slot: tilgangsrettigheter 


_Tilgangsrettar for ressursen._





URI: [dct:accessRights](http://purl.org/dc/terms/accessRights)
Alias: tilgangsrettigheter

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datatjeneste](Datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  no  |
| [Datasett](Datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Rettighetserklaring](Rettighetserklaring.md) |
| Domain Of | [Datasett](Datasett.md), [Datatjeneste](Datatjeneste.md) |
| Slot URI | [dct:accessRights](http://purl.org/dc/terms/accessRights) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:accessRights |
| native | https://data.norge.no/linkml/dcat-ap-no/tilgangsrettigheter |




## LinkML Source

<details>
```yaml
name: tilgangsrettigheter
description: Tilgangsrettar for ressursen.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dct:accessRights
alias: tilgangsrettigheter
domain_of:
- Datasett
- Datatjeneste
range: Rettighetserklaring

```
</details>