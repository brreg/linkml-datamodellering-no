

# Slot: organisasjonsnummer 



URI: [https://schema.fintlabs.no/utdanning/:organisasjonsnummer](https://schema.fintlabs.no/utdanning/:organisasjonsnummer)
Alias: organisasjonsnummer

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
| self | https://schema.fintlabs.no/utdanning/:organisasjonsnummer |
| native | https://schema.fintlabs.no/utdanning/:organisasjonsnummer |




## LinkML Source

<details>
```yaml
name: organisasjonsnummer
alias: organisasjonsnummer
domain_of:
- Skole
- Enhet
range: string

```
</details>