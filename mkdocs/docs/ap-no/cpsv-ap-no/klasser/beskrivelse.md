

# Slot: beskrivelse 


_Fritekstbeskrivelse av ressursen (dct:description)._





URI: [dct:description](http://purl.org/dc/terms/description)
Alias: beskrivelse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Tjenestekanal](Tjenestekanal.md) | Ein kanal for å få tilgang til ei teneste (t |  yes  |
| [Regel](Regel.md) | Eit regelverk eller retningsliner som styrer levering av ei teneste |  yes  |
| [Hendelse](Hendelse.md) | Ei hending som kan utløyse behov for ei offentleg teneste |  yes  |
| [Gebyr](Gebyr.md) | Eit gebyr knytt til ei teneste |  yes  |
| [LovpalagtTjeneste](LovpalagtTjeneste.md) | Ei lovpålagd teneste som offentlege organ er pålagde å utføre |  yes  |
| [OffentligTjeneste](OffentligTjeneste.md) | Ei konkret offentleg teneste levert av ein offentleg organisasjon |  yes  |
| [Katalog](Katalog.md) | Ein katalog over offentlege tenester og hendingar |  yes  |
| [Livshendelse](Livshendelse.md) | Ei livshending som kan utløyse behov for tenester (t |  no  |
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
| Domain Of | [LovpalagtTjeneste](LovpalagtTjeneste.md), [OffentligTjeneste](OffentligTjeneste.md), [Tjeneste](Tjeneste.md), [Hendelse](Hendelse.md), [Tjenestekanal](Tjenestekanal.md), [Dokumentasjonstype](Dokumentasjonstype.md), [Tjenesteresultattype](Tjenesteresultattype.md), [Tjenesteresultattypeliste](Tjenesteresultattypeliste.md), [Gebyr](Gebyr.md), [Regel](Regel.md), [Katalog](Katalog.md) |
| Slot URI | [dct:description](http://purl.org/dc/terms/description) |

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
| self | dct:description |
| native | https://data.norge.no/linkml/cpsv-ap-no/beskrivelse |




## LinkML Source

<details>
```yaml
name: beskrivelse
description: Fritekstbeskrivelse av ressursen (dct:description).
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: dct:description
alias: beskrivelse
domain_of:
- LovpalagtTjeneste
- OffentligTjeneste
- Tjeneste
- Hendelse
- Tjenestekanal
- Dokumentasjonstype
- Tjenesteresultattype
- Tjenesteresultattypeliste
- Gebyr
- Regel
- Katalog
range: LangString
multivalued: true

```
</details>