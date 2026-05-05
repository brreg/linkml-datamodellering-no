

# Slot: overfores 


_Angir om fråvær av denne typen skal overførast til HR._





URI: [adm:overfores](https://schema.fintlabs.no/administrasjon/overfores)
Alias: overfores

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fravaerstype](fravaerstype.md) | Type fråvær |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](boolean.md) |
| Domain Of | [Fravaerstype](fravaerstype.md) |
| Slot URI | [adm:overfores](https://schema.fintlabs.no/administrasjon/overfores) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Fravaerstype](fravaerstype.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:overfores |
| native | https://schema.fintlabs.no/administrasjon/:overfores |




## LinkML Source

<details>
```yaml
name: overfores
description: Angir om fråvær av denne typen skal overførast til HR.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:overfores
alias: overfores
owner: Fravaerstype
domain_of:
- Fravaerstype
range: boolean

```
</details>