

# Slot: bostedsadresser 



URI: [https://data.norge.no/ngr/ngr-person/bostedsadresser](https://data.norge.no/ngr/ngr-person/bostedsadresser)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonContainer](personcontainer.md) | Rotklasse for NGR-person-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Bostedsadresse](bostedsadresse.md) |
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
| self | https://data.norge.no/ngr/ngr-person/bostedsadresser |
| native | https://data.norge.no/ngr/ngr-person/bostedsadresser |




## LinkML Source

<details>
```yaml
name: bostedsadresser
from_schema: https://data.norge.no/ngr/ngr-person
rank: 1000
owner: PersonContainer
domain_of:
- PersonContainer
range: Bostedsadresse
multivalued: true
inlined: true
inlined_as_list: true

```
</details>