

# Slot: forretningsadresser 



URI: [https://data.norge.no/ngr/ngr-virksomhet/forretningsadresser](https://data.norge.no/ngr/ngr-virksomhet/forretningsadresser)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [VirksomhetContainer](virksomhetcontainer.md) | Rotklasse for NGR-virksomhet-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Forretningsadresse](forretningsadresse.md) |
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
| self | https://data.norge.no/ngr/ngr-virksomhet/forretningsadresser |
| native | https://data.norge.no/ngr/ngr-virksomhet/forretningsadresser |




## LinkML Source

<details>
```yaml
name: forretningsadresser
from_schema: https://data.norge.no/ngr/ngr-virksomhet
rank: 1000
owner: VirksomhetContainer
domain_of:
- VirksomhetContainer
range: Forretningsadresse
multivalued: true
inlined: true
inlined_as_list: true

```
</details>