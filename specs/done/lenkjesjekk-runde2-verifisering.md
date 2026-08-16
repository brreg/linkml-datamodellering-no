# Ny verifisering av utvalde lenkjesjekk-funn (runde 2)

## Bakgrunn

Brukaren limte inn eit utdrag av `lenkjesjekk`-oppsummeringa frå
`lenkje-og-mermaid-sjekk.yml` (etter at `specs/done/lenkjesjekk-3817-feil-evaluering.md`
sine 6 kategoriar alt var fiksa, jf. commit `7e1a2ac7`) og bad om at **kvar
distinkte lenkje** i utdraget vart testa på nytt direkte (ikkje berre
vurdert ut frå tidlegare funn) og at resultatet vart dokumentert som ei ny
spesifikasjon. Same metodikk som runde 1: direkte HTTP-oppslag mot kvar
unike URL (fleire gjentekne forsøk med nettlesar-`User-Agent` for å utelukke
forbigåande feil), samt filsystemsjekk for interne lenkjer.

**Oppdatering:** verifiseringa er no følgd opp med faktisk implementering
(sjå § Utført til slutt i dokumentet).

## Kategoriar

### A. `arkitektur/valideringsregler#bronze`/`#gold` — REELL FEIL (ny, ikkje dekt av runde 1)

Genereringsskriptet `mkdocs/lib/scripts/generate-validation-md.py` line 86
byggjer lenkja slik:

```python
policy_link = f"[policy: {policy}](../../arkitektur/valideringsregler/#{anchor})"
```

Dette brukar ein **trailing slash utan `.md`-ending**
(`valideringsregler/#anchor`), som er eit anna mønster enn den etablerte
konvensjonen for portal-interne relative lenkjer andre stader i repoet
(stadfesta i `mkdocs/docs/kom-i-gang/ny-domenemodell.md:205` og
`ny-org.md:124`, som begge brukar `../arkitektur/valideringsregler.md`).
`arkitektur/valideringsregler.md` finst (stadfesta, med overskriftene
`### bronze`, `### silver`, `### gold` som gjev korrekte MkDocs-ankernamn
`#bronze`/`#silver`/`#gold`), men **fila** `arkitektur/valideringsregler`
(utan `.md`, med trailing slash tolka som katalog) finst ikkje i
kjeldetreet lychee skannar — MkDocs sin eigen clean-URL-oppløysing
(`.md` → `/`) skjer først ved bygg, lychee ser berre rå kjeldefiler.
Stadfesta via CLAUDE.md § «Relative vs. absolutte lenkjer i portalinnhald»:
riktig mønster er `.md`-ending, ikkje trailing slash.

Feilen arvast til **alle** genererte `index.md`-sider som har eit
`## Valideringsresultat`-avsnitt (stadfesta i utdraget: common-ap-no,
cpsv-ap-no, dcat-ap-no, dqv-ap-no — truleg alle domene med
`validation_policy` sett).

**Fiks:** endre line 86 til
```python
policy_link = f"[policy: {policy}](../../arkitektur/valideringsregler.md#{anchor})"
```

### B. `purl.org/adms/publishertype/PrivateIndividual` — REELL FEIL (revidert frå runde 1)

Runde 1 (kategori 3) fjerna ein `(s)`-typo frå denne URI-en og rekna saka
som løyst. **Stadfesta no at sjølve den korrigerte URI-en 404-ar**, ikkje
berre den gamle typo-varianten:

```
http://purl.org/adms/publishertype/PrivateIndividual
  → 302 → https://purl.org/adms/publishertype/PrivateIndividual
  → 307 → https://purl.archive.org/adms/publishertype/PrivateIndividual
  → 404
```

