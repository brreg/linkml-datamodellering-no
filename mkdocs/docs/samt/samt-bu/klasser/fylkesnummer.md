

# Slot: fylkesnummer 


_Fylkesnummer er definerte identifikasjonskoder for Norges fylker og to territorier (Svalbard og Jan Mayen)._





URI: [dcat:identifier](http://www.w3.org/ns/dcat#identifier)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fylke](fylke.md) | Fylke (etter norrønt fylki) er en betegnelse på et undernasjonalt, regionalt ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Fylke](fylke.md) |
| Slot URI | [dcat:identifier](http://www.w3.org/ns/dcat#identifier) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:identifier |
| native | samtbuskole:fylkesnummer |
| close | skos:notation |




## LinkML Source

<details>
```yaml
name: fylkesnummer
description: Fylkesnummer er definerte identifikasjonskoder for Norges fylker og to
  territorier (Svalbard og Jan Mayen).
from_schema: https://example.no/ontology/samt-bu-skole
close_mappings:
- skos:notation
rank: 1000
slot_uri: dcat:identifier
domain_of:
- Fylke
range: string

```
</details>