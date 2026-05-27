

# Slot: referanse 


_Ekstern referanse, t.d. fakturanummer._





URI: [okn:referanse](https://schema.fintlabs.no/okonomi/referanse)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Bilag](bilag.md) | Dokumentasjon til ein transaksjon (kompleks datatype) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Bilag](bilag.md) |
| Slot URI | [okn:referanse](https://schema.fintlabs.no/okonomi/referanse) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:referanse |
| native | https://schema.fintlabs.no/okonomi/:referanse |




## LinkML Source

<details>
```yaml
name: referanse
description: Ekstern referanse, t.d. fakturanummer.
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
slot_uri: okn:referanse
domain_of:
- Bilag
range: string

```
</details>