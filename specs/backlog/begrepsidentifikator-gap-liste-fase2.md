# Gap-liste — Fase 2: begrepsidentifikator-søk mot Felles Begrepskatalog

## Bakgrunn

Fase 2 i `plan-konsekvent-begrepsidentifikator.md`: køyr `sok_begrepskatalog` sitt eksakt-namnetreff-steg (`skos:prefLabel`/`skos:altLabel` via SPARQL mot `sparql.fellesdatakatalog.digdir.no`) mot alle domenemodell-klassar som manglar `annotations.begrepsidentifikator` og har ei reell skildring, og produser ei gap-liste for Fase 3 (menneskeleg stadfesting av treff) og Fase 4 (nyregistrering for klassar utan treff).

## Metode og avgrensing

- **Berre eksakt SPARQL-namnetreff vart køyrd i bulk** (ikkje fritekstsøk-fallback). Fritekstsøket produserer støyete, upresise kandidatar utan verdi i stor skala utan menneskeleg vurdering per treff (verifisert i Prioritet 1-arbeidet: søk på `privat virksomhet` gav berre irrelevante skatterelaterte treff). Fritekstsøk kan køyrast individuelt via `sok_begrepskatalog`-verktøyet for enkeltklassar i Fase 3/4 ved behov.
- **Datakvalitetsfiks undervegs:** første køyring fann at den harvesta SPARQL-grafen òg inneheld ressursar med `skos:prefLabel` frå **andre** vokabular enn Felles Begrepskatalog (LOS-ord under `psi.norge.no/los/ord/`, interne "subjects"-taggar under `catalog-admin-service.fellesdatakatalog.digdir.no`) — 17 av 122 opphavlege treff peika feilaktig dit. `concept_search.py` sitt eksakt-søk avgrensar no eksplisitt til `concept-catalog.fellesdatakatalog.digdir.no`-namnerommet. Denne gap-lista er frå den retta køyringa.
- **Fleire kandidatar er vanleg for korte/tvetydige ord** (53 av 121 treff har meir enn éin kandidat, t.d. fleire ulike konsept kalla "klasse" frå ulike organisasjonar). Alle kandidatar er lista — **vel aldri automatisk den første**, les definisjonen mot klassen si eiga skildring.
- **326 av 463 klassar i omfang vart søkt.** Dei resterande 137 er anten alt løyste (7, sjå `plan-konsekvent-begrepsidentifikator.md` Prioritet 1) eller har ingen reell skildring å søkje etter (130 — bokstaveleg `'TODO: beskriv klassen'` eller tom `description`, hovudsakleg dei 7 `enhetsregisteret-bvr*`-skjemaa sine framleis uferdige scaffold-klassar). Desse 130 er ikkje inkluderte i gap-lista under — dei treng skildring **før** eit meiningsfullt begrepssøk er mogleg.
- Søkjeterm var klassenamnet i LinkML (PascalCase, t.d. `Kommune`), søkt som lower-case eksakt namn. Samansette scaffold-klassenamn (t.d. `VirksomhetsinformasjonHovedenhet`) gir naturleg nok sjeldan eksakt treff — det er venta, ikkje ein metodefeil.

## Resultat: 121 treff, 205 ingen treff (av 326 søkte)

| Skjema | Treff | Ingen treff | Søkte totalt |
|---|---|---|---|
| `fint-utdanning` | 3 | 63 | 66 |
| `fint-arkiv` | 17 | 22 | 39 |
| `ngr-eiendom` | 16 | 22 | 38 |
| `fint-administrasjon` | 9 | 23 | 32 |
| `ngr-person` | 12 | 20 | 32 |
| `ngr-adresse` | 14 | 6 | 20 |
| `register-over-aksjeeiere` | 8 | 10 | 18 |
| `ngr-virksomhet` | 15 | 2 | 17 |
| `fint-common` | 13 | 3 | 16 |
| `fint-ressurs` | 5 | 11 | 16 |
| `fint-okonomi` | 6 | 8 | 14 |
| `javazonetalk` | 0 | 6 | 6 |
| `fair-metadata` | 0 | 5 | 5 |
| `fint-personvern` | 2 | 3 | 5 |
| `enhetsregisteret_bvrstiftelsesdokument` | 1 | 0 | 1 |
| `samt-bu` | 0 | 1 | 1 |

## Treff — klar for Fase 3 (menneskeleg stadfesting)

**Viktig:** dette er *kandidatar*, ikkje ferdig stadfesta verdiar. Kvar kandidat sin `definisjon` må lesast mot klassen si eiga `description` før éin `uri` vert vald og skriven inn som `begrepsidentifikator` — same framgangsmåte som synte seg naudsynt i Prioritet 1 (t.d. der `fylkeskommune` var rett kandidat for `Fylke`, sjølv om namnet ikkje er identisk). Rader med fleire kandidatar krev eit medvite val, ikkje berre den første i lista.

### `fint-utdanning` (3 treff)

**`Klasse`** — Ei fast klasse av elevar ved ein skule (tidlegare kalla Basisgruppe).

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| klasse | bestanddelene i et klassifikasjonssystem | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/5d005716-7680-491b-abb6-204ee0db22d3 |
| klasse | bestanddel i et klassifikasjonssystem | https://concept-catalog.fellesdatakatalog.digdir.no/collections/961181399/concepts/42598056-b90a-41e8-bfe6-cb4d2c29027a |
| klasse | bestanddel i et klassifikasjonssystem. | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/49e6980d-5955-11e6-86bf-12156fd09fb5 |
| klasse | organisering av skoleelever på samme alder som samles i et antall og får en felles "gruppeidentit... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/964338531/concepts/3d7b34e4-37e3-4983-9d9b-c3adca56d6fa |

**`Sensor`** — Ein sensor for ein eksamen.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| sensor | sakkyndig person som vurderer kandidatens ferdigheter ved praktisk prøve, og kunnskap ved avlegge... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/971032081/concepts/acf01c5b-b1b5-4126-ab25-42dba5a2a0af |

**`Skole`** — Ein skule eller opplæringsinstitusjon.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| skole | institusjon hvor det gies undervisning i ulike fag | https://concept-catalog.fellesdatakatalog.digdir.no/collections/964338531/concepts/017cdf77-afb1-44e3-8845-08fe570e251d |

### `fint-arkiv` (17 treff)

**`Arkivdel`** — Ein vilkårleg definert del av eit arkiv.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| arkivdel | avgrenset del av arkiv der arkivmateriale er ordnet etter ett og samme ordningsprinsipp | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/49e69800-5955-11e6-86bf-12156fd09fb5 |
| arkivdel | vilkårlig definert del av et arkiv (enkeltarkiv), hvor alt materiale er ordnet etter ett og samme... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/88da091b-61f6-4877-8212-585b0b2f8580 |

**`Autorisasjon`** — Siling av kva ein innlogga brukar får lov til å gjere i løysinga.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| autorisasjon | gyldig tillatelse til å utføre visse oppgaver og/eller få tilgang til definerte ressurser | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/2367ad9e-8dcd-4d64-b9e8-e4ee8b7f6d7a |

**`Avskrivning`** — Avskriving av ein journalpost (markering som ferdigbehandla).

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| avskrivning | systematisk periodisering av anskaffelseskost for en eiendel med lang, men begrenset levetid | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/576104da-106c-4423-a0f0-ba88eec43b55 |
| avskrivning | systematisk periodisering av anskaffelseskost for en eiendel med lang, men begrenset økonomisk le... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/bad3116b-63b8-4897-bdf0-fe6bce8d75f2 |
| avskrivning | å føre krav, eller deler av et krav, ut av reskontro og regnskap fordi det ikke lenger er rettsli... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/35c63107-86e6-11e6-a97e-ba992a0501a6 |
| avskrivning | registrering av opplysninger i journalen om når og hvordan behandlingen av et inngående dokument ... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/edfda291-2fdb-4c0d-be4a-565e3e581dd5 |
| avskrivning | registrering av opplysninger i journalen om når og hvordan behandlingen av et inngående dokument ... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/961181399/concepts/a5ddfcdf-4217-4195-bd5a-b068a95f2936 |

**`DokumentType`** — Type dokument.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| dokumenttype | beskriver dokumentets art i et arkiv- og saksbehandlingssystem forhold til om det er eksternt mot... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/8ef7c438-0ef8-11e7-a910-005056821322 |
| dokumenttype | angivelsen av hvilken type dokumentinnhold som er opprettet | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/20b52b19-9fe1-11e5-a9f8-e4115b280940 |

