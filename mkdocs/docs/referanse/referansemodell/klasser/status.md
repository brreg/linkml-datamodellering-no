

# Slot: status 


_Status for ressursen. Verdien SKAL veljast frå ADMS Status-vokabularet (http://purl.org/adms/status/). Gyldige verdiar: Completed (ferdigstilt), Deprecated (foreldet), UnderDevelopment (under utvikling), Withdrawn (trukket tilbake). Sjå enumerasjonen ADMSStatus i common-ap-no._





URI: [adms:status](http://www.w3.org/ns/adms#status)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Distribusjon](distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett. |  yes  |
| [Datatjeneste](datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt. |  yes  |
| [Katalogpost](katalogpost.md) | Ein katalogpost som beskriv ein ressurs i katalogen. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Konsept](konsept.md) |
| Domain Of | [Distribusjon](distribusjon.md), [Datatjeneste](datatjeneste.md), [Katalogpost](katalogpost.md) |
| Slot URI | [adms:status](http://www.w3.org/ns/adms#status) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| gyldige_verdier | http://purl.org/adms/status/ |
| vokabular_krav | skal |
| vokabular_pattern | `^http://purl\.org/adms/status/(Completed|Deprecated|UnderDevelopment|Withdrawn)$` |
| enum_referanse | ADMSStatus |
| enum_dekning | full |




### Schema Source


* from schema: https://data.norge.no/ap-no/common-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adms:status |
| native | https://data.norge.no/ap-no/common-ap-no/status |




## LinkML Source

<details>
```yaml
name: status
annotations:
  gyldige_verdier:
    tag: gyldige_verdier
    value: http://purl.org/adms/status/
  vokabular_krav:
    tag: vokabular_krav
    value: skal
  vokabular_pattern:
    tag: vokabular_pattern
    value: ^http://purl\.org/adms/status/(Completed|Deprecated|UnderDevelopment|Withdrawn)$
  enum_referanse:
    tag: enum_referanse
    value: ADMSStatus
  enum_dekning:
    tag: enum_dekning
    value: full
description: 'Status for ressursen. Verdien SKAL veljast frå ADMS Status-vokabularet
  (http://purl.org/adms/status/). Gyldige verdiar: Completed (ferdigstilt), Deprecated
  (foreldet), UnderDevelopment (under utvikling), Withdrawn (trukket tilbake). Sjå
  enumerasjonen ADMSStatus i common-ap-no.'
from_schema: https://data.norge.no/ap-no/common-ap-no
slot_uri: adms:status
domain_of:
- Distribusjon
- Datatjeneste
- Katalogpost
range: Konsept

```
</details>