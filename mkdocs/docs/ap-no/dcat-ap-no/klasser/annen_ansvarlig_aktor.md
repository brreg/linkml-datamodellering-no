

# Slot: annen_ansvarlig_aktor 


_Kvalifisert attributering til ansvarleg aktør._





URI: [prov:qualifiedAttribution](http://www.w3.org/ns/prov#qualifiedAttribution)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Datasett](datasett.md) |
| Slot URI | [prov:qualifiedAttribution](http://www.w3.org/ns/prov#qualifiedAttribution) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| gyldige_verdier | prov:Attribution |




### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | prov:qualifiedAttribution |
| native | https://data.norge.no/linkml/dcat-ap-no/annen_ansvarlig_aktor |




## LinkML Source

<details>
```yaml
name: annen_ansvarlig_aktor
annotations:
  gyldige_verdier:
    tag: gyldige_verdier
    value: prov:Attribution
description: Kvalifisert attributering til ansvarleg aktør.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: prov:qualifiedAttribution
domain_of:
- Datasett
range: string
multivalued: true

```
</details>