# Nasjonale grunndata – Eiendom

Domenemodell for norske eigedomsdata basert på Nasjonale grunndata (utkast). Modellerer Fast eiendom, Borettslagsandel, Matrikkelenhet, Bygning, Eierforhold og tilknytta klasser. Basert på https://informasjonsforvaltning.github.io/nasjonale-grunndata/

URI: https://data.norge.no/ngr/ngr-eiendom

Name: ngr-eiendom



## Classes







### Obligatorisk

| Class | Description |
| --- | --- |
| [Andel](andel.md) | Ein eigarandel i eit heimelsdokument (også kalt eierandel) |
| [Borettslag](borettslag.md) | Eit burettslag er ein type hovudeining (juridisk person) som eig burettslagsb... |
| [Borettslagsandel](borettslagsandel.md) | Ein andel i eit burettslag som gir eksklusiv bruksrett til ein bestemt bustad... |
| [Bruksenhet](bruksenhet.md) | Ei brukseining (leilegheit, kontor o |
| [Bruksenhetsnummer](bruksenhetsnummer.md) | Identifikator for ei brukseining innanfor ein bygning, t |
| [Bruksnummer](bruksnummer.md) | Bruksnummer innanfor gardsnamnet |
| [Bygning](bygning.md) | Ein bygning registrert i Matrikkelen |
| [Bygningsnummer](bygningsnummer.md) | Offisiell identifikator for ein bygning i Matrikkelen |
| [Eierforhold](eierforhold.md) | Abstrakt klasse for eigarforhold forvalta av Grunnboka |
| [Etasje](etasje.md) | Ei etasje i ein bygning |
| [FastEiendom](fasteiendom.md) | Fast eiendom er eit grunnomgrep i eigedomsdomenet |
| [Festenummer](festenummer.md) | Festenummer, aktuelt berre for festegrunn (0 |
| [Gaardsnummer](gaardsnummer.md) | Gårdsnummer innanfor kommunen |
| [Hjemmel](hjemmel.md) | Abstrakt klasse for heimelsdokument |
| [Kommune](kommune.md) | Norsk kommune |
| [Kommunenummer](kommunenummer.md) | Firesifra kommunenummer (t |
| [Matrikkelenhet](matrikkelenhet.md) | Abstrakt overklasse for alle typar matrikkeleiningar registrert i Matrikkelen |
| [Matrikkelnummer](matrikkelnummer.md) | Offisiell identifikator for ei matrikkelenheit, beståande av kommunenummer, g... |
| [Representasjonspunkt](representasjonspunkt.md) | Geografisk punkt (koordinatpar) som representerer posisjonen til bygningen |
| [SamletFastEiendom](samletfasteiendom.md) | Samling av to eller fleire faste eigedommar som er organiserte saman |
| [Seksjonsnummer](seksjonsnummer.md) | Seksjonsnummer, aktuelt berre for eigarseksjonar (0 |
| [YtreInngang](ytreinngang.md) | Ytre inngang til ein bygning |




### Anbefalt

| Class | Description |
| --- | --- |
| [Eierseksjon](eierseksjon.md) | Ein eigarseksjon er ein eigarandel i ein seksjonert eigedom |




### Valgfri

| Class | Description |
| --- | --- |
| [Festegrunn](festegrunn.md) | Ein del av ei grunneigendom eller eit jordsameige som nokon har festa til |
| [Grunneiendom](grunneiendom.md) | Den vanlegaste typen matrikkelenheit |
| [Jordsameie](jordsameie.md) | Eit fellesareal som vert eigd av fleire eigedommar |
| [Rettighetshaver](rettighetshaver.md) | Den som har ein rett knytt til ein eigedom |




### Andre

| Class | Description |
| --- | --- |
| [Anleggseiendom](anleggseiendom.md) | Eit volum – ein bygning eller konstruksjon – oppretta frå ei eller fleire gru... |
| [Anleggsprojeksjonsflate](anleggsprojeksjonsflate.md) | Fotavtrykk av 3D-eigedommar (anleggseigedommar) |
| [AnnenMatrikkelenhet](annenmatrikkelenhet.md) | Matrikkelenheit som ikkje fell inn under dei andre underklassane |
| [HjemmelTilEiendomsrett](hjemmeltileiendomsrett.md) | Heimelsdokument for eigedomsrett (full eigarrett) |
| [HjemmelTilFesterett](hjemmeltilfesterett.md) | Heimelsdokument for festerett (langvarig bruksrett til festegrunn) |
| [HjemmelTilFramfesterett](hjemmeltilframfesterett.md) | Heimelsdokument for framfesterett (vidarefestekontrakt) |
| [Hovedenhet](hovedenhet.md) | Ei hovudeining i Einingsregisteret |
| [IkkeTinglystEierforhold](ikketinglysteierforhold.md) | Eigarforhold som ikkje er registrert i Grunnboka |
| [OffisiellAdresse](offisielladresse.md) | Offisiell adresse tildelt av kommunen |
| [Person](person.md) | Ein fysisk person |
| [RettighetForAaBenytteEiendom](rettighetforaabenytteeiendom.md) | Rettar og avtalar som er nødvendige for å kunne benytte eigedommen |
| [Teig](teig.md) | Eit samanhengande areal med same type grenser |
| [TinglystEierforhold](tinglysteierforhold.md) | Eigarforhold registrert (tinglyst) i Grunnboka |
| [TinglystHeftelse](tinglystheftelse.md) | Heftelse tinglyst i Grunnboka mot ein eigedom eller burettslagsandel |





## Slots

| Slot | Description |
| --- | --- |
| [bestar_av_bruksnummer](bestar_av_bruksnummer.md) | Bruksnummerdelen av matrikkelnummeret |
| [bestar_av_bygning](bestar_av_bygning.md) | Bygning(ar) som inngår i denne faste eigedommen |
| [bestar_av_fast_eiendom](bestar_av_fast_eiendom.md) | Faste eigedommar som inngår i samlinga (minimum 2) |
| [bestar_av_festenummer](bestar_av_festenummer.md) | Festenummerdelen av matrikkelnummeret (berre for festegrunn) |
| [bestar_av_gaardsnummer](bestar_av_gaardsnummer.md) | Gårdsnummerdelen av matrikkelnummeret |
| [bestar_av_kommunenummer](bestar_av_kommunenummer.md) | Kommunenummerdelen av matrikkelnummeret |
| [bestar_av_matrikkelenhet](bestar_av_matrikkelenhet.md) | Matrikkeleininga denne faste eigedommen fysisk består av |
| [bestar_av_rettighet](bestar_av_rettighet.md) | Rettar som er nødvendige for å benytte eigedommen |
| [bestar_av_seksjonsnummer](bestar_av_seksjonsnummer.md) | Seksjonsnummerdelen av matrikkelnummeret (berre for eigarseksjonar) |
| [bruksnummer_verdi](bruksnummer_verdi.md) | Bruksnummer innanfor gardsnamnet |
| [bygningsnummer_verdi](bygningsnummer_verdi.md) | Unikt bygningsnummer i Matrikkelen |
| [er_av_type_hovedenhet](er_av_type_hovedenhet.md) | Hovudeininga (juridisk person) som er rettigheitshavar |
| [er_av_type_person](er_av_type_person.md) | Personen som er rettigheitshavar (fysisk person) |
| [er_del_av_teig](er_del_av_teig.md) | Teigen(e) matrikkeleininga er del av |
| [er_knyttet_til_matrikkelenhet](er_knyttet_til_matrikkelenhet.md) | Matrikkeleininga bygningen er knytt til |
| [er_tilknyttet_matrikkelenhet](er_tilknyttet_matrikkelenhet.md) | Matrikkeleininga brukseininga er knytt til |
| [etasjenummer](etasjenummer.md) | Etasjenummer (t |
| [etasjeplan](etasjeplan.md) | Kode for kva del av bygningen brukseininga ligg i (H/U/K/L/M) |
| [festenummer_verdi](festenummer_verdi.md) | Festenummer (0 |
| [gaardsnummer_verdi](gaardsnummer_verdi.md) | Gårdsnummer innanfor kommunen |
| [gjelder_bruksenhet](gjelder_bruksenhet.md) | Brukseiningane den ytre inngangen gir tilgang til |
| [gjelder_hjemmel_eiendomsrett](gjelder_hjemmel_eiendomsrett.md) | Heimelsdokument for eigedomsrett knytt til dette eigarforholdet |
| [gjelder_hjemmel_festerett](gjelder_hjemmel_festerett.md) | Heimelsdokument for festerett knytt til dette eigarforholdet |
| [gjelder_hjemmel_framfesterett](gjelder_hjemmel_framfesterett.md) | Heimelsdokument for framfesterett knytt til dette eigarforholdet |
| [gjelder_matrikkelenhet](gjelder_matrikkelenhet.md) | Matrikkeleininga dette eigarforholdet gjeld |
| [har_andel](har_andel.md) | Andel(ar) i heimelsdokumentet |
| [har_anleggsprojeksjonsflate](har_anleggsprojeksjonsflate.md) | Anleggsprojeksjonsflata (fotavtrykket) for anleggseigedommen |
| [har_bruksenhet](har_bruksenhet.md) | Brukseining(ar) i bygningen |
| [har_bruksenhetsnummer](har_bruksenhetsnummer.md) | Bruksenheitsnummeret for brukseininga |
| [har_bygningsnummer](har_bygningsnummer.md) | Offisiell bygningsnummer for bygningen |
| [har_eierforhold](har_eierforhold.md) | Eigarforhold knytt til eigedommen eller burettslagsandelen |
| [har_etasje](har_etasje.md) | Etasjar i bygningen |
| [har_offisiell_adresse](har_offisiell_adresse.md) | Offisiell adresse for den ytre inngangen eller brukseininga |
| [har_representasjonspunkt](har_representasjonspunkt.md) | Geografisk representasjonspunkt for bygningen |
| [har_rettighetshaver](har_rettighetshaver.md) | Rettigheitshavar(ar) for andelen |
| [har_teig](har_teig.md) | Teigen(e) som tilhøyrer matrikkeleininga |
| [har_tinglyst_heftelse](har_tinglyst_heftelse.md) | Tinglyste heftingar knytt til eigedommen eller burettslagsandelen |
| [har_ytre_inngang](har_ytre_inngang.md) | Ytre inngang(ar) til bygningen |
| [id](id.md) | URI-identifikator for ressursen |
| [identifiseres_av](identifiseres_av.md) | Matrikkeleininga som identifiserer denne faste eigedommen |
| [identifiseres_med](identifiseres_med.md) | Matrikkelnummeret som identifiserer matrikkeleininga |
| [kan_gjelde_borettslagsandel](kan_gjelde_borettslagsandel.md) | Burettslagsandelen dette eigarforholdet eventuelt gjeld |
| [kan_vaere_pa](kan_vaere_pa.md) | Matrikkeleininga denne eininga ligg på eller er knytt til |
| [kommunenummer_verdi](kommunenummer_verdi.md) | Firesifra kommunenummer (t |
| [koordinat_nord](koordinat_nord.md) | Nordleg koordinat (Y) i det angitte koordinatsystemet |
| [koordinat_ost](koordinat_ost.md) | Austleg koordinat (X) i det angitte koordinatsystemet |
| [koordinatsystem](koordinatsystem.md) | Koordinatsystem/projeksjon (t |
| [ligger_i_etasje](ligger_i_etasje.md) | Etasjen(e) brukseininga ligg i |
| [ligger_innenfor_kommune](ligger_innenfor_kommune.md) | Kommunen matrikkeleininga ligg innanfor |
| [nummerering_i_etasjen](nummerering_i_etasjen.md) | Løpenummer for brukseininga innanfor etasjen |
| [seksjonsnummer_verdi](seksjonsnummer_verdi.md) | Seksjonsnummer (0 |
| [tilhoerer_borettslag](tilhoerer_borettslag.md) | Burettslagsandelen tilhøyrer dette burettslaget |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [Etasjeplan](etasjeplan.md) | Kode for kva del av bygningen ei brukseining ligg i |


## Types

| Type | Description |
| --- | --- |


## Subsets

| Subset | Description |
| --- | --- |
| [Anbefalt](anbefalt.md) | Anbefalte eigenskapar i domenemodellen |
| [Obligatorisk](obligatorisk.md) | Obligatoriske eigenskapar i domenemodellen |
| [Valgfri](valgfri.md) | Valfrie eigenskapar i domenemodellen |
