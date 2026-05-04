

# Slot: forretningsadresse 



URI: [https://schema.fintlabs.no/administrasjon/:forretningsadresse](https://schema.fintlabs.no/administrasjon/:forretningsadresse)
Alias: forretningsadresse

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
| self | https://schema.fintlabs.no/administrasjon/:forretningsadresse |
| native | https://schema.fintlabs.no/administrasjon/:forretningsadresse |




## LinkML Source

<details>
```yaml
name: forretningsadresse
alias: forretningsadresse
domain_of:
- Arbeidslokasjon
- Organisasjonselement
- Enhet
range: string

```
</details>