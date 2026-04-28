

# Slot: har_rolle 


_Rolle ein aktør eller ressurs har i ein relasjon._





URI: [dcat:hadRole](http://www.w3.org/ns/dcat#hadRole)
Alias: har_rolle

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Relasjon](Relasjon.md) | Ein kvalifisert relasjon mellom to ressursar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Begrep](Begrep.md) |
| Domain Of | [Relasjon](Relasjon.md) |
| Slot URI | [dcat:hadRole](http://www.w3.org/ns/dcat#hadRole) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:hadRole |
| native | https://data.norge.no/linkml/dcat-ap-no/har_rolle |




## LinkML Source

<details>
```yaml
name: har_rolle
description: Rolle ein aktør eller ressurs har i ein relasjon.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dcat:hadRole
alias: har_rolle
domain_of:
- Relasjon
range: Begrep

```
</details>