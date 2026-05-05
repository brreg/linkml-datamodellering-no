

# Slot: relasjon_til 


_Den relaterte ressursen i ein kvalifisert relasjon._





URI: [dct:relation](http://purl.org/dc/terms/relation)
Alias: relasjon_til

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Relasjon](relasjon.md) | Ein kvalifisert relasjon mellom to ressursar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](uri.md) |
| Domain Of | [Relasjon](relasjon.md) |
| Slot URI | [dct:relation](http://purl.org/dc/terms/relation) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:relation |
| native | samtbuskole:relasjon_til |




## LinkML Source

<details>
```yaml
name: relasjon_til
description: Den relaterte ressursen i ein kvalifisert relasjon.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
slot_uri: dct:relation
alias: relasjon_til
domain_of:
- Relasjon
range: uri

```
</details>