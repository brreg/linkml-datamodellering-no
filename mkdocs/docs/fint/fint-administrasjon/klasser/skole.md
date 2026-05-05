

# Slot: skole 


_Referanse til Skole (Utdanning)._





URI: [adm:skole](https://schema.fintlabs.no/administrasjon/skole)
Alias: skole

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Organisasjonselement](organisasjonselement.md) | Eit element i organisasjonsstrukturen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](uriorcurie.md) |
| Domain Of | [Organisasjonselement](organisasjonselement.md) |
| Slot URI | [adm:skole](https://schema.fintlabs.no/administrasjon/skole) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Organisasjonselement](organisasjonselement.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:skole |
| native | https://schema.fintlabs.no/administrasjon/:skole |




## LinkML Source

<details>
```yaml
name: skole
description: Referanse til Skole (Utdanning).
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:skole
alias: skole
owner: Organisasjonselement
domain_of:
- Organisasjonselement
range: uriorcurie

```
</details>