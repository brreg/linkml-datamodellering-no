# Nasjonale grunndata – Adresse

Domenemodell for norske adressar basert på Nasjonale grunndata (utkast). Modellerer Offisiell adresse og Postboksadresse med tilhøyrande geografiske inndelingar og adressekomponentar. Basert på https://informasjonsforvaltning.github.io/nasjonale-grunndata/#Adresse

URI: https://data.norge.no/linkml/ngr-adresse

Name: ngr-adresse



## Classes





### Obligatorisk

| Class | Description |
| --- | --- |
| [Adressekode](adressekode.md) | Firesifra kommunal kode som identifiserer eit adressenavn |
| [Adressenavn](adressenavn.md) | Offisielt namn på ei veglenke eller eit adresseobjekt i ein kommune, tildelt ... |
| [Bruksenhetsnummer](bruksenhetsnummer.md) | Identifikator for ei brukseining (leilegheit o |
| [Fylke](fylke.md) | Eit norsk fylke |
| [Husnummer](husnummer.md) | Husnummer beståande av eit obligatorisk nummer og ein valfri bokstav (t |
| [Kommune](kommune.md) | Ein norsk kommune |
| [OffisiellAdresse](offisielladresse.md) | Ei offisiell adresse tildelt av kommunen, beståande av vegadresse (adressenav... |
| [Postboks](postboks.md) | Ei postboks registrert i Postboksregisteret |
| [Postboksadresse](postboksadresse.md) | Ei postboksadresse registrert i Postboksregisteret (Posten Norge) |
| [Poststed](poststed.md) | Eit poststed identifisert med postnummer, forvalta av Postnummerregisteret |
| [Representasjonspunkt](representasjonspunkt.md) | Eit geografisk punkt (koordinatpar) som representerer posisjonen til adressa |








### Andre

| Class | Description |
| --- | --- |
| [Adresseomrade](adresseomrade.md) | Geografisk område eit adressenavn høyrer til, t |
| [Bruksenhet](bruksenhet.md) | Referanse til ei brukseining (leilegheit/lokale) i Matrikkelen |
| [Bygning](bygning.md) | Referanse til ein bygning i Matrikkelen |
| [GeografiskAdresse](geografiskadresse.md) | Abstrakt basisklasse for norske adressar |
| [GeografiskOmrade](geografiskomrade.md) | Abstrakt klasse for geografiske inndelingar som offisielle adressar refererer... |
| [Grunnkrets](grunnkrets.md) | Ei grunnkrets – minste geografiske eining i statistisk inndeling |
| [Kirkesokn](kirkesokn.md) | Eit kyrkjesokn |
| [KommunalKrets](kommunalkrets.md) | Ein kommunal krets (administrativ inndeling definert av kommunen) |
| [Stemmekrets](stemmekrets.md) | Ei stemmekrets brukt ved val |
| [Svalbard](svalbard.md) | Svalbard som særskild geografisk område |
| [Tettsted](tettsted.md) | Eit tettbygd område definert av SSB |





## Slots

| Slot | Description |
| --- | --- |
| [adressekode_ref](adressekode_ref.md) | Kommunal adressekode for adressa |
| [adressekoder](adressekoder.md) |  |
| [adressenavn](adressenavn.md) |  |
| [adressenavn_ref](adressenavn_ref.md) | Adressenavn (vegnamn o |
| [adressenavn_tekst](adressenavn_tekst.md) | Tekstleg namn på vegen eller stadnamnet (locn:thoroughfare) |
| [adresseomrade_ref](adresseomrade_ref.md) | Adresseområdet dette adressenamnet eller adressekoden høyrer til |
| [adresseomrader](adresseomrader.md) |  |
| [adresserer_annet_objekt](adresserer_annet_objekt.md) | Anna objekt (t |
| [adresserer_bruksenhet](adresserer_bruksenhet.md) | Brukseining denne adressa er tildelt (forvaltar: Matrikkelen) |
| [adresserer_bygning](adresserer_bygning.md) | Bygning denne adressa er tildelt (forvaltar: Matrikkelen) |
| [adressetilleggsnavn](adressetilleggsnavn.md) | Offisielt tilleggsnamn til vegadressa (t |
| [bokstav](bokstav.md) | Husbokstav (A–Å) som skil einingar med same husnummer |
| [bruksenheter](bruksenheter.md) |  |
| [bruksenhetsnummer](bruksenhetsnummer.md) |  |
| [bruksenhetsnummer_ref](bruksenhetsnummer_ref.md) | Bruksenhetsnummer for leilegheit eller lokale |
| [bygningar](bygningar.md) |  |
| [etasjenummer](etasjenummer.md) | Etasjenummer (t |
| [etasjeplan](etasjeplan.md) | Kode for kva del av bygningen brukseininga ligg i (H/U/K/L/M) |
| [fylke](fylke.md) |  |
| [fylkesnummer](fylkesnummer.md) | Tosifra fylkesnummer (t |
| [geografisk_omrade](geografisk_omrade.md) | Geografiske inndelingar (kommune, poststed, grunnkrets osv |
| [grunnkretsar](grunnkretsar.md) |  |
| [grunnkretsnummer](grunnkretsnummer.md) | Åttesifra grunnkretsnummer (kommunenummer + firesifra kretsnummer) |
| [har_adressekode](har_adressekode.md) | Adressekode tilknytt dette adressenamnet |
| [husnummer](husnummer.md) |  |
| [husnummer_ref](husnummer_ref.md) | Husnummer (nummer + bokstav) for adressa |
| [id](id.md) | URI-identifikator for ressursen |
| [kirkesokn](kirkesokn.md) |  |
| [kirkesoknnummer](kirkesoknnummer.md) | Kysokn-nummer frå Kyrkja |
| [kode](kode.md) | Numerisk kode for adressekoden (kommunal firesifra kode) |
| [kommunaleKretsar](kommunalekretsar.md) |  |
| [kommunar](kommunar.md) |  |
| [kommunenummer_kode](kommunenummer_kode.md) | Firesifra kommunenummer (t |
| [kommunenummer_ref](kommunenummer_ref.md) | Kommunen denne adressa ligg i |
| [koordinat_nord](koordinat_nord.md) | Nordleg koordinat (Y) i det angitte koordinatsystemet |
| [koordinat_ost](koordinat_ost.md) | Austleg koordinat (X) i det angitte koordinatsystemet |
| [koordinatsystem](koordinatsystem.md) | Koordinatsystem/projeksjon (t |
| [kretsnummer](kretsnummer.md) | Kommunalt kretsnummer |
| [matrikkelnummer](matrikkelnummer.md) | Matrikkelnummer for adresser utan vegadresse (t |
| [namn](namn.md) | Namn på det geografiske området eller adressekomponenten |
| [nummer](nummer.md) | Husnummeret (heltalsverdi) |
| [nummerering_i_etasjen](nummerering_i_etasjen.md) | Løpenummer for brukseininga innanfor etasjen |
| [offisielleAdresser](offisielleadresser.md) |  |
| [postboks_ref](postboks_ref.md) | Postboksen denne postboksadressa tilhøyrer |
| [postboksadresser](postboksadresser.md) |  |
| [postboksanleggsnavn](postboksanleggsnavn.md) | Namn på postboksanlegget (t |
| [postboksar](postboksar.md) |  |
| [postboksnummer](postboksnummer.md) | Postboksnummer (heiltal) |
| [postnummer](postnummer.md) | Firesifra postnummer (locn:postCode) |
| [poststed_ref](poststed_ref.md) | Poststedet (postnummer) denne adressa høyrer til |
| [poststeder](poststeder.md) |  |
| [representasjonspunkt](representasjonspunkt.md) |  |
| [representasjonspunkt_ref](representasjonspunkt_ref.md) | Geografisk punkt som representerer adressas posisjon |
| [stemmekretsar](stemmekretsar.md) |  |
| [stemmekretsnummer](stemmekretsnummer.md) | Stemmekretsnummer |
| [svalbardOmrader](svalbardomrader.md) |  |
| [tettstadar](tettstadar.md) |  |
| [tettstedsnummer](tettstedsnummer.md) | SSB-tettstedsnummer |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [Etasjeplan](etasjeplan.md) | Kode for kva del av bygningen eit bruksenhetsnummer refererer til |


## Types

| Type | Description |
| --- | --- |


## Subsets

| Subset | Description |
| --- | --- |
| [Anbefalt](anbefalt.md) | Anbefalte eigenskapar i domenemodellen |
| [Obligatorisk](obligatorisk.md) | Obligatoriske eigenskapar i domenemodellen |
| [Valgfri](valgfri.md) | Valfrie eigenskapar i domenemodellen |
