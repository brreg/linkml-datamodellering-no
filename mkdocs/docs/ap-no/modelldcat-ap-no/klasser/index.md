# ModelDCAT-AP-NO

Norsk applikasjonsprofil for beskriving av informasjonsmodellar i DCAT-format, modellert i LinkML. Basert på https://data.norge.no/specification/modelldcat-ap-no

URI: https://data.norge.no/linkml/modelldcat-ap-no

Name: modelldcat-ap-no



## Classes





### Obligatorisk

| Class | Description |
| --- | --- |
| [Aktor](aktor.md) | Ein aktør (person, organisasjon eller system) med ansvar for ein ressurs |
| [Betingelsesregel](betingelsesregel.md) | Ein betingelsesregel — ei formell avgrensing på modellelement eller eigenskap... |
| [Informasjonsmodell](informasjonsmodell.md) | Ein informasjonsmodell som er katalogisert i ein modelkatalog (modelldcatno:I... |
| [Kodeelement](kodeelement.md) | Eit element i ei kodeliste (modelldcatno:CodeElement) |
| [Modelkatalog](modelkatalog.md) | Ei kuratert samling av metadata om informasjonsmodellar (dcat:Catalog) |
| [Modellelement](modellelement.md) | Abstrakt basisklasse for alle modellelement i ein informasjonsmodell |
| [Standard](standard.md) | Ein standard (dct:Standard) |




### Anbefalt

| Class | Description |
| --- | --- |
| [Abstraksjon](abstraksjon.md) | Ein abstraksjon — ein forenkling som representerer eit modellelement |
| [Assosiasjon](assosiasjon.md) | Ein assosiasjon — ein eigenskap som refererer til eit anna modellelement |
| [Attributt](attributt.md) | Ein attributt — ein eigenskap med ein datatype eller enkel type som verdi |
| [Avhengighet](avhengighet.md) | Ein avhengighet — ein relasjon der det eine modellelementet avheng av det and... |
| [Eigenskap](eigenskap.md) | Abstrakt basisklasse for eigenskapar knytt til eit modellelement |
| [EnkelType](enkeltype.md) | Ein enkel type med restriksjonar (xsd-fasettar) |
| [Merknad](merknad.md) | Ei merknad knytt til eit modellelement eller eigenskap |
| [Realisering](realisering.md) | Ein realisering — ein implementasjonsrelasjon mellom modellelement |
| [Rolle](rolle.md) | Ein rolle — ein eigenskap som knyter ein objekttype til ein assosiasjon |
| [Sammensetning](sammensetning.md) | Ein sammensetning — ein sterk eigarelskapsrelasjon mellom modellelement |
| [Spesialisering](spesialisering.md) | Ein spesialisering — eit arveforhold frå eit spesielt til eit generelt modell... |
| [Valg](valg.md) | Eit val — ein eigenskap som representerer eit val mellom modellelement |






### Andre

| Class | Description |
| --- | --- |
| [AlleAv](alleav.md) | Alle av — alle modellelementa i lista må gjelde (logisk OG-mengd) |
| [Datatype](datatype.md) | Ein datatype — ein strukturert samansett type |
| [Dokument](dokument.md) | Eit dokument (foaf:Document) |
| [Eller](eller.md) | Eller — logisk ELLER-betingelse; minst eitt modellelement må gjelde |
| [Ikke](ikke.md) | Ikkje — negasjon; modellelementet det refererer til må ikkje gjelde |
| [KatalogisertRessurs](katalogisertressurs.md) | Basisklasse for ressursar som kan katalogiserast (dcat:Resource) |
| [Kodeliste](kodeliste.md) | Ei kodeliste — eit kontrollert vokabular av tillate verdiar |
| [Kontaktopplysning](kontaktopplysning.md) | Kontaktinformasjon (vcard:Organization) |
| [Lisensdokument](lisensdokument.md) | Eit lisensdokument (dct:LicenseDocument) |
| [Lokasjon](lokasjon.md) | Eit geografisk område (dct:Location) |
| [Modul](modul.md) | Ein modul som grupperer modellelement i informasjonsmodellen |
| [NoenAv](noenav.md) | Nokon av — minst eitt modellelement i lista må gjelde (logisk ELLER-mengd) |
| [Objekttype](objekttype.md) | Ein objekttype — ein klasse med eigenskapar i informasjonsmodellen |
| [Og](og.md) | Og — logisk OG-betingelse; alle deltakande modellelement må gjelde |
| [RootObjekttype](rootobjekttype.md) | Ein rotobjekttype — toppnivå-klasse i informasjonsmodellen |
| [Samling](samling.md) | Ein samling — ein eigenskap som representerer ei uordna mengd av modellelemen... |
| [Tidsperiode](tidsperiode.md) | Eit tidsintervall med start- og sluttdato |
| [XEllerY](xellery.md) | Xor — eksklusiv ELLER-betingelse; nøyaktig eitt modellelement må gjelde |





## Slots

| Slot | Description |
| --- | --- |
| [alternativ_term](alternativ_term.md) | Alternativ term for kodeelementet (skos:altLabel) |
| [annoterer](annoterer.md) | Modellelement denne merknaden gjeld (modelldcatno:annotates) |
| [avhengig_av](avhengig_av.md) | Modellelement dette elementet avheng av (modelldcatno:dependentOn) |
| [begrep](begrep.md) | Fagomgrep ressursen handlar om (dct:subject) |
| [betingelsesuttrykk](betingelsesuttrykk.md) | Formelt uttrykk for betingelsesregelen (modelldcatno:constraintExpression) |
| [betinger](betinger.md) | Modellelement betingelsesregelen avgrensar (modelldcatno:constrains) |
| [danner_symmetri_med](danner_symmetri_med.md) | Eigenskap som denne eigenskapen dannar symmetri med (modelldcatno:formsSymmet... |
| [definisjon](definisjon.md) | Definisjon av kodeelementet (skos:definition) |
| [eigenskapsmerknad](eigenskapsmerknad.md) | Fritekstmerknad om ein eigenskap (modelldcatno:propertyNote) |
| [eksempel_kode](eksempel_kode.md) | Eksempel på bruk av kodeelementet (skos:example) |
| [eksklusjonsnotat](eksklusjonsnotat.md) | Notat om kva som er ekskludert frå kodeelementet (xkos:exclusionNote) |
| [er_abstraksjon_av](er_abstraksjon_av.md) | Modellelement denne abstraksjonen representerer (modelldcatno:isAbstractionOf... |
| [er_del_av_katalog](er_del_av_katalog.md) | Overordna modelkatalog (dct:isPartOf) |
| [er_del_av_modell](er_del_av_modell.md) | Overordna informasjonsmodell (dct:isPartOf) |
| [er_erstatta_av](er_erstatta_av.md) | Informasjonsmodell som erstattar denne (dct:isReplacedBy) |
| [er_i_samsvar_med](er_i_samsvar_med.md) | Standard ressursen er i samsvar med (dct:conformsTo) |
| [er_profil_av](er_profil_av.md) | Standard denne informasjonsmodellen er ein profil av (prof:isProfileOf) |
| [erstatter](erstatter.md) | Informasjonsmodell som denne erstattar (dct:replaces) |
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
| [har_noe](har_noe.md) | Modellelement som inngår i valet (modelldcatno:hasSome) |
| [har_objekttype](har_objekttype.md) | Objekttype knytt til rolla (modelldcatno:hasObjectType) |
| [har_type](har_type.md) | Type modellelement for eigenskapen (modelldcatno:hasType) |
| [har_verdi_fra](har_verdi_fra.md) | Kodeliste for tillate verdiar til attributten (modelldcatno:hasValueFrom) |
| [i_skjema](i_skjema.md) | Kodeliste dette kodeelementet tilhøyrer (skos:inScheme) |
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
| [notasjon](notasjon.md) | Kode/notasjon for kodeelementet (skos:notation) |
| [notat](notat.md) | Generelt notat om kodeelementet (skos:note) |
| [omfangsnotat](omfangsnotat.md) | Notat om omfanget til kodeelementet (skos:scopeNote) |
| [refererer_til](refererer_til.md) | Modellelement som eigenskapen refererer til (modelldcatno:refersTo) |
| [relasjonsegenskapetikett](relasjonsegenskapetikett.md) | Lesetekst for eigenskapen i ein relasjon (modelldcatno:relationPropertyLabel) |
| [sekvensnummer](sekvensnummer.md) | Sekvensnummer for eigenskapen i modellelementet (modelldcatno:sequenceNumber) |
| [skapar](skapar.md) | Aktøren som primært har skapt ressursen (dct:creator) |
| [skjult_term](skjult_term.md) | Skjult term for kodeelementet (skos:hiddenLabel) |
| [sluttdato](sluttdato.md) | Sluttdato for tidsperioden (dcat:endDate) |
| [startdato](startdato.md) | Startdato for tidsperioden (dcat:startDate) |
| [tema](tema.md) | Tema frå eit kontrollert vokabular (dcat:theme) |
| [temaer](temaer.md) | Temavokabular brukt i katalogen (dcat:themeTaxonomy) |
| [tidsperiode](tidsperiode.md) | Tidsperiode ressursen dekkar (dct:temporal) |
| [tilhorer_modul](tilhorer_modul.md) | Modul dette elementet tilhøyrer (modelldcatno:belongsToModule) |
| [topp_begrep_av](topp_begrep_av.md) | Kodeliste dette kodeelementet er eit toppomgrep av (skos:topConceptOf) |
| [totalt_sifre](totalt_sifre.md) | Maks totalt tal på siffer (xsd:totalDigits) |
| [typedefinisjon_referanse](typedefinisjon_referanse.md) | Referanse til typedefinisjon (modelldcatno:typeDefinitionReference) |
| [utgiver](utgiver.md) | Aktøren ansvarleg for å tilgjengeleggjere ressursen (dct:publisher) |


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