**`Dokumentbeskrivelse`** — Skildring av eit dokument tilknytt ein journalpost.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| dokumentbeskrivelse | metadata til arkivdokument, som angir arkivdokumentets innhold | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/f325f875-e417-4ba3-a4ee-c62b51306e5c |
| dokumentbeskrivelse | metadata til arkivdokument i en arkivstruktur, angir arkivdokumentets innhold | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/df81b85a-3474-11e6-af6b-9614a8212dd3 |

**`Dokumentobjekt`** — Referanse til éin og berre éin dokumentfil.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| dokumentobjekt | metadata til dokumentfiler   | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/f3f05323-3bd5-48a2-873c-36ba5d393bf9 |
| dokumentobjekt | metadata om dokumentet, refererer til én og kun en dokumentfil som er en lagring av et dokumenti ... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/976bf450-65fb-11e6-a009-0050568351d2 |

**`Format`** — Dokumentets filformat.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| format | angivelse av versjon for tolkning av dokumentinnholdet og tilleggsinformasjon | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/20b52b1b-9fe1-11e5-a9f8-e4115b280940 |

**`Journalpost`** — Ein journalpost (inn- eller utgåande dokument, notat o.l.) i ei saksmappe.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| journalpost | enkelt registrering i en journal, det vil si opplysningene om et saksdokument med eventuelle vedlegg | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/b2daa1f6-cc16-414a-ae4a-6e781cf4a8ed |
| journalpost | registrering (innførsel) i en journal, dvs. opplysningene om et saksdokument med eventuelle vedle... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/8ef7c44e-0ef8-11e7-a910-005056821322 |
| journalpost | enkeltregistrering i en journal | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/df81b860-3474-11e6-af6b-9614a8212dd3 |
| journalpost | en enkelt registrering i en journal | https://concept-catalog.fellesdatakatalog.digdir.no/collections/961181399/concepts/f1213019-c6cc-4581-bcd9-dd931ca34138 |

