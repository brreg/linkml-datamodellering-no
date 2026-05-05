# modelldcat-ap-no

## Artefacts

| Artefakt | Fil |
|----------|-----|
| SHACL shapes | [modelldcat-ap-no-shapes.ttl](modelldcat-ap-no-shapes.ttl) |
| JSON-LD kontekst | [modelldcat-ap-no-context.jsonld](modelldcat-ap-no-context.jsonld) |
| JSON Schema | [modelldcat-ap-no-schema.json](modelldcat-ap-no-schema.json) |
| OWL ontologi | [modelldcat-ap-no-ontology.ttl](modelldcat-ap-no-ontology.ttl) |
| RDF/Turtle skjema | [modelldcat-ap-no-schema.ttl](modelldcat-ap-no-schema.ttl) |
| Python-klasser | [modelldcat-ap-no-model.py](modelldcat-ap-no-model.py) |
| ER-diagram (Mermaid) | [modelldcat-ap-no-erdiagram.md](modelldcat-ap-no-erdiagram.md) |
| Eksempeldata (Turtle) | [modelldcat-ap-no-eksempel.ttl](modelldcat-ap-no-eksempel.ttl) |

## Oversiktsdiagram

```mermaid
erDiagram
Abstraksjon {
    uriorcurie id  
    LangStringList beskrivelse  
    string identifikator_literal  
    string maks_multiplisitet  
    NonNegativeInteger min_multiplisitet  
    boolean navigerbar  
    LangStringList relasjonsegenskapetikett  
    NonNegativeInteger sekvensnummer  
    LangStringList tittel  
}
Aktor {
    uriorcurie id  
    string identifikator_literal  
    LangStringList namn_aktor  
}
AlleAv {
    uriorcurie id  
    LangStringList beskrivelse  
    string identifikator_literal  
    string maks_multiplisitet  
    NonNegativeInteger min_multiplisitet  
    boolean navigerbar  
    LangStringList relasjonsegenskapetikett  
    NonNegativeInteger sekvensnummer  
    LangStringList tittel  
}
Assosiasjon {
    uriorcurie id  
    LangStringList beskrivelse  
    string identifikator_literal  
    string maks_multiplisitet  
    NonNegativeInteger min_multiplisitet  
    boolean navigerbar  
    LangStringList relasjonsegenskapetikett  
    NonNegativeInteger sekvensnummer  
    LangStringList tittel  
}
Attributt {
    uriorcurie id  
    LangStringList beskrivelse  
    string identifikator_literal  
    string maks_multiplisitet  
    NonNegativeInteger min_multiplisitet  
    boolean navigerbar  
    LangStringList relasjonsegenskapetikett  
    NonNegativeInteger sekvensnummer  
    LangStringList tittel  
}
Avhengighet {
    uriorcurie id  
    LangStringList beskrivelse  
    string identifikator_literal  
    string maks_multiplisitet  
    NonNegativeInteger min_multiplisitet  
    boolean navigerbar  
    LangStringList relasjonsegenskapetikett  
    NonNegativeInteger sekvensnummer  
    LangStringList tittel  
}
Begrepssamling {
    uriorcurie id  
}
Betingelsesregel {
    LangStringList betingelsesuttrykk  
    uriorcurie id  
    LangStringList eigenskapsmerknad  
    string identifikator_literal  
    LangStringList tittel  
}
Datatype {
    uriorcurie id  
    LangStringList beskrivelse  
    string identifikator_literal  
    LangStringList tittel  
}
Dokument {
    uriorcurie id  
    LangStringList tittel  
}
Eigenskap {
    uriorcurie id  
    LangStringList beskrivelse  
    string identifikator_literal  
    string maks_multiplisitet  
    NonNegativeInteger min_multiplisitet  
    boolean navigerbar  
    LangStringList relasjonsegenskapetikett  
    NonNegativeInteger sekvensnummer  
    LangStringList tittel  
}
Eller {
    uriorcurie id  
    LangStringList betingelsesuttrykk  
    LangStringList eigenskapsmerknad  
    string identifikator_literal  
    LangStringList tittel  
}
EnkelType {
    NonNegativeInteger fraksjonssifre  
    NonNegativeInteger lengde  
    string maks_eksklusiv  
    string maks_inklusiv  
    NonNegativeInteger maks_lengde  
    string min_eksklusiv  
    string min_inklusiv  
    NonNegativeInteger min_lengde  
    string monster  
    NonNegativeInteger totalt_sifre  
    uri typedefinisjon_referanse  
    uriorcurie id  
    LangStringList beskrivelse  
    string identifikator_literal  
    LangStringList tittel  
}
Ikke {
    uriorcurie id  
    LangStringList betingelsesuttrykk  
    LangStringList eigenskapsmerknad  
    string identifikator_literal  
    LangStringList tittel  
}
Informasjonsmodell {
    uriorcurie id  
    LangStringList beskrivelse  
    date endringsdato  
    string har_versjonsnummer  
    uriList heimeside  
    string identifikator_literal  
    string informasjonsmodellidentifikator  
    LangStringList nokkelord  
    LangStringList tittel  
    date utgivelsesdato  
    LangStringList versjonsmerknad  
}
KatalogisertRessurs {
    uriorcurie id  
}
Kodeelement {
    uriorcurie id  
    LangStringList alternativ_term  
    LangStringList anbefalt_term  
    LangStringList definisjon  
    LangStringList eksempel_kode  
    LangStringList eksklusjonsnotat  
    string identifikator_literal  
    LangStringList inklusjonsnotat  
    string notasjon  
    LangStringList notat  
    LangStringList omfangsnotat  
    LangStringList skjult_term  
}
Kodeliste {
    uriList har_referanse  
    uriorcurie id  
    LangStringList beskrivelse  
    string identifikator_literal  
    LangStringList tittel  
}
Konsept {
    uriorcurie id  
}
Kontaktopplysning {
    uriorcurie id  
}
Lisensdokument {
    uriorcurie id  
}
Lokasjon {
    uriorcurie id  
}
Mediatype {
    uriorcurie id  
}
Merknad {
    uriorcurie id  
    LangStringList eigenskapsmerknad  
    string identifikator_literal  
    LangStringList tittel  
}
Modelkatalog {
    uriorcurie id  
    LangStringList beskrivelse  
    date endringsdato  
    uriList heimeside  
    string identifikator_literal  
    LangStringList tittel  
    date utgivelsesdato  
}
Modellelement {
    uriorcurie id  
    LangStringList beskrivelse  
    string identifikator_literal  
    LangStringList tittel  
}
Modul {
    uriorcurie id  
    LangStringList beskrivelse  
    string identifikator_literal  
    LangStringList tittel  
}
NoenAv {
    uriorcurie id  
    LangStringList beskrivelse  
    string identifikator_literal  
    string maks_multiplisitet  
    NonNegativeInteger min_multiplisitet  
    boolean navigerbar  
    LangStringList relasjonsegenskapetikett  
    NonNegativeInteger sekvensnummer  
    LangStringList tittel  
}
Objekttype {
    uriorcurie id  
    LangStringList beskrivelse  
    string identifikator_literal  
    LangStringList tittel  
}
Og {
    uriorcurie id  
    LangStringList betingelsesuttrykk  
    LangStringList eigenskapsmerknad  
    string identifikator_literal  
    LangStringList tittel  
}
Realisering {
    uriorcurie id  
    LangStringList beskrivelse  
    string identifikator_literal  
    string maks_multiplisitet  
    NonNegativeInteger min_multiplisitet  
    boolean navigerbar  
    LangStringList relasjonsegenskapetikett  
    NonNegativeInteger sekvensnummer  
    LangStringList tittel  
}
Rolle {
    uriorcurie id  
    LangStringList beskrivelse  
    string identifikator_literal  
    string maks_multiplisitet  
    NonNegativeInteger min_multiplisitet  
    boolean navigerbar  
    LangStringList relasjonsegenskapetikett  
    NonNegativeInteger sekvensnummer  
    LangStringList tittel  
}
RootObjekttype {
    uriorcurie id  
    LangStringList beskrivelse  
    string identifikator_literal  
    LangStringList tittel  
}
Samling {
    uriorcurie id  
    LangStringList beskrivelse  
    string identifikator_literal  
    string maks_multiplisitet  
    NonNegativeInteger min_multiplisitet  
    boolean navigerbar  
    LangStringList relasjonsegenskapetikett  
    NonNegativeInteger sekvensnummer  
    LangStringList tittel  
}
Sammensetning {
    uriorcurie id  
    LangStringList beskrivelse  
    string identifikator_literal  
    string maks_multiplisitet  
    NonNegativeInteger min_multiplisitet  
    boolean navigerbar  
    LangStringList relasjonsegenskapetikett  
    NonNegativeInteger sekvensnummer  
    LangStringList tittel  
}
Spesialisering {
    uriorcurie id  
    LangStringList beskrivelse  
    string identifikator_literal  
    string maks_multiplisitet  
    NonNegativeInteger min_multiplisitet  
    boolean navigerbar  
    LangStringList relasjonsegenskapetikett  
    NonNegativeInteger sekvensnummer  
    LangStringList tittel  
}
Spraak {
    uriorcurie id  
}
Standard {
    uriorcurie id  
    uriList har_referanse  
    string har_versjonsnummer  
    LangStringList tittel  
}
Tidsperiode {
    uriorcurie id  
    date sluttdato  
    date startdato  
}
Valg {
    uriorcurie id  
    LangStringList beskrivelse  
    string identifikator_literal  
    string maks_multiplisitet  
    NonNegativeInteger min_multiplisitet  
    boolean navigerbar  
    LangStringList relasjonsegenskapetikett  
    NonNegativeInteger sekvensnummer  
    LangStringList tittel  
}
XEllerY {
    uriorcurie id  
    LangStringList betingelsesuttrykk  
    LangStringList eigenskapsmerknad  
    string identifikator_literal  
    LangStringList tittel  
}

Abstraksjon ||--|o Eigenskap : "danner_symmetri_med"
Abstraksjon ||--|o Modellelement : "er_abstraksjon_av"
Abstraksjon ||--}o Konsept : "begrep"
Abstraksjon ||--}o Modellelement : "har_type"
Abstraksjon ||--}o Modul : "tilhorer_modul"
Aktor ||--|o Konsept : "type_concept"
AlleAv ||--|o Eigenskap : "danner_symmetri_med"
AlleAv ||--}o Konsept : "begrep"
AlleAv ||--}o Modellelement : "har_noe, har_type"
AlleAv ||--}o Modul : "tilhorer_modul"
Assosiasjon ||--|o Eigenskap : "danner_symmetri_med"
Assosiasjon ||--|o Modellelement : "refererer_til"
Assosiasjon ||--}o Konsept : "begrep"
Assosiasjon ||--}o Modellelement : "har_type"
Assosiasjon ||--}o Modul : "tilhorer_modul"
Attributt ||--|o Eigenskap : "danner_symmetri_med"
Attributt ||--}o Datatype : "har_datatype"
Attributt ||--}o EnkelType : "har_enkel_type"
Attributt ||--}o Kodeliste : "har_verdi_fra"
Attributt ||--}o Konsept : "begrep"
Attributt ||--}o Modellelement : "har_type"
Attributt ||--}o Modul : "tilhorer_modul"
Attributt ||--}o Objekttype : "inneholder_objekttype"
Avhengighet ||--|o Eigenskap : "danner_symmetri_med"
Avhengighet ||--|o Modellelement : "avhengig_av"
Avhengighet ||--}o Konsept : "begrep"
Avhengighet ||--}o Modellelement : "har_type"
Avhengighet ||--}o Modul : "tilhorer_modul"
Betingelsesregel ||--}o Modellelement : "annoterer"
Betingelsesregel ||--}o Modul : "tilhorer_modul"
Betingelsesregel ||--}| Modellelement : "betinger"
Datatype ||--}o Eigenskap : "har_eigenskap"
Datatype ||--}o Konsept : "begrep"
Datatype ||--}o Modul : "tilhorer_modul"
Dokument ||--|o Mediatype : "format"
Dokument ||--}o Spraak : "sprak"
Eigenskap ||--|o Eigenskap : "danner_symmetri_med"
Eigenskap ||--}o Konsept : "begrep"
Eigenskap ||--}o Modellelement : "har_type"
Eigenskap ||--}o Modul : "tilhorer_modul"
Eller ||--}o Modellelement : "annoterer"
Eller ||--}o Modul : "tilhorer_modul"
Eller ||--}| Modellelement : "betinger"
EnkelType ||--}o Eigenskap : "har_eigenskap"
EnkelType ||--}o Konsept : "begrep"
EnkelType ||--}o Modul : "tilhorer_modul"
Ikke ||--}o Modellelement : "annoterer"
Ikke ||--}o Modul : "tilhorer_modul"
Ikke ||--}| Modellelement : "betinger"
Informasjonsmodell ||--|o Aktor : "skapar"
Informasjonsmodell ||--|o Konsept : "status, type_concept"
Informasjonsmodell ||--|o Lisensdokument : "lisens"
Informasjonsmodell ||--|| Aktor : "utgiver"
Informasjonsmodell ||--}o Dokument : "har_format"
Informasjonsmodell ||--}o Informasjonsmodell : "er_del_av_modell, er_erstatta_av, erstatter, har_del_modell"
Informasjonsmodell ||--}o Konsept : "begrep, dekningsomrade, tema"
Informasjonsmodell ||--}o Kontaktopplysning : "kontaktpunkt"
Informasjonsmodell ||--}o Modellelement : "inneholder_modellelement"
Informasjonsmodell ||--}o Spraak : "sprak"
Informasjonsmodell ||--}o Standard : "er_i_samsvar_med, er_profil_av"
Informasjonsmodell ||--}o Tidsperiode : "tidsperiode"
Kodeelement ||--|o Kodeelement : "forrige, neste"
Kodeelement ||--}o Kodeliste : "topp_begrep_av"
Kodeelement ||--}o Konsept : "begrep"
Kodeelement ||--}| Kodeliste : "i_skjema"
Kodeliste ||--}o Eigenskap : "har_eigenskap"
Kodeliste ||--}o Konsept : "begrep"
Kodeliste ||--}o Modul : "tilhorer_modul"
Lisensdokument ||--|o Konsept : "type_concept"
Merknad ||--}o Modellelement : "annoterer"
Merknad ||--}o Modul : "tilhorer_modul"
Modelkatalog ||--|o Lisensdokument : "lisens"
Modelkatalog ||--|o Modelkatalog : "er_del_av_katalog"
Modelkatalog ||--|| Aktor : "utgiver"
Modelkatalog ||--}o Begrepssamling : "temaer"
Modelkatalog ||--}o Informasjonsmodell : "modell"
Modelkatalog ||--}o Konsept : "tema"
Modelkatalog ||--}o Spraak : "sprak"
Modelkatalog ||--}| KatalogisertRessurs : "har_del"
Modelkatalog ||--}| Kontaktopplysning : "kontaktpunkt"
Modellelement ||--}o Eigenskap : "har_eigenskap"
Modellelement ||--}o Konsept : "begrep"
Modellelement ||--}o Modul : "tilhorer_modul"
Modul ||--}o Eigenskap : "har_eigenskap"
Modul ||--}o Konsept : "begrep"
Modul ||--}o Modul : "tilhorer_modul"
NoenAv ||--|o Eigenskap : "danner_symmetri_med"
NoenAv ||--}o Konsept : "begrep"
NoenAv ||--}o Modellelement : "har_noe, har_type"
NoenAv ||--}o Modul : "tilhorer_modul"
Objekttype ||--}o Eigenskap : "har_eigenskap"
Objekttype ||--}o Konsept : "begrep"
Objekttype ||--}o Modul : "tilhorer_modul"
Og ||--}o Modellelement : "annoterer"
Og ||--}o Modul : "tilhorer_modul"
Og ||--}| Modellelement : "betinger"
Realisering ||--|o Eigenskap : "danner_symmetri_med"
Realisering ||--|o Modellelement : "har_leverandor"
Realisering ||--}o Konsept : "begrep"
Realisering ||--}o Modellelement : "har_type"
Realisering ||--}o Modul : "tilhorer_modul"
Rolle ||--|o Eigenskap : "danner_symmetri_med"
Rolle ||--|o Objekttype : "har_objekttype"
Rolle ||--}o Konsept : "begrep"
Rolle ||--}o Modellelement : "har_type"
Rolle ||--}o Modul : "tilhorer_modul"
RootObjekttype ||--}o Eigenskap : "har_eigenskap"
RootObjekttype ||--}o Konsept : "begrep"
RootObjekttype ||--}o Modul : "tilhorer_modul"
Samling ||--|o Eigenskap : "danner_symmetri_med"
Samling ||--}o Konsept : "begrep"
Samling ||--}o Modellelement : "har_type"
Samling ||--}o Modul : "tilhorer_modul"
Sammensetning ||--|o Eigenskap : "danner_symmetri_med"
Sammensetning ||--|o Modellelement : "inneholder"
Sammensetning ||--}o Konsept : "begrep"
Sammensetning ||--}o Modellelement : "har_type"
Sammensetning ||--}o Modul : "tilhorer_modul"
Spesialisering ||--|o Eigenskap : "danner_symmetri_med"
Spesialisering ||--|o Modellelement : "har_generelt_begrep"
Spesialisering ||--}o Konsept : "begrep"
Spesialisering ||--}o Modellelement : "har_type"
Spesialisering ||--}o Modul : "tilhorer_modul"
Valg ||--|o Eigenskap : "danner_symmetri_med"
Valg ||--}o Konsept : "begrep"
Valg ||--}o Modellelement : "har_noe, har_type"
Valg ||--}o Modul : "tilhorer_modul"
XEllerY ||--}o Modellelement : "annoterer"
XEllerY ||--}o Modul : "tilhorer_modul"
XEllerY ||--}| Modellelement : "betinger"

```



