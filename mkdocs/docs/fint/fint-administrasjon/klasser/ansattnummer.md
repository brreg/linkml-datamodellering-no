

# Slot: ansattnummer 


_Unik identifikator for den tilsette i HR-systemet._





URI: [adm:ansattnummer](https://schema.fintlabs.no/administrasjon/ansattnummer)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Personalressurs](personalressurs.md) | Arbeidstakar eller oppdragstakar i organisasjonen |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identifikator](identifikator.md) |
| Domain Of | [Personalressurs](personalressurs.md) |
| Slot URI | [adm:ansattnummer](https://schema.fintlabs.no/administrasjon/ansattnummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:ansattnummer |
| native | https://schema.fintlabs.no/administrasjon/:ansattnummer |




## LinkML Source

<details>
```yaml
name: ansattnummer
description: Unik identifikator for den tilsette i HR-systemet.
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_uri: adm:ansattnummer
domain_of:
- Personalressurs
range: Identifikator
inlined: true

```
</details>