

# Slot: navn 


_Namn på ressursen._





URI: [samtbuskole:navn](https://example.no/ontology/skole#navn)
Alias: navn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Skoleeier](skoleeier.md) | Superklasse for alle typer skoleeiere |  no  |
| [Basisgruppe](basisgruppe.md) | Skoleklasse som hovedsaklig samler elever i ulike fag |  no  |
| [Skole](skole.md) | En skole er en privat eller offentlig institusjon eller et lærested hvor lære... |  no  |
| [Kontaktlaerer](kontaktlaerer.md) | En lærer med ansvar for ei basisgruppe og er skolens kontaktpunkt for elevane... |  no  |
| [PrivatVirksomhet](privatvirksomhet.md) | Virksomhet, eller foretak, er betegnelser for en juridisk person eller en org... |  no  |
| [Rektor](rektor.md) | Høgaste akademiske leder av en skole |  no  |
| [Person](person.md) | Eit menneske individ |  no  |
| [Kommune](kommune.md) | En kommune er et geografisk avgrenset område som utgjør en egen politisk og a... |  no  |
| [Fylke](fylke.md) | Fylke (etter norrønt fylki) er en betegnelse på et undernasjonalt, regionalt ... |  no  |
| [Elev](elev.md) | En person som går på skole |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Skole](skole.md), [Skoleeier](skoleeier.md), [Basisgruppe](basisgruppe.md), [Person](person.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | samtbuskole:navn |
| native | samtbuskole:navn |




## LinkML Source

<details>
```yaml
name: navn
description: Namn på ressursen.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
alias: navn
domain_of:
- Skole
- Skoleeier
- Basisgruppe
- Person
range: string

```
</details>