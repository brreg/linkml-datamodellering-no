

# Slot: ansvar 


_Ansvarsomrade._





URI: [okn:ansvar](https://schema.fintlabs.no/okonomi/ansvar)
Alias: ansvar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontostreng](kontostreng.md) | Kontodimensjonar for ei postering (kompleks datatype) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Kontostreng](kontostreng.md) |
| Slot URI | [okn:ansvar](https://schema.fintlabs.no/okonomi/ansvar) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Kontostreng](kontostreng.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




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
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:ansvar
alias: ansvar
owner: Kontostreng
domain_of:
- Kontostreng
range: string

```
</details>