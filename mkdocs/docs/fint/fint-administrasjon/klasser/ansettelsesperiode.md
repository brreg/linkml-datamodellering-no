

# Slot: ansettelsesperiode 


_Perioden personalressursen er i eit tilhøve til organisasjonen._





URI: [adm:ansettelsesperiode](https://schema.fintlabs.no/administrasjon/ansettelsesperiode)
Alias: ansettelsesperiode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Personalressurs](Personalressurs.md) | Arbeidstakar eller oppdragstakar i organisasjonen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Periode](Periode.md) |
| Domain Of | [Personalressurs](Personalressurs.md) |
| Slot URI | [adm:ansettelsesperiode](https://schema.fintlabs.no/administrasjon/ansettelsesperiode) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Personalressurs](Personalressurs.md) |








## In Subsets


* [Obligatorisk](Obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




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
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:ansettelsesperiode
alias: ansettelsesperiode
owner: Personalressurs
domain_of:
- Personalressurs
range: Periode
required: true
inlined: true

```
</details>