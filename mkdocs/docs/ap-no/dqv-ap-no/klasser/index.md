# DQV-AP-NO

Norsk applikasjonsprofil av DQV (Data Quality Vocabulary), modellert i LinkML med lenking framfor inlining. Basert på https://informasjonsforvaltning.github.io/dqv-ap-no/

URI: https://data.norge.no/linkml/dqv-ap-no

Name: dqv-ap-no



## Classes

| Class | Description |
| --- | --- |
| [Begrepssamling](begrepssamling.md) | Ei SKOS-omgrepssamling (temavokabular) |
| [Datasett](datasett.md) | Eit datasett (dcat:Dataset) utvida med DQV-AP-NO-eigenskapar for kvalitetsinf... |
| [DcatRessurs](dcatressurs.md) | Ein katalogisert ressurs (brukt som målklasse for oa:hasTarget) |
| [Konsept](konsept.md) | Referanse til eit SKOS-omgrep frå eit kontrollert vokabular |
| [Kvalitetsdimensjon](kvalitetsdimensjon.md) | Ein kvalitetsdimensjon som grupperer relaterte kvalitetsmål |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kvalitetsdeldimensjon](kvalitetsdeldimensjon.md) | Ein deldimensjon av ein kvalitetsdimensjon |
| [Kvalitetsmaal](kvalitetsmaal.md) | Eit kvalitetsmål som operasjonaliserer ein kvalitetsdeldimensjon |
| [Kvalitetsmaaling](kvalitetsmaaling.md) | Ei konkret måling av eit kvalitetsmål for eit datasett |
| [Kvalitetsmerknad](kvalitetsmerknad.md) | Ein merknad om kvaliteten til eit datasett |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Brukartilbakemelding](brukartilbakemelding.md) | Tilbakemelding frå ein brukar om kvaliteten til eit datasett |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kvalitetssertifikat](kvalitetssertifikat.md) | Eit sertifikat som stadfester kvaliteten til eit datasett |
| [Mediatype](mediatype.md) | Ein medietype eller filformat (dct:MediaTypeOrExtent) |
| [Motivasjon](motivasjon.md) | Motivasjonen bak ein kvalitetsmerknad (Web Annotation) |
| [Spraak](spraak.md) | Ein språkreferanse (dct:LinguisticSystem) |
| [Standard](standard.md) | Ein standard eller spesifikasjon som eit datasett er i samsvar med |
| [Tekstdel](tekstdel.md) | Ein tekstleg del av ein kvalitetsmerknad (Web Annotation) |



## Slots

| Slot | Description |
| --- | --- |
| [anbefalt_term](anbefalt_term.md) | Føretrukke term/namn for ressursen (skos:prefLabel) |
| [beskrivelse](beskrivelse.md) | Fritekstbeskrivelse av ressursen (dct:description) |
| [dekningsomrade](dekningsomrade.md) | Geografisk dekningsområde (dct:spatial) |
| [endringsdato](endringsdato.md) | Dato for siste endring av ressursen (dct:modified) |
| [er_deldimensjon_av](er_deldimensjon_av.md) | Overordna kvalitetsdimensjon denne deldimensjonen høyrer til |
| [er_i_kvalitetsdeldimensjon](er_i_kvalitetsdeldimensjon.md) | Kvalitetsdeldimensjonen dette målet operasjonaliserer |
| [er_i_kvalitetsdimensjon](er_i_kvalitetsdimensjon.md) | Kvalitetsdimensjonen denne merknaden eller standarden gjeld |
| [er_i_samsvar_med](er_i_samsvar_med.md) | Standard eller spesifikasjon datasettet er i samsvar med |
| [er_kvalitetsmaaling_av](er_kvalitetsmaaling_av.md) | Kvalitetsmålet denne målinga er ei måling av |
| [er_motivert_av](er_motivert_av.md) | Motivasjonen bak kvalitetsmerknaden (t |
| [format](format.md) | Filformat eller medietype (dct:format) |
| [har_anbefalt_term](har_anbefalt_term.md) | Føretrekt term/namn for dimensjonen eller målet |
| [har_definisjon](har_definisjon.md) | Definisjon av dimensjonen eller målet |
| [har_forventet_datatype](har_forventet_datatype.md) | Forventa XSD-datatype for verdien av ei kvalitetsmåling |
| [har_kvalitetsmaaling](har_kvalitetsmaaling.md) | Kvalitetsmåling knytt til datasettet |
| [har_kvalitetsmerknad](har_kvalitetsmerknad.md) | Kvalitetsmerknad knytt til datasettet |
| [har_maal](har_maal.md) | Ressursen merknaden gjeld |
| [har_merknad](har_merknad.md) | Fritekstmerknad (rdfs:comment) |
| [har_referanse](har_referanse.md) | Referanse til ekstern ressurs (rdfs:seeAlso) |
| [har_tekstdel](har_tekstdel.md) | Tekstleg innhald i merknaden |
| [har_verdi](har_verdi.md) | Målt verdi (xsd:boolean, xsd:double, xsd:nonNegativeInteger eller rdfs:Litera... |
| [har_verdi_tekstdel](har_verdi_tekstdel.md) | Tekstinnhaldet i tekstdelen |
| [har_versjonsnummer](har_versjonsnummer.md) | Versjonsnummer for ressursen (owl:versionInfo) |
| [heimeside](heimeside.md) | Heimeside for ressursen eller organisasjonen (foaf:homepage) |
| [id](id.md) | URI-identifikator for ressursen |
| [identifikator_literal](identifikator_literal.md) | Tekstleg identifikator for ressursen (dct:identifier) |
| [nokkelord](nokkelord.md) | Nøkkelord som beskriv ressursen (dcat:keyword) |
| [sprak](sprak.md) | Språk brukt i ressursen (dct:language) |
| [status](status.md) | Status for ressursen frå eit kontrollert vokabular (adms:status) |
| [tittel](tittel.md) | Namn/tittel på ressursen (dct:title) |
| [type_concept](type_concept.md) | Type ressurs frå eit kontrollert vokabular (dct:type) |
| [utgivelsesdato](utgivelsesdato.md) | Dato ressursen vart første gong publisert (dct:issued) |
| [valuta](valuta.md) | Valuta (cv:currency) |
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
