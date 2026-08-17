# Evaluering: dekker release-please-workflowen `endringsdato` for alle skjema?

## Bakgrunn

Brukaren ber om ei evaluering av om `release-please.yml` oppdaterer
`annotations.endringsdato` på **alle** skjema — spesielt for skjema med
avvikande filnamngjeving og for modellkatalogar som deler mappe med fleire
skjema. Dette er ei rein evaluering, ingen kodeendring er utført.

**Mekanismen som skal evaluerast** ligg i steget "Oppdater schema-versjonar i
release-PR" i `.github/workflows/release-please.yml`. For kvar `pkg_path` i
`.github/release-please-manifest.json` gjer steget:

```bash
schema=$(find "$pkg_path" -maxdepth 1 -name "*-schema.yaml" 2>/dev/null | head -1)
...
yq eval -i ".annotations.endringsdato = \"$TODAY\"" "$schema"
```

Merk: dette er **ikkje** det same som `src/assets/scripts/update-schema-dates.py`
(dokumentert i `specs/done/auto-datoannotasjonar-release.md`) — det scriptet
finst i repoet, men vert **ikkje kalla** frå `release-please.yml` slik
workflowen ser ut i dag. Den faktiske logikken er ein enklare, direkte
`find | head -1`-basert inline-bash i workflowen. Dette avviket mellom spec og
faktisk workflow bør merkast, sjølv om det ikkje var hovudspørsmålet.

To eigenskapar ved `find "$pkg_path" -maxdepth 1 -name "*-schema.yaml" | head -1`
er avgjerande for svaret:

1. **`-maxdepth 1`** — finn berre skjema *direkte* i `pkg_path`. Viss
   `pkg_path` i `release-please-config.json`/`-manifest.json` peikar på ei
   mappe som er eitt nivå *over* der skjemaet faktisk ligg, finn `find`
   ingenting.
2. **`| head -1`** — viss `pkg_path` inneheld **fleire** `*-schema.yaml`-filer
   (delte katalogar via det dokumenterte `submodels:`-unntaket, jf.
   CONVENTIONS.md § "Éin modell per katalog"), vert berre den første
   (alfabetisk, via `find`s katalogrekkjefølgje) oppdatert. Resten vert aldri
   rørt av dette steget.

## Metode

