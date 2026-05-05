# fint-administrasjon

## Artefacts

| Artefakt | Fil |
|----------|-----|
| SHACL shapes | [fint-administrasjon-shapes.ttl](fint-administrasjon-shapes.ttl) |
| JSON-LD kontekst | [fint-administrasjon-context.jsonld](fint-administrasjon-context.jsonld) |
| JSON Schema | [fint-administrasjon-schema.json](fint-administrasjon-schema.json) |
| OWL ontologi | [fint-administrasjon-ontology.ttl](fint-administrasjon-ontology.ttl) |
| Python-klasser | [fint-administrasjon-model.py](fint-administrasjon-model.py) |
| ER-diagram (Mermaid) | [fint-administrasjon-erdiagram.md](fint-administrasjon-erdiagram.md) |
| Eksempeldata (Turtle) | [fint-administrasjon-eksempel.ttl](fint-administrasjon-eksempel.ttl) |

## Oversiktsdiagram

```mermaid
erDiagram
Adresse {
    stringList adresselinje  
    string postnummer  
    string poststed  
}
Aktivitet {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Anlegg {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Ansvar {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Arbeidsforhold {
    uriorcurie id  
    integer aarslonn  
    integer ansettelsesprosent  
    boolean hovedstilling  
    integer lonnsprosent  
    string stillingsnummer  
    string stillingstittel  
    integer tilstedeprosent  
    uriorcurie undervisningsforhold  
}
Arbeidsforholdstype {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Arbeidslokasjon {
    uriorcurie id  
    string lokasjonsnavn  
    string organisasjonsnavn  
}
Art {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Diverse {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Fastlonn {
    integer prosent  
    uriorcurie id  
    datetime anvist  
    datetime attestert  
    string beskrivelse  
    datetime kontert  
}
Fasttillegg {
    integer belop  
    uriorcurie id  
    datetime anvist  
    datetime attestert  
    string beskrivelse  
    datetime kontert  
}
Formaal {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Fravaer {
    uriorcurie id  
    datetime godkjent  
    integer prosent  
}
Fravaersgrunn {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Fravaerstype {
    boolean overfores  
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Fullmakt {
    uriorcurie id  
}
Funksjon {
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
Kjonn {
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
Kontostreng {

}
Kontrakt {
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
Lonsart {
    string kategori  
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Lopenummer {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Objekt {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Organisasjonselement {
    uriorcurie id  
    string kortnavn  
    string navn  
    string organisasjonsnavn  
    uriorcurie skole  
}
Organisasjonstype {
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
    uriorcurie elev  
    date fodselsdato  
    uriorcurieList laerling  
    uriorcurie otungdom  
    uriorcurie personalressurs  
}
Personalressurs {
    uriorcurie id  
    date ansiennitet  
    string jobbtittel  
    uriorcurie skoleressurs  
}
Personalressurskategori {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Personnavn {
    string etternavn  
    string fornavn  
    string mellomnavn  
}
Prosjekt {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Prosjektart {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Ramme {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Rolle {
    uriorcurie id  
    string beskrivelse  
}
Spraak {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Stillingskode {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Uketimetall {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Valuta {
    uriorcurie id  
    string navn  
}
Variabellonn {
    integer antall  
    integer belop  
    uriorcurie id  
    datetime anvist  
    datetime attestert  
    string beskrivelse  
    datetime kontert  
}
Virksomhet {
    uriorcurie id  
    uriorcurieList laerling  
    string organisasjonsnavn  
}

Adresse ||--|o Landkode : "land"
Aktivitet ||--|o Periode : "gyldighetsperiode"
Anlegg ||--|o Periode : "gyldighetsperiode"
Ansvar ||--|o Ansvar : "overordnet"
Ansvar ||--|o Periode : "gyldighetsperiode"
Ansvar ||--}o Ansvar : "underordnet"
Ansvar ||--}o Organisasjonselement : "organisasjonselement"
Arbeidsforhold ||--|o Aktivitet : "aktivitet"
Arbeidsforhold ||--|o Anlegg : "anlegg"
Arbeidsforhold ||--|o Ansvar : "ansvar"
Arbeidsforhold ||--|o Arbeidsforholdstype : "arbeidsforholdstype"
Arbeidsforhold ||--|o Arbeidslokasjon : "arbeidslokasjon"
Arbeidsforhold ||--|o Art : "art"
Arbeidsforhold ||--|o Diverse : "diverse"
Arbeidsforhold ||--|o Formaal : "formaal"
Arbeidsforhold ||--|o Funksjon : "funksjon"
Arbeidsforhold ||--|o Kontrakt : "kontrakt"
Arbeidsforhold ||--|o Lopenummer : "lopenummer"
Arbeidsforhold ||--|o Objekt : "objekt"
Arbeidsforhold ||--|o Periode : "arbeidsforholdsperiode"
Arbeidsforhold ||--|o Personalressurs : "personalleder"
Arbeidsforhold ||--|o Prosjekt : "prosjekt"
Arbeidsforhold ||--|o Ramme : "ramme"
Arbeidsforhold ||--|o Stillingskode : "stillingskode"
Arbeidsforhold ||--|o Uketimetall : "timerPerUke"
Arbeidsforhold ||--|| Organisasjonselement : "arbeidssted"
Arbeidsforhold ||--|| Periode : "gyldighetsperiode"
Arbeidsforhold ||--|| Personalressurs : "personalressurs"
Arbeidsforhold ||--}o Fastlonn : "fastlonn"
Arbeidsforhold ||--}o Fasttillegg : "fasttillegg"
Arbeidsforhold ||--}o Fravaer : "fravaer"
Arbeidsforhold ||--}o Variabellonn : "variabellonn"
Arbeidsforholdstype ||--|o Arbeidsforholdstype : "forelder"
Arbeidsforholdstype ||--|o Periode : "gyldighetsperiode"
Arbeidslokasjon ||--|o Adresse : "forretningsadresse, postadresse"
Arbeidslokasjon ||--|o Identifikator : "organisasjonsnummer"
Arbeidslokasjon ||--|o Kontaktinformasjon : "kontaktinformasjon"
Arbeidslokasjon ||--|| Identifikator : "lokasjonskode"
Arbeidslokasjon ||--}o Arbeidsforhold : "arbeidsforhold"
Art ||--|o Periode : "gyldighetsperiode"
Diverse ||--|o Periode : "gyldighetsperiode"
Fastlonn ||--|o Identifikator : "kildesystemId"
Fastlonn ||--|o Lonsart : "lonsart"
Fastlonn ||--|o Periode : "opptjent"
Fastlonn ||--|o Personalressurs : "anviser, attestant, konterer"
Fastlonn ||--|| Arbeidsforhold : "arbeidsforhold"
Fastlonn ||--|| Kontostreng : "kontostreng"
Fastlonn ||--|| Periode : "periode"
Fasttillegg ||--|o Identifikator : "kildesystemId"
Fasttillegg ||--|o Periode : "opptjent"
Fasttillegg ||--|o Personalressurs : "anviser, attestant, konterer"
Fasttillegg ||--|| Arbeidsforhold : "arbeidsforhold"
Fasttillegg ||--|| Kontostreng : "kontostreng"
Fasttillegg ||--|| Lonsart : "lonsart"
Fasttillegg ||--|| Periode : "periode"
Formaal ||--|o Periode : "gyldighetsperiode"
Fravaer ||--|o Fravaer : "fortsettelse, fortsetter"
Fravaer ||--|o Fravaersgrunn : "fravaersgrunn"
Fravaer ||--|o Identifikator : "kildesystemId"
Fravaer ||--|o Personalressurs : "godkjenner"
Fravaer ||--|| Fravaerstype : "fravaerstype"
Fravaer ||--|| Periode : "periode"
Fravaer ||--}| Arbeidsforhold : "arbeidsforhold"
Fravaersgrunn ||--|o Periode : "gyldighetsperiode"
Fravaerstype ||--|o Lonsart : "lonsart"
Fravaerstype ||--|o Periode : "gyldighetsperiode"
Fullmakt ||--|o Aktivitet : "aktivitet"
Fullmakt ||--|o Anlegg : "anlegg"
Fullmakt ||--|o Ansvar : "ansvar"
Fullmakt ||--|o Art : "art"
Fullmakt ||--|o Diverse : "diverse"
Fullmakt ||--|o Formaal : "formaal"
Fullmakt ||--|o Funksjon : "funksjon"
Fullmakt ||--|o Kontrakt : "kontrakt"
Fullmakt ||--|o Lopenummer : "lopenummer"
Fullmakt ||--|o Objekt : "objekt"
Fullmakt ||--|o Organisasjonselement : "organisasjonselement"
Fullmakt ||--|o Personalressurs : "fullmektig, stedfortreder"
Fullmakt ||--|o Prosjekt : "prosjekt"
Fullmakt ||--|o Ramme : "ramme"
Fullmakt ||--|| Periode : "gyldighetsperiode"
Fullmakt ||--|| Rolle : "rolle"
Funksjon ||--|o Funksjon : "overordnet"
Funksjon ||--|o Periode : "gyldighetsperiode"
Funksjon ||--}o Funksjon : "underordnet"
Fylke ||--|o Periode : "gyldighetsperiode"
Fylke ||--}o Kommune : "kommune"
Identifikator ||--|o Periode : "gyldighetsperiode"
Kjonn ||--|o Periode : "gyldighetsperiode"
Kommune ||--|o Periode : "gyldighetsperiode"
Kommune ||--|| Fylke : "fylke"
Kontaktperson ||--|o Kontaktinformasjon : "kontaktinformasjon"
Kontaktperson ||--|o Personnavn : "navn"
Kontaktperson ||--}o Person : "kontaktperson"
Kontostreng ||--|o Aktivitet : "aktivitet"
Kontostreng ||--|o Anlegg : "anlegg"
Kontostreng ||--|o Diverse : "diverse"
Kontostreng ||--|o Formaal : "formaal"
Kontostreng ||--|o Kontrakt : "kontrakt"
Kontostreng ||--|o Lopenummer : "lopenummer"
Kontostreng ||--|o Objekt : "objekt"
Kontostreng ||--|o Prosjekt : "prosjekt"
Kontostreng ||--|o Prosjektart : "prosjektart"
Kontostreng ||--|o Ramme : "ramme"
Kontostreng ||--|| Ansvar : "ansvar"
Kontostreng ||--|| Art : "art"
Kontostreng ||--|| Funksjon : "funksjon"
Kontrakt ||--|o Periode : "gyldighetsperiode"
Landkode ||--|o Periode : "gyldighetsperiode"
Lonsart ||--|o Art : "art"
Lonsart ||--|o Periode : "gyldighetsperiode"
Lopenummer ||--|o Periode : "gyldighetsperiode"
Objekt ||--|o Periode : "gyldighetsperiode"
Organisasjonselement ||--|o Adresse : "forretningsadresse, postadresse"
Organisasjonselement ||--|o Identifikator : "organisasjonsnummer"
Organisasjonselement ||--|o Kontaktinformasjon : "kontaktinformasjon"
Organisasjonselement ||--|o Organisasjonstype : "organisasjonstype"
Organisasjonselement ||--|o Periode : "gyldighetsperiode"
Organisasjonselement ||--|o Personalressurs : "leder"
Organisasjonselement ||--|| Identifikator : "organisasjonsId, organisasjonsKode"
Organisasjonselement ||--|| Organisasjonselement : "overordnet"
Organisasjonselement ||--}o Ansvar : "ansvar"
Organisasjonselement ||--}o Arbeidsforhold : "arbeidsforhold"
Organisasjonselement ||--}o Organisasjonselement : "underordnet"
Organisasjonstype ||--|o Periode : "gyldighetsperiode"
Person ||--|o Adresse : "bostedsadresse, postadresse"
Person ||--|o Kjonn : "kjonn"
Person ||--|o Kommune : "kommune"
Person ||--|o Kontaktinformasjon : "kontaktinformasjon"
Person ||--|o Spraak : "maalform, morsmaal"
Person ||--|| Identifikator : "fodselsnummer"
Person ||--|| Personnavn : "navn"
Person ||--}o Kontaktperson : "parorende"
Person ||--}o Landkode : "statsborgerskap"
Person ||--}o Person : "foreldre, foreldreansvar"
Personalressurs ||--|o Identifikator : "brukernavn"
Personalressurs ||--|o Kontaktinformasjon : "kontaktinformasjon"
Personalressurs ||--|| Identifikator : "ansattnummer"
Personalressurs ||--|| Periode : "ansettelsesperiode"
Personalressurs ||--|| Person : "person"
Personalressurs ||--|| Personalressurskategori : "personalressurskategori"
Personalressurs ||--}o Arbeidsforhold : "arbeidsforhold, personalansvar"
Personalressurs ||--}o Fullmakt : "fullmakt, stedfortreder"
Personalressurs ||--}o Organisasjonselement : "lederFor"
Personalressurskategori ||--|o Periode : "gyldighetsperiode"
Prosjekt ||--|o Periode : "gyldighetsperiode"
Prosjekt ||--}o Prosjektart : "prosjektart"
Prosjektart ||--|o Periode : "gyldighetsperiode"
Prosjektart ||--|o Prosjekt : "prosjekt"
Prosjektart ||--|o Prosjektart : "overordnet"
Prosjektart ||--}o Prosjektart : "underordnet"
Ramme ||--|o Periode : "gyldighetsperiode"
Rolle ||--|| Identifikator : "rolleNavn"
Rolle ||--}| Fullmakt : "fullmakt"
Spraak ||--|o Periode : "gyldighetsperiode"
Stillingskode ||--|o Periode : "gyldighetsperiode"
Stillingskode ||--|o Stillingskode : "forelder"
Uketimetall ||--|o Periode : "gyldighetsperiode"
Valuta ||--|| Identifikator : "bokstavkode, nummerkode"
Variabellonn ||--|o Identifikator : "kildesystemId"
Variabellonn ||--|o Periode : "opptjent"
Variabellonn ||--|o Personalressurs : "anviser, attestant, konterer"
Variabellonn ||--|| Arbeidsforhold : "arbeidsforhold"
Variabellonn ||--|| Kontostreng : "kontostreng"
Variabellonn ||--|| Lonsart : "lonsart"
Variabellonn ||--|| Periode : "periode"
Virksomhet ||--|o Adresse : "forretningsadresse, postadresse"
Virksomhet ||--|o Identifikator : "organisasjonsnummer"
Virksomhet ||--|o Kontaktinformasjon : "kontaktinformasjon"
Virksomhet ||--|| Identifikator : "virksomhetsId"

```



