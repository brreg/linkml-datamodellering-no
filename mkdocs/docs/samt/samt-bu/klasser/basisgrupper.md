

# Slot: basisgrupper 



URI: [samtbuskole:basisgrupper](https://example.no/ontology/skole#basisgrupper)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SamtBuContainer](samtbucontainer.md) | Containerklasse for alle klasser som kan inngå i datasettet |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Basisgruppe](basisgruppe.md) |
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
| self | samtbuskole:basisgrupper |
| native | samtbuskole:basisgrupper |




## LinkML Source

<details>
```yaml
name: basisgrupper
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
owner: SamtBuContainer
domain_of:
- SamtBuContainer
range: Basisgruppe
multivalued: true
inlined: true
inlined_as_list: true

```
</details>