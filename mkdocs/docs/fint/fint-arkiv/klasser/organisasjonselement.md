

# Slot: organisasjonselement 


_Referanse til Organisasjonselement i Administrasjon-domenet._





URI: [ark:organisasjonselement](https://schema.fintlabs.no/arkiv/organisasjonselement)
Alias: organisasjonselement

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrativEnhet](AdministrativEnhet.md) | Administrativ eining med ansvar for saksbehandling |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [AdministrativEnhet](AdministrativEnhet.md) |
| Slot URI | [ark:organisasjonselement](https://schema.fintlabs.no/arkiv/organisasjonselement) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AdministrativEnhet](AdministrativEnhet.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:organisasjonselement |
| native | https://schema.fintlabs.no/arkiv/:organisasjonselement |




## LinkML Source

<details>
```yaml
name: organisasjonselement
description: Referanse til Organisasjonselement i Administrasjon-domenet.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:organisasjonselement
alias: organisasjonselement
owner: AdministrativEnhet
domain_of:
- AdministrativEnhet
range: uriorcurie

```
</details>