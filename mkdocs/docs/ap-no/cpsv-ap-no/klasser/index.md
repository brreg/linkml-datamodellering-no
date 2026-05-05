# CPSV-AP-NO

Norsk applikasjonsprofil av CPSV (Core Public Service Vocabulary), modellert i LinkML med lenking framfor inlining. Basert på https://informasjonsforvaltning.github.io/cpsv-ap-no/

URI: https://data.norge.no/linkml/cpsv-ap-no

Name: cpsv-ap-no



## Classes

| Class | Description |
| --- | --- |
| [Adresse](adresse.md) | Ei postadresse knytt til ein aktør, organisasjon eller kontaktpunkt |
| [Aktor](aktor.md) | Ein aktør (person eller organisasjon) relatert til ei teneste |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OffentligOrganisasjon](offentligorganisasjon.md) | Ein offentleg organisasjon som er ansvarleg for ei teneste |
| [Begrepssamling](begrepssamling.md) | Ei SKOS-omgrepssamling (temavokabular) |
| [Deltagelse](deltagelse.md) | Ei rolle ein aktør har i leveringa av ei teneste |
| [Dokumentasjonstype](dokumentasjonstype.md) | Ein type dokumentasjon som krevst for å levere ei teneste |
| [Gebyr](gebyr.md) | Eit gebyr knytt til ei teneste |
| [Hendelse](hendelse.md) | Ei hending som kan utløyse behov for ei offentleg teneste |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Livshendelse](livshendelse.md) | Ei livshending som kan utløyse behov for tenester (t |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Virksomhetshendelse](virksomhetshendelse.md) | Ei verksemdhending som kan utløyse behov for tenester (t |
| [Katalog](katalog.md) | Ein katalog over offentlege tenester og hendingar |
| [Konsept](konsept.md) | Referanse til eit SKOS-omgrep frå eit kontrollert vokabular |
| [Kontaktpunkt](kontaktpunkt.md) | Kontaktinformasjon for ei teneste eller ein organisasjon |
| [LovpalagtTjeneste](lovpalagttjeneste.md) | Ei lovpålagd teneste som offentlege organ er pålagde å utføre |
| [Mediatype](mediatype.md) | Ein medietype eller filformat (dct:MediaTypeOrExtent) |
| [OffentligTjeneste](offentligtjeneste.md) | Ei konkret offentleg teneste levert av ein offentleg organisasjon |
| [Regel](regel.md) | Eit regelverk eller retningsliner som styrer levering av ei teneste |
| [RegulativRessurs](regulativressurs.md) | Ein regulativ ressurs (lov, forskrift o |
| [Spraak](spraak.md) | Ein språkreferanse (dct:LinguisticSystem) |
| [Tjeneste](tjeneste.md) | Ei teneste levert av ein ikkje-offentleg aktør |
| [Tjenestekanal](tjenestekanal.md) | Ein kanal for å få tilgang til ei teneste (t |
| [Tjenesteresultattype](tjenesteresultattype.md) | Typen resultat som ei teneste produserer |
| [Tjenesteresultattypeliste](tjenesteresultattypeliste.md) | Ei liste over moglege tjenesteresultattypar |



## Slots

| Slot | Description |
| --- | --- |
| [adresse_ref](adresse_ref.md) | Postadresse knytt til aktøren |
| [anbefalt_term](anbefalt_term.md) | Føretrukke term/namn for ressursen (skos:prefLabel) |
| [behandlingstid](behandlingstid.md) | Forventa behandlingstid for tenesta eller kanalen (ISO 8601) |
| [beskrivelse](beskrivelse.md) | Fritekstbeskrivelse av ressursen (dct:description) |
| [dekningsomrade](dekningsomrade.md) | Geografisk dekningsområde (dct:spatial) |
| [deltakar](deltakar.md) | Aktøren som deltek |
| [deltek_i](deltek_i.md) | Deltakingar aktøren er del av |
| [eigd_av](eigd_av.md) | Aktør som eig eller er ansvarleg for tenesta |
| [endringsdato](endringsdato.md) | Dato for siste endring av ressursen (dct:modified) |
| [epost](epost.md) | E-postadresse (mailto:-URI) |
| [er_beskrive_av](er_beskrive_av.md) | Datasett som beskriv ressursen |
| [er_del_av](er_del_av.md) | Tenesta er del av ei anna teneste |
| [er_gruppert_av](er_gruppert_av.md) | Hending(ar) som grupperer tenesta |
| [er_klassifisert_av](er_klassifisert_av.md) | Omgrep tenesta er klassifisert med |
| [er_spesifisert_i](er_spesifisert_i.md) | Liste eller spesifikasjon ressursen er del av |
| [folger](folger.md) | Regelverk tenesta følgjer |
| [foretrekt_namn](foretrekt_namn.md) | Føretrekt namn/term for organisasjonen |
| [format](format.md) | Filformat eller medietype (dct:format) |
| [full_adresse](full_adresse.md) | Full adresse som fritekst |
| [godtek_sprak](godtek_sprak.md) | Språk dokumentasjonstypen er akseptert i |
| [gyldig_i](gyldig_i.md) | Kor lenge dokumentasjonen er gyldig (ISO 8601 varigheit) |
| [har_ansvarleg_styremakt](har_ansvarleg_styremakt.md) | Offentleg organisasjon ansvarleg for tenesta |
| [har_del](har_del.md) | Deltenester som inngår i denne tenesta |
| [har_deltaking](har_deltaking.md) | Deltakarar med spesifikke roller i levering av tenesta |
| [har_dokumentasjonstype](har_dokumentasjonstype.md) | Dokumentasjon som krevst for tenesta |
| [har_gebyr](har_gebyr.md) | Gebyr knytt til tenesta |
| [har_kontaktpunkt](har_kontaktpunkt.md) | Kontaktpunkt for tenesta eller organisasjonen |
| [har_merknad](har_merknad.md) | Fritekstmerknad (rdfs:comment) |
| [har_referanse](har_referanse.md) | Referanse til ekstern ressurs (rdfs:seeAlso) |
| [har_regulativ_ressurs](har_regulativ_ressurs.md) | Regulativ ressurs (lov, forskrift) knytt til tenesta |
| [har_rolle](har_rolle.md) | Rolla aktøren har i ei deltaking |
| [har_tenestekanal](har_tenestekanal.md) | Kanal for tilgang til tenesta |
| [har_tenesteresultattype](har_tenesteresultattype.md) | Typen resultat tenesta kan produsere |
| [har_versjonsnummer](har_versjonsnummer.md) | Versjonsnummer for ressursen (owl:versionInfo) |
| [heimeside](heimeside.md) | Heimeside for ressursen eller organisasjonen (foaf:homepage) |
| [id](id.md) | URI-identifikator for ressursen |
| [identifikator_literal](identifikator_literal.md) | Tekstleg identifikator for ressursen (dct:identifier) |
| [inneheld_hending](inneheld_hending.md) | Hendingar i katalogen |
| [inneheld_teneste](inneheld_teneste.md) | Offentlege tenester i katalogen |
| [kan_skape_hending](kan_skape_hending.md) | Hending tenesteresultatet kan skape |
| [kan_utlose](kan_utlose.md) | Offentlege tenester hendinga kan utløyse |
| [kan_utlose_behov_for](kan_utlose_behov_for.md) | Tenester det kan oppstå behov for som følgje av hendinga |
| [kategori](kategori.md) | Kategori for kontaktpunktet |
| [klassifisering](klassifisering.md) | Klassifisering av dokumentasjonstypen |
| [kontaktside](kontaktside.md) | Kontaktside (nettadresse) |
| [krev](krev.md) | Teneste eller ressurs denne tenesta krev |
| [land](land.md) | Land (ISO 3166-1 alpha-2 kode) |
| [lisens](lisens.md) | Lisens for katalogen |
| [malgruppe](malgruppe.md) | Målgruppe for tenesta |
| [mogleg_sprak](mogleg_sprak.md) | Mogleg språk for tenesteresultatet |
| [nettside](nettside.md) | Nettside for tenestekanalane |
| [nokkelord](nokkelord.md) | Nøkkelord som beskriv ressursen (dcat:keyword) |
| [opningstider](opningstider.md) | Opningstider |
| [oppdateringsfrekvens](oppdateringsfrekvens.md) | Kor ofte katalogen vert oppdatert |
| [postnummer](postnummer.md) | Postnummer |
| [poststad](poststad.md) | Poststad/by |
| [realiserer](realiserer.md) | Lovpålagd teneste denne offentlege tenesta realiserer |
| [relatert_teneste](relatert_teneste.md) | Relatert teneste |
| [sektor](sektor.md) | Industri/sektor tenesta tilhøyrer |
| [sprak](sprak.md) | Språk brukt i ressursen (dct:language) |
| [status](status.md) | Status for ressursen frå eit kontrollert vokabular (adms:status) |
| [telefon](telefon.md) | Telefonnummer |
| [tema](tema.md) | Emne/tema tenesta handlar om |
| [temaomrade](temaomrade.md) | Tematisk område for tenesta |
| [tittel](tittel.md) | Namn/tittel på ressursen (dct:title) |
| [type_concept](type_concept.md) | Type ressurs frå eit kontrollert vokabular (dct:type) |
| [utgivelsesdato](utgivelsesdato.md) | Dato ressursen vart første gong publisert (dct:issued) |
| [utgjevar](utgjevar.md) | Utgjevar av katalogen |
| [utstedingsstad](utstedingsstad.md) | Stad dokumentasjonen er akseptert frå |
| [valuta](valuta.md) | Valuta (cv:currency) |
| [verdi](verdi.md) | Verdien av gebyret |
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