Norsk applikasjonsprofil for beskriving av informasjonsmodellar i DCAT-format, modellert i LinkML. Basert på https://data.norge.no/specification/modelldcat-ap-no

URI: https://data.norge.no/linkml/modelldcat-ap-no

Name: modelldcat-ap-no



## Classes

| Class | Description |
| --- | --- |
| [Aktor](klasser/aktor.md) | Ein aktør (person, organisasjon eller system) med ansvar for ein ressurs |
| [Begrepssamling](klasser/begrepssamling.md) | Ei SKOS-omgrepssamling (temavokabular) |
| [Dokument](klasser/dokument.md) | Eit dokument (foaf:Document) |
| [Eigenskap](klasser/eigenskap.md) | Abstrakt basisklasse for eigenskapar knytt til eit modellelement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Abstraksjon](klasser/abstraksjon.md) | Ein abstraksjon — ein forenkling som representerer eit modellelement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Assosiasjon](klasser/assosiasjon.md) | Ein assosiasjon — ein eigenskap som refererer til eit anna modellelement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Attributt](klasser/attributt.md) | Ein attributt — ein eigenskap med ein datatype eller enkel type som verdi |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Avhengighet](klasser/avhengighet.md) | Ein avhengighet — ein relasjon der det eine modellelementet avheng av det and... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Realisering](klasser/realisering.md) | Ein realisering — ein implementasjonsrelasjon mellom modellelement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Rolle](klasser/rolle.md) | Ein rolle — ein eigenskap som knyter ein objekttype til ein assosiasjon |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Samling](klasser/samling.md) | Ein samling — ein eigenskap som representerer ei uordna mengd av modellelemen... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Sammensetning](klasser/sammensetning.md) | Ein sammensetning — ein sterk eigarelskapsrelasjon mellom modellelement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Spesialisering](klasser/spesialisering.md) | Ein spesialisering — eit arveforhold frå eit spesielt til eit generelt modell... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Valg](klasser/valg.md) | Eit val — ein eigenskap som representerer eit val mellom modellelement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AlleAv](klasser/alleav.md) | Alle av — alle modellelementa i lista må gjelde (logisk OG-mengd) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NoenAv](klasser/noenav.md) | Nokon av — minst eitt modellelement i lista må gjelde (logisk ELLER-mengd) |
| [Informasjonsmodell](klasser/informasjonsmodell.md) | Ein informasjonsmodell som er katalogisert i ein modelkatalog (modelldcatno:I... |
| [KatalogisertRessurs](klasser/katalogisertressurs.md) | Basisklasse for ressursar som kan katalogiserast (dcat:Resource) |
| [Kodeelement](klasser/kodeelement.md) | Eit element i ei kodeliste (modelldcatno:CodeElement) |
| [Konsept](klasser/konsept.md) | Referanse til eit SKOS-omgrep frå eit kontrollert vokabular |
| [Kontaktopplysning](klasser/kontaktopplysning.md) | Kontaktinformasjon (vcard:Organization) |
| [Lisensdokument](klasser/lisensdokument.md) | Eit lisensdokument (dct:LicenseDocument) |
| [Lokasjon](klasser/lokasjon.md) | Eit geografisk område (dct:Location) |
| [Mediatype](klasser/mediatype.md) | Ein medietype eller filformat (dct:MediaTypeOrExtent) |
| [Merknad](klasser/merknad.md) | Ei merknad knytt til eit modellelement eller eigenskap |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Betingelsesregel](klasser/betingelsesregel.md) | Ein betingelsesregel — ei formell avgrensing på modellelement eller eigenskap... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Eller](klasser/eller.md) | Eller — logisk ELLER-betingelse; minst eitt modellelement må gjelde |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Ikke](klasser/ikke.md) | Ikkje — negasjon; modellelementet det refererer til må ikkje gjelde |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Og](klasser/og.md) | Og — logisk OG-betingelse; alle deltakande modellelement må gjelde |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XEllerY](klasser/xellery.md) | Xor — eksklusiv ELLER-betingelse; nøyaktig eitt modellelement må gjelde |
| [Modelkatalog](klasser/modelkatalog.md) | Ei kuratert samling av metadata om informasjonsmodellar (dcat:Catalog) |
| [Modellelement](klasser/modellelement.md) | Abstrakt basisklasse for alle modellelement i ein informasjonsmodell |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Datatype](klasser/datatype.md) | Ein datatype — ein strukturert samansett type |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EnkelType](klasser/enkeltype.md) | Ein enkel type med restriksjonar (xsd-fasettar) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kodeliste](klasser/kodeliste.md) | Ei kodeliste — eit kontrollert vokabular av tillate verdiar |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Modul](klasser/modul.md) | Ein modul som grupperer modellelement i informasjonsmodellen |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Objekttype](klasser/objekttype.md) | Ein objekttype — ein klasse med eigenskapar i informasjonsmodellen |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RootObjekttype](klasser/rootobjekttype.md) | Ein rotobjekttype — toppnivå-klasse i informasjonsmodellen |
| [Spraak](klasser/spraak.md) | Ein språkreferanse (dct:LinguisticSystem) |
| [Standard](klasser/standard.md) | Ein standard (dct:Standard) |
| [Tidsperiode](klasser/tidsperiode.md) | Eit tidsintervall med start- og sluttdato |



