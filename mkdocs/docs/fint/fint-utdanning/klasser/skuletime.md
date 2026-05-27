

# Slot: skuletime 


_Ein skuletime i timeplanen._





URI: [utd:skuletime](https://schema.fintlabs.no/utdanning/skuletime)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Rom](rom.md) | Eit rom eller lokale ved ein skule |  yes  |
| [Undervisningsforhold](undervisningsforhold.md) | Eit tilhøve mellom ein skoleressurs og undervisningsaktivitetar |  yes  |
| [Undervisningsgruppe](undervisningsgruppe.md) | Ei gruppe elevar som følgjer same undervisning i eit eller fleire fag |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Time](time.md) |
| Domain Of | [Rom](rom.md), [Undervisningsforhold](undervisningsforhold.md), [Undervisningsgruppe](undervisningsgruppe.md) |
| Slot URI | [utd:skuletime](https://schema.fintlabs.no/utdanning/skuletime) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:skuletime |
| native | https://schema.fintlabs.no/utdanning/:skuletime |




## LinkML Source

<details>
```yaml
name: skuletime
description: Ein skuletime i timeplanen.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:skuletime
domain_of:
- Rom
- Undervisningsforhold
- Undervisningsgruppe
range: Time
multivalued: true

```
</details>