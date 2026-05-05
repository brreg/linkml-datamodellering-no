

# Slot: partRolle 


_Rolla til parten._





URI: [ark:partRolle](https://schema.fintlabs.no/arkiv/partRolle)
Alias: partRolle

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Part](part.md) | Part til Mappe, Registrering eller Dokumentbeskrivelse |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PartRolle](partrolle.md) |
| Domain Of | [Part](part.md) |
| Slot URI | [ark:partRolle](https://schema.fintlabs.no/arkiv/partRolle) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Part](part.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:partRolle |
| native | https://schema.fintlabs.no/arkiv/:partRolle |




## LinkML Source

<details>
```yaml
name: partRolle
description: Rolla til parten.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:partRolle
alias: partRolle
owner: Part
domain_of:
- Part
range: PartRolle

```
</details>