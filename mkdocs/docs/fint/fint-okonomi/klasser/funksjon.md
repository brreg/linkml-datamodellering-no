

# Slot: funksjon 


_Funksjonskode (KOSTRA)._





URI: [okn:funksjon](https://schema.fintlabs.no/okonomi/funksjon)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontostreng](kontostreng.md) | Kontodimensjonar for ei postering (kompleks datatype) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Kontostreng](kontostreng.md) |
| Slot URI | [okn:funksjon](https://schema.fintlabs.no/okonomi/funksjon) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:funksjon |
| native | https://schema.fintlabs.no/okonomi/:funksjon |




## LinkML Source

<details>
```yaml
name: funksjon
description: Funksjonskode (KOSTRA).
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
slot_uri: okn:funksjon
domain_of:
- Kontostreng
range: string

```
</details>