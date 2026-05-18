

# Slot: vitnemalsmerknad 


_Vitnemålsmerknad._





URI: [utd:vitnemalsmerknad](https://schema.fintlabs.no/utdanning/vitnemalsmerknad)
Alias: vitnemalsmerknad

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Elevvurdering](elevvurdering.md) | Samling av alle vurderingar for ein elev i eit elevforhold |  yes  |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Vitnemalsmerknad](vitnemalsmerknad.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Elevvurdering](elevvurdering.md) |
| Slot URI | [utd:vitnemalsmerknad](https://schema.fintlabs.no/utdanning/vitnemalsmerknad) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:vitnemalsmerknad |
| native | https://schema.fintlabs.no/utdanning/:vitnemalsmerknad |




## LinkML Source

<details>
```yaml
name: vitnemalsmerknad
description: Vitnemålsmerknad.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:vitnemalsmerknad
alias: vitnemalsmerknad
domain_of:
- UtdanningContainer
- Elevvurdering
range: Vitnemalsmerknad

```
</details>