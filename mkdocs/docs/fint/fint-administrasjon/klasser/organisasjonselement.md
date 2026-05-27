

# Slot: organisasjonselement 


_Organisasjonselement ressursen er knytt til._





URI: [adm:organisasjonselement](https://schema.fintlabs.no/administrasjon/organisasjonselement)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Ansvar](ansvar.md) | Del av kontostrengen som beskriv kven som har ansvaret for ei utgift eller in... |  yes  |
| [Fullmakt](fullmakt.md) | Fullmakt til å gjere handlingar i høve til ei gjeven Rolle |  yes  |
| [AdministrasjonContainer](administrasjoncontainer.md) | Rotcontainer for FINT Administrasjon-instansar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Organisasjonselement](organisasjonselement.md) |
| Domain Of | [AdministrasjonContainer](administrasjoncontainer.md), [Ansvar](ansvar.md), [Fullmakt](fullmakt.md) |
| Slot URI | [adm:organisasjonselement](https://schema.fintlabs.no/administrasjon/organisasjonselement) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:organisasjonselement |
| native | https://schema.fintlabs.no/administrasjon/:organisasjonselement |




## LinkML Source

<details>
```yaml
name: organisasjonselement
description: Organisasjonselement ressursen er knytt til.
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_uri: adm:organisasjonselement
domain_of:
- AdministrasjonContainer
- Ansvar
- Fullmakt
range: Organisasjonselement

```
</details>