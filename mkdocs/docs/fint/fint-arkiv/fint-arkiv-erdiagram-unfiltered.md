```mermaid
erDiagram
AdministrativEnhet {
    uriorcurie id  
    string navn  
    uriorcurie organisasjonselement  
}
Adresse {
    stringList adresselinje  
    string postnummer  
    string poststed  
}
Arkivdel {
    uriorcurie id  
    string tittel  
}
Arkivressurs {
    uriorcurie id  
    uriorcurie personalressurs  
}
Autorisasjon {
    uriorcurie id  
}
Avskrivning {
    string avskrevetAv  
    datetime avskrivningsdato  
    string avskrivningsmate  
}
DispensasjonAutomatiskFredaKulturminne {
    string kulturminneId  
    string tiltak  
    uriorcurie id  
    datetime avsluttetDato  
    string beskrivelse  
    stringList noekkelord  
    string offentligTittel  
    datetime opprettetDato  
    string saksaar  
    datetime saksdato  
    string sakssekvensnummer  
    string tittel  
    datetime utlaantDato  
}
DokumentStatus {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
DokumentType {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Dokumentbeskrivelse {
    uriorcurie id  
    string beskrivelse  
    integer dokumentnummer  
    stringList forfatter  
    datetime opprettetDato  
    stringList referanseArkivdel  
    datetime tilknyttetDato  
    string tittel  
}
Dokumentfil {
    uriorcurie id  
    string data  
    string filnavn  
    string format  
}
Dokumentobjekt {
    string filstorrelse  
    string formatDetaljer  
    string sjekksum  
    string sjekksumAlgoritme  
    integer versjonsnummer  
}
Elev {
    uriorcurie id  
}
Format {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Fylke {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Identifikator {
    string identifikatorverdi  
}
JournalStatus {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Journalpost {
    integer antallVedlegg  
    datetime dokumentetsDato  
    datetime forfallsDato  
    string journalAr  
    datetime journalDato  
    integer journalPostnummer  
    integer journalSekvensnummer  
    datetime mottattDato  
    datetime offentlighetsvurdertDato  
    datetime sendtDato  
    uriorcurie id  
    datetime arkivertDato  
    string beskrivelse  
    stringList forfatter  
    stringList nokkelord  
    string offentligTittel  
    datetime opprettetDato  
    stringList referanseArkivDel  
    string registreringsId  
    string tittel  
}
JournalpostType {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Kjonn {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Klasse {
    string klasseId  
    integer rekkefoelge  
    string tittel  
}
Klassifikasjonssystem {
    uriorcurie id  
    string avsluttetAvNavn  
    datetime avsluttetDato  
    string beskrivelse  
    string opprettetAvNavn  
    datetime opprettetDato  
    string tittel  
}
Klassifikasjonstype {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Kommune {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Kontaktinformasjon {
    string epostadresse  
    string mobiltelefonnummer  
    string nettsted  
    string sip  
    string telefonnummer  
}
Kontaktperson {
    uriorcurie id  
    string type  
}
Korrespondansepart {
    string foedselsnummer  
    string kontaktperson_str  
    string korrespondansepartNavn  
    string orgnummer  
}
KorrespondansepartType {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Landkode {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Matrikkelnummer {
    string bruksnummer  
    string festenummer  
    string gaardsnummer  
    string seksjonsnummer  
}
Merknad {
    datetime merknadsdato  
    string merknadstekst  
}
Merknadstype {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Part {
    string foedselsnummer  
    string kontaktperson_str  
    string orgnummer  
    string partNavn  
}
PartRolle {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Periode {
    string beskrivelse  
    datetime slutt  
    datetime start  
}
Person {
    uriorcurie id  
    string bilde  
    date fodselsdato  
    uriorcurieList laerling  
    uriorcurie otungdom  
    uriorcurie personalressurs  
}
Personalmappe {
    uriorcurie arbeidssted  
    uriorcurie leder  
    uriorcurie personalressurs  
    uriorcurie id  
    datetime avsluttetDato  
    string beskrivelse  
    stringList noekkelord  
    string offentligTittel  
    datetime opprettetDato  
    string saksaar  
    datetime saksdato  
    string sakssekvensnummer  
    string tittel  
    datetime utlaantDato  
}
Personnavn {
    string etternavn  
    string fornavn  
    string mellomnavn  
}
Rolle {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Sak {
    uriorcurie id  
    datetime avsluttetDato  
    string beskrivelse  
    stringList noekkelord  
    string offentligTittel  
    datetime opprettetDato  
    string saksaar  
    datetime saksdato  
    string sakssekvensnummer  
    string tittel  
    datetime utlaantDato  
}
Saksmappetype {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Saksstatus {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Skjerming {

}
Skjermingshjemmel {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
SoeknadDrosjeloeyve {
    string organisasjonsnavn  
    string orgnummer  
    uriorcurie id  
    datetime avsluttetDato  
    string beskrivelse  
    stringList noekkelord  
    string offentligTittel  
    datetime opprettetDato  
    string saksaar  
    datetime saksdato  
    string sakssekvensnummer  
    string tittel  
    datetime utlaantDato  
}
Spraak {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Tilgang {
    uriorcurie id  
    string tittel  
}
Tilgangsgruppe {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Tilgangsrestriksjon {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
TilknyttetRegistreringSom {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
TilskuddFartoy {
    string fartoyNavn  
    string kallesignal  
    string kulturminneId  
    uriorcurie id  
    datetime avsluttetDato  
    string beskrivelse  
    stringList noekkelord  
    string offentligTittel  
    datetime opprettetDato  
    string saksaar  
    datetime saksdato  
    string sakssekvensnummer  
    string tittel  
    datetime utlaantDato  
}
TilskuddFredaBygningPrivatEie {
    string bygningsnavn  
    string kulturminneId  
    uriorcurie id  
    datetime avsluttetDato  
    string beskrivelse  
    stringList noekkelord  
    string offentligTittel  
    datetime opprettetDato  
    string saksaar  
    datetime saksdato  
    string sakssekvensnummer  
    string tittel  
    datetime utlaantDato  
}
Variantformat {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}

AdministrativEnhet ||--|o Periode : "gyldighetsperiode"
Adresse ||--|o Landkode : "land"
Arkivdel ||--}o Klassifikasjonssystem : "klassifikasjonssystem"
Arkivressurs ||--|o Identifikator : "kildesystemId"
Arkivressurs ||--}o Autorisasjon : "autorisasjon"
Arkivressurs ||--}o Tilgang : "tilgang"
Autorisasjon ||--}o AdministrativEnhet : "administrativenhet"
Autorisasjon ||--}o Arkivressurs : "arkivressurs"
Autorisasjon ||--}| Tilgangsrestriksjon : "tilgangsrestriksjon"
DispensasjonAutomatiskFredaKulturminne ||--|o AdministrativEnhet : "journalenhet"
DispensasjonAutomatiskFredaKulturminne ||--|o Arkivdel : "arkivdel"
DispensasjonAutomatiskFredaKulturminne ||--|o Arkivressurs : "avsluttetAv"
DispensasjonAutomatiskFredaKulturminne ||--|o Identifikator : "mappeId"
DispensasjonAutomatiskFredaKulturminne ||--|o Saksmappetype : "saksmappetype"
DispensasjonAutomatiskFredaKulturminne ||--|o Skjerming : "skjerming"
DispensasjonAutomatiskFredaKulturminne ||--|o Tilgangsgruppe : "tilgangsgruppe"
DispensasjonAutomatiskFredaKulturminne ||--|| AdministrativEnhet : "administrativEnhet"
DispensasjonAutomatiskFredaKulturminne ||--|| Arkivressurs : "opprettetAv, saksansvarlig"
DispensasjonAutomatiskFredaKulturminne ||--|| Identifikator : "soeknadsnummer"
DispensasjonAutomatiskFredaKulturminne ||--|| Matrikkelnummer : "matrikkelnummer"
DispensasjonAutomatiskFredaKulturminne ||--|| Saksstatus : "saksstatus"
DispensasjonAutomatiskFredaKulturminne ||--}o Journalpost : "journalpost"
DispensasjonAutomatiskFredaKulturminne ||--}o Klasse : "klasse"
DispensasjonAutomatiskFredaKulturminne ||--}o Merknad : "merknad"
DispensasjonAutomatiskFredaKulturminne ||--}o Part : "part"
DokumentStatus ||--|o Periode : "gyldighetsperiode"
DokumentType ||--|o Periode : "gyldighetsperiode"
Dokumentbeskrivelse ||--|o Skjerming : "skjerming"
Dokumentbeskrivelse ||--|| Arkivressurs : "opprettetAv, tilknyttetAv"
Dokumentbeskrivelse ||--|| DokumentStatus : "dokumentstatus"
Dokumentbeskrivelse ||--|| DokumentType : "dokumentType"
Dokumentbeskrivelse ||--}o Dokumentobjekt : "dokumentobjekt"
Dokumentbeskrivelse ||--}o Part : "part"
Dokumentbeskrivelse ||--}| TilknyttetRegistreringSom : "tilknyttetRegistreringSom"
Dokumentobjekt ||--|o Dokumentfil : "referanseDokumentfil"
Dokumentobjekt ||--|o Format : "filformat"
Dokumentobjekt ||--|| Arkivressurs : "opprettetAv"
Dokumentobjekt ||--|| Variantformat : "variantFormat"
Elev ||--|o Identifikator : "elevnummer"
Elev ||--|o Person : "person"
Format ||--|o Periode : "gyldighetsperiode"
Fylke ||--|o Periode : "gyldighetsperiode"
Fylke ||--}o Kommune : "kommune"
Identifikator ||--|o Periode : "gyldighetsperiode"
JournalStatus ||--|o Periode : "gyldighetsperiode"
Journalpost ||--|o AdministrativEnhet : "administrativEnhet, journalenhet"
Journalpost ||--|o Arkivdel : "arkivdel"
Journalpost ||--|o Arkivressurs : "saksbehandler"
Journalpost ||--|o Avskrivning : "avskrivning"
Journalpost ||--|o Klasse : "klasse"
Journalpost ||--|o Skjerming : "skjerming"
Journalpost ||--|o Tilgangsgruppe : "tilgangsgruppe"
Journalpost ||--|| Arkivressurs : "arkivertAv, opprettetAv"
Journalpost ||--|| JournalStatus : "journalstatus"
Journalpost ||--|| JournalpostType : "journalposttype"
Journalpost ||--}o Dokumentbeskrivelse : "dokumentbeskrivelse"
Journalpost ||--}o Korrespondansepart : "korrespondansepart"
Journalpost ||--}o Merknad : "merknad"
Journalpost ||--}o Part : "part"
JournalpostType ||--|o Periode : "gyldighetsperiode"
Kjonn ||--|o Periode : "gyldighetsperiode"
Klasse ||--|o Skjerming : "skjerming"
Klasse ||--|| Klassifikasjonssystem : "klassifikasjonssystem"
Klassifikasjonssystem ||--|o Klassifikasjonstype : "klassifikasjonstype"
Klassifikasjonssystem ||--}| Arkivdel : "arkivdel"
Klassifikasjonssystem ||--}| Klasse : "klasse"
Klassifikasjonstype ||--|o Periode : "gyldighetsperiode"
Kommune ||--|o Periode : "gyldighetsperiode"
Kommune ||--|| Fylke : "fylke"
Kontaktperson ||--|o Kontaktinformasjon : "kontaktinformasjon"
Kontaktperson ||--|o Personnavn : "kontaktperson_navn"
Kontaktperson ||--}o Person : "kontaktperson"
Korrespondansepart ||--|o Adresse : "adresse"
Korrespondansepart ||--|o Kontaktinformasjon : "kontaktinformasjon"
Korrespondansepart ||--|o Skjerming : "skjerming"
Korrespondansepart ||--|| KorrespondansepartType : "korrespondanseparttype"
KorrespondansepartType ||--|o Periode : "gyldighetsperiode"
Landkode ||--|o Periode : "gyldighetsperiode"
Matrikkelnummer ||--|o Adresse : "adresse"
Matrikkelnummer ||--|o Kommune : "kommunenummer"
Merknad ||--|| Arkivressurs : "merknadRegistrertAv"
Merknad ||--|| Merknadstype : "merknadstype"
Merknadstype ||--|o Periode : "gyldighetsperiode"
Part ||--|o Adresse : "adresse"
Part ||--|o Kontaktinformasjon : "kontaktinformasjon"
Part ||--|o PartRolle : "partRolle"
PartRolle ||--|o Periode : "gyldighetsperiode"
Person ||--|o Adresse : "bostedsadresse, postadresse"
Person ||--|o Elev : "elev"
Person ||--|o Kjonn : "kjonn"
Person ||--|o Kommune : "kommune"
Person ||--|o Kontaktinformasjon : "kontaktinformasjon"
Person ||--|o Spraak : "maalform, morsmaal"
Person ||--|| Identifikator : "fodselsnummer"
Person ||--|| Personnavn : "person_navn"
Person ||--}o Kontaktperson : "parorende"
Person ||--}o Landkode : "statsborgerskap"
Person ||--}o Person : "foreldre, foreldreansvar"
Personalmappe ||--|o AdministrativEnhet : "journalenhet"
Personalmappe ||--|o Arkivdel : "arkivdel"
Personalmappe ||--|o Arkivressurs : "avsluttetAv"
Personalmappe ||--|o Identifikator : "mappeId"
Personalmappe ||--|o Saksmappetype : "saksmappetype"
Personalmappe ||--|o Skjerming : "skjerming"
Personalmappe ||--|o Tilgangsgruppe : "tilgangsgruppe"
Personalmappe ||--|| AdministrativEnhet : "administrativEnhet"
Personalmappe ||--|| Arkivressurs : "opprettetAv, saksansvarlig"
Personalmappe ||--|| Person : "person"
Personalmappe ||--|| Personnavn : "personnavn"
Personalmappe ||--|| Saksstatus : "saksstatus"
Personalmappe ||--}o Journalpost : "journalpost"
Personalmappe ||--}o Klasse : "klasse"
Personalmappe ||--}o Merknad : "merknad"
Personalmappe ||--}o Part : "part"
Rolle ||--|o Periode : "gyldighetsperiode"
Sak ||--|o AdministrativEnhet : "journalenhet"
Sak ||--|o Arkivdel : "arkivdel"
Sak ||--|o Arkivressurs : "avsluttetAv"
Sak ||--|o Identifikator : "mappeId"
Sak ||--|o Saksmappetype : "saksmappetype"
Sak ||--|o Skjerming : "skjerming"
Sak ||--|o Tilgangsgruppe : "tilgangsgruppe"
Sak ||--|| AdministrativEnhet : "administrativEnhet"
Sak ||--|| Arkivressurs : "opprettetAv, saksansvarlig"
Sak ||--|| Saksstatus : "saksstatus"
Sak ||--}o Journalpost : "journalpost"
Sak ||--}o Klasse : "klasse"
Sak ||--}o Merknad : "merknad"
Sak ||--}o Part : "part"
Saksmappetype ||--|o Periode : "gyldighetsperiode"
Saksstatus ||--|o Periode : "gyldighetsperiode"
Skjerming ||--|| Skjermingshjemmel : "skjermingshjemmel"
Skjerming ||--|| Tilgangsrestriksjon : "tilgangsrestriksjon"
Skjermingshjemmel ||--|o Periode : "gyldighetsperiode"
SoeknadDrosjeloeyve ||--|o AdministrativEnhet : "journalenhet"
SoeknadDrosjeloeyve ||--|o Arkivdel : "arkivdel"
SoeknadDrosjeloeyve ||--|o Arkivressurs : "avsluttetAv"
SoeknadDrosjeloeyve ||--|o Identifikator : "mappeId"
SoeknadDrosjeloeyve ||--|o Saksmappetype : "saksmappetype"
SoeknadDrosjeloeyve ||--|o Skjerming : "skjerming"
SoeknadDrosjeloeyve ||--|o Tilgangsgruppe : "tilgangsgruppe"
SoeknadDrosjeloeyve ||--|| AdministrativEnhet : "administrativEnhet"
SoeknadDrosjeloeyve ||--|| Arkivressurs : "opprettetAv, saksansvarlig"
SoeknadDrosjeloeyve ||--|| Saksstatus : "saksstatus"
SoeknadDrosjeloeyve ||--}o Journalpost : "journalpost"
SoeknadDrosjeloeyve ||--}o Klasse : "klasse"
SoeknadDrosjeloeyve ||--}o Merknad : "merknad"
SoeknadDrosjeloeyve ||--}o Part : "part"
Spraak ||--|o Periode : "gyldighetsperiode"
Tilgang ||--|o AdministrativEnhet : "administrativEnhet"
Tilgang ||--|o Arkivdel : "arkivdel"
Tilgang ||--|| Rolle : "rolle"
Tilgang ||--}o Arkivressurs : "arkivressurs"
Tilgangsgruppe ||--|o Periode : "gyldighetsperiode"
Tilgangsrestriksjon ||--|o Periode : "gyldighetsperiode"
TilknyttetRegistreringSom ||--|o Periode : "gyldighetsperiode"
TilskuddFartoy ||--|o AdministrativEnhet : "journalenhet"
TilskuddFartoy ||--|o Arkivdel : "arkivdel"
TilskuddFartoy ||--|o Arkivressurs : "avsluttetAv"
TilskuddFartoy ||--|o Identifikator : "mappeId"
TilskuddFartoy ||--|o Saksmappetype : "saksmappetype"
TilskuddFartoy ||--|o Skjerming : "skjerming"
TilskuddFartoy ||--|o Tilgangsgruppe : "tilgangsgruppe"
TilskuddFartoy ||--|| AdministrativEnhet : "administrativEnhet"
TilskuddFartoy ||--|| Arkivressurs : "opprettetAv, saksansvarlig"
TilskuddFartoy ||--|| Identifikator : "soeknadsnummer"
TilskuddFartoy ||--|| Saksstatus : "saksstatus"
TilskuddFartoy ||--}o Journalpost : "journalpost"
TilskuddFartoy ||--}o Klasse : "klasse"
TilskuddFartoy ||--}o Merknad : "merknad"
TilskuddFartoy ||--}o Part : "part"
TilskuddFredaBygningPrivatEie ||--|o AdministrativEnhet : "journalenhet"
TilskuddFredaBygningPrivatEie ||--|o Arkivdel : "arkivdel"
TilskuddFredaBygningPrivatEie ||--|o Arkivressurs : "avsluttetAv"
TilskuddFredaBygningPrivatEie ||--|o Identifikator : "mappeId, soeknadsnummer"
TilskuddFredaBygningPrivatEie ||--|o Matrikkelnummer : "matrikkelnummer"
TilskuddFredaBygningPrivatEie ||--|o Saksmappetype : "saksmappetype"
TilskuddFredaBygningPrivatEie ||--|o Skjerming : "skjerming"
TilskuddFredaBygningPrivatEie ||--|o Tilgangsgruppe : "tilgangsgruppe"
TilskuddFredaBygningPrivatEie ||--|| AdministrativEnhet : "administrativEnhet"
TilskuddFredaBygningPrivatEie ||--|| Arkivressurs : "opprettetAv, saksansvarlig"
TilskuddFredaBygningPrivatEie ||--|| Saksstatus : "saksstatus"
TilskuddFredaBygningPrivatEie ||--}o Journalpost : "journalpost"
TilskuddFredaBygningPrivatEie ||--}o Klasse : "klasse"
TilskuddFredaBygningPrivatEie ||--}o Merknad : "merknad"
TilskuddFredaBygningPrivatEie ||--}o Part : "part"
Variantformat ||--|o Periode : "gyldighetsperiode"

```

