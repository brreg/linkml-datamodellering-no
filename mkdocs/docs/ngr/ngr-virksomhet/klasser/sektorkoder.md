

# Slot: sektorkoder 



URI: [https://data.norge.no/ngr/ngr-virksomhet/sektorkoder](https://data.norge.no/ngr/ngr-virksomhet/sektorkoder)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [VirksomhetContainer](virksomhetcontainer.md) | Rotklasse for NGR-virksomhet-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Sektorkode](sektorkode.md) |
| Domain Of | [VirksomhetContainer](virksomhetcontainer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [VirksomhetContainer](virksomhetcontainer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-virksomhet




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/ngr/ngr-virksomhet/sektorkoder |
| native | https://data.norge.no/ngr/ngr-virksomhet/sektorkoder |




## LinkML Source

<details>
```yaml
name: sektorkoder
from_schema: https://data.norge.no/ngr/ngr-virksomhet
rank: 1000
owner: VirksomhetContainer
domain_of:
- VirksomhetContainer
range: Sektorkode
multivalued: true
inlined: true
inlined_as_list: true

```
</details>