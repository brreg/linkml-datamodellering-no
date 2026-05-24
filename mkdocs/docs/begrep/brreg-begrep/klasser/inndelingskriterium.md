

# Slot: inndelingskriterium 


_Inndelingskriterium for ein generisk eller partitiv relasjon (dct:description)._





URI: [dct:description](http://purl.org/dc/terms/description)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeneriskRelasjon](generiskrelasjon.md) | Ein generisk relasjon mellom eit overomgrep og eit underomgrep |  yes  |
| [PartitivRelasjon](partitivrelasjon.md) | Ein partitiv relasjon mellom eit heilskapleg og eit partitivt omgrep |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LangString](langstring.md) |
| Domain Of | [GeneriskRelasjon](generiskrelasjon.md), [PartitivRelasjon](partitivrelasjon.md) |
| Slot URI | [dct:description](http://purl.org/dc/terms/description) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/skos-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:description |
| native | https://data.norge.no/linkml/skos-ap-no/inndelingskriterium |




## LinkML Source

<details>
```yaml
name: inndelingskriterium
description: Inndelingskriterium for ein generisk eller partitiv relasjon (dct:description).
from_schema: https://data.norge.no/linkml/skos-ap-no
slot_uri: dct:description
domain_of:
- GeneriskRelasjon
- PartitivRelasjon
range: LangString
multivalued: true

```
</details>