

# Slot: navn_aktoer 


_Namn på aktøren._





URI: [foaf:name](http://xmlns.com/foaf/0.1/name)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Aktoer](aktoer.md) | Ein aktør (person, organisasjon eller system) med ansvar for ein ressurs |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LangString](langstring.md) |
| Domain Of | [Aktoer](aktoer.md) |
| Slot URI | [foaf:name](http://xmlns.com/foaf/0.1/name) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | foaf:name |
| native | https://data.norge.no/ap-no/dcat-ap-no/navn_aktoer |




## LinkML Source

<details>
```yaml
name: navn_aktoer
description: Namn på aktøren.
from_schema: https://data.norge.no/ap-no/dcat-ap-no
slot_uri: foaf:name
domain_of:
- Aktoer
range: LangString
multivalued: true

```
</details>