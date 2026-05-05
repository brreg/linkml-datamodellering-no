

# Slot: tilgangsrettigheter 


_Tilgangsrettar for ressursen._





URI: [dct:accessRights](http://purl.org/dc/terms/accessRights)
Alias: tilgangsrettigheter

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  yes  |
| [Datatjeneste](datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Rettighetserklaring](rettighetserklaring.md) |
| Domain Of | [Datasett](datasett.md), [Datatjeneste](datatjeneste.md) |
| Slot URI | [dct:accessRights](http://purl.org/dc/terms/accessRights) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:accessRights |
| native | samtbuskole:tilgangsrettigheter |




## LinkML Source

<details>
```yaml
name: tilgangsrettigheter
description: Tilgangsrettar for ressursen.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
slot_uri: dct:accessRights
alias: tilgangsrettigheter
domain_of:
- Datasett
- Datatjeneste
range: Rettighetserklaring

```
</details>