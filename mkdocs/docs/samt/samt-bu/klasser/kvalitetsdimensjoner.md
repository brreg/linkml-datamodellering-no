

# Slot: kvalitetsdimensjoner 



URI: [samtbuskole:kvalitetsdimensjoner](https://example.no/ontology/skole#kvalitetsdimensjoner)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SamtBuContainer](samtbucontainer.md) | Containerklasse for alle klasser som kan inngå i datasettet |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kvalitetsdimensjon](kvalitetsdimensjon.md) |
| Domain Of | [SamtBuContainer](samtbucontainer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [SamtBuContainer](samtbucontainer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | samtbuskole:kvalitetsdimensjoner |
| native | samtbuskole:kvalitetsdimensjoner |




## LinkML Source

<details>
```yaml
name: kvalitetsdimensjoner
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
owner: SamtBuContainer
domain_of:
- SamtBuContainer
range: Kvalitetsdimensjon
multivalued: true
inlined: true
inlined_as_list: true

```
</details>