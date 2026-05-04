

# Slot: eierskiftedatoer 


_Dato(ar) for eigarskifte i underleininga._





URI: [ngrv:eierskiftedato](https://data.norge.no/vocabulary/ngr-virksomhet#eierskiftedato)
Alias: eierskiftedatoer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Underenhet](Underenhet.md) | Ei underleining er ein geografisk lokasjon der aktiviteten til ei hovudeining... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
| Domain Of | [Underenhet](Underenhet.md) |
| Slot URI | [ngrv:eierskiftedato](https://data.norge.no/vocabulary/ngr-virksomhet#eierskiftedato) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-virksomhet




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrv:eierskiftedato |
| native | https://data.norge.no/linkml/ngr-virksomhet/eierskiftedatoer |




## LinkML Source

<details>
```yaml
name: eierskiftedatoer
description: Dato(ar) for eigarskifte i underleininga.
from_schema: https://data.norge.no/linkml/ngr-virksomhet
rank: 1000
slot_uri: ngrv:eierskiftedato
alias: eierskiftedatoer
domain_of:
- Underenhet
range: date
multivalued: true

```
</details>