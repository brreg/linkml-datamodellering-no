# fair-metadata

```mermaid
erDiagram
FAIRMetadata {
    uriorcurie id  
    uriorcurie beskrivelse  
    uriorcurie ressursIdentifikator  
    uriorcurie ressurstype  
}
Gjenbruksmetadata {
    string bruksavgrensingar  
    uriorcurie lisens  
    uriorcurieList standardoverensstemming  
    uriorcurieList vokabular  
}
Katalogregistrering {
    uriorcurie katalogOppfoeringURL  
    date registreringsdato  
    uriorcurie registrertIKatalog  
}
Proveniensmetadata {
    uriorcurie ansvarlegAktoer  
    date endringsdato  
    uriorcurie generertAvAktivitet  
    date opprettingsdato  
}
Tilgangsmetadata {
    boolean autentiseringPaakrevd  
    boolean metadataPersistens  
    uriorcurie tilgangsURL  
    string tilgangsprotokoll  
    uriorcurie tilgangsrettar  
}

FAIRMetadata ||--|o Gjenbruksmetadata : "gjenbruksmetadata"
FAIRMetadata ||--|o Katalogregistrering : "katalogregistrering"
FAIRMetadata ||--|o Proveniensmetadata : "proveniensmetadata"
FAIRMetadata ||--|o Tilgangsmetadata : "tilgangsmetadata"


```


FAIR metadata-overbygning som utfyllar norske applikasjonsprofilar for å sikre maskin-aksjonerbar FAIR-konformitet i tråd med FAIR-prinsippa (Findable, Accessible, Interoperable, Reusable).


URI: https://data.norge.no/fair/fair-metadata

Name: fair-metadata



## Classes













### Andre

| Class | Description |
| --- | --- |
| [FAIRMetadata](klasser/fairmetadata.md) | Maskin-aksjonerbar metadata som beskriver ein digital ressurs i tråd med FAIR... |
| [Gjenbruksmetadata](klasser/gjenbruksmetadata.md) | Metadata som støttar gjenbruk av ressursen (FAIR R1 |
| [Katalogregistrering](klasser/katalogregistrering.md) | Dokumenterer registrering i søkbar katalog (FAIR F4) |
| [Proveniensmetadata](klasser/proveniensmetadata.md) | Metadata om opphav og endringshistorie (FAIR R1 |
| [Tilgangsmetadata](klasser/tilgangsmetadata.md) | Metadata for tilgang, autentisering og tilgjengelegheit (FAIR A1/A2) |





## Slots

| Slot | Description |
| --- | --- |
| [ansvarlegAktoer](klasser/ansvarlegaktoer.md) | Organisasjon eller aktør som er ansvarleg for ressursen, som URI (FAIR R1 |
| [autentiseringPaakrevd](klasser/autentiseringpaakrevd.md) | Om autentisering eller autorisasjon er nødvendig (FAIR A1 |
| [beskrivelse](klasser/beskrivelse.md) | URI til ressursen som denne metadata-posten beskriver (FAIR F3) |
| [bruksavgrensingar](klasser/bruksavgrensingar.md) | Eventuelle juridiske eller praktiske bruksavgrensingar (FAIR R1 |
| [endringsdato](klasser/endringsdato.md) | Sist endra dato (FAIR R1 |
| [generertAvAktivitet](klasser/generertavaktivitet.md) | Aktivitet som har generert ressursen (FAIR R1 |
| [gjenbruksmetadata](klasser/gjenbruksmetadata.md) | Metadata som støttar gjenbruk av ressursen (FAIR R1 |
| [id](klasser/id.md) | Persistent URI-identifikator for metadata-posten (FAIR F1) |
| [katalogOppfoeringURL](klasser/katalogoppfoeringurl.md) | Direkte URL til oppføringa i katalogen (FAIR F4) |
| [katalogregistrering](klasser/katalogregistrering.md) | Dokumenterer registrering i søkbar katalog (FAIR F4) |
| [lisens](klasser/lisens.md) | Brukslisens for ressursen som URI (FAIR R1 |
| [metadataPersistens](klasser/metadatapersistens.md) | Metadata er tilgjengeleg sjølv om sjølve ressursen ikkje lenger er tilgjengel... |
| [opprettingsdato](klasser/opprettingsdato.md) | Dato ressursen blei oppretta (FAIR R1 |
| [proveniensmetadata](klasser/proveniensmetadata.md) | Metadata om opphav og endringshistorie (FAIR R1 |
| [registreringsdato](klasser/registreringsdato.md) | Dato for katalogregistrering (FAIR F4) |
| [registrertIKatalog](klasser/registrertikatalog.md) | URI til katalogen der metadata er registrert (FAIR F4) |
| [ressursIdentifikator](klasser/ressursidentifikator.md) | Global og persistent identifikator for ressursen (FAIR F1) |
| [ressurstype](klasser/ressurstype.md) | Type digital ressurs, t |
| [standardoverensstemming](klasser/standardoverensstemming.md) | Standardar eller profilar ressursen følgjer, t |
| [tilgangsmetadata](klasser/tilgangsmetadata.md) | Metadata for tilgang og tilgjengelegheit (FAIR A1/A2) |
| [tilgangsprotokoll](klasser/tilgangsprotokoll.md) | Kommunikasjonsprotokoll, t |
| [tilgangsrettar](klasser/tilgangsrettar.md) | Tilgangsnivå som URI, t |
| [tilgangsURL](klasser/tilgangsurl.md) | URL for maskinell tilgang til ressurs eller metadata (FAIR A1) |
| [vokabular](klasser/vokabular.md) | Kontrollerte vokabular eller ontologiar som ressursen brukar (FAIR I2) |


## Enumerations

| Enumeration | Description |
| --- | --- |


## Types

| Type | Description |
| --- | --- |


## Subsets

| Subset | Description |
| --- | --- |
| [Accessible](klasser/accessible.md) | Eigenskapar knytt til FAIR A-prinsippa (Accessible) |
| [Findable](klasser/findable.md) | Eigenskapar knytt til FAIR F-prinsippa (Findable) |
| [Interoperable](klasser/interoperable.md) | Eigenskapar knytt til FAIR I-prinsippa (Interoperable) |
| [Reusable](klasser/reusable.md) | Eigenskapar knytt til FAIR R-prinsippa (Reusable) |


## Generated artifacts

| Artefakt | Fil |
|----------|-----|
| SHACL shapes | [fair-metadata-shapes.ttl](fair-metadata-shapes.ttl) |
| JSON-LD kontekst | [fair-metadata-context.jsonld](fair-metadata-context.jsonld) |
| JSON Schema | [fair-metadata-schema.json](fair-metadata-schema.json) |
| OWL ontologi | [fair-metadata-ontology.ttl](fair-metadata-ontology.ttl) |
| RDF/Turtle skjema | [fair-metadata-schema.ttl](fair-metadata-schema.ttl) |
| Python-klasser | [fair-metadata-model.py](fair-metadata-model.py) |
| Protobuf-skjema | [fair-metadata-schema.proto](fair-metadata-schema.proto) |
| ER-diagram (Mermaid) | [fair-metadata-erdiagram.md](fair-metadata-erdiagram.md) |
| PlantUML-diagram | [fair-metadata.svg](diagrams/fair-metadata.svg) · [fair-metadata.puml](diagrams/fair-metadata.puml) |
