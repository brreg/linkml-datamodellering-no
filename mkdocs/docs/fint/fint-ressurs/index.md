# fint-ressurs

```mermaid
erDiagram
Applikasjon {
    uriorcurie id  
    string beskrivelse  
    string navn  
}
Applikasjonskategori {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Applikasjonsressurs {
    uriorcurie id  
    string beskrivelse  
    uriorcurie eier  
    integer enhetskostnad  
    boolean kreverGodkjenning  
    integer lisensantall  
    string navn  
}
Applikasjonsressurstilgjengelighet {
    uriorcurie id  
    uriorcurie konsument  
    integer lisensantall  
}
Brukertype {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
DigitalEnhet {
    uriorcurie id  
    uriorcurie administrator  
    uriorcurie eier  
    boolean flerbrukerenhet  
    string navn  
    uriorcurie personalressurs  
    boolean privateid  
    string serienummer  
}
Enhetsgruppe {
    uriorcurie id  
    string navn  
    uriorcurie organisasjonsenhet  
}
Enhetsgruppemedlemskap {
    uriorcurie id  
}
Enhetstype {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Handhevingstype {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Identitet {
    uriorcurie id  
    uriorcurie personalressurs  
}
Lisensmodell {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Plattform {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Produsent {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Rettighet {
    uriorcurie id  
    string beskrivelse  
    string kode  
    string navn  
    boolean passiv  
}
Status {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}

Applikasjon ||--}o Applikasjonskategori : "applikasjonskategori"
Applikasjon ||--}o Applikasjonsressurs : "applikasjonsressurs"
Applikasjon ||--}o Plattform : "plattform"
Applikasjonsressurs ||--|o Handhevingstype : "handhevingstype"
Applikasjonsressurs ||--|o Lisensmodell : "lisensmodell"
Applikasjonsressurs ||--|| Applikasjon : "applikasjon"
Applikasjonsressurs ||--}o Applikasjonsressurstilgjengelighet : "ressurstilgjengelighet"
Applikasjonsressurs ||--}| Brukertype : "brukertype"
Applikasjonsressurstilgjengelighet ||--|| Applikasjonsressurs : "ressursRef"
DigitalEnhet ||--|o Produsent : "produsent"
DigitalEnhet ||--|o Status : "status"
DigitalEnhet ||--|| Enhetstype : "enhetstype"
DigitalEnhet ||--|| Plattform : "plattform"
DigitalEnhet ||--}o Enhetsgruppemedlemskap : "enhetsgruppemedlemskap"
Enhetsgruppe ||--|| Enhetstype : "enhetstype"
Enhetsgruppe ||--|| Plattform : "plattform"
Enhetsgruppe ||--}o Enhetsgruppemedlemskap : "enhetsgruppemedlemskap"
Enhetsgruppemedlemskap ||--|| DigitalEnhet : "digitalEnhet"
Enhetsgruppemedlemskap ||--|| Enhetsgruppe : "enhetsgruppe"
Identitet ||--}o Rettighet : "rettighet"
Rettighet ||--}o Identitet : "identitet"


```


FINT-domenemodell for ressursstyring. Dekkjer tre sub-pakkar: ressurs.eiendel (applikasjonar og lisensressursar), ressurs.datautstyr (digitale einingar og einingsgrupper) og ressurs.tilgang (identitetar og rettigheiter).


URI: https://data.norge.no/fint/fint-ressurs

Name: fint-ressurs



## Classes







### Obligatorisk

| Class | Description |
| --- | --- |
| [Applikasjon](klasser/applikasjon.md) | Ein applikasjon med tilhøyrande ressursar |
| [Applikasjonsressurs](klasser/applikasjonsressurs.md) | Informasjon om kor ein applikasjon kan nyttast (lisensressurs) |
| [Applikasjonsressurstilgjengelighet](klasser/applikasjonsressurstilgjengelighet.md) | Kva organisasjonselements brukarar som har tilgang til ein ressurs |
| [DigitalEnhet](klasser/digitalenhet.md) | Ei digital eining som t |
| [Enhetsgruppe](klasser/enhetsgruppe.md) | Ei gruppering av einsarta digitale einingar |
| [Enhetsgruppemedlemskap](klasser/enhetsgruppemedlemskap.md) | Medlemskap mellom ei digital eining og ei einingsgruppe |
| [Rettighet](klasser/rettighet.md) | Ei namngitt rettighet |






### Valgfri

| Class | Description |
| --- | --- |
| [Applikasjonskategori](klasser/applikasjonskategori.md) | Kategori av applikasjonar |
| [Brukertype](klasser/brukertype.md) | Dei ulike brukartypane som kan nytte lisensen |
| [Enhetstype](klasser/enhetstype.md) | Type digital eining |
| [Handhevingstype](klasser/handhevingstype.md) | Korleis ulike lisensmodellar kan handhevast |
| [Identitet](klasser/identitet.md) | Identitet som identifiserer innehavaren av rettigheiter i organisasjonen |
| [Lisensmodell](klasser/lisensmodell.md) | Lisensmodellar som kan knytast til ein lisens |
| [Plattform](klasser/plattform.md) | Plattforma tenesta kan leverast på |
| [Produsent](klasser/produsent.md) | Produsent av ei digital eining |
| [Status](klasser/status.md) | Status på ei digital eining i fagsystemet |