Samanlikna `packages`-lista i `.github/release-please-config.json` mot alle
faktiske `src/linkml/**/*-schema.yaml`-filer i repoet, og verifiserte funna
direkte mot innhaldet i dei aktuelle skjemafilene (`version`, `endringsdato`,
`utgivelsesdato`, fråvær av `CHANGELOG.md` som proxy for "aldri releasa av
release-please").

## Funn

### Kategori A — modellar heilt utanfor `packages`-lista (9 stk)

Desse følgjer **standard namngjeving** (`<modell>/<modell>-schema.yaml`) — dei
er altså ikkje eit namngjevingsavvik i seg sjølv, men manglar heilt som
`package`-oppføring i `release-please-config.json`. `release-please` kan difor
aldri oppdage ei endring for dei, og «Oppdater schema-versjonar i
release-PR»-steget køyrer aldri for dei:

- `src/linkml/ap-no/common-ap-no`
- `src/linkml/ap-no/xkos-ap-no`
- `src/linkml/modellkatalog/digdir-modellkatalog`
- `src/linkml/modellkatalog/kartverket-modellkatalog`
- `src/linkml/modellkatalog/ksdigital-modellkatalog`
- `src/linkml/modellkatalog/novari-modellkatalog`
- `src/linkml/modellkatalog/skatteetaten-modellkatalog`
- `src/linkml/oreg/enhetsregisteret-bvrinn`
- `src/linkml/oreg/lunchregisteret`

**Stadfesting:** ingen av desse har `CHANGELOG.md` (som `release-please`
oppretter automatisk for alle pakkar det faktisk releasar). `common-ap-no` og
`xkos-ap-no` har `version: "1.0.0"` og `utgivelsesdato: "2023-01-01"` —
opphavlege placeholder-verdiar som aldri har vorte automatisk oppdaterte.
Interessant nok viste `.github/valid-scopes.txt` (som er dynamisk generert frå
katalogstrukturen, ikkje frå `release-please-config.json`) alle 9 som **gyldige
commit-scope** — ein commit som `fix(xkos-ap-no): ...` passerer altså
skip-sjekken i `release-please.yml` og trigger workflowen, men gjev likevel
ingen release fordi pakken ikkje finst i `packages`. Feilen er stille: verken
commit-forfattar eller CI-logg indikerer at scope-et manglar effekt.

Dei 5 org-modellkatalogane (digdir/kartverket/ksdigital/novari/skatteetaten)
hadde fram til siste commit (`d9a700ca`) manglande `endringsdato`/
`utgivelsesdato`/`license`/`utgiver` heilt — dette vart nettopp **manuelt**
retta i `specs/backlog/badge-fullstendigheit-kartlegging.md` (tiltak T3/T7),
ikkje av release-please-automatikken. Utan ei fast løysing her vil desse felta
gå stale igjen ved neste reelle endring i skjemaa, sidan automatikken framleis
ikkje dekkjer dei.

### Kategori B — delte katalogar via `submodels:` (dqv-ap-no, modelldcat-ap-no)

CONVENTIONS.md dokumenterer eksplisitt at éin katalog kan innehalde fleire
`*-schema.yaml` via `submodels:`-feltet (sirkulær-import-unngåing og logisk
spesifikasjonsseparasjon). To katalogar brukar dette i dag:

| Katalog (`pkg_path`) | Skjema i katalogen |
|---|---|
| `src/linkml/ap-no/dqv-ap-no` | `dqv-ap-no-schema.yaml`, `dqv-core-schema.yaml` |
| `src/linkml/ap-no/modelldcat-ap-no` | `modelldcat-ap-no-schema.yaml`, `modelldcat-katalog-schema.yaml`, `modelldcat-modell-schema.yaml` |

`find "$pkg_path" -maxdepth 1 -name "*-schema.yaml"` matchar **alle** filene i
kvar katalog, men `| head -1` plukkar berre den alfabetisk første
(`dqv-ap-no-schema.yaml` og `modelldcat-ap-no-schema.yaml`). Berre desse to får
`version`/`endringsdato`/`utgivelsesdato` automatisk synkronisert; dei tre
undermodellane (`dqv-core`, `modelldcat-katalog`, `modelldcat-modell`) vert
**aldri** rørte av dette steget, uansett kor mange release-PR-ar som går
gjennom.

**Stadfesting (drift observert i faktiske filer):**
- `dqv-ap-no-schema.yaml`: `version: "1.16.0"` — aktivt versjonert
- `dqv-core-schema.yaml`: `version: "1.0.0"` — aldri bumpa sidan oppretting
- `modelldcat-katalog-schema.yaml`: `version: "1.0.0"` — aldri bumpa
- `modelldcat-modell-schema.yaml`: `version: "1.14.0"` — *har* vorte bumpa
  historisk (truleg frå ei tidlegare config der `separate-pull-requests: true`
  gav han eigen pakke, før konsolideringa til éin kombinert PR — sjå
  `specs/done/release-please-scope-mapping.md` og
  `specs/done/fiks-release-please-multi-pr-bug.md`), men får ikkje lenger
  oppdateringar via dagens `head -1`-logikk.
- `dqv-core-schema.yaml` sin `utgivelsesdato` stod på placeholder-verdien
  `"2023-01-01"` heilt fram til han vart **manuelt** retta i commit `d9a700ca`
  (same commit som Kategori A over) — direkte prova ved at same
  automatikk-hòl råkar submodels òg.

### Kategori C — `referanse`-domenet: pakke-sti peikar éitt nivå for høgt

`src/linkml/referanse/` inneheld **fire fullstendig sjølvstendige og
konvensjons-korrekte** modellkatalogar (kvar med eigen `<modell>-schema.yaml`,
eigen `build.yaml`, eigen `generators:`-konfig — dette er *ikkje* eit
`submodels:`-tilfelle, jf. `specs/done/referansemodell-policy-varianter-eigne-mapper.md`):

```
src/linkml/referanse/
  referansemodell/referansemodell-schema.yaml
  referansemodell-bronze/referansemodell-bronze-schema.yaml
  referansemodell-silver/referansemodell-silver-schema.yaml
  referansemodell-gold/referansemodell-gold-schema.yaml
```

Men `release-please-config.json` og `-manifest.json` registrerer berre **éin**
pakke for heile domenet: `"src/linkml/referanse": {"component": "referanse", ...}`
— altså éitt nivå *over* der alle fire skjemafilene faktisk ligg. Sidan
`find "$pkg_path" -maxdepth 1 -name "*-schema.yaml"` berre søkjer direkte i
`pkg_path`, finn han **ingen** treff i `src/linkml/referanse` (skjemaa ligg éin
katalog djupare) — heile oppdateringssteget hoppar difor over **alle fire**
referansemodellane, kvar gong.

**Stadfesting (drift observert):**
- `.github/release-please-manifest.json` seier `src/linkml/referanse: "1.4.0"`
- `referansemodell-schema.yaml` sitt eige `version:`-felt seier `"1.3.0"` —
  eitt steg bak manifestet, altså nettopp den typen drift denne logikken skal
  hindre
- `referansemodell-bronze-schema.yaml` manglar **heilt** `endringsdato:`/
  `utgivelsesdato:` (ikkje berre stale — feltet finst ikkje), og alle tre
  bronze/silver/gold-variantane står fast på `version: "1.0.0"` sidan dei vart
  oppretta
- `referansemodell/` (utan suffiks) har derimot oppdaterte datoar og ein
  kommentar i skjemaet: `## version, endringsdato og utgivelsesdato vert
  automatisk oppdatert av CI` — ein rest frå før domenet vart splitta opp
  (`referansemodell-policy-varianter-eigne-mapper.md`), då pakke-stien truleg
  peikte direkte på `src/linkml/referanse/referansemodell` (depth matcha då).
  Splitten flytta pakke-stien opp eitt nivå for å dekkje alle fire, utan at
  `-maxdepth 1`-logikken i workflowen vart justert tilsvarande.

Same rotårsak (pakke-sti eitt nivå for høgt, `src/linkml/referanse` har berre
3 stisegment mot standard 4: `src/linkml/<domain>/<modell>`) gjev òg eit
sekundært avvik i steget "Last opp artefakter til GitHub Releases", som
ekstraherer domene/modell med `cut -d/ -f3` / `cut -d/ -f4` — for
`src/linkml/referanse` gjev `-f4` ein tom streng, så opplastinga ville forsøkt
`generated/referanse//referanse-schema.json` (finst ikkje) og berre logga ei
åtvaring. Lågare alvorsgrad enn hovudfunnet, men same underliggjande orsak.

## Kopling til `badge-fullstendigheit-kartlegging.md`

Dei manglande badgene som vart kartlagde og **manuelt** retta i
`specs/backlog/badge-fullstendigheit-kartlegging.md` (T1, T3, T7 — dqv-core,
modelldcat-katalog, modelldcat-modell, dei 5 org-modellkatalogane) er nøyaktig
dei same skjemaa som Kategori A og B over. Det tidlegare arbeidet retta
**symptomet** (feltet mangla verdi), ikkje **årsaka** (automatikken som skal
halde feltet oppdatert dekkjer ikkje desse skjemaa). Utan tiltak her vil desse
felta drifte stale igjen første gong nokon av desse skjemaa vert reelt endra —
akkurat slik dei gjorde fram til no.

## Tilråding

| Kategori | Tilråding | Kompleksitet |
|---|---|---|
| A — 9 manglande pakkar | Legg til manglande `packages`-oppføringar i `release-please-config.json` + startversjon i `-manifest.json`, éin per modell (same mønster som eksisterande pakkar) | Låg — reint config, ingen workflow-logikk-endring |
| C — `referanse`-domenet | Splitt éin pakke (`src/linkml/referanse`) til fire (`.../referansemodell`, `.../referansemodell-bronze`, `.../referansemodell-silver`, `.../referansemodell-gold`), kvar med standard `<domain>/<modell>`-djupne | Låg — reint config, løyser depth-mismatchen fullstendig utan workflow-endring, og er meir korrekt sidan dei fire uansett er sjølvstendige modellar |
| B — `submodels:`-katalogar | **Supersedert, sjå under** — i staden for å utvide workflow-logikken til å handtere fleire skjema per katalog, gjer dei tre submodels (`dqv-core`, `modelldcat-katalog`, `modelldcat-modell`) om til ordinære, sjølvstendige modellkatalogar (jf. `submodels-eigne-modellkatalogar-vurdering.md`) | Låg — same handsaming som Kategori A, ingen workflow-spesialkode naudsynt |

## Avgjerder (avklart med brukar 2026-08-17)

**Spørsmål 2 — Kategori A:** Alle 9 manglande modellar skal versjonerast
**uavhengig**. Dei skal altså inn i `release-please-config.json`/
`-manifest.json` som 9 fullverdige, sjølvstendige pakkar — same mønster som
alle andre pakkar i dag (eigen `component`, eigen SemVer-historikk).

**Spørsmål 3 — script vs. inline-bash:** `src/assets/scripts/update-schema-dates.py`
skal brukast **konsekvent, alle stader**, i staden for `find ... | head -1`-
inline-bash. Dette gjeld alle tre stega i `release-please.yml` som i dag har
sin eigen `find`-basert fil-oppdaging: "Oppdater schema-versjonar i
release-PR", "Generer artefakter for releases" og "Opprett per-schema
git-tags".

### Konsekvens for scriptet — kva må utvidast

Scriptet slik det står i dag (les tilbake, jf. Bakgrunn) er **ikkje**
tilstrekkeleg til å dekkje "alle stader" utan endring:

1. **Manglar versjons-oppdatering.** Scriptet oppdaterer i dag berre
   `endringsdato`/`utgivelsesdato` — `version:`-feltet vert framleis sett av
   den separate `yq eval -i ".version = ..."`-lina i inline-bashen. Skal
   inline-bash fjernast heilt, må scriptet utvidast til også å skrive
   `version:`.
2. **Les berre `extra_files[0]`** — nøyaktig det same `head -1`-problemet som
   inline-bashen har for Kategori B, berre flytta frå bash til Python. Må
   endrast til å loope over **alle** oppføringar i `extra-files` for ein
   pakke.
3. **`extra-files` finst ikkje i dagens config.** Verken `release-please-config.json`
   sine 22 eksisterande pakkar eller dei nye pakkane frå Kategori A/C har
   `extra-files` sett i dag — scriptet ville i praksis logga "ÅTVARING: ingen
   extra-files for ..." for absolutt alle pakkar slik config ser ut no.
   `extra-files: [{"path": "<sti-til-skjema>"}]` må leggjast til eksplisitt
   for kvar pakke som skal datoppdaterast av scriptet.
4. **Artefakt- og tag-stega brukar `find` til noko meir enn datoar** — dei
   skal finne *kva skjemafil som høyrer til pakken* for `make gen-*`-kall og
   for å byggje `<schema>-v<version>`-tag-namn. Scriptet må difor eksponere
   fil-oppdaginga si (t.d. eit `--list-schema-files <pkg_path>`-modus, eller
   ein delt Python-funksjon som begge stega kallar) slik at desse to stega
   òg kan slutte å bruke `find -maxdepth 1 ... | head -1` og i staden lese
   frå same `extra-files`-kjelde som datosteget.

**Nytt gunstig biprodukt:** sidan `extra-files` peikar på ei eksplisitt fil,
ikkje ei mappe + `-maxdepth 1`, forsvinn depth-mismatchen frå Kategori C
(referanse) automatisk — uavhengig av om `referanse` vert verande éin pakke
eller vert splitta til fire. Tilrådinga under held likevel fast på å splitte
pakken, sidan dei fire referansemodellane uansett er sjølvstendige modellar
(jf. Kategori C-funna) og bør ha kvar sin uavhengige versjonshistorikk, i
tråd med prinsippet i svar på spørsmål 2.

## Kategori B — løyst: submodels vert eigne modellkatalogar

**Oppdatert 2026-08-17 — supersedert av `specs/done/submodels-eigne-modellkatalogar-vurdering.md`.**

Det opphavlege utkastet her hevda at reell uavhengig versjonering for
Kategori B ville krevje å flytte submodels ut i eigne kataloger, og at dette
"reintroduserer akkurat den sirkulær-import-risikoen `submodels:`-mekanismen
vart innført for å unngå". **Denne påstanden er verifisert feil** i den
oppfølgjande vurderinga: fysisk samlokalisering var aldri det som løyste
sirkulær-import-problemet — det var eksistensen av `dqv-core` som ei eiga,
importerbar fil. Flytting av `dqv-core-schema.yaml` (og `modelldcat-katalog`/
`-modell`) til eigne søskenmapper krev berre å oppdatere fire konkrete
import-linjer (verifisert direkte mot faktiske `imports:`-lister); kven som
importerer kven endrar seg ikkje.

**Ny, gjeldande tilråding for Kategori B:** gjer alle tre submodels
(`dqv-core`, `modelldcat-katalog`, `modelldcat-modell`) til ordinære,
sjølvstendige `<domain>/<modell>`-katalogar — nøyaktig same handsaming som
Kategori A og C. Dette gjev reell uavhengig SemVer (i tråd med prinsippet i
svar på spørsmål 2, i staden for det tidlegare "spegle versjon"-kompromisset
under), fjernar Kategori B som eigen spesialkategori heilt, og fjernar i
tillegg ein heil klasse dokumentert delmodell-spesialkode i
dokumentasjonsgenereringa (DRY-gevinst). Sjå
`submodels-eigne-modellkatalogar-vurdering.md` for full grunngjeving,
migreringskostnad og handlingsliste.

Med dette alternativet forsvinn òg behovet for punkt 2 og 4 i "Konsekvens for
scriptet"-lista over (loop over fleire `extra-files`-oppføringar) — kvar
pakke får då nøyaktig éin skjemafil, same som alle andre pakkar.

## Ny vurdering: får desse funna betydning for `modellkatalog-fleire-skjema-evaluering.md`?

Brukaren ba om ei ny vurdering av om funna over endrar konklusjonane i den
arkiverte evalueringa `specs/done/modellkatalog-fleire-skjema-evaluering.md`.
Den evalueringa (2026, før denne kartlegginga) konkluderte at
`submodels:`-mekanismen bør behaldast uendra, og at kostnaden var "avgrensa i
omfang" og "konsentrert til dokumentasjonsgenereringa" — med eksplisitt
påstand om at "kjernefunksjonalitet (lint, validering, **versjonering**,
build) er urørt".

