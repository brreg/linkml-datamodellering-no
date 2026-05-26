# CPSV-AP-NO

Norsk applikasjonsprofil av CPSV (Core Public Service Vocabulary), modellert i LinkML med lenking framfor inlining. Basert på https://informasjonsforvaltning.github.io/cpsv-ap-no/

URI: https://data.norge.no/linkml/cpsv-ap-no

Name: cpsv-ap-no



## Classes







### Obligatorisk

| Class | Description |
| --- | --- |
| [Aktor](aktor.md) | Ein aktør (person eller organisasjon) relatert til ei teneste |
| [Dokumentasjonstype](dokumentasjonstype.md) | Ein type dokumentasjon som krevst for å levere ei teneste |
| [Hendelse](hendelse.md) | Ei hending som kan utløyse behov for ei offentleg teneste |
| [Katalog](katalog.md) | Ein katalog over offentlege tenester og hendingar |
| [OffentligOrganisasjon](offentligorganisasjon.md) | Ein offentleg organisasjon som er ansvarleg for ei teneste |
| [OffentligTjeneste](offentligtjeneste.md) | Ei konkret offentleg teneste levert av ein offentleg organisasjon |
| [Tjeneste](tjeneste.md) | Ei teneste levert av ein ikkje-offentleg aktør |
| [Tjenestekanal](tjenestekanal.md) | Ein kanal for å få tilgang til ei teneste (t |
| [Tjenesteresultattype](tjenesteresultattype.md) | Typen resultat som ei teneste produserer |




### Anbefalt

| Class | Description |
| --- | --- |
| [Livshendelse](livshendelse.md) | Ei livshending som kan utløyse behov for tenester (t |
| [Virksomhetshendelse](virksomhetshendelse.md) | Ei verksemdhending som kan utløyse behov for tenester (t |




### Valgfri

| Class | Description |
| --- | --- |
| [Adresse](adresse.md) | Ei postadresse knytt til ein aktør, organisasjon eller kontaktpunkt |
| [Deltagelse](deltagelse.md) | Ei rolle ein aktør har i leveringa av ei teneste |
| [Gebyr](gebyr.md) | Eit gebyr knytt til ei teneste |
| [Kontaktpunkt](kontaktpunkt.md) | Kontaktinformasjon for ei teneste eller ein organisasjon |
| [Regel](regel.md) | Eit regelverk eller retningsliner som styrer levering av ei teneste |
| [RegulativRessurs](regulativressurs.md) | Ein regulativ ressurs (lov, forskrift o |




### Andre

| Class | Description |
| --- | --- |
| [Tjenesteresultattypeliste](tjenesteresultattypeliste.md) | Ei liste over moglege tjenesteresultattypar |





## Slots

| Slot | Description |
| --- | --- |

| [adresse_ref](adresse_ref.md) | Postadresse knytt til aktøren |

| [behandlingstid](behandlingstid.md) | Forventa behandlingstid for tenesta eller kanalen (ISO 8601) |

| [deltakar](deltakar.md) | Aktøren som deltek |

| [deltek_i](deltek_i.md) | Deltakingar aktøren er del av |

| [eigd_av](eigd_av.md) | Aktør som eig eller er ansvarleg for tenesta |

| [epost](epost.md) | E-postadresse (mailto:-URI) |

| [er_beskrive_av](er_beskrive_av.md) | Datasett som beskriv ressursen |

| [er_del_av](er_del_av.md) | Tenesta er del av ei anna teneste |

| [er_gruppert_av](er_gruppert_av.md) | Hending(ar) som grupperer tenesta |

| [er_klassifisert_av](er_klassifisert_av.md) | Omgrep tenesta er klassifisert med |

| [er_spesifisert_i](er_spesifisert_i.md) | Liste eller spesifikasjon ressursen er del av |

| [folger](folger.md) | Regelverk tenesta følgjer |

| [foretrekt_namn](foretrekt_namn.md) | Føretrekt namn/term for organisasjonen |

| [full_adresse](full_adresse.md) | Full adresse som fritekst |

| [godtek_spraak](godtek_spraak.md) | Språk dokumentasjonstypen er akseptert i |

| [gyldig_i](gyldig_i.md) | Kor lenge dokumentasjonen er gyldig (ISO 8601 varigheit) |

| [har_ansvarleg_styremakt](har_ansvarleg_styremakt.md) | Offentleg organisasjon ansvarleg for tenesta |

| [har_del](har_del.md) | Deltenester som inngår i denne tenesta |

| [har_deltaking](har_deltaking.md) | Deltakarar med spesifikke roller i levering av tenesta |

| [har_dokumentasjonstype](har_dokumentasjonstype.md) | Dokumentasjon som krevst for tenesta |

| [har_gebyr](har_gebyr.md) | Gebyr knytt til tenesta |

| [har_kontaktpunkt](har_kontaktpunkt.md) | Kontaktpunkt for tenesta eller organisasjonen |

| [har_regulativ_ressurs](har_regulativ_ressurs.md) | Regulativ ressurs (lov, forskrift) knytt til tenesta |

| [har_rolle](har_rolle.md) | Rolla aktøren har i ei deltaking |

| [har_tenestekanal](har_tenestekanal.md) | Kanal for tilgang til tenesta |

| [har_tenesteresultattype](har_tenesteresultattype.md) | Typen resultat tenesta kan produsere |

| [inneheld_hending](inneheld_hending.md) | Hendingar i katalogen |

| [inneheld_teneste](inneheld_teneste.md) | Offentlege tenester i katalogen |

| [kan_skape_hending](kan_skape_hending.md) | Hending tenesteresultatet kan skape |

| [kan_utlose](kan_utlose.md) | Offentlege tenester hendinga kan utløyse |

| [kan_utlose_behov_for](kan_utlose_behov_for.md) | Tenester det kan oppstå behov for som følgje av hendinga |

| [kategori](kategori.md) | Kategori for kontaktpunktet |

| [klassifisering](klassifisering.md) | Klassifisering av dokumentasjonstypen |

| [kontaktside](kontaktside.md) | Kontaktside (nettadresse) |

| [krev](krev.md) | Teneste eller ressurs denne tenesta krev |

| [land](land.md) | Land (ISO 3166-1 alpha-2 kode) |

| [lisens](lisens.md) | Lisens for katalogen |

| [malgruppe](malgruppe.md) | Målgruppe for tenesta |

| [mogleg_spraak](mogleg_spraak.md) | Mogleg språk for tenesteresultatet |

| [nettside](nettside.md) | Nettside for tenestekanalane |

| [opningstider](opningstider.md) | Opningstider |

| [oppdateringsfrekvens](oppdateringsfrekvens.md) | Kor ofte katalogen vert oppdatert |

| [postnummer](postnummer.md) | Postnummer |

| [poststad](poststad.md) | Poststad/by |

| [relatert_teneste](relatert_teneste.md) | Relatert teneste |

| [sektor](sektor.md) | Industri/sektor tenesta tilhøyrer |

| [telefon](telefon.md) | Telefonnummer |

| [tema](tema.md) | Emne/tema tenesta handlar om |

| [temaomrade](temaomrade.md) | Tematisk område for tenesta |

| [utgjevar](utgjevar.md) | Utgjevar av katalogen |

| [utstedingsstad](utstedingsstad.md) | Stad dokumentasjonen er akseptert frå |

| [verdi](verdi.md) | Verdien av gebyret |


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
