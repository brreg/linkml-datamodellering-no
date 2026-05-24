

# Slot: aksjekapitaler 



URI: [https://data.norge.no/linkml/register-over-aksjeeiere/:aksjekapitaler](https://data.norge.no/linkml/register-over-aksjeeiere/:aksjekapitaler)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AksjeeierContainer](aksjeeiercontainer.md) | Containerklasse for alle forretningsobjekt i modellen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Aksjekapital](aksjekapital.md) |
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
| self | https://data.norge.no/linkml/register-over-aksjeeiere/:aksjekapitaler |
| native | https://data.norge.no/linkml/register-over-aksjeeiere/:aksjekapitaler |




## LinkML Source

<details>
```yaml
name: aksjekapitaler
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
owner: AksjeeierContainer
domain_of:
- AksjeeierContainer
range: Aksjekapital
multivalued: true
inlined: true
inlined_as_list: true

```
</details>