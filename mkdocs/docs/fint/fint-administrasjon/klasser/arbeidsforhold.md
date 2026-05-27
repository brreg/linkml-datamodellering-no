

# Slot: arbeidsforhold 


_Arbeidsforhold ressursen er knytt til._





URI: [adm:arbeidsforhold](https://schema.fintlabs.no/administrasjon/arbeidsforhold)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fastlonn](fastlonn.md) | Informasjon om fast lønnsbeordring |  yes  |
| [Fasttillegg](fasttillegg.md) | Faste tillegg til utbetaling |  yes  |
| [Variabellonn](variabellonn.md) | Informasjon om variabel lønn |  yes  |
| [Fravaer](fravaer.md) | Fråvær frå eit arbeidsforhold |  yes  |
| [Arbeidslokasjon](arbeidslokasjon.md) | Fysisk lokasjon der ein tilsett har sitt arbeidsstad |  yes  |
| [Organisasjonselement](organisasjonselement.md) | Eit element i organisasjonsstrukturen |  yes  |
| [Personalressurs](personalressurs.md) | Arbeidstakar eller oppdragstakar i organisasjonen |  yes  |
| [AdministrasjonContainer](administrasjoncontainer.md) | Rotcontainer for FINT Administrasjon-instansar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Arbeidsforhold](arbeidsforhold.md) |
| Domain Of | [AdministrasjonContainer](administrasjoncontainer.md), [Fastlonn](fastlonn.md), [Fasttillegg](fasttillegg.md), [Variabellonn](variabellonn.md), [Fravaer](fravaer.md), [Arbeidslokasjon](arbeidslokasjon.md), [Organisasjonselement](organisasjonselement.md), [Personalressurs](personalressurs.md) |
| Slot URI | [adm:arbeidsforhold](https://schema.fintlabs.no/administrasjon/arbeidsforhold) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:arbeidsforhold |
| native | https://schema.fintlabs.no/administrasjon/:arbeidsforhold |




## LinkML Source

<details>
```yaml
name: arbeidsforhold
description: Arbeidsforhold ressursen er knytt til.
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_uri: adm:arbeidsforhold
domain_of:
- AdministrasjonContainer
- Fastlonn
- Fasttillegg
- Variabellonn
- Fravaer
- Arbeidslokasjon
- Organisasjonselement
- Personalressurs
range: Arbeidsforhold

```
</details>