

# Slot: foretrekt_namn 


_Føretrekt namn/term for organisasjonen._





URI: [skos:prefLabel](http://www.w3.org/2004/02/skos/core#prefLabel)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OffentligOrganisasjon](offentligorganisasjon.md) | Ein offentleg organisasjon som er ansvarleg for ei teneste |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LangString](langstring.md) |
| Domain Of | [OffentligOrganisasjon](offentligorganisasjon.md) |
| Slot URI | [skos:prefLabel](http://www.w3.org/2004/02/skos/core#prefLabel) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/cpsv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | skos:prefLabel |
| native | https://data.norge.no/ap-no/cpsv-ap-no/foretrekt_namn |




## LinkML Source

<details>
```yaml
name: foretrekt_namn
description: Føretrekt namn/term for organisasjonen.
from_schema: https://data.norge.no/ap-no/cpsv-ap-no
rank: 1000
slot_uri: skos:prefLabel
domain_of:
- OffentligOrganisasjon
range: LangString
multivalued: true

```
</details>