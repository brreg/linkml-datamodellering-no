

# Slot: kontaktpunkt 



URI: [https://data.norge.no/linkml/brreg-begrep/kontaktpunkt](https://data.norge.no/linkml/brreg-begrep/kontaktpunkt)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BegrepContainer](begrepcontainer.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [VCardKontakt](vcardkontakt.md) |
| Domain Of | [BegrepContainer](begrepcontainer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [BegrepContainer](begrepcontainer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/brreg-begrep




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/linkml/brreg-begrep/kontaktpunkt |
| native | https://data.norge.no/linkml/brreg-begrep/kontaktpunkt |




## LinkML Source

<details>
```yaml
name: kontaktpunkt
from_schema: https://data.norge.no/linkml/brreg-begrep
rank: 1000
owner: BegrepContainer
domain_of:
- BegrepContainer
range: VCardKontakt
multivalued: true
inlined: true
inlined_as_list: true

```
</details>