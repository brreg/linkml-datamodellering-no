

# Slot: gruppemedlemskap 



URI: [https://schema.fintlabs.no/utdanning/:gruppemedlemskap](https://schema.fintlabs.no/utdanning/:gruppemedlemskap)
Alias: gruppemedlemskap

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontaktlaerergruppe](kontaktlaerergruppe.md) | Gruppe av elevar med felles kontaktlærar |  no  |
| [Programomrade](programomrade.md) | Eit programområde innanfor eit utdanningsprogram (t |  no  |
| [Undervisningsgruppe](undervisningsgruppe.md) | Ei gruppe elevar som følgjer same undervisning i eit eller fleire fag |  no  |
| [Eksamensgruppe](eksamensgruppe.md) | Ei gruppe elevar som avlegg same eksamen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Kontaktlaerergruppe](kontaktlaerergruppe.md), [Programomrade](programomrade.md), [Undervisningsgruppe](undervisningsgruppe.md), [Eksamensgruppe](eksamensgruppe.md) |

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