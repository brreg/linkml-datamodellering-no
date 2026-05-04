# SKOS-AP-NO

Norsk applikasjonsprofil av SKOS for omgrep (begrep), modellert i LinkML med lenking framfor inlining. Basert på https://informasjonsforvaltning.github.io/skos-ap-no-begrep/

URI: https://data.norge.no/linkml/skos-ap-no

Name: skos-ap-no



## Classes

| Class | Description |
| --- | --- |
| [AssosiativRelasjon](AssosiativRelasjon.md) | Ein assosiativ relasjon mellom to omgrep |
| [Begrep](Begrep.md) | Eit omgrep med definisjon og tilhøyrande metadata (skos:Concept) |
| [Begrepssamling](Begrepssamling.md) | Ei SKOS-omgrepssamling (temavokabular) |
| [Definisjon](Definisjon.md) | Ein definisjon av eit omgrep via eit eige objekt (euvoc:XlNote) |
| [GeneriskRelasjon](GeneriskRelasjon.md) | Ein generisk relasjon mellom eit overomgrep og eit underomgrep |
| [Konsept](Konsept.md) | Referanse til eit SKOS-omgrep frå eit kontrollert vokabular |
| [Mediatype](Mediatype.md) | Ein medietype eller filformat (dct:MediaTypeOrExtent) |
| [Organisasjon](Organisasjon.md) | Ein organisasjon som er utgjevar eller ansvarleg for eit omgrep |
| [PartitivRelasjon](PartitivRelasjon.md) | Ein partitiv relasjon mellom eit heilskapleg og eit partitivt omgrep |
| [Samling](Samling.md) | Ei namngitt samling av omgrep (skos:Collection) |
| [Spraak](Spraak.md) | Ein språkreferanse (dct:LinguisticSystem) |
| [VCardKontakt](VCardKontakt.md) | Kontaktinformasjon (vCard) for omgrepseigaren |



## Slots

