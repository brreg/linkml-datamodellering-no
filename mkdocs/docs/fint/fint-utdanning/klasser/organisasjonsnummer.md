

# Slot: organisasjonsnummer 



URI: [https://schema.fintlabs.no/utdanning/:organisasjonsnummer](https://schema.fintlabs.no/utdanning/:organisasjonsnummer)
Alias: organisasjonsnummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Virksomhet](virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |
| [Enhet](enhet.md) | Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd iden... |  no  |
| [Skole](skole.md) | Ein skule eller opplæringsinstitusjon |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Skole](skole.md), [Enhet](enhet.md) |

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