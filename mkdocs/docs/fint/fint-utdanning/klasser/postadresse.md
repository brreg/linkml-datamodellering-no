

# Slot: postadresse 



URI: [https://schema.fintlabs.no/utdanning/:postadresse](https://schema.fintlabs.no/utdanning/:postadresse)
Alias: postadresse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Aktoer](aktoer.md) | Abstrakt base for person eller eining vi samhandlar med |  no  |
| [Virksomhet](virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |
| [Skole](skole.md) | Ein skule eller opplæringsinstitusjon |  no  |
| [Enhet](enhet.md) | Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd iden... |  no  |
| [Person](person.md) | Fysiske private personar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Skole](skole.md), [Aktoer](aktoer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:postadresse |
| native | https://schema.fintlabs.no/utdanning/:postadresse |




## LinkML Source

<details>
```yaml
name: postadresse
alias: postadresse
domain_of:
- Skole
- Aktoer
range: string

```
</details>