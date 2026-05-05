

# Slot: har_gebyr 


_Gebyr knytt til bruk av datatjenesten._





URI: [cv:hasCost](http://data.europa.eu/m8g/hasCost)
Alias: har_gebyr

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


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cv:hasCost |
| native | samtbuskole:har_gebyr |




## LinkML Source

<details>
```yaml
name: har_gebyr
description: Gebyr knytt til bruk av datatjenesten.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
slot_uri: cv:hasCost
alias: har_gebyr
domain_of:
- Datatjeneste
range: Gebyr
multivalued: true

```
</details>