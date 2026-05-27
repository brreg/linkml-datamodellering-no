

# Slot: lokasjonsnavn 


_Namn som beskriv ein arbeidslokasjon._





URI: [adm:lokasjonsnavn](https://schema.fintlabs.no/administrasjon/lokasjonsnavn)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Arbeidslokasjon](arbeidslokasjon.md) | Fysisk lokasjon der ein tilsett har sitt arbeidsstad |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Arbeidslokasjon](arbeidslokasjon.md) |
| Slot URI | [adm:lokasjonsnavn](https://schema.fintlabs.no/administrasjon/lokasjonsnavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:lokasjonsnavn |
| native | https://schema.fintlabs.no/administrasjon/:lokasjonsnavn |




## LinkML Source

<details>
```yaml
name: lokasjonsnavn
description: Namn som beskriv ein arbeidslokasjon.
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_uri: adm:lokasjonsnavn
domain_of:
- Arbeidslokasjon
range: string

```
</details>