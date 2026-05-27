# XKOS-AP-NO

LinkML-modell for XKOS-AP-NO – norsk applikasjonsprofil for utvida SKOS-klassifikasjonar. Basert på https://data.norge.no/specification/xkos-ap-no

URI: https://data.norge.no/ap-no/xkos-ap-no

Name: xkos-ap-no



## Classes







### Obligatorisk

| Class | Description |
| --- | --- |
| [Kategori](kategori.md) | Ein kategori i ein klassifikasjon (skos:Concept) |
| [Klassifikasjon](klassifikasjon.md) | Ei klassifikasjon – ein systematisk struktur av kategoriar brukt til å klassi... |
| [Klassifikasjonsnivaa](klassifikasjonsnivaa.md) | Eit nivå i ein klassifikasjon (xkos:ClassificationLevel) |
| [Klassifikasjonssamanlikning](klassifikasjonssamanlikning.md) | Ein samanlikning mellom to klassifikasjonar (xkos:Correspondence) |




### Anbefalt

| Class | Description |
| --- | --- |
| [Kategorisamanlikning](kategorisamanlikning.md) | Ein samanlikning mellom to kategoriar på tvers av klassifikasjonar (xkos:Conc... |






### Andre

| Class | Description |
| --- | --- |
| [Organisasjon](organisasjon.md) | Ein organisasjon eller aktør (foaf:Agent) |
| [Tidsrom](tidsrom.md) | Eit tidsrom med start- og/eller sluttdato (dct:PeriodOfTime) |





## Slots

| Slot | Description |
| --- | --- |
| [antall_nivaa](antall_nivaa.md) | Antal nivå i klassifikasjonen (xkos:numberOfLevels) |
| [bestar_av](bestar_av.md) | Kategorisamanlikningar som inngår i klassifikasjonssamanlikninga (xkos:madeOf... |
| [er_eksklusivt_ekvivalent_med](er_eksklusivt_ekvivalent_med.md) | Eksklusiv breid ekvivalens (xkos:exclusivelyBroadMatch) |
| [er_ekvivalent_med](er_ekvivalent_med.md) | Breid ekvivalens til kategori i annan klassifikasjon (uneskos:broadMatch) |
| [er_i_klassifikasjon](er_i_klassifikasjon.md) | Klassifikasjonen kategorien tilhøyrer (skos:inScheme) |
| [er_ikkje_ekvivalent_med](er_ikkje_ekvivalent_med.md) | Klar ikkje-ekvivalens til kategori i annan klassifikasjon (xkos:disjointMatch... |
| [er_samanlikna_med](er_samanlikna_med.md) | Klassifikasjonar som er samanlikna (xkos:compares) |
| [forste_nivaa](forste_nivaa.md) | Toppnivå i klassifikasjonen (xkos:levels) |
| [gjeld_for_tidsrom](gjeld_for_tidsrom.md) | Tidsrom klassifikasjonen er gyldig for (dct:temporal) |
| [har_medlem](har_medlem.md) | Kategoriar som høyrer til dette nivået (skos:member) |
| [har_notat](har_notat.md) | Fritekstnotat om kategorien (skos:note) |
| [kjeldeomgrep](kjeldeomgrep.md) | Kjeldeomgrep i ein kategorisamanlikning (xkos:sourceConcept) |
| [maalomgrep](maalomgrep.md) | Måleomgrep i ein kategorisamanlikning (xkos:targetConcept) |
| [nivaa_djupn](nivaa_djupn.md) | Djupna (nivånummer) i klassifikasjonsstrukturen (xkos:depth) |
| [overordna_kategori](overordna_kategori.md) | Overordna kategori (skos:broader) |
| [samanliknar](samanliknar.md) | Klassifikasjonar som er samanlikna i korrespondansen (xkos:compares) |
| [tema](tema.md) | Fagleg tema klassifikasjonen dekkjer (dct:subject) |
| [tidsrom_slutt](tidsrom_slutt.md) | Sluttdato for tidsromet (dct:endDate) |
| [tidsrom_start](tidsrom_start.md) | Startdato for tidsromet (dct:startDate) |
| [tilhorande_klassifikasjonsnivaa](tilhorande_klassifikasjonsnivaa.md) | Klassifikasjonsnivå kategorien høyrer til (xkos:belongsTo) |
| [underordna_kategori](underordna_kategori.md) | Underordna kategori (skos:narrower) |
| [underordna_klassifikasjonsnivaa](underordna_klassifikasjonsnivaa.md) | Underordna klassifikasjonsnivå (xkos:nextLevel) |
| [utgjevar](utgjevar.md) | Organisasjon som er ansvarleg utgjevar (dct:publisher) |


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
