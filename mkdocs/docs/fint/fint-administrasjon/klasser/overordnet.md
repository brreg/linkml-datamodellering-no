

# Slot: overordnet 


_Overordna element i hierarkiet._





URI: [adm:overordnet](https://schema.fintlabs.no/administrasjon/overordnet)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Ansvar](ansvar.md) | Del av kontostrengen som beskriv kven som har ansvaret for ei utgift eller in... |  yes  |
| [Funksjon](funksjon.md) | Del av kontostrengen som beskriv kva som vert produsert |  yes  |
| [Prosjektart](prosjektart.md) | Element i ei prosjektnedbrytningsstruktur eller arbeidsnedbrytningsstruktur |  yes  |
| [Organisasjonselement](organisasjonselement.md) | Eit element i organisasjonsstrukturen |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Ansvar](ansvar.md), [Funksjon](funksjon.md), [Prosjektart](prosjektart.md), [Organisasjonselement](organisasjonselement.md) |
| Slot URI | [adm:overordnet](https://schema.fintlabs.no/administrasjon/overordnet) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:overordnet |
| native | https://schema.fintlabs.no/administrasjon/:overordnet |




## LinkML Source

<details>
```yaml
name: overordnet
description: Overordna element i hierarkiet.
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_uri: adm:overordnet
domain_of:
- Ansvar
- Funksjon
- Prosjektart
- Organisasjonselement
range: string

```
</details>