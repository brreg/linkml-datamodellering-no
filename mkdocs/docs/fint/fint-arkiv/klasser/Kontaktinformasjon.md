

# Slot: kontaktinformasjon 



URI: [https://schema.fintlabs.no/arkiv/:kontaktinformasjon](https://schema.fintlabs.no/arkiv/:kontaktinformasjon)
Alias: kontaktinformasjon

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontaktperson](kontaktperson.md) | Kontaktperson (pårørande) til ein person |  no  |
| [Korrespondansepart](korrespondansepart.md) | Verksemd eller person som arkivskapar mottek eller sender arkivdokument til |  no  |
| [Enhet](enhet.md) | Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd iden... |  no  |
| [Aktoer](aktoer.md) | Abstrakt base for person eller eining vi samhandlar med |  no  |
| [Virksomhet](virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |
| [Part](part.md) | Part til Mappe, Registrering eller Dokumentbeskrivelse |  no  |
| [Person](person.md) | Fysiske private personar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Korrespondansepart](korrespondansepart.md), [Part](part.md), [Aktoer](aktoer.md), [Kontaktperson](kontaktperson.md) |

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