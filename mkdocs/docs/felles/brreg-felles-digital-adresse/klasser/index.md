# BRREG felles digital adresse

## Modellmetadata

> Modellmetadata viser sentrale metadata for modellen, inkludert versjon, status, lisens, identifikatorar og avhengigheiter. Verdiane er henta direkte frå skjemaet.

| Felt | Verdi |
| --- | --- |
| Name | brreg-felles-digital-adresse |
| Title | BRREG felles digital adresse |
| Description | Gjenbrukbare digitale adresseklassar utleia frå Brønnøysundregistrene (BR) sin interne BRReferansemodell_v3 (MagicDraw/XMI), pakken "Adresse" (DigitalAdresse-hierarkiet). Sjå specs/done/felles-typar-enhetsregisteret-fra-br-katalogar.md for bakgrunn, metode og avklaringane denne modellen byggjer på.
BR sin eigen `Nettadresse`-undertype "Aksesspunkt" er medvite utelaten her: feltet `aksesspunktoperatoer` peikar til `Virksomhet` (definert i brreg-felles-aktoer, som importerer denne modellen) og ville gjort importgrafen sirkulær. Sjå nemnde spec § Funn 4. |
| Schema URI | [https://data.norge.no/felles/brreg-felles-digital-adresse](https://data.norge.no/felles/brreg-felles-digital-adresse) |
| Versjon | 0.1.0 |
| Lisens | [https://data.norge.no/nlod/no/2.0](https://data.norge.no/nlod/no/2.0) |
| Utgiver | [https://data.norge.no/organizations/974760673](https://data.norge.no/organizations/974760673) |
| Status | [http://purl.org/adms/status/UnderDevelopment](http://purl.org/adms/status/UnderDevelopment) |
| Endringsdato | 2026-09-01 |
| Utgivelsesdato | 2026-09-01 |
| Imports | `linkml:types`<br>`../brreg-felles-typer/brreg-felles-typer-schema` |


### Classes (7)

> Classes viser klasser som er definerte lokalt i brreg-felles-digital-adresse modellen. 
> Klasser frå importerte modellar er ikkje inkluderte i teljinga, men kan vere refererte frå lokale klasser og kan inngå i valideringsresultat og diagram.  
> Klasser grupperes i Obligatorisk, Anbefalt, Valgfri og Andre (uklassifisert).

#### Andre (7)

| Class | Description |
| --- | --- |
| [DigitalAdresse](digitaladresse.md) | Ei digital adresse. Abstrakt basisklasse for dei konkrete digitale adressetypane under. |
| [EPostadresse](epostadresse.md) | Ei e-postadresse, delt opp i brukarnamn og domenenavn. |
| [IPAdresse](ipadresse.md) | Ei IP-adresse. |
| [Meldingsboks](meldingsboks.md) | Ei digital meldingsboks (t.d. Altinn). |
| [Mobiltelefonnummer](mobiltelefonnummer.md) | Eit mobiltelefonnummer. |
| [Nettadresse](nettadresse.md) | Ei nettadresse (protokoll, domenenavn og filsti). |
| [Telefonnummer](telefonnummer.md) | Eit fasttelefonnummer. |

### Slots (11)

> Slots viser **eigenskapar** som er definert i eller brukt av lokale klasser i modellen.  
> Eigenskapar grupperes i "Verdiar" som inneheld data, og "Refransar" som refererer til andre klasser.  
> *Defined in* kolonna angir kildeskjemaet for eigenskapen.
#### Verdiar (11)

| Slot | Description | Defined in |
| --- | --- | --- |
| [brukernavn](brukernavn.md) | Brukarnamnet (lokaldelen) i e-postadressa. | [https://data.norge.no/felles/brreg-felles-digital-adresse](https://data.norge.no/felles/brreg-felles-digital-adresse) |
| [digital_adresse_id](digital_adresse_id.md) | URI-identifikator for ressursen. | [https://data.norge.no/felles/brreg-felles-digital-adresse](https://data.norge.no/felles/brreg-felles-digital-adresse) |
| [digital_adresse_type](digital_adresse_type.md) | Diskriminator for kva slag adresse dette er. | [https://data.norge.no/felles/brreg-felles-digital-adresse](https://data.norge.no/felles/brreg-felles-digital-adresse) |
| [domenenavn](domenenavn.md) | Domenenamnet i adressa. | [https://data.norge.no/felles/brreg-felles-digital-adresse](https://data.norge.no/felles/brreg-felles-digital-adresse) |
| [filsti](filsti.md) | Filstien i nettadressa. | [https://data.norge.no/felles/brreg-felles-digital-adresse](https://data.norge.no/felles/brreg-felles-digital-adresse) |
| [identifikator](identifikator.md) | Generisk identifikator (form varierer per samanheng — brukt både for digitale adresser og, via brreg-felles-aktoer, for aktørar generelt). | [https://data.norge.no/felles/brreg-felles-digital-adresse](https://data.norge.no/felles/brreg-felles-digital-adresse) |
| [ip_nummer](ip_nummer.md) | IP-nummeret. | [https://data.norge.no/felles/brreg-felles-digital-adresse](https://data.norge.no/felles/brreg-felles-digital-adresse) |
| [meldingsbokstype](meldingsbokstype.md) | Kva type digital meldingsboks dette er (t.d. Altinn). | [https://data.norge.no/felles/brreg-felles-digital-adresse](https://data.norge.no/felles/brreg-felles-digital-adresse) |
| [nasjonalt_nummer](nasjonalt_nummer.md) | Telefonnummeret utan landkode/prefiks. | [https://data.norge.no/felles/brreg-felles-digital-adresse](https://data.norge.no/felles/brreg-felles-digital-adresse) |
| [prefiks_med_nasjonal_kode](prefiks_med_nasjonal_kode.md) | Internasjonalt telefonprefiks (landkode), t.d. "+47". | [https://data.norge.no/felles/brreg-felles-digital-adresse](https://data.norge.no/felles/brreg-felles-digital-adresse) |
| [protokoll](protokoll.md) | Protokollen for nettadressa, t.d. https. | [https://data.norge.no/felles/brreg-felles-digital-adresse](https://data.norge.no/felles/brreg-felles-digital-adresse) |


### Enumerations (0)

> Enumerations viser kontrollerte **verdiområder** som er definert i eller brukt lokalt i modellen.  
> *Defined in* kolonna angir kildeskjemaet for verdiområdet.


*Ingen enumerations definert lokalt eller brukt i denne modellen.*


### Types (4)

> Types viser primitive **verdiformat** som datoar, URI-ar, språkstrengar og andre grunnleggjande datatypar som er definert i eller brukt i modellen.  
> *Defined in* kolonna angir kildeskjemaet for verdiformatet.

| Type | URI | Description | Defined in |
| --- | --- | --- | --- |
| NasjonaltNummer | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Telefonnummer utan landkode/prefiks. | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| PrefiksMedNasjonalKode | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Internasjonalt telefonprefiks (landkode), t.d. "+47". | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| string | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | A character string | [linkml:types](https://github.com/linkml/linkml-model/blob/main/linkml_model/model/schema/types.yaml) |
| uriorcurie | [xsd:anyURI](https://www.w3.org/TR/xmlschema11-2/#anyURI) | a URI or a CURIE | [linkml:types](https://github.com/linkml/linkml-model/blob/main/linkml_model/model/schema/types.yaml) |
### Subsets (0)

> Subsets viser **klassifiseringar** av klasser og slots som blir brukt i modellen. For AP-NO-modellar vil dette typisk vere Obligatorisk, Anbefalt og Valgfri.  
> *Defined in* kolonna angir kildeskjemaet for klassifiseringa.

*Ingen subsets definert lokalt eller brukt i denne modellen.*
