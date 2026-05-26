

# Slot: har_gebyr 


_Gebyr knytt til bruk av datatjenesten._





URI: [cv:hasCost](http://data.europa.eu/m8g/hasCost)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datatjeneste](datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Gebyr](gebyr.md) |
| Domain Of | [Datatjeneste](datatjeneste.md) |
| Slot URI | [cv:hasCost](http://data.europa.eu/m8g/hasCost) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cv:hasCost |
| native | https://data.norge.no/linkml/dcat-ap-no/har_gebyr |




## LinkML Source

<details>
```yaml
name: har_gebyr
description: Gebyr knytt til bruk av datatjenesten.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: cv:hasCost
domain_of:
- Datatjeneste
range: Gebyr
multivalued: true

```
</details>