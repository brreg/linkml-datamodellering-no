

# Slot: applikasjonskategori 


_Kategoriar av applikasjonar._





URI: [res:applikasjonskategori](https://schema.fintlabs.no/ressurs/applikasjonskategori)
Alias: applikasjonskategori

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Applikasjon](applikasjon.md) | Ein applikasjon med tilhøyrande ressursar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Applikasjonskategori](applikasjonskategori.md) |
| Domain Of | [Applikasjon](applikasjon.md) |
| Slot URI | [res:applikasjonskategori](https://schema.fintlabs.no/ressurs/applikasjonskategori) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Applikasjon](applikasjon.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | res:applikasjonskategori |
| native | https://schema.fintlabs.no/ressurs/:applikasjonskategori |




## LinkML Source

<details>
```yaml
name: applikasjonskategori
description: Kategoriar av applikasjonar.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
slot_uri: res:applikasjonskategori
alias: applikasjonskategori
owner: Applikasjon
domain_of:
- Applikasjon
range: Applikasjonskategori
multivalued: true

```
</details>