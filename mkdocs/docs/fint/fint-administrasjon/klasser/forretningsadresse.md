

# Slot: forretningsadresse 



URI: [https://schema.fintlabs.no/administrasjon/:forretningsadresse](https://schema.fintlabs.no/administrasjon/:forretningsadresse)
Alias: forretningsadresse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Virksomhet](virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |
| [Enhet](enhet.md) | Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd iden... |  no  |
| [Organisasjonselement](organisasjonselement.md) | Eit element i organisasjonsstrukturen |  no  |
| [Arbeidslokasjon](arbeidslokasjon.md) | Fysisk lokasjon der ein tilsett har sitt arbeidsstad |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Arbeidslokasjon](arbeidslokasjon.md), [Organisasjonselement](organisasjonselement.md), [Enhet](enhet.md) |

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