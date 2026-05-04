

# Slot: personalressurs 



URI: [https://schema.fintlabs.no/ressurs/:personalressurs](https://schema.fintlabs.no/ressurs/:personalressurs)
Alias: personalressurs

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Identitet](Identitet.md) | Identitet som identifiserer innehavaren av rettigheiter i organisasjonen |  no  |
| [Person](Person.md) | Fysiske private personar |  no  |
| [DigitalEnhet](DigitalEnhet.md) | Ei digital eining som t |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [DigitalEnhet](DigitalEnhet.md), [Identitet](Identitet.md), [Person](Person.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/ressurs/:personalressurs |
| native | https://schema.fintlabs.no/ressurs/:personalressurs |




## LinkML Source

<details>
```yaml
name: personalressurs
alias: personalressurs
domain_of:
- DigitalEnhet
- Identitet
- Person
range: string

```
</details>