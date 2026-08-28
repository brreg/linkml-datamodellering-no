# Undersøking: brukar nokon skjema class_uri frå andre modellar/ontologiar?

## Bakgrunn

Brukaren stilte spørsmål ved om `class_uri` — som dei forsto som «URI-en til
den lokale klassen» — kan ha blitt feilaktig sett til ein URI som eigentleg
høyrer til ein annan LinkML-modell eller ontologi. Oppgåva var å undersøkje
alle LinkML-skjema i repoet og skrive funna til `/specs`.

## Presisering av kva `class_uri` faktisk er

`class_uri` i LinkML er **ikkje** meint å alltid vere ein lokal, sjølv-eigd
URI. Feltet sitt føremål er å seie *«denne lokale klassen er semantisk
ekvivalent med denne RDF-klassen»* — og den RDF-klassen er i dei aller
fleste tilfelle definert av ein **ekstern, publisert standard**
(W3C DCAT/DCT/FOAF/SKOS/VCard, EU-vokabular, ModelDCAT-AP-NO, DQV-AP-NO,
XKOS-AP-NO, CPSV-AP-NO, FINT sin API-spesifikasjon, o.l.). Dette er
eksplisitt repo-konvensjon, ikkje eit avvik:

> «Alle klasser og slots har eksplisitt `class_uri` / `slot_uri` som mapper
> til de korrekte RDF-vokabularene (`dcat:`, `dct:`, `foaf:`, `vcard:` osv.)»
> — `.claude/rules/linkml-schema.md`

Spørsmålet denne undersøkinga faktisk svarar på er difor meir presist:
**har nokon klasse fått ein `class_uri` som stille peikar inn i eit anna,
*ueigna* lokalt skjema sin eigen URI-namnerom** (dvs. ei reell feilkobling
til ein urelatert intern modell, ikkje ei tilsikta mapping til ein ekte,
delt ekstern standard)?

## Metode

Alle 43 `*-schema.yaml`-filer vart parsa med PyYAML. For kvart skjema vart
`id:`/`default_prefix:` registrert som «eigd namnerom». For kvar av dei 630
klassane i repoet vart `class_uri` løyst til full URI via skjemaet sin eigen
`prefixes:`-blokk, og kryssjekka mot alle andre skjema sine eigde namnerom.

Fire separate sjekkar vart gjort:

1. **Kryssdomene-treff**: løyser ein klasse sin `class_uri` seg til eit anna
   skjema sitt eige `id`/`default_prefix`-namnerom, på tvers av ulike
   toppnivådomene (`ap-no/`, `ngr/`, `oreg/`, `fint/`, `modellkatalog/` osv.)?
2. **Same-domene-treff**: same sjekk, men innanfor éin domenefamilie (der
   delt vokabular er forventa, t.d. FINT-familien).
3. **Udeklarerte prefiks**: brukar nokon `class_uri` eit prefiks som ikkje
   finst i skjemaet sin eigen `prefixes:`-blokk (typisk teikn på skrivefeil)?
4. **Manglande `class_uri`**: kva klassar manglar `class_uri` heilt, og er
   dei eventuelt unnatekne (`tree_root`/`abstract`/`mixin`)?

## Funn

### 1 — Kryssdomene-treff: **0**

Ingen klasse i noko skjema har ein `class_uri` som løyser seg til eit anna,
urelatert lokalt skjema sitt eige namnerom. Repoet har **ikkje** noko
tilfelle av at t.d. ein NGR-klasse ved eit uhell fekk `class_uri` frå eit
FINT- eller oreg-skjema, eller omvendt.

### 2 — Same-domene-treff: 181, alle legitime

181 klassar (alle i `fint-administrasjon`, `fint-arkiv`, `fint-okonomi`,
`fint-personvern`, `fint-ressurs`, `fint-utdanning`) har `class_uri` som
løyser seg inn under `fint-common-schema.yaml` sitt eige `id`
(`https://schema.fintlabs.no`). Dette er **korrekt, ikkje ein feil**: alle
FINT-skjema implementerer ulike delar av éin ekte, delt, ekstern
spesifikasjon (FINT sitt API-namnerom `schema.fintlabs.no`), som
`fint-common` tilfeldigvis også sjølv er modellert under. Mønsteret er
identisk med korleis AP-NO-profilane deler `dcat:`/`dct:`/`dcatno:` — fleire
lokale skjema implementerer legitimt éin felles, ekstern vokabular.

