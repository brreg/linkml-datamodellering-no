

# Slot: id 


_URI-identifikator for ressursen._





URI: [https://data.norge.no/linkml/cpsv-ap-no/id](https://data.norge.no/linkml/cpsv-ap-no/id)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Regel](regel.md) | Eit regelverk eller retningsliner som styrer levering av ei teneste |  no  |
| [Gebyr](gebyr.md) | Eit gebyr knytt til ei teneste |  no  |
| [Spraak](spraak.md) | Ein språkreferanse (dct:LinguisticSystem) |  no  |
| [Tjenesteresultattype](tjenesteresultattype.md) | Typen resultat som ei teneste produserer |  no  |
| [Tjeneste](tjeneste.md) | Ei teneste levert av ein ikkje-offentleg aktør |  no  |
| [Konsept](konsept.md) | Referanse til eit SKOS-omgrep frå eit kontrollert vokabular |  no  |
| [Katalog](katalog.md) | Ein katalog over offentlege tenester og hendingar |  no  |
| [Virksomhetshendelse](virksomhetshendelse.md) | Ei verksemdhending som kan utløyse behov for tenester (t |  no  |
| [Adresse](adresse.md) | Ei postadresse knytt til ein aktør, organisasjon eller kontaktpunkt |  no  |
| [Deltagelse](deltagelse.md) | Ei rolle ein aktør har i leveringa av ei teneste |  no  |
| [OffentligOrganisasjon](offentligorganisasjon.md) | Ein offentleg organisasjon som er ansvarleg for ei teneste |  no  |
| [Mediatype](mediatype.md) | Ein medietype eller filformat (dct:MediaTypeOrExtent) |  no  |
| [Tjenestekanal](tjenestekanal.md) | Ein kanal for å få tilgang til ei teneste (t |  no  |
| [Dokumentasjonstype](dokumentasjonstype.md) | Ein type dokumentasjon som krevst for å levere ei teneste |  no  |
| [RegulativRessurs](regulativressurs.md) | Ein regulativ ressurs (lov, forskrift o |  no  |
| [Livshendelse](livshendelse.md) | Ei livshending som kan utløyse behov for tenester (t |  no  |
| [OffentligTjeneste](offentligtjeneste.md) | Ei konkret offentleg teneste levert av ein offentleg organisasjon |  no  |
| [Kontaktpunkt](kontaktpunkt.md) | Kontaktinformasjon for ei teneste eller ein organisasjon |  no  |
| [Hendelse](hendelse.md) | Ei hending som kan utløyse behov for ei offentleg teneste |  no  |
| [Aktor](aktor.md) | Ein aktør (person eller organisasjon) relatert til ei teneste |  no  |
| [LovpalagtTjeneste](lovpalagttjeneste.md) | Ei lovpålagd teneste som offentlege organ er pålagde å utføre |  no  |
| [Begrepssamling](begrepssamling.md) | Ei SKOS-omgrepssamling (temavokabular) |  no  |
| [Tjenesteresultattypeliste](tjenesteresultattypeliste.md) | Ei liste over moglege tjenesteresultattypar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](uriorcurie.md) |
| Domain Of | [LovpalagtTjeneste](lovpalagttjeneste.md), [OffentligTjeneste](offentligtjeneste.md), [Tjeneste](tjeneste.md), [Hendelse](hendelse.md), [Aktor](aktor.md), [Kontaktpunkt](kontaktpunkt.md), [Tjenestekanal](tjenestekanal.md), [Dokumentasjonstype](dokumentasjonstype.md), [Tjenesteresultattype](tjenesteresultattype.md), [Tjenesteresultattypeliste](tjenesteresultattypeliste.md), [Gebyr](gebyr.md), [Regel](regel.md), [RegulativRessurs](regulativressurs.md), [Deltagelse](deltagelse.md), [Adresse](adresse.md), [Katalog](katalog.md), [Spraak](spraak.md), [Mediatype](mediatype.md), [Konsept](konsept.md), [Begrepssamling](begrepssamling.md) |

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