

# Slot: kontaktperson 



URI: [https://schema.fintlabs.no/arkiv/:kontaktperson](https://schema.fintlabs.no/arkiv/:kontaktperson)
Alias: kontaktperson

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Korrespondansepart](korrespondansepart.md) | Verksemd eller person som arkivskapar mottek eller sender arkivdokument til |  no  |
| [Kontaktperson](kontaktperson.md) | Kontaktperson (pårørande) til ein person |  no  |
| [Part](part.md) | Part til Mappe, Registrering eller Dokumentbeskrivelse |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Korrespondansepart](korrespondansepart.md), [Part](part.md), [Kontaktperson](kontaktperson.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/arkiv/:kontaktperson |
| native | https://schema.fintlabs.no/arkiv/:kontaktperson |




## LinkML Source

<details>
```yaml
name: kontaktperson
alias: kontaktperson
domain_of:
- Korrespondansepart
- Part
- Kontaktperson
range: string

```
</details>