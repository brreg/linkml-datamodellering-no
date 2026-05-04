# Nasjonale grunndata – Adresse

Domenemodell for norske adressar basert på Nasjonale grunndata (utkast). Modellerer Offisiell adresse og Postboksadresse med tilhøyrande geografiske inndelingar og adressekomponentar. Basert på https://informasjonsforvaltning.github.io/nasjonale-grunndata/#Adresse

URI: https://data.norge.no/linkml/ngr-adresse

Name: ngr-adresse



## Classes

| Class | Description |
| --- | --- |
| [AdresseContainer](AdresseContainer.md) | Rotklasse for NGR-adresse-datafiler |
| [Adressekode](Adressekode.md) | Firesifra kommunal kode som identifiserer eit adressenavn |
| [Adressenavn](Adressenavn.md) | Offisielt namn på ei veglenke eller eit adresseobjekt i ein kommune, tildelt ... |
| [Adresseomrade](Adresseomrade.md) | Geografisk område eit adressenavn høyrer til, t |
| [Bruksenhet](Bruksenhet.md) | Referanse til ei brukseining (leilegheit/lokale) i Matrikkelen |
| [Bruksenhetsnummer](Bruksenhetsnummer.md) | Identifikator for ei brukseining (leilegheit o |
| [Bygning](Bygning.md) | Referanse til ein bygning i Matrikkelen |
| [GeografiskAdresse](GeografiskAdresse.md) | Abstrakt basisklasse for norske adressar |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OffisiellAdresse](OffisiellAdresse.md) | Ei offisiell adresse tildelt av kommunen, beståande av vegadresse (adressenav... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Postboksadresse](Postboksadresse.md) | Ei postboksadresse registrert i Postboksregisteret (Posten Norge) |
| [GeografiskOmrade](GeografiskOmrade.md) | Abstrakt klasse for geografiske inndelingar som offisielle adressar refererer... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fylke](Fylke.md) | Eit norsk fylke |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Grunnkrets](Grunnkrets.md) | Ei grunnkrets – minste geografiske eining i statistisk inndeling |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kirkesokn](Kirkesokn.md) | Eit kyrkjesokn |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[KommunalKrets](KommunalKrets.md) | Ein kommunal krets (administrativ inndeling definert av kommunen) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kommune](Kommune.md) | Ein norsk kommune |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Poststed](Poststed.md) | Eit poststed identifisert med postnummer, forvalta av Postnummerregisteret |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Stemmekrets](Stemmekrets.md) | Ei stemmekrets brukt ved val |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Svalbard](Svalbard.md) | Svalbard som særskild geografisk område |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Tettsted](Tettsted.md) | Eit tettbygd område definert av SSB |
| [Husnummer](Husnummer.md) | Husnummer beståande av eit obligatorisk nummer og ein valfri bokstav (t |
| [Postboks](Postboks.md) | Ei postboks registrert i Postboksregisteret |
| [Representasjonspunkt](Representasjonspunkt.md) | Eit geografisk punkt (koordinatpar) som representerer posisjonen til adressa |



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
| [kommunaleKretsar](kommunaleKretsar.md) |  |
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
| [offisielleAdresser](offisielleAdresser.md) |  |
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
| [svalbardOmrader](svalbardOmrader.md) |  |
| [tettstadar](tettstadar.md) |  |
| [tettstedsnummer](tettstedsnummer.md) | SSB-tettstedsnummer |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [Etasjeplan](Etasjeplan.md) | Kode for kva del av bygningen eit bruksenhetsnummer refererer til |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
| [Anbefalt](Anbefalt.md) | Anbefalte eigenskapar i domenemodellen |
| [Obligatorisk](Obligatorisk.md) | Obligatoriske eigenskapar i domenemodellen |
| [Valgfri](Valgfri.md) | Valfrie eigenskapar i domenemodellen |