**Denne påstanden er no vist å vere feil på eitt punkt:** versjonering *er*
rørt. Kategori B i denne kartlegginga dokumenterer med konkrete tal at
`dqv-core-schema.yaml` og `modelldcat-katalog-schema.yaml` har stått fast på
`version: "1.0.0"` sidan dei vart oppretta, og at `endringsdato`/
`utgivelsesdato` for desse same filene dreiv til dei vart manuelt lappa i
`badge-fullstendigheit-kartlegging.md` (T1/T3/T7). Den tidlegare evalueringa
undersøkte `make`-verktøykjeda (som er filbasert og difor upåverka av delt
katalog) og dokumentasjonslaget, men undersøkte **ikkje**
release-please/CI-automatikken sitt handtering av delte kataloger — det var
eit reelt blindpunkt i det opphavlege funnet, ikkje ei bevisst avgrensing.

**Betyr dette at anbefalinga "behald submodels-mekanismen" bør reverserast?**
**Delvis, ja** — oppdatert etter `submodels-eigne-modellkatalogar-vurdering.md`.
Den vurderinga viste at fysisk samlokalisering aldri var det som løyste
sirkulær-import-problemet (det var eksistensen av ei eiga importerbar fil),
og at alle tre noverande brukstilfelle av `submodels:` (`dqv-core`,
`modelldcat-katalog`, `modelldcat-modell`) trygt kan gjerast om til ordinære,
sjølvstendige modellkatalogar — med fire trivielle import-sti-oppdateringar
som einaste reelle kopling til sjølve mekanismen. Tilrådinga er difor no å
**fjerne dei tre eksisterande bruka** av `submodels:` (ikkje fjerne feltet
frå kodebasen som mekanisme — det kan framleis vere dokumentert for eit
hypotetisk framtidig behov, jf. handlingslista i den vurderinga).

