

# Slot: eierskapshistorikk 


_Opphav og eigarskapshistorikk for ressursen._





URI: [dct:provenance](http://purl.org/dc/terms/provenance)
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
| Slot URI | [dct:provenance](http://purl.org/dc/terms/provenance) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| gyldige_verdier | dct:ProvenanceStatement |




### Schema Source


* from schema: https://data.norge.no/ap-no/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:provenance |
| native | https://data.norge.no/ap-no/dcat-ap-no/eierskapshistorikk |




## LinkML Source

<details>
```yaml
name: eierskapshistorikk
annotations:
  gyldige_verdier:
    tag: gyldige_verdier
    value: dct:ProvenanceStatement
description: Opphav og eigarskapshistorikk for ressursen.
from_schema: https://data.norge.no/ap-no/dcat-ap-no
rank: 1000
slot_uri: dct:provenance
domain_of:
- Datasett
range: string
multivalued: true

```
</details>