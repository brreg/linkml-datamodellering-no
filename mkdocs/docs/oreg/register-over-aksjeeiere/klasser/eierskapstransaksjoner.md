

# Slot: eierskapstransaksjoner 



URI: [https://data.norge.no/linkml/register-over-aksjeeiere/:eierskapstransaksjoner](https://data.norge.no/linkml/register-over-aksjeeiere/:eierskapstransaksjoner)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AksjeeierContainer](aksjeeiercontainer.md) | Containerklasse for alle forretningsobjekt i modellen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Eierskapstransaksjon](eierskapstransaksjon.md) |
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
| self | https://data.norge.no/linkml/register-over-aksjeeiere/:eierskapstransaksjoner |
| native | https://data.norge.no/linkml/register-over-aksjeeiere/:eierskapstransaksjoner |




## LinkML Source

<details>
```yaml
name: eierskapstransaksjoner
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
owner: AksjeeierContainer
domain_of:
- AksjeeierContainer
range: Eierskapstransaksjon
multivalued: true
inlined: true
inlined_as_list: true

```
</details>