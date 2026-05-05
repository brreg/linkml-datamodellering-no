

# Slot: identifikator 


_Global identifikator (CURIE/URI)._





URI: [samtbuskole:identifikator](https://example.no/ontology/skole#identifikator)
Alias: identifikator

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Skole](skole.md) | En skole er en privat eller offentlig institusjon eller et lærested hvor lære... |  no  |
| [Person](person.md) | Eit menneske individ |  no  |
| [Containerklasse](containerklasse.md) | Containerklasse for alle klasser som kan inngå i datasettet |  no  |
| [Skoleeier](skoleeier.md) | Superklasse for alle typer skoleeiere |  no  |
| [Kommune](kommune.md) | En kommune er et geografisk avgrenset område som utgjør en egen politisk og a... |  no  |
| [Rektor](rektor.md) | Høgaste akademiske leder av en skole |  no  |
| [Kontaktlaerer](kontaktlaerer.md) | En lærer med ansvar for ei basisgruppe og er skolens kontaktpunkt for elevane... |  no  |
| [Fylke](fylke.md) | Fylke (etter norrønt fylki) er en betegnelse på et undernasjonalt, regionalt ... |  no  |
| [Elev](elev.md) | En person som går på skole |  no  |
| [PrivatVirksomhet](privatvirksomhet.md) | Virksomhet, eller foretak, er betegnelser for en juridisk person eller en org... |  no  |
| [Basisgruppe](basisgruppe.md) | Skoleklasse som hovedsaklig samler elever i ulike fag |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](uriorcurie.md) |
| Domain Of | [Containerklasse](containerklasse.md), [Skole](skole.md), [Skoleeier](skoleeier.md), [Basisgruppe](basisgruppe.md), [Person](person.md) |

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


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | samtbuskole:identifikator |
| native | samtbuskole:identifikator |




## LinkML Source

<details>
```yaml
name: identifikator
description: Global identifikator (CURIE/URI).
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
identifier: true
alias: identifikator
domain_of:
- Containerklasse
- Skole
- Skoleeier
- Basisgruppe
- Person
range: uriorcurie
required: true

```
</details>