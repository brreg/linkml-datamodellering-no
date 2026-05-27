

# Slot: debet 


_Angir om posteringa er debet eller kredit._





URI: [okn:debet](https://schema.fintlabs.no/okonomi/debet)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Postering](postering.md) | Føring på ein konto i rekneskapet |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:boolean](http://www.w3.org/2001/XMLSchema#boolean) |
| Domain Of | [Postering](postering.md) |
| Slot URI | [okn:debet](https://schema.fintlabs.no/okonomi/debet) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:debet |
| native | https://schema.fintlabs.no/okonomi/:debet |




## LinkML Source

<details>
```yaml
name: debet
description: Angir om posteringa er debet eller kredit.
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
slot_uri: okn:debet
domain_of:
- Postering
range: boolean

```
</details>