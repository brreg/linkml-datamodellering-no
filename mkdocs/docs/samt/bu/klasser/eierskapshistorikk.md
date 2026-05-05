

# Slot: eierskapshistorikk 


_Opphav og eigarskapshistorikk for ressursen._





URI: [dct:provenance](http://purl.org/dc/terms/provenance)
Alias: eierskapshistorikk

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ProvenanceStatement](provenancestatement.md) |
| Domain Of | [Datasett](datasett.md) |
| Slot URI | [dct:provenance](http://purl.org/dc/terms/provenance) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:provenance |
| native | samtbuskole:eierskapshistorikk |




## LinkML Source

<details>
```yaml
name: eierskapshistorikk
description: Opphav og eigarskapshistorikk for ressursen.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
slot_uri: dct:provenance
alias: eierskapshistorikk
domain_of:
- Datasett
range: ProvenanceStatement
multivalued: true

```
</details>