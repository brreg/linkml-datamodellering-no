

# Slot: spraak 


_Språk brukt i ressursen. Verdien SKAL veljast frå EUs kontrollerte vokabular Language (http://publications.europa.eu/resource/authority/language/). Enumerasjonen EULanguage i common-ap-no dekkjer norske språk (bokmål, nynorsk, samiske språk). For andre språk, bruk URI frå EU Language-vokabularet (t.d. ENG for engelsk, SWE for svensk)._





URI: [dct:language](http://purl.org/dc/terms/language)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Tekstdel](tekstdel.md) | Ein tekstleg del av ein kvalitetsmerknad (Web Annotation). |  yes  |
| [RegulativRessurs](regulativressurs.md) | Ein regulativ ressurs (lov, forskrift o.l.) som gjeld for ein ressurs. |  yes  |
| [Distribusjon](distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett. |  yes  |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør. |  yes  |
| [Katalogpost](katalogpost.md) | Ein katalogpost som beskriv ein ressurs i katalogen. |  yes  |
| [Katalog](katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre katalogar. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Konsept](konsept.md) |
| Domain Of | [Tekstdel](tekstdel.md), [RegulativRessurs](regulativressurs.md), [Distribusjon](distribusjon.md), [Datasett](datasett.md), [Katalogpost](katalogpost.md), [Katalog](katalog.md) |
| Slot URI | [dct:language](http://purl.org/dc/terms/language) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| gyldige_verdier | http://publications.europa.eu/resource/authority/language/ |
| vokabular_krav | skal |
| vokabular_pattern | ^http://publications\.europa\.eu/resource/authority/language/[A-Z]{3}$ |
| enum_referanse | EULanguage |
| enum_dekning | delvis |




### Schema Source


* from schema: https://data.norge.no/ap-no/common-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:language |
| native | https://data.norge.no/ap-no/common-ap-no/spraak |




## LinkML Source

<details>
```yaml
name: spraak
annotations:
  gyldige_verdier:
    tag: gyldige_verdier
    value: http://publications.europa.eu/resource/authority/language/
  vokabular_krav:
    tag: vokabular_krav
    value: skal
  vokabular_pattern:
    tag: vokabular_pattern
    value: ^http://publications\.europa\.eu/resource/authority/language/[A-Z]{3}$
  enum_referanse:
    tag: enum_referanse
    value: EULanguage
  enum_dekning:
    tag: enum_dekning
    value: delvis
description: Språk brukt i ressursen. Verdien SKAL veljast frå EUs kontrollerte vokabular
  Language (http://publications.europa.eu/resource/authority/language/). Enumerasjonen
  EULanguage i common-ap-no dekkjer norske språk (bokmål, nynorsk, samiske språk).
  For andre språk, bruk URI frå EU Language-vokabularet (t.d. ENG for engelsk, SWE
  for svensk).
from_schema: https://data.norge.no/ap-no/common-ap-no
slot_uri: dct:language
domain_of:
- Tekstdel
- RegulativRessurs
- Distribusjon
- Datasett
- Katalogpost
- Katalog
range: Konsept
multivalued: true

```
</details>