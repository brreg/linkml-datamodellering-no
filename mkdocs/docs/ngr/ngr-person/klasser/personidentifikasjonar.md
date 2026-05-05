

# Slot: personidentifikasjonar 



URI: [https://data.norge.no/linkml/ngr-person/personidentifikasjonar](https://data.norge.no/linkml/ngr-person/personidentifikasjonar)
Alias: personidentifikasjonar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonContainer](personcontainer.md) | Rotklasse for NGR-person-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Personidentifikasjon](personidentifikasjon.md) |
| Domain Of | [PersonContainer](personcontainer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PersonContainer](personcontainer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/linkml/ngr-person/personidentifikasjonar |
| native | https://data.norge.no/linkml/ngr-person/personidentifikasjonar |




## LinkML Source

<details>
```yaml
name: personidentifikasjonar
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
alias: personidentifikasjonar
owner: PersonContainer
domain_of:
- PersonContainer
range: Personidentifikasjon
multivalued: true
inlined: true
inlined_as_list: true

```
</details>