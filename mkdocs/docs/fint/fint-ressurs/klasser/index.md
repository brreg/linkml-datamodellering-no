# FINT Ressurs

FINT-domenemodell for ressursstyring. Dekkjer tre sub-pakkar: ressurs.eiendel (applikasjonar og lisensressursar), ressurs.datautstyr (digitale einingar og einingsgrupper) og ressurs.tilgang (identitetar og rettigheiter).


URI: https://data.norge.no/linkml/fint-ressurs

Name: fint-ressurs



## Classes





### Obligatorisk

| Class | Description |
| --- | --- |
| [Applikasjon](applikasjon.md) | Ein applikasjon med tilhøyrande ressursar |
| [Applikasjonsressurs](applikasjonsressurs.md) | Informasjon om kor ein applikasjon kan nyttast (lisensressurs) |
| [Applikasjonsressurstilgjengelighet](applikasjonsressurstilgjengelighet.md) | Kva organisasjonselements brukarar som har tilgang til ein ressurs |
| [DigitalEnhet](digitalenhet.md) | Ei digital eining som t |
| [Enhetsgruppe](enhetsgruppe.md) | Ei gruppering av einsarta digitale einingar |
| [Enhetsgruppemedlemskap](enhetsgruppemedlemskap.md) | Medlemskap mellom ei digital eining og ei einingsgruppe |
| [Rettighet](rettighet.md) | Ei namngitt rettighet |






### Valgfri

| Class | Description |
| --- | --- |
| [Applikasjonskategori](applikasjonskategori.md) | Kategori av applikasjonar |
| [Brukertype](brukertype.md) | Dei ulike brukartypane som kan nytte lisensen |
| [Enhetstype](enhetstype.md) | Type digital eining |
| [Handhevingstype](handhevingstype.md) | Korleis ulike lisensmodellar kan handhevast |
| [Identitet](identitet.md) | Identitet som identifiserer innehavaren av rettigheiter i organisasjonen |
| [Lisensmodell](lisensmodell.md) | Lisensmodellar som kan knytast til ein lisens |
| [Plattform](plattform.md) | Plattforma tenesta kan leverast på |
| [Produsent](produsent.md) | Produsent av ei digital eining |
| [Status](status.md) | Status på ei digital eining i fagsystemet |




### Andre

| Class | Description |
| --- | --- |





## Slots

| Slot | Description |
| --- | --- |
| [administrator](administrator.md) | Referanse til Organisasjonselement som administrerer eininga |
| [applikasjon](applikasjon.md) | Applikasjonen ressursen (lisensen) er knytt til |
| [applikasjonar](applikasjonar.md) |  |
| [applikasjonskategori](applikasjonskategori.md) | Kategoriar av applikasjonar |
| [applikasjonskategoriar](applikasjonskategoriar.md) |  |
| [applikasjonsressurs](applikasjonsressurs.md) | Ulike ressursar (lisensar) knytt til ein applikasjon |
| [applikasjonsressursar](applikasjonsressursar.md) |  |
| [applikasjonsressurstilgjengelegheit](applikasjonsressurstilgjengelegheit.md) |  |
| [brukertypar](brukertypar.md) |  |
| [brukertype](brukertype.md) | For kva brukertypar lisensen er gyldig |
| [dataobjektId](dataobjektid.md) | Einingsens ID i datakatalogen |
| [digitaleEiningar](digitaleeiningar.md) |  |
| [digitalEnhet](digitalenhet.md) | Den digitale eininga dette medlemskapet tilhøyrer |
| [eier](eier.md) | Referanse til Organisasjonselement som har eigarskap |
| [einingsgruppedmedlemskap](einingsgruppedmedlemskap.md) |  |
| [einingsgrupper](einingsgrupper.md) |  |
| [einingstypar](einingstypar.md) |  |
| [enhetsgruppe](enhetsgruppe.md) | Einingsgruppen dette medlemskapet tilhøyrer |
| [enhetsgruppemedlemskap](enhetsgruppemedlemskap.md) | Einingsgruppemelemskap |
| [enhetskostnad](enhetskostnad.md) | Kostnad per ressurs |
| [enhetstype](enhetstype.md) | Type digital eining |
| [flerbrukerenhet](flerbrukerenhet.md) | Kvifor eininga er ein- eller flerbrukarenheit |
| [handhaevingstypar](handhaevingstypar.md) |  |
| [handhevingstype](handhevingstype.md) | Korleis lisensmodellen skal handhevast |
| [identitet](identitet.md) | Identitetar knytt til rettigheta |
| [identitetar](identitetar.md) |  |
| [konsument](konsument.md) | Referanse til Organisasjonselement som har tilgang til ressursen |
| [kreverGodkjenning](krevergodkjenning.md) | True dersom tildeling av ressursen krev godkjenning |
| [lisensantall](lisensantall.md) | Totalt tal på lisensar |
| [lisensmodell](lisensmodell.md) | Lisensmodellen applikasjonsressursen har |
| [lisensmodellar](lisensmodellar.md) |  |
| [organisasjonsenhet](organisasjonsenhet.md) | Referanse til Organisasjonselement grupperinga er tilknytt |
| [personalressurs](personalressurs.md) | Referanse til Personalressurs (Administrasjon) |
| [plattform](plattform.md) | Plattforma ressursen er knytt til |
| [plattformar](plattformar.md) |  |
| [privateid](privateid.md) | Angir om eininga er eigd av organisasjonen eller privatperson |
| [produsent](produsent.md) | Namn på produsenten av eininga |
| [produsentar](produsentar.md) |  |
| [ressursRef](ressursref.md) | Ressursen organisasjonselementet har tilgang til |
| [ressurstilgjengelighet](ressurstilgjengelighet.md) | Angir kva organisasjonseining og kor mange ressursar som skal tilordnast |
| [rettigheiter](rettigheiter.md) |  |
| [rettighet](rettighet.md) | Rettigheiter knytt til identiteten |
| [serienummer](serienummer.md) | Unikt serienummer frå einingsprodusentens |
| [status](status.md) | Status på eininga i fagsystemet |
| [statusar](statusar.md) |  |


## Enumerations

| Enumeration | Description |
| --- | --- |


## Types

| Type | Description |
| --- | --- |


## Subsets

| Subset | Description |
| --- | --- |
| [Anbefalt](anbefalt.md) | Anbefalt eigensskap |
| [Obligatorisk](obligatorisk.md) | Obligatorisk eigensskap |
| [Valgfri](valgfri.md) | Valfri eigensskap |
