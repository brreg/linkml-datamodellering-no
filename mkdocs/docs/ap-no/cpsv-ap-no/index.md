# cpsv-ap-no



Norsk applikasjonsprofil av CPSV (Core Public Service Vocabulary), modellert i LinkML med lenking framfor inlining. Basert på https://informasjonsforvaltning.github.io/cpsv-ap-no/

URI: https://data.norge.no/linkml/cpsv-ap-no

Name: cpsv-ap-no



## Classes







### Obligatorisk

| Class | Description |
| --- | --- |
| [Aktor](klasser/aktor.md) | Ein aktør (person eller organisasjon) relatert til ei teneste |
| [Dokumentasjonstype](klasser/dokumentasjonstype.md) | Ein type dokumentasjon som krevst for å levere ei teneste |
| [Hendelse](klasser/hendelse.md) | Ei hending som kan utløyse behov for ei offentleg teneste |
| [Katalog](klasser/katalog.md) | Ein katalog over offentlege tenester og hendingar |
| [OffentligOrganisasjon](klasser/offentligorganisasjon.md) | Ein offentleg organisasjon som er ansvarleg for ei teneste |
| [OffentligTjeneste](klasser/offentligtjeneste.md) | Ei konkret offentleg teneste levert av ein offentleg organisasjon |
| [Tjeneste](klasser/tjeneste.md) | Ei teneste levert av ein ikkje-offentleg aktør |
| [Tjenestekanal](klasser/tjenestekanal.md) | Ein kanal for å få tilgang til ei teneste (t |
| [Tjenesteresultattype](klasser/tjenesteresultattype.md) | Typen resultat som ei teneste produserer |




### Anbefalt

| Class | Description |
| --- | --- |
| [Livshendelse](klasser/livshendelse.md) | Ei livshending som kan utløyse behov for tenester (t |
| [Virksomhetshendelse](klasser/virksomhetshendelse.md) | Ei verksemdhending som kan utløyse behov for tenester (t |




### Valgfri

| Class | Description |
| --- | --- |
| [Adresse](klasser/adresse.md) | Ei postadresse knytt til ein aktør, organisasjon eller kontaktpunkt |
| [Deltagelse](klasser/deltagelse.md) | Ei rolle ein aktør har i leveringa av ei teneste |
| [Gebyr](klasser/gebyr.md) | Eit gebyr knytt til ei teneste |
| [Kontaktpunkt](klasser/kontaktpunkt.md) | Kontaktinformasjon for ei teneste eller ein organisasjon |
| [Regel](klasser/regel.md) | Eit regelverk eller retningsliner som styrer levering av ei teneste |
| [RegulativRessurs](klasser/regulativressurs.md) | Ein regulativ ressurs (lov, forskrift o |




### Andre

| Class | Description |
| --- | --- |
| [Tjenesteresultattypeliste](klasser/tjenesteresultattypeliste.md) | Ei liste over moglege tjenesteresultattypar |





## Slots

| Slot | Description |
| --- | --- |

| [adresse_ref](klasser/adresse_ref.md) | Postadresse knytt til aktøren |

| [behandlingstid](klasser/behandlingstid.md) | Forventa behandlingstid for tenesta eller kanalen (ISO 8601) |

| [deltakar](klasser/deltakar.md) | Aktøren som deltek |

| [deltek_i](klasser/deltek_i.md) | Deltakingar aktøren er del av |

| [eigd_av](klasser/eigd_av.md) | Aktør som eig eller er ansvarleg for tenesta |

| [epost](klasser/epost.md) | E-postadresse (mailto:-URI) |

| [er_beskrive_av](klasser/er_beskrive_av.md) | Datasett som beskriv ressursen |

| [er_del_av](klasser/er_del_av.md) | Tenesta er del av ei anna teneste |

| [er_gruppert_av](klasser/er_gruppert_av.md) | Hending(ar) som grupperer tenesta |

| [er_klassifisert_av](klasser/er_klassifisert_av.md) | Omgrep tenesta er klassifisert med |

| [er_spesifisert_i](klasser/er_spesifisert_i.md) | Liste eller spesifikasjon ressursen er del av |

| [folger](klasser/folger.md) | Regelverk tenesta følgjer |

| [foretrekt_namn](klasser/foretrekt_namn.md) | Føretrekt namn/term for organisasjonen |

| [full_adresse](klasser/full_adresse.md) | Full adresse som fritekst |

| [godtek_spraak](klasser/godtek_spraak.md) | Språk dokumentasjonstypen er akseptert i |

| [gyldig_i](klasser/gyldig_i.md) | Kor lenge dokumentasjonen er gyldig (ISO 8601 varigheit) |

| [har_ansvarleg_styremakt](klasser/har_ansvarleg_styremakt.md) | Offentleg organisasjon ansvarleg for tenesta |

| [har_del](klasser/har_del.md) | Deltenester som inngår i denne tenesta |

| [har_deltaking](klasser/har_deltaking.md) | Deltakarar med spesifikke roller i levering av tenesta |

| [har_dokumentasjonstype](klasser/har_dokumentasjonstype.md) | Dokumentasjon som krevst for tenesta |

| [har_gebyr](klasser/har_gebyr.md) | Gebyr knytt til tenesta |

| [har_kontaktpunkt](klasser/har_kontaktpunkt.md) | Kontaktpunkt for tenesta eller organisasjonen |

| [har_regulativ_ressurs](klasser/har_regulativ_ressurs.md) | Regulativ ressurs (lov, forskrift) knytt til tenesta |

| [har_rolle](klasser/har_rolle.md) | Rolla aktøren har i ei deltaking |

| [har_tenestekanal](klasser/har_tenestekanal.md) | Kanal for tilgang til tenesta |

| [har_tenesteresultattype](klasser/har_tenesteresultattype.md) | Typen resultat tenesta kan produsere |

| [inneheld_hending](klasser/inneheld_hending.md) | Hendingar i katalogen |

| [inneheld_teneste](klasser/inneheld_teneste.md) | Offentlege tenester i katalogen |

| [kan_skape_hending](klasser/kan_skape_hending.md) | Hending tenesteresultatet kan skape |

| [kan_utlose](klasser/kan_utlose.md) | Offentlege tenester hendinga kan utløyse |

| [kan_utlose_behov_for](klasser/kan_utlose_behov_for.md) | Tenester det kan oppstå behov for som følgje av hendinga |

| [kategori](klasser/kategori.md) | Kategori for kontaktpunktet |

| [klassifisering](klasser/klassifisering.md) | Klassifisering av dokumentasjonstypen |

| [kontaktside](klasser/kontaktside.md) | Kontaktside (nettadresse) |

| [krev](klasser/krev.md) | Teneste eller ressurs denne tenesta krev |

| [land](klasser/land.md) | Land (ISO 3166-1 alpha-2 kode) |

| [lisens](klasser/lisens.md) | Lisens for katalogen |

| [malgruppe](klasser/malgruppe.md) | Målgruppe for tenesta |

| [mogleg_spraak](klasser/mogleg_spraak.md) | Mogleg språk for tenesteresultatet |

| [nettside](klasser/nettside.md) | Nettside for tenestekanalane |

| [opningstider](klasser/opningstider.md) | Opningstider |

| [oppdateringsfrekvens](klasser/oppdateringsfrekvens.md) | Kor ofte katalogen vert oppdatert |

| [postnummer](klasser/postnummer.md) | Postnummer |

| [poststad](klasser/poststad.md) | Poststad/by |

| [relatert_teneste](klasser/relatert_teneste.md) | Relatert teneste |

| [sektor](klasser/sektor.md) | Industri/sektor tenesta tilhøyrer |

| [telefon](klasser/telefon.md) | Telefonnummer |

| [tema](klasser/tema.md) | Emne/tema tenesta handlar om |

| [temaomrade](klasser/temaomrade.md) | Tematisk område for tenesta |

| [utgjevar](klasser/utgjevar.md) | Utgjevar av katalogen |

| [utstedingsstad](klasser/utstedingsstad.md) | Stad dokumentasjonen er akseptert frå |

| [verdi](klasser/verdi.md) | Verdien av gebyret |


## Enumerations

| Enumeration | Description |
| --- | --- |


## Types

| Type | Description |
| --- | --- |


## Subsets

| Subset | Description |
| --- | --- |
| [Anbefalt](klasser/anbefalt.md) | Anbefalte eigenskapar i ein AP-NO-profil |
| [Obligatorisk](klasser/obligatorisk.md) | Obligatoriske eigenskapar i ein AP-NO-profil |
| [Valgfri](klasser/valgfri.md) | Valfrie eigenskapar i ein AP-NO-profil |


## Generated artifacts

| Artefakt | Fil |
|----------|-----|
| SHACL shapes | [cpsv-ap-no-shapes.ttl](cpsv-ap-no-shapes.ttl) |
| OWL ontologi | [cpsv-ap-no-ontology.ttl](cpsv-ap-no-ontology.ttl) |
| Protobuf-skjema | [cpsv-ap-no-schema.proto](cpsv-ap-no-schema.proto) |
| PlantUML-diagram | [cpsv-ap-no.svg](diagrams/cpsv-ap-no.svg) · [cpsv-ap-no.puml](diagrams/cpsv-ap-no.puml) |
