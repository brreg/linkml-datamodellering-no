

# Slot: eierskapshistorikk 


_Opphav og eigarskapshistorikk for ressursen. BØR brukast til å skildre kjeldetype (autoritativ/sjølvinnsamla eller avleidd/samanstilt frå andre kjelder), jf. Digdir sin veileder «Orden i eget hus», steg 5 — beskrive._





URI: [dct:provenance](http://purl.org/dc/terms/provenance)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør. |  yes  |






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
| vokabular_krav | bør |




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
  vokabular_krav:
    tag: vokabular_krav
    value: bør
description: Opphav og eigarskapshistorikk for ressursen. BØR brukast til å skildre
  kjeldetype (autoritativ/sjølvinnsamla eller avleidd/samanstilt frå andre kjelder),
  jf. Digdir sin veileder «Orden i eget hus», steg 5 — beskrive.
from_schema: https://data.norge.no/ap-no/dcat-ap-no
slot_uri: dct:provenance
domain_of:
- Datasett
range: string
multivalued: true

```
</details>