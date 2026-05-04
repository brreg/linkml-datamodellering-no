

# Slot: tema 


_Fagleg tema klassifikasjonen dekkjer (dct:subject)._





URI: [dct:subject](http://purl.org/dc/terms/subject)
Alias: tema

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Klassifikasjon](Klassifikasjon.md) | Ei klassifikasjon – ein systematisk struktur av kategoriar brukt til å klassi... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Konsept](Konsept.md) |
| Domain Of | [Klassifikasjon](Klassifikasjon.md) |
| Slot URI | [dct:subject](http://purl.org/dc/terms/subject) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/xkos-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:subject |
| native | https://data.norge.no/linkml/xkos-ap-no/tema |




## LinkML Source

<details>
```yaml
name: tema
description: Fagleg tema klassifikasjonen dekkjer (dct:subject).
from_schema: https://data.norge.no/linkml/xkos-ap-no
rank: 1000
slot_uri: dct:subject
alias: tema
domain_of:
- Klassifikasjon
range: Konsept
multivalued: true

```
</details>