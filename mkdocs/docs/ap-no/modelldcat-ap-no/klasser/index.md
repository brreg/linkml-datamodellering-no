# ModelDCAT-AP-NO

Norsk applikasjonsprofil for beskriving av informasjonsmodellar i DCAT-format, modellert i LinkML. Basert på https://data.norge.no/specification/modelldcat-ap-no

URI: https://data.norge.no/linkml/modelldcat-ap-no

Name: modelldcat-ap-no



## Classes

| Class | Description |
| --- | --- |
| [Aktor](aktor.md) | Ein aktør (person, organisasjon eller system) med ansvar for ein ressurs |
| [Begrepssamling](begrepssamling.md) | Ei SKOS-omgrepssamling (temavokabular) |
| [Dokument](dokument.md) | Eit dokument (foaf:Document) |
| [Eigenskap](eigenskap.md) | Abstrakt basisklasse for eigenskapar knytt til eit modellelement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Abstraksjon](abstraksjon.md) | Ein abstraksjon — ein forenkling som representerer eit modellelement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Assosiasjon](assosiasjon.md) | Ein assosiasjon — ein eigenskap som refererer til eit anna modellelement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Attributt](attributt.md) | Ein attributt — ein eigenskap med ein datatype eller enkel type som verdi |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Avhengighet](avhengighet.md) | Ein avhengighet — ein relasjon der det eine modellelementet avheng av det and... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Realisering](realisering.md) | Ein realisering — ein implementasjonsrelasjon mellom modellelement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Rolle](rolle.md) | Ein rolle — ein eigenskap som knyter ein objekttype til ein assosiasjon |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Samling](samling.md) | Ein samling — ein eigenskap som representerer ei uordna mengd av modellelemen... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Sammensetning](sammensetning.md) | Ein sammensetning — ein sterk eigarelskapsrelasjon mellom modellelement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Spesialisering](spesialisering.md) | Ein spesialisering — eit arveforhold frå eit spesielt til eit generelt modell... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Valg](valg.md) | Eit val — ein eigenskap som representerer eit val mellom modellelement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AlleAv](alleav.md) | Alle av — alle modellelementa i lista må gjelde (logisk OG-mengd) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NoenAv](noenav.md) | Nokon av — minst eitt modellelement i lista må gjelde (logisk ELLER-mengd) |
| [Informasjonsmodell](informasjonsmodell.md) | Ein informasjonsmodell som er katalogisert i ein modelkatalog (modelldcatno:I... |
| [KatalogisertRessurs](katalogisertressurs.md) | Basisklasse for ressursar som kan katalogiserast (dcat:Resource) |
| [Kodeelement](kodeelement.md) | Eit element i ei kodeliste (modelldcatno:CodeElement) |
| [Konsept](konsept.md) | Referanse til eit SKOS-omgrep frå eit kontrollert vokabular |
| [Kontaktopplysning](kontaktopplysning.md) | Kontaktinformasjon (vcard:Organization) |
| [Lisensdokument](lisensdokument.md) | Eit lisensdokument (dct:LicenseDocument) |
| [Lokasjon](lokasjon.md) | Eit geografisk område (dct:Location) |
| [Mediatype](mediatype.md) | Ein medietype eller filformat (dct:MediaTypeOrExtent) |
| [Merknad](merknad.md) | Ei merknad knytt til eit modellelement eller eigenskap |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Betingelsesregel](betingelsesregel.md) | Ein betingelsesregel — ei formell avgrensing på modellelement eller eigenskap... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Eller](eller.md) | Eller — logisk ELLER-betingelse; minst eitt modellelement må gjelde |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Ikke](ikke.md) | Ikkje — negasjon; modellelementet det refererer til må ikkje gjelde |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Og](og.md) | Og — logisk OG-betingelse; alle deltakande modellelement må gjelde |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XEllerY](xellery.md) | Xor — eksklusiv ELLER-betingelse; nøyaktig eitt modellelement må gjelde |
| [Modelkatalog](modelkatalog.md) | Ei kuratert samling av metadata om informasjonsmodellar (dcat:Catalog) |
| [Modellelement](modellelement.md) | Abstrakt basisklasse for alle modellelement i ein informasjonsmodell |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Datatype](datatype.md) | Ein datatype — ein strukturert samansett type |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EnkelType](enkeltype.md) | Ein enkel type med restriksjonar (xsd-fasettar) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kodeliste](kodeliste.md) | Ei kodeliste — eit kontrollert vokabular av tillate verdiar |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Modul](modul.md) | Ein modul som grupperer modellelement i informasjonsmodellen |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Objekttype](objekttype.md) | Ein objekttype — ein klasse med eigenskapar i informasjonsmodellen |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RootObjekttype](rootobjekttype.md) | Ein rotobjekttype — toppnivå-klasse i informasjonsmodellen |
| [Spraak](spraak.md) | Ein språkreferanse (dct:LinguisticSystem) |
| [Standard](standard.md) | Ein standard (dct:Standard) |
| [Tidsperiode](tidsperiode.md) | Eit tidsintervall med start- og sluttdato |



