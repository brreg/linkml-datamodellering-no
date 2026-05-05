

# Slot: organisasjonsKode 


_Beskriven kode for organisasjonselementet._





URI: [adm:organisasjonsKode](https://schema.fintlabs.no/administrasjon/organisasjonsKode)
Alias: organisasjonsKode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Organisasjonselement](organisasjonselement.md) | Eit element i organisasjonsstrukturen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identifikator](identifikator.md) |
| Domain Of | [Organisasjonselement](organisasjonselement.md) |
| Slot URI | [adm:organisasjonsKode](https://schema.fintlabs.no/administrasjon/organisasjonsKode) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Organisasjonselement](organisasjonselement.md) |








## In Subsets


* [Obligatorisk](obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:organisasjonsKode |
| native | https://schema.fintlabs.no/administrasjon/:organisasjonsKode |




## LinkML Source

<details>
```yaml
name: organisasjonsKode
description: Beskriven kode for organisasjonselementet.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:organisasjonsKode
alias: organisasjonsKode
owner: Organisasjonselement
domain_of:
- Organisasjonselement
range: Identifikator
required: true
inlined: true

```
</details>