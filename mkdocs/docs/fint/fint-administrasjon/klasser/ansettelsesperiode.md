

# Slot: ansettelsesperiode 


_Perioden personalressursen er i eit tilhøve til organisasjonen._





URI: [adm:ansettelsesperiode](https://schema.fintlabs.no/administrasjon/ansettelsesperiode)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Personalressurs](personalressurs.md) | Arbeidstakar eller oppdragstakar i organisasjonen |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Periode](periode.md) |
| Domain Of | [Personalressurs](personalressurs.md) |
| Slot URI | [adm:ansettelsesperiode](https://schema.fintlabs.no/administrasjon/ansettelsesperiode) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:ansettelsesperiode |
| native | https://schema.fintlabs.no/administrasjon/:ansettelsesperiode |




## LinkML Source

<details>
```yaml
name: ansettelsesperiode
description: Perioden personalressursen er i eit tilhøve til organisasjonen.
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_uri: adm:ansettelsesperiode
domain_of:
- Personalressurs
range: Periode
inlined: true

```
</details>