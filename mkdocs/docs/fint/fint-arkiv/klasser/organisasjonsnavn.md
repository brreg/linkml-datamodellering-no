

# Slot: organisasjonsnavn 



URI: [https://schema.fintlabs.no/arkiv/:organisasjonsnavn](https://schema.fintlabs.no/arkiv/:organisasjonsnavn)
Alias: organisasjonsnavn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Virksomhet](Virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |
| [SoeknadDrosjeloeyve](SoeknadDrosjeloeyve.md) | Sak om søknad om løyve til å køyre drosje |  no  |
| [Enhet](Enhet.md) | Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd iden... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [SoeknadDrosjeloeyve](SoeknadDrosjeloeyve.md), [Enhet](Enhet.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/arkiv/:organisasjonsnavn |
| native | https://schema.fintlabs.no/arkiv/:organisasjonsnavn |




## LinkML Source

<details>
```yaml
name: organisasjonsnavn
alias: organisasjonsnavn
domain_of:
- SoeknadDrosjeloeyve
- Enhet
range: string

```
</details>