## Slots

| Slot | Description |
| --- | --- |
| [alternativ_term](alternativ_term.md) | Alternativ term for kodeelementet (skos:altLabel) |
| [anbefalt_term](anbefalt_term.md) | Føretrukke term/namn for ressursen (skos:prefLabel) |
| [annoterer](annoterer.md) | Modellelement denne merknaden gjeld (modelldcatno:annotates) |
| [avhengig_av](avhengig_av.md) | Modellelement dette elementet avheng av (modelldcatno:dependentOn) |
| [begrep](begrep.md) | Fagomgrep ressursen handlar om (dct:subject) |
| [beskrivelse](beskrivelse.md) | Fritekstbeskrivelse av ressursen (dct:description) |
| [betingelsesuttrykk](betingelsesuttrykk.md) | Formelt uttrykk for betingelsesregelen (modelldcatno:constraintExpression) |
| [betinger](betinger.md) | Modellelement betingelsesregelen avgrensar (modelldcatno:constrains) |
| [danner_symmetri_med](danner_symmetri_med.md) | Eigenskap som denne eigenskapen dannar symmetri med (modelldcatno:formsSymmet... |
| [definisjon](definisjon.md) | Definisjon av kodeelementet (skos:definition) |
| [dekningsomrade](dekningsomrade.md) | Geografisk dekningsområde (dct:spatial) |
| [eigenskapsmerknad](eigenskapsmerknad.md) | Fritekstmerknad om ein eigenskap (modelldcatno:propertyNote) |
| [eksempel_kode](eksempel_kode.md) | Eksempel på bruk av kodeelementet (skos:example) |
| [eksklusjonsnotat](eksklusjonsnotat.md) | Notat om kva som er ekskludert frå kodeelementet (xkos:exclusionNote) |
| [endringsdato](endringsdato.md) | Dato for siste endring av ressursen (dct:modified) |
| [er_abstraksjon_av](er_abstraksjon_av.md) | Modellelement denne abstraksjonen representerer (modelldcatno:isAbstractionOf... |
| [er_del_av_katalog](er_del_av_katalog.md) | Overordna modelkatalog (dct:isPartOf) |
| [er_del_av_modell](er_del_av_modell.md) | Overordna informasjonsmodell (dct:isPartOf) |
| [er_erstatta_av](er_erstatta_av.md) | Informasjonsmodell som erstattar denne (dct:isReplacedBy) |
| [er_i_samsvar_med](er_i_samsvar_med.md) | Standard ressursen er i samsvar med (dct:conformsTo) |
| [er_profil_av](er_profil_av.md) | Standard denne informasjonsmodellen er ein profil av (prof:isProfileOf) |
| [erstatter](erstatter.md) | Informasjonsmodell som denne erstattar (dct:replaces) |
| [format](format.md) | Filformat eller medietype (dct:format) |
| [forrige](forrige.md) | Førre kodeelement i ein ordna kodeliste (xkos:previous) |
| [fraksjonssifre](fraksjonssifre.md) | Maks tal på desimalsiffer (xsd:fractionDigits) |
| [har_datatype](har_datatype.md) | Datatype for attributten (modelldcatno:hasDataType) |
| [har_del](har_del.md) | Del-ressurs inkludert i denne katalogen (dct:hasPart) |
| [har_del_modell](har_del_modell.md) | Del-informasjonsmodell av denne modellen (dct:hasPart) |
| [har_eigenskap](har_eigenskap.md) | Eigenskapar modellelementet har (modelldcatno:hasProperty) |
| [har_enkel_type](har_enkel_type.md) | Enkel type for attributten (modelldcatno:hasSimpleType) |
| [har_format](har_format.md) | Dokument som representerer ein annan form av modellen (dct:hasFormat) |
| [har_generelt_begrep](har_generelt_begrep.md) | Det generelle modellelementet i ei spesialisering (modelldcatno:hasGeneralCon... |
| [har_leverandor](har_leverandor.md) | Leverandør-modellelement i realiseringa (modelldcatno:hasSupplier) |
| [har_merknad](har_merknad.md) | Fritekstmerknad (rdfs:comment) |
| [har_noe](har_noe.md) | Modellelement som inngår i valet (modelldcatno:hasSome) |
| [har_objekttype](har_objekttype.md) | Objekttype knytt til rolla (modelldcatno:hasObjectType) |
| [har_referanse](har_referanse.md) | Referanse til ekstern ressurs (rdfs:seeAlso) |
| [har_type](har_type.md) | Type modellelement for eigenskapen (modelldcatno:hasType) |
| [har_verdi_fra](har_verdi_fra.md) | Kodeliste for tillate verdiar til attributten (modelldcatno:hasValueFrom) |
| [har_versjonsnummer](har_versjonsnummer.md) | Versjonsnummer for ressursen (owl:versionInfo) |
| [heimeside](heimeside.md) | Heimeside for ressursen eller organisasjonen (foaf:homepage) |
| [i_skjema](i_skjema.md) | Kodeliste dette kodeelementet tilhøyrer (skos:inScheme) |
| [id](id.md) | URI-identifikator for ressursen |
| [identifikator_literal](identifikator_literal.md) | Tekstleg identifikator for ressursen (dct:identifier) |
| [informasjonsmodellidentifikator](informasjonsmodellidentifikator.md) | Identifikator for informasjonsmodellen i domenet (modelldcatno:informationMod... |
| [inklusjonsnotat](inklusjonsnotat.md) | Notat om kva som er inkludert i kodeelementet (xkos:inclusionNote) |
| [inneholder](inneholder.md) | Modellelement som er del av samansetjinga (modelldcatno:contains) |
| [inneholder_modellelement](inneholder_modellelement.md) | Modellelement som er del av informasjonsmodellen (modelldcatno:containsModelE... |
| [inneholder_objekttype](inneholder_objekttype.md) | Objekttype som attributten inneheld (modelldcatno:containsObjectType) |
| [kontaktpunkt](kontaktpunkt.md) | Kontaktinformasjon for ressursen (dcat:contactPoint) |
| [lengde](lengde.md) | Nøyaktig lengd av strengen (xsd:length) |
| [lisens](lisens.md) | Lisens for bruk av ressursen (dct:license) |
| [maks_eksklusiv](maks_eksklusiv.md) | Eksklusiv maksimumsverdi (xsd:maxExclusive) |
| [maks_inklusiv](maks_inklusiv.md) | Inklusiv maksimumsverdi (xsd:maxInclusive) |
| [maks_lengde](maks_lengde.md) | Maksimal lengd av strengen (xsd:maxLength) |
| [maks_multiplisitet](maks_multiplisitet.md) | Høgste multiplisitet — heltalstal, "n" eller "*" (modelldcatno:maxOccurs) |
| [min_eksklusiv](min_eksklusiv.md) | Eksklusiv minimumsverdi (xsd:minExclusive) |
| [min_inklusiv](min_inklusiv.md) | Inklusiv minimumsverdi (xsd:minInclusive) |
| [min_lengde](min_lengde.md) | Minimal lengd av strengen (xsd:minLength) |
| [min_multiplisitet](min_multiplisitet.md) | Minste multiplisitet for eigenskapen (modelldcatno:minOccurs) |
| [modell](modell.md) | Informasjonsmodellar i modelkatalogen (modelldcatno:model) |
| [monster](monster.md) | Regulært uttrykk for tillate strengverdiar (xsd:pattern) |
| [namn_aktor](namn_aktor.md) | Namn på aktøren (foaf:name) |
| [navigerbar](navigerbar.md) | Om eigenskapen er navigerbar i begge retningar (modelldcatno:navigable) |
| [neste](neste.md) | Neste kodeelement i ein ordna kodeliste (xkos:next) |
| [nokkelord](nokkelord.md) | Nøkkelord som beskriv ressursen (dcat:keyword) |
| [notasjon](notasjon.md) | Kode/notasjon for kodeelementet (skos:notation) |
| [notat](notat.md) | Generelt notat om kodeelementet (skos:note) |
| [omfangsnotat](omfangsnotat.md) | Notat om omfanget til kodeelementet (skos:scopeNote) |
| [refererer_til](refererer_til.md) | Modellelement som eigenskapen refererer til (modelldcatno:refersTo) |
| [relasjonsegenskapetikett](relasjonsegenskapetikett.md) | Lesetekst for eigenskapen i ein relasjon (modelldcatno:relationPropertyLabel) |
| [sekvensnummer](sekvensnummer.md) | Sekvensnummer for eigenskapen i modellelementet (modelldcatno:sequenceNumber) |
| [skapar](skapar.md) | Aktøren som primært har skapt ressursen (dct:creator) |
| [skjult_term](skjult_term.md) | Skjult term for kodeelementet (skos:hiddenLabel) |
| [sluttdato](sluttdato.md) | Sluttdato for tidsperioden (dcat:endDate) |
| [sprak](sprak.md) | Språk brukt i ressursen (dct:language) |
| [startdato](startdato.md) | Startdato for tidsperioden (dcat:startDate) |
| [status](status.md) | Status for ressursen frå eit kontrollert vokabular (adms:status) |
| [tema](tema.md) | Tema frå eit kontrollert vokabular (dcat:theme) |
| [temaer](temaer.md) | Temavokabular brukt i katalogen (dcat:themeTaxonomy) |
| [tidsperiode](tidsperiode.md) | Tidsperiode ressursen dekkar (dct:temporal) |
| [tilhorer_modul](tilhorer_modul.md) | Modul dette elementet tilhøyrer (modelldcatno:belongsToModule) |
| [tittel](tittel.md) | Namn/tittel på ressursen (dct:title) |
| [topp_begrep_av](topp_begrep_av.md) | Kodeliste dette kodeelementet er eit toppomgrep av (skos:topConceptOf) |
| [totalt_sifre](totalt_sifre.md) | Maks totalt tal på siffer (xsd:totalDigits) |
| [type_concept](type_concept.md) | Type ressurs frå eit kontrollert vokabular (dct:type) |
| [typedefinisjon_referanse](typedefinisjon_referanse.md) | Referanse til typedefinisjon (modelldcatno:typeDefinitionReference) |
| [utgivelsesdato](utgivelsesdato.md) | Dato ressursen vart første gong publisert (dct:issued) |
| [utgiver](utgiver.md) | Aktøren ansvarleg for å tilgjengeleggjere ressursen (dct:publisher) |
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
