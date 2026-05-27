

# Slot: brukernavn 


_Brukarnamn til den tilsette._





URI: [adm:brukernavn](https://schema.fintlabs.no/administrasjon/brukernavn)
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
| Slot URI | [adm:brukernavn](https://schema.fintlabs.no/administrasjon/brukernavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:brukernavn |
| native | https://schema.fintlabs.no/administrasjon/:brukernavn |




## LinkML Source

<details>
```yaml
name: brukernavn
description: Brukarnamn til den tilsette.
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_uri: adm:brukernavn
domain_of:
- Personalressurs
range: Identifikator
inlined: true

```
</details>