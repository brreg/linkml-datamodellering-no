

# Slot: gruppemedlemskap 


_Gruppemedlemskap._





URI: [utd:gruppemedlemskap](https://schema.fintlabs.no/utdanning/gruppemedlemskap)
Alias: gruppemedlemskap

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Undervisningsgruppe](undervisningsgruppe.md) | Ei gruppe elevar som følgjer same undervisning i eit eller fleire fag |  yes  |
| [Programomrade](programomrade.md) | Eit programområde innanfor eit utdanningsprogram (t |  yes  |
| [Kontaktlaerergruppe](kontaktlaerergruppe.md) | Gruppe av elevar med felles kontaktlærar |  yes  |
| [Eksamensgruppe](eksamensgruppe.md) | Ei gruppe elevar som avlegg same eksamen |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Gruppemedlemskap](gruppemedlemskap.md) |
| Domain Of | [Kontaktlaerergruppe](kontaktlaerergruppe.md), [Programomrade](programomrade.md), [Undervisningsgruppe](undervisningsgruppe.md), [Eksamensgruppe](eksamensgruppe.md) |
| Slot URI | [utd:gruppemedlemskap](https://schema.fintlabs.no/utdanning/gruppemedlemskap) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:gruppemedlemskap |
| native | https://schema.fintlabs.no/utdanning/:gruppemedlemskap |




## LinkML Source

<details>
```yaml
name: gruppemedlemskap
description: Gruppemedlemskap.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:gruppemedlemskap
alias: gruppemedlemskap
domain_of:
- Kontaktlaerergruppe
- Programomrade
- Undervisningsgruppe
- Eksamensgruppe
range: Gruppemedlemskap
multivalued: true

```
</details>