**`JournalpostType`** — Navn på type journalpost.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| journalposttype | typen av journalpost (inngående,utgående,internt uten oppfølging,intern med oppfølging eller unde... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/df81b865-3474-11e6-af6b-9614a8212dd3 |

**`Klasse`** — Ein klasse i eit klassifikasjonssystem.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| klasse | bestanddelene i et klassifikasjonssystem | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/5d005716-7680-491b-abb6-204ee0db22d3 |
| klasse | bestanddel i et klassifikasjonssystem | https://concept-catalog.fellesdatakatalog.digdir.no/collections/961181399/concepts/42598056-b90a-41e8-bfe6-cb4d2c29027a |
| klasse | bestanddel i et klassifikasjonssystem. | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/49e6980d-5955-11e6-86bf-12156fd09fb5 |
| klasse | organisering av skoleelever på samme alder som samles i et antall og får en felles "gruppeidentit... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/964338531/concepts/3d7b34e4-37e3-4983-9d9b-c3adca56d6fa |

**`Klassifikasjonssystem`** — Overordna struktur for mappene i ein eller fleire arkivdelar.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| klassifikasjonssystem | klasser som beskriver arkivskapers funksjoner, aktiviteter, emner eller objekter  | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/2c05b870-cd34-4cd7-b7ed-75b463d0fccd |
| klassifikasjonssystem | kontrollmekanisme for dokumentasjon, som brukes til å knytte saker og dokumenter til deres opphav... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/8ef7c453-0ef8-11e7-a910-005056821322 |
| klassifikasjonssystem | system bestående av klasser som beskriver arkivskapers funksjoner og aktiviteter | https://concept-catalog.fellesdatakatalog.digdir.no/collections/961181399/concepts/35b21126-c2ae-474c-9665-a3dc1288ab31 |
| klassifikasjonssystem | system for organisering av klasser i en arkivdel | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/49e6980e-5955-11e6-86bf-12156fd09fb5 |

**`Korrespondansepart`** — Verksemd eller person som arkivskapar mottek eller sender arkivdokument til.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| korrespondansepart | virksomhet eller person som arkivskaper mottar eller sender arkivdokumenter til | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/a9afa87a-d181-49bf-aa09-9a46f25a3c68 |
| korrespondansepart | virksomhet eller person som arkivskaper mottar eller sender arkivdokumenter til | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/df81b868-3474-11e6-af6b-9614a8212dd3 |

**`Merknad`** — Merknad knytt til mappe, registrering eller dokumentbeskrivelse.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| merknad | forklaring til innholdet i melding eller spesifikasjonslinje | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/c38de2c0-145a-11eb-8086-0050568351d2 |
| merknad | tilleggsopplysning, fotnote. I arkiv: dokumenterer spesielle forhold rundt saksgang eller dokumenter | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/df81b86e-3474-11e6-af6b-9614a8212dd3 |

**`Part`** — Part til Mappe, Registrering eller Dokumentbeskrivelse.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| Part | en person eller et foretak som er involvert i en sak, og som ikke er en aktør (advokat, sakkyndig... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/984195796/concepts/aa13b14b-87e9-46bb-92f7-52f632f323da |
| part | person som en avgjørelse retter seg mot eller som saken ellers direkte gjelder | https://concept-catalog.fellesdatakatalog.digdir.no/collections/970205039/concepts/2579e786-177a-4ecc-a0d4-249a9dde87dc |
| part | rettssubjekter som har eller kan få rettigheter eller plikter innenfor Skatteetatens virkeområde,... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/20b52adb-9fe1-11e5-a9f8-e4115b280940 |

**`Rolle`** — Rolla til ein arkivressurs.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| rolle | karakteristikk for klassifikator basert på en assosiasjonsende | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/20b2e2bf-9fe1-11e5-a9f8-e4115b280940 |
| rolle | vanlige eller forventede funksjonen en aktør har, eller den funksjonen noe eller noen utgjør i en... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/964338531/concepts/4ffe3aa5-452f-4c91-b25c-9e7e3ecc178a |

**`Sak`** — Generisk saksmappe (konkret Sak i Noark).

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| sak | dokumentasjon skapt som ledd i utførelsen av en enkeltstående oppgave eller arbeidsprosess | https://concept-catalog.fellesdatakatalog.digdir.no/collections/961181399/concepts/3eb46a60-3d7d-4471-a7b3-e8fd1ad2e01d |

**`Skjerming`** — Skjerming av mappe, registrering eller dokument etter offentleglova.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| skjerming | handling eller løsning for å gjøre registrerte opplysninger eller enkeltdokumenter utilgjengelige... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/afdb4e0b-0171-4f1d-956a-2f20ee283bb7 |

### `ngr-eiendom` (16 treff)

**`Borettslag`** — Eit burettslag er ein type hovudeining (juridisk person) som eig burettslagsbygningen. Burettslagsandelar tilhøyrer eit burettslag.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| borettslag | samvirkeforetak som har til formål å gi andelseierne bruksrett til boenhet i foretakets eiendom (... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/20b2e17d-9fe1-11e5-a9f8-e4115b280940 |

**`Bruksenhet`** — Ei brukseining (leilegheit, kontor o.l.) innanfor ein bygning. Har eit bruksenheitsnummer, ligg i minst éi etasje og kan vere knytt til ei matrikkelenheit.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| bruksenhet | bygning eller del av bygning (lokale), f.eks. bolig, kontorenhet, verksted og lager, dvs. et rom ... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/971040238/concepts/9acc8b93-ae2f-4464-9a45-7e691d7dd19a |
| bruksenhet | samling av bygninger, rom, lokaler, anlegg, og eventuelle tilleggsdeler som sammen anvendes i en ... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/20b2e16f-9fe1-11e5-a9f8-e4115b280940 |

**`Bruksenhetsnummer`** — Identifikator for ei brukseining innanfor ein bygning, t.d. H0201 = 2. etasje, eining 1 (etasjeplan + etasjenummer + nummerering).

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| bruksenhetsnummer | en bokstav og fire siffer som entydig identifiserer den enkelte bruksenheten innenfor en adresser... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/20b2e101-9fe1-11e5-a9f8-e4115b280940 |
| bruksenhetsnummer | en bokstav og fire siffer som entydig identifiserer den enkelte bruksenheten innenfor en adresser... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/72e6316e-e671-4ad2-81b5-468a27bb1580 |
| bruksenhetsnummer | En bokstav og fire siffer som entydig identifiserer den enkelte bruksenheten innenfor en adresser... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/971040238/concepts/b19e31e0-3b1a-4cf1-9f56-25ce1afac64a |

**`Bruksnummer`** — Bruksnummer innanfor gardsnavnet.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| bruksnummer | del av matrikkelnummeret til en fast eiendom (matrikkelenhet). En eiendom identifiseres med kommu... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/971040238/concepts/b35111d1-cad4-4b66-acf8-c32c72f8033c |
| bruksnummer | en del av matrikkelnummeret til en fast eiendom, og er fortløpende nummerering innenfor gårdsnumm... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/20b2e102-9fe1-11e5-a9f8-e4115b280940 |

**`Bygning`** — Ein bygning registrert i Matrikkelen. Knytt til éi matrikkelenheit og kan ha fleire ytre innganger, brukseiningar og etasjar. Bygningsinformasjon er i dag sp...

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| bygning | konstruksjon som kan anvendes separat, er oppført for et permanent formål, og er egnet eller bere... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/9c33fd03-2964-11e6-b2bc-96405985e0fa |
| bygning | adresseegenskap som beskriver navn og/eller nummer på bygning | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/20b2e306-9fe1-11e5-a9f8-e4115b280940 |
| bygning | frittstående fast konstruksjon som har som en av sine hovedfunksjoner å gi beskyttelse for de som... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/964338531/concepts/6682f81b-214a-4075-b31e-c5910441402e |

**`Eierseksjon`** — Ein eigarseksjon er ein eigarandel i ein seksjonert eigedom. Eigaren har einerett til å bruke ein bestemt del av eigedommen, medan heile eigedommen er i same...

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| eierseksjon | en leilighet der eieren har enerett til å bruke selve leiligheten mens hele eiendommen (bygning o... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/20b2e172-9fe1-11e5-a9f8-e4115b280940 |

**`Festenummer`** — Festenummer, aktuelt berre for festegrunn (0..1 i matrikkelnummeret).

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| festenummer | del av matrikkelnummeret som identifiserer festegrunn (tomt). Tas i bruk når et bruksnummer skal ... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/20b2e10a-9fe1-11e5-a9f8-e4115b280940 |
| festenummer | del av matrikkelnummeret til en fast eiendom (matrikkelenhet). En eiendom identifiseres med kommu... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/971040238/concepts/ed1f2327-c39e-4365-86f3-831ecc96583b |

**`Hovedenhet`** — Ei hovudeining i Einingsregisteret. Juridisk person som kan ha undereiningar. Tilhøyrer Domene virksomhet.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| hovedenhet | virksomhet på øverste nivå i registreringsstrukturen i Enhetsregisteret | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/b934718f-2d49-4ca2-81f4-317df5141524 |

**`Kommune`** — Norsk kommune. Tilhøyrer Domene nasjonal inndelingsbase og forvaltast av Nasjonal inndelingsbase.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| kommune | område som utgjør en egen politisk og administrativ enhet underlagt staten, men med et visst selv... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/20b2e0f1-9fe1-11e5-a9f8-e4115b280940 |

**`Kommunenummer`** — Firesifra kommunenummer (t.d. 0301 for Oslo).

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| kommunenummer | nummerering av kommuner i henhold til Statistisk sentralbyrå sin offisielle liste | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/9d683a9e-1e65-4ac1-843d-2c473b56735e |
| kommunenummer | et nummer som identifiserer en kommune eller et kommunelignende område | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/20b2e0f3-9fe1-11e5-a9f8-e4115b280940 |
| kommunenummer | firesifret kode som entydig identifiserer en kommune | https://concept-catalog.fellesdatakatalog.digdir.no/collections/971526920/concepts/399c275c-764c-402b-b49c-ae95392bd6fc |

**`Matrikkelnummer`** — Offisiell identifikator for ei matrikkelenheit, beståande av kommunenummer, gards-, bruks- og eventuelt feste- og seksjonsnummer.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| matrikkelnummer | entydig identifisering av matrikkelenhet innen kommune, definert i matrikkelforskrift § 7e | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/20b2e115-9fe1-11e5-a9f8-e4115b280940 |
| matrikkelnummer | den offisielle nemninga for kvar enkelt matrikkeleining | https://concept-catalog.fellesdatakatalog.digdir.no/collections/971040238/concepts/ae049afc-dd7e-436b-8bff-b3ab5f0ec986 |
| matrikkelnummer | unikt nummer som identifiserer en fast eiendom i Norge | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/03c54c71-fca0-4536-a169-df82b9bdee2d |

**`OffisiellAdresse`** — Offisiell adresse tildelt av kommunen. Tilhøyrer Domene adresse og forvaltast av Matrikkelen via NGR-adresse.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| offisiellAdresse | den fullstendige adressen for en bygning, bygningsdel, bruksenhet, eiendom eller et annet objekt ... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/971040238/concepts/0be32f31-fed4-4b07-ac1d-1892c86e8aa9 |

**`Person`** — Ein fysisk person. Tilhøyrer Domene person.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| person | objekt som er et menneske | https://concept-catalog.fellesdatakatalog.digdir.no/collections/971032081/concepts/aa223af4-b183-4f30-9a1e-ccb668a4ce9a |
| person | objekt som er et menneske | https://concept-catalog.fellesdatakatalog.digdir.no/collections/971527404/concepts/6c1197a7-5c17-48f6-b399-a031d66cd8da |
| person | objekt som er et menneske | https://concept-catalog.fellesdatakatalog.digdir.no/collections/964338531/concepts/27834a63-e3ee-48c2-98b3-45e77d93e1dd |

**`Representasjonspunkt`** — Geografisk punkt (koordinatpar) som representerer posisjonen til bygningen.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| representasjonspunkt | et geografisk punkt angitt ved hjelp av rettvinklede koordinat-par (nord/øst) basert på en geodet... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/971040238/concepts/da56081e-d08e-4c2c-859a-aa1ebb31d738 |

**`Rettighetshaver`** — Den som har ein rett knytt til ein eigedom. Kan vere ein fysisk person eller ei hovudeining (juridisk person).

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| rettighetshaver | den som har en rettighet i henhold til en etablert rettsstiftelse | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/b2835498-be80-493e-b0f1-bb1d8e10fed6 |

**`Seksjonsnummer`** — Seksjonsnummer, aktuelt berre for eigarseksjonar (0..1 i matrikkelnummeret).

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| seksjonsnummer | fortløpende nummerering av seksjoner under gårdsnummer/bruksnummer og eventuelt festenummer | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/20b2e124-9fe1-11e5-a9f8-e4115b280940 |
| seksjonsnummer | del av matrikkelnummeret til en fast eiendom (matrikkelenhet). En eiendom identifiseres med kommu... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/971040238/concepts/0289aa6a-9dc6-4a31-b283-5871ab0ed02c |

### `fint-administrasjon` (9 treff)

**`Aktivitet`** — Del av kontostrengen og detaljering av funksjon.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| aktivitet | beskrivelse av hva virksomheten driver med | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/f20e8bda-39cc-4d88-832f-594d0b82b61c |
| aktivitet | minste identifiserte enhet av arbeid i en prosess | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/5e20d183-07df-11e7-9a7f-005056821322 |

**`Anlegg`** — Del av kontostrengen; objekt som skal aktiverast eller avskrivast.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| anlegg | enkelt utstyr, et sett med utstyr, settet med utstyr i en installasjon, eller alt utstyr nødvendi... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/970205039/concepts/6468ab93-1e88-4b38-a94f-c1c9fb31789c |

**`Arbeidsforhold`** — Eit avtaleforhold mellom personalressurs og arbeidsgjevar.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| arbeidsforhold | avtaleforhold hvor den ene part (arbeidstakeren) forplikter seg til å utføre arbeid for den annen... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/dcfb46ef-e484-11e6-9cb3-005056821322 |

**`Arbeidsforholdstype`** — Viser kva behov hos arbeidsgjevar arbeidsforholdet dekkjer.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| arbeidsforholdstype | hovedkategorisering av arbeidsforhold basert på hvor arbeidet utføres, hvilken selvstendighet arb... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/dcfb46f2-e484-11e6-9cb3-005056821322 |

**`Fullmakt`** — Fullmakt til å gjere handlingar i høve til ei gjeven Rolle.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| fullmakt | en tillatelse som innebærer at en fysisk person har myndighet til å opptre og handle på vegne av ... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/6409df32-cc4e-46da-9e09-89b952526d45 |
| fullmakt | formell tillatelse som innebærer at en person (fullmektigen) har myndighet til å opptre og handle... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/5138da0a-be20-11e6-8004-005056825ca0 |

**`Funksjon`** — Del av kontostrengen som beskriv kva som vert produsert.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| funksjon | et ansvarsområde som en virksomhet forvalter for å oppnå bestemte mål, og som består av en gruppe... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/961181399/concepts/5181097f-090c-4dcb-bc50-b4f83e40adab |
| Funksjon | Rollen som ansvarlig søker, ansvarlig prosjekterende, ansvarlig utførende eller ansvarlig kontrol... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760223/concepts/9e2b7184-237c-4de2-8d79-0a20360678c4 |

**`Kontrakt`** — Kontrakt transaksjonen er knytt til.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| kontrakt | avtale mellom en tjenestekonsument og en tjenestetilbyder som etablererer funksjonelle og ikke-fu... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/964338531/concepts/9f5c9628-bb8d-4372-9bc8-01f2e8bb00af |

**`Prosjekt`** — Del av kontostrengen som peikar på løpande prosjekt.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| Prosjekt | Ein midlertidig organisasjon etablert med den hensikt å levere eit eller fleire produkt som grunn... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/917641404/concepts/3b3bae8a-5639-4547-8b4a-76c21ed907a0 |
| prosjekt | et enkelt endringsprosjekt som leverer forretningsverdi til organisasjonen | https://concept-catalog.fellesdatakatalog.digdir.no/collections/964338531/concepts/827af65d-4f2c-41ca-89ed-90e571082054 |

**`Rolle`** — Rettighet eller type fullmakt.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| rolle | karakteristikk for klassifikator basert på en assosiasjonsende | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/20b2e2bf-9fe1-11e5-a9f8-e4115b280940 |
| rolle | vanlige eller forventede funksjonen en aktør har, eller den funksjonen noe eller noen utgjør i en... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/964338531/concepts/4ffe3aa5-452f-4c91-b25c-9e7e3ecc178a |

### `ngr-person` (12 treff)

**`Adressebeskyttelse`** — Gradering av adressebeskyttelse for innflyttede personar til Noreg. Tidlegare kalla kode 6 (strengt fortroleg) og kode 7 (fortroleg).

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| adressebeskyttelse | beskyttelse av en persons adresseinformasjon i folkeregisteret | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/92f82e52-fb04-11e9-92b0-005056828ed3 |

**`Bostedsadresse`** — Adressa personen er registrert busett på i Folkeregisteret.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| bostedsadresse | adresse hvor en person er registrert bosatt i Folkeregisteret | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/5138d9e3-be20-11e6-8004-005056825ca0 |
| bostedsadresse | adressen hvor en person bor, ifølge Folkeregisteret | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/efa2ce12-8c83-4848-91fb-a56e300a2187 |

**`Identifikasjonsdokument`** — Utanlandsk identifikasjonsdokument som pass, førekort eller nasjonalt ID-kort knytt til ein person.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| identifikasjonsdokument | dokument med opplysninger om en persons identitet sammen med annen informasjon (som biometriske k... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/5138da1a-be20-11e6-8004-005056825ca0 |

**`Identitetsgrunnlag`** — Grunnlaget som er brukt for å fastsetje identiteten til ein person ved registrering i Folkeregisteret.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| identitetsgrunnlag | opplysninger som danner grunnlaget for,  og tiltroen til, den identiteten som er registrert i Fol... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/5138da15-be20-11e6-8004-005056825ca0 |

**`Oppholdsadresse`** — Adressa der personen faktisk oppheld seg (ikkje nødvendigvis bustadsadressa).

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| oppholdsadresse | en annen adresse enn bostedsadresse der personen faktisk oppholder seg | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/df78aa35-2c12-11e7-959c-005056825ca0 |

**`Person`** — Ein fysisk person registrert i Folkeregisteret. Hovudbegrepet i domene person.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| person | objekt som er et menneske | https://concept-catalog.fellesdatakatalog.digdir.no/collections/971032081/concepts/aa223af4-b183-4f30-9a1e-ccb668a4ce9a |
| person | objekt som er et menneske | https://concept-catalog.fellesdatakatalog.digdir.no/collections/971527404/concepts/6c1197a7-5c17-48f6-b399-a031d66cd8da |
| person | objekt som er et menneske | https://concept-catalog.fellesdatakatalog.digdir.no/collections/964338531/concepts/27834a63-e3ee-48c2-98b3-45e77d93e1dd |

**`Personnavn`** — Offisielt registrert navn på ein person i Folkeregisteret.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| personnavn | navn på person som består av fornavn og ett enkelt eller dobbelt etternavn og kan i tillegg bestå... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/88804c45-ff43-11e6-9d97-005056825ca0 |

**`Personstatus`** — Status for ein person i Folkeregisteret (t.d. bosatt, utflyttet, død).

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| personstatus | kode for en persons status i forhold til dennes tilknytning til Norge og Folkeregisteret | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/92f82e46-fb04-11e9-92b0-005056828ed3 |

**`Postadresse`** — Adressa der personen mottar post.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| postadresse | geografisk adresse der post ønskes levert | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/c2112eda-f1e7-4a9b-af65-70d74643d705 |
| postadresse | adresse der person ønsker at post skal leveres | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/88804c49-ff43-11e6-9d97-005056825ca0 |

**`Sivilstand`** — Sivilstand registrert på ein person i Folkeregisteret.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| sivilstand | myndighetenes kategorisering av en persons stilling i nære parforhold til en annen levende eller ... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/88804c58-ff43-11e6-9d97-005056825ca0 |

**`Statsborgerskap`** — Statsborgerskap registrert på ein person i Folkeregisteret.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| statsborgerskap | en persons forhold til et land som innebærer at man har visse rettigheter og plikter som følger a... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/88804c5a-ff43-11e6-9d97-005056825ca0 |
| statsborgerskap | det rettslige båndet mellom en person og en stat som består av både plikter og rettigheter | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/5882e3bb-8646-46c1-9eb4-e6c435a7c6ed |
| statsborgerskap | rettslig bånd mellom en person og en stat som består av både plikter og rettigheter, og som er er... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760746/concepts/d106e0a9-b865-4746-bd2d-89974f709e23 |

**`Verge`** — Ein verje (anten person eller institusjon) som er oppnemnd for å ivareta interessene til ein person. Er av type Person.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| verge | en person som ivaretar en annen person sine personlige og/eller økonomiske interesser | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/32b2c492-15ac-47a1-8eca-2ee310da8a95 |
| verge | person som varetar umyndiges interesser og opptrer som rettslig representant på umyndiges vegne i... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/be5d8b8c-c3fb-11e9-8d53-005056825ca0 |

### `ngr-adresse` (14 treff)

**`Adressekode`** — Firesifra kommunal kode som identifiserer eit adressenavn.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| adressekode | Entydig numerisk identifikasjon innenfor kommunen for gater, veger, stier, plasser og områder som... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/971040238/concepts/e58fc49e-2261-4ef7-9f84-315086dfb10e |
| adressekode | nummer som entydig identifiserer adresserbare gater, veger, stier, plasser og områder  som er før... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/20b2e0f8-9fe1-11e5-a9f8-e4115b280940 |

**`Adressenavn`** — Offisielt navn på ei veglenke eller eit adresseobjekt i ein kommune, tildelt av kommunen og godkjent av Kartverket.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| adressenavn | navn på gate, veg, sti, plass eller område [...] | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/fb46ed39-8772-4347-9cba-9be3040464c0 |
| adressenavn | navn på gate, veg, sti, plass eller område, brukt som del av den offisielle adressen | https://concept-catalog.fellesdatakatalog.digdir.no/collections/971040238/concepts/52c28953-af85-477f-b612-a10e76f977c4 |
| adressenavn | navn på gate, veg, sti, plass eller område, brukt som del av den offisielle adressen | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/20b2e0f9-9fe1-11e5-a9f8-e4115b280940 |

**`Bruksenhet`** — Referanse til ei brukseining (leilegheit/lokale) i Matrikkelen.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| bruksenhet | bygning eller del av bygning (lokale), f.eks. bolig, kontorenhet, verksted og lager, dvs. et rom ... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/971040238/concepts/9acc8b93-ae2f-4464-9a45-7e691d7dd19a |
| bruksenhet | samling av bygninger, rom, lokaler, anlegg, og eventuelle tilleggsdeler som sammen anvendes i en ... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/20b2e16f-9fe1-11e5-a9f8-e4115b280940 |

**`Bruksenhetsnummer`** — Identifikator for ei brukseining (leilegheit o.l.) innanfor ein bygning, t.d. H0201 = 2. etasje, eining 1.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| bruksenhetsnummer | en bokstav og fire siffer som entydig identifiserer den enkelte bruksenheten innenfor en adresser... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/20b2e101-9fe1-11e5-a9f8-e4115b280940 |
| bruksenhetsnummer | en bokstav og fire siffer som entydig identifiserer den enkelte bruksenheten innenfor en adresser... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/72e6316e-e671-4ad2-81b5-468a27bb1580 |
| bruksenhetsnummer | En bokstav og fire siffer som entydig identifiserer den enkelte bruksenheten innenfor en adresser... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/971040238/concepts/b19e31e0-3b1a-4cf1-9f56-25ce1afac64a |

**`Bygning`** — Referanse til ein bygning i Matrikkelen. Offisiell adresse kan adressere ytre inngang(ar) til bygningen.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| bygning | konstruksjon som kan anvendes separat, er oppført for et permanent formål, og er egnet eller bere... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/9c33fd03-2964-11e6-b2bc-96405985e0fa |
| bygning | adresseegenskap som beskriver navn og/eller nummer på bygning | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/20b2e306-9fe1-11e5-a9f8-e4115b280940 |
| bygning | frittstående fast konstruksjon som har som en av sine hovedfunksjoner å gi beskyttelse for de som... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/964338531/concepts/6682f81b-214a-4075-b31e-c5910441402e |

**`Grunnkrets`** — Ei grunnkrets - minste geografiske eining i statistisk inndeling.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| grunnkrets | et lite og geografisk sammenhengende område som er mest mulig ensartet når det gjelder natur og n... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/108097cc-25fc-11e9-85c0-005056821322 |

**`Husnummer`** — Husnummer beståande av eit obligatorisk nummer og ein valfri bokstav (t.d. 12 eller 12B).

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| husnummer | nummer som entydig identifiserer eiendommer, anlegg, bygninger eller innganger til bygninger inne... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/20b2e111-9fe1-11e5-a9f8-e4115b280940 |

**`Kommune`** — Ein norsk kommune.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| kommune | område som utgjør en egen politisk og administrativ enhet underlagt staten, men med et visst selv... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/20b2e0f1-9fe1-11e5-a9f8-e4115b280940 |

**`OffisiellAdresse`** — Ei offisiell adresse tildelt av kommunen, beståande av vegadresse (adressenavn + husnummer) eller matrikkelnummer. Forvaltas av Matrikkelen.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| offisiellAdresse | den fullstendige adressen for en bygning, bygningsdel, bruksenhet, eiendom eller et annet objekt ... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/971040238/concepts/0be32f31-fed4-4b07-ac1d-1892c86e8aa9 |

**`Postboks`** — Ei postboks registrert i Postboksregisteret.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| postboks | identifikator på postboks som består av landets betegnelse for postboks samt den alfanumeriske id... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/20b2e308-9fe1-11e5-a9f8-e4115b280940 |

**`Postboksadresse`** — Ei postboksadresse registrert i Postboksregisteret (Posten Norge).

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| postboksadresse | adresse for å nå noen eller noe levert til en postboks | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/19b53b7f-b47a-4dce-8f70-9452ce8c037e |
| postboksadresse | Adresse for å sende noe til en postboks | https://concept-catalog.fellesdatakatalog.digdir.no/collections/971040238/concepts/fdcb929f-cb81-46d6-b419-b6ac520ed065 |
| postboksadresse | postadresse til en postboks | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/20b2e11c-9fe1-11e5-a9f8-e4115b280940 |

**`Poststed`** — Eit poststed identifisert med postnummer, forvalta av Postnummerregisteret.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| poststed | geografisk inndeling av postmottakere | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/e994f3e6-8fc4-4dd3-894f-7d5af313c0b0 |
| poststed | Kombinasjon av postnummer og poststedsnavn | https://concept-catalog.fellesdatakatalog.digdir.no/collections/971040238/concepts/4141472d-e770-4e4a-a85e-d12d9eb05a43 |
| poststed | et geografisk område med felles postnummer | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/20b2e122-9fe1-11e5-a9f8-e4115b280940 |

**`Representasjonspunkt`** — Eit geografisk punkt (koordinatpar) som representerer posisjonen til adressa.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| representasjonspunkt | et geografisk punkt angitt ved hjelp av rettvinklede koordinat-par (nord/øst) basert på en geodet... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/971040238/concepts/da56081e-d08e-4c2c-859a-aa1ebb31d738 |

**`Stemmekrets`** — Ei stemmekrets brukt ved val.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| stemmekrets | del av en geografisk inndeling av kommunen som er bestemt av valgstyret | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/92f82e4c-fb04-11e9-92b0-005056828ed3 |

### `register-over-aksjeeiere` (8 treff)

**`Aksje`** — Ei enkelt aksje utstedt av eit aksjeselskap.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| aksje | eierandel i selskap som har aksjekapital | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/ccc14d51-73f6-40d8-a9f4-1cc04653a560 |

**`Aksjeeier`** — Person eller organisasjon som eig aksjar.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| aksjeeier | eier av andel i boligselskap | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/20b2e177-9fe1-11e5-a9f8-e4115b280940 |

**`Aksjeinnskudd`** — Innskot knytt til aksjar i samband med selskapshending.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| aksjeinnskudd | det beløpet som betales for hver aksje ved aksjetegning | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/b5d97ef7-60ef-4471-b2b8-ff39a32c9b6f |

**`Aksjekapital`** — Den registrerte aksjekapitalen i eit aksjeselskap.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| aksjekapital | ansvarskapitalen i et aksjeselskap, allmennaksjeselskap eller europeisk selskap | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/627b9de7-9ae4-45e0-8b1d-c2f8cbf1f93c |

**`Aksjeklasse`** — Klasse aksjar høyrer til, med eigne rettigheiter.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| aksjeklasse | Gruppe av aksjer der selskapets vedtekter særskilt regulerer disse aksjenes rettigheter. | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/1e333067-6837-11e6-a7ce-fac03dffe1d7 |

**`Aksjeselskap`** — Selskap som utsteder aksjar og har aksjekapital.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| aksjeselskap | selskap hvor eierskapet er fordelt gjennom aksjer og hvor ingen av aksjonærene har personlig ansv... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/d67e2d32-6dcf-11e6-be2b-ba992a0501a6 |
| aksjeselskap | selskap med begrenset ansvar, der eierandelene er fordelt på aksjer | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/25e4979d-6f6d-4f79-affe-2554e5aef699 |

**`Selskapshendelse`** — Hending som påverkar selskapet sitt eigarskap eller kapital.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| selskapshendelse | en kapitalendring eller utbytteutdeling i selskapet. | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/1e3330b0-6837-11e6-a7ce-fac03dffe1d7 |

**`Utbytte`** — Utbytte knytt til ein eigarposisjon.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| utbytte | enhver utdeling som innebærer en vederlagsfri overføring av verdier fra selskap til aksjonær | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/698a22a4-cb67-11e7-a210-0050568204d6 |

### `ngr-virksomhet` (15 treff)

**`Aktivitet`** — Skildring av kva aktivitet ei hovudeining utøver. Svarer til formålsparagrafen eller føremålet til verksemda.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| aktivitet | beskrivelse av hva virksomheten driver med | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/f20e8bda-39cc-4d88-832f-594d0b82b61c |
| aktivitet | minste identifiserte enhet av arbeid i en prosess | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/5e20d183-07df-11e7-9a7f-005056821322 |

**`Beliggenhetsadresse`** — Beliggenheitsadressa til underleininga - den fysiske adressa der aktiviteten vert utøvd.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| beliggenhetsadresse | geografisk adresse der virksomhetens aktivitet foregår | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/3df8eeef-e44a-41f6-9251-ad083fcb34fa |

**`Forretningsadresse`** — Forretningsadressa til hovudeininga - adressa der hovudkontoret held til.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| forretningsadresse | geografisk adresse hvor hovedkontoret til virksomheten ligger | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/92b95731-13f2-4c86-ab83-f00fed2ee36f |

**`Hovedenhet`** — Ei hovudeining er den juridiske eininga registrert i Enhetsregisteret (t.d. AS, ENK, BA). Kan ha undereiningar og rolleinnehavarar.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| hovedenhet | virksomhet på øverste nivå i registreringsstrukturen i Enhetsregisteret | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/b934718f-2d49-4ca2-81f4-317df5141524 |

**`Kontaktinformasjon`** — Kontaktinformasjon for verksemda registrert i Enhetsregisteret.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| kontaktinformasjon | informasjon som en avsender trenger for å kommunisere med en mottaker  | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/796f9881-572a-4b53-ab6b-7b4229502326 |
| kontaktinformasjon | informasjon som kan brukes for uformell kontakt med parten | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/20b52ad9-9fe1-11e5-a9f8-e4115b280940 |
| kontaktinformasjon | informasjon som kan benyttes for å komme i kontakt med noen | https://concept-catalog.fellesdatakatalog.digdir.no/collections/991825827/concepts/94328aca-770b-4502-95e5-94e44cb6d62f |
| kontaktinformasjon | kontaktinformasjon hos den ansvarlige tilsynsmyndigheten, som registreres knyttet til et tilsyn  | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/61da079b-2e6e-427a-a5d6-4b5ffa7ee51e |

**`Organisasjonsform`** — Klassifikasjon av juridisk organisasjonsform (t.d. AS, ENK, BA, NUF). Kodeverk forvalta av Enhetsregisteret.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| organisasjonsform | inndeling av virksomheter i forskjellige typer ut fra egenskaper disse har til felles    | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/59c07423-a89f-4916-90ec-83746862dc24 |

**`Person`** — Ein fysisk person. Tilhøyrer Domene person og forvaltast av Folkeregisteret. Enhetsregisteret nyttar kopi av data frå Folkeregisteret.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| person | objekt som er et menneske | https://concept-catalog.fellesdatakatalog.digdir.no/collections/971032081/concepts/aa223af4-b183-4f30-9a1e-ccb668a4ce9a |
| person | objekt som er et menneske | https://concept-catalog.fellesdatakatalog.digdir.no/collections/971527404/concepts/6c1197a7-5c17-48f6-b399-a031d66cd8da |
| person | objekt som er et menneske | https://concept-catalog.fellesdatakatalog.digdir.no/collections/964338531/concepts/27834a63-e3ee-48c2-98b3-45e77d93e1dd |

**`Postadresse`** — Postadressa verksemda mottar post på.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| postadresse | geografisk adresse der post ønskes levert | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/c2112eda-f1e7-4a9b-af65-70d74643d705 |
| postadresse | adresse der person ønsker at post skal leveres | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/88804c49-ff43-11e6-9d97-005056825ca0 |

**`Prokura`** — Prokura gjev ein person fullmakt til å handle på vegne av verksemda i næringssaker. Verksemda kan ha fleire prokuraistar.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| prokura | begrenset fullmakt til å inngå avtaler på vegne av virksomheten i alt som hører til driften av denne | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/9c684df1-0a51-4e87-86ba-68553cad275a |

**`Rolleinnehaver`** — Den som innehar ein rolle i ei verksemd. Kan vere ein fysisk person (frå Folkeregisteret) eller ei anna eining.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| rolleinnehaver | fysisk eller juridisk person som er registrert med en funksjon for en virksomhet | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/254bf7ae-1d0a-4994-b20b-575d4e28e674 |

**`Sektorkode`** — Institusjonell sektorkode som klassifiserer kva sektor verksemda tilhøyrer (t.d. offentleg, privat).

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| sektorkode | fire- eller femsifrede sektorkoder som skal benyttes ved innrapportering av tredjepartsopplysning... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/20b2e32d-9fe1-11e5-a9f8-e4115b280940 |

**`Signaturrett`** — Bestemmelse om kven som har rett til å signere på vegne av verksemda (t.d. "Styret i fellesskap" eller "Dagleg leiar aleine").

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| signaturrett | ubegrenset fullmakt til å inngå avtaler på vegne av virksomheten | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/e072caae-797c-47bf-8793-85209c921e7f |

**`Tilstand`** — Registrert tilstand (status) for ei verksemd i Enhetsregisteret, med gyldigheitsperiode for historisk sporing.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| tilstand | status et gitt informasjonselement har ift prosessen knyttet til egenfastsetting vs myndighetsfas... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/46f4d77e-4c6c-11e8-bb3e-005056821322 |

**`Underenhet`** — Ei underleining er ein geografisk lokasjon der aktiviteten til ei hovudeining vert utøvd. Knyt seg til ei hovudeining via organisasjonsnummeret.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| underenhet | virksomhet på laveste nivå i registreringsstrukturen i Enhetsregisteret | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/22b3ce34-867a-4ac9-879b-e4e53a6e8f12 |

**`Varslingsadresse`** — Offisiell varslingsadresse for verksemda - e-post eller mobilnummer som vert brukt for offisielle meldingar frå offentlege styresmakter.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| varslingsadresse | elektronisk adresse som brukes for å varsle virksomhet eller person | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/e65d1c73-5b62-47c9-be38-01afd1a8d7b0 |

### `fint-common` (13 treff)

**`Adresse`** — Fysisk adresse eller postadresse.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| adresse | noe avsender bruker for å nå mottaker | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/25033a3e-b1f5-47d0-887b-4cca54f02dc4 |
| adresse | noe avsender bruker for å nå mottaker | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/20b2e0f5-9fe1-11e5-a9f8-e4115b280940 |
| adresse | tegn som blir brukt for å finne fram til eller stedfeste et objekt | https://concept-catalog.fellesdatakatalog.digdir.no/collections/971527404/concepts/fea0e9f2-3b62-4c6b-9df3-27dd2f7cd530 |
| adresse | tegn som blir brukt for å finne fram til, eller stedfeste et objekt  | https://concept-catalog.fellesdatakatalog.digdir.no/collections/964338531/concepts/7e0e47e9-e675-4582-8aac-15791d0db90e |
| adresse | tekst for ustrukturert adresse innen et poststed | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/20b2e0fb-9fe1-11e5-a9f8-e4115b280940 |

**`Elev`** — Ein elev registrert i skulesystemet.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| elev | person som mottar undervisning, veiledning eller lignende, særlig i skole eller hos lærer eller f... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/964338531/concepts/e6bfeb15-5a47-4e68-83cd-03b0710f89d6 |

**`Identifikator`** — Unik identifikasjon til eit objekt.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| identifikator | noe som representerer identiteten | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/20b2e2f8-9fe1-11e5-a9f8-e4115b280940 |
| identifikator | tegn som på en entydig måte identifiserer et objekt innenfor et sett av objekter | https://concept-catalog.fellesdatakatalog.digdir.no/collections/971527404/concepts/f34cf23b-abfc-4413-8d46-afd175e1c872 |
| identifikator | unikt nummer som identifiserer opplysningspliktig, virksomhet eller inntektsmottaker. Kan være no... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/e6c4c0e0-2405-11e7-8e60-0050568351d2 |

**`Kommune`** — Liste over Norges kommunar.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| kommune | område som utgjør en egen politisk og administrativ enhet underlagt staten, men med et visst selv... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/20b2e0f1-9fe1-11e5-a9f8-e4115b280940 |

**`Kontaktinformasjon`** — Informasjon som kan brukast for å oppnå kontakt.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| kontaktinformasjon | informasjon som en avsender trenger for å kommunisere med en mottaker  | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/796f9881-572a-4b53-ab6b-7b4229502326 |
| kontaktinformasjon | informasjon som kan brukes for uformell kontakt med parten | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/20b52ad9-9fe1-11e5-a9f8-e4115b280940 |
| kontaktinformasjon | informasjon som kan benyttes for å komme i kontakt med noen | https://concept-catalog.fellesdatakatalog.digdir.no/collections/991825827/concepts/94328aca-770b-4502-95e5-94e44cb6d62f |
| kontaktinformasjon | kontaktinformasjon hos den ansvarlige tilsynsmyndigheten, som registreres knyttet til et tilsyn  | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/61da079b-2e6e-427a-a5d6-4b5ffa7ee51e |

**`Kontaktperson`** — Kontaktperson (pårørande) til ein person.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| kontaktperson | fysisk person som representerer en virksomhet | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/de386aeb-ea96-4be6-a99c-f16b5a7583c0 |

**`Landkode`** — Landskode i ISO 3166-1 alpha-2 format.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| landkode | kode for å representere navn på et land eller en underinndeling av et land | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/20b2e112-9fe1-11e5-a9f8-e4115b280940 |

**`Matrikkelnummer`** — Eintydleg identifisering av matrikkeleining innanfor kommune.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| matrikkelnummer | entydig identifisering av matrikkelenhet innen kommune, definert i matrikkelforskrift § 7e | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/20b2e115-9fe1-11e5-a9f8-e4115b280940 |
| matrikkelnummer | den offisielle nemninga for kvar enkelt matrikkeleining | https://concept-catalog.fellesdatakatalog.digdir.no/collections/971040238/concepts/ae049afc-dd7e-436b-8bff-b3ab5f0ec986 |
| matrikkelnummer | unikt nummer som identifiserer en fast eiendom i Norge | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/03c54c71-fca0-4536-a169-df82b9bdee2d |

**`Periode`** — Tidsperiode med obligatorisk start og valfri slutt.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| periode | tiden mellom to tidspunkt | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/20b52b6d-9fe1-11e5-a9f8-e4115b280940 |

**`Person`** — Fysiske private personar.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| person | objekt som er et menneske | https://concept-catalog.fellesdatakatalog.digdir.no/collections/971032081/concepts/aa223af4-b183-4f30-9a1e-ccb668a4ce9a |
| person | objekt som er et menneske | https://concept-catalog.fellesdatakatalog.digdir.no/collections/971527404/concepts/6c1197a7-5c17-48f6-b399-a031d66cd8da |
| person | objekt som er et menneske | https://concept-catalog.fellesdatakatalog.digdir.no/collections/964338531/concepts/27834a63-e3ee-48c2-98b3-45e77d93e1dd |

**`Personnavn`** — Navn på ein person.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| personnavn | navn på person som består av fornavn og ett enkelt eller dobbelt etternavn og kan i tillegg bestå... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/88804c45-ff43-11e6-9d97-005056825ca0 |

**`Valuta`** — Valutakodar for offisielle valutaer.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| valuta | enhet eller benevning på et betalingsmiddel for ett eller flere land | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/9c63765b-74e0-4bbb-8a80-33a7a5fd89c8 |

**`Virksomhet`** — Ein juridisk organisasjon som produserer varer eller tenester.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| virksomhet | aktør som har et formål og opptrer som en enhet | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/c5fee487-68ab-4281-968d-2bc2dac7c336 |
| virksomhet | en bestemt inntektsgivende aktivitet som tar sikte på å ha en viss varighet, har et visst omfang,... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/20b2e1aa-9fe1-11e5-a9f8-e4115b280940 |
| virksomhet | med begrepet Organisasjon mener vi organisasjon, virksomhet, foretak, enhet og juridisk person | https://concept-catalog.fellesdatakatalog.digdir.no/collections/971032081/concepts/9fe89f1a-a266-49a0-a526-7a4629255912 |

### `fint-ressurs` (5 treff)

**`Applikasjon`** — Ein applikasjon med tilhøyrande ressursar.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| applikasjon | kjørbar programvare som tilbyr funksjonalitet som understøtter definerte behov i en eller flere a... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/964338531/concepts/fc078b7e-3e33-447a-9c46-9bf44b7acd43 |

**`Enhetstype`** — Type digital eining.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| enhetstype | klasse av objekt man er interessert i | https://concept-catalog.fellesdatakatalog.digdir.no/collections/971526920/concepts/5ea970ad-d899-4308-b86a-fd00048cdc72 |

**`Plattform`** — Plattforma tenesta kan leverast på.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| plattform | kombinasjon av teknologiske infrastrukturprodukter og -komponenter som kan utgjøre kjøremiljø for... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/964338531/concepts/2e0fa7c7-cd61-47a6-b4e9-a9c655246292 |

**`Rettighet`** — Ei navngitt rettighet.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| rettighet | rettsvirkning som har positiv konsekvens for en aktør | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760746/concepts/7ba07c16-c5a7-4559-ab5c-ed193e5dd444 |

**`Status`** — Status på ei digital eining i fagsystemet.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| status | status som angir hvorvidt tilsynet er under planlegging, eller åpent og da fortsatt pågår, eller ... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/3b020269-db85-4838-9afb-d53b33640996 |

### `fint-okonomi` (6 treff)

**`Bilag`** — Dokumentasjon til ein transaksjon (kompleks datatype).

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| bilag | noe som er lagt ved | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/d0db1980-1a4b-11e9-a7bb-0050568351d2 |

**`Fakturagrunnlag`** — Grunnlag for fakturering.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| fakturagrunnlag | all dokumentasjon som inngår i grunnlaget for å fakturere | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/566ff3ec-679b-49e8-80c3-2da9bc49b58e |

**`Fakturamottaker`** — Aktør som skal betale faktura (kompleks datatype).

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| fakturamottaker | den fakturaen er adressert til | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/9a74a32f-d3ac-4d80-84ba-0a31162b1825 |

**`Merverdiavgift`** — Kodeverk for merverdiavgifter.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| merverdiavgift | avgift til staten som skal beregnes ved omsetning, uttak og innførsel av varer og tjenester | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/38e2a356-4758-11e6-b166-8e8050d1fd96 |

**`Transaksjon`** — Overføring av pengar til eller frå eksterne partar.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| transaksjon | interaksjon mellom en bruker og en datamaskin hvor brukeren gir en kommando for å oppnå et spesif... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/964338531/concepts/c4f8467a-e3d8-4f99-bd90-98e0420d9605 |
| transaksjon | angir forholdet kunden har til en vare og kan ha verdiene 1) kjøpe i fast regning, 2) konsignasjo... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/54f7f1d2-af50-11e8-89d2-005056821322 |

**`Vare`** — Vare eller teneste som kan leverast og fakturerast.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| vare | eiendel med økonomisk verdi anskaffet eller tilvirket med sikte på salg i foretakets inntektsgive... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/fcb13b89-d8a7-ea4e-8b0d-211db8ec7dbe |

### `fint-personvern` (2 treff)

**`Samtykke`** — Tillating til behandling av personopplysning.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| samtykke | en frivillig, uttrykkelig og informert erklæring fra den registrerte om at han eller hun godtar b... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/88804c57-ff43-11e6-9d97-005056825ca0 |

**`Tjeneste`** — Teneste eller system som behandlar personopplysningar.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| tjeneste | avgrenset sett av aktiviteter som utføres av eller på vegne av en virksomhet for en aktør | https://concept-catalog.fellesdatakatalog.digdir.no/collections/991825827/concepts/e51d808c-f6f9-45f6-939f-b36b446760ba |
| tjeneste | utgangsfaktor fra en organisasjon der minst en aktivitet nødvndighvis utføres mellom organisasjon... | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/5e20d18d-07df-11e7-9a7f-005056821322 |
| tjeneste | ikke-fysisk ytelse som omsettes | https://concept-catalog.fellesdatakatalog.digdir.no/collections/974761076/concepts/20b2e162-9fe1-11e5-a9f8-e4115b280940 |

### `enhetsregisteret_bvrstiftelsesdokument` (1 treff)

**`Person`** — Definisjon: menneske slik det opptrer i en sosial sammenheng.

| Kandidat-term | Kandidat-definisjon | URI |
|---|---|---|
| person | objekt som er et menneske | https://concept-catalog.fellesdatakatalog.digdir.no/collections/971032081/concepts/aa223af4-b183-4f30-9a1e-ccb668a4ce9a |
| person | objekt som er et menneske | https://concept-catalog.fellesdatakatalog.digdir.no/collections/971527404/concepts/6c1197a7-5c17-48f6-b399-a031d66cd8da |
| person | objekt som er et menneske | https://concept-catalog.fellesdatakatalog.digdir.no/collections/964338531/concepts/27834a63-e3ee-48c2-98b3-45e77d93e1dd |

## Ingen treff — kandidatar for Fase 4 (nyregistrering)

Ingen eksakt namnetreff funne i Felles Begrepskatalog. Dette tyder **ikkje** automatisk at konseptet ikkje finst — berre at klassenamnet ikkje matchar noko `skos:prefLabel`/`skos:altLabel` presist der. Eit fritekstsøk (via `sok_begrepskatalog`) eller manuelt søk på `data.norge.no/concepts` kan framleis finne eit treff for enkeltklassar — sjå metode-avsnittet over for kvifor dette ikkje vart gjort i bulk.

**`fint-utdanning`** (63): `Anmerkninger`, `Arstrinn`, `Avbruddsaarsak`, `AvlagtProve`, `Betalingsstatus`, `Bevistype`, `Brevtype`, `Eksamen`, `Eksamensform`, `Eksamensgruppe`, `Eksamensgruppemedlemskap`, `Eksamensvurdering`, `Elevforhold`, `Elevfravar`, `Elevkategori`, `Elevtilrettelegging`, `Elevvurdering`, `Fag`, `Faggruppe`, `Faggruppemedlemskap`, `Fagmerknad`, `Fagstatus`, `Fravarsoversikt`, `Fravarsprosent`, `Fravartype`, `Fraversregistrering`, `Fullfortkode`, `Halvaarsfagvurdering`, `Halvaarsordensvurdering`, `Karakterhistorie`, `Karakterskala`, `Karakterstatus`, `Karakterverdi`, `Klassemedlemskap`, `Kontaktlaerergruppe`, `Kontaktlaerergruppemedlemskap`, `Laerling`, `OtEnhet`, `OtStatus`, `OtUngdom`, `Persongruppe`, `Persongruppemedlemskap`, `Programomrade`, `Programomrademedlemskap`, `Provestatus`, `Rom`, `Skoleaar`, `Skoleeiertype`, `Skoleressurs`, `Sluttfagvurdering`, `Sluttordensvurdering`, `Termin`, `Tilrettelegging`, `Time`, `Underveisfagvurdering`, `Underveisordensvurdering`, `Undervisningsforhold`, `Undervisningsgruppe`, `Undervisningsgruppemedlemskap`, `Utdanningsprogram`, `Varsel`, `Varseltype`, `Vitnemalsmerknad`

**`fint-arkiv`** (22): `AdministrativEnhet`, `Arkivressurs`, `DispensasjonAutomatiskFredaKulturminne`, `DokumentStatus`, `Dokumentfil`, `JournalStatus`, `Klassifikasjonstype`, `KorrespondansepartType`, `Merknadstype`, `PartRolle`, `Personalmappe`, `Saksmappetype`, `Saksstatus`, `Skjermingshjemmel`, `SoeknadDrosjeloeyve`, `Tilgang`, `Tilgangsgruppe`, `Tilgangsrestriksjon`, `TilknyttetRegistreringSom`, `TilskuddFartoy`, `TilskuddFredaBygningPrivatEie`, `Variantformat`

**`ngr-eiendom`** (22): `Andel`, `Anleggseiendom`, `Anleggsprojeksjonsflate`, `AnnenMatrikkelenhet`, `Borettslagsandel`, `Bygningsnummer`, `Etasje`, `FastEiendom`, `Festegrunn`, `Gaardsnummer`, `Grunneiendom`, `HjemmelTilEiendomsrett`, `HjemmelTilFesterett`, `HjemmelTilFramfesterett`, `IkkeTinglystEierforhold`, `Jordsameie`, `RettighetForAaBenytteEiendom`, `SamletFastEiendom`, `Teig`, `TinglystEierforhold`, `TinglystHeftelse`, `YtreInngang`

**`fint-administrasjon`** (23): `Ansvar`, `Arbeidslokasjon`, `Art`, `Diverse`, `Fastlonn`, `Fasttillegg`, `Formaal`, `Fravaer`, `Fravaersgrunn`, `Fravaerstype`, `Kontostreng`, `Lonsart`, `Lopenummer`, `Objekt`, `Organisasjonselement`, `Organisasjonstype`, `Personalressurs`, `Personalressurskategori`, `Prosjektart`, `Ramme`, `Stillingskode`, `Uketimetall`, `Variabellonn`

**`ngr-person`** (20): `DNummer`, `Dodsfall`, `FalskIdentitet`, `FamilierelasjonBarn`, `FamilierelasjonEktefelle`, `FamilierelasjonForelder`, `Foedsel`, `Foedselsnummer`, `ForeldreansvarBarn`, `ForeldreansvarForelder`, `InnflyttingTilNorge`, `Kjoenn`, `KontaktinformasjonDoedsbo`, `Kontaktopplysninger`, `Opphold`, `Personidentifikasjon`, `ReservasjonMotKommunikasjonPaaNett`, `RettsligHandleevne`, `SpraakForElektroniskKommunikasjon`, `UtflyttingFraNorge`

**`ngr-adresse`** (6): `Adresseomrade`, `Fylke`, `Kirkesokn`, `KommunalKrets`, `Svalbard`, `Tettsted`

**`register-over-aksjeeiere`** (10): `Aksjeeierrettighet`, `Aksjeoverdragelse`, `Aksjepost`, `Eierposisjon`, `Eierskapstransaksjon`, `InnbetaltAksjekapital`, `InnbetaltOverkurs`, `Tidspunkt`, `Utdeling`, `Vederlag`

**`ngr-virksomhet`** (2): `Naeringskode`, `RolleIVirksomhet`

**`fint-common`** (3): `Fylke`, `Kjonn`, `Spraak`

**`fint-ressurs`** (11): `Applikasjonskategori`, `Applikasjonsressurs`, `Applikasjonsressurstilgjengelighet`, `Brukertype`, `DigitalEnhet`, `Enhetsgruppe`, `Enhetsgruppemedlemskap`, `Handhevingstype`, `Identitet`, `Lisensmodell`, `Produsent`

**`fint-okonomi`** (8): `Faktura`, `Fakturalinje`, `Fakturautsteder`, `Kontostreng`, `Leverandor`, `Leverandorgruppe`, `OkonomiValuta`, `Postering`

**`javazonetalk`** (6): `Foredrag`, `Foredragsholder`, `Konferanse`, `Sesjon`, `Sesjonslokale`, `Timeplan`

**`fair-metadata`** (5): `FAIRMetadata`, `Gjenbruksmetadata`, `Katalogregistrering`, `Proveniensmetadata`, `Tilgangsmetadata`

**`fint-personvern`** (3): `Behandling`, `Behandlingsgrunnlag`, `Personopplysning`

**`samt-bu`** (1): `PrivatVirksomhet`

## Ikkje søkt — manglar reell skildring (130 klassar)

Desse klassane (hovudsakleg dei 7 `enhetsregisteret-bvr*`-scaffold-skjemaa) har `description: 'TODO: beskriv klassen'` eller tom skildring. Eit begrepssøk utan reell skildring å stadfeste mot ville vore urimeleg upresist — dei må først få ei ordentleg skildring (separat, ikkje-triviell arbeidsoppgåve for kvart skjema sin fagansvarlege) før søk gir meining. Sjå `specs/backlog/plan-konsekvent-begrepsidentifikator.md` for full kartlegging av kva skjema dette gjeld.

## Neste steg

1. **Fase 3:** gå gjennom dei 121 treffa over, vel/avvis kandidat(-ar) mot klassen si eiga skildring, skriv stadfesta `begrepsidentifikator`-verdiar inn i skjemaa.
2. **Fase 4:** for dei 205 utan treff (og eventuelt fleire etter individuelt fritekstsøk): vurder nyregistrering hjå rett organisasjon.
3. Skriv skildringar for dei 130 `TODO`-klassane, køyr så søket på nytt for dei.

## Utført

Fase 2 gjennomført 2026-08-28. Batch-søk (326 klassar, eksakt SPARQL-namnetreff, ~0,6s mellom kvart kall, 0 nettverksfeil) via `concept_search.py` sin `_exact_label_match()`, køyrd direkte (utan MCP-container) for å handtere volumet effektivt. Ein datakvalitetsfeil (namnetreff frå andre vokabular enn Felles Begrepskatalog) vart oppdaga og retta i `concept_search.py` undervegs, og søket vart køyrd på nytt. Råresultat lagra i sesjonen sin scratchpad (`begrep-lookup-output.json`), oppsummert til denne gap-lista.
