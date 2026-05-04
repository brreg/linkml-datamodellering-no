

# Slot: elevforhold 



URI: [https://schema.fintlabs.no/utdanning/:elevforhold](https://schema.fintlabs.no/utdanning/:elevforhold)
Alias: elevforhold

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Faggruppemedlemskap](Faggruppemedlemskap.md) | Eit elevs medlemskap i ei faggruppe |  no  |
| [Fravarsoversikt](Fravarsoversikt.md) | Oversikt over fråvær for ein elev i eit fag |  no  |
| [Persongruppemedlemskap](Persongruppemedlemskap.md) | Eit elevs medlemskap i ei persongruppe |  no  |
| [Elevfravar](Elevfravar.md) | Fråværsregistreringar for ein elev knytt til eit elevforhold |  no  |
| [Kontaktlaerergruppemedlemskap](Kontaktlaerergruppemedlemskap.md) | Eit elevs medlemskap i ei kontaktlærargruppe |  no  |
| [Klassemedlemskap](Klassemedlemskap.md) | Eit elevs medlemskap i ei klasse |  no  |
| [UtdanningContainer](UtdanningContainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |
| [Elevvurdering](Elevvurdering.md) | Samling av alle vurderingar for ein elev i eit elevforhold |  no  |
| [Programomrademedlemskap](Programomrademedlemskap.md) | Eit elevs tilknyting til eit programområde |  no  |
| [Undervisningsgruppemedlemskap](Undervisningsgruppemedlemskap.md) | Eit elevs medlemskap i ei undervisningsgruppe |  no  |
| [Eksamensgruppemedlemskap](Eksamensgruppemedlemskap.md) | Eit elevs deltaking i ei eksamensgruppe |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [UtdanningContainer](UtdanningContainer.md), [Klassemedlemskap](Klassemedlemskap.md), [Kontaktlaerergruppemedlemskap](Kontaktlaerergruppemedlemskap.md), [Persongruppemedlemskap](Persongruppemedlemskap.md), [Programomrademedlemskap](Programomrademedlemskap.md), [Faggruppemedlemskap](Faggruppemedlemskap.md), [Undervisningsgruppemedlemskap](Undervisningsgruppemedlemskap.md), [Eksamensgruppemedlemskap](Eksamensgruppemedlemskap.md), [Elevfravar](Elevfravar.md), [Elevvurdering](Elevvurdering.md), [Fravarsoversikt](Fravarsoversikt.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:elevforhold |
| native | https://schema.fintlabs.no/utdanning/:elevforhold |




## LinkML Source

<details>
```yaml
name: elevforhold
alias: elevforhold
domain_of:
- UtdanningContainer
- Klassemedlemskap
- Kontaktlaerergruppemedlemskap
- Persongruppemedlemskap
- Programomrademedlemskap
- Faggruppemedlemskap
- Undervisningsgruppemedlemskap
- Eksamensgruppemedlemskap
- Elevfravar
- Elevvurdering
- Fravarsoversikt
range: string

```
</details>