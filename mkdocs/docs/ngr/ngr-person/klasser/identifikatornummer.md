

# Slot: identifikatornummer 


_Sjølve identifikatoren som tekststreng (11 siffer for fødselsnummer/D-nummer)._





URI: [ngrp:identifikatornummer](https://data.norge.no/vocabulary/ngr-person#identifikatornummer)
Alias: identifikatornummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Folkeregisteridentifikator](Folkeregisteridentifikator.md) | Abstrakt overklasse for unik identifikator i Folkeregisteret |  no  |
| [DNummer](DNummer.md) | Elleve-sifra D-nummer tildelt utanlandske personar med mellombels opphald i N... |  yes  |
| [Personidentifikasjon](Personidentifikasjon.md) | Utanlandsk eller alternativ identifikasjon av ein person, t |  yes  |
| [Foedselsnummer](Foedselsnummer.md) | Elleve-sifra fødselsnummer tildelt norske statsborgarar og personar med fast ... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Folkeregisteridentifikator](Folkeregisteridentifikator.md), [Personidentifikasjon](Personidentifikasjon.md) |
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