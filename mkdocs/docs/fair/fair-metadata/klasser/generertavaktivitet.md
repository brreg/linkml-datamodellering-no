

# Slot: generertAvAktivitet 


_Aktivitet som har generert ressursen (FAIR R1.2)._





URI: [prov:wasGeneratedBy](http://www.w3.org/ns/prov#wasGeneratedBy)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Proveniensmetadata](proveniensmetadata.md) | Metadata om opphav og endringshistorie (FAIR R1 |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain Of | [Proveniensmetadata](proveniensmetadata.md) |
| Slot URI | [prov:wasGeneratedBy](http://www.w3.org/ns/prov#wasGeneratedBy) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fair/fair-metadata




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | prov:wasGeneratedBy |
| native | https://data.norge.no/fair#:generertAvAktivitet |




## LinkML Source

<details>
```yaml
name: generertAvAktivitet
description: Aktivitet som har generert ressursen (FAIR R1.2).
from_schema: https://data.norge.no/fair/fair-metadata
rank: 1000
slot_uri: prov:wasGeneratedBy
domain_of:
- Proveniensmetadata
range: uriorcurie

```
</details>