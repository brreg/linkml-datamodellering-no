

# Slot: forfallsdato 



URI: [https://schema.fintlabs.no/okonomi/:forfallsdato](https://schema.fintlabs.no/okonomi/:forfallsdato)
Alias: forfallsdato

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Transaksjon](transaksjon.md) | Overføring av pengar til eller frå eksterne partar |  no  |
| [Faktura](faktura.md) | Betalingskrav utforma og oversendt frå fakturautstedar til fakturamottakar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Faktura](faktura.md), [Transaksjon](transaksjon.md) |

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