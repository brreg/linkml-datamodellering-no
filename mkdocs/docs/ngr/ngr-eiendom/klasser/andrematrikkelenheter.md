

# Slot: andreMatrikkelenheter 



URI: [https://data.norge.no/ngr/ngr-eiendom/andreMatrikkelenheter](https://data.norge.no/ngr/ngr-eiendom/andreMatrikkelenheter)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EiendomContainer](eiendomcontainer.md) | Rotklasse for NGR-eiendom-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AnnenMatrikkelenhet](annenmatrikkelenhet.md) |
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
| self | https://data.norge.no/ngr/ngr-eiendom/andreMatrikkelenheter |
| native | https://data.norge.no/ngr/ngr-eiendom/andreMatrikkelenheter |




## LinkML Source

<details>
```yaml
name: andreMatrikkelenheter
from_schema: https://data.norge.no/ngr/ngr-eiendom
rank: 1000
owner: EiendomContainer
domain_of:
- EiendomContainer
range: AnnenMatrikkelenhet
multivalued: true
inlined: true
inlined_as_list: true

```
</details>