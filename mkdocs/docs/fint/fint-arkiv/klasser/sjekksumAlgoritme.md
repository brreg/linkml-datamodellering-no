

# Slot: sjekksumAlgoritme 


_Algoritme nytta for å berekne sjekksummen._





URI: [ark:sjekksumAlgoritme](https://schema.fintlabs.no/arkiv/sjekksumAlgoritme)
Alias: sjekksumAlgoritme

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dokumentobjekt](dokumentobjekt.md) | Referanse til éin og berre éin dokumentfil |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Dokumentobjekt](dokumentobjekt.md) |
| Slot URI | [ark:sjekksumAlgoritme](https://schema.fintlabs.no/arkiv/sjekksumAlgoritme) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Dokumentobjekt](dokumentobjekt.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:sjekksumAlgoritme |
| native | https://schema.fintlabs.no/arkiv/:sjekksumAlgoritme |




## LinkML Source

<details>
```yaml
name: sjekksumAlgoritme
description: Algoritme nytta for å berekne sjekksummen.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:sjekksumAlgoritme
alias: sjekksumAlgoritme
owner: Dokumentobjekt
domain_of:
- Dokumentobjekt
range: string

```
</details>