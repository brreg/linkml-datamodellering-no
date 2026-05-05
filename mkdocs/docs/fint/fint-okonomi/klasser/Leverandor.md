

# Slot: leverandor 



URI: [https://schema.fintlabs.no/okonomi/:leverandor](https://schema.fintlabs.no/okonomi/:leverandor)
Alias: leverandor

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Leverandorgruppe](leverandorgruppe.md) | Gruppering av leverandørar (Leverandørgruppe) |  no  |
| [Transaksjon](transaksjon.md) | Overføring av pengar til eller frå eksterne partar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Transaksjon](transaksjon.md), [Leverandorgruppe](leverandorgruppe.md) |

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