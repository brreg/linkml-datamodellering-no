

# Slot: tittel 


_Namn/tittel på ressursen (dct:title)._





URI: [dct:title](http://purl.org/dc/terms/title)
Alias: tittel

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Standard](Standard.md) | Ein standard eller spesifikasjon som eit datasett er i samsvar med |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LangString](LangString.md) |
| Domain Of | [Standard](Standard.md) |
| Slot URI | [dct:title](http://purl.org/dc/terms/title) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dqv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:title |
| native | https://data.norge.no/linkml/dqv-ap-no/tittel |




## LinkML Source

<details>
```yaml
name: tittel
description: Namn/tittel på ressursen (dct:title).
from_schema: https://data.norge.no/linkml/dqv-ap-no
rank: 1000
slot_uri: dct:title
alias: tittel
domain_of:
- Standard
range: LangString
multivalued: true

```
</details>