Reprodusert konsistent i 3 forsøk med nettlesar-UA (ikkje forbigåande).
Rotårsak: `purl.org` sin PURL-resolvingsteneste er migrert til
`purl.archive.org` (Internet Archive), og den nye verten manglar ein
route for dette spesifikke, individuelle vokabular-*termet* — sjølve
namnerommet **verkar** framleis (`http://purl.org/adms/publishertype/`
utan term gjev 200, redirecta til ei RDF-fil på
`raw.githubusercontent.com/SEMICeu/ADMS-AP/...`). Same mønster som
`concept-catalog.fellesdatakatalog.digdir.no` (runde 1, kategori 6) og
`data.norge.no/vocabulary/cccevno` (kategori D under): URI-en er ein
gyldig RDF-vokabular-identifikator, men ikkje meint å vere ei sjølvstendig
nettlesarvenleg side per term.

`meaning:`-verdien i `common-ap-no-schema.yaml:214` er sjølv **korrekt**
(dette er den rette ADMS-termen — ingen skjemaendring skal gjerast).

**Fiks:** legg til eksklusjon i `.github/lychee.toml`, t.d.
`"^https?://purl\\.(org|archive\\.org)/adms/"` (eller breiare
`purl\\.org`/`purl\\.archive\\.org` viss fleire purl.org-baserte
vokabular-termar dukkar opp same veg — sjekk om andre `purl.org`-referansar
i repoet òg er individuelle termar før ei så brei eksklusjon).

### C. `w3id.org/linkml/types` — REELL FEIL for automatiserte klientar, men ikkje "flaks" (revidert to gonger)

Runde 1 (kategori 7) konkluderte «flaks/transient». Første re-test i denne
runda (utan forklarande header/JS-analyse) konkluderte «reelt daud».
**Ingen av delane er heilt presise.** Rotårsaka, stadfesta ved å lese
sjølve respons-kroppen:

```
https://w3id.org/linkml/types
  → 302 → https://linkml.github.io/linkml-model/types
  → 301 → https://linkml.io/linkml-model/types
  → HTTP 404, MEN kroppen er ei "mike"-versjonsrouter-side (mkdocs sitt
    versjoneringsverktøy) med denne <script>-logikken:
    window.location.href = window.location.href.replace(basePath, `${basePath}/latest`)
```

Sida gjer altså ein **klientside JavaScript-redirect** til
`/linkml-model/latest/types` — ikkje ein HTTP-redirect. Ein nettlesar
køyrer scriptet og landar på fungerande innhald (stadfesta av brukaren sin
manuelle test). `curl`/lychee køyrer ikkje JavaScript og ser difor den
statiske 404-merkte landingssida sin bokstavelege HTTP-status. Dette er
**ikkje** content negotiation (jf. D under) og kan **ikkje** rettast med ein
`Accept`-header — det er ein strukturell avgrensing i alle ikkje-JS
lenkjesjekkarar, lychee inkludert.

Denne URI-en kjem frå LinkML sin eigen `from_schema`-metadata for den
innebygde `linkml:types`-basisskjemaet (importert av `common-ap-no-schema`
jf. CLAUDE.md § Importhierarki) — **ikkje** noko vårt eige repo skriv eller
kan rette i kjeldeskjemaa. Han opptrer i `types.md` i alle domene som
transitivt importerer `linkml:types` (stadfesta: common-ap-no, cpsv-ap-no,
dcat-ap-no, dqv-ap-no i utdraget — truleg alle).

**Fiks:** legg til eksklusjon i `.github/lychee.toml` for
`^https://w3id\\.org/linkml/` — dette er ein oppstraums, aldri-redigerbar
referanse frå sjølve LinkML-verktøyet, og eit strukturelt (JS-redirect)
avvik ingen lychee-konfig kan løyse. Merk i kommentaren at ressursen **er**
levande for menneskelege lesarar (stadfesta manuelt), berre ikkje for
ikkje-JS HTTP-klientar.

### D. `xmlns.com/foaf/0.1/Agent` — FALSK POSITIV (revidert to gonger — rotårsak er content negotiation, ikkje daud lenkje)