Ingen andre same-domene-treff vart funne (0 utanfor FINT-familien).

### 3 — Udeklarerte prefiks: **0**

Alle `class_uri`-prefiks som er brukt, finst deklarert i vedkomande skjema
sin eigen `prefixes:`-blokk. Ingen skrivefeil funne.

### 4 — Manglande `class_uri`: 49 klassar, 19 ikkje unnatekne

581 av 630 klassar (92 %) har `class_uri`. Av dei 49 utan:
- 30 er `tree_root`/`abstract`/`mixin` — korrekt unnateke kravet
  (jf. `.claude/rules/linkml-schema.md`: containerklassar treng ikkje
  `class_uri`).
- **19 er ikkje unnatekne, og manglar difor `class_uri` utan grunngjeving:**
  18 av dei i `register-over-aksjeeiere-schema.yaml` (`Aksjeselskap`,
  `Aksjekapital`, `Aksje`, `Aksjeklasse`, `Aksjeeierrettighet`, `Aksjeeier`,
  `Eierposisjon`, `Aksjepost`, `Utbytte`, `Utdeling`, `Tidspunkt`,
  `Eierskapstransaksjon`, `Aksjeoverdragelse`, `Vederlag`,
  `Selskapshendelse`, `Aksjeinnskudd`, `InnbetaltAksjekapital`,
  `InnbetaltOverkurs`), og éin i `samt-bu-schema.yaml` (`Kontaktlaerer`).
  Dette er ei anna type gap enn det brukaren spurde om (manglande, ikkje
  feilaktig `class_uri`) — nemnt her fordi det dukka opp i same
  gjennomgang, men ikkje undersøkt vidare eller retta.

## Konklusjon

**Brukaren sin bekymring stadfestast ikkje**: ingen skjema i repoet har
brukt ein `class_uri` som peikar inn i eit anna, urelatert lokalt
LinkML-skjema sitt eige namnerom. All bruk av eksterne/delte
vokabular-prefiks (`dcat:`, `dcatno:`, `dqv:`, FINT-prefiksa, osv.) er
tilsikta, korrekt mapping til publiserte, delte standardar — ikkje
feilkoblingar. Repoet følgjer sin eigen dokumenterte konvensjon konsekvent.

Det einaste beslekta, kjende avviket er frå før (gap 3 i
`standardetterleving.md`): `Representasjonspunkt` i `ngr-adresse-schema.yaml`
brukar sitt eige lokale `ngr:`-prefiks der ein betre, ekstern
geometri-vokabular (`locn:`/`geo:`) burde vore brukt — dette er ein annan
type avvik (eigd fallback-prefiks brukt der ein betre standard fanst), ikkje
ei feilkobling til ein urelatert modell.

## Ikkje gjort

- Vidare undersøking av om ekstern-vokabular-mappingane (`dcatno:`, `dqv:`
  osv.) faktisk er *korrekte* semantiske val (dvs. om klassen verkeleg
  tilsvarar den eksterne termen) — denne undersøkinga sjekka berre om
  `class_uri` peikar inn i eit **anna urelatert lokalt skjema**, ikkje om
  kvar enkelt ekstern mapping er fagleg presis.

## Utført

Undersøking fullført 2026-08-28. Alle 43 skjema, 630 klassar gjennomgått
programmatisk (PyYAML-parsing + namneromsoppslag). Hovudspørsmålet
(feilkoblingar til andre lokale modellar) hadde eit negativt (reassurerande)
resultat — ingen kodeendring naudsynt der.

**Tilleggsoppdrag (etter brukarønske):** dei 19 manglande `class_uri`-verdiane
vart retta:

- `register-over-aksjeeiere-schema.yaml`: 18 klassar fekk
  `class_uri: aksje:<Klassenavn>`, ved å ta i bruk det alt deklarerte, men
  til då ubrukte, lokale `aksje:`-prefikset (`https://data.norge.no/oreg/register-over-aksjeeiere/`)
  — same fallback-mønster som `enhetsregisteret_bvrinn:`, `ngr:` m.fl. brukar
  når ingen ekstern standardklasse passar.
