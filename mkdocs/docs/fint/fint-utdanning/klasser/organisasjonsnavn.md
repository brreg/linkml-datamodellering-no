

# Slot: organisasjonsnavn 



URI: [https://schema.fintlabs.no/utdanning/:organisasjonsnavn](https://schema.fintlabs.no/utdanning/:organisasjonsnavn)
Alias: organisasjonsnavn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Enhet](Enhet.md) | Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd iden... |  no  |
| [Virksomhet](Virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |
| [Skole](Skole.md) | Ein skule eller opplæringsinstitusjon |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Skole](Skole.md), [Enhet](Enhet.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:organisasjonsnavn |
| native | https://schema.fintlabs.no/utdanning/:organisasjonsnavn |




## LinkML Source

<details>
```yaml
name: organisasjonsnavn
alias: organisasjonsnavn
domain_of:
- Skole
- Enhet
range: string

```
</details>