Runde 1 konkluderte «flaks/transient». Første re-test i denne runda (utan
`Accept`-header) konkluderte «reelt daud, same struktur som B». **Begge var
feil.** Stadfesta ved å sende ein nettlesarrealistisk `Accept`-header:

```
# Utan Accept-header (lychee sin standard, ingen eksplisitt Accept sett):
http://xmlns.com/foaf/0.1/Agent → 302 → https://xmlns.com/foaf/0.1/Agent → 404

# Med Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
# (det ein nettlesar faktisk sender):
http://xmlns.com/foaf/0.1/Agent → 302 → 303 See Other → https://xmlns.com/foaf/spec/ → 200
```

Serveren gjer ekte content negotiation på term-URI-en (vanleg mønster for
RDF-namnerom som konjunkt tilbyr både maskinlesbar RDF og menneskelesbar
HTML for same URI). Utan ein eksplisitt `Accept: text/html` returnerer
serveren 404 i staden for å 303-redirecte til spec-sida. Dette er **ikkje**
same feilklasse som B (purl.org, der term-stien manglar heilt uansett
header — stadfesta med same header-test, framleis 404).

`slot_uri`/`class_uri`-referansane til `foaf:Agent` i skjemaa er
**korrekte** — ingen skjemaendring.

**Fiks (betre enn eksklusjon):** lychee støttar per-host custom headers
(`-H`/`[hosts."...".headers]`, jf.
<https://lychee.cli.rs/troubleshooting/custom-headers/> — same mekanisme
som t.d. GitHub-token-header for API-rate-limit). Legg til i
`.github/lychee.toml`:
```toml
[hosts."xmlns.com"]
headers = ["Accept: text/html"]
```
Dette let lychee faktisk stadfeste at ressursen er levande, i staden for å
gøyme feilen bak ein eksklusjon som ville skjult ei framtidig ekte
lenkjeråte på same host.

### E. `data.norge.no/vocabulary/cccevno#...` — STADFESTA OPE, retesta med korrekt Accept-header

I lys av funna i C, D og F (content negotiation-blindsone i grunnleggjande
`curl`-oppslag utan `Accept`-header) vart denne kategorien **retesta** med
same nettlesar-realistiske `Accept: text/html,...`-header som avslørte
falske positivar andre stader. Resultatet er uendra: sjølve namnerommet
(`https://data.norge.no/vocabulary/cccevno`, utan fragment) gjev framleis
eit ekte backend-404 —
```
HTTP/2 404
content-type: application/json; charset=utf-8
{"detail": "Not Found"}
```
— eit JSON API-svar, ikkje ei SPA-skal-side (samanlikn med F under, der
same vert-domenet returnerer ei 200 SPA-skal-side for gyldige konsept-IDar).
Dette stadfestar at manglet er reelt: `data.norge.no` sin backend
attkjenner ikkje `/vocabulary/cccevno` som ein gyldig ressurs i det heile,
uavhengig av `Accept`-header. Ingen endring frå konklusjonen i
`specs/done/lenkjesjekk-3817-feil-evaluering.md` § Merk.

**Tilråding:** ingen kodeendring. Vurder å leggje `cpsv-ap-no-schema.yaml`
sine `cccevno:`-referansar til same type eksklusjon som B/C
(`^https://data\\.norge\\.no/vocabulary/cccevno`) dersom dette skal reknast
som eit varig kjent avvik — men det krev ei aktiv avgjerd om at namnerommet
aldri vil verte publisert, som ikkje er stadfesta her.

### F. `data.norge.no/concepts/<uuid>` — FALSK POSITIV (revidert frå runde 1 — konklusjonen der var feil)

**Viktig korrigering:** runde 1 (og første utkast av denne spec-en) rekna
alle desse som stadfesta, ekte 404-ar som kravde manuelt søk etter
erstattings-ID-ar i Felles begrepskatalog. **Dette var feil**, oppdaga då
brukaren melde at manuell nettlesartesting av eit anna funn i same
kategori-familie (D) synte lesbart innhald — som fekk oss til å teste alle
`data.norge.no`-oppslag på nytt med ein eksplisitt `Accept`-header i staden
for `curl` sin standard (`Accept: */*`).

