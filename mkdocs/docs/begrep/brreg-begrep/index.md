# brreg-begrep

```mermaid
erDiagram
AssosiativRelasjon {
    uriorcurie id  
    LangString relasjontype  
}
Begrep {
    uriorcurie id  
    LangStringList anbefalt_term  
    stringList datastruktur_term  
    LangStringList definisjon  
    LangStringList eksempel  
    date endringsdato  
    LangStringList forkasta_term  
    date gyldig_fra  
    date gyldig_til  
    string har_versjonsnummer  
    string identifikator_literal  
    LangStringList merknad  
    date opprettingsdato  
    LangStringList tillate_term  
    LangStringList verdiomrade  
    LangStringList versjonsmerknad  
}
Definisjon {
    uriorcurie id  
    uriList kjelde  
    LangString tekst  
}
GeneriskRelasjon {
    uriorcurie id  
    LangStringList inndelingskriterium  
}
Organisasjon {
    uriorcurie id  
}
PartitivRelasjon {
    uriorcurie id  
    LangStringList inndelingskriterium  
}
Samling {
    uriorcurie id  
    LangStringList beskrivelse  
    string identifikator_literal  
    LangStringList tittel  
}
VCardKontakt {
    uriorcurie id  
}

AssosiativRelasjon ||--}| Begrep : "til_omgrep"
Begrep ||--|o Begrep : "euvoc_status"
Begrep ||--|o Organisasjon : "ansvarleg_verksemd"
Begrep ||--|| Organisasjon : "utgjevar"
Begrep ||--}o AssosiativRelasjon : "er_fra_omgrep_i"
Begrep ||--}o Begrep : "assosiert_med, er_del_av_omgrep, er_erstatta_av, erstattar, fagomrade, generaliserer, har_del_omgrep, naert_samsvar, noyaktig_samsvar, sja_ogsa_omgrep, spesifiserer"
Begrep ||--}o Definisjon : "har_definisjon"
Begrep ||--}o GeneriskRelasjon : "har_generisk_relasjon"
Begrep ||--}o PartitivRelasjon : "har_partitiv_relasjon"
Begrep ||--}o Samling : "er_medlem_av"
Begrep ||--}| VCardKontakt : "kontaktpunkt_vcard"
Definisjon ||--|o Begrep : "kjelde_relasjon, malgruppe_def"
GeneriskRelasjon ||--}o Begrep : "har_generisk_omgrep, har_spesifikt_omgrep"
PartitivRelasjon ||--}o Begrep : "har_heilskapleg_omgrep, har_partitivt_omgrep"
Samling ||--|| Organisasjon : "utgjevar"
Samling ||--}| Begrep : "medlem"
Samling ||--}| VCardKontakt : "kontaktpunkt_vcard"

```



Begrepskatalog for Registerenheten i Brønnøysund. Begreper modellert lokalt med midlertidige URI-ar, klare for validering og eksport til Felles Begrepskatalog.

URI: https://data.norge.no/linkml/brreg-begrep

Name: brreg-begrep



## Classes











### Andre

| Class | Description |
| --- | --- |





## Slots

| Slot | Description |
| --- | --- |
| [assosiative_relasjonar](klasser/assosiative_relasjonar.md) |  |
| [begrep](klasser/begrep.md) |  |
| [definisjoner](klasser/definisjoner.md) |  |
| [generiske_relasjonar](klasser/generiske_relasjonar.md) |  |
| [kontaktpunkt](klasser/kontaktpunkt.md) |  |
| [organisasjonar](klasser/organisasjonar.md) |  |
| [partitive_relasjonar](klasser/partitive_relasjonar.md) |  |
| [samlingar](klasser/samlingar.md) |  |


## Enumerations

| Enumeration | Description |
| --- | --- |


## Types

| Type | Description |
| --- | --- |


## Subsets

| Subset | Description |
| --- | --- |
| [Anbefalt](klasser/anbefalt.md) | Anbefalte eigenskapar i ein AP-NO-profil |
| [Obligatorisk](klasser/obligatorisk.md) | Obligatoriske eigenskapar i ein AP-NO-profil |
| [Valgfri](klasser/valgfri.md) | Valfrie eigenskapar i ein AP-NO-profil |


## Generated artifacts

| Artefakt | Fil |
|----------|-----|
| SHACL shapes | [brreg-begrep-shapes.ttl](brreg-begrep-shapes.ttl) |
| JSON-LD kontekst | [brreg-begrep-context.jsonld](brreg-begrep-context.jsonld) |
| JSON Schema | [brreg-begrep-schema.json](brreg-begrep-schema.json) |
| OWL ontologi | [brreg-begrep-ontology.ttl](brreg-begrep-ontology.ttl) |
| RDF/Turtle skjema | [brreg-begrep-schema.ttl](brreg-begrep-schema.ttl) |
| Python-klasser | [brreg-begrep-model.py](brreg-begrep-model.py) |
| Protobuf-skjema | [brreg-begrep-schema.proto](brreg-begrep-schema.proto) |
| ER-diagram (Mermaid) | [brreg-begrep-erdiagram.md](brreg-begrep-erdiagram.md) |
| Eksempeldata (Turtle) | [brreg-begrep-eksempel.ttl](brreg-begrep-eksempel.ttl) |
| PlantUML-diagram | [brreg-begrep.svg](diagrams/brreg-begrep.svg) · [brreg-begrep.puml](diagrams/brreg-begrep.puml) |
