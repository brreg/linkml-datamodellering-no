

# Slot: aksjeeiere 



URI: [https://data.norge.no/linkml/register-over-aksjeeiere/:aksjeeiere](https://data.norge.no/linkml/register-over-aksjeeiere/:aksjeeiere)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AksjeeierContainer](aksjeeiercontainer.md) | Containerklasse for alle forretningsobjekt i modellen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Aksjeeier](aksjeeier.md) |
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
| self | https://data.norge.no/linkml/register-over-aksjeeiere/:aksjeeiere |
| native | https://data.norge.no/linkml/register-over-aksjeeiere/:aksjeeiere |




## LinkML Source

<details>
```yaml
name: aksjeeiere
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
owner: AksjeeierContainer
domain_of:
- AksjeeierContainer
range: Aksjeeier
multivalued: true
inlined: true
inlined_as_list: true

```
</details>