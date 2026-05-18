

# Class: Grunneiendom 


_Den vanlegaste typen matrikkelenheit. Eit avgrensa areal av jord- eller vassoverflate (eventuelt med undergrunn og luftrom) innanfor ein kommune._





URI: [ngre:Grunneiendom](https://data.norge.no/vocabulary/ngr-eiendom#Grunneiendom)





```mermaid
 classDiagram
    class Grunneiendom
    click Grunneiendom href "../Grunneiendom/"
      Matrikkelenhet <|-- Grunneiendom
        click Matrikkelenhet href "../Matrikkelenhet/"
      
      Grunneiendom : er_del_av_teig
        
          
    
        
        
        Grunneiendom --> "*" Teig : er_del_av_teig
        click Teig href "../Teig/"
    

        
      Grunneiendom : har_anleggsprojeksjonsflate
        
          
    
        
        
        Grunneiendom --> "0..1" Anleggsprojeksjonsflate : har_anleggsprojeksjonsflate
        click Anleggsprojeksjonsflate href "../Anleggsprojeksjonsflate/"
    

        
      Grunneiendom : har_teig
        
          
    
        
        
        Grunneiendom --> "*" Teig : har_teig
        click Teig href "../Teig/"
    

        
      Grunneiendom : id
        
          
    
        
        
        Grunneiendom --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Grunneiendom : identifiseres_med
        
          
    
        
        
        Grunneiendom --> "1" Matrikkelnummer : identifiseres_med
        click Matrikkelnummer href "../Matrikkelnummer/"
    

        
      Grunneiendom : kan_vaere_pa
        
          
    
        
        
        Grunneiendom --> "0..1" Matrikkelenhet : kan_vaere_pa
        click Matrikkelenhet href "../Matrikkelenhet/"
    

        
      Grunneiendom : ligger_innenfor_kommune
        
          
    
        
        
        Grunneiendom --> "1" Kommune : ligger_innenfor_kommune
        click Kommune href "../Kommune/"
    

        
      
```





## Inheritance
* [Matrikkelenhet](matrikkelenhet.md)
    * **Grunneiendom**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngre:Grunneiendom](https://data.norge.no/vocabulary/ngr-eiendom#Grunneiendom) |


## Eigenskapar







  
  





  
  





  
  
    
  


### Valgfri

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [kan_vaere_pa](kan_vaere_pa.md) | 0..1 <br/> [Matrikkelenhet](matrikkelenhet.md) | Matrikkeleininga denne eininga ligg på eller er knytt til |






  
  
  
    
      
    
      
    
      
    
  
  




### Arva

| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- || [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen | [Matrikkelenhet](matrikkelenhet.md) |
| [identifiseres_med](identifiseres_med.md) | 1 <br/> [Matrikkelnummer](matrikkelnummer.md) | Matrikkelnummeret som identifiserer matrikkeleininga | [Matrikkelenhet](matrikkelenhet.md) |
| [ligger_innenfor_kommune](ligger_innenfor_kommune.md) | 1 <br/> [Kommune](kommune.md) | Kommunen matrikkeleininga ligg innanfor | [Matrikkelenhet](matrikkelenhet.md) |
| [er_del_av_teig](er_del_av_teig.md) | * <br/> [Teig](teig.md) | Teigen(e) matrikkeleininga er del av | [Matrikkelenhet](matrikkelenhet.md) |
| [har_teig](har_teig.md) | * <br/> [Teig](teig.md) | Teigen(e) som tilhøyrer matrikkeleininga | [Matrikkelenhet](matrikkelenhet.md) |
| [har_anleggsprojeksjonsflate](har_anleggsprojeksjonsflate.md) | 0..1 <br/> [Anleggsprojeksjonsflate](anleggsprojeksjonsflate.md) | Anleggsprojeksjonsflata (fotavtrykket) for anleggseigedommen | [Matrikkelenhet](matrikkelenhet.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [EiendomContainer](eiendomcontainer.md) | [grunneiendommer](grunneiendommer.md) | range | [Grunneiendom](grunneiendom.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:Grunneiendom |
| native | https://data.norge.no/linkml/ngr-eiendom/Grunneiendom |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Grunneiendom
description: Den vanlegaste typen matrikkelenheit. Eit avgrensa areal av jord- eller
  vassoverflate (eventuelt med undergrunn og luftrom) innanfor ein kommune.
from_schema: https://data.norge.no/linkml/ngr-eiendom
rank: 1000
is_a: Matrikkelenhet
slots:
- kan_vaere_pa
slot_usage:
  kan_vaere_pa:
    name: kan_vaere_pa
    in_subset:
    - Valgfri
class_uri: ngre:Grunneiendom

```
</details>

### Induced

<details>
```yaml
name: Grunneiendom
description: Den vanlegaste typen matrikkelenheit. Eit avgrensa areal av jord- eller
  vassoverflate (eventuelt med undergrunn og luftrom) innanfor ein kommune.
from_schema: https://data.norge.no/linkml/ngr-eiendom
rank: 1000
is_a: Matrikkelenhet
slot_usage:
  kan_vaere_pa:
    name: kan_vaere_pa
    in_subset:
    - Valgfri
attributes:
  kan_vaere_pa:
    name: kan_vaere_pa
    description: Matrikkeleininga denne eininga ligg på eller er knytt til. Festegrunn
      kan liggje på grunneigendom eller jordsameige; eigarseksjon kan liggje på grunneigendom,
      festegrunn eller anleggseigendom.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/ngr-eiendom
    rank: 1000
    slot_uri: ngre:kanVaerePa
    alias: kan_vaere_pa
    owner: Grunneiendom
    domain_of:
    - Grunneiendom
    - Festegrunn
    - Jordsameie
    - Eierseksjon
    range: Matrikkelenhet
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/ngr-eiendom
    rank: 1000
    identifier: true
    alias: id
    owner: Grunneiendom
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
  identifiseres_med:
    name: identifiseres_med
    description: Matrikkelnummeret som identifiserer matrikkeleininga.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/ngr-eiendom
    rank: 1000
    slot_uri: ngre:identifiseresMed
    alias: identifiseres_med
    owner: Grunneiendom
    domain_of:
    - Matrikkelenhet
    range: Matrikkelnummer
    required: true
  ligger_innenfor_kommune:
    name: ligger_innenfor_kommune
    description: Kommunen matrikkeleininga ligg innanfor.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/ngr-eiendom
    rank: 1000
    slot_uri: ngre:liggerInnenforKommune
    alias: ligger_innenfor_kommune
    owner: Grunneiendom
    domain_of:
    - Matrikkelenhet
    range: Kommune
    required: true
  er_del_av_teig:
    name: er_del_av_teig
    description: Teigen(e) matrikkeleininga er del av.
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/linkml/ngr-eiendom
    rank: 1000
    slot_uri: ngre:erDelAvTeig
    alias: er_del_av_teig
    owner: Grunneiendom
    domain_of:
    - Matrikkelenhet
    range: Teig
    multivalued: true
  har_teig:
    name: har_teig
    description: Teigen(e) som tilhøyrer matrikkeleininga.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/ngr-eiendom
    rank: 1000
    slot_uri: ngre:harTeig
    alias: har_teig
    owner: Grunneiendom
    domain_of:
    - Matrikkelenhet
    range: Teig
    multivalued: true
  har_anleggsprojeksjonsflate:
    name: har_anleggsprojeksjonsflate
    description: Anleggsprojeksjonsflata (fotavtrykket) for anleggseigedommen.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/ngr-eiendom
    rank: 1000
    slot_uri: ngre:harAnleggsprojeksjonsflate
    alias: har_anleggsprojeksjonsflate
    owner: Grunneiendom
    domain_of:
    - Matrikkelenhet
    range: Anleggsprojeksjonsflate
class_uri: ngre:Grunneiendom

```
</details>