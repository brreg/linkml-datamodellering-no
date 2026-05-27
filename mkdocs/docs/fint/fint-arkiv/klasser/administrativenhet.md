

# Slot: administrativenhet 


_Administrative einingar autorisasjonen er gyldig for._





URI: [ark:administrativenhet](https://schema.fintlabs.no/arkiv/administrativenhet)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Autorisasjon](autorisasjon.md) | Siling av kva ein innlogga brukar får lov til å gjere i løysinga |  yes  |






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










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-arkiv




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
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
slot_uri: ark:administrativenhet
domain_of:
- Autorisasjon
range: AdministrativEnhet
multivalued: true

```
</details>