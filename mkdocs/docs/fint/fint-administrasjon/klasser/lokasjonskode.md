

# Slot: lokasjonskode 


_Kode som identifiserer ein arbeidslokasjon._





URI: [adm:lokasjonskode](https://schema.fintlabs.no/administrasjon/lokasjonskode)
Alias: lokasjonskode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Arbeidslokasjon](Arbeidslokasjon.md) | Fysisk lokasjon der ein tilsett har sitt arbeidsstad |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identifikator](Identifikator.md) |
| Domain Of | [Arbeidslokasjon](Arbeidslokasjon.md) |
| Slot URI | [adm:lokasjonskode](https://schema.fintlabs.no/administrasjon/lokasjonskode) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Arbeidslokasjon](Arbeidslokasjon.md) |








## In Subsets


* [Obligatorisk](Obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:lokasjonskode |
| native | https://schema.fintlabs.no/administrasjon/:lokasjonskode |




## LinkML Source

<details>
```yaml
name: lokasjonskode
description: Kode som identifiserer ein arbeidslokasjon.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:lokasjonskode
alias: lokasjonskode
owner: Arbeidslokasjon
domain_of:
- Arbeidslokasjon
range: Identifikator
required: true
inlined: true

```
</details>