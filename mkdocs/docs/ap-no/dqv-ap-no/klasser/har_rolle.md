

# Slot: har_rolle 


_Rolle ein aktør eller ressurs har i ein relasjon._





URI: [dcat:hadRole](http://www.w3.org/ns/dcat#hadRole)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Relasjon](relasjon.md) | Ein kvalifisert relasjon mellom to ressursar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Relasjon](relasjon.md) |
| Slot URI | [dcat:hadRole](http://www.w3.org/ns/dcat#hadRole) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:hadRole |
| native | https://data.norge.no/ap-no/dcat-ap-no/har_rolle |




## LinkML Source

<details>
```yaml
name: har_rolle
description: Rolle ein aktør eller ressurs har i ein relasjon.
from_schema: https://data.norge.no/ap-no/dcat-ap-no
slot_uri: dcat:hadRole
domain_of:
- Relasjon
range: string

```
</details>