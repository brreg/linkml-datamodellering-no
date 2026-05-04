

# Slot: adresse 



URI: [https://schema.fintlabs.no/arkiv/:adresse](https://schema.fintlabs.no/arkiv/:adresse)
Alias: adresse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Matrikkelnummer](Matrikkelnummer.md) | Eintydleg identifisering av matrikkeleining innanfor kommune |  no  |
| [Part](Part.md) | Part til Mappe, Registrering eller Dokumentbeskrivelse |  no  |
| [Korrespondansepart](Korrespondansepart.md) | Verksemd eller person som arkivskapar mottek eller sender arkivdokument til |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Korrespondansepart](Korrespondansepart.md), [Part](Part.md), [Matrikkelnummer](Matrikkelnummer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/arkiv/:adresse |
| native | https://schema.fintlabs.no/arkiv/:adresse |




## LinkML Source

<details>
```yaml
name: adresse
alias: adresse
domain_of:
- Korrespondansepart
- Part
- Matrikkelnummer
range: string

```
</details>