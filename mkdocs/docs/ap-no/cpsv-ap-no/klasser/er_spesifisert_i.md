

# Slot: er_spesifisert_i 


_Liste eller spesifikasjon ressursen er del av._





URI: [cv:isSpecifiedIn](http://data.europa.eu/m8g/isSpecifiedIn)
Alias: er_spesifisert_i

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dokumentasjonstype](dokumentasjonstype.md) | Ein type dokumentasjon som krevst for å levere ei teneste |  yes  |
| [Tjenesteresultattype](tjenesteresultattype.md) | Typen resultat som ei teneste produserer |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](uriorcurie.md) |
| Domain Of | [Dokumentasjonstype](dokumentasjonstype.md), [Tjenesteresultattype](tjenesteresultattype.md) |
| Slot URI | [cv:isSpecifiedIn](http://data.europa.eu/m8g/isSpecifiedIn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/cpsv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cv:isSpecifiedIn |
| native | https://data.norge.no/linkml/cpsv-ap-no/er_spesifisert_i |




## LinkML Source

<details>
```yaml
name: er_spesifisert_i
description: Liste eller spesifikasjon ressursen er del av.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: cv:isSpecifiedIn
alias: er_spesifisert_i
domain_of:
- Dokumentasjonstype
- Tjenesteresultattype
range: uriorcurie

```
</details>