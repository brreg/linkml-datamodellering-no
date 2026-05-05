# Aksje- og eigarskapsmodell

LinkML-modell for aksjeselskap, aksjar, eigarskap og eigarskapshendingar. Modellen er tilpassa RDF-generering, SHACL og Ontodia-visualisering.


URI: https://example.no/ontology/aksje-eierskap

Name: aksje_eierskap



## Classes

| Class | Description |
| --- | --- |
| [Aksje](aksje.md) | Ei enkelt aksje utstedt av eit aksjeselskap |
| [Aksjeeier](aksjeeier.md) | Person eller organisasjon som eig aksjar |
| [Aksjeeierrettighet](aksjeeierrettighet.md) | Rettigheiter knytt til aksjar, til dømes stemmerett |
| [Aksjeinnskudd](aksjeinnskudd.md) | Innskot knytt til aksjar i samband med selskapshending |
| [Aksjekapital](aksjekapital.md) | Den registrerte aksjekapitalen i eit aksjeselskap |
| [Aksjeklasse](aksjeklasse.md) | Klasse aksjar høyrer til, med eigne rettigheiter |
| [Aksjeoverdragelse](aksjeoverdragelse.md) | Overdraging av aksjar mellom partar |
| [Aksjepost](aksjepost.md) | Samling aksjar eigd av ein aksjeeigar |
| [Aksjeselskap](aksjeselskap.md) | Selskap som utsteder aksjar og har aksjekapital |
| [Containerklasse](containerklasse.md) | Containerklasse for alle forretningsobjekt i modellen |
| [Eierposisjon](eierposisjon.md) | Eierens samla posisjon i eit selskap |
| [Eierskapstransaksjon](eierskapstransaksjon.md) | Transaksjon som påverkar eigarskap i selskapet |
| [InnbetaltAksjekapital](innbetaltaksjekapital.md) | Innbetalt aksjekapital |
| [InnbetaltOverkurs](innbetaltoverkurs.md) | Innbetalt overkurs utover pålydande |
| [Selskapshendelse](selskapshendelse.md) | Hending som påverkar selskapet sitt eigarskap eller kapital |
| [Tidspunkt](tidspunkt.md) | Tidspunkt for ei hending |
| [Utbytte](utbytte.md) | Utbytte knytt til ein eigarposisjon |
| [Utdeling](utdeling.md) | Konkret utdeling av verdiar til aksjeeigarar |
| [Vederlag](vederlag.md) | Vederlag knytt til ei aksjeoverdraging |



## Slots

| Slot | Description |
| --- | --- |
| [aksjeeiere](aksjeeiere.md) | Samling av aksjeeigarar |
| [aksjeeierrettigheter](aksjeeierrettigheter.md) | Samling av aksjeeierrettigheiter |
| [aksjeinnskudder](aksjeinnskudder.md) | Samling av aksjeinnskot |
| [aksjekapitaler](aksjekapitaler.md) | Samling av aksjekapitalar |
| [aksjeklasser](aksjeklasser.md) | Samling av aksjeklasser |
| [aksjeoverdragelser](aksjeoverdragelser.md) | Samling av aksjeoverdragingar |
| [aksjeposter](aksjeposter.md) | Samling av aksjepostar |
| [aksjer](aksjer.md) | Samling av aksjar |
| [aksjeselskaper](aksjeselskaper.md) | Samling av aksjeselskap |
| [antall](antall.md) | Numerisk verdi |
| [belop](belop.md) | Monetært beløp |
| [beskrivelse](beskrivelse.md) | Tekstleg forklaring av instansen |
| [dato](dato.md) | Kalenderdato |
| [eierposisjoner](eierposisjoner.md) | Samling av eigarposisjonar |
| [eierskapstransaksjoner](eierskapstransaksjoner.md) | Samling av eigarskapstransaksjonar |
| [er_basert_paa_eierposisjon](er_basert_paa_eierposisjon.md) | Utbytte knytt til eigarposisjonen |
| [gjelder_aksjepost](gjelder_aksjepost.md) | Aksjepost som inngår i eigarposisjonen |
| [gjelder_aksjer_i_aksjeklasse](gjelder_aksjer_i_aksjeklasse.md) | Rettigheiter knytt til aksjeklassen |
| [gjelder_innbetalt_aksjekapital](gjelder_innbetalt_aksjekapital.md) | Innbetalt aksjekapital |
| [gjelder_innbetalt_overkurs](gjelder_innbetalt_overkurs.md) | Innbetalt overkurs |
| [har_aksjekapital](har_aksjekapital.md) | Aksjekapital som høyrer til selskapet |
| [har_antall_aksjer](har_antall_aksjer.md) | Tal aksjar |
| [har_eierposisjon](har_eierposisjon.md) | Eierposisjon aksjeeigaren har |
| [har_palydende_belop](har_palydende_belop.md) | Pålydande verdi for aksja |
| [har_utdeling](har_utdeling.md) | Utdeling knytt til utbyttet |
| [identifikator](identifikator.md) | Global identifikator for instansen |
| [innbetalt_aksjekapitaler](innbetalt_aksjekapitaler.md) | Samling av innbetalt aksjekapital |
| [innbetalt_overkurser](innbetalt_overkurser.md) | Samling av innbetalt overkurs |
| [kan_ha_aksjeinnskudd](kan_ha_aksjeinnskudd.md) | Aksjeinnskot i selskapshending |
| [kan_ha_vederlag](kan_ha_vederlag.md) | Vederlag for aksjeoverdraging |
| [kan_vaere_aksjeoverdragelse](kan_vaere_aksjeoverdragelse.md) | Aksjeoverdraging i transaksjonen |
| [kan_vaere_selskapshendelse](kan_vaere_selskapshendelse.md) | Selskapshendelse i transaksjonen |
| [navn](navn.md) | Namn på instansen |
| [paavirker_eierposisjon](paavirker_eierposisjon.md) | Eierskapstransaksjon knytt til eigarposisjonen |
| [selskapshendelser](selskapshendelser.md) | Samling av selskapshendingar |
| [tidspunkt](tidspunkt.md) | Tidspunkt for utbytte/eierskapstransaksjon |
| [tilhorer_aksjeklasse](tilhorer_aksjeklasse.md) | Klassen aksja høyrer til |
| [utbytter](utbytter.md) | Samling av utbytte |
| [utdelinger](utdelinger.md) | Samling av utdelingar |
| [utsteder_aksje](utsteder_aksje.md) | Aksje utstedt av selskapet |
| [vederlager](vederlager.md) | Samling av vederlag |


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
| [Float](float.md) | A real number that conforms to the xsd:float specification |
| [Integer](integer.md) | An integer |
| [Jsonpath](jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](string.md) | A character string |
| [Time](time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](uri.md) | a complete URI |
| [Uriorcurie](uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
