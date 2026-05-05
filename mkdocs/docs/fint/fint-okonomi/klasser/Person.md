

# Slot: person 



URI: [https://schema.fintlabs.no/okonomi/:person](https://schema.fintlabs.no/okonomi/:person)
Alias: person

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fakturamottaker](fakturamottaker.md) | Aktør som skal betale faktura (kompleks datatype) |  no  |
| [Leverandor](leverandor.md) | Person eller verksemd som leverer produkt eller tenester (Leverandør) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Fakturamottaker](fakturamottaker.md), [Leverandor](leverandor.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/okonomi/:person |
| native | https://schema.fintlabs.no/okonomi/:person |




## LinkML Source

<details>
```yaml
name: person
alias: person
domain_of:
- Fakturamottaker
- Leverandor
range: string

```
</details>