

# Slot: kontaktinformasjon 



URI: [https://schema.fintlabs.no/okonomi/:kontaktinformasjon](https://schema.fintlabs.no/okonomi/:kontaktinformasjon)
Alias: kontaktinformasjon

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Enhet](enhet.md) | Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd iden... |  no  |
| [Aktoer](aktoer.md) | Abstrakt base for person eller eining vi samhandlar med |  no  |
| [Person](person.md) | Fysiske private personar |  no  |
| [Virksomhet](virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |
| [Kontaktperson](kontaktperson.md) | Kontaktperson (pårørande) til ein person |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Aktoer](aktoer.md), [Kontaktperson](kontaktperson.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/okonomi/:kontaktinformasjon |
| native | https://schema.fintlabs.no/okonomi/:kontaktinformasjon |




## LinkML Source

<details>
```yaml
name: kontaktinformasjon
alias: kontaktinformasjon
domain_of:
- Aktoer
- Kontaktperson
range: string

```
</details>