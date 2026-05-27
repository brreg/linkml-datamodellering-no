

# Slot: kontaktopplysningar 



URI: [https://data.norge.no/ngr/ngr-person/kontaktopplysningar](https://data.norge.no/ngr/ngr-person/kontaktopplysningar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonContainer](personcontainer.md) | Rotklasse for NGR-person-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kontaktopplysninger](kontaktopplysninger.md) |
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
| self | https://data.norge.no/ngr/ngr-person/kontaktopplysningar |
| native | https://data.norge.no/ngr/ngr-person/kontaktopplysningar |




## LinkML Source

<details>
```yaml
name: kontaktopplysningar
from_schema: https://data.norge.no/ngr/ngr-person
rank: 1000
owner: PersonContainer
domain_of:
- PersonContainer
range: Kontaktopplysninger
multivalued: true
inlined: true
inlined_as_list: true

```
</details>