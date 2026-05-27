

# Slot: forelder 


_Foreldreelement i hierarki._





URI: [adm:forelder](https://schema.fintlabs.no/administrasjon/forelder)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Arbeidsforholdstype](arbeidsforholdstype.md) | Viser kva behov hos arbeidsgjevar arbeidsforholdet dekkjer |  yes  |
| [Stillingskode](stillingskode.md) | Felles kodeverk for stillingar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Arbeidsforholdstype](arbeidsforholdstype.md), [Stillingskode](stillingskode.md) |
| Slot URI | [adm:forelder](https://schema.fintlabs.no/administrasjon/forelder) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:forelder |
| native | https://schema.fintlabs.no/administrasjon/:forelder |




## LinkML Source

<details>
```yaml
name: forelder
description: Foreldreelement i hierarki.
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_uri: adm:forelder
domain_of:
- Arbeidsforholdstype
- Stillingskode
range: string

```
</details>