

# Slot: ansiennitet 


_Ansiennitet for personalressurs hos arbeidsgjevar._





URI: [adm:ansiennitet](https://schema.fintlabs.no/administrasjon/ansiennitet)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Personalressurs](personalressurs.md) | Arbeidstakar eller oppdragstakar i organisasjonen |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:date](http://www.w3.org/2001/XMLSchema#date) |
| Domain Of | [Personalressurs](personalressurs.md) |
| Slot URI | [adm:ansiennitet](https://schema.fintlabs.no/administrasjon/ansiennitet) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:ansiennitet |
| native | https://schema.fintlabs.no/administrasjon/:ansiennitet |




## LinkML Source

<details>
```yaml
name: ansiennitet
description: Ansiennitet for personalressurs hos arbeidsgjevar.
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_uri: adm:ansiennitet
domain_of:
- Personalressurs
range: date

```
</details>