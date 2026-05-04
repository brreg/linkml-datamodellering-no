

# Slot: til_omgrep 


_Til-omgrepet i den assosiative relasjonen (skosno:hasToConcept)._





URI: [skosno:hasToConcept](https://data.norge.no/vocabulary/skosno#hasToConcept)
Alias: til_omgrep

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AssosiativRelasjon](AssosiativRelasjon.md) | Ein assosiativ relasjon mellom to omgrep |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Begrep](Begrep.md) |
| Domain Of | [AssosiativRelasjon](AssosiativRelasjon.md) |
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
rank: 1000
slot_uri: skosno:hasToConcept
alias: til_omgrep
domain_of:
- AssosiativRelasjon
range: Begrep
multivalued: true

```
</details>