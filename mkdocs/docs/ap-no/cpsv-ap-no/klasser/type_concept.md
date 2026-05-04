

# Slot: type_concept 


_Type ressurs frå eit kontrollert vokabular (dct:type)._





URI: [dct:type](http://purl.org/dc/terms/type)
Alias: type_concept

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Tjenestekanal](Tjenestekanal.md) | Ein kanal for å få tilgang til ei teneste (t |  yes  |
| [Regel](Regel.md) | Eit regelverk eller retningsliner som styrer levering av ei teneste |  yes  |
| [Hendelse](Hendelse.md) | Ei hending som kan utløyse behov for ei offentleg teneste |  yes  |
| [LovpalagtTjeneste](LovpalagtTjeneste.md) | Ei lovpålagd teneste som offentlege organ er pålagde å utføre |  yes  |
| [Tjeneste](Tjeneste.md) | Ei teneste levert av ein ikkje-offentleg aktør |  no  |
| [RegulativRessurs](RegulativRessurs.md) | Ein regulativ ressurs (lov, forskrift o |  yes  |
| [OffentligTjeneste](OffentligTjeneste.md) | Ei konkret offentleg teneste levert av ein offentleg organisasjon |  yes  |
| [Livshendelse](Livshendelse.md) | Ei livshending som kan utløyse behov for tenester (t |  no  |
| [Virksomhetshendelse](Virksomhetshendelse.md) | Ei verksemdhending som kan utløyse behov for tenester (t |  no  |
| [Tjenesteresultattype](Tjenesteresultattype.md) | Typen resultat som ei teneste produserer |  yes  |
| [OffentligOrganisasjon](OffentligOrganisasjon.md) | Ein offentleg organisasjon som er ansvarleg for ei teneste |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Konsept](Konsept.md) |
| Domain Of | [LovpalagtTjeneste](LovpalagtTjeneste.md), [OffentligTjeneste](OffentligTjeneste.md), [Tjeneste](Tjeneste.md), [Hendelse](Hendelse.md), [OffentligOrganisasjon](OffentligOrganisasjon.md), [Tjenestekanal](Tjenestekanal.md), [Tjenesteresultattype](Tjenesteresultattype.md), [Regel](Regel.md), [RegulativRessurs](RegulativRessurs.md) |
| Slot URI | [dct:type](http://purl.org/dc/terms/type) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/cpsv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:type |
| native | https://data.norge.no/linkml/cpsv-ap-no/type_concept |




## LinkML Source

<details>
```yaml
name: type_concept
description: Type ressurs frå eit kontrollert vokabular (dct:type).
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: dct:type
alias: type_concept
domain_of:
- LovpalagtTjeneste
- OffentligTjeneste
- Tjeneste
- Hendelse
- OffentligOrganisasjon
- Tjenestekanal
- Tjenesteresultattype
- Regel
- RegulativRessurs
range: Konsept

```
</details>