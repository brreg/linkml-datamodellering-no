

# Slot: organisasjonselement 


_Referanse til Organisasjonselement (Administrasjon) som kan utstede faktura._





URI: [okn:organisasjonselement](https://schema.fintlabs.no/okonomi/organisasjonselement)
Alias: organisasjonselement

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fakturautsteder](fakturautsteder.md) | Eining som utformar og oversender faktura og mottar betaling |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](uriorcurie.md) |
| Domain Of | [Fakturautsteder](fakturautsteder.md) |
| Slot URI | [okn:organisasjonselement](https://schema.fintlabs.no/okonomi/organisasjonselement) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Fakturautsteder](fakturautsteder.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:organisasjonselement |
| native | https://schema.fintlabs.no/okonomi/:organisasjonselement |




## LinkML Source

<details>
```yaml
name: organisasjonselement
description: Referanse til Organisasjonselement (Administrasjon) som kan utstede faktura.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:organisasjonselement
alias: organisasjonselement
owner: Fakturautsteder
domain_of:
- Fakturautsteder
range: uriorcurie

```
</details>