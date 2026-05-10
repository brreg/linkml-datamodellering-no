

# Slot: kan_utlose 


_Offentlege tenester hendinga kan utløyse._





URI: [cpsvno:mayTrigger](https://data.norge.no/vocabulary/cpsvno#mayTrigger)
Alias: kan_utlose

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Livshendelse](livshendelse.md) | Ei livshending som kan utløyse behov for tenester (t |  no  |
| [Virksomhetshendelse](virksomhetshendelse.md) | Ei verksemdhending som kan utløyse behov for tenester (t |  no  |
| [Hendelse](hendelse.md) | Ei hending som kan utløyse behov for ei offentleg teneste |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [OffentligTjeneste](offentligtjeneste.md) |
| Domain Of | [Hendelse](hendelse.md) |
| Slot URI | [cpsvno:mayTrigger](https://data.norge.no/vocabulary/cpsvno#mayTrigger) |

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
| self | cpsvno:mayTrigger |
| native | https://data.norge.no/linkml/cpsv-ap-no/kan_utlose |




## LinkML Source

<details>
```yaml
name: kan_utlose
description: Offentlege tenester hendinga kan utløyse.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: cpsvno:mayTrigger
alias: kan_utlose
domain_of:
- Hendelse
range: OffentligTjeneste
multivalued: true

```
</details>