

# Slot: elevforhold 


_Elevforholdet dette gjeld._





URI: [utd:elevforhold](https://schema.fintlabs.no/utdanning/elevforhold)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Klassemedlemskap](klassemedlemskap.md) | Eit elevs medlemskap i ei klasse |  yes  |
| [Kontaktlaerergruppemedlemskap](kontaktlaerergruppemedlemskap.md) | Eit elevs medlemskap i ei kontaktlærargruppe |  yes  |
| [Persongruppemedlemskap](persongruppemedlemskap.md) | Eit elevs medlemskap i ei persongruppe |  yes  |
| [Programomrademedlemskap](programomrademedlemskap.md) | Eit elevs tilknyting til eit programområde |  yes  |
| [Faggruppemedlemskap](faggruppemedlemskap.md) | Eit elevs medlemskap i ei faggruppe |  yes  |
| [Undervisningsgruppemedlemskap](undervisningsgruppemedlemskap.md) | Eit elevs medlemskap i ei undervisningsgruppe |  yes  |
| [Eksamensgruppemedlemskap](eksamensgruppemedlemskap.md) | Eit elevs deltaking i ei eksamensgruppe |  yes  |
| [Elevfravar](elevfravar.md) | Fråværsregistreringar for ein elev knytt til eit elevforhold |  yes  |
| [Elevvurdering](elevvurdering.md) | Samling av alle vurderingar for ein elev i eit elevforhold |  yes  |
| [Fravarsoversikt](fravarsoversikt.md) | Oversikt over fråvær for ein elev i eit fag |  yes  |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Elevforhold](elevforhold.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Klassemedlemskap](klassemedlemskap.md), [Kontaktlaerergruppemedlemskap](kontaktlaerergruppemedlemskap.md), [Persongruppemedlemskap](persongruppemedlemskap.md), [Programomrademedlemskap](programomrademedlemskap.md), [Faggruppemedlemskap](faggruppemedlemskap.md), [Undervisningsgruppemedlemskap](undervisningsgruppemedlemskap.md), [Eksamensgruppemedlemskap](eksamensgruppemedlemskap.md), [Elevfravar](elevfravar.md), [Elevvurdering](elevvurdering.md), [Fravarsoversikt](fravarsoversikt.md) |
| Slot URI | [utd:elevforhold](https://schema.fintlabs.no/utdanning/elevforhold) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:elevforhold |
| native | https://schema.fintlabs.no/utdanning/:elevforhold |




## LinkML Source

<details>
```yaml
name: elevforhold
description: Elevforholdet dette gjeld.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:elevforhold
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
range: Elevforhold

```
</details>