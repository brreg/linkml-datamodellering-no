

# Slot: referanseDokumentfil 


_Referanse til fila som inneheld det elektroniske dokumentet._





URI: [ark:referanseDokumentfil](https://schema.fintlabs.no/arkiv/referanseDokumentfil)
Alias: referanseDokumentfil

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dokumentobjekt](Dokumentobjekt.md) | Referanse til éin og berre éin dokumentfil |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Dokumentfil](Dokumentfil.md) |
| Domain Of | [Dokumentobjekt](Dokumentobjekt.md) |
| Slot URI | [ark:referanseDokumentfil](https://schema.fintlabs.no/arkiv/referanseDokumentfil) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Dokumentobjekt](Dokumentobjekt.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:referanseDokumentfil |
| native | https://schema.fintlabs.no/arkiv/:referanseDokumentfil |




## LinkML Source

<details>
```yaml
name: referanseDokumentfil
description: Referanse til fila som inneheld det elektroniske dokumentet.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:referanseDokumentfil
alias: referanseDokumentfil
owner: Dokumentobjekt
domain_of:
- Dokumentobjekt
range: Dokumentfil

```
</details>