

# Slot: begrep 


_Fagomgrep som datasettet handlar om._





URI: [dct:subject](http://purl.org/dc/terms/subject)
Alias: begrep

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasett](Datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Begrep](Begrep.md) |
| Domain Of | [Datasett](Datasett.md) |
| Slot URI | [dct:subject](http://purl.org/dc/terms/subject) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:subject |
| native | https://data.norge.no/linkml/dcat-ap-no/begrep |




## LinkML Source

<details>
```yaml
name: begrep
description: Fagomgrep som datasettet handlar om.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dct:subject
alias: begrep
domain_of:
- Datasett
range: Begrep
multivalued: true

```
</details>