| Slot | Description |
| --- | --- |
| [anbefalt_term](anbefalt_term.md) | Føretrukke term/namn for ressursen (skos:prefLabel) |
| [ansvarleg_verksemd](ansvarleg_verksemd.md) | Fagleg ansvarleg organisasjon for omgrepet (dct:creator) |
| [assosiert_med](assosiert_med.md) | Omgrep dette omgrepet er assosiert med (skos:related) |
| [beskrivelse](beskrivelse.md) | Fritekstbeskrivelse av ressursen (dct:description) |
| [datastruktur_term](datastruktur_term.md) | Term brukt i datastrukturar (skosno:dataStructureLabel) |
| [definisjon](definisjon.md) | Direkte definisjon som fritekst (skos:definition) |
| [dekningsomrade](dekningsomrade.md) | Geografisk dekningsområde (dct:spatial) |
| [eksempel](eksempel.md) | Eksempel på bruk av omgrepet (skos:example) |
| [endringsdato](endringsdato.md) | Dato for siste endring av ressursen (dct:modified) |
| [er_del_av_omgrep](er_del_av_omgrep.md) | Omgrep dette omgrepet er ein del av (xkos:isPartOf) |
| [er_erstatta_av](er_erstatta_av.md) | Omgrep som erstattar dette omgrepet (dct:isReplacedBy) |
| [er_fra_omgrep_i](er_fra_omgrep_i.md) | Assosiativ relasjon der dette omgrepet er frå-omgrepet (skosno:isFromConceptI... |
| [er_medlem_av](er_medlem_av.md) | Samling dette omgrepet er medlem av (uneskos:memberOf) |
| [erstattar](erstattar.md) | Omgrep dette omgrepet erstattar (dct:replaces) |
| [euvoc_status](euvoc_status.md) | Status for omgrepet frå eit kontrollert vokabular (euvoc:status) |
| [fagomrade](fagomrade.md) | Fagområde omgrepet høyrer til (dct:subject) |
| [forkasta_term](forkasta_term.md) | Tidlegare brukt, no forkasta term (skos:hiddenLabel) |
| [format](format.md) | Filformat eller medietype (dct:format) |
| [generaliserer](generaliserer.md) | Omgrep dette omgrepet generaliserer (xkos:generalizes) |
| [gyldig_fra](gyldig_fra.md) | Dato omgrepet er gyldig frå (euvoc:startDate) |
| [gyldig_til](gyldig_til.md) | Dato omgrepet er gyldig til (euvoc:endDate) |
| [har_definisjon](har_definisjon.md) | Definisjon via eige objekt (euvoc:xlDefinition) |
| [har_del_omgrep](har_del_omgrep.md) | Omgrep som er ein del av dette omgrepet (xkos:hasPart) |
| [har_generisk_omgrep](har_generisk_omgrep.md) | Overomgrepet i ein generisk relasjon (skosno:hasGenericConcept) |
| [har_generisk_relasjon](har_generisk_relasjon.md) | Generisk relasjon dette omgrepet er del av (skosno:hasGenericConceptRelation) |
| [har_heilskapleg_omgrep](har_heilskapleg_omgrep.md) | Heilskapleg omgrep i ein partitiv relasjon (skosno:hasComprehensiveConcept) |
| [har_merknad](har_merknad.md) | Fritekstmerknad (rdfs:comment) |
| [har_partitiv_relasjon](har_partitiv_relasjon.md) | Partitiv relasjon dette omgrepet er del av (skosno:hasPartitiveConceptRelatio... |
| [har_partitivt_omgrep](har_partitivt_omgrep.md) | Delomgrepet i ein partitiv relasjon (skosno:hasPartitiveConcept) |
| [har_referanse](har_referanse.md) | Referanse til ekstern ressurs (rdfs:seeAlso) |
| [har_spesifikt_omgrep](har_spesifikt_omgrep.md) | Underomgrepet i ein generisk relasjon (skosno:hasSpecificConcept) |
| [har_versjonsnummer](har_versjonsnummer.md) | Versjonsnummer for ressursen (owl:versionInfo) |
| [heimeside](heimeside.md) | Heimeside for ressursen eller organisasjonen (foaf:homepage) |
| [id](id.md) | URI-identifikator for ressursen |
| [identifikator_literal](identifikator_literal.md) | Tekstleg identifikator for ressursen (dct:identifier) |
| [inndelingskriterium](inndelingskriterium.md) | Inndelingskriterium for ein generisk eller partitiv relasjon (dct:description... |
| [kjelde](kjelde.md) | Kjelde til definisjonen (dct:source) |
| [kjelde_relasjon](kjelde_relasjon.md) | Omgrep som beskriv forholdet mellom definisjonen og kjelda (skosno:relationsh... |
| [kontaktpunkt_vcard](kontaktpunkt_vcard.md) | Kontaktpunkt (vCard) for omgrepet eller samlinga (dcat:contactPoint) |
| [malgruppe_def](malgruppe_def.md) | Målgruppe definisjonen er retta mot (dct:audience) |
| [medlem](medlem.md) | Omgrep som er medlem av samlinga (skos:member) |
| [merknad](merknad.md) | Merknad om bruksomfanget for omgrepet (skos:scopeNote) |
| [naert_samsvar](naert_samsvar.md) | Omgrep med nær, men ikkje nøyaktig same meining (skos:closeMatch) |
| [nokkelord](nokkelord.md) | Nøkkelord som beskriv ressursen (dcat:keyword) |
| [noyaktig_samsvar](noyaktig_samsvar.md) | Omgrep med nøyaktig same meining i anna vokabular (skos:exactMatch) |
| [opprettingsdato](opprettingsdato.md) | Dato omgrepet vart oppretta (dct:created) |
| [relasjontype](relasjontype.md) | Rolle eller type av den assosiative relasjonen (skosno:relationRole) |
| [sja_ogsa_omgrep](sja_ogsa_omgrep.md) | Relatert omgrep (rdfs:seeAlso) |
| [spesifiserer](spesifiserer.md) | Omgrep dette omgrepet spesifiserer (xkos:specializes) |
| [sprak](sprak.md) | Språk brukt i ressursen (dct:language) |
| [status](status.md) | Status for ressursen frå eit kontrollert vokabular (adms:status) |
| [tekst](tekst.md) | Definissjonstekst (rdf:value) |
| [til_omgrep](til_omgrep.md) | Til-omgrepet i den assosiative relasjonen (skosno:hasToConcept) |
| [tillate_term](tillate_term.md) | Tillaten alternativ term for omgrepet (skos:altLabel) |
| [tittel](tittel.md) | Namn/tittel på ressursen (dct:title) |
| [type_concept](type_concept.md) | Type ressurs frå eit kontrollert vokabular (dct:type) |
| [utgivelsesdato](utgivelsesdato.md) | Dato ressursen vart første gong publisert (dct:issued) |
| [utgjevar](utgjevar.md) | Organisasjon ansvarleg for å publisere omgrepet (dct:publisher) |
| [valuta](valuta.md) | Valuta (cv:currency) |
| [verdiomrade](verdiomrade.md) | Verdiområde for omgrepet (skosno:valueRange) |
| [versjonsmerknad](versjonsmerknad.md) | Merknad om endringar i denne versjonen (adms:versionNotes) |


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
