# DQV-AP-NO

Norsk applikasjonsprofil av DQV (Data Quality Vocabulary), modellert i LinkML med lenking framfor inlining. Basert på https://informasjonsforvaltning.github.io/dqv-ap-no/

URI: https://data.norge.no/linkml/dqv-ap-no

Name: dqv-ap-no



## Classes

| Class | Description |
| --- | --- |
| [Begrep](Begrep.md) | Eit SKOS-omgrep frå eit kontrollert vokabular |
| [Begrepssamling](Begrepssamling.md) | Ei SKOS-omgrepssamling (temavokabular) |
| [Container](Container.md) | Rotklasse for DQV-AP-NO-datafiler |
| [Datasett](Datasett.md) | Eit datasett (dcat:Dataset) utvida med DQV-AP-NO-eigenskapar for kvalitetsinf... |
| [DcatRessurs](DcatRessurs.md) | Ein katalogisert ressurs (brukt som målklasse for oa:hasTarget) |
| [Kvalitetsdimensjon](Kvalitetsdimensjon.md) | Ein kvalitetsdimensjon som grupperer relaterte kvalitetsmål |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kvalitetsdeldimensjon](Kvalitetsdeldimensjon.md) | Ein deldimensjon av ein kvalitetsdimensjon |
| [Kvalitetsmaal](Kvalitetsmaal.md) | Eit kvalitetsmål som operasjonaliserer ein kvalitetsdeldimensjon |
| [Kvalitetsmaaling](Kvalitetsmaaling.md) | Ei konkret måling av eit kvalitetsmål for eit datasett |
| [Kvalitetsmerknad](Kvalitetsmerknad.md) | Ein merknad om kvaliteten til eit datasett |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Brukartilbakemelding](Brukartilbakemelding.md) | Tilbakemelding frå ein brukar om kvaliteten til eit datasett |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kvalitetssertifikat](Kvalitetssertifikat.md) | Eit sertifikat som stadfester kvaliteten til eit datasett |
| [Mediatype](Mediatype.md) | Ein medietype eller filformat (dct:MediaTypeOrExtent) |
| [Motivasjon](Motivasjon.md) | Motivasjonen bak ein kvalitetsmerknad (Web Annotation) |
| [Spraak](Spraak.md) | Ein språkreferanse (dct:LinguisticSystem) |
| [Standard](Standard.md) | Ein standard eller spesifikasjon som eit datasett er i samsvar med |
| [Tekstdel](Tekstdel.md) | Ein tekstleg del av ein kvalitetsmerknad (Web Annotation) |



## Slots

| Slot | Description |
| --- | --- |
| [beskrivelse](beskrivelse.md) | Fritekstbeskrivelse av ressursen (dct:description) |
| [brukartilbakemeldingar](brukartilbakemeldingar.md) |  |
| [datasett](datasett.md) |  |
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
| [id](id.md) | URI-identifikator for ressursen |
| [identifikator_literal](identifikator_literal.md) | Tekstleg identifikator for ressursen (dct:identifier) |
| [kvalitetsdeldimensjonar](kvalitetsdeldimensjonar.md) |  |
| [kvalitetsdimensjonar](kvalitetsdimensjonar.md) |  |
| [kvalitetsmaal](kvalitetsmaal.md) |  |
| [kvalitetsmaalingar](kvalitetsmaalingar.md) |  |
| [kvalitetsmerknader](kvalitetsmerknader.md) |  |
| [kvalitetssertifikat](kvalitetssertifikat.md) |  |
| [sprak](sprak.md) | Språk brukt i ressursen (dct:language) |
| [standardar](standardar.md) |  |
| [tekstdelar](tekstdelar.md) |  |
| [tittel](tittel.md) | Namn/tittel på ressursen (dct:title) |
| [type_concept](type_concept.md) | Type ressurs frå eit kontrollert vokabular (dct:type) |
| [utgivelsesdato](utgivelsesdato.md) | Dato ressursen vart første gong publisert (dct:issued) |


## Enumerations

| Enumeration | Description |
| --- | --- |


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
| [Duration](Duration.md) | ISO 8601-varigheit (xsd:duration), t |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [GYear](GYear.md) | Gregorisk årstal (xsd:gYear), t |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [LangString](LangString.md) | Språktagget streng (rdf:langString) |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [NonNegativeInteger](NonNegativeInteger.md) | Ikkje-negativ heltalsverdi (xsd:nonNegativeInteger) |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
| [Anbefalt](Anbefalt.md) | Anbefalte eigenskapar i ein AP-NO-profil |
| [Obligatorisk](Obligatorisk.md) | Obligatoriske eigenskapar i ein AP-NO-profil |
| [Valgfri](Valgfri.md) | Valfrie eigenskapar i ein AP-NO-profil |
