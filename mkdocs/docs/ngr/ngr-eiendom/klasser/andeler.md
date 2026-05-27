

# Slot: andeler 



URI: [https://data.norge.no/ngr/ngr-eiendom/andeler](https://data.norge.no/ngr/ngr-eiendom/andeler)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EiendomContainer](eiendomcontainer.md) | Rotklasse for NGR-eiendom-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Andel](andel.md) |
| Domain Of | [EiendomContainer](eiendomcontainer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [EiendomContainer](eiendomcontainer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/ngr/ngr-eiendom/andeler |
| native | https://data.norge.no/ngr/ngr-eiendom/andeler |




## LinkML Source

<details>
```yaml
name: andeler
from_schema: https://data.norge.no/ngr/ngr-eiendom
rank: 1000
owner: EiendomContainer
domain_of:
- EiendomContainer
range: Andel
multivalued: true
inlined: true
inlined_as_list: true

```
</details>