- `samt-bu-schema.yaml`: `Kontaktlaerer` fekk `class_uri: samtbuskole:Kontaktlaerer`,
  konsistent med syskenklassane `Elev`/`Rektor` (same `is_a: Person`,
  same `samtbuskole:`-namnerom).

**Validering:** `make lint` — ingen nye åtvaringar utover eksisterande
"manglar description"-åtvaringar på containerattributt (uendra av desse
endringane). `make roundtrip` for `register-over-aksjeeiere` — OK (JSON + TTL).
`make roundtrip` for `samt-bu` — `roundtrip-ttl` feilar med
«No pred for https://data.norge.no/samt/samt-bu/id», men dette er **BUG-3**
(`bugs/mappingerror-rdflib-roundtrip.md`, `status: open`), verifisert
pre-eksisterande og uavhengig av denne endringa (reproduserer identisk med
`git stash` på `samt-bu-schema.yaml` — feilen gjeld `SamtBuContainer` sin
`id`-slot, ikkje `Kontaktlaerer`). `make validate-instance` mot
`samt-bu-eksempel.yaml` — «No issues found».

---

## Fase 2 — kryssjekk mot LinkML-dokumentasjon og ny konvensjonsregel

Brukaren følgde opp med å samanlikne funna mot den offisielle LinkML-
dokumentasjonen (`https://linkml.io/linkml/intro/overview.html` →
`schemas/uris-and-mappings.html` → metamodell-kjelda
`linkml-model/meta.yaml`).

**Stadfesta:**
- Metamodell-definisjonen av `class_uri`: «The URI may come from any
  namespace and may be shared between schemas» — lokalt prefiks er teknisk
  gyldig, ingen restriksjon i spesifikasjonen.
- Men: LinkML sitt einaste eksplisitte `class_uri`-døme i dokumentasjonen
  peikar eksternt (`class_uri: schema:Person`). Det finst ikkje noko
  dokumentert døme på eksplisitt lokalt `class_uri`.
- Nøkkelmekanismen: «If class and slot uris are omitted, then they are
  still generated behind the scenes, using the `default_prefix` slot» —
  LinkML genererer sjølv ein lokal URI automatisk når `class_uri` er
  utelaten. Eit eksplisitt lokalt `class_uri` (som dei 19 vi la til i fase 1)
  gir difor **inga ny RDF-semantikk** utover kva LinkML uansett ville
  generert — verdien av å setje feltet eksplisitt ligg i å *overstyre*
  fallback-en med ei ekte, ekstern mapping.
- `exact_mappings`/`close_mappings` har eit **anna** føremål enn `class_uri`:
  «You may wish to avoid committing to completely reusing a linked data
  concept, whilst wanting to retain a mapping» — dei uttrykkjer ein lausare,
  ikkje-forpliktande semantisk likskap, medan `class_uri` forpliktar
  identiteten.

**Ny konvensjonsregel lagt til** i `.claude/rules/linkml-schema.md` (seksjonen
«Slot-uri og class-uri»): ekstern ekvivalent er no eksplisitt føretrekt bruk
av `class_uri`; lokalt prefiks er berre fallback når ingen rimeleg ekstern
ekvivalent finst. (Brukaren bad om «CLAUDE.md» — regelen er lagt i
`.claude/rules/linkml-schema.md`, som er den faktiske, DRY-korrekte plasseringa
for LinkML-skjemakonvensjonar; CLAUDE.md peikar sjølv dit for denne typen
regel og duplisererer ikkje innhald derifrå, jf. CLAUDE.md sin eigen
DRY-regel.)

## Fase 3 — full gjennomgang av lokale class_uri (i gang)

Brukaren bad om ein full gjennomgang av **alle** `class_uri` som peikar til
eit lokalt (ikkje-eksternt) namnerom, for å finne eksterne ekvivalentar der
det er mogleg.

### Presisert omfang

Eit `class_uri` er rekna som **lokalt** (i omfang for gjennomgangen) når
den URI-basen prefikset løyser til:

1. **Ikkje** høyrer til ein kjend, ekte tredjeparts standardorganisasjon
   (`w3.org`, `purl.org`, `xmlns.com`, `schema.org`, `opengis.net`,
   `data.europa.eu`, `spdx.org`, `w3id.org`) — desse er alltid ekskluderte,
   dei er allereie korrekt eksterne.
