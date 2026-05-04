

# Slot: kontaktinformasjon 



URI: [https://schema.fintlabs.no/arkiv/:kontaktinformasjon](https://schema.fintlabs.no/arkiv/:kontaktinformasjon)
Alias: kontaktinformasjon

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Aktoer](Aktoer.md) | Abstrakt base for person eller eining vi samhandlar med |  no  |
| [Korrespondansepart](Korrespondansepart.md) | Verksemd eller person som arkivskapar mottek eller sender arkivdokument til |  no  |
| [Kontaktperson](Kontaktperson.md) | Kontaktperson (pårørande) til ein person |  no  |
| [Person](Person.md) | Fysiske private personar |  no  |
| [Virksomhet](Virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |
| [Enhet](Enhet.md) | Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd iden... |  no  |
| [Part](Part.md) | Part til Mappe, Registrering eller Dokumentbeskrivelse |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Korrespondansepart](Korrespondansepart.md), [Part](Part.md), [Aktoer](Aktoer.md), [Kontaktperson](Kontaktperson.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/arkiv/:kontaktinformasjon |
| native | https://schema.fintlabs.no/arkiv/:kontaktinformasjon |




## LinkML Source

<details>
```yaml
name: kontaktinformasjon
alias: kontaktinformasjon
domain_of:
- Korrespondansepart
- Part
- Aktoer
- Kontaktperson
range: string

```
</details>