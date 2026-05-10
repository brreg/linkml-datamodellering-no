

# Slot: identifikatornummer 


_Sjølve identifikatoren som tekststreng (11 siffer for fødselsnummer/D-nummer)._





URI: [ngrp:identifikatornummer](https://data.norge.no/vocabulary/ngr-person#identifikatornummer)
Alias: identifikatornummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DNummer](dnummer.md) | Elleve-sifra D-nummer tildelt utanlandske personar med mellombels opphald i N... |  yes  |
| [Foedselsnummer](foedselsnummer.md) | Elleve-sifra fødselsnummer tildelt norske statsborgarar og personar med fast ... |  yes  |
| [Personidentifikasjon](personidentifikasjon.md) | Utanlandsk eller alternativ identifikasjon av ein person, t |  yes  |
| [Folkeregisteridentifikator](folkeregisteridentifikator.md) | Abstrakt overklasse for unik identifikator i Folkeregisteret |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Folkeregisteridentifikator](folkeregisteridentifikator.md), [Personidentifikasjon](personidentifikasjon.md) |
| Slot URI | [ngrp:identifikatornummer](https://data.norge.no/vocabulary/ngr-person#identifikatornummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:identifikatornummer |
| native | https://data.norge.no/linkml/ngr-person/identifikatornummer |




## LinkML Source

<details>
```yaml
name: identifikatornummer
description: Sjølve identifikatoren som tekststreng (11 siffer for fødselsnummer/D-nummer).
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
slot_uri: ngrp:identifikatornummer
alias: identifikatornummer
domain_of:
- Folkeregisteridentifikator
- Personidentifikasjon
range: string

```
</details>