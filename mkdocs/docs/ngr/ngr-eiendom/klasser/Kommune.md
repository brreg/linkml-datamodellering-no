

# Class: Kommune 


_Norsk kommune. Tilhøyrer Domene nasjonal inndelingsbase og forvaltast av Nasjonal inndelingsbase._





URI: [ngre:Kommune](https://data.norge.no/vocabulary/ngr-eiendom#Kommune)





```mermaid
 classDiagram
    class Kommune
    click Kommune href "../Kommune/"
      Kommune : id
        
          
    
        
        
        Kommune --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Kommune : kommunenummer_verdi
        
          
    
        
        
        Kommune --> "1" String : kommunenummer_verdi
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngre:Kommune](https://data.norge.no/vocabulary/ngr-eiendom#Kommune) |


## Eigenskapar







  
  

  
  
    
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [kommunenummer_verdi](kommunenummer_verdi.md) | 1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Firesifra kommunenummer (t |





  
  

  
  





  
  

  
  






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Matrikkelenhet](matrikkelenhet.md) | [ligger_innenfor_kommune](ligger_innenfor_kommune.md) | range | [Kommune](kommune.md) |
| [Grunneiendom](grunneiendom.md) | [ligger_innenfor_kommune](ligger_innenfor_kommune.md) | range | [Kommune](kommune.md) |
| [Festegrunn](festegrunn.md) | [ligger_innenfor_kommune](ligger_innenfor_kommune.md) | range | [Kommune](kommune.md) |
| [Jordsameie](jordsameie.md) | [ligger_innenfor_kommune](ligger_innenfor_kommune.md) | range | [Kommune](kommune.md) |
| [Eierseksjon](eierseksjon.md) | [ligger_innenfor_kommune](ligger_innenfor_kommune.md) | range | [Kommune](kommune.md) |
| [Anleggseiendom](anleggseiendom.md) | [ligger_innenfor_kommune](ligger_innenfor_kommune.md) | range | [Kommune](kommune.md) |
| [AnnenMatrikkelenhet](annenmatrikkelenhet.md) | [ligger_innenfor_kommune](ligger_innenfor_kommune.md) | range | [Kommune](kommune.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:Kommune |
| native | https://data.norge.no/linkml/ngr-eiendom/Kommune |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Kommune
description: Norsk kommune. Tilhøyrer Domene nasjonal inndelingsbase og forvaltast
  av Nasjonal inndelingsbase.
from_schema: https://data.norge.no/linkml/ngr-eiendom
rank: 1000
slots:
- id
- kommunenummer_verdi
slot_usage:
  kommunenummer_verdi:
    name: kommunenummer_verdi
    in_subset:
    - Obligatorisk
    required: true
class_uri: ngre:Kommune

```
</details>

### Induced

<details>
```yaml
name: Kommune
description: Norsk kommune. Tilhøyrer Domene nasjonal inndelingsbase og forvaltast
  av Nasjonal inndelingsbase.
from_schema: https://data.norge.no/linkml/ngr-eiendom
rank: 1000
slot_usage:
  kommunenummer_verdi:
    name: kommunenummer_verdi
    in_subset:
    - Obligatorisk
    required: true
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/ngr-eiendom
    rank: 1000
    identifier: true
    alias: id
    owner: Kommune
    domain_of:
    - FastEiendom
    - SamletFastEiendom
    - Borettslagsandel
    - Matrikkelenhet
    - Matrikkelnummer
    - Kommunenummer
    - Gaardsnummer
    - Bruksnummer
    - Festenummer
    - Seksjonsnummer
    - Bygning
    - Bygningsnummer
    - Representasjonspunkt
    - YtreInngang
    - Bruksenhet
    - Bruksenhetsnummer
    - Etasje
    - Teig
    - Anleggsprojeksjonsflate
    - Eierforhold
    - Hjemmel
    - Andel
    - Rettighetshaver
    - TinglystHeftelse
    - RettighetForAaBenytteEiendom
    - Borettslag
    - OffisiellAdresse
    - Person
    - Hovedenhet
    - Kommune
    range: uriorcurie
    required: true
  kommunenummer_verdi:
    name: kommunenummer_verdi
    description: Firesifra kommunenummer (t.d. 0301 for Oslo).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/ngr-eiendom
    rank: 1000
    slot_uri: ngre:kommunenummer
    alias: kommunenummer_verdi
    owner: Kommune
    domain_of:
    - Kommunenummer
    - Kommune
    range: string
    required: true
class_uri: ngre:Kommune

```
</details>