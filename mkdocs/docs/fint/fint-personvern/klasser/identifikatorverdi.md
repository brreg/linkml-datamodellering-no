

# Slot: identifikatorverdi 


_Ein konkret kombinasjon av teikn og/eller bokstavar som utgjer ein bestemt identifikator._





URI: [fint:identifikatorverdi](https://schema.fintlabs.no/identifikatorverdi)
Alias: identifikatorverdi

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Identifikator](identifikator.md) | Unik identifikasjon til eit objekt |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Identifikator](identifikator.md) |
| Slot URI | [fint:identifikatorverdi](https://schema.fintlabs.no/identifikatorverdi) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Identifikator](identifikator.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-personvern




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:identifikatorverdi |
| native | https://schema.fintlabs.no/personvern/:identifikatorverdi |




## LinkML Source

<details>
```yaml
name: identifikatorverdi
description: Ein konkret kombinasjon av teikn og/eller bokstavar som utgjer ein bestemt
  identifikator.
from_schema: https://data.norge.no/linkml/fint-personvern
rank: 1000
slot_uri: fint:identifikatorverdi
alias: identifikatorverdi
owner: Identifikator
domain_of:
- Identifikator
range: string
required: true

```
</details>