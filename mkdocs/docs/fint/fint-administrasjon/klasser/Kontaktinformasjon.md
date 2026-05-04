

# Slot: kontaktinformasjon 



URI: [https://schema.fintlabs.no/administrasjon/:kontaktinformasjon](https://schema.fintlabs.no/administrasjon/:kontaktinformasjon)
Alias: kontaktinformasjon

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Enhet](Enhet.md) | Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd iden... |  no  |
| [Arbeidslokasjon](Arbeidslokasjon.md) | Fysisk lokasjon der ein tilsett har sitt arbeidsstad |  no  |
| [Organisasjonselement](Organisasjonselement.md) | Eit element i organisasjonsstrukturen |  no  |
| [Kontaktperson](Kontaktperson.md) | Kontaktperson (pårørande) til ein person |  no  |
| [Personalressurs](Personalressurs.md) | Arbeidstakar eller oppdragstakar i organisasjonen |  no  |
| [Person](Person.md) | Fysiske private personar |  no  |
| [Aktoer](Aktoer.md) | Abstrakt base for person eller eining vi samhandlar med |  no  |
| [Virksomhet](Virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Arbeidslokasjon](Arbeidslokasjon.md), [Organisasjonselement](Organisasjonselement.md), [Personalressurs](Personalressurs.md), [Aktoer](Aktoer.md), [Kontaktperson](Kontaktperson.md) |

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