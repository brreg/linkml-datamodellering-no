

# Slot: rolleNavn 


_Namn på rolla; unik identifikator._





URI: [adm:rolleNavn](https://schema.fintlabs.no/administrasjon/rolleNavn)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Rolle](rolle.md) | Rettighet eller type fullmakt |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identifikator](identifikator.md) |
| Domain Of | [Rolle](rolle.md) |
| Slot URI | [adm:rolleNavn](https://schema.fintlabs.no/administrasjon/rolleNavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:rolleNavn |
| native | https://schema.fintlabs.no/administrasjon/:rolleNavn |




## LinkML Source

<details>
```yaml
name: rolleNavn
description: Namn på rolla; unik identifikator.
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_uri: adm:rolleNavn
domain_of:
- Rolle
range: Identifikator
inlined: true

```
</details>