# DCAT-AP-NO

Norsk applikasjonsprofil av DCAT-AP, modellert i LinkML med lenking framfor inlining. Basert på https://informasjonsforvaltning.github.io/dcat-ap-no/

URI: https://data.norge.no/ap-no/dcat-ap-no

Name: dcat-ap-no



## Classes







### Obligatorisk

| Class | Description |
| --- | --- |
| [Aktor](aktor.md) | Ein aktør (person, organisasjon eller system) med ansvar for ein ressurs |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |
| [Datasettserie](datasettserie.md) | Ei serie av relaterte datasett publisert separat men med felles metadata |
| [Datatjeneste](datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |
| [Distribusjon](distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |
| [Identifikator](identifikator.md) | Ein alternativ identifikator for ein ressurs |
| [Katalog](katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre kata... |
| [Katalogpost](katalogpost.md) | Ein katalogpost som beskriv ein ressurs i katalogen |
| [Kontaktopplysning](kontaktopplysning.md) | Kontaktinformasjon for ein aktør |
| [Relasjon](relasjon.md) | Ein kvalifisert relasjon mellom to ressursar |
| [Sjekksum](sjekksum.md) | Ein sjekksum for ein distribusjon |








### Andre

| Class | Description |
| --- | --- |
| [Gebyr](gebyr.md) | Eit gebyr knytt til bruk av ein datatjeneste |
| [KatalogisertRessurs](katalogisertressurs.md) | Basisklasse for ressursar som kan katalogiserast |
| [RegulativRessurs](regulativressurs.md) | Ein regulativ ressurs (lov, forskrift o |
| [Rettighetserklaring](rettighetserklaring.md) | Ei erklæring om rettar til ein ressurs (ODRS) |
| [Tidsrom](tidsrom.md) | Eit tidsintervall med start- og sluttdato |





## Slots

| Slot | Description |
| --- | --- |
| [algoritme](algoritme.md) | Hash-algoritme brukt for sjekksummen |
| [annen_ansvarlig_aktor](annen_ansvarlig_aktor.md) | Kvalifisert attributering til ansvarleg aktør |
| [annen_identifikator](annen_identifikator.md) | Alternativ identifikator frå eit anna system |
| [annen_spesifikk_relasjon](annen_spesifikk_relasjon.md) | Kvalifisert relasjon til ein annan ressurs |
| [anvendelsesretningslinjer](anvendelsesretningslinjer.md) | Retningslinjer for gjenbruk av data |
| [begrep](begrep.md) | Fagomgrep som datasettet handlar om |
| [begynnelse](begynnelse.md) | Starttidspunkt for eit tidsrom |
| [belop](belop.md) | Beløp for gebyret |
| [ble_generert_ved](ble_generert_ved.md) | Brukes til å referere til en aktivitet som genererte datasettet, eller som gi... |
| [datasett](datasett.md) | Datasett som er del av katalogen |
| [datasettdistribusjon](datasettdistribusjon.md) | Tilgjengelege distribusjonar av datasettet |
| [datatjeneste](datatjeneste.md) | Datatjeneste som er del av katalogen |
| [dokumentasjon](dokumentasjon.md) | Lenke til dokumentasjon om ressursen |
| [eierskapshistorikk](eierskapshistorikk.md) | Opphav og eigarskapshistorikk for ressursen |
| [eksempeldata](eksempeldata.md) | Eksempeldata som distribusjon |
| [endepunkts_url](endepunkts_url.md) | URL til datatjenestens endepunkt |
| [endepunktsbeskrivelse](endepunktsbeskrivelse.md) | URL til beskriving av endepunktet (t |
| [filstorrelse](filstorrelse.md) | Filstørrelse i bytes |
| [forste](forste.md) | Første datasett i ei datasettserie |
| [frekvens](frekvens.md) | Oppdateringsfrekvens for datasettet |
| [gjeldende_lovgivning](gjeldende_lovgivning.md) | Lovgjeving som gjeld for ressursen |
| [har_del](har_del.md) | Delkatalog inkludert i denne katalogen |
| [har_epost](har_epost.md) | E-postadresse til kontaktpunktet |
| [har_gebyr](har_gebyr.md) | Gebyr knytt til bruk av datatjenesten |
| [har_kontaktside](har_kontaktside.md) | Nettside for kontakt |
| [har_kvalitetsmerknad](har_kvalitetsmerknad.md) | Kvalitetsmerknad knytt til datasettet |
| [har_rolle](har_rolle.md) | Rolle ein aktør eller ressurs har i ein relasjon |
| [i_samsvar_med](i_samsvar_med.md) | Standard ressursen er i samsvar med |
| [i_serie](i_serie.md) | Datasettserie dette datasettet er ein del av |
| [jurisdiksjon](jurisdiksjon.md) | Jurisdiksjon for rettigheitserklæringa |
| [katalogpost](katalogpost.md) | Katalogpostar i katalogen |
| [kilde_datasett](kilde_datasett.md) | Datasett dette datasettet er avleidd frå |
| [kilde_post](kilde_post.md) | Kjelde for katalogposten (ekstern oppføring) |
| [komprimeringsformat](komprimeringsformat.md) | Komprimeringsformat brukt i distribusjonen |
| [kontaktpunkt](kontaktpunkt.md) | Kontaktinformasjon for hendvendelsar om ressursen |
| [krediteringstekst](krediteringstekst.md) | Tekst som skal brukast ved kreditering |
| [krediteringsurl](krediteringsurl.md) | URL for kreditering av rettshavar |
| [landingsside](landingsside.md) | Nettside med informasjon om ressursen |
| [lisens](lisens.md) | Lisens for bruk av ressursen |
| [medietype](medietype.md) | Medietype i samsvar med IANA-registeret |
| [navn_aktor](navn_aktor.md) | Namn på aktøren |
| [navn_vcard](navn_vcard.md) | Formatert namn (vCard) |
| [nedlastningslenke](nedlastningslenke.md) | Direkte nedlastingslenke for distribusjonsfila |
| [notasjon](notasjon.md) | Notasjon/kode for identifikatoren |
| [opphavsrettsaar](opphavsrettsaar.md) | Årstal for opphavsrett |
| [opphavsrettserklaring](opphavsrettserklaring.md) | Opphavsrettserklæring |
| [opphavsrettsinnehaver](opphavsrettsinnehaver.md) | Namn på opphavsrettsinnehavar |
| [opphavsrettsnotis](opphavsrettsnotis.md) | Opphavsrettsnotis |
| [pakkeformat](pakkeformat.md) | Pakkeformat brukt i distribusjonen |
| [policy](policy.md) | ODRL-policy som regulerer bruk av ressursen |
| [primaertema](primaertema.md) | Ressursen katalogposten primært beskriv |
| [produsent](produsent.md) | Aktøren som primært har skapt ressursen |
| [referanse](referanse.md) | Referanse til ekstern ressurs |
| [relasjon_til](relasjon_til.md) | Den relaterte ressursen i ein kvalifisert relasjon |
| [relatert_regulativ_ressurs](relatert_regulativ_ressurs.md) | Relatert regulativ ressurs |
| [relatert_ressurs](relatert_ressurs.md) | Generisk relasjon til ein annan ressurs |
| [rettigheter](rettigheter.md) | Rettar knytte til ressursen |
| [siste](siste.md) | Siste datasett i ei datasettserie |
| [sjekksum](sjekksum.md) | Sjekksum for distribusjonsfila |
| [sjekksumverdi](sjekksumverdi.md) | Sjekksumverdi som heksadesimal streng |
| [slutt](slutt.md) | Sluttidspunkt for eit tidsrom |
| [sluttdato](sluttdato.md) | Sluttdato for tidsrommet |
| [startdato](startdato.md) | Startdato for tidsrommet |
| [tema](tema.md) | Tema frå eit kontrollert vokabular |
| [temaer](temaer.md) | Temavokabular som vert brukt i katalogen |
| [tidsopplosning](tidsopplosning.md) | Minste tidsoppløysing i datasettet |
| [tidsrom](tidsrom.md) | Tidsperiode ressursen dekkar |
| [tilgangs_url](tilgangs_url.md) | URL for tilgang til distribusjonen |
| [tilgangsrettigheter](tilgangsrettigheter.md) | Egenskapen brukes til å angi om det er allmenn tilgang, betinget tilgang elle... |
| [tilgangstjeneste](tilgangstjeneste.md) | Datatjeneste som gjev tilgang til distribusjonen |
| [tilgjengeliggjor_datasett](tilgjengeliggjor_datasett.md) | Datasett som datatjenesten tilgjengeleggjer |
| [tilgjengelighet](tilgjengelighet.md) | Planlagt tilgjengelegheit for ressursen |
| [tittel_literal](tittel_literal.md) | Namn/tittel utan språktag |
| [underkatalog](underkatalog.md) | Katalog som er ein del av denne katalogen |
| [utgiver](utgiver.md) | Aktøren som er ansvarleg for å tilgjengeleggjere ressursen |
| [versjon](versjon.md) | Versjonsnummer |


## Enumerations

| Enumeration | Description |
| --- | --- |


## Types

| Type | Description |
| --- | --- |


## Subsets

| Subset | Description |
| --- | --- |
| [Anbefalt](anbefalt.md) | Anbefalte eigenskapar i ein AP-NO-profil |
| [Obligatorisk](obligatorisk.md) | Obligatoriske eigenskapar i ein AP-NO-profil |
| [Valgfri](valgfri.md) | Valfrie eigenskapar i ein AP-NO-profil |
