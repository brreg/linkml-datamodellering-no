

# Slot: begrep 


_Fagomgrep som datasettet handlar om._





URI: [dct:subject](http://purl.org/dc/terms/subject)
Alias: begrep

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Konsept](konsept.md) |
| Domain Of | [Datasett](datasett.md) |
| Slot URI | [dct:subject](http://purl.org/dc/terms/subject) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:subject |
| native | samtbuskole:begrep |




## LinkML Source

<details>
```yaml
name: begrep
description: Fagomgrep som datasettet handlar om.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
slot_uri: dct:subject
alias: begrep
domain_of:
- Datasett
range: Konsept
multivalued: true

```
</details>