

# Slot: adresse 


_Adresse til matrikkeleining._





URI: [fint:adresse](https://schema.fintlabs.no/adresse)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Matrikkelnummer](matrikkelnummer.md) | Eintydleg identifisering av matrikkeleining innanfor kommune |  no  |
| [Korrespondansepart](korrespondansepart.md) | Verksemd eller person som arkivskapar mottek eller sender arkivdokument til |  yes  |
| [Part](part.md) | Part til Mappe, Registrering eller Dokumentbeskrivelse |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Adresse](adresse.md) |
| Domain Of | [Matrikkelnummer](matrikkelnummer.md), [Korrespondansepart](korrespondansepart.md), [Part](part.md) |
| Slot URI | [fint:adresse](https://schema.fintlabs.no/adresse) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:adresse |
| native | https://schema.fintlabs.no/:adresse |




## LinkML Source

<details>
```yaml
name: adresse
description: Adresse til matrikkeleining.
from_schema: https://data.norge.no/fint/fint-common
slot_uri: fint:adresse
domain_of:
- Matrikkelnummer
- Korrespondansepart
- Part
range: Adresse
inlined: true

```
</details>