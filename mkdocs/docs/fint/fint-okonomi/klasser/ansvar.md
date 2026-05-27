

# Slot: ansvar 


_Ansvarsomrade._





URI: [okn:ansvar](https://schema.fintlabs.no/okonomi/ansvar)
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
| Slot URI | [okn:ansvar](https://schema.fintlabs.no/okonomi/ansvar) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:ansvar |
| native | https://schema.fintlabs.no/okonomi/:ansvar |




## LinkML Source

<details>
```yaml
name: ansvar
description: Ansvarsomrade.
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
slot_uri: okn:ansvar
domain_of:
- Kontostreng
range: string

```
</details>