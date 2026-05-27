

# Slot: prosjekt 


_Prosjektkode._





URI: [okn:prosjekt](https://schema.fintlabs.no/okonomi/prosjekt)
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
| Slot URI | [okn:prosjekt](https://schema.fintlabs.no/okonomi/prosjekt) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:prosjekt |
| native | https://schema.fintlabs.no/okonomi/:prosjekt |




## LinkML Source

<details>
```yaml
name: prosjekt
description: Prosjektkode.
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
slot_uri: okn:prosjekt
domain_of:
- Kontostreng
range: string

```
</details>