

# Slot: beskrivelse 


_Fritekstbeskrivelse av ressursen (dct:description)._





URI: [dct:description](http://purl.org/dc/terms/description)
Alias: beskrivelse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Livshendelse](livshendelse.md) | Ei livshending som kan utløyse behov for tenester (t |  no  |
| [Katalog](katalog.md) | Ein katalog over offentlege tenester og hendingar |  yes  |
| [Tjenesteresultattype](tjenesteresultattype.md) | Typen resultat som ei teneste produserer |  yes  |
| [Virksomhetshendelse](virksomhetshendelse.md) | Ei verksemdhending som kan utløyse behov for tenester (t |  no  |
| [Regel](regel.md) | Eit regelverk eller retningsliner som styrer levering av ei teneste |  yes  |
| [Hendelse](hendelse.md) | Ei hending som kan utløyse behov for ei offentleg teneste |  yes  |
| [Gebyr](gebyr.md) | Eit gebyr knytt til ei teneste |  yes  |
| [Tjenesteresultattypeliste](tjenesteresultattypeliste.md) | Ei liste over moglege tjenesteresultattypar |  no  |
| [LovpalagtTjeneste](lovpalagttjeneste.md) | Ei lovpålagd teneste som offentlege organ er pålagde å utføre |  yes  |
| [Tjenestekanal](tjenestekanal.md) | Ein kanal for å få tilgang til ei teneste (t |  yes  |
| [Dokumentasjonstype](dokumentasjonstype.md) | Ein type dokumentasjon som krevst for å levere ei teneste |  yes  |
| [OffentligTjeneste](offentligtjeneste.md) | Ei konkret offentleg teneste levert av ein offentleg organisasjon |  yes  |
| [Tjeneste](tjeneste.md) | Ei teneste levert av ein ikkje-offentleg aktør |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LangString](langstring.md) |
| Domain Of | [LovpalagtTjeneste](lovpalagttjeneste.md), [OffentligTjeneste](offentligtjeneste.md), [Tjeneste](tjeneste.md), [Hendelse](hendelse.md), [Tjenestekanal](tjenestekanal.md), [Dokumentasjonstype](dokumentasjonstype.md), [Tjenesteresultattype](tjenesteresultattype.md), [Tjenesteresultattypeliste](tjenesteresultattypeliste.md), [Gebyr](gebyr.md), [Regel](regel.md), [Katalog](katalog.md) |
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