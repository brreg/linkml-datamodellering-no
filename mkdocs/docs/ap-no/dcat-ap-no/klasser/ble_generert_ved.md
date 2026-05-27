

# Slot: ble_generert_ved 


_Brukes til å referere til en aktivitet som genererte datasettet, eller som gir forretningskontekst for oppretting av det._





URI: [prov:wasGeneratedBy](http://www.w3.org/ns/prov#wasGeneratedBy)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain | [Datasett](datasett.md) |
| Domain Of | [Datasett](datasett.md) |
| Slot URI | [prov:wasGeneratedBy](http://www.w3.org/ns/prov#wasGeneratedBy) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| gyldige_verdier | URI til prov:Activity |




### Schema Source


* from schema: https://data.norge.no/ap-no/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | prov:wasGeneratedBy |
| native | https://data.norge.no/ap-no/dcat-ap-no/ble_generert_ved |




## LinkML Source

<details>
```yaml
name: ble_generert_ved
annotations:
  gyldige_verdier:
    tag: gyldige_verdier
    value: URI til prov:Activity
description: Brukes til å referere til en aktivitet som genererte datasettet, eller
  som gir forretningskontekst for oppretting av det.
from_schema: https://data.norge.no/ap-no/dcat-ap-no
rank: 1000
domain: Datasett
slot_uri: prov:wasGeneratedBy
domain_of:
- Datasett
range: uri
multivalued: true

```
</details>