

# Slot: kvalitetsmerknader 



URI: [samtbuskole:kvalitetsmerknader](https://example.no/ontology/skole#kvalitetsmerknader)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SamtBuContainer](samtbucontainer.md) | Containerklasse for alle klasser som kan inngå i datasettet |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kvalitetsmerknad](kvalitetsmerknad.md) |
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
| self | samtbuskole:kvalitetsmerknader |
| native | samtbuskole:kvalitetsmerknader |




## LinkML Source

<details>
```yaml
name: kvalitetsmerknader
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
owner: SamtBuContainer
domain_of:
- SamtBuContainer
range: Kvalitetsmerknad
multivalued: true
inlined: true
inlined_as_list: true

```
</details>