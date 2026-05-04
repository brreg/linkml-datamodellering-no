

# Slot: reservasjonar 



URI: [https://data.norge.no/linkml/ngr-person/reservasjonar](https://data.norge.no/linkml/ngr-person/reservasjonar)
Alias: reservasjonar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonContainer](PersonContainer.md) | Rotklasse for NGR-person-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ReservasjonMotKommunikasjonPaaNett](ReservasjonMotKommunikasjonPaaNett.md) |
| Domain Of | [PersonContainer](PersonContainer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PersonContainer](PersonContainer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/linkml/ngr-person/reservasjonar |
| native | https://data.norge.no/linkml/ngr-person/reservasjonar |




## LinkML Source

<details>
```yaml
name: reservasjonar
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
alias: reservasjonar
owner: PersonContainer
domain_of:
- PersonContainer
range: ReservasjonMotKommunikasjonPaaNett
multivalued: true
inlined: true
inlined_as_list: true

```
</details>