**Konkret tillegg til den arkiverte evalueringa sitt kostnadsbilete (§2 "Der
ho kostar noko"):** ein ny kostnadskategori — **CI/release-automatikk** — bør
leggjast til lista saman med dei alt dokumenterte (`publish.sh`,
`mkdocs/lib/sections/delmodellar.sh`, `generate-informasjonsmodell.py`).
Denne nye kategorien er samstundes det som gjer at total-kostnaden av å
**behalde** dagens tre bruk no veg tyngre enn total-kostnaden av å fjerne
dei — vurderinga i den arkiverte evalueringa (§2, "kostnaden er reell, men
avgrensa") heldt då automatikk-hòlet var ukjent. Konklusjon #3 (ikkje innfør
eit tredje grupperingsnivå) står framleis ved lag uendra — det er ortogonalt
til dette spørsmålet.

**Handsaming:** `specs/done/` skal stå urørt (jf. CLAUDE.md). Denne vurderinga
vert difor ikkje skriven inn i den arkiverte fila, men står her som
kryssreferert oppdatering. Dersom brukar ønskjer at det arkiverte dokumentet
sjølv skal reflektere dette (t.d. ei kort "Sjå òg"-tilvising til denne
specen), er det eit eige, eksplisitt steg — ikkje gjort automatisk her.

## Handlingsliste

- [x] Kategori B: løyst via `submodels-eigne-modellkatalogar-vurdering.md` —
      `dqv-core`, `modelldcat-katalog` og `modelldcat-modell` er no eigne
      modellkatalogar, registrerte som tre nye, sjølvstendige pakkar i
      `release-please-config.json`/`-manifest.json` (startversjon = noverande
      `version:`-felt i kvart skjema). Ingen `extra-files`-spegling naudsynt —
      same handsaming som alle andre pakkar.
- [ ] Kategori A: legg til 9 nye, sjølvstendige pakkar i `release-please-config.json` + `-manifest.json`
- [ ] Kategori C: splitt `referanse`-pakken i 4 sjølvstendige pakkar, fjern den generiske `src/linkml/referanse`-oppføringa
- [ ] Utvid `update-schema-dates.py`: skriv òg `version:` (ikkje berre datoar). Loop over `extra-files`-oppføringar er **ikkje lenger naudsynt** dersom Kategori B vert løyst via eigne modellkatalogar — kvar pakke har då nøyaktig éin skjemafil, som alle andre pakkar
- [ ] Erstatt `find ... | head -1` i alle tre steg i `release-please.yml` ("Oppdater schema-versjonar", "Generer artefakter", "Opprett per-schema git-tags") med kall til det utvida scriptet
- [ ] `actionlint` mot `release-please.yml` etter kvar endring (obligatorisk jf. CLAUDE.md)
- [ ] Verifiser med ein reell release-PR at alle kategoriar (A, B, C) no får korrekt `version`/`endringsdato`/`utgivelsesdato`
- [ ] Avklar med brukar om `modellkatalog-fleire-skjema-evaluering.md` skal få ei kort kryssreferanse til denne specen og til `submodels-eigne-modellkatalogar-vurdering.md` (valfritt, sjå vurdering over)
