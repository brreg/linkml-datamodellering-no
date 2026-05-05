

# Slot: kommune 



URI: [https://schema.fintlabs.no/utdanning/:kommune](https://schema.fintlabs.no/utdanning/:kommune)
Alias: kommune

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](person.md) | Fysiske private personar |  no  |
| [OtEnhet](otenhet.md) | Eining i oppfølgingstenesta (OT) |  no  |
| [Fylke](fylke.md) | Liste over Norges fylker |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [OtEnhet](otenhet.md), [Fylke](fylke.md), [Person](person.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:kommune |
| native | https://schema.fintlabs.no/utdanning/:kommune |




## LinkML Source

<details>
```yaml
name: kommune
alias: kommune
domain_of:
- OtEnhet
- Fylke
- Person
range: string

```
</details>