2. **Ikkje** er delt av fleire skjema i repoet (t.d.
   `data.norge.no/vocabulary/modelldcatno#` brukt av både
   `modelldcat-katalog` og `modelldcat-modell`, eller EU sine `m8g:`/`eli:`
   kjernevokabular brukt av fleire AP-NO-profilar) — desse er *de facto*
   publiserte, delte standardar internt i økosystemet, sjølv om dei ikkje
   er W3C/EU, og er difor også ekskluderte.
3. FINT-prefiksa (`adm:`, `ark:`, `utd:`, `res:`, `okn:`, `pvn:`, `cv:`,
   `fint:`) er ekskluderte sidan dei løyser til FINT sitt eige,
   ekte publiserte API-namnerom (`schema.fintlabs.no`) — allereie korrekt
   ekstern mapping, sjølv om det berre er brukt av éin skjemafamilie.

Att står **296 klassar i 19 skjemafiler**, der `class_uri` brukar eit
prefiks som berre det eine skjemaet sjølv brukar (anten identisk med
`default_prefix`, som `aksje:`, eller ein eigen "vokabular#"-stil URI som
berre det skjemaet brukar, som NGR sine `ngr:`/`ngre:`/`ngrp:`/`ngrv:`):

| Skjema | Tal klassar |
|---|---|
| `ngr-eiendom` | 41 |
| `enhetsregisteret-bvrinn` | 39 |
| `enhetsregisteret-bvrinnfelles` | 39 |
| `ngr-person` | 34 |
| `enhetsregisteret-bvrstiftelsesdokument` | 25 |
| `ngr-adresse` | 21 |
| `ngr-virksomhet` | 19 |
| `register-over-aksjeeiere` | 18 |
| `enhetsregisteret-bvrfriv` | 10 |
| `samt-bu` | 10 |
| `enhetsregisteret-frivilligorganisasjonapi` | 9 |
| `javazonetalk` | 7 |
| `enhetsregisteret-bvrbekreftelse` | 6 |
| `fair-metadata` | 5 |
| `cpsv-ap-no` | 4 |
| `skos-ap-no` | 3 |
| `xkos-ap-no` | 3 |
| `enhetsregisteret-bvrettersendingavvedlegg` | 2 |
| `dqv-core` | 1 |

### Metode for vidare arbeid

For kvar klasse: undersøk om det finst ein presis, etablert ekstern
ekvivalent i vokabular som alt er i bruk/kjende i norsk offentleg samanheng
— prioritert i denne rekkjefølgja:

1. EU sine kjernevokabular: Core Business Vocabulary (`m8g:`/`rov:` —
   særleg relevant for registerdata som `Aksjeselskap`/verksemder), Core
   Person Vocabulary, Core Location Vocabulary (`locn:`), Core Public
   Organisation Vocabulary.
2. W3C: `org:` (organisasjonsstruktur), `foaf:` (aktørar), `prov:`
   (heilagt/opphav), `vcard:` (kontaktinfo), `time:` (tidsrom).
3. `schema.org` (breitt dekkande, brukt fleire stader alt i repoet).
4. Andre publiserte norske/nordiske standardar der relevant.

Berre foreslå endring der ekvivalensen er **semantisk presis** — ikkje
tvinge fram svake/omtrentlege treff berre for å fjerne eit lokalt prefiks.
Klassar utan rimeleg ekstern ekvivalent (venta å vere hovudtyngda —
mange av desse er svært Noreg-/registerspesifikke forretningsomgrep utan
internasjonal standardklasse) skal **behalde** lokalt `class_uri`
uendra — det er den korrekte, tilsikta bruken av fallback-mønsteret.

### Status — gjennomført

Tre parallelle undersøkingsagentar granska kvar sin del av dei 296 klassane
(verifiserte kandidat-URI-ar mot faktiske vokabularkjelder via WebFetch/
WebSearch, ikkje gjetting). Konservativ line: berre semantisk presise treff
vart tilrådde, resten behalde lokalt.

**24 klassar fekk retta `class_uri` til ein verifisert ekstern ekvivalent:**

