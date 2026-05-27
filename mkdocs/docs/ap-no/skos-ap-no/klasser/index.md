# SKOS-AP-NO

Norsk applikasjonsprofil av SKOS for omgrep (begrep), modellert i LinkML med lenking framfor inlining. Basert på https://informasjonsforvaltning.github.io/skos-ap-no-begrep/

URI: https://data.norge.no/ap-no/skos-ap-no

Name: skos-ap-no



## Classes







### Obligatorisk

| Class | Description |
| --- | --- |
| [AssosiativRelasjon](assosiativrelasjon.md) | Ein assosiativ relasjon mellom to omgrep |
| [Begrep](begrep.md) | Eit omgrep med definisjon og tilhøyrande metadata (skos:Concept) |
| [Definisjon](definisjon.md) | Ein definisjon av eit omgrep via eit eige objekt (euvoc:XlNote) |
| [GeneriskRelasjon](generiskrelasjon.md) | Ein generisk relasjon mellom eit overomgrep og eit underomgrep |
| [PartitivRelasjon](partitivrelasjon.md) | Ein partitiv relasjon mellom eit heilskapleg og eit partitivt omgrep |
| [Samling](samling.md) | Ei namngitt samling av omgrep (skos:Collection) |








### Andre

| Class | Description |
| --- | --- |
| [Organisasjon](organisasjon.md) | Ein organisasjon som er utgjevar eller ansvarleg for eit omgrep |
| [VCardKontakt](vcardkontakt.md) | Kontaktinformasjon (vCard) for omgrepseigaren |





## Slots

| Slot | Description |
| --- | --- |
| [ansvarleg_verksemd](ansvarleg_verksemd.md) | Fagleg ansvarleg organisasjon for omgrepet (dct:creator) |
| [assosiert_med](assosiert_med.md) | Omgrep dette omgrepet er assosiert med (skos:related) |
| [datastruktur_term](datastruktur_term.md) | Term brukt i datastrukturar (skosno:dataStructureLabel) |
| [definisjon](definisjon.md) | Direkte definisjon som fritekst (skos:definition) |
| [eksempel](eksempel.md) | Eksempel på bruk av omgrepet (skos:example) |
| [er_del_av_omgrep](er_del_av_omgrep.md) | Omgrep dette omgrepet er ein del av (xkos:isPartOf) |
| [er_erstatta_av](er_erstatta_av.md) | Omgrep som erstattar dette omgrepet (dct:isReplacedBy) |
| [er_fra_omgrep_i](er_fra_omgrep_i.md) | Assosiativ relasjon der dette omgrepet er frå-omgrepet (skosno:isFromConceptI... |
| [er_medlem_av](er_medlem_av.md) | Samling dette omgrepet er medlem av (uneskos:memberOf) |
| [erstattar](erstattar.md) | Omgrep dette omgrepet erstattar (dct:replaces) |
| [euvoc_status](euvoc_status.md) | Status for omgrepet frå eit kontrollert vokabular (euvoc:status) |
| [fagomrade](fagomrade.md) | Fagområde omgrepet høyrer til (dct:subject) |
| [forkasta_term](forkasta_term.md) | Tidlegare brukt, no forkasta term (skos:hiddenLabel) |
| [generaliserer](generaliserer.md) | Omgrep dette omgrepet generaliserer (xkos:generalizes) |
| [gyldig_fra](gyldig_fra.md) | Dato omgrepet er gyldig frå (euvoc:startDate) |
| [gyldig_til](gyldig_til.md) | Dato omgrepet er gyldig til (euvoc:endDate) |
| [har_definisjon](har_definisjon.md) | Definisjon via eige objekt (euvoc:xlDefinition) |
| [har_del_omgrep](har_del_omgrep.md) | Omgrep som er ein del av dette omgrepet (xkos:hasPart) |
| [har_generisk_omgrep](har_generisk_omgrep.md) | Overomgrepet i ein generisk relasjon (skosno:hasGenericConcept) |
| [har_generisk_relasjon](har_generisk_relasjon.md) | Generisk relasjon dette omgrepet er del av (skosno:hasGenericConceptRelation) |
| [har_heilskapleg_omgrep](har_heilskapleg_omgrep.md) | Heilskapleg omgrep i ein partitiv relasjon (skosno:hasComprehensiveConcept) |
| [har_partitiv_relasjon](har_partitiv_relasjon.md) | Partitiv relasjon dette omgrepet er del av (skosno:hasPartitiveConceptRelatio... |
| [har_partitivt_omgrep](har_partitivt_omgrep.md) | Delomgrepet i ein partitiv relasjon (skosno:hasPartitiveConcept) |
| [har_spesifikt_omgrep](har_spesifikt_omgrep.md) | Underomgrepet i ein generisk relasjon (skosno:hasSpecificConcept) |
| [inndelingskriterium](inndelingskriterium.md) | Inndelingskriterium for ein generisk eller partitiv relasjon (dct:description... |
| [kjelde](kjelde.md) | Kjelde til definisjonen (dct:source) |
| [kjelde_relasjon](kjelde_relasjon.md) | Omgrep som beskriv forholdet mellom definisjonen og kjelda (skosno:relationsh... |
| [kontaktpunkt_vcard](kontaktpunkt_vcard.md) | Kontaktpunkt (vCard) for omgrepet eller samlinga (dcat:contactPoint) |
| [malgruppe_def](malgruppe_def.md) | Målgruppe definisjonen er retta mot (dct:audience) |
| [medlem](medlem.md) | Omgrep som er medlem av samlinga (skos:member) |
| [merknad](merknad.md) | Merknad om bruksomfanget for omgrepet (skos:scopeNote) |
| [naert_samsvar](naert_samsvar.md) | Omgrep med nær, men ikkje nøyaktig same meining (skos:closeMatch) |
| [noyaktig_samsvar](noyaktig_samsvar.md) | Omgrep med nøyaktig same meining i anna vokabular (skos:exactMatch) |
| [opprettingsdato](opprettingsdato.md) | Dato omgrepet vart oppretta (dct:created) |
| [relasjontype](relasjontype.md) | Rolle eller type av den assosiative relasjonen (skosno:relationRole) |
| [sja_ogsa_omgrep](sja_ogsa_omgrep.md) | Relatert omgrep (rdfs:seeAlso) |
| [spesifiserer](spesifiserer.md) | Omgrep dette omgrepet spesifiserer (xkos:specializes) |
| [tekst](tekst.md) | Definissjonstekst (rdf:value) |
| [til_omgrep](til_omgrep.md) | Til-omgrepet i den assosiative relasjonen (skosno:hasToConcept) |
| [tillate_term](tillate_term.md) | Tillaten alternativ term for omgrepet (skos:altLabel) |
| [utgjevar](utgjevar.md) | Organisasjon ansvarleg for å publisere omgrepet (dct:publisher) |
| [verdiomrade](verdiomrade.md) | Verdiområde for omgrepet (skosno:valueRange) |


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
