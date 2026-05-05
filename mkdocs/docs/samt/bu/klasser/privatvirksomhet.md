

# Class: PrivatVirksomhet 


_Virksomhet, eller foretak, er betegnelser for en juridisk person eller en organisasjon som produserer varer eller tjenester._





URI: [samtbuskole:PrivatVirksomhet](https://example.no/ontology/skole#PrivatVirksomhet)





```mermaid
 classDiagram
    class PrivatVirksomhet
    click PrivatVirksomhet href "../PrivatVirksomhet/"
      Skoleeier <|-- PrivatVirksomhet
        click Skoleeier href "../Skoleeier/"
      
      PrivatVirksomhet : identifikator
        
      PrivatVirksomhet : navn
        
      PrivatVirksomhet : organisasjonsnummer
        
      
```





## Inheritance
* [Skoleeier](skoleeier.md)
    * **PrivatVirksomhet**


## Eigenskapar







  
  





  
  





  
  






  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [organisasjonsnummer](organisasjonsnummer.md) | 0..1 <br/> [String](string.md) | Organisasjonsnummer er i Norge et ni-sifret registreringsnummer som tildeles ... |




### Arva

| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- || [identifikator](identifikator.md) | 1 <br/> [Uriorcurie](uriorcurie.md) | Global identifikator (CURIE/URI) | [Skoleeier](skoleeier.md) |
| [navn](navn.md) | 0..1 <br/> [String](string.md) | Namn på ressursen | [Skoleeier](skoleeier.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Containerklasse](containerklasse.md) | [private_virksomheter](private_virksomheter.md) | range | [PrivatVirksomhet](privatvirksomhet.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | samtbuskole:PrivatVirksomhet |
| native | samtbuskole:PrivatVirksomhet |
| exact | org:Organization, schema:Organization |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PrivatVirksomhet
description: Virksomhet, eller foretak, er betegnelser for en juridisk person eller
  en organisasjon som produserer varer eller tjenester.
from_schema: https://example.no/ontology/samt-bu-skole
exact_mappings:
- org:Organization
- schema:Organization
is_a: Skoleeier
slots:
- organisasjonsnummer

```
</details>

### Induced

<details>
```yaml
name: PrivatVirksomhet
description: Virksomhet, eller foretak, er betegnelser for en juridisk person eller
  en organisasjon som produserer varer eller tjenester.
from_schema: https://example.no/ontology/samt-bu-skole
exact_mappings:
- org:Organization
- schema:Organization
is_a: Skoleeier
attributes:
  organisasjonsnummer:
    name: organisasjonsnummer
    description: Organisasjonsnummer er i Norge et ni-sifret registreringsnummer som
      tildeles av Enhetsregisteret ved Brønnøysundregistrene for en organisasjon (foretak,
      idrettslag og lignende).
    from_schema: https://example.no/ontology/samt-bu-skole
    exact_mappings:
    - adms:identifier
    rank: 1000
    slot_uri: dct:identifier
    alias: organisasjonsnummer
    owner: PrivatVirksomhet
    domain_of:
    - PrivatVirksomhet
    range: string
  identifikator:
    name: identifikator
    description: Global identifikator (CURIE/URI).
    from_schema: https://example.no/ontology/samt-bu-skole
    rank: 1000
    identifier: true
    alias: identifikator
    owner: PrivatVirksomhet
    domain_of:
    - Containerklasse
    - Skole
    - Skoleeier
    - Basisgruppe
    - Person
    range: uriorcurie
    required: true
  navn:
    name: navn
    description: Namn på ressursen.
    from_schema: https://example.no/ontology/samt-bu-skole
    rank: 1000
    alias: navn
    owner: PrivatVirksomhet
    domain_of:
    - Skole
    - Skoleeier
    - Basisgruppe
    - Person
    range: string

```
</details>