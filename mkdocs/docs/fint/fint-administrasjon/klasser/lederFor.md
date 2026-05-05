

# Slot: lederFor 


_Organisasjonselement personalressursen er leiar for._





URI: [adm:lederFor](https://schema.fintlabs.no/administrasjon/lederFor)
Alias: lederFor

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Personalressurs](personalressurs.md) | Arbeidstakar eller oppdragstakar i organisasjonen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Organisasjonselement](organisasjonselement.md) |
| Domain Of | [Personalressurs](personalressurs.md) |
| Slot URI | [adm:lederFor](https://schema.fintlabs.no/administrasjon/lederFor) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Personalressurs](personalressurs.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:lederFor |
| native | https://schema.fintlabs.no/administrasjon/:lederFor |




## LinkML Source

<details>
```yaml
name: lederFor
description: Organisasjonselement personalressursen er leiar for.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:lederFor
alias: lederFor
owner: Personalressurs
domain_of:
- Personalressurs
range: Organisasjonselement
multivalued: true

```
</details>