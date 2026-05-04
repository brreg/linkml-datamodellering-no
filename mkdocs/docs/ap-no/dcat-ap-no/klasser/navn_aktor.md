

# Slot: navn_aktor 


_Namn på aktøren._





URI: [foaf:name](http://xmlns.com/foaf/0.1/name)
Alias: navn_aktor

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Aktor](Aktor.md) | Ein aktør (person, organisasjon eller system) med ansvar for ein ressurs |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LangString](LangString.md) |
| Domain Of | [Aktor](Aktor.md) |
| Slot URI | [foaf:name](http://xmlns.com/foaf/0.1/name) |

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
| self | foaf:name |
| native | https://data.norge.no/linkml/dcat-ap-no/navn_aktor |




## LinkML Source

<details>
```yaml
name: navn_aktor
description: Namn på aktøren.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: foaf:name
alias: navn_aktor
domain_of:
- Aktor
range: LangString
multivalued: true

```
</details>