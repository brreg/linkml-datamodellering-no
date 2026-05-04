

# Slot: leverandor 



URI: [https://schema.fintlabs.no/okonomi/:leverandor](https://schema.fintlabs.no/okonomi/:leverandor)
Alias: leverandor

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Leverandorgruppe](Leverandorgruppe.md) | Gruppering av leverandørar (Leverandørgruppe) |  no  |
| [Transaksjon](Transaksjon.md) | Overføring av pengar til eller frå eksterne partar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Transaksjon](Transaksjon.md), [Leverandorgruppe](Leverandorgruppe.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/okonomi/:leverandor |
| native | https://schema.fintlabs.no/okonomi/:leverandor |




## LinkML Source

<details>
```yaml
name: leverandor
alias: leverandor
domain_of:
- Transaksjon
- Leverandorgruppe
range: string

```
</details>