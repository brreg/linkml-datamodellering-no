

# Slot: id 


_URI-identifikator for ressursen._





URI: [https://data.norge.no/linkml/cpsv-ap-no/id](https://data.norge.no/linkml/cpsv-ap-no/id)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Regel](Regel.md) | Eit regelverk eller retningsliner som styrer levering av ei teneste |  no  |
| [Adresse](Adresse.md) | Ei postadresse knytt til ein aktør, organisasjon eller kontaktpunkt |  no  |
| [OffentligTjeneste](OffentligTjeneste.md) | Ei konkret offentleg teneste levert av ein offentleg organisasjon |  no  |
| [Konsept](Konsept.md) | Referanse til eit SKOS-omgrep frå eit kontrollert vokabular |  no  |
| [Gebyr](Gebyr.md) | Eit gebyr knytt til ei teneste |  no  |
| [LovpalagtTjeneste](LovpalagtTjeneste.md) | Ei lovpålagd teneste som offentlege organ er pålagde å utføre |  no  |
| [Dokumentasjonstype](Dokumentasjonstype.md) | Ein type dokumentasjon som krevst for å levere ei teneste |  no  |
| [Tjenesteresultattype](Tjenesteresultattype.md) | Typen resultat som ei teneste produserer |  no  |
| [Mediatype](Mediatype.md) | Ein medietype eller filformat (dct:MediaTypeOrExtent) |  no  |
| [RegulativRessurs](RegulativRessurs.md) | Ein regulativ ressurs (lov, forskrift o |  no  |
| [Katalog](Katalog.md) | Ein katalog over offentlege tenester og hendingar |  no  |
| [Livshendelse](Livshendelse.md) | Ei livshending som kan utløyse behov for tenester (t |  no  |
| [Kontaktpunkt](Kontaktpunkt.md) | Kontaktinformasjon for ei teneste eller ein organisasjon |  no  |
| [Virksomhetshendelse](Virksomhetshendelse.md) | Ei verksemdhending som kan utløyse behov for tenester (t |  no  |
| [Tjeneste](Tjeneste.md) | Ei teneste levert av ein ikkje-offentleg aktør |  no  |
| [Tjenestekanal](Tjenestekanal.md) | Ein kanal for å få tilgang til ei teneste (t |  no  |
| [OffentligOrganisasjon](OffentligOrganisasjon.md) | Ein offentleg organisasjon som er ansvarleg for ei teneste |  no  |
| [Hendelse](Hendelse.md) | Ei hending som kan utløyse behov for ei offentleg teneste |  no  |
| [Aktor](Aktor.md) | Ein aktør (person eller organisasjon) relatert til ei teneste |  no  |
| [Deltagelse](Deltagelse.md) | Ei rolle ein aktør har i leveringa av ei teneste |  no  |
| [Tjenesteresultattypeliste](Tjenesteresultattypeliste.md) | Ei liste over moglege tjenesteresultattypar |  no  |
| [Begrepssamling](Begrepssamling.md) | Ei SKOS-omgrepssamling (temavokabular) |  no  |
| [Spraak](Spraak.md) | Ein språkreferanse (dct:LinguisticSystem) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [LovpalagtTjeneste](LovpalagtTjeneste.md), [OffentligTjeneste](OffentligTjeneste.md), [Tjeneste](Tjeneste.md), [Hendelse](Hendelse.md), [Aktor](Aktor.md), [Kontaktpunkt](Kontaktpunkt.md), [Tjenestekanal](Tjenestekanal.md), [Dokumentasjonstype](Dokumentasjonstype.md), [Tjenesteresultattype](Tjenesteresultattype.md), [Tjenesteresultattypeliste](Tjenesteresultattypeliste.md), [Gebyr](Gebyr.md), [Regel](Regel.md), [RegulativRessurs](RegulativRessurs.md), [Deltagelse](Deltagelse.md), [Adresse](Adresse.md), [Katalog](Katalog.md), [Spraak](Spraak.md), [Mediatype](Mediatype.md), [Konsept](Konsept.md), [Begrepssamling](Begrepssamling.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/cpsv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/linkml/cpsv-ap-no/id |
| native | https://data.norge.no/linkml/cpsv-ap-no/id |




## LinkML Source

<details>
```yaml
name: id
description: URI-identifikator for ressursen.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
identifier: true
alias: id
domain_of:
- LovpalagtTjeneste
- OffentligTjeneste
- Tjeneste
- Hendelse
- Aktor
- Kontaktpunkt
- Tjenestekanal
- Dokumentasjonstype
- Tjenesteresultattype
- Tjenesteresultattypeliste
- Gebyr
- Regel
- RegulativRessurs
- Deltagelse
- Adresse
- Katalog
- Spraak
- Mediatype
- Konsept
- Begrepssamling
range: uriorcurie
required: true

```
</details>