

# Slot: tittel 


_Namn/tittel på ressursen (dct:title)._





URI: [dct:title](http://purl.org/dc/terms/title)
Alias: tittel

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Regel](Regel.md) | Eit regelverk eller retningsliner som styrer levering av ei teneste |  yes  |
| [Hendelse](Hendelse.md) | Ei hending som kan utløyse behov for ei offentleg teneste |  yes  |
| [LovpalagtTjeneste](LovpalagtTjeneste.md) | Ei lovpålagd teneste som offentlege organ er pålagde å utføre |  yes  |
| [Aktor](Aktor.md) | Ein aktør (person eller organisasjon) relatert til ei teneste |  yes  |
| [RegulativRessurs](RegulativRessurs.md) | Ein regulativ ressurs (lov, forskrift o |  yes  |
| [OffentligTjeneste](OffentligTjeneste.md) | Ei konkret offentleg teneste levert av ein offentleg organisasjon |  yes  |
| [Katalog](Katalog.md) | Ein katalog over offentlege tenester og hendingar |  yes  |
| [Livshendelse](Livshendelse.md) | Ei livshending som kan utløyse behov for tenester (t |  no  |
| [OffentligOrganisasjon](OffentligOrganisasjon.md) | Ein offentleg organisasjon som er ansvarleg for ei teneste |  no  |
| [Virksomhetshendelse](Virksomhetshendelse.md) | Ei verksemdhending som kan utløyse behov for tenester (t |  no  |
| [Tjenesteresultattypeliste](Tjenesteresultattypeliste.md) | Ei liste over moglege tjenesteresultattypar |  no  |
| [Dokumentasjonstype](Dokumentasjonstype.md) | Ein type dokumentasjon som krevst for å levere ei teneste |  yes  |
| [Tjenesteresultattype](Tjenesteresultattype.md) | Typen resultat som ei teneste produserer |  yes  |
| [Tjeneste](Tjeneste.md) | Ei teneste levert av ein ikkje-offentleg aktør |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LangString](LangString.md) |
| Domain Of | [LovpalagtTjeneste](LovpalagtTjeneste.md), [OffentligTjeneste](OffentligTjeneste.md), [Tjeneste](Tjeneste.md), [Hendelse](Hendelse.md), [Aktor](Aktor.md), [Dokumentasjonstype](Dokumentasjonstype.md), [Tjenesteresultattype](Tjenesteresultattype.md), [Tjenesteresultattypeliste](Tjenesteresultattypeliste.md), [Regel](Regel.md), [RegulativRessurs](RegulativRessurs.md), [Katalog](Katalog.md) |
| Slot URI | [dct:title](http://purl.org/dc/terms/title) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/cpsv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:title |
| native | https://data.norge.no/linkml/cpsv-ap-no/tittel |




## LinkML Source

<details>
```yaml
name: tittel
description: Namn/tittel på ressursen (dct:title).
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: dct:title
alias: tittel
domain_of:
- LovpalagtTjeneste
- OffentligTjeneste
- Tjeneste
- Hendelse
- Aktor
- Dokumentasjonstype
- Tjenesteresultattype
- Tjenesteresultattypeliste
- Regel
- RegulativRessurs
- Katalog
range: LangString
multivalued: true

```
</details>