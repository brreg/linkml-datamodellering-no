

# Slot: fullmakt 


_Fullmakt ressursen er knytt til._





URI: [adm:fullmakt](https://schema.fintlabs.no/administrasjon/fullmakt)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Rolle](rolle.md) | Rettighet eller type fullmakt |  yes  |
| [Personalressurs](personalressurs.md) | Arbeidstakar eller oppdragstakar i organisasjonen |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Fullmakt](fullmakt.md) |
| Domain Of | [Rolle](rolle.md), [Personalressurs](personalressurs.md) |
| Slot URI | [adm:fullmakt](https://schema.fintlabs.no/administrasjon/fullmakt) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:fullmakt |
| native | https://schema.fintlabs.no/administrasjon/:fullmakt |




## LinkML Source

<details>
```yaml
name: fullmakt
description: Fullmakt ressursen er knytt til.
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_uri: adm:fullmakt
domain_of:
- Rolle
- Personalressurs
range: Fullmakt

```
</details>