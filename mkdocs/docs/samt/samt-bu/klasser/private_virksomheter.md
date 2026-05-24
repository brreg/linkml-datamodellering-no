

# Slot: private_virksomheter 



URI: [samtbuskole:private_virksomheter](https://example.no/ontology/skole#private_virksomheter)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SamtBuContainer](samtbucontainer.md) | Containerklasse for alle klasser som kan inngå i datasettet |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PrivatVirksomhet](privatvirksomhet.md) |
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
| self | samtbuskole:private_virksomheter |
| native | samtbuskole:private_virksomheter |




## LinkML Source

<details>
```yaml
name: private_virksomheter
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
owner: SamtBuContainer
domain_of:
- SamtBuContainer
range: PrivatVirksomhet
multivalued: true
inlined: true
inlined_as_list: true

```
</details>