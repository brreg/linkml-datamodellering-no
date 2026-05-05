# XKOS-AP-NO

LinkML-modell for XKOS-AP-NO – norsk applikasjonsprofil for utvida SKOS-klassifikasjonar. Basert på https://data.norge.no/specification/xkos-ap-no

URI: https://data.norge.no/linkml/xkos-ap-no

Name: xkos-ap-no



## Classes

| Class | Description |
| --- | --- |
| [Begrepssamling](begrepssamling.md) | Ei SKOS-omgrepssamling (temavokabular) |
| [Kategori](kategori.md) | Ein kategori i ein klassifikasjon (skos:Concept) |
| [Kategorisamanlikning](kategorisamanlikning.md) | Ein samanlikning mellom to kategoriar på tvers av klassifikasjonar (xkos:Conc... |
| [Klassifikasjon](klassifikasjon.md) | Ei klassifikasjon – ein systematisk struktur av kategoriar brukt til å klassi... |
| [Klassifikasjonsnivaa](klassifikasjonsnivaa.md) | Eit nivå i ein klassifikasjon (xkos:ClassificationLevel) |
| [Klassifikasjonssamanlikning](klassifikasjonssamanlikning.md) | Ein samanlikning mellom to klassifikasjonar (xkos:Correspondence) |
| [Konsept](konsept.md) | Referanse til eit SKOS-omgrep frå eit kontrollert vokabular |
| [Mediatype](mediatype.md) | Ein medietype eller filformat (dct:MediaTypeOrExtent) |
| [Organisasjon](organisasjon.md) | Ein organisasjon eller aktør (foaf:Agent) |
| [Spraak](spraak.md) | Ein språkreferanse (dct:LinguisticSystem) |
| [Tidsrom](tidsrom.md) | Eit tidsrom med start- og/eller sluttdato (dct:PeriodOfTime) |



## Slots

| Slot | Description |
| --- | --- |
| [anbefalt_term](anbefalt_term.md) | Føretrukke term/namn for ressursen (skos:prefLabel) |
| [antall_nivaa](antall_nivaa.md) | Antal nivå i klassifikasjonen (xkos:numberOfLevels) |
| [beskrivelse](beskrivelse.md) | Fritekstbeskrivelse av ressursen (dct:description) |
| [bestar_av](bestar_av.md) | Kategorisamanlikningar som inngår i klassifikasjonssamanlikninga (xkos:madeOf... |
| [dekningsomrade](dekningsomrade.md) | Geografisk dekningsområde (dct:spatial) |
| [endringsdato](endringsdato.md) | Dato for siste endring av ressursen (dct:modified) |
| [er_eksklusivt_ekvivalent_med](er_eksklusivt_ekvivalent_med.md) | Eksklusiv breid ekvivalens (xkos:exclusivelyBroadMatch) |
| [er_ekvivalent_med](er_ekvivalent_med.md) | Breid ekvivalens til kategori i annan klassifikasjon (uneskos:broadMatch) |
| [er_i_klassifikasjon](er_i_klassifikasjon.md) | Klassifikasjonen kategorien tilhøyrer (skos:inScheme) |
| [er_ikkje_ekvivalent_med](er_ikkje_ekvivalent_med.md) | Klar ikkje-ekvivalens til kategori i annan klassifikasjon (xkos:disjointMatch... |
| [er_samanlikna_med](er_samanlikna_med.md) | Klassifikasjonar som er samanlikna (xkos:compares) |
| [format](format.md) | Filformat eller medietype (dct:format) |
| [forste_nivaa](forste_nivaa.md) | Toppnivå i klassifikasjonen (xkos:levels) |
| [gjeld_for_tidsrom](gjeld_for_tidsrom.md) | Tidsrom klassifikasjonen er gyldig for (dct:temporal) |
| [har_medlem](har_medlem.md) | Kategoriar som høyrer til dette nivået (skos:member) |
| [har_merknad](har_merknad.md) | Fritekstmerknad (rdfs:comment) |
| [har_notat](har_notat.md) | Fritekstnotat om kategorien (skos:note) |
| [har_referanse](har_referanse.md) | Referanse til ekstern ressurs (rdfs:seeAlso) |
| [har_versjonsnummer](har_versjonsnummer.md) | Versjonsnummer for ressursen (owl:versionInfo) |
| [heimeside](heimeside.md) | Heimeside for ressursen eller organisasjonen (foaf:homepage) |
| [id](id.md) | URI-identifikator for ressursen |
| [identifikator_literal](identifikator_literal.md) | Tekstleg identifikator for ressursen (dct:identifier) |
| [kjeldeomgrep](kjeldeomgrep.md) | Kjeldeomgrep i ein kategorisamanlikning (xkos:sourceConcept) |
| [maalomgrep](maalomgrep.md) | Måleomgrep i ein kategorisamanlikning (xkos:targetConcept) |
| [nivaa_djupn](nivaa_djupn.md) | Djupna (nivånummer) i klassifikasjonsstrukturen (xkos:depth) |
| [nokkelord](nokkelord.md) | Nøkkelord som beskriv ressursen (dcat:keyword) |
| [overordna_kategori](overordna_kategori.md) | Overordna kategori (skos:broader) |
| [samanliknar](samanliknar.md) | Klassifikasjonar som er samanlikna i korrespondansen (xkos:compares) |
| [sprak](sprak.md) | Språk brukt i ressursen (dct:language) |
| [status](status.md) | Status for ressursen frå eit kontrollert vokabular (adms:status) |
| [tema](tema.md) | Fagleg tema klassifikasjonen dekkjer (dct:subject) |
| [tidsrom_slutt](tidsrom_slutt.md) | Sluttdato for tidsromet (dct:endDate) |
| [tidsrom_start](tidsrom_start.md) | Startdato for tidsromet (dct:startDate) |
| [tilhorande_klassifikasjonsnivaa](tilhorande_klassifikasjonsnivaa.md) | Klassifikasjonsnivå kategorien høyrer til (xkos:belongsTo) |
| [tittel](tittel.md) | Namn/tittel på ressursen (dct:title) |
| [type_concept](type_concept.md) | Type ressurs frå eit kontrollert vokabular (dct:type) |
| [underordna_kategori](underordna_kategori.md) | Underordna kategori (skos:narrower) |
| [underordna_klassifikasjonsnivaa](underordna_klassifikasjonsnivaa.md) | Underordna klassifikasjonsnivå (xkos:nextLevel) |
| [utgivelsesdato](utgivelsesdato.md) | Dato ressursen vart første gong publisert (dct:issued) |
| [utgjevar](utgjevar.md) | Organisasjon som er ansvarleg utgjevar (dct:publisher) |
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
