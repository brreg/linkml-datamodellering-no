

# Slot: adresse 



URI: [https://schema.fintlabs.no/arkiv/:adresse](https://schema.fintlabs.no/arkiv/:adresse)
Alias: adresse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Korrespondansepart](korrespondansepart.md) | Verksemd eller person som arkivskapar mottek eller sender arkivdokument til |  no  |
| [Matrikkelnummer](matrikkelnummer.md) | Eintydleg identifisering av matrikkeleining innanfor kommune |  no  |
| [Part](part.md) | Part til Mappe, Registrering eller Dokumentbeskrivelse |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Korrespondansepart](korrespondansepart.md), [Part](part.md), [Matrikkelnummer](matrikkelnummer.md) |

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