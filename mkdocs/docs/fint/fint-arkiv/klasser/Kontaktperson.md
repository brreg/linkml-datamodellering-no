

# Slot: kontaktperson 



URI: [https://schema.fintlabs.no/arkiv/:kontaktperson](https://schema.fintlabs.no/arkiv/:kontaktperson)
Alias: kontaktperson

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Part](Part.md) | Part til Mappe, Registrering eller Dokumentbeskrivelse |  no  |
| [Korrespondansepart](Korrespondansepart.md) | Verksemd eller person som arkivskapar mottek eller sender arkivdokument til |  no  |
| [Kontaktperson](Kontaktperson.md) | Kontaktperson (pårørande) til ein person |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Korrespondansepart](Korrespondansepart.md), [Part](Part.md), [Kontaktperson](Kontaktperson.md) |

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