

# Slot: eigd_av 


_Aktør som eig eller er ansvarleg for tenesta._





URI: [cv:ownedBy](http://data.europa.eu/m8g/ownedBy)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Tjeneste](tjeneste.md) | Ei teneste levert av ein ikkje-offentleg aktør |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Aktor](aktor.md) |
| Domain Of | [Tjeneste](tjeneste.md) |
| Slot URI | [cv:ownedBy](http://data.europa.eu/m8g/ownedBy) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/cpsv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cv:ownedBy |
| native | https://data.norge.no/linkml/cpsv-ap-no/eigd_av |




## LinkML Source

<details>
```yaml
name: eigd_av
description: Aktør som eig eller er ansvarleg for tenesta.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: cv:ownedBy
domain_of:
- Tjeneste
range: Aktor
multivalued: true

```
</details>