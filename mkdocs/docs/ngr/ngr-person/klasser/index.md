# Nasjonale grunndata – Person

Domenemodell for persondata basert på Nasjonale grunndata (utkast). Modellerer Person med identifikasjon, familierelasjonar, adresser, eigarrettar og kontaktopplysningar frå Folkeregisteret og KRR. Basert på https://informasjonsforvaltning.github.io/nasjonale-grunndata/

URI: https://data.norge.no/linkml/ngr-person

Name: ngr-person



## Classes

| Class | Description |
| --- | --- |
| [Adressebeskyttelse](Adressebeskyttelse.md) | Gradering av adressebeskyttelse for innflyttede personar til Noreg |
| [Dodsfall](Dodsfall.md) | Dødsfallsinformasjon om ein person registrert i Folkeregisteret |
| [FalskIdentitet](FalskIdentitet.md) | Registrering av at ein person har opptrådt med falsk identitet |
| [FamilierelasjonBarn](FamilierelasjonBarn.md) | Familierelasjon der den relaterte personen er barn |
| [FamilierelasjonEktefelle](FamilierelasjonEktefelle.md) | Familierelasjon der den relaterte personen er ektefelle eller registrert part... |
| [FamilierelasjonForelder](FamilierelasjonForelder.md) | Familierelasjon der den relaterte personen er forelder |
| [Foedsel](Foedsel.md) | Fødselsinformasjon om ein person registrert i Folkeregisteret |
| [Folkeregisteridentifikator](Folkeregisteridentifikator.md) | Abstrakt overklasse for unik identifikator i Folkeregisteret |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DNummer](DNummer.md) | Elleve-sifra D-nummer tildelt utanlandske personar med mellombels opphald i N... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Foedselsnummer](Foedselsnummer.md) | Elleve-sifra fødselsnummer tildelt norske statsborgarar og personar med fast ... |
| [ForeldreansvarBarn](ForeldreansvarBarn.md) | Relasjonsklasse som registrerer at eit barn er under foreldreansvaret til ein... |
| [ForeldreansvarForelder](ForeldreansvarForelder.md) | Relasjonsklasse som registrerer kven som har det juridiske foreldreansvaret f... |
| [GeografiskAdresse](GeografiskAdresse.md) | Abstrakt klasse for geografiske adresser |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Bostedsadresse](Bostedsadresse.md) | Adressa personen er registrert busett på i Folkeregisteret |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Oppholdsadresse](Oppholdsadresse.md) | Adressa der personen faktisk oppheld seg (ikkje nødvendigvis bustadsadressa) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Postadresse](Postadresse.md) | Adressa der personen mottar post |
| [Identifikasjonsdokument](Identifikasjonsdokument.md) | Utanlandsk identifikasjonsdokument som pass, førekort eller nasjonalt ID-kort... |
| [Identitetsgrunnlag](Identitetsgrunnlag.md) | Grunnlaget som er brukt for å fastsetje identiteten til ein person ved regist... |
| [InnflyttingTilNorge](InnflyttingTilNorge.md) | Registrering av innflytting til Noreg i Folkeregisteret |
| [Kjoenn](Kjoenn.md) | Kjønn registrert på ein person i Folkeregisteret |
| [KontaktinformasjonDoedsbo](KontaktinformasjonDoedsbo.md) | Kontaktinformasjon for eit dødsbu |
| [Kontaktopplysninger](Kontaktopplysninger.md) | Kontaktopplysningar (e-post og mobilnummer) for digital kommunikasjon med det... |
| [Opphold](Opphold.md) | Lovleg opphaldsgrunnlag for utanlandske statsborgarar registrert i Folkeregis... |
| [Person](Person.md) | Ein fysisk person registrert i Folkeregisteret |
| [PersonContainer](PersonContainer.md) | Rotklasse for NGR-person-datafiler |
| [Personidentifikasjon](Personidentifikasjon.md) | Utanlandsk eller alternativ identifikasjon av ein person, t |
| [Personnavn](Personnavn.md) | Offisielt registrert namn på ein person i Folkeregisteret |
| [Personstatus](Personstatus.md) | Status for ein person i Folkeregisteret (t |
| [ReservasjonMotKommunikasjonPaaNett](ReservasjonMotKommunikasjonPaaNett.md) | Registrering av at ein person har reservert seg mot digital kommunikasjon frå... |
| [RettsligHandleevne](RettsligHandleevne.md) | Registrering av avgrensing i rettsleg handleevne for ein person, t |
| [Sivilstand](Sivilstand.md) | Sivilstand registrert på ein person i Folkeregisteret |
| [SpraakForElektroniskKommunikasjon](SpraakForElektroniskKommunikasjon.md) | Føretrekt språk for elektronisk kommunikasjon med offentlege styresmakter, va... |
| [Statsborgerskap](Statsborgerskap.md) | Statsborgerskap registrert på ein person i Folkeregisteret |
| [UtflyttingFraNorge](UtflyttingFraNorge.md) | Registrering av utflytting frå Noreg i Folkeregisteret |
| [Verge](Verge.md) | Ein verje (anten person eller institusjon) som er oppnemnd for å ivareta inte... |



## Slots

| Slot | Description |
| --- | --- |
| [adressebeskyttelse](adressebeskyttelse.md) |  |
| [adressebeskyttelse_gradering](adressebeskyttelse_gradering.md) | Graderinga av adressebeskyttelsen (STRENGT_FORTROLIG, FORTROLIG o |
| [ansvarsstatus](ansvarsstatus.md) | Status for foreldreansvaret (t |
| [bostedsadresser](bostedsadresser.md) |  |
| [dnummer](dnummer.md) |  |
| [dodsfall](dodsfall.md) |  |
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
| [falskIdentitetar](falskIdentitetar.md) |  |
| [familierelasjonBarn](familierelasjonBarn.md) |  |
| [familierelasjonEktefelle](familierelasjonEktefelle.md) |  |
| [familierelasjonForelder](familierelasjonForelder.md) |  |
| [foedested](foedested.md) | Fødested (kommune eller land) |
| [foedselsaar](foedselsaar.md) | Fødselsår (alltid tilgjengeleg, sjølv om fullstendig dato manglar) |
| [foedselsdato](foedselsdato.md) | Fødselsdato (kan vere ukjent for eldre registreringar) |
| [foedselsnummer](foedselsnummer.md) |  |
| [foedslar](foedslar.md) |  |
| [foreldreansvarBarn](foreldreansvarBarn.md) |  |
| [foreldreansvarForelder](foreldreansvarForelder.md) |  |
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
| [identifikasjonsdokument](identifikasjonsdokument.md) |  |
| [identifikasjonstype](identifikasjonstype.md) | Type utanlandsk identifikasjon (t |
| [identifikatornummer](identifikatornummer.md) | Sjølve identifikatoren som tekststreng (11 siffer for fødselsnummer/D-nummer) |
| [identitetsgrunnlag](identitetsgrunnlag.md) |  |
| [identitetsgrunnlag_kilde](identitetsgrunnlag_kilde.md) | Kjelde for identitetsgrunnlaget |
| [identitetsgrunnlag_status](identitetsgrunnlag_status.md) | Status/type for identitetsgrunnlaget (t |
| [innflytting](innflytting.md) |  |
| [innflyttingsdato](innflyttingsdato.md) | Dato personen vart registrert innflytta til Noreg |
| [kjoenn](kjoenn.md) |  |
| [kjoenn_kode](kjoenn_kode.md) | Kjønnskode (MANN, KVINNE, UKJENT) |
| [kontaktinformasjonDoedsbo](kontaktinformasjonDoedsbo.md) |  |
| [kontaktopplysningar](kontaktopplysningar.md) |  |
| [landkode](landkode.md) | ISO 3166-1 alfa-2 landkode (t |
| [mellomnavn](mellomnavn.md) | Mellomnamn til personen |
| [mobiltelefonnummer](mobiltelefonnummer.md) | Mobiltelefonnummer registrert i KRR |
| [mottar_post_paa](mottar_post_paa.md) | Adressa personen mottar post på |
| [navn](navn.md) | Namn på person eller institusjon |
| [omfang](omfang.md) | Omfanget av vergemålet eller avgrensinga i rettsleg handleevne |
| [opphold](opphold.md) |  |
| [oppholder_seg_paa](oppholder_seg_paa.md) | Adressa personen faktisk oppheld seg på |
| [oppholds_type](oppholds_type.md) | Type opphald (MIDLERTIDIG, PERMANENT, OPPLYSNING_MANGLER) |
| [oppholdsadresser](oppholdsadresser.md) |  |
| [personar](personar.md) |  |
| [personidentifikasjonar](personidentifikasjonar.md) |  |
| [personnavn](personnavn.md) |  |
| [personstatus](personstatus.md) |  |
| [personstatus_type](personstatus_type.md) | Personstatustype (BOSATT, UTFLYTTET, DOED o |
| [postadresser](postadresser.md) |  |
| [relatert_ved_sivilstand](relatert_ved_sivilstand.md) | Person ein er gift/partnar med (utfyller sivilstand GIFT, REGISTRERT_PARTNER ... |
| [reservasjonar](reservasjonar.md) |  |
| [rett_identitet](rett_identitet.md) | Den rette identiteten til ein person som har opptrådt med falsk identitet |
| [rett_identitet_er_ukjent](rett_identitet_er_ukjent.md) | Om den rette identiteten er ukjent (når falsk identitet er registrert) |
| [rettslig_handleevne_type](rettslig_handleevne_type.md) | Type avgrensing i rettsleg handleevne |
| [rettsligHandleevne](rettsligHandleevne.md) |  |
| [sist_oppdatert](sist_oppdatert.md) | Dato kontaktopplysningane sist vart oppdatert |
| [sivilstand](sivilstand.md) |  |
| [sivilstand_type](sivilstand_type.md) | Sivilstandstype (UGIFT, GIFT, SKILT o |
| [spraak](spraak.md) |  |
| [spraakkode](spraakkode.md) | BCP 47 språkkode for føretrekt kommunikasjonsspråk (t |
| [statsborgerskap](statsborgerskap.md) |  |
| [telefonnummer](telefonnummer.md) | Telefonnummer |
| [tilflyttingsland](tilflyttingsland.md) | ISO 3166-1 landkode for landet personen flytta til |
| [tilflyttingssted_i_utlandet](tilflyttingssted_i_utlandet.md) | Stad i utlandet personen flytta til |
| [utflytting](utflytting.md) |  |
| [utflyttingsdato](utflyttingsdato.md) | Dato personen vart registrert utflytta frå Noreg |
| [utloepsdato](utloepsdato.md) | Datoen dokumentet går ut på dato |
| [utstederland](utstederland.md) | ISO 3166-1 landkode for landet som utsteda dokumentet |
| [utstedtdato](utstedtdato.md) | Datoen dokumentet vart utstedt |
| [verger](verger.md) |  |
| [vergetype](vergetype.md) | Type vergemål (mindreårig, vaksen o |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [AdressebeskyttelseGradering](AdressebeskyttelseGradering.md) | Gradering av adressebeskyttelse (tidlegare kode 6/7) |
| [IdentifikasjonsdokumentType](IdentifikasjonsdokumentType.md) | Type utanlandsk identifikasjonsdokument |
| [KjoennKode](KjoennKode.md) | Kjønn registrert i Folkeregisteret |
| [OppholdstypeKode](OppholdstypeKode.md) | Type opphaldstillatelse registrert i Folkeregisteret |
| [PersonstatusType](PersonstatusType.md) | Personens status i Folkeregisteret |
| [RettsligHandleevneType](RettsligHandleevneType.md) | Type avgrensing av rettsleg handleevne |
| [SivilstandType](SivilstandType.md) | Sivilstandskode frå Folkeregisteret |
| [VergetypeKode](VergetypeKode.md) | Type vergemål |


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
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
| [Anbefalt](Anbefalt.md) | Anbefalte eigenskapar i domenemodellen |
| [Obligatorisk](Obligatorisk.md) | Obligatoriske eigenskapar i domenemodellen |
| [Valgfri](Valgfri.md) | Valfrie eigenskapar i domenemodellen |
