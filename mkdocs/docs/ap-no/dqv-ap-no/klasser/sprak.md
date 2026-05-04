

# Slot: sprak 


_Språk brukt i ressursen (dct:language)._





URI: [dct:language](http://purl.org/dc/terms/language)
Alias: sprak

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Tekstdel](Tekstdel.md) | Ein tekstleg del av ein kvalitetsmerknad (Web Annotation) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Spraak](Spraak.md) |
| Domain Of | [Tekstdel](Tekstdel.md) |
| Slot URI | [dct:language](http://purl.org/dc/terms/language) |

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
| self | dct:language |
| native | https://data.norge.no/linkml/dqv-ap-no/sprak |




## LinkML Source

<details>
```yaml
name: sprak
description: Språk brukt i ressursen (dct:language).
from_schema: https://data.norge.no/linkml/dqv-ap-no
rank: 1000
slot_uri: dct:language
alias: sprak
domain_of:
- Tekstdel
range: Spraak
multivalued: true

```
</details>