FINT-domenemodell for administrasjon og HR. Dekkjer personalressursar, arbeidsforhold, fullmakter og organisasjonsstruktur.


URI: https://data.norge.no/linkml/fint-administrasjon

Name: fint-administrasjon



## Classes

| Class | Description |
| --- | --- |
| [AdministrasjonContainer](klasser/administrasjoncontainer.md) | Rotcontainer for FINT Administrasjon-instansar |
| [Adresse](klasser/adresse.md) | Fysisk adresse eller postadresse |
| [Aktoer](klasser/aktoer.md) | Abstrakt base for person eller eining vi samhandlar med |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Enhet](klasser/enhet.md) | Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd iden... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Virksomhet](klasser/virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Person](klasser/person.md) | Fysiske private personar |
| [Arbeidsforhold](klasser/arbeidsforhold.md) | Eit avtaleforhold mellom personalressurs og arbeidsgjevar |
| [Arbeidslokasjon](klasser/arbeidslokasjon.md) | Fysisk lokasjon der ein tilsett har sitt arbeidsstad |
| [Begrep](klasser/begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Aktivitet](klasser/aktivitet.md) | Del av kontostrengen og detaljering av funksjon |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Anlegg](klasser/anlegg.md) | Del av kontostrengen; objekt som skal aktiverast eller avskrivast |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Ansvar](klasser/ansvar.md) | Del av kontostrengen som beskriv kven som har ansvaret for ei utgift eller in... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Arbeidsforholdstype](klasser/arbeidsforholdstype.md) | Viser kva behov hos arbeidsgjevar arbeidsforholdet dekkjer |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Art](klasser/art.md) | Del av kontostrengen som beskriv kva slags inntekter og utgifter det gjeld |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Diverse](klasser/diverse.md) | Del av kontostrengen; supplement til øvrige dimensjonar |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Formaal](klasser/formaal.md) | Del av kontostrengen som detaljerer inntekter og utgifter ved drift |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fravaersgrunn](klasser/fravaersgrunn.md) | Grunn til fråvær |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fravaerstype](klasser/fravaerstype.md) | Type fråvær |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Funksjon](klasser/funksjon.md) | Del av kontostrengen som beskriv kva som vert produsert |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fylke](klasser/fylke.md) | Liste over Norges fylker |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kjonn](klasser/kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kommune](klasser/kommune.md) | Liste over Norges kommunar |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kontrakt](klasser/kontrakt.md) | Kontrakt transaksjonen er knytt til |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Landkode](klasser/landkode.md) | Landskode i ISO 3166-1 alpha-2 format |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Lonsart](klasser/lonsart.md) | Type ytelse |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Lopenummer](klasser/lopenummer.md) | Løpenummer i ei nummerserie |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Objekt](klasser/objekt.md) | Eit bygg, ein veg eller ein mottakar av ei teneste eller eit tilskott |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Organisasjonstype](klasser/organisasjonstype.md) | Typen til eit organisasjonselement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Personalressurskategori](klasser/personalressurskategori.md) | Ansettelsesform til eit arbeidsforhold |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Prosjekt](klasser/prosjekt.md) | Del av kontostrengen som peikar på løpande prosjekt |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Prosjektart](klasser/prosjektart.md) | Element i ei prosjektnedbrytningsstruktur eller arbeidsnedbrytningsstruktur |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Ramme](klasser/ramme.md) | Del av kontostrengen som viser kva budsjettramme som skal bere kostnadane |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Spraak](klasser/spraak.md) | Verdiar for språk (2 bokstavar) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Stillingskode](klasser/stillingskode.md) | Felles kodeverk for stillingar |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Uketimetall](klasser/uketimetall.md) | Timer per veke i 100 % stilling |
| [Fravaer](klasser/fravaer.md) | Fråvær frå eit arbeidsforhold |
| [Fullmakt](klasser/fullmakt.md) | Fullmakt til å gjere handlingar i høve til ei gjeven Rolle |
| [Identifikator](klasser/identifikator.md) | Unik identifikasjon til eit objekt |
| [Kontaktinformasjon](klasser/kontaktinformasjon.md) | Informasjon som kan brukast for å oppnå kontakt |
| [Kontaktperson](klasser/kontaktperson.md) | Kontaktperson (pårørande) til ein person |
| [Kontostreng](klasser/kontostreng.md) | Sammensetning av kontodimensjonar for bokføring |
| [Lonn](klasser/lonn.md) | Informasjon om lønn for eit arbeidsforhold (abstrakt base) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fastlonn](klasser/fastlonn.md) | Informasjon om fast lønnsbeordring |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fasttillegg](klasser/fasttillegg.md) | Faste tillegg til utbetaling |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Variabellonn](klasser/variabellonn.md) | Informasjon om variabel lønn |
| [Matrikkelnummer](klasser/matrikkelnummer.md) | Eintydleg identifisering av matrikkeleining innanfor kommune |
| [Organisasjonselement](klasser/organisasjonselement.md) | Eit element i organisasjonsstrukturen |
| [Periode](klasser/periode.md) | Tidsperiode med obligatorisk start og valfri slutt |
| [Personalressurs](klasser/personalressurs.md) | Arbeidstakar eller oppdragstakar i organisasjonen |
| [Personnavn](klasser/personnavn.md) | Namn på ein person |
| [Rolle](klasser/rolle.md) | Rettighet eller type fullmakt |
| [Valuta](klasser/valuta.md) | Valutakodar for offisielle valutaer |



