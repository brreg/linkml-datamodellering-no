

# Slot: elevforhold 



URI: [https://schema.fintlabs.no/utdanning/:elevforhold](https://schema.fintlabs.no/utdanning/:elevforhold)
Alias: elevforhold

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Eksamensgruppemedlemskap](eksamensgruppemedlemskap.md) | Eit elevs deltaking i ei eksamensgruppe |  no  |
| [Elevfravar](elevfravar.md) | Fråværsregistreringar for ein elev knytt til eit elevforhold |  no  |
| [Programomrademedlemskap](programomrademedlemskap.md) | Eit elevs tilknyting til eit programområde |  no  |
| [Elevvurdering](elevvurdering.md) | Samling av alle vurderingar for ein elev i eit elevforhold |  no  |
| [Fravarsoversikt](fravarsoversikt.md) | Oversikt over fråvær for ein elev i eit fag |  no  |
| [Persongruppemedlemskap](persongruppemedlemskap.md) | Eit elevs medlemskap i ei persongruppe |  no  |
| [Undervisningsgruppemedlemskap](undervisningsgruppemedlemskap.md) | Eit elevs medlemskap i ei undervisningsgruppe |  no  |
| [Kontaktlaerergruppemedlemskap](kontaktlaerergruppemedlemskap.md) | Eit elevs medlemskap i ei kontaktlærargruppe |  no  |
| [Klassemedlemskap](klassemedlemskap.md) | Eit elevs medlemskap i ei klasse |  no  |
| [Faggruppemedlemskap](faggruppemedlemskap.md) | Eit elevs medlemskap i ei faggruppe |  no  |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Klassemedlemskap](klassemedlemskap.md), [Kontaktlaerergruppemedlemskap](kontaktlaerergruppemedlemskap.md), [Persongruppemedlemskap](persongruppemedlemskap.md), [Programomrademedlemskap](programomrademedlemskap.md), [Faggruppemedlemskap](faggruppemedlemskap.md), [Undervisningsgruppemedlemskap](undervisningsgruppemedlemskap.md), [Eksamensgruppemedlemskap](eksamensgruppemedlemskap.md), [Elevfravar](elevfravar.md), [Elevvurdering](elevvurdering.md), [Fravarsoversikt](fravarsoversikt.md) |

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