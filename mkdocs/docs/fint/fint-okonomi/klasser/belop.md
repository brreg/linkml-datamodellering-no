

# Slot: belop 



URI: [https://schema.fintlabs.no/okonomi/:belop](https://schema.fintlabs.no/okonomi/:belop)
Alias: belop

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Postering](Postering.md) | Føring på ein konto i rekneskapet |  no  |
| [Transaksjon](Transaksjon.md) | Overføring av pengar til eller frå eksterne partar |  no  |
| [Faktura](Faktura.md) | Betalingskrav utforma og oversendt frå fakturautstedar til fakturamottakar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Faktura](Faktura.md), [Transaksjon](Transaksjon.md), [Postering](Postering.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/okonomi/:belop |
| native | https://schema.fintlabs.no/okonomi/:belop |




## LinkML Source

<details>
```yaml
name: belop
alias: belop
domain_of:
- Faktura
- Transaksjon
- Postering
range: string

```
</details>