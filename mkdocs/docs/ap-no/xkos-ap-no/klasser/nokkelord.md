

# Slot: nokkelord 


_Nøkkelord som beskriv ressursen (dcat:keyword)._





URI: [dcat:keyword](http://www.w3.org/ns/dcat#keyword)
Alias: nokkelord

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Klassifikasjon](Klassifikasjon.md) | Ei klassifikasjon – ein systematisk struktur av kategoriar brukt til å klassi... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LangString](LangString.md) |
| Domain Of | [Klassifikasjon](Klassifikasjon.md) |
| Slot URI | [dcat:keyword](http://www.w3.org/ns/dcat#keyword) |

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
| self | dcat:keyword |
| native | https://data.norge.no/linkml/xkos-ap-no/nokkelord |




## LinkML Source

<details>
```yaml
name: nokkelord
description: Nøkkelord som beskriv ressursen (dcat:keyword).
from_schema: https://data.norge.no/linkml/xkos-ap-no
rank: 1000
slot_uri: dcat:keyword
alias: nokkelord
domain_of:
- Klassifikasjon
range: LangString
multivalued: true

```
</details>