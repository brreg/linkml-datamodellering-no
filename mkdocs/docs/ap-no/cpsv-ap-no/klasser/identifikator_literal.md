

# Slot: identifikator_literal 


_Tekstleg identifikator for ressursen (dct:identifier)._





URI: [dct:identifier](http://purl.org/dc/terms/identifier)
Alias: identifikator_literal

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Tjenestekanal](Tjenestekanal.md) | Ein kanal for å få tilgang til ei teneste (t |  yes  |
| [Regel](Regel.md) | Eit regelverk eller retningsliner som styrer levering av ei teneste |  yes  |
| [Hendelse](Hendelse.md) | Ei hending som kan utløyse behov for ei offentleg teneste |  yes  |
| [Gebyr](Gebyr.md) | Eit gebyr knytt til ei teneste |  yes  |
| [LovpalagtTjeneste](LovpalagtTjeneste.md) | Ei lovpålagd teneste som offentlege organ er pålagde å utføre |  yes  |
| [Aktor](Aktor.md) | Ein aktør (person eller organisasjon) relatert til ei teneste |  yes  |
| [RegulativRessurs](RegulativRessurs.md) | Ein regulativ ressurs (lov, forskrift o |  yes  |
| [OffentligTjeneste](OffentligTjeneste.md) | Ei konkret offentleg teneste levert av ein offentleg organisasjon |  yes  |
| [Katalog](Katalog.md) | Ein katalog over offentlege tenester og hendingar |  yes  |
| [Livshendelse](Livshendelse.md) | Ei livshending som kan utløyse behov for tenester (t |  no  |
| [OffentligOrganisasjon](OffentligOrganisasjon.md) | Ein offentleg organisasjon som er ansvarleg for ei teneste |  no  |
| [Virksomhetshendelse](Virksomhetshendelse.md) | Ei verksemdhending som kan utløyse behov for tenester (t |  no  |
| [Dokumentasjonstype](Dokumentasjonstype.md) | Ein type dokumentasjon som krevst for å levere ei teneste |  yes  |
| [Tjenesteresultattype](Tjenesteresultattype.md) | Typen resultat som ei teneste produserer |  yes  |
| [Tjeneste](Tjeneste.md) | Ei teneste levert av ein ikkje-offentleg aktør |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [LovpalagtTjeneste](LovpalagtTjeneste.md), [OffentligTjeneste](OffentligTjeneste.md), [Tjeneste](Tjeneste.md), [Hendelse](Hendelse.md), [Aktor](Aktor.md), [Tjenestekanal](Tjenestekanal.md), [Dokumentasjonstype](Dokumentasjonstype.md), [Tjenesteresultattype](Tjenesteresultattype.md), [Gebyr](Gebyr.md), [Regel](Regel.md), [RegulativRessurs](RegulativRessurs.md), [Katalog](Katalog.md) |
| Slot URI | [dct:identifier](http://purl.org/dc/terms/identifier) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/cpsv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:identifier |
| native | https://data.norge.no/linkml/cpsv-ap-no/identifikator_literal |




## LinkML Source

<details>
```yaml
name: identifikator_literal
description: Tekstleg identifikator for ressursen (dct:identifier).
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: dct:identifier
alias: identifikator_literal
domain_of:
- LovpalagtTjeneste
- OffentligTjeneste
- Tjeneste
- Hendelse
- Aktor
- Tjenestekanal
- Dokumentasjonstype
- Tjenesteresultattype
- Gebyr
- Regel
- RegulativRessurs
- Katalog
range: string

```
</details>