## Slots

| Slot | Description |
| --- | --- |
| [aarslonn](klasser/aarslonn.md) | Årslønn/grunnlønn i 100 % stilling |
| [adresse](klasser/adresse.md) | Adresse til matrikkeleining |
| [adresselinje](klasser/adresselinje.md) | Adresseinformasjon |
| [aktivitet](klasser/aktivitet.md) | Detaljering av funksjon |
| [aktivitetar](klasser/aktivitetar.md) |  |
| [anlegg](klasser/anlegg.md) |  |
| [ansattnummer](klasser/ansattnummer.md) | Unik identifikator for den tilsette i HR-systemet |
| [ansettelsesperiode](klasser/ansettelsesperiode.md) | Perioden personalressursen er i eit tilhøve til organisasjonen |
| [ansettelsesprosent](klasser/ansettelsesprosent.md) | Prosenten personalressursen eig i høve til arbeidsavtalen |
| [ansiennitet](klasser/ansiennitet.md) | Ansiennitet for personalressurs hos arbeidsgjevar |
| [ansvar](klasser/ansvar.md) |  |
| [antall](klasser/antall.md) | Mengde som vert beskriven av tillegget, i hundredeler |
| [anviser](klasser/anviser.md) | Personalressurs som har anvist lønsmeldinga etter fullmakt |
| [anvist](klasser/anvist.md) | Tidspunkt då lønn vart anvist |
| [arbeidsforhold](klasser/arbeidsforhold.md) |  |
| [arbeidsforholdsperiode](klasser/arbeidsforholdsperiode.md) | Periode for ei gjeven stilling |
| [arbeidsforholdstypar](klasser/arbeidsforholdstypar.md) |  |
| [arbeidsforholdstype](klasser/arbeidsforholdstype.md) | Beskriven kode som kategoriserer kva funksjon stillinga er gruppert til |
| [arbeidslokasjon](klasser/arbeidslokasjon.md) | Fysisk lokasjon der den tilsette har sitt arbeidsstad |
| [arbeidslokasjoner](klasser/arbeidslokasjoner.md) |  |
| [arbeidssted](klasser/arbeidssted.md) | Tilhøyrsle til organisasjonsstrukturen |
| [art](klasser/art.md) | Type inntekt eller utgift |
| [artar](klasser/artar.md) |  |
| [attestant](klasser/attestant.md) | Personalressurs som har attestert lønsmeldinga etter fullmakt |
| [attestert](klasser/attestert.md) | Tidspunkt då lønn vart attestert |
| [belop](klasser/belop.md) | Beløp i øre |
| [beskrivelse](klasser/beskrivelse.md) | Beskriving av lønn til føring på lønnslipp |
| [bilde](klasser/bilde.md) | HTTP(S)-lenkje til eit bilete av personen |
| [bokstavkode](klasser/bokstavkode.md) | Bokstavkode for aktuell valuta |
| [bostedsadresse](klasser/bostedsadresse.md) | Folkeregistrert adresse til personen |
| [brukernavn](klasser/brukernavn.md) | Brukarnamn til den tilsette |
| [bruksnummer](klasser/bruksnummer.md) | Fortløpande nummerering av bruk under gårdsnummer |
| [diverse](klasser/diverse.md) |  |
| [elev](klasser/elev.md) | Referanse til Elev (Utdanning) |
| [epostadresse](klasser/epostadresse.md) | Namngitt elektronisk adresse for mottak av e-post |
| [etternavn](klasser/etternavn.md) | Etternamn til personen |
| [fastlonn](klasser/fastlonn.md) |  |
| [fasttillegg](klasser/fasttillegg.md) |  |
| [festenummer](klasser/festenummer.md) | Fortløpande nummerering av festar under gårdsnummer/bruksnummer |
| [fodselsdato](klasser/fodselsdato.md) | Dato for fødsel |
| [fodselsnummer](klasser/fodselsnummer.md) | Fødselsnummer eller ein av dei fiktive variantane |
| [forelder](klasser/forelder.md) | For å byggje hierarki av Arbeidsforholdstype |
| [foreldre](klasser/foreldre.md) | Den/dei som har foreldreansvar til personen |
| [foreldreansvar](klasser/foreldreansvar.md) | Personar denne personen har foreldreansvar for |
| [formaal](klasser/formaal.md) |  |
| [fornavn](klasser/fornavn.md) | Fornamn til personen |
| [forretningsadresse](klasser/forretningsadresse.md) | Besøksadresse til organisasjonseininga |
| [fortsettelse](klasser/fortsettelse.md) | Fortsetjande fråvær |
| [fortsetter](klasser/fortsetter.md) | Fråværet dette fråværet er fortsetjing av |
| [fravaer](klasser/fravaer.md) |  |
| [fravaersgrunn](klasser/fravaersgrunn.md) | Grunn til fråværet |
| [fravaersgrunnar](klasser/fravaersgrunnar.md) |  |
| [fravaerstypar](klasser/fravaerstypar.md) |  |
| [fravaerstype](klasser/fravaerstype.md) | Type fråvær |
| [fullmakt](klasser/fullmakt.md) | Alle fullmakter av denne typen |
| [fullmakter](klasser/fullmakter.md) |  |
| [fullmektig](klasser/fullmektig.md) | Personalressurs som har fått fullmakt til ei gjeven rolle |
| [funksjon](klasser/funksjon.md) | Det som vert produsert eller tenesta som vert levert |
| [funksjonar](klasser/funksjonar.md) |  |
| [fylke](klasser/fylke.md) |  |
| [gaardsnummer](klasser/gaardsnummer.md) | Nummerering av gårdseiging i matrikkelen, unik innanfor kommune |
| [godkjenner](klasser/godkjenner.md) | Personalressurs som har godkjent fråværsmeldinga |
| [godkjent](klasser/godkjent.md) | Tidspunkt då fråværet vart godkjent |
| [gyldighetsperiode](klasser/gyldighetsperiode.md) | Periode fullmakta er gyldig for |
| [hovedstilling](klasser/hovedstilling.md) | Angir kva arbeidsforhold som er hovudarbeidsforhold |
| [id](klasser/id.md) | URI-identifikator for ressursen |
| [identifikatorverdi](klasser/identifikatorverdi.md) | Ein konkret kombinasjon av teikn og/eller bokstavar som utgjer ein bestemt id... |
| [jobbtittel](klasser/jobbtittel.md) | Namn som beskriv jobben eller stillinga |
| [kategori](klasser/kategori.md) | Kategori lønnsart |
| [kildesystemId](klasser/kildesystemid.md) | Kjeldesystemets unike identifikator for lønn |
| [kjonn](klasser/kjonn.md) |  |
| [kode](klasser/kode.md) | Verdi som identifiserer omgrepet |
| [kommunar](klasser/kommunar.md) |  |
| [kommune](klasser/kommune.md) | Alle kommunar som inngår i fylket |
| [kommunenummer](klasser/kommunenummer.md) | Nummerering av kommunen i høve til SSB si offisielle liste |
| [kontaktinformasjon](klasser/kontaktinformasjon.md) | Kontaktinformasjon til arbeidslokasjonen |
| [kontaktperson](klasser/kontaktperson.md) | Personar kontaktpersonen er pårørande for |
| [kontaktpersonar](klasser/kontaktpersonar.md) |  |
| [konterer](klasser/konterer.md) | Personalressurs som har kontert lønsmeldinga etter fullmakt |
| [kontert](klasser/kontert.md) | Tidspunkt då lønn vart kontert |
| [kontostreng](klasser/kontostreng.md) | Kontering av lønn |
| [kontrakt](klasser/kontrakt.md) | Kontostrengens kontraktsegment |
| [kontrakter](klasser/kontrakter.md) |  |
| [kortnavn](klasser/kortnavn.md) | Forkorta namn som beskriv organisasjonselementet |
| [laerling](klasser/laerling.md) | Referanse til Laerling (Utdanning) |
| [land](klasser/land.md) | Land der adressa befinn seg |
| [landkodar](klasser/landkodar.md) |  |
| [leder](klasser/leder.md) | Ansvarleg leiar for organisasjonselementet |
| [lederFor](klasser/lederfor.md) | Organisasjonselement personalressursen er leiar for |
| [lokasjonskode](klasser/lokasjonskode.md) | Kode som identifiserer ein arbeidslokasjon |
| [lokasjonsnavn](klasser/lokasjonsnavn.md) | Namn som beskriv ein arbeidslokasjon |
| [lonnsprosent](klasser/lonnsprosent.md) | Prosent av årslønn den tilsette skal ha utbetalt |
| [lonsart](klasser/lonsart.md) | Lønnsart fråværstypen vert ført på |
| [lonsartar](klasser/lonsartar.md) |  |
| [lopenummer](klasser/lopenummer.md) |  |
| [maalform](klasser/maalform.md) | Målform personen føretrekkjer |
| [mellomnavn](klasser/mellomnavn.md) | Mellomnamn |
| [mobiltelefonnummer](klasser/mobiltelefonnummer.md) | Mobiltelefonnummer |
| [morsmaal](klasser/morsmaal.md) | Morsmål til personen |
| [navn](klasser/navn.md) | Namn på organisasjonselementet |
| [nettsted](klasser/nettsted.md) | Adresse til eit nettstad |
| [nummerkode](klasser/nummerkode.md) | Nummerkode for aktuell valuta |
| [objekt](klasser/objekt.md) |  |
| [opptjent](klasser/opptjent.md) | Periode der lønn vart opptent |
| [organisasjonselement](klasser/organisasjonselement.md) |  |
| [organisasjonsId](klasser/organisasjonsid.md) | Unikt internnummer for organisasjonselementet |
| [organisasjonsKode](klasser/organisasjonskode.md) | Beskriven kode for organisasjonselementet |
| [organisasjonsnavn](klasser/organisasjonsnavn.md) | Namn på eining registrert i Einingsregisteret |
| [organisasjonsnummer](klasser/organisasjonsnummer.md) | Niisifra nummer som eintydleg identifiserer einingar i Einingsregisteret |
| [organisasjonstypar](klasser/organisasjonstypar.md) |  |
| [organisasjonstype](klasser/organisasjonstype.md) | Kva type organisasjonselement dette er |
| [otungdom](klasser/otungdom.md) | Referanse til OtUngdom (Utdanning) |
| [overfores](klasser/overfores.md) | Angir om fråvær av denne typen skal overførast til HR |
| [overordnet](klasser/overordnet.md) | Overordna ansvar |
| [parorende](klasser/parorende.md) | Pårørande kontaktperson til personen |
| [passiv](klasser/passiv.md) | Angir at koden er passiv og ikkje kan veljast |
| [periode](klasser/periode.md) | Periode lønn vert utbetalt |
| [person](klasser/person.md) | Person som er ein personalressurs |
| [personalansvar](klasser/personalansvar.md) | Arbeidsforhold der personalressursen har personalansvar |
| [personalleder](klasser/personalleder.md) | Personalleiar til arbeidsforholdet |
| [personalressurs](klasser/personalressurs.md) | Personalressurs til arbeidsforholdet |
| [personalressursar](klasser/personalressursar.md) |  |
| [personalressurskategori](klasser/personalressurskategori.md) | Kategori for personalressursen |
| [personalressurskategoriar](klasser/personalressurskategoriar.md) |  |
| [personar](klasser/personar.md) |  |
| [postadresse](klasser/postadresse.md) | Postadresse til arbeidslokasjonen |
| [postnummer](klasser/postnummer.md) | Postnummer |
| [poststed](klasser/poststed.md) | Poststad |
| [prosent](klasser/prosent.md) | Andel av lønnsprosent som vert beslaglagt |
| [prosjekt](klasser/prosjekt.md) |  |
| [prosjektart](klasser/prosjektart.md) | Deloppgåve eller delprosjekt |
| [prosjektartar](klasser/prosjektartar.md) |  |
| [ramme](klasser/ramme.md) | Budsjettramme som skal bere kostnadane |
| [rammer](klasser/rammer.md) |  |
| [rollar](klasser/rollar.md) |  |
| [rolle](klasser/rolle.md) | Kva type fullmakt |
| [rolleNavn](klasser/rollenavn.md) | Namn på rolla; unik identifikator |
| [seksjonsnummer](klasser/seksjonsnummer.md) | Fortløpande nummerering av seksjonar under gårdsnummer/bruksnummer |
| [sip](klasser/sip.md) | SIP-protokoll for VoIP (IP-telefoni) |
| [skole](klasser/skole.md) | Referanse til Skole (Utdanning) |
| [skoleressurs](klasser/skoleressurs.md) | Referanse til Skoleressurs (Utdanning) |
| [slutt](klasser/slutt.md) | Til tidspunkt |
| [spraak](klasser/spraak.md) |  |
| [start](klasser/start.md) | Frå tidspunkt |
| [statsborgerskap](klasser/statsborgerskap.md) | Alle statsborgarskap personen har |
| [stedfortreder](klasser/stedfortreder.md) | Personalressurs som er stedfortredar for den fullmektige |
| [stillingskode](klasser/stillingskode.md) | Firesifra stillingskode frå KS, eventuelt utvida med to siffer |
| [stillingskoder](klasser/stillingskoder.md) |  |
| [stillingsnummer](klasser/stillingsnummer.md) | Løpenummer for stillinga |
| [stillingstittel](klasser/stillingstittel.md) | Arbeidstakarens stillingstittel i gjeldande stilling |
| [telefonnummer](klasser/telefonnummer.md) | Telefonnummer |
| [tilstedeprosent](klasser/tilstedeprosent.md) | Det personalressursen faktisk jobbar |
| [timerPerUke](klasser/timerperuke.md) | Timer per veke i 100 % stilling |
| [type](klasser/type.md) | Beskriv kva slags type kontaktperson |
| [uketimetall](klasser/uketimetall.md) |  |
| [underordnet](klasser/underordnet.md) | Alle underansvar |
| [undervisningsforhold](klasser/undervisningsforhold.md) | Referanse til Undervisningsforhold (Utdanning) |
| [valuta](klasser/valuta.md) |  |
| [variabellonn](klasser/variabellonn.md) |  |
| [virksomhetar](klasser/virksomhetar.md) |  |
| [virksomhetsId](klasser/virksomhetsid.md) | Intern unik identifikator i økonomisystemet |


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
| [Float](klasser/float.md) | A real number that conforms to the xsd:float specification |
| [Integer](klasser/integer.md) | An integer |
| [Jsonpath](klasser/jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](klasser/jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](klasser/ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](klasser/nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](klasser/objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](klasser/sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](klasser/string.md) | A character string |
| [Time](klasser/time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](klasser/uri.md) | a complete URI |
| [Uriorcurie](klasser/uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
| [Anbefalt](klasser/anbefalt.md) | Anbefalt eigensskap |
| [Obligatorisk](klasser/obligatorisk.md) | Obligatorisk eigensskap |
| [Valgfri](klasser/valgfri.md) | Valfri eigensskap |
