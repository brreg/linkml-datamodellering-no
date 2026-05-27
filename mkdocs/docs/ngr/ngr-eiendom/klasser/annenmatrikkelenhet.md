

# Class: AnnenMatrikkelenhet 


_Matrikkelenheit som ikkje fell inn under dei andre underklassane._





URI: [ngre:AnnenMatrikkelenhet](https://data.norge.no/vocabulary/ngr-eiendom#AnnenMatrikkelenhet)





```mermaid
 classDiagram
    class AnnenMatrikkelenhet
    click AnnenMatrikkelenhet href "../AnnenMatrikkelenhet/"
      Matrikkelenhet <|-- AnnenMatrikkelenhet
        click Matrikkelenhet href "../Matrikkelenhet/"
      
      AnnenMatrikkelenhet : er_del_av_teig
        
          
    
        
        
        AnnenMatrikkelenhet --> "*" Teig : er_del_av_teig
        click Teig href "../Teig/"
    

        
      AnnenMatrikkelenhet : har_anleggsprojeksjonsflate
        
          
    
        
        
        AnnenMatrikkelenhet --> "0..1" Anleggsprojeksjonsflate : har_anleggsprojeksjonsflate
        click Anleggsprojeksjonsflate href "../Anleggsprojeksjonsflate/"
    

        
      AnnenMatrikkelenhet : har_teig
        
          
    
        
        
        AnnenMatrikkelenhet --> "*" Teig : har_teig
        click Teig href "../Teig/"
    

        
      AnnenMatrikkelenhet : id
        
          
    
        
        
        AnnenMatrikkelenhet --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      AnnenMatrikkelenhet : identifiseres_med
        
          
    
        
        
        AnnenMatrikkelenhet --> "1" Matrikkelnummer : identifiseres_med
        click Matrikkelnummer href "../Matrikkelnummer/"
    

        
      AnnenMatrikkelenhet : ligger_innenfor_kommune
        
          
    
        
        
        AnnenMatrikkelenhet --> "1" Kommune : ligger_innenfor_kommune
        click Kommune href "../Kommune/"
    

        
      
```





## Inheritance
* [Matrikkelenhet](matrikkelenhet.md)
    * **AnnenMatrikkelenhet**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngre:AnnenMatrikkelenhet](https://data.norge.no/vocabulary/ngr-eiendom#AnnenMatrikkelenhet) |


## Eigenskapar























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
| [EiendomContainer](eiendomcontainer.md) | [andreMatrikkelenheter](andrematrikkelenheter.md) | range | [AnnenMatrikkelenhet](annenmatrikkelenhet.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:AnnenMatrikkelenhet |
| native | https://data.norge.no/ngr/ngr-eiendom/AnnenMatrikkelenhet |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AnnenMatrikkelenhet
description: Matrikkelenheit som ikkje fell inn under dei andre underklassane.
from_schema: https://data.norge.no/ngr/ngr-eiendom
rank: 1000
is_a: Matrikkelenhet
class_uri: ngre:AnnenMatrikkelenhet

```
</details>

### Induced

<details>
```yaml
name: AnnenMatrikkelenhet
description: Matrikkelenheit som ikkje fell inn under dei andre underklassane.
from_schema: https://data.norge.no/ngr/ngr-eiendom
rank: 1000
is_a: Matrikkelenhet
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ngr/ngr-eiendom
    rank: 1000
    identifier: true
    owner: AnnenMatrikkelenhet
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
    from_schema: https://data.norge.no/ngr/ngr-eiendom
    rank: 1000
    slot_uri: ngre:identifiseresMed
    owner: AnnenMatrikkelenhet
    domain_of:
    - Matrikkelenhet
    range: Matrikkelnummer
    required: true
  ligger_innenfor_kommune:
    name: ligger_innenfor_kommune
    description: Kommunen matrikkeleininga ligg innanfor.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/ngr/ngr-eiendom
    rank: 1000
    slot_uri: ngre:liggerInnenforKommune
    owner: AnnenMatrikkelenhet
    domain_of:
    - Matrikkelenhet
    range: Kommune
    required: true
  er_del_av_teig:
    name: er_del_av_teig
    description: Teigen(e) matrikkeleininga er del av.
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ngr/ngr-eiendom
    rank: 1000
    slot_uri: ngre:erDelAvTeig
    owner: AnnenMatrikkelenhet
    domain_of:
    - Matrikkelenhet
    range: Teig
    multivalued: true
  har_teig:
    name: har_teig
    description: Teigen(e) som tilhøyrer matrikkeleininga.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ngr/ngr-eiendom
    rank: 1000
    slot_uri: ngre:harTeig
    owner: AnnenMatrikkelenhet
    domain_of:
    - Matrikkelenhet
    range: Teig
    multivalued: true
  har_anleggsprojeksjonsflate:
    name: har_anleggsprojeksjonsflate
    description: Anleggsprojeksjonsflata (fotavtrykket) for anleggseigedommen.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ngr/ngr-eiendom
    rank: 1000
    slot_uri: ngre:harAnleggsprojeksjonsflate
    owner: AnnenMatrikkelenhet
    domain_of:
    - Matrikkelenhet
    range: Anleggsprojeksjonsflate
class_uri: ngre:AnnenMatrikkelenhet

```
</details>