```
# Utan Accept-header (lychee sin implisitte åtferd, det opphavlege testoppsettet):
https://data.norge.no/concepts/02131737-bb20-3204-93e0-46678b7d57be → 404

# Med Accept: application/json:
https://data.norge.no/concepts/02131737-bb20-3204-93e0-46678b7d57be → 200
{"id":"02131737-...","uri":"https://concept-catalog.fellesdatakatalog.digdir.no/collections/970205039/concepts/d2799493-...",
 "prefLabel":{"nb":"konsept",...},"publisher":{"name":"Norges vassdrags- og energidirektorat (nve)",...}, ...}
```

Alle 5 UUID-ane i utdraget stadfesta **200 med ekte, gyldig konseptdata**
via JSON-API-et (same mønster, kontrollert éin og éin):
`02131737-bb20-3204-93e0-46678b7d57be`, `d85379a6-837b-3102-b202-999a99240d69`,
`806b0e3a-38ab-3a3a-88d6-ddc7f8669f4a`, `9c17b5e3-6763-3650-a741-b879e7bbdecc`,
`67a58f0e-2e39-33dc-bca9-1ef29a001b2f`. Desse er **ikkje** daude referansar
— dei er gyldige, eksisterande omgrep i Felles begrepskatalog, harvesta og
publiserte via `data.norge.no`. Rotårsaka er identisk med kategori D: serveren
gjer content negotiation og returnerer 404 for tomme/`*/*`-Accept-headrar i
staden for anten HTML-SPA-skalet eller JSON-representasjonen.

**Dette gjer runde 1 sin research-oppgåve («finn erstattings-UUID-ar i
Felles begrepskatalog») overflødig for desse 5 URI-ane** — dei treng ingen
erstatning. Det opphavlege opne punktet i
`specs/done/lenkjesjekk-3817-feil-evaluering.md` § Merk bør reviderast
tilsvarande (ikkje gjort her, sidan den fila er arkivert og urørt per
CLAUDE.md-konvensjon — noter det som ny informasjon i staden).

**Fiks (same mekanisme som D):** legg til per-host `Accept`-header for
`data.norge.no` i `.github/lychee.toml`:
```toml
[hosts."data.norge.no"]
headers = ["Accept: application/json"]
```
Merk: sidan `data.norge.no` òg vert brukt til andre ting enn
`/concepts/`-oppslag (t.d. schema-ID-ar, jf. avvik 4 i
`specs/backlog/avvik-peikarar-til-offentlege-ressursar.md`), bør denne
headeren testast mot eit representativt utval av alle `data.norge.no`-URL-ar
i repoet før ho vert lagt til globalt for verten — ein `Accept:
application/json`-header kan i prinsippet endre respons-forma (og dermed
lychee sin tolking av gyldig 2xx/3xx) for URL-ar som er meint å vise
HTML-sider, ikkje JSON. Test begge headerval
(`application/json` og `text/html,...`) mot fulle lista over
`data.norge.no`-treff i ein `lychee --dump`-køyring før val.

### G. GitHub CHANGELOG compare-lenkjer — STADFESTA OPE, mønsteret har vakse (delvis ny informasjon)

Stadfesta at git-taggane manglar for begge domena i utdraget:

| Domene | Tag-ar som finst | Tag-ar som **manglar** |
|---|---|---|
| `dcat-ap-no` | v2.6.0, v2.8.0, v2.10.0 | **v2.7.0, v2.9.0** |
| `dqv-ap-no` | v1.7.0, v1.10.0, v1.12.0 | **v1.8.0, v1.9.0, v1.11.0** |

