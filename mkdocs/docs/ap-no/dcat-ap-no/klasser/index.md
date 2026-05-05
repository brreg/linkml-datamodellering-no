# DCAT-AP-NO

Norsk applikasjonsprofil av DCAT-AP, modellert i LinkML med lenking framfor inlining. Basert på https://informasjonsforvaltning.github.io/dcat-ap-no/

URI: https://data.norge.no/linkml/dcat-ap-no

Name: dcat-ap-no



## Classes

| Class | Description |
| --- | --- |
| [Aktor](aktor.md) | Ein aktør (person, organisasjon eller system) med ansvar for ein ressurs |
| [Begrepssamling](begrepssamling.md) | Ei SKOS-omgrepssamling (temavokabular) |
| [Distribusjon](distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |
| [Frekvens](frekvens.md) | Ein oppdateringsfrekvens |
| [Gebyr](gebyr.md) | Eit gebyr knytt til bruk av ein datatjeneste |
| [Identifikator](identifikator.md) | Ein alternativ identifikator for ein ressurs |
| [KatalogisertRessurs](katalogisertressurs.md) | Basisklasse for ressursar som kan katalogiserast |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Datasettserie](datasettserie.md) | Ei serie av relaterte datasett publisert separat men med felles metadata |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Datatjeneste](datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Katalog](katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre kata... |
| [Katalogpost](katalogpost.md) | Ein katalogpost som beskriv ein ressurs i katalogen |
| [Konsept](konsept.md) | Referanse til eit SKOS-omgrep frå eit kontrollert vokabular |
| [Kontaktopplysning](kontaktopplysning.md) | Kontaktinformasjon for ein aktør |
| [Mediatype](mediatype.md) | Ein medietype eller filformat (dct:MediaTypeOrExtent) |
| [OdrlPolicy](odrlpolicy.md) | Ein ODRL-policy |
| [ProvAktivitet](provaktivitet.md) | Ein PROV-aktivitet |
| [ProvAttributering](provattributering.md) | Ein kvalifisert PROV-attributering |
| [ProvenanceStatement](provenancestatement.md) | Ein provenienserklæring |
| [RegulativRessurs](regulativressurs.md) | Ein regulativ ressurs (lov, forskrift o |
| [Relasjon](relasjon.md) | Ein kvalifisert relasjon mellom to ressursar |
| [Rettighetserklaring](rettighetserklaring.md) | Ei erklæring om rettar til ein ressurs (ODRS) |
| [Sjekksum](sjekksum.md) | Ein sjekksum for ein distribusjon |
| [Spraak](spraak.md) | Ein språkreferanse (dct:LinguisticSystem) |
| [Standard](standard.md) | Ein standard som ein ressurs er i samsvar med |
| [Tidsinstant](tidsinstant.md) | Eit tidspunkt (OWL Time) |
| [Tidsrom](tidsrom.md) | Eit tidsintervall med start- og sluttdato |



## Slots

| Slot | Description |
| --- | --- |
| [algoritme](algoritme.md) | Hash-algoritme brukt for sjekksummen |
| [anbefalt_term](anbefalt_term.md) | Føretrukke term/namn for ressursen (skos:prefLabel) |
| [annen_ansvarlig_aktor](annen_ansvarlig_aktor.md) | Kvalifisert attributering til ansvarleg aktør |
| [annen_identifikator](annen_identifikator.md) | Alternativ identifikator frå eit anna system |
| [annen_spesifikk_relasjon](annen_spesifikk_relasjon.md) | Kvalifisert relasjon til ein annan ressurs |
| [anvendelsesretningslinjer](anvendelsesretningslinjer.md) | Retningslinjer for gjenbruk av data |
| [begrep](begrep.md) | Fagomgrep som datasettet handlar om |
| [begynnelse](begynnelse.md) | Starttidspunkt for eit tidsrom |
| [belop](belop.md) | Beløp for gebyret |
| [beskrivelse](beskrivelse.md) | Fritekstbeskrivelse av ressursen (dct:description) |
| [ble_generert_ved](ble_generert_ved.md) | Aktiviteten som genererte datasettet |
| [datasett](datasett.md) | Datasett som er del av katalogen |
| [datasettdistribusjon](datasettdistribusjon.md) | Tilgjengelege distribusjonar av datasettet |
| [datatjeneste](datatjeneste.md) | Datatjeneste som er del av katalogen |
| [dekningsomrade](dekningsomrade.md) | Geografisk dekningsområde (dct:spatial) |
| [dokumentasjon](dokumentasjon.md) | Lenke til dokumentasjon om ressursen |
| [eierskapshistorikk](eierskapshistorikk.md) | Opphav og eigarskapshistorikk for ressursen |
| [eksempeldata](eksempeldata.md) | Eksempeldata som distribusjon |
| [endepunkts_url](endepunkts_url.md) | URL til datatjenestens endepunkt |
| [endepunktsbeskrivelse](endepunktsbeskrivelse.md) | URL til beskriving av endepunktet (t |
| [endringsdato](endringsdato.md) | Dato for siste endring av ressursen (dct:modified) |
| [filstorrelse](filstorrelse.md) | Filstørrelse i bytes |
| [format](format.md) | Filformat eller medietype (dct:format) |
| [forste](forste.md) | Første datasett i ei datasettserie |
| [frekvens](frekvens.md) | Oppdateringsfrekvens for datasettet |
| [gjeldende_lovgivning](gjeldende_lovgivning.md) | Lovgjeving som gjeld for ressursen |
| [har_del](har_del.md) | Delkatalog inkludert i denne katalogen |
| [har_epost](har_epost.md) | E-postadresse til kontaktpunktet |
| [har_gebyr](har_gebyr.md) | Gebyr knytt til bruk av datatjenesten |
| [har_kontaktside](har_kontaktside.md) | Nettside for kontakt |
| [har_merknad](har_merknad.md) | Fritekstmerknad (rdfs:comment) |
| [har_referanse](har_referanse.md) | Referanse til ekstern ressurs (rdfs:seeAlso) |
| [har_rolle](har_rolle.md) | Rolle ein aktør eller ressurs har i ein relasjon |
| [har_versjonsnummer](har_versjonsnummer.md) | Versjonsnummer for ressursen (owl:versionInfo) |
| [heimeside](heimeside.md) | Heimeside for ressursen eller organisasjonen (foaf:homepage) |
| [i_samsvar_med](i_samsvar_med.md) | Standard ressursen er i samsvar med |
| [i_serie](i_serie.md) | Datasettserie dette datasettet er ein del av |
| [id](id.md) | URI-identifikator for ressursen |
| [identifikator_literal](identifikator_literal.md) | Tekstleg identifikator for ressursen (dct:identifier) |
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
| [nokkelord](nokkelord.md) | Nøkkelord som beskriv ressursen (dcat:keyword) |
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
| [sprak](sprak.md) | Språk brukt i ressursen (dct:language) |
| [startdato](startdato.md) | Startdato for tidsrommet |
| [status](status.md) | Status for ressursen frå eit kontrollert vokabular (adms:status) |
| [tema](tema.md) | Tema frå eit kontrollert vokabular |
| [temaer](temaer.md) | Temavokabular som vert brukt i katalogen |
| [tidsopplosning](tidsopplosning.md) | Minste tidsoppløysing i datasettet |
| [tidsrom](tidsrom.md) | Tidsperiode ressursen dekkar |
| [tilgangs_url](tilgangs_url.md) | URL for tilgang til distribusjonen |
| [tilgangsrettigheter](tilgangsrettigheter.md) | Tilgangsrettar for ressursen |
| [tilgangstjeneste](tilgangstjeneste.md) | Datatjeneste som gjev tilgang til distribusjonen |
| [tilgjengeliggjor_datasett](tilgjengeliggjor_datasett.md) | Datasett som datatjenesten tilgjengeleggjer |
| [tilgjengelighet](tilgjengelighet.md) | Planlagt tilgjengelegheit for ressursen |
| [tittel](tittel.md) | Namn/tittel på ressursen (dct:title) |
| [tittel_literal](tittel_literal.md) | Namn/tittel utan språktag |
| [type_concept](type_concept.md) | Type ressurs frå eit kontrollert vokabular (dct:type) |
| [underkatalog](underkatalog.md) | Katalog som er ein del av denne katalogen |
| [utgivelsesdato](utgivelsesdato.md) | Dato ressursen vart første gong publisert (dct:issued) |
| [utgiver](utgiver.md) | Aktøren som er ansvarleg for å tilgjengeleggjere ressursen |
| [valuta](valuta.md) | Valuta (cv:currency) |
| [versjon](versjon.md) | Versjonsnummer |
| [versjonsmerknad](versjonsmerknad.md) | Merknad om endringar i denne versjonen (adms:versionNotes) |


## Enumerations

| Enumeration | Description |
| --- | --- |


## Types

| Type | Description |
| --- | --- |
| [Boolean](boolean.md) | A binary (true or false) value |
| [Curie](curie.md) | a compact URI |
| [Date](date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](dateordatetime.md) | Either a date or a datetime |
| [Datetime](datetime.md) | The combination of a date and time |
| [Decimal](decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](double.md) | A real number that conforms to the xsd:double specification |
| [Duration](duration.md) | ISO 8601-varigheit (xsd:duration), t |
| [Float](float.md) | A real number that conforms to the xsd:float specification |
| [GYear](gyear.md) | Gregorisk årstal (xsd:gYear), t |
| [Integer](integer.md) | An integer |
| [Jsonpath](jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](jsonpointer.md) | A string encoding a JSON Pointer |
| [LangString](langstring.md) | Språktagget streng (rdf:langString) |
| [Ncname](ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [NonNegativeInteger](nonnegativeinteger.md) | Ikkje-negativ heltalsverdi (xsd:nonNegativeInteger) |
| [Objectidentifier](objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](string.md) | A character string |
| [Time](time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](uri.md) | a complete URI |
| [Uriorcurie](uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
| [Anbefalt](anbefalt.md) | Anbefalte eigenskapar i ein AP-NO-profil |
| [Obligatorisk](obligatorisk.md) | Obligatoriske eigenskapar i ein AP-NO-profil |
| [Valgfri](valgfri.md) | Valfrie eigenskapar i ein AP-NO-profil |
