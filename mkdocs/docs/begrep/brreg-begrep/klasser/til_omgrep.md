

# Slot: til_omgrep 


_Til-omgrepet i den assosiative relasjonen (skosno:hasToConcept)._





URI: [skosno:hasToConcept](https://data.norge.no/vocabulary/skosno#hasToConcept)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AssosiativRelasjon](assosiativrelasjon.md) | Ein assosiativ relasjon mellom to omgrep |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Begrep](begrep.md) |
| Domain Of | [AssosiativRelasjon](assosiativrelasjon.md) |
| Slot URI | [skosno:hasToConcept](https://data.norge.no/vocabulary/skosno#hasToConcept) |

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
| self | skosno:hasToConcept |
| native | https://data.norge.no/linkml/skos-ap-no/til_omgrep |




## LinkML Source

<details>
```yaml
name: til_omgrep
description: Til-omgrepet i den assosiative relasjonen (skosno:hasToConcept).
from_schema: https://data.norge.no/linkml/skos-ap-no
slot_uri: skosno:hasToConcept
domain_of:
- AssosiativRelasjon
range: Begrep
multivalued: true

```
</details>