Same rotårsak som runde 1 (sjå
`specs/done/lenkjesjekk-3817-feil-evaluering.md` § Merk, tredje punkt) —
`CHANGELOG.md` er auto-generert av release-please, som tydelegvis ikkje
skapar ein git-tag for kvar versjon han skriv eit changelog-avsnitt for.
Mønsteret er ikkje reint alternerande (dqv-ap-no manglar to samanhengande
versjonar, 1.8.0 og 1.9.0), så det er ikkje eit enkelt "kvar andre
versjon"-mønster — krev eiga gransking av
`.github/release-please-config.json`/`.github/release-please-manifest.json`
og `release-please.yml`-historikken for å finne rotårsaka. Utanfor omfanget
til denne verifiseringa.

**Tilråding (kortsiktig, same som runde 1 sitt forslag):** legg til
eksklusjon i `.github/lychee.toml` for GitHub compare-URL-ar under dette
repoet, sidan dei er autogenererte og ikkje under direkte redigeringskontroll:
```toml
"^https://github\\.com/brreg/linkml-datamodellering-no/compare/"
```
**Tilråding (langsiktig, ny):** opprett eigen, separat spec for å granske
kvifor release-please hoppar over tag-oppretting for enkelte versjonar — dette
er ein separat root cause frå lenkjesjekk-arbeidet og bør ikkje blandast inn
i ein lychee-konfig-fiks.

## Samandrag

| Kategori | Type | Handling |
|---|---|---|
| A — `valideringsregler#anchor` | Reell feil (ny) | Rett `.md`-ending i genereringsskript |
| B — `purl.org/.../PrivateIndividual` | Reell feil (stadfesta med og utan `Accept`-header) | Lychee-eksklusjon |
| C — `w3id.org/linkml/types` | Reell feil for ikkje-JS-klientar (JS-redirect, ikkje conneg) | Lychee-eksklusjon |
| D — `xmlns.com/foaf/0.1/Agent` | **Falsk positiv** (content negotiation) | Per-host `Accept`-header i lychee.toml |
| E — `data.norge.no/vocabulary/cccevno` | Reell feil (stadfesta med korrekt `Accept`-header) | Ingen tiltak / vurder eksklusjon |
| F — `data.norge.no/concepts/<uuid>` | **Falsk positiv** (content negotiation, same som D) | Per-host `Accept`-header i lychee.toml |
| G — GitHub compare-lenkjer | Reell feil (stadfesta via GitHub API, autoritativt) | Lychee-eksklusjon (kort sikt) + eigen spec (lang sikt) |

**Merk om metodikk — dette er den viktigaste lærdomen frå denne runda:**
Fleire vertar i denne rapporten (`xmlns.com`, `data.norge.no`) gjer ekte
HTTP content negotiation og returnerer 404 for eit bart `curl`-oppslag utan
eksplisitt `Accept`-header (lychee sin implisitte standardåtferd), sjølv om
ressursen er fullt fungerande for ein nettlesar. Denne feilkjelda vart
oppdaga fordi **brukaren manuelt stadfesta lesbart innhald** for to av
funna (C og D) etter at første utkast av denne spec-en feilaktig
klassifiserte begge som «stadfesta daude» — det fekk oss til å retesta
**alle** dei attverande kategoriane (E, F, G) med same metodikk, som
avdekte at F (5 konsept-URI-ar) òg var ein falsk positiv av same årsak,
medan E og G heldt stand som reelle feil sjølv under fornya testing.
**Lærdom for framtidige lenkjesjekk-evalueringar:** eit bart `curl`/HEAD-kall
utan `Accept`-header er ikkje tilstrekkeleg til å stadfeste eit funn som
«reelt daud» — test alltid med ein nettlesar-realistisk
`Accept`-header før konklusjon, særleg for vertar som tydeleg har
API+HTML-dobbelrepresentasjon (innhaldstype varierer i `Vary`-responsheader).
Same prinsipp gjeld omvendt for kategori C: eit funn kan vere "levande for
menneske" (browser køyrer JS-redirect) men framleis eit **reelt, permanent**
funn for lychee, sidan lychee aldri kan køyre JavaScript — her hjelper
ingen header.

