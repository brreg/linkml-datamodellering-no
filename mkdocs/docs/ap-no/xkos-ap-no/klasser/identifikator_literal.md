

# Slot: identifikator_literal 


_Tekstleg identifikator for ressursen (dct:identifier)._





URI: [dct:identifier](http://purl.org/dc/terms/identifier)
Alias: identifikator_literal

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
| Range | [String](String.md) |
| Domain Of | [Klassifikasjon](Klassifikasjon.md), [Klassifikasjonssamanlikning](Klassifikasjonssamanlikning.md) |
| Slot URI | [dct:identifier](http://purl.org/dc/terms/identifier) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/xkos-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:identifier |
| native | https://data.norge.no/linkml/xkos-ap-no/identifikator_literal |




## LinkML Source

<details>
```yaml
name: identifikator_literal
description: Tekstleg identifikator for ressursen (dct:identifier).
from_schema: https://data.norge.no/linkml/xkos-ap-no
rank: 1000
slot_uri: dct:identifier
alias: identifikator_literal
domain_of:
- Klassifikasjon
- Klassifikasjonssamanlikning
range: string

```
</details>