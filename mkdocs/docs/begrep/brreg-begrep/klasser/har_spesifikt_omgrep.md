

# Slot: har_spesifikt_omgrep 


_Underomgrepet i ein generisk relasjon (skosno:hasSpecificConcept)._





URI: [skosno:hasSpecificConcept](https://data.norge.no/vocabulary/skosno#hasSpecificConcept)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeneriskRelasjon](generiskrelasjon.md) | Ein generisk relasjon mellom eit overomgrep og eit underomgrep |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Begrep](begrep.md) |
| Domain Of | [GeneriskRelasjon](generiskrelasjon.md) |
| Slot URI | [skosno:hasSpecificConcept](https://data.norge.no/vocabulary/skosno#hasSpecificConcept) |

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
| self | skosno:hasSpecificConcept |
| native | https://data.norge.no/linkml/skos-ap-no/har_spesifikt_omgrep |




## LinkML Source

<details>
```yaml
name: har_spesifikt_omgrep
description: Underomgrepet i ein generisk relasjon (skosno:hasSpecificConcept).
from_schema: https://data.norge.no/linkml/skos-ap-no
slot_uri: skosno:hasSpecificConcept
domain_of:
- GeneriskRelasjon
range: Begrep
multivalued: true

```
</details>