## Steg

1. `mkdocs/lib/scripts/generate-validation-md.py` line 86: endre
   `valideringsregler/#{anchor}` → `valideringsregler.md#{anchor}` (kategori A).
2. `.github/lychee.toml`: legg til per-host `Accept`-headerar for
   `xmlns.com` (kategori D) og `data.norge.no` (kategori F) — test
   `data.norge.no`-headeren mot eit representativt utval av alle URL-ar til
   verten i repoet først (sjå åtvaring i kategori F).
3. `.github/lychee.toml`: legg til eksklusjonar for kategori B, C, G (sjå
   konkrete regex-forslag i kvar kategori over).
4. Regenerer docs (`make gen-docs DOMAIN=<domain>` for alle domene som har
   `## Valideringsresultat`, deretter `make docs-publish`) for å bake inn
   kategori A-fiksen.
5. Køyr lychee lokalt på nytt for å stadfeste at kategori A, B, C, D, F, G
   er borte frå rapporten (D og F skal no gje reelle 2xx-treff, ikkje
   eksklusjon-hopp).
6. Vurder (separat, seinare spec) å granske release-please sin
   tag-opprettingslogikk for kategori G sin rotårsak.
7. Vurder å notere korrigeringa av kategori F (falsk positiv, ikkje
   forskingsbehov) ein stad synleg for framtidig lesing av
   `specs/done/lenkjesjekk-3817-feil-evaluering.md` § Merk, sidan den fila
   sjølv skal stå urørt (arkivert) per CLAUDE.md.

## Handlingsliste

- [x] Kategori A: rett `.md`-ending i `generate-validation-md.py`
- [x] Kategori B: lychee-eksklusjon for `purl.org/adms/publishertype/PrivateIndividual`
      (avgrensa til denne eine termen, **ikkje** ei brei `purl.org/adms`-eksklusjon —
      søskenterma resolvar korrekt og skal framleis sjekkast)
- [x] Kategori C: lychee-eksklusjon for `w3id.org/linkml/`
- [x] Kategori D: per-host `Accept`-header for `xmlns.com` i lychee.toml (**ikkje** eksklusjon — ressursen er levande)
- [x] Kategori E: ingen tiltak (stadfesta framleis eit ekte 404 i verifiseringssteget, ingen eksklusjon lagt til)
- [x] Kategori F: per-host `Accept`-header for `data.norge.no` i lychee.toml (**ikkje** eksklusjon, **ikkje** UUID-erstatting — alle 5 konsept stadfesta gyldige), verifisert mot representativt utval av `data.norge.no`-treff (schema-ID, concepts, organizations) før ho vart lagt til globalt
- [x] Kategori G: lychee-eksklusjon for GitHub compare-lenkjer i dette repoet
- [x] Regenerer docs + lokal lychee-verifisering av reduksjon
- [ ] Vurder eiga spec for release-please tag-gap-gransking (kategori G, lang sikt) — **ikkje utført**, framleis ope for seinare

## Utført

Alle kategoriar frå Handlingslista er implementerte og verifiserte, med to
funn undervegs som endra planen frå det opphavlege utkastet:

**1. TOML-syntaksfeil i første utkast (D, F).** `.github/lychee.toml` sin
`[hosts."...".headers]`-nøkkel forventar ein **inline table**
(`headers = { "accept" = "..." }`), ikkje ei liste av `"Name: Value"`-strengar
(det er CLI-flagget `-H` sitt format, ikkje TOML-config-formatet). Stadfesta
mot lychee sin offisielle `lychee.example.toml` (v0.24.2) og retta før
verifisering — første forsøk på lokal lychee-køyring feila med
`TOML parse error ... invalid type: sequence, expected a map`.

