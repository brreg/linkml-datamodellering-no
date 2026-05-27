

# Slot: ramme 


_Budsjettramme som skal bere kostnadane._





URI: [adm:ramme](https://schema.fintlabs.no/administrasjon/ramme)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontostreng](kontostreng.md) | Sammensetning av kontodimensjonar for bokføring |  yes  |
| [Fullmakt](fullmakt.md) | Fullmakt til å gjere handlingar i høve til ei gjeven Rolle |  yes  |
| [Arbeidsforhold](arbeidsforhold.md) | Eit avtaleforhold mellom personalressurs og arbeidsgjevar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Ramme](ramme.md) |
| Domain Of | [Kontostreng](kontostreng.md), [Fullmakt](fullmakt.md), [Arbeidsforhold](arbeidsforhold.md) |
| Slot URI | [adm:ramme](https://schema.fintlabs.no/administrasjon/ramme) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:ramme |
| native | https://schema.fintlabs.no/administrasjon/:ramme |




## LinkML Source

<details>
```yaml
name: ramme
description: Budsjettramme som skal bere kostnadane.
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_uri: adm:ramme
domain_of:
- Kontostreng
- Fullmakt
- Arbeidsforhold
range: Ramme

```
</details>