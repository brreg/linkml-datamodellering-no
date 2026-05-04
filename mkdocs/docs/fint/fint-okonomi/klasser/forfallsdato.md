

# Slot: forfallsdato 



URI: [https://schema.fintlabs.no/okonomi/:forfallsdato](https://schema.fintlabs.no/okonomi/:forfallsdato)
Alias: forfallsdato

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Transaksjon](Transaksjon.md) | Overføring av pengar til eller frå eksterne partar |  no  |
| [Faktura](Faktura.md) | Betalingskrav utforma og oversendt frå fakturautstedar til fakturamottakar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Faktura](Faktura.md), [Transaksjon](Transaksjon.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/okonomi/:forfallsdato |
| native | https://schema.fintlabs.no/okonomi/:forfallsdato |




## LinkML Source

<details>
```yaml
name: forfallsdato
alias: forfallsdato
domain_of:
- Faktura
- Transaksjon
range: string

```
</details>