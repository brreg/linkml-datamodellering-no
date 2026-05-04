

# Slot: prosjekt 


_Prosjektkode._





URI: [okn:prosjekt](https://schema.fintlabs.no/okonomi/prosjekt)
Alias: prosjekt

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontostreng](Kontostreng.md) | Kontodimensjonar for ei postering (kompleks datatype) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Kontostreng](Kontostreng.md) |
| Slot URI | [okn:prosjekt](https://schema.fintlabs.no/okonomi/prosjekt) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Kontostreng](Kontostreng.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




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
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:prosjekt
alias: prosjekt
owner: Kontostreng
domain_of:
- Kontostreng
range: string

```
</details>