| # | Skjema | Klasse | Ny `class_uri` |
|---|---|---|---|
| 1 | ngr-adresse | Representasjonspunkt | `locn:Geometry` |
| 2 | ngr-eiendom | Representasjonspunkt | `locn:Geometry` |
| 3 | ngr-eiendom | Person | `person:Person` |
| 4 | ngr-eiendom | Hovedenhet | `rov:RegisteredOrganization` |
| 5 | ngr-person | Person | `person:Person` |
| 6 | ngr-person | GeografiskAdresse | `locn:Address` |
| 7 | ngr-virksomhet | Person | `person:Person` |
| 8 | ngr-virksomhet | Hovedenhet | `rov:RegisteredOrganization` |
| 9 | ngr-virksomhet | Underenhet | `org:OrganizationalUnit` |
| 10 | ngr-virksomhet | RolleIVirksomhet | `org:Post` |
| 11 | ngr-virksomhet | GeografiskAdresse | `locn:Address` |
| 12 | enhetsregisteret-bvrinn | Kontaktopplysning | `vcard:Kind` |
| 13 | enhetsregisteret-bvrinn | Virksomhet | `rov:RegisteredOrganization` |
| 14 | enhetsregisteret-bvrinn | Person | `foaf:Person` |
| 15 | enhetsregisteret-bvrinnfelles | Kontaktopplysning | `vcard:Kind` |
| 16 | enhetsregisteret-bvrinnfelles | Virksomhet | `rov:RegisteredOrganization` |
| 17 | enhetsregisteret-bvrinnfelles | Person | `foaf:Person` |
| 18 | enhetsregisteret-bvrstiftelsesdokument | Virksomhet | `rov:RegisteredOrganization` |
| 19 | enhetsregisteret-bvrstiftelsesdokument | Person | `foaf:Person` |
| 20 | enhetsregisteret-bvrstiftelsesdokument | GeografiskAdresse | `locn:Address` |
| 21 | enhetsregisteret-bvrbekreftelse | Virksomhet | `rov:RegisteredOrganization` |
| 22 | enhetsregisteret-bvrbekreftelse | Person | `foaf:Person` |
| 23 | enhetsregisteret-frivilligorganisasjonapi | Tidsperiode | `dct:PeriodOfTime` |
| 24 | register-over-aksjeeiere | Tidspunkt | `time:Instant` |

Nødvendige nye prefiks lagt til (`locn:`, `person:`, `rov:`, `org:`, `vcard:`,
`time:`) — `foaf:`/`dct:` var alt til stades i dei fleste av desse skjemaa.

**Mønster i dei 24:** `Person` → `person:Person`/`foaf:Person` (7×, EU Core
Person Vocabulary vs. FOAF avhengig av kva som alt var i bruk i skjemaet),
`Virksomhet`/`Hovedenhet` → `rov:RegisteredOrganization` (6×, W3C Registered
Organization Vocabulary — presis match for eit registrert rettssubjekt i
Enhetsregisteret), `GeografiskAdresse`/`Representasjonspunkt` → `locn:Address`/
`locn:Geometry` (5×, EU Core Location Vocabulary — berre på **abstrakte/
paraply-klassar**, konkrete adressetype-underklassar som `Vegadresse`/
`Postboksadresse` er medvite **behaldne lokalt** sidan LOCN ikkje har
underklassar for adressetypar og ei kollapsing ville øydelagt
`rdf:type`-skiljet mellom dei). Sistnemnde løyser gap 3 frå
`standardetterleving.md` (Attverande gap) som del av same fiks.

**272 klassar behaldne lokalt** — enten fordi ingen presis ekstern ekvivalent
finst (fleirtalet: svært Noreg-/register-/lovverksspesifikke omgrep som
`Prokura`, `Signaturrett`, `Aksjeinnskudd`, norske adresseundertypar,
Folkeregister-spesifikke omgrep), eller fordi klassen alt hadde ei medviten
`exact_mappings`/`close_mappings`-løysing (t.d. heile `samt-bu`, sjå eige
avsnitt under) som ville mista informasjon om han vart erstatta med eit
enkelt `class_uri`.

**11 klassar fjerna frå omfanget** (falske positivar i den opphavlege
296-lista): `cpsv-ap-no`, `skos-ap-no`, `xkos-ap-no` og `dqv-core` sine
"lokale" treff var i røynda alt korrekt eksterne — dei brukar kvar sitt
publiserte AP-NO-vokabular (`cpsvno:`, `skosno:`, `xkos:` — sistnemnde er
ikkje eingong norsk, det er DDI Alliance sin publiserte ontologi) som berre
tilfeldigvis vart klassifiserte som "eine-skjema-bruk" av det opphavlege
skriptet. Ingen endring gjort på desse.

