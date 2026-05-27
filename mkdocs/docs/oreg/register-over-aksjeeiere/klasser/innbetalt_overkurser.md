

# Slot: innbetalt_overkurser 



URI: [https://data.norge.no/oreg/register-over-aksjeeiere/:innbetalt_overkurser](https://data.norge.no/oreg/register-over-aksjeeiere/:innbetalt_overkurser)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AksjeeierContainer](aksjeeiercontainer.md) | Containerklasse for alle forretningsobjekt i modellen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [InnbetaltOverkurs](innbetaltoverkurs.md) |
| Domain Of | [AksjeeierContainer](aksjeeiercontainer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AksjeeierContainer](aksjeeiercontainer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/aksje-eierskap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/oreg/register-over-aksjeeiere/:innbetalt_overkurser |
| native | https://data.norge.no/oreg/register-over-aksjeeiere/:innbetalt_overkurser |




## LinkML Source

<details>
```yaml
name: innbetalt_overkurser
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
owner: AksjeeierContainer
domain_of:
- AksjeeierContainer
range: InnbetaltOverkurs
multivalued: true
inlined: true
inlined_as_list: true

```
</details>