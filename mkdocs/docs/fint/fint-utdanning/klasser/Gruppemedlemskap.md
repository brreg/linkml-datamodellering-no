

# Slot: gruppemedlemskap 



URI: [https://schema.fintlabs.no/utdanning/:gruppemedlemskap](https://schema.fintlabs.no/utdanning/:gruppemedlemskap)
Alias: gruppemedlemskap

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Undervisningsgruppe](Undervisningsgruppe.md) | Ei gruppe elevar som følgjer same undervisning i eit eller fleire fag |  no  |
| [Eksamensgruppe](Eksamensgruppe.md) | Ei gruppe elevar som avlegg same eksamen |  no  |
| [Programomrade](Programomrade.md) | Eit programområde innanfor eit utdanningsprogram (t |  no  |
| [Kontaktlaerergruppe](Kontaktlaerergruppe.md) | Gruppe av elevar med felles kontaktlærar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Kontaktlaerergruppe](Kontaktlaerergruppe.md), [Programomrade](Programomrade.md), [Undervisningsgruppe](Undervisningsgruppe.md), [Eksamensgruppe](Eksamensgruppe.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:gruppemedlemskap |
| native | https://schema.fintlabs.no/utdanning/:gruppemedlemskap |




## LinkML Source

<details>
```yaml
name: gruppemedlemskap
alias: gruppemedlemskap
domain_of:
- Kontaktlaerergruppe
- Programomrade
- Undervisningsgruppe
- Eksamensgruppe
range: string

```
</details>