**Uavklara/ikkje-applikerte forslag (medvite ikkje gjennomført):**
- `ngr-eiendom.OffisiellAdresse` → `locn:Address` (moderat tillit — flagga av
  forskingsagenten som ei duplikat/kryssreferanse-oppføring, ikkje den
  kanoniske definisjonen; behalde lokalt for konsistens med korleis
  `ngr-adresse` sjølv handterer same-namngjeve konkrete underklasse)
- `ngr-virksomhet.Rolleinnehaver` → `org:Membership` (moderat tillit —
  semantisk skilnad mellom "innehavar" (entitet) og "medlemskap"
  (relasjon); behalde lokalt)
- `enhetsregisteret-bvrfriv/-frivilligorganisasjonapi.FrivilligOrganisasjon`
  → `rov:RegisteredOrganization` (flagga som grensetilfelle av
  forskingsagenten sidan klassen har fleire FRIV-spesifikke felt utover ei
  minimal registrerings-stubb; behalde lokalt)
- `adms:Identifier` for ymse identifikator-klassar (`Matrikkelnummer`,
  `Folkeregisteridentifikator`, `Foedselsnummer`, `DNummer`) — vurdert for
  lite presist av forskingsagenten, ikkje applikert

**Spesialtilfelle stadfesta som korrekt as-is:** `samt-bu-schema.yaml` sine
10 klassar har alle alt anten `exact_mappings` eller `close_mappings` til
presise eksterne omgrep (t.d. `Elev` → `close_mappings: schema:Student`,
`Kommune`/`Fylke`/`PrivatVirksomhet` → delt `exact_mappings: org:Organization`).
Dette er *ikkje* eit gap — det er nøyaktig den tilrådde bruken av
mappings-felta (jf. Fase 2: «avoid committing... whilst retaining a mapping»)
når fleire syskenklassar ville kollapse til same eksterne klasse og miste
`rdf:type`-skiljet seg imellom. `.claude/rules/linkml-schema.md` sin nye
regel har alt eit eksplisitt unntak for nett dette tilfellet.

### Validering

- `make lint` for alle 10 endra skjemafiler: ingen nye åtvaringar (kun
  pre-eksisterande "manglar description"-åtvaringar på containerattributt).
- `make roundtrip` for alle 10: 9/10 OK (JSON + TTL). Eitt avvik
  (`enhetsregisteret-bvrinnfelles`, `roundtrip-ttl`) — verifisert
  **pre-eksisterande og uavhengig** av desse endringane via `git stash`
  (feilar identisk med og utan class_uri-fiksane).
- `make validate-instance` mot eksempelfiler: 6/10 «No issues found». Dei 4
  attverande (`bvrinnfelles`, `bvrstiftelsesdokument`, `bvrbekreftelse`,
  `frivilligorganisasjonapi`) feilar med `ValueError: Unknown CURIE prefix:
  https` — verifisert **pre-eksisterande og uavhengig** av desse endringane
  via `git stash` (identisk feil før klasse_uri-fiksane). Rotårsak: desse
  fire er eksplisitt merka «Generert av mcp-linkml-generator — dette er eit
  utkast» med `imports:` som ei rå `https://raw.githubusercontent.com/...`-
  URL (ikkje ein CURIE/relativ sti), som `schemaloader` ikkje klarer å løyse
  i `validate-instance`-kommandoen (skil seg frå `lint`/`roundtrip`, som
  begge fungerer fint på same filene). Ikkje retta — utanfor omfanget for
  denne specen, og skjemaa er alt eksplisitt merka som utkast.

## Utført

Fase 1-3 fullførte 2026-08-28. `.claude/rules/linkml-schema.md` oppdatert med
ny konvensjonsregel. 24 klassar i 10 skjemafiler fekk retta `class_uri` til
verifiserte eksterne ekvivalentar (deriblant gap 3 frå
`standardetterleving.md`, no løyst). 272 klassar stadfesta korrekt behaldne
lokalt etter grundig, kjeldeverifisert vurdering. Alle endringar validerte
(lint reint, roundtrip/validate-instance-avvik verifisert pre-eksisterande
og uavhengig av arbeidet her).
