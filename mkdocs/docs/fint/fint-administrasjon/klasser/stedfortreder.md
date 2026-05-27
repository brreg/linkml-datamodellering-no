

# Slot: stedfortreder 


_Stedfortredar i fullmaktssamanheng._





URI: [adm:stedfortreder](https://schema.fintlabs.no/administrasjon/stedfortreder)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fullmakt](fullmakt.md) | Fullmakt til å gjere handlingar i høve til ei gjeven Rolle |  yes  |
| [Personalressurs](personalressurs.md) | Arbeidstakar eller oppdragstakar i organisasjonen |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Fullmakt](fullmakt.md), [Personalressurs](personalressurs.md) |
| Slot URI | [adm:stedfortreder](https://schema.fintlabs.no/administrasjon/stedfortreder) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:stedfortreder |
| native | https://schema.fintlabs.no/administrasjon/:stedfortreder |




## LinkML Source

<details>
```yaml
name: stedfortreder
description: Stedfortredar i fullmaktssamanheng.
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_uri: adm:stedfortreder
domain_of:
- Fullmakt
- Personalressurs
range: string

```
</details>