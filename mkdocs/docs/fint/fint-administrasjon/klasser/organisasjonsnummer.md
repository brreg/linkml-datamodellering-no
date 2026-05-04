

# Slot: organisasjonsnummer 



URI: [https://schema.fintlabs.no/administrasjon/:organisasjonsnummer](https://schema.fintlabs.no/administrasjon/:organisasjonsnummer)
Alias: organisasjonsnummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Organisasjonselement](Organisasjonselement.md) | Eit element i organisasjonsstrukturen |  no  |
| [Enhet](Enhet.md) | Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd iden... |  no  |
| [Arbeidslokasjon](Arbeidslokasjon.md) | Fysisk lokasjon der ein tilsett har sitt arbeidsstad |  no  |
| [Virksomhet](Virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Arbeidslokasjon](Arbeidslokasjon.md), [Organisasjonselement](Organisasjonselement.md), [Enhet](Enhet.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/administrasjon/:organisasjonsnummer |
| native | https://schema.fintlabs.no/administrasjon/:organisasjonsnummer |




## LinkML Source

<details>
```yaml
name: organisasjonsnummer
alias: organisasjonsnummer
domain_of:
- Arbeidslokasjon
- Organisasjonselement
- Enhet
range: string

```
</details>