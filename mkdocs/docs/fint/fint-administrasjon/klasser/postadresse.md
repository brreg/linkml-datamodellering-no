

# Slot: postadresse 



URI: [https://schema.fintlabs.no/administrasjon/:postadresse](https://schema.fintlabs.no/administrasjon/:postadresse)
Alias: postadresse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Enhet](Enhet.md) | Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd iden... |  no  |
| [Arbeidslokasjon](Arbeidslokasjon.md) | Fysisk lokasjon der ein tilsett har sitt arbeidsstad |  no  |
| [Organisasjonselement](Organisasjonselement.md) | Eit element i organisasjonsstrukturen |  no  |
| [Person](Person.md) | Fysiske private personar |  no  |
| [Aktoer](Aktoer.md) | Abstrakt base for person eller eining vi samhandlar med |  no  |
| [Virksomhet](Virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Arbeidslokasjon](Arbeidslokasjon.md), [Organisasjonselement](Organisasjonselement.md), [Aktoer](Aktoer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/administrasjon/:postadresse |
| native | https://schema.fintlabs.no/administrasjon/:postadresse |




## LinkML Source

<details>
```yaml
name: postadresse
alias: postadresse
domain_of:
- Arbeidslokasjon
- Organisasjonselement
- Aktoer
range: string

```
</details>