

# Slot: art 


_Artskonto (type utgift/inntekt)._





URI: [okn:art](https://schema.fintlabs.no/okonomi/art)
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
| Slot URI | [okn:art](https://schema.fintlabs.no/okonomi/art) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:art |
| native | https://schema.fintlabs.no/okonomi/:art |




## LinkML Source

<details>
```yaml
name: art
description: Artskonto (type utgift/inntekt).
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
slot_uri: okn:art
domain_of:
- Kontostreng
range: string

```
</details>