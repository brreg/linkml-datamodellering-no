

# Slot: kontaktinformasjon 



URI: [https://schema.fintlabs.no/administrasjon/:kontaktinformasjon](https://schema.fintlabs.no/administrasjon/:kontaktinformasjon)
Alias: kontaktinformasjon

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Aktoer](aktoer.md) | Abstrakt base for person eller eining vi samhandlar med |  no  |
| [Virksomhet](virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |
| [Personalressurs](personalressurs.md) | Arbeidstakar eller oppdragstakar i organisasjonen |  no  |
| [Arbeidslokasjon](arbeidslokasjon.md) | Fysisk lokasjon der ein tilsett har sitt arbeidsstad |  no  |
| [Person](person.md) | Fysiske private personar |  no  |
| [Enhet](enhet.md) | Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd iden... |  no  |
| [Kontaktperson](kontaktperson.md) | Kontaktperson (pårørande) til ein person |  no  |
| [Organisasjonselement](organisasjonselement.md) | Eit element i organisasjonsstrukturen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Arbeidslokasjon](arbeidslokasjon.md), [Organisasjonselement](organisasjonselement.md), [Personalressurs](personalressurs.md), [Aktoer](aktoer.md), [Kontaktperson](kontaktperson.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/administrasjon/:kontaktinformasjon |
| native | https://schema.fintlabs.no/administrasjon/:kontaktinformasjon |




## LinkML Source

<details>
```yaml
name: kontaktinformasjon
alias: kontaktinformasjon
domain_of:
- Arbeidslokasjon
- Organisasjonselement
- Personalressurs
- Aktoer
- Kontaktperson
range: string

```
</details>