**2. `PrivateIndividual(s)` er den korrekte ADMS-AP-vokabulartermen, ikkje
ein typo (kategori B, ny informasjon oppdaga under implementering).** Ved å
teste om andre `purl.org/adms/publishertype/*`-termar (Company,
LocalAuthority m.fl.) resolvar normalt (dei gjer det, 200), vart det tydeleg
at berre `PrivateIndividual` skilde seg ut. Henta den offisielle ADMS-AP
SKOS-vokabularfila (`SEMICeu/ADMS-AP` sin `ADMS_SKOS_v1.00.rdf` på GitHub) og
stadfesta at `skos:notation` for denne termen faktisk **er**
`PrivateIndividual(s)` — parentesen er del av den kanoniske vokabularverdien,
ikkje ein feilinnlimt fleirtalsmarkør. Runde 1 (kategori 3,
`specs/done/lenkjesjekk-3817-feil-evaluering.md`, commit `7e1a2ac7`) fjerna
denne parentesen i god tru, men endra dermed `meaning:`-verdien til ein URI
som ikkje finst i vokabularet i det heile. Retta tilbake i
`common-ap-no-schema.yaml`. Verken variant (med eller utan parentes,
url-enkoda eller ikkje) resolvar som eiga nettside via `purl.archive.org`
— stadfesta at lychee-eksklusjonen framleis er naudsynt, no avgrensa
presist til denne eine termen.

**Endra filer:**
- `mkdocs/lib/scripts/generate-validation-md.py`: `.md`-ending i
  policy-lenkja (kategori A)
- `src/linkml/ap-no/common-ap-no/common-ap-no-schema.yaml`: retta
  `PRIVATE_INDIVIDUAL.meaning` tilbake til den kanoniske
  `PrivateIndividual(s)`-verdien
- `.github/lychee.toml`: 3 nye eksklusjonar (B — avgrensa til
  `PrivateIndividual`-termen, C, G) + 2 nye per-host `Accept`-headerar
  (D — `xmlns.com`, F — `data.norge.no`)

**Validering:**
- `make lint SCHEMA=.../common-ap-no-schema.yaml`: 4 pre-eksisterande
  `canonical_prefixes`-åtvaringar, **ingen nye** (identisk baseline til
  runde 1 sin sluttkontroll)
- `make roundtrip SCHEMA=.../common-ap-no-schema.yaml`: 2 OK, 0 feil
- `.github/lychee.toml` validert som gyldig TOML (`tomllib`) og som gyldig
  lychee-config (containerkøyring, etter header-syntaksretting)
- `make docs-publish` køyrt (alle 9 domene, ~2,5 min) for å bake inn
  kategori A- og B-fiksane i genererte sider
- Direkte scriptkøyring (`generate-validation-md.py` mot
  `generated/samt/samt-bu/validation/1.9.0/silver.json`, einaste lokalt
  tilgjengelege ekte valideringsresultat) stadfesta korrekt lenkje:
  `[policy: silver](../../arkitektur/valideringsregler.md#silver)`
- Lokal `lychee`-køyring (podman, faktisk `.github/lychee.toml`) mot alle
  sidene i det opphavlege brukarutdraget:
  - `admspublishertype.md`, `konsept.md`, `types.md`, `aktoer.md`,
    `dcat-ap-no/CHANGELOG.md`: **0 feil** (var 8+ feil i utdraget)
  - `samt-bu/index.md` (einaste sida med eit ekte
    `## Valideringsresultat`-avsnitt lokalt): policy-anker-feilen borte
  - `cpsv-ap-no`-sidene med `cccevno#...`-referansar: **framleis 404**,
    som venta (kategori E, ingen tiltak — stadfesta at eksklusjonen ikkje
    skjuler denne, sidan ho aldri vart lagt til)
- `actionlint` ikkje naudsynt (ingen `.github/workflows/*.yml`-fil endra)

**Ikkje utført (bevisst, jf. Steg 6):** eiga spec for å granske
release-please sin manglande tag-oppretting (kategori G sin rotårsak) —
utanfor omfanget til lenkjesjekk-arbeidet, ope for seinare.