## Slots

| Slot | Description |
| --- | --- |
| [alternativ_term](klasser/alternativ_term.md) | Alternativ term for kodeelementet (skos:altLabel) |
| [anbefalt_term](klasser/anbefalt_term.md) | Føretrukke term/namn for ressursen (skos:prefLabel) |
| [annoterer](klasser/annoterer.md) | Modellelement denne merknaden gjeld (modelldcatno:annotates) |
| [avhengig_av](klasser/avhengig_av.md) | Modellelement dette elementet avheng av (modelldcatno:dependentOn) |
| [begrep](klasser/begrep.md) | Fagomgrep ressursen handlar om (dct:subject) |
| [beskrivelse](klasser/beskrivelse.md) | Fritekstbeskrivelse av ressursen (dct:description) |
| [betingelsesuttrykk](klasser/betingelsesuttrykk.md) | Formelt uttrykk for betingelsesregelen (modelldcatno:constraintExpression) |
| [betinger](klasser/betinger.md) | Modellelement betingelsesregelen avgrensar (modelldcatno:constrains) |
| [danner_symmetri_med](klasser/danner_symmetri_med.md) | Eigenskap som denne eigenskapen dannar symmetri med (modelldcatno:formsSymmet... |
| [definisjon](klasser/definisjon.md) | Definisjon av kodeelementet (skos:definition) |
| [dekningsomrade](klasser/dekningsomrade.md) | Geografisk dekningsområde (dct:spatial) |
| [eigenskapsmerknad](klasser/eigenskapsmerknad.md) | Fritekstmerknad om ein eigenskap (modelldcatno:propertyNote) |
| [eksempel_kode](klasser/eksempel_kode.md) | Eksempel på bruk av kodeelementet (skos:example) |
| [eksklusjonsnotat](klasser/eksklusjonsnotat.md) | Notat om kva som er ekskludert frå kodeelementet (xkos:exclusionNote) |
| [endringsdato](klasser/endringsdato.md) | Dato for siste endring av ressursen (dct:modified) |
| [er_abstraksjon_av](klasser/er_abstraksjon_av.md) | Modellelement denne abstraksjonen representerer (modelldcatno:isAbstractionOf... |
| [er_del_av_katalog](klasser/er_del_av_katalog.md) | Overordna modelkatalog (dct:isPartOf) |
| [er_del_av_modell](klasser/er_del_av_modell.md) | Overordna informasjonsmodell (dct:isPartOf) |
| [er_erstatta_av](klasser/er_erstatta_av.md) | Informasjonsmodell som erstattar denne (dct:isReplacedBy) |
| [er_i_samsvar_med](klasser/er_i_samsvar_med.md) | Standard ressursen er i samsvar med (dct:conformsTo) |
| [er_profil_av](klasser/er_profil_av.md) | Standard denne informasjonsmodellen er ein profil av (prof:isProfileOf) |
| [erstatter](klasser/erstatter.md) | Informasjonsmodell som denne erstattar (dct:replaces) |
| [format](klasser/format.md) | Filformat eller medietype (dct:format) |
| [forrige](klasser/forrige.md) | Førre kodeelement i ein ordna kodeliste (xkos:previous) |
| [fraksjonssifre](klasser/fraksjonssifre.md) | Maks tal på desimalsiffer (xsd:fractionDigits) |
| [har_datatype](klasser/har_datatype.md) | Datatype for attributten (modelldcatno:hasDataType) |
| [har_del](klasser/har_del.md) | Del-ressurs inkludert i denne katalogen (dct:hasPart) |
| [har_del_modell](klasser/har_del_modell.md) | Del-informasjonsmodell av denne modellen (dct:hasPart) |
| [har_eigenskap](klasser/har_eigenskap.md) | Eigenskapar modellelementet har (modelldcatno:hasProperty) |
| [har_enkel_type](klasser/har_enkel_type.md) | Enkel type for attributten (modelldcatno:hasSimpleType) |
| [har_format](klasser/har_format.md) | Dokument som representerer ein annan form av modellen (dct:hasFormat) |
| [har_generelt_begrep](klasser/har_generelt_begrep.md) | Det generelle modellelementet i ei spesialisering (modelldcatno:hasGeneralCon... |
| [har_leverandor](klasser/har_leverandor.md) | Leverandør-modellelement i realiseringa (modelldcatno:hasSupplier) |
| [har_merknad](klasser/har_merknad.md) | Fritekstmerknad (rdfs:comment) |
| [har_noe](klasser/har_noe.md) | Modellelement som inngår i valet (modelldcatno:hasSome) |
| [har_objekttype](klasser/har_objekttype.md) | Objekttype knytt til rolla (modelldcatno:hasObjectType) |
| [har_referanse](klasser/har_referanse.md) | Referanse til ekstern ressurs (rdfs:seeAlso) |
| [har_type](klasser/har_type.md) | Type modellelement for eigenskapen (modelldcatno:hasType) |
| [har_verdi_fra](klasser/har_verdi_fra.md) | Kodeliste for tillate verdiar til attributten (modelldcatno:hasValueFrom) |
| [har_versjonsnummer](klasser/har_versjonsnummer.md) | Versjonsnummer for ressursen (owl:versionInfo) |
| [heimeside](klasser/heimeside.md) | Heimeside for ressursen eller organisasjonen (foaf:homepage) |
| [i_skjema](klasser/i_skjema.md) | Kodeliste dette kodeelementet tilhøyrer (skos:inScheme) |
| [id](klasser/id.md) | URI-identifikator for ressursen |
| [identifikator_literal](klasser/identifikator_literal.md) | Tekstleg identifikator for ressursen (dct:identifier) |
| [informasjonsmodellidentifikator](klasser/informasjonsmodellidentifikator.md) | Identifikator for informasjonsmodellen i domenet (modelldcatno:informationMod... |
| [inklusjonsnotat](klasser/inklusjonsnotat.md) | Notat om kva som er inkludert i kodeelementet (xkos:inclusionNote) |
| [inneholder](klasser/inneholder.md) | Modellelement som er del av samansetjinga (modelldcatno:contains) |
| [inneholder_modellelement](klasser/inneholder_modellelement.md) | Modellelement som er del av informasjonsmodellen (modelldcatno:containsModelE... |
| [inneholder_objekttype](klasser/inneholder_objekttype.md) | Objekttype som attributten inneheld (modelldcatno:containsObjectType) |
| [kontaktpunkt](klasser/kontaktpunkt.md) | Kontaktinformasjon for ressursen (dcat:contactPoint) |
| [lengde](klasser/lengde.md) | Nøyaktig lengd av strengen (xsd:length) |
| [lisens](klasser/lisens.md) | Lisens for bruk av ressursen (dct:license) |
| [maks_eksklusiv](klasser/maks_eksklusiv.md) | Eksklusiv maksimumsverdi (xsd:maxExclusive) |
| [maks_inklusiv](klasser/maks_inklusiv.md) | Inklusiv maksimumsverdi (xsd:maxInclusive) |
| [maks_lengde](klasser/maks_lengde.md) | Maksimal lengd av strengen (xsd:maxLength) |
| [maks_multiplisitet](klasser/maks_multiplisitet.md) | Høgste multiplisitet — heltalstal, "n" eller "*" (modelldcatno:maxOccurs) |
| [min_eksklusiv](klasser/min_eksklusiv.md) | Eksklusiv minimumsverdi (xsd:minExclusive) |
| [min_inklusiv](klasser/min_inklusiv.md) | Inklusiv minimumsverdi (xsd:minInclusive) |
| [min_lengde](klasser/min_lengde.md) | Minimal lengd av strengen (xsd:minLength) |
| [min_multiplisitet](klasser/min_multiplisitet.md) | Minste multiplisitet for eigenskapen (modelldcatno:minOccurs) |
| [modell](klasser/modell.md) | Informasjonsmodellar i modelkatalogen (modelldcatno:model) |
| [monster](klasser/monster.md) | Regulært uttrykk for tillate strengverdiar (xsd:pattern) |
| [namn_aktor](klasser/namn_aktor.md) | Namn på aktøren (foaf:name) |
| [navigerbar](klasser/navigerbar.md) | Om eigenskapen er navigerbar i begge retningar (modelldcatno:navigable) |
| [neste](klasser/neste.md) | Neste kodeelement i ein ordna kodeliste (xkos:next) |
| [nokkelord](klasser/nokkelord.md) | Nøkkelord som beskriv ressursen (dcat:keyword) |
| [notasjon](klasser/notasjon.md) | Kode/notasjon for kodeelementet (skos:notation) |
| [notat](klasser/notat.md) | Generelt notat om kodeelementet (skos:note) |
| [omfangsnotat](klasser/omfangsnotat.md) | Notat om omfanget til kodeelementet (skos:scopeNote) |
| [refererer_til](klasser/refererer_til.md) | Modellelement som eigenskapen refererer til (modelldcatno:refersTo) |
| [relasjonsegenskapetikett](klasser/relasjonsegenskapetikett.md) | Lesetekst for eigenskapen i ein relasjon (modelldcatno:relationPropertyLabel) |
| [sekvensnummer](klasser/sekvensnummer.md) | Sekvensnummer for eigenskapen i modellelementet (modelldcatno:sequenceNumber) |
| [skapar](klasser/skapar.md) | Aktøren som primært har skapt ressursen (dct:creator) |
| [skjult_term](klasser/skjult_term.md) | Skjult term for kodeelementet (skos:hiddenLabel) |
| [sluttdato](klasser/sluttdato.md) | Sluttdato for tidsperioden (dcat:endDate) |
| [sprak](klasser/sprak.md) | Språk brukt i ressursen (dct:language) |
| [startdato](klasser/startdato.md) | Startdato for tidsperioden (dcat:startDate) |
| [status](klasser/status.md) | Status for ressursen frå eit kontrollert vokabular (adms:status) |
| [tema](klasser/tema.md) | Tema frå eit kontrollert vokabular (dcat:theme) |
| [temaer](klasser/temaer.md) | Temavokabular brukt i katalogen (dcat:themeTaxonomy) |
| [tidsperiode](klasser/tidsperiode.md) | Tidsperiode ressursen dekkar (dct:temporal) |
| [tilhorer_modul](klasser/tilhorer_modul.md) | Modul dette elementet tilhøyrer (modelldcatno:belongsToModule) |
| [tittel](klasser/tittel.md) | Namn/tittel på ressursen (dct:title) |
| [topp_begrep_av](klasser/topp_begrep_av.md) | Kodeliste dette kodeelementet er eit toppomgrep av (skos:topConceptOf) |
| [totalt_sifre](klasser/totalt_sifre.md) | Maks totalt tal på siffer (xsd:totalDigits) |
| [type_concept](klasser/type_concept.md) | Type ressurs frå eit kontrollert vokabular (dct:type) |
| [typedefinisjon_referanse](klasser/typedefinisjon_referanse.md) | Referanse til typedefinisjon (modelldcatno:typeDefinitionReference) |
| [utgivelsesdato](klasser/utgivelsesdato.md) | Dato ressursen vart første gong publisert (dct:issued) |
| [utgiver](klasser/utgiver.md) | Aktøren ansvarleg for å tilgjengeleggjere ressursen (dct:publisher) |
| [valuta](klasser/valuta.md) | Valuta (cv:currency) |
| [versjonsmerknad](klasser/versjonsmerknad.md) | Merknad om endringar i denne versjonen (adms:versionNotes) |


## Enumerations

| Enumeration | Description |
| --- | --- |


## Types

| Type | Description |
| --- | --- |
| [Boolean](klasser/boolean.md) | A binary (true or false) value |
| [Curie](klasser/curie.md) | a compact URI |
| [Date](klasser/date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](klasser/dateordatetime.md) | Either a date or a datetime |
| [Datetime](klasser/datetime.md) | The combination of a date and time |
| [Decimal](klasser/decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](klasser/double.md) | A real number that conforms to the xsd:double specification |
| [Duration](klasser/duration.md) | ISO 8601-varigheit (xsd:duration), t |
| [Float](klasser/float.md) | A real number that conforms to the xsd:float specification |
| [GYear](klasser/gyear.md) | Gregorisk årstal (xsd:gYear), t |
| [Integer](klasser/integer.md) | An integer |
| [Jsonpath](klasser/jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](klasser/jsonpointer.md) | A string encoding a JSON Pointer |
| [LangString](klasser/langstring.md) | Språktagget streng (rdf:langString) |
| [Ncname](klasser/ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](klasser/nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [NonNegativeInteger](klasser/nonnegativeinteger.md) | Ikkje-negativ heltalsverdi (xsd:nonNegativeInteger) |
| [Objectidentifier](klasser/objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](klasser/sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](klasser/string.md) | A character string |
| [Time](klasser/time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](klasser/uri.md) | a complete URI |
| [Uriorcurie](klasser/uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
| [Anbefalt](klasser/anbefalt.md) | Anbefalte eigenskapar i ein AP-NO-profil |
| [Obligatorisk](klasser/obligatorisk.md) | Obligatoriske eigenskapar i ein AP-NO-profil |
| [Valgfri](klasser/valgfri.md) | Valfrie eigenskapar i ein AP-NO-profil |
