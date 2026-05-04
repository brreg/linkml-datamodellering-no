

# Slot: utgjevar 


_Organisasjon som er ansvarleg utgjevar (dct:publisher)._





URI: [dct:publisher](http://purl.org/dc/terms/publisher)
Alias: utgjevar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Klassifikasjonssamanlikning](Klassifikasjonssamanlikning.md) | Ein samanlikning mellom to klassifikasjonar (xkos:Correspondence) |  yes  |
| [Klassifikasjon](Klassifikasjon.md) | Ei klassifikasjon – ein systematisk struktur av kategoriar brukt til å klassi... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Organisasjon](Organisasjon.md) |
| Domain Of | [Klassifikasjon](Klassifikasjon.md), [Klassifikasjonssamanlikning](Klassifikasjonssamanlikning.md) |
| Slot URI | [dct:publisher](http://purl.org/dc/terms/publisher) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/xkos-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:publisher |
| native | https://data.norge.no/linkml/xkos-ap-no/utgjevar |




## LinkML Source

<details>
```yaml
name: utgjevar
description: Organisasjon som er ansvarleg utgjevar (dct:publisher).
from_schema: https://data.norge.no/linkml/xkos-ap-no
rank: 1000
slot_uri: dct:publisher
alias: utgjevar
domain_of:
- Klassifikasjon
- Klassifikasjonssamanlikning
range: Organisasjon

```
</details>