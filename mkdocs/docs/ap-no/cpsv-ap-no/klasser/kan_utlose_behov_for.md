

# Slot: kan_utlose_behov_for 


_Tenester det kan oppstå behov for som følgje av hendinga._





URI: [cpsvno:mayTriggerNeedFor](https://data.norge.no/vocabulary/cpsvno#mayTriggerNeedFor)
Alias: kan_utlose_behov_for

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Virksomhetshendelse](virksomhetshendelse.md) | Ei verksemdhending som kan utløyse behov for tenester (t |  yes  |
| [Livshendelse](livshendelse.md) | Ei livshending som kan utløyse behov for tenester (t |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain Of | [Livshendelse](livshendelse.md), [Virksomhetshendelse](virksomhetshendelse.md) |
| Slot URI | [cpsvno:mayTriggerNeedFor](https://data.norge.no/vocabulary/cpsvno#mayTriggerNeedFor) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/cpsv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cpsvno:mayTriggerNeedFor |
| native | https://data.norge.no/linkml/cpsv-ap-no/kan_utlose_behov_for |




## LinkML Source

<details>
```yaml
name: kan_utlose_behov_for
description: Tenester det kan oppstå behov for som følgje av hendinga.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: cpsvno:mayTriggerNeedFor
alias: kan_utlose_behov_for
domain_of:
- Livshendelse
- Virksomhetshendelse
range: uriorcurie
multivalued: true

```
</details>