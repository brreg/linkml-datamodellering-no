

# Slot: standardoverensstemming 


_Standardar eller profilar ressursen følgjer, t.d. DCAT-AP-NO eller ISO 19115 (FAIR R1.3 / I3)._

__





URI: [dct:conformsTo](http://purl.org/dc/terms/conformsTo)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Gjenbruksmetadata](gjenbruksmetadata.md) | Metadata som støttar gjenbruk av ressursen (FAIR R1 |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain Of | [Gjenbruksmetadata](gjenbruksmetadata.md) |
| Slot URI | [dct:conformsTo](http://purl.org/dc/terms/conformsTo) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fair/fair-metadata




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:conformsTo |
| native | https://data.norge.no/fair#:standardoverensstemming |




## LinkML Source

<details>
```yaml
name: standardoverensstemming
description: 'Standardar eller profilar ressursen følgjer, t.d. DCAT-AP-NO eller ISO
  19115 (FAIR R1.3 / I3).

  '
from_schema: https://data.norge.no/fair/fair-metadata
rank: 1000
slot_uri: dct:conformsTo
domain_of:
- Gjenbruksmetadata
range: uriorcurie
multivalued: true

```
</details>