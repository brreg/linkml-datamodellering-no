

# Slot: administrativenhet 


_Administrative einingar autorisasjonen er gyldig for._





URI: [ark:administrativenhet](https://schema.fintlabs.no/arkiv/administrativenhet)
Alias: administrativenhet

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Autorisasjon](autorisasjon.md) | Siling av kva ein innlogga brukar får lov til å gjere i løysinga |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AdministrativEnhet](administrativenhet.md) |
| Domain Of | [Autorisasjon](autorisasjon.md) |
| Slot URI | [ark:administrativenhet](https://schema.fintlabs.no/arkiv/administrativenhet) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Autorisasjon](autorisasjon.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:administrativenhet |
| native | https://schema.fintlabs.no/arkiv/:administrativenhet |




## LinkML Source

<details>
```yaml
name: administrativenhet
description: Administrative einingar autorisasjonen er gyldig for.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:administrativenhet
alias: administrativenhet
owner: Autorisasjon
domain_of:
- Autorisasjon
range: AdministrativEnhet
multivalued: true

```
</details>