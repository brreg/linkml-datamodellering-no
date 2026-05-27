

# Slot: eksamen 


_Eksamen._





URI: [utd:eksamen](https://schema.fintlabs.no/utdanning/eksamen)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Rom](rom.md) | Eit rom eller lokale ved ein skule |  yes  |
| [Eksamensgruppe](eksamensgruppe.md) | Ei gruppe elevar som avlegg same eksamen |  yes  |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Eksamen](eksamen.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Rom](rom.md), [Eksamensgruppe](eksamensgruppe.md) |
| Slot URI | [utd:eksamen](https://schema.fintlabs.no/utdanning/eksamen) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:eksamen |
| native | https://schema.fintlabs.no/utdanning/:eksamen |




## LinkML Source

<details>
```yaml
name: eksamen
description: Eksamen.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:eksamen
domain_of:
- UtdanningContainer
- Rom
- Eksamensgruppe
range: Eksamen

```
</details>