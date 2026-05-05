

# Slot: identifikator_literal 


_Tekstleg identifikator for ressursen (dct:identifier)._





URI: [dct:identifier](http://purl.org/dc/terms/identifier)
Alias: identifikator_literal

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Livshendelse](livshendelse.md) | Ei livshending som kan utløyse behov for tenester (t |  no  |
| [Katalog](katalog.md) | Ein katalog over offentlege tenester og hendingar |  yes  |
| [Tjenesteresultattype](tjenesteresultattype.md) | Typen resultat som ei teneste produserer |  yes  |
| [Virksomhetshendelse](virksomhetshendelse.md) | Ei verksemdhending som kan utløyse behov for tenester (t |  no  |
| [Regel](regel.md) | Eit regelverk eller retningsliner som styrer levering av ei teneste |  yes  |
| [OffentligOrganisasjon](offentligorganisasjon.md) | Ein offentleg organisasjon som er ansvarleg for ei teneste |  no  |
| [Hendelse](hendelse.md) | Ei hending som kan utløyse behov for ei offentleg teneste |  yes  |
| [Aktor](aktor.md) | Ein aktør (person eller organisasjon) relatert til ei teneste |  yes  |
| [Gebyr](gebyr.md) | Eit gebyr knytt til ei teneste |  yes  |
| [LovpalagtTjeneste](lovpalagttjeneste.md) | Ei lovpålagd teneste som offentlege organ er pålagde å utføre |  yes  |
| [Tjenestekanal](tjenestekanal.md) | Ein kanal for å få tilgang til ei teneste (t |  yes  |
| [Dokumentasjonstype](dokumentasjonstype.md) | Ein type dokumentasjon som krevst for å levere ei teneste |  yes  |
| [OffentligTjeneste](offentligtjeneste.md) | Ei konkret offentleg teneste levert av ein offentleg organisasjon |  yes  |
| [RegulativRessurs](regulativressurs.md) | Ein regulativ ressurs (lov, forskrift o |  yes  |
| [Tjeneste](tjeneste.md) | Ei teneste levert av ein ikkje-offentleg aktør |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [LovpalagtTjeneste](lovpalagttjeneste.md), [OffentligTjeneste](offentligtjeneste.md), [Tjeneste](tjeneste.md), [Hendelse](hendelse.md), [Aktor](aktor.md), [Tjenestekanal](tjenestekanal.md), [Dokumentasjonstype](dokumentasjonstype.md), [Tjenesteresultattype](tjenesteresultattype.md), [Gebyr](gebyr.md), [Regel](regel.md), [RegulativRessurs](regulativressurs.md), [Katalog](katalog.md) |
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