

# Slot: gjeldende_lovgivninger 



URI: [samtbu:gjeldende_lovgivninger](https://data.norge.no/samt/samt-bu/gjeldende_lovgivninger)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SamtBuContainer](samtbucontainer.md) | Containerklasse for alle klasser som kan inngå i datasettet |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [RegulativRessurs](regulativressurs.md) |
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
| self | samtbu:gjeldende_lovgivninger |
| native | samtbu:gjeldende_lovgivninger |




## LinkML Source

<details>
```yaml
name: gjeldende_lovgivninger
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
owner: SamtBuContainer
domain_of:
- SamtBuContainer
range: RegulativRessurs
multivalued: true
inlined: true
inlined_as_list: true

```
</details>