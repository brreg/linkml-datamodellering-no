

# Slot: reservasjonar 



URI: [https://data.norge.no/ngr/ngr-person/reservasjonar](https://data.norge.no/ngr/ngr-person/reservasjonar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonContainer](personcontainer.md) | Rotklasse for NGR-person-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ReservasjonMotKommunikasjonPaaNett](reservasjonmotkommunikasjonpaanett.md) |
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


* from schema: https://data.norge.no/ngr/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/ngr/ngr-person/reservasjonar |
| native | https://data.norge.no/ngr/ngr-person/reservasjonar |




## LinkML Source

<details>
```yaml
name: reservasjonar
from_schema: https://data.norge.no/ngr/ngr-person
rank: 1000
owner: PersonContainer
domain_of:
- PersonContainer
range: ReservasjonMotKommunikasjonPaaNett
multivalued: true
inlined: true
inlined_as_list: true

```
</details>