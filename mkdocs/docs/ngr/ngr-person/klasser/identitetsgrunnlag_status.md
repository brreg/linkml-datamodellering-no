

# Slot: identitetsgrunnlag_status 


_Status/type for identitetsgrunnlaget (t.d. FOLKEREGISTERET, PASS)._





URI: [ngrp:identitetsgrunnlagStatus](https://data.norge.no/vocabulary/ngr-person#identitetsgrunnlagStatus)
Alias: identitetsgrunnlag_status

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Identitetsgrunnlag](Identitetsgrunnlag.md) | Grunnlaget som er brukt for å fastsetje identiteten til ein person ved regist... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Identitetsgrunnlag](Identitetsgrunnlag.md) |
| Slot URI | [ngrp:identitetsgrunnlagStatus](https://data.norge.no/vocabulary/ngr-person#identitetsgrunnlagStatus) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:identitetsgrunnlagStatus |
| native | https://data.norge.no/linkml/ngr-person/identitetsgrunnlag_status |




## LinkML Source

<details>
```yaml
name: identitetsgrunnlag_status
description: Status/type for identitetsgrunnlaget (t.d. FOLKEREGISTERET, PASS).
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
slot_uri: ngrp:identitetsgrunnlagStatus
alias: identitetsgrunnlag_status
domain_of:
- Identitetsgrunnlag
range: string

```
</details>