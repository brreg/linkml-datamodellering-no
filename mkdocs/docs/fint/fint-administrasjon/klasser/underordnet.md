

# Slot: underordnet 


_Underordna element i hierarkiet._





URI: [adm:underordnet](https://schema.fintlabs.no/administrasjon/underordnet)
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
| Slot URI | [adm:underordnet](https://schema.fintlabs.no/administrasjon/underordnet) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:underordnet |
| native | https://schema.fintlabs.no/administrasjon/:underordnet |




## LinkML Source

<details>
```yaml
name: underordnet
description: Underordna element i hierarkiet.
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_uri: adm:underordnet
domain_of:
- Ansvar
- Funksjon
- Prosjektart
- Organisasjonselement
range: string
multivalued: true

```
</details>