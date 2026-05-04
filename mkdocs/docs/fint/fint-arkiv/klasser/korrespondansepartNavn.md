

# Slot: korrespondansepartNavn 


_Namn på person eller organisasjon som er avsender eller mottakar._





URI: [ark:korrespondansepartNavn](https://schema.fintlabs.no/arkiv/korrespondansepartNavn)
Alias: korrespondansepartNavn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Korrespondansepart](Korrespondansepart.md) | Verksemd eller person som arkivskapar mottek eller sender arkivdokument til |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Korrespondansepart](Korrespondansepart.md) |
| Slot URI | [ark:korrespondansepartNavn](https://schema.fintlabs.no/arkiv/korrespondansepartNavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Korrespondansepart](Korrespondansepart.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:korrespondansepartNavn |
| native | https://schema.fintlabs.no/arkiv/:korrespondansepartNavn |




## LinkML Source

<details>
```yaml
name: korrespondansepartNavn
description: Namn på person eller organisasjon som er avsender eller mottakar.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:korrespondansepartNavn
alias: korrespondansepartNavn
owner: Korrespondansepart
domain_of:
- Korrespondansepart
range: string

```
</details>