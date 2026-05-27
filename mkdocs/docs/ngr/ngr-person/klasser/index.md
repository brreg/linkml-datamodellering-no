# Nasjonale grunndata – Person

Domenemodell for persondata basert på Nasjonale grunndata (utkast). Modellerer Person med identifikasjon, familierelasjonar, adresser, eigarrettar og kontaktopplysningar frå Folkeregisteret og KRR. Basert på https://informasjonsforvaltning.github.io/nasjonale-grunndata/

URI: https://data.norge.no/ngr/ngr-person

Name: ngr-person



## Classes







### Obligatorisk

| Class | Description |
| --- | --- |
| [Adressebeskyttelse](adressebeskyttelse.md) | Gradering av adressebeskyttelse for innflyttede personar til Noreg |
| [DNummer](dnummer.md) | Elleve-sifra D-nummer tildelt utanlandske personar med mellombels opphald i N... |
| [Dodsfall](dodsfall.md) | Dødsfallsinformasjon om ein person registrert i Folkeregisteret |
| [FalskIdentitet](falskidentitet.md) | Registrering av at ein person har opptrådt med falsk identitet |
| [FamilierelasjonBarn](familierelasjonbarn.md) | Familierelasjon der den relaterte personen er barn |
| [FamilierelasjonEktefelle](familierelasjonektefelle.md) | Familierelasjon der den relaterte personen er ektefelle eller registrert part... |
| [FamilierelasjonForelder](familierelasjonforelder.md) | Familierelasjon der den relaterte personen er forelder |
| [Foedsel](foedsel.md) | Fødselsinformasjon om ein person registrert i Folkeregisteret |
| [Foedselsnummer](foedselsnummer.md) | Elleve-sifra fødselsnummer tildelt norske statsborgarar og personar med fast ... |
| [ForeldreansvarBarn](foreldreansvarbarn.md) | Relasjonsklasse som registrerer at eit barn er under foreldreansvaret til ein... |
| [ForeldreansvarForelder](foreldreansvarforelder.md) | Relasjonsklasse som registrerer kven som har det juridiske foreldreansvaret f... |
| [Identifikasjonsdokument](identifikasjonsdokument.md) | Utanlandsk identifikasjonsdokument som pass, førekort eller nasjonalt ID-kort... |
| [Identitetsgrunnlag](identitetsgrunnlag.md) | Grunnlaget som er brukt for å fastsetje identiteten til ein person ved regist... |
| [InnflyttingTilNorge](innflyttingtilnorge.md) | Registrering av innflytting til Noreg i Folkeregisteret |
| [Kjoenn](kjoenn.md) | Kjønn registrert på ein person i Folkeregisteret |
| [KontaktinformasjonDoedsbo](kontaktinformasjondoedsbo.md) | Kontaktinformasjon for eit dødsbu |
| [Opphold](opphold.md) | Lovleg opphaldsgrunnlag for utanlandske statsborgarar registrert i Folkeregis... |
| [Person](person.md) | Ein fysisk person registrert i Folkeregisteret |
| [Personidentifikasjon](personidentifikasjon.md) | Utanlandsk eller alternativ identifikasjon av ein person, t |
| [Personnavn](personnavn.md) | Offisielt registrert namn på ein person i Folkeregisteret |
| [Personstatus](personstatus.md) | Status for ein person i Folkeregisteret (t |
| [ReservasjonMotKommunikasjonPaaNett](reservasjonmotkommunikasjonpaanett.md) | Registrering av at ein person har reservert seg mot digital kommunikasjon frå... |
| [RettsligHandleevne](rettslighandleevne.md) | Registrering av avgrensing i rettsleg handleevne for ein person, t |
| [Sivilstand](sivilstand.md) | Sivilstand registrert på ein person i Folkeregisteret |
| [SpraakForElektroniskKommunikasjon](spraakforelektroniskkommunikasjon.md) | Føretrekt språk for elektronisk kommunikasjon med offentlege styresmakter, va... |
| [Statsborgerskap](statsborgerskap.md) | Statsborgerskap registrert på ein person i Folkeregisteret |
| [UtflyttingFraNorge](utflyttingfranorge.md) | Registrering av utflytting frå Noreg i Folkeregisteret |
| [Verge](verge.md) | Ein verje (anten person eller institusjon) som er oppnemnd for å ivareta inte... |




### Anbefalt

| Class | Description |
| --- | --- |
| [Bostedsadresse](bostedsadresse.md) | Adressa personen er registrert busett på i Folkeregisteret |
| [Kontaktopplysninger](kontaktopplysninger.md) | Kontaktopplysningar (e-post og mobilnummer) for digital kommunikasjon med det... |
| [Oppholdsadresse](oppholdsadresse.md) | Adressa der personen faktisk oppheld seg (ikkje nødvendigvis bustadsadressa) |
| [Postadresse](postadresse.md) | Adressa der personen mottar post |






### Andre

| Class | Description |
| --- | --- |
| [Folkeregisteridentifikator](folkeregisteridentifikator.md) | Abstrakt overklasse for unik identifikator i Folkeregisteret |
| [GeografiskAdresse](geografiskadresse.md) | Abstrakt klasse for geografiske adresser |





## Slots

| Slot | Description |
| --- | --- |
| [adressebeskyttelse_gradering](adressebeskyttelse_gradering.md) | Graderinga av adressebeskyttelsen (STRENGT_FORTROLIG, FORTROLIG o |
| [ansvarsstatus](ansvarsstatus.md) | Status for foreldreansvaret (t |
| [doedsdato](doedsdato.md) | Dato for dødsfallet |
| [doedssted](doedssted.md) | Stad for dødsfallet |
| [dokumentnummer](dokumentnummer.md) | Nummeret på identifikasjonsdokumentet |
| [dokumenttype](dokumenttype.md) | Type identifikasjonsdokument (pass, førekort, nasjonalt ID-kort o |
| [embete](embete.md) | Statsforvaltarembetet som oppnemnde vergjet |
| [epostadresse_verdi](epostadresse_verdi.md) | E-postadresse |
| [er_av_type_person](er_av_type_person.md) | Personen som denne relasjonen peikar til |
| [er_falsk](er_falsk.md) | Om denne identiteten er registrert som falsk |
| [er_reservert](er_reservert.md) | Om personen er reservert mot digital kommunikasjon frå det offentlege |
| [etternavn](etternavn.md) | Etternamn til personen |
| [foedested](foedested.md) | Fødested (kommune eller land) |
| [foedselsaar](foedselsaar.md) | Fødselsår (alltid tilgjengeleg, sjølv om fullstendig dato manglar) |
| [foedselsdato](foedselsdato.md) | Fødselsdato (kan vere ukjent for eldre registreringar) |
| [foreldrerelasjon_type](foreldrerelasjon_type.md) | Type foreldrerelasjon (MOR, FAR, MEDMOR o |
| [forkortet_navn](forkortet_navn.md) | Forkorta versjon av fullt namn |
| [fornavn](fornavn.md) | Fornamn(et/a) til personen |
| [fraflyttingsland](fraflyttingsland.md) | ISO 3166-1 landkode for landet personen flytta frå |
| [fraflyttingssted_i_utlandet](fraflyttingssted_i_utlandet.md) | Stad i utlandet personen flytta frå |
| [gyldig_fra_og_med](gyldig_fra_og_med.md) | Dato opplysinga er gyldig frå og med |
| [gyldig_til_og_med](gyldig_til_og_med.md) | Dato opplysinga er gyldig til og med |
| [har_adressebeskyttelse](har_adressebeskyttelse.md) | Adressebeskyttelse registrert på personen |
| [har_bosted_paa](har_bosted_paa.md) | Adressa personen er registrert busett på |
| [har_dodsfall](har_dodsfall.md) | Dødsfallsinformasjon om personen |
| [har_falsk_identitet](har_falsk_identitet.md) | Registrering av at personen har opptrådt med falsk identitet |
| [har_familierelasjon_barn](har_familierelasjon_barn.md) | Familierelasjonar der den relaterte personen er barn |
| [har_familierelasjon_ektefelle](har_familierelasjon_ektefelle.md) | Familierelasjon til ektefelle eller registrert partnar |
| [har_familierelasjon_forelder](har_familierelasjon_forelder.md) | Familierelasjonar der den relaterte personen er forelder (maks 2) |
| [har_foedsel](har_foedsel.md) | Fødselsinformasjon om personen |
| [har_folkeregisteridentifikator](har_folkeregisteridentifikator.md) | Unik identifikator i Folkeregisteret (fødselsnummer eller D-nummer) |
| [har_foreldreansvar_barn](har_foreldreansvar_barn.md) | Barn som denne personen har juridisk foreldreansvar for |
| [har_foreldreansvar_forelder](har_foreldreansvar_forelder.md) | Personar med juridisk foreldreansvar for denne personen (maks 2) |
| [har_identitetsgrunnlag](har_identitetsgrunnlag.md) | Grunnlaget for personens identitetsfastsetjing |
| [har_innflytting_til_norge](har_innflytting_til_norge.md) | Siste innflyttingsregistrering til Noreg |
| [har_kjoenn](har_kjoenn.md) | Kjønn registrert på personen |
| [har_kontaktinformasjon_doedsbo](har_kontaktinformasjon_doedsbo.md) | Kontaktinformasjon for personens dødsbu |
| [har_kontaktopplysninger](har_kontaktopplysninger.md) | Kontaktopplysningar registrert i KRR |
| [har_lovlig_opphold](har_lovlig_opphold.md) | Lovleg opphaldsgrunnlag for utanlandske statsborgarar |
| [har_personidentifikasjon](har_personidentifikasjon.md) | Utanlandsk eller alternativ identifikasjon av personen |
| [har_personnavn](har_personnavn.md) | Offisielt registrert namn på personen |
| [har_personstatus](har_personstatus.md) | Status for personen i Folkeregisteret |
| [har_reservasjon_mot_kommunikasjon](har_reservasjon_mot_kommunikasjon.md) | Reservasjon mot digital kommunikasjon frå det offentlege |
| [har_rettslig_handleevne](har_rettslig_handleevne.md) | Avgrensing i rettsleg handleevne registrert for personen |
| [har_sivilstand](har_sivilstand.md) | Sivilstand registrert på personen |
| [har_statsborgerskap](har_statsborgerskap.md) | Statsborgerskap registrert på personen (minimum 1) |
| [har_utenlandsk_identifikasjonsdokument](har_utenlandsk_identifikasjonsdokument.md) | Utanlandske identifikasjonsdokument knytt til personen |
| [har_utflytting_fra_norge](har_utflytting_fra_norge.md) | Siste utflyttingsregistrering frå Noreg |
| [har_valgt_spraak](har_valgt_spraak.md) | Føretrekt språk for elektronisk kommunikasjon valt av personen |
| [har_verge](har_verge.md) | Verje(r) oppnemnd for personen |
| [id](id.md) | URI-identifikator for ressursen |
| [identifikasjonstype](identifikasjonstype.md) | Type utanlandsk identifikasjon (t |
| [identifikatornummer](identifikatornummer.md) | Sjølve identifikatoren som tekststreng (11 siffer for fødselsnummer/D-nummer) |
| [identitetsgrunnlag_kilde](identitetsgrunnlag_kilde.md) | Kjelde for identitetsgrunnlaget |
| [identitetsgrunnlag_status](identitetsgrunnlag_status.md) | Status/type for identitetsgrunnlaget (t |
| [innflyttingsdato](innflyttingsdato.md) | Dato personen vart registrert innflytta til Noreg |
| [kjoenn_kode](kjoenn_kode.md) | Kjønnskode (MANN, KVINNE, UKJENT) |
| [landkode](landkode.md) | ISO 3166-1 alfa-2 landkode (t |
| [mellomnavn](mellomnavn.md) | Mellomnamn til personen |
| [mobiltelefonnummer](mobiltelefonnummer.md) | Mobiltelefonnummer registrert i KRR |
| [mottar_post_paa](mottar_post_paa.md) | Adressa personen mottar post på |
| [navn](navn.md) | Namn på person eller institusjon |
| [omfang](omfang.md) | Omfanget av vergemålet eller avgrensinga i rettsleg handleevne |
| [oppholder_seg_paa](oppholder_seg_paa.md) | Adressa personen faktisk oppheld seg på |
| [oppholds_type](oppholds_type.md) | Type opphald (MIDLERTIDIG, PERMANENT, OPPLYSNING_MANGLER) |
| [personstatus_type](personstatus_type.md) | Personstatustype (BOSATT, UTFLYTTET, DOED o |
| [relatert_ved_sivilstand](relatert_ved_sivilstand.md) | Person ein er gift/partnar med (utfyller sivilstand GIFT, REGISTRERT_PARTNER ... |
| [rett_identitet](rett_identitet.md) | Den rette identiteten til ein person som har opptrådt med falsk identitet |
| [rett_identitet_er_ukjent](rett_identitet_er_ukjent.md) | Om den rette identiteten er ukjent (når falsk identitet er registrert) |
| [rettslig_handleevne_type](rettslig_handleevne_type.md) | Type avgrensing i rettsleg handleevne |
| [sist_oppdatert](sist_oppdatert.md) | Dato kontaktopplysningane sist vart oppdatert |
| [sivilstand_type](sivilstand_type.md) | Sivilstandstype (UGIFT, GIFT, SKILT o |
| [spraakkode](spraakkode.md) | BCP 47 språkkode for føretrekt kommunikasjonsspråk (t |
| [telefonnummer](telefonnummer.md) | Telefonnummer |
| [tilflyttingsland](tilflyttingsland.md) | ISO 3166-1 landkode for landet personen flytta til |
| [tilflyttingssted_i_utlandet](tilflyttingssted_i_utlandet.md) | Stad i utlandet personen flytta til |
| [utflyttingsdato](utflyttingsdato.md) | Dato personen vart registrert utflytta frå Noreg |
| [utloepsdato](utloepsdato.md) | Datoen dokumentet går ut på dato |
| [utstederland](utstederland.md) | ISO 3166-1 landkode for landet som utsteda dokumentet |
| [utstedtdato](utstedtdato.md) | Datoen dokumentet vart utstedt |
| [vergetype](vergetype.md) | Type vergemål (mindreårig, vaksen o |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [AdressebeskyttelseGradering](adressebeskyttelsegradering.md) | Gradering av adressebeskyttelse (tidlegare kode 6/7) |
| [IdentifikasjonsdokumentType](identifikasjonsdokumenttype.md) | Type utanlandsk identifikasjonsdokument |
| [KjoennKode](kjoennkode.md) | Kjønn registrert i Folkeregisteret |
| [OppholdstypeKode](oppholdstypekode.md) | Type opphaldstillatelse registrert i Folkeregisteret |
| [PersonstatusType](personstatustype.md) | Personens status i Folkeregisteret |
| [RettsligHandleevneType](rettslighandleevnetype.md) | Type avgrensing av rettsleg handleevne |
| [SivilstandType](sivilstandtype.md) | Sivilstandskode frå Folkeregisteret |
| [VergetypeKode](vergetypekode.md) | Type vergemål |


## Types

| Type | Description |
| --- | --- |


## Subsets

| Subset | Description |
| --- | --- |
| [Anbefalt](anbefalt.md) | Anbefalte eigenskapar i domenemodellen |
| [Obligatorisk](obligatorisk.md) | Obligatoriske eigenskapar i domenemodellen |
| [Valgfri](valgfri.md) | Valfrie eigenskapar i domenemodellen |
