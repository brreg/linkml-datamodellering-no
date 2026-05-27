

# Slot: kontering 


_Kontodimensjonar._





URI: [okn:kontering](https://schema.fintlabs.no/okonomi/kontering)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Postering](postering.md) | Føring på ein konto i rekneskapet |  yes  |
| [Vare](vare.md) | Vare eller teneste som kan leverast og fakturerast |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kontostreng](kontostreng.md) |
| Domain Of | [Postering](postering.md), [Vare](vare.md) |
| Slot URI | [okn:kontering](https://schema.fintlabs.no/okonomi/kontering) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:kontering |
| native | https://schema.fintlabs.no/okonomi/:kontering |




## LinkML Source

<details>
```yaml
name: kontering
description: Kontodimensjonar.
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
slot_uri: okn:kontering
domain_of:
- Postering
- Vare
range: Kontostreng
inlined: true

```
</details>