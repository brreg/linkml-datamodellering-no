

# Slot: tittel 


_Namn/tittel på ressursen (dct:title)._





URI: [dct:title](http://purl.org/dc/terms/title)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OffentligTjeneste](offentligtjeneste.md) | Ei konkret offentleg teneste levert av ein offentleg organisasjon |  yes  |
| [Tjeneste](tjeneste.md) | Ei teneste levert av ein ikkje-offentleg aktør |  yes  |
| [Hendelse](hendelse.md) | Ei hending som kan utløyse behov for ei offentleg teneste |  yes  |
| [Aktor](aktor.md) | Ein aktør (person eller organisasjon) relatert til ei teneste |  yes  |
| [Dokumentasjonstype](dokumentasjonstype.md) | Ein type dokumentasjon som krevst for å levere ei teneste |  yes  |
| [Tjenesteresultattype](tjenesteresultattype.md) | Typen resultat som ei teneste produserer |  yes  |
| [Tjenesteresultattypeliste](tjenesteresultattypeliste.md) | Ei liste over moglege tjenesteresultattypar |  no  |
| [Regel](regel.md) | Eit regelverk eller retningsliner som styrer levering av ei teneste |  yes  |
| [RegulativRessurs](regulativressurs.md) | Ein regulativ ressurs (lov, forskrift o |  yes  |
| [Katalog](katalog.md) | Ein katalog over offentlege tenester og hendingar |  yes  |
| [Livshendelse](livshendelse.md) | Ei livshending som kan utløyse behov for tenester (t |  no  |
| [Virksomhetshendelse](virksomhetshendelse.md) | Ei verksemdhending som kan utløyse behov for tenester (t |  no  |
| [OffentligOrganisasjon](offentligorganisasjon.md) | Ein offentleg organisasjon som er ansvarleg for ei teneste |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LangString](langstring.md) |
| Domain Of | [OffentligTjeneste](offentligtjeneste.md), [Tjeneste](tjeneste.md), [Hendelse](hendelse.md), [Aktor](aktor.md), [Dokumentasjonstype](dokumentasjonstype.md), [Tjenesteresultattype](tjenesteresultattype.md), [Tjenesteresultattypeliste](tjenesteresultattypeliste.md), [Regel](regel.md), [RegulativRessurs](regulativressurs.md), [Katalog](katalog.md) |
| Slot URI | [dct:title](http://purl.org/dc/terms/title) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/common-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:title |
| native | https://data.norge.no/ap-no/common-ap-no/tittel |




## LinkML Source

<details>
```yaml
name: tittel
description: Namn/tittel på ressursen (dct:title).
from_schema: https://data.norge.no/ap-no/common-ap-no
slot_uri: dct:title
domain_of:
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