## Slots

| Slot | Description |
| --- | --- |
| [administrator](klasser/administrator.md) | Referanse til Organisasjonselement som administrerer eininga |
| [applikasjon](klasser/applikasjon.md) | Applikasjonen ressursen (lisensen) er knytt til |
| [applikasjonskategori](klasser/applikasjonskategori.md) | Kategoriar av applikasjonar |
| [applikasjonsressurs](klasser/applikasjonsressurs.md) | Ulike ressursar (lisensar) knytt til ein applikasjon |
| [brukertype](klasser/brukertype.md) | For kva brukertypar lisensen er gyldig |
| [dataobjektId](klasser/dataobjektid.md) | Einingsens ID i datakatalogen |
| [digitalEnhet](klasser/digitalenhet.md) | Den digitale eininga dette medlemskapet tilhøyrer |
| [eier](klasser/eier.md) | Referanse til Organisasjonselement som har eigarskap |
| [enhetsgruppe](klasser/enhetsgruppe.md) | Einingsgruppen dette medlemskapet tilhøyrer |
| [enhetsgruppemedlemskap](klasser/enhetsgruppemedlemskap.md) | Einingsgruppemelemskap |
| [enhetskostnad](klasser/enhetskostnad.md) | Kostnad per ressurs |
| [enhetstype](klasser/enhetstype.md) | Type digital eining |
| [flerbrukerenhet](klasser/flerbrukerenhet.md) | Kvifor eininga er ein- eller flerbrukarenheit |
| [handhevingstype](klasser/handhevingstype.md) | Korleis lisensmodellen skal handhevast |
| [identitet](klasser/identitet.md) | Identitetar knytt til rettigheta |
| [konsument](klasser/konsument.md) | Referanse til Organisasjonselement som har tilgang til ressursen |
| [kreverGodkjenning](klasser/krevergodkjenning.md) | True dersom tildeling av ressursen krev godkjenning |
| [lisensantall](klasser/lisensantall.md) | Totalt tal på lisensar |
| [lisensmodell](klasser/lisensmodell.md) | Lisensmodellen applikasjonsressursen har |
| [organisasjonsenhet](klasser/organisasjonsenhet.md) | Referanse til Organisasjonselement grupperinga er tilknytt |
| [personalressurs](klasser/personalressurs.md) | Referanse til Personalressurs (Administrasjon) |
| [plattform](klasser/plattform.md) | Plattforma ressursen er knytt til |
| [privateid](klasser/privateid.md) | Angir om eininga er eigd av organisasjonen eller privatperson |
| [produsent](klasser/produsent.md) | Namn på produsenten av eininga |
| [ressursRef](klasser/ressursref.md) | Ressursen organisasjonselementet har tilgang til |
| [ressurstilgjengelighet](klasser/ressurstilgjengelighet.md) | Angir kva organisasjonseining og kor mange ressursar som skal tilordnast |
| [rettighet](klasser/rettighet.md) | Rettigheiter knytt til identiteten |
| [serienummer](klasser/serienummer.md) | Unikt serienummer frå einingsprodusentens |
| [status](klasser/status.md) | Status på eininga i fagsystemet |


## Enumerations

| Enumeration | Description |
| --- | --- |


## Types

| Type | Description |
| --- | --- |


## Subsets

| Subset | Description |
| --- | --- |
| [Anbefalt](klasser/anbefalt.md) | Anbefalt eigensskap |
| [Obligatorisk](klasser/obligatorisk.md) | Obligatorisk eigensskap |
| [Valgfri](klasser/valgfri.md) | Valfri eigensskap |


## Generated artifacts

| Artefakt | Fil |
|----------|-----|
| SHACL shapes | [fint-ressurs-shapes.ttl](fint-ressurs-shapes.ttl) |
| JSON-LD kontekst | [fint-ressurs-context.jsonld](fint-ressurs-context.jsonld) |
| JSON Schema | [fint-ressurs-schema.json](fint-ressurs-schema.json) |
| OWL ontologi | [fint-ressurs-ontology.ttl](fint-ressurs-ontology.ttl) |
| Python-klasser | [fint-ressurs-model.py](fint-ressurs-model.py) |
| Protobuf-skjema | [fint-ressurs-schema.proto](fint-ressurs-schema.proto) |
| ER-diagram (Mermaid) | [fint-ressurs-erdiagram.md](fint-ressurs-erdiagram.md) |
| Eksempeldata (Turtle) | [fint-ressurs-eksempel.ttl](fint-ressurs-eksempel.ttl) |
| PlantUML-diagram | [fint-ressurs.svg](diagrams/fint-ressurs.svg) · [fint-ressurs.puml](diagrams/fint-ressurs.puml) |
