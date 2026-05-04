

# Slot: beskrivelse 


_Beskriven namn på perioden._





URI: [fint:beskrivelse](https://schema.fintlabs.no/beskrivelse)
Alias: beskrivelse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Periode](Periode.md) | Tidsperiode med obligatorisk start og valfri slutt |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Periode](Periode.md) |
| Slot URI | [fint:beskrivelse](https://schema.fintlabs.no/beskrivelse) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Periode](Periode.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-personvern




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:beskrivelse |
| native | https://schema.fintlabs.no/personvern/:beskrivelse |




## LinkML Source

<details>
```yaml
name: beskrivelse
description: Beskriven namn på perioden.
from_schema: https://data.norge.no/linkml/fint-personvern
rank: 1000
slot_uri: fint:beskrivelse
alias: beskrivelse
owner: Periode
domain_of:
- Periode
range: string

```
</details>