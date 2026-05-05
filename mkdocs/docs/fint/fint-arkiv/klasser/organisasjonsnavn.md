

# Slot: organisasjonsnavn 



URI: [https://schema.fintlabs.no/arkiv/:organisasjonsnavn](https://schema.fintlabs.no/arkiv/:organisasjonsnavn)
Alias: organisasjonsnavn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Virksomhet](virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |
| [Enhet](enhet.md) | Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd iden... |  no  |
| [SoeknadDrosjeloeyve](soeknaddrosjeloeyve.md) | Sak om søknad om løyve til å køyre drosje |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [SoeknadDrosjeloeyve](soeknaddrosjeloeyve.md), [Enhet](enhet.md) |

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