

# Slot: postadresser 



URI: [https://data.norge.no/ngr/ngr-person/postadresser](https://data.norge.no/ngr/ngr-person/postadresser)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonContainer](personcontainer.md) | Rotklasse for NGR-person-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Postadresse](postadresse.md) |
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
| self | https://data.norge.no/ngr/ngr-person/postadresser |
| native | https://data.norge.no/ngr/ngr-person/postadresser |




## LinkML Source

<details>
```yaml
name: postadresser
from_schema: https://data.norge.no/ngr/ngr-person
rank: 1000
owner: PersonContainer
domain_of:
- PersonContainer
range: Postadresse
multivalued: true
inlined: true
inlined_as_list: true

```
</details>