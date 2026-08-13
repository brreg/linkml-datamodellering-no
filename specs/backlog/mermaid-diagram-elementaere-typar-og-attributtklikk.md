# Plan: 404 på elementære datatypar og misvisande attributtklikk i mermaid-klassediagram

**Kortnamn:** `mermaid-diagram-elementaere-typar-og-attributtklikk`
**Eksempel:** `mkdocs/docs/ap-no/cpsv-ap-no/klasser/adresse.md`,
`mkdocs/docs/samt/samt-bu/klasser/rektor.md`
**Dato:** 2026-08-12

---

## Bakgrunn

`mkdocs/docs/ap-no/cpsv-ap-no/klasser/adresse.md` sitt mermaid `classDiagram`
for klassen `Adresse` avdekkjer to distinkte, urelaterte problem som begge
gjeld korrektheita til `click ... href`-direktiv i genererte klasse-/slot-sider
(same underliggjande mekanisme som vart delvis retta i
`specs/done/mermaid-klikkbare-lenker-404.md`, men to nye, ikkje-dekte
feilklassar).

### Problem A: 404 på klikkbare lenkjer til elementære datatypar

I `adresse.md` sitt diagram peikar `click String href "../string/"` og
`click Uriorcurie href "../uriorcurie/"` til sider som **ikkje finst** i
`mkdocs/docs/ap-no/cpsv-ap-no/klasser/` — verifisert:

```bash
$ ls mkdocs/docs/ap-no/cpsv-ap-no/klasser/ | grep -iE "string|uriorcurie|langstring"
langstring.md
```

Berre `langstring.md` finst. `click LangString href "../langstring/"` (same
diagram) fungerer difor korrekt — det er nettopp kontrasten brukaren la merke
til.

**Same mønster stadfesta i eit heilt anna domene:**
`mkdocs/docs/samt/samt-bu/klasser/rektor.md` sitt diagram for klassen
`Rektor` har `click Skole href "../skole/"` og `click Person href
"../person/"` (klassereferansar — fungerer) side om side med `click Uriorcurie
href "../uriorcurie/"` og `click String href "../string/"` (elementære
typar — 404), akkurat same asymmetri som i `Adresse`.

**Viktig korrigering — retta rotårsaksanalyse:**
Den første versjonen av denne specen samanlikna berre lokale, `.gitignore`-a
byggartefaktar (`generated/`, `mkdocs/docs/<domain>/`) på tvers av skjema, og
konkluderte feilaktig at `samt-bu` og `enhetsregisteret-bvrinn` genererer
`String.md`/`Uriorcurie.md` korrekt medan `cpsv-ap-no` ikkje gjer det. Dette
var **feil**, fordi dei lokale artefaktane var utdaterte:
`generated/samt/samt-bu/docs/String.md` var datert 5. juli 2026 — over ein
månad gammal, frå eit tidlegare lokalt byggsteg, ikkje representativ for
gjeldande CI/pipeline-åtferd.

Verifisert direkte mot **produksjonssida** (`sitemap.xml` på
`https://brreg.github.io/linkml-datamodellering-no/`, som reflekterer siste
vellykka `generate.yml`-køyring, `25bb4321`, 2026-08-12T16:48 UTC):

```bash
$ curl -s https://brreg.github.io/linkml-datamodellering-no/sitemap.xml \
    | grep -iE "cpsv-ap-no/klasser|samt-bu/klasser" | grep -iE "string|uriorcurie"
# (ingen treff for verken cpsv-ap-no eller samt-bu)
```

**Alle tre testa domene manglar `string`/`uriorcurie`-sider i produksjon** —
`ap-no/cpsv-ap-no`, `samt/samt-bu` **og** `oreg/enhetsregisteret-bvrinn`.
Dette er altså **ikkje** eit skjema-spesifikt problem, men eit **portalomfattande**
gap: LinkML sin `gen-doc` genererer tilsynelatande aldri individuelle
dokumentasjonssider for elementære, ikkje-lokalt-omdefinerte typar frå
`linkml:types` (`string`, `uriorcurie`, truleg `integer`/`boolean`/`float`/`date`
også) — dei vert bundla inn i éi samle-stubbside (`types.md`, "Shared type
definitions for the core LinkML mode and metamodel") i staden. Typar som
**er** lokalt omdefinerte i eit skjema sin eigen `types:`-blokk (t.d.
`Duration`, `GYear`, `NonNegativeInteger` i `cpsv-ap-no-schema.yaml`) får
derimot eigne sider — det er truleg denne skilnaden (lokalt definert vs.
importert-uendra) som er den faktiske, konsistente rotårsaka, ikkje
diamant-import eller skjemastorleik slik tidlegare versjon av denne specen
spekulerte i.

**Metodisk lærdom for vidare arbeid i denne specen:** verifiser alltid mot
**produksjonssida sitt `sitemap.xml`** (eller ein fersk `make gen-doc`-køyring
i ein reint checka-ut container) — **aldri** mot eksisterande filer i
`generated/` eller `mkdocs/docs/<domain>/` åleine, sidan begge er
`.gitignore`-a byggoutput som fritt kan vere utdaterte lokale rester frå
tidlegare økter.

**Omfang:** minst 5 filer i `cpsv-ap-no` (`adresse.md`, `aktor.md`,
`dokumentasjonstype.md`, m.fl.) og minst 1 fil i `samt-bu` (`rektor.md`,
truleg fleire) har broten `click String href`/`click Uriorcurie href`.
Sidan gapet ser ut til å vere portalomfattande og systemisk (alle tre testa
domene råka), er reell utbreiing truleg svært stor — full kartlegging er
steg 5 under.

### Problem B: attributtklikk i diagrammet peikar alltid til klassa sjølv, ikkje til sloten

I same diagram er `Adresse : full_adresse`, `Adresse : id`, `Adresse : land`,
`Adresse : postnummer` og `Adresse : poststad` rendra som medlemsrader inni
same klasseboks som `class Adresse` + `click Adresse href "../adresse/"`.
Mermaid sin `classDiagram`-syntaks støttar **kun eitt `click`-mål per
klasseboks** — det finst ingen eigen `click`-mekanisme for enkelte
medlemsrader. All tekst inni boksen (tittel og medlemsliste) er difor
klikkbar, men utløyser **same** href, uansett kva for medlemsrad brukaren
klikkar på. Resultatet: eit klikk på `full_adresse`-teksten i diagrammet
navigerer til `Adresse`-sida sjølv, ikkje til `full_adresse.md` (som
`## Eigenskapar`-tabellen lenger nede på same side korrekt lenkjer til).

Dette er ikkje ein regresjon i `copy_artifacts.sh` eller i LinkML sin
`gen-doc` — det er ei **grunnleggjande avgrensing i mermaid sin
classDiagram-click-syntaks**, og gjeld systematisk for **alle** klassar med
minst éin attributt i heile portalen, ikkje berre `Adresse`. Kan difor ikkje
løysast med same slags sed-regel-fiks som Problem A og
`mermaid-klikkbare-lenker-404.md`.

---

## Steg

### Problem A — 404 på elementære datatypar

1. Reproduser med ein **fersk** `make gen-doc SCHEMA=src/linkml/ap-no/cpsv-ap-no/cpsv-ap-no-schema.yaml`
   (ikkje stol på eksisterande filer i `generated/` — dei kan vere
   utdaterte lokale rester, jf. funnet over) og stadfest at
   `generated/ap-no/cpsv-ap-no/docs/` manglar `String.md`/`Uriorcurie.md`
   (og eventuelt andre elementære typar brukt i skjemaet, t.d. `Boolean`,
   `Integer`, `Date` dersom dei finst). Gjenta for `samt-bu` for å stadfeste
   at same skjer der (produksjonsverifisert, men ikkje enno stadfesta med ein
   fersk lokal `make gen-doc`-køyring).
2. Stadfest hypotesen frå Bakgrunn-seksjonen: samanlikn `types:`-blokka i
   `cpsv-ap-no-schema.yaml` (som har lokale typedefinisjonar `Duration`,
   `GYear`, `NonNegativeInteger` — desse FÅR eigne sider) mot bruken av
   `string`/`uriorcurie` (importerte, ikkje lokalt omdefinerte — desse FÅR
   IKKJE eigne sider). Stadfest at dette mønsteret held for alle elementære
   typar på tvers av fleire skjema, ikkje berre dei to testa her.
3. Diagnostiser kvifor LinkML sin `DocGenerator` berre genererer
   enkelttype-sider for lokalt omdefinerte typar, ikkje for typar brukt
   uendra frå eit importert skjema (`linkml:types`) — sjekk om dette er
   dokumentert, tilsikta åtferd i LinkML sin `gen-doc` (sjekk LinkML sin
   GitHub-issue-tracker/dokumentasjon for "docgen types not generated" eller
   tilsvarande), eller ein upstream-bug. Dokumenter funnet i `bugs/` dersom
   det er ein stadfesta upstream-avgrensing/tilsikta åtferd (jf. mønsteret i
   BUG-6/BUG-7).
4. Vel og implementer fiks basert på funn i steg 3 — mest sannsynleg
   alternativ gitt at dette er portalomfattande og systemisk: eit
   post-prosesseringssteg i `copy_artifacts.sh` (eller eit nytt steg i
   `publish.sh`) som genererer minimale stub-sider for alle elementære
   `linkml:types`-typar som er referert i eit `click ... href`-direktiv, men
   som ikkje har fått ei eiga side frå `gen-doc`. Alternativt (b) ei
   skjemaendring som unngår føresetnaden, eller (c) ei anna løysing avdekt i
   steg 3. Skal avklarast med brukaren før implementering dersom fleire
   alternativ er aktuelle.
5. Kartlegg full omfang **mot produksjonssida sitt `sitemap.xml`** (ikkje
   lokale artefaktar) på tvers av **alle** domene/skjema — bruk
   `check-mermaid-click-hrefs.py` (som alt hentar frå publisert portal) for
   dette, eller ein tilsvarande grep mot `sitemap.xml` for kvart elementært
   typenamn (`string`, `uriorcurie`, `integer`, `boolean`, `float`, `date`,
   osv.) kombinert med `klasser/`-stien.
6. Verifiser fiksen: `make docs-publish`, stadfest at
   `mkdocs/docs/ap-no/cpsv-ap-no/klasser/string.md`,
   `.../uriorcurie.md` og `mkdocs/docs/samt/samt-bu/klasser/string.md`,
   `.../uriorcurie.md` finst og at `adresse.md` og `rektor.md` sine
   `click`-lenkjer resolvar korrekt.
7. Legg til regresjonstest i `tests/test_make.sh` som stadfestar at alle
   `click <Namn> href`-mål i `klasser/*.md` faktisk har eit korresponderande
   `.md`-filnamn i same katalog (utvidar/kompletterer den eksisterande
   `test_copy_artifacts_click_href`-testen frå
   `specs/done/mermaid-klikkbare-lenker-404.md`, som verifiserer href-format
   men ikkje at målfila faktisk finst).

### Problem B — misvisande attributtklikk (avgrensing, ikkje enkel fiks)

8. Avklar med brukaren kva for tilnærming som er ønskt, sidan dette ikkje er
   ein rein kodefeil:
   - **(a) Aksepter som kjend avgrensing** — dokumenter i `bugs/` med
     forklaring om mermaid sin classDiagram-click-syntaks, og legg til ei
     kort forklarande linje ved diagramma i mkdocs (eller i
     `mkdocs/docs/index.md` sine "Kjende avgrensingar") om at
     `## Eigenskapar`-tabellen under diagrammet er fasiten for
     slot-spesifikke lenkjer.
   - **(b) Fjern det misvisande visuelle inntrykket** — undersøk om
     `gen-doc`-malen (eller eit post-prosesseringssteg) kan generere
     diagram utan attributt-rader inni klasseboksen (kun klassenamn +
     relasjonspiler til andre klassar/typar), slik at det ikkje ser ut som
     kvar attributt-rad er individuelt klikkbar.
   - **(c) Anna diagramtype/verktøy** som støttar per-medlem-click (t.d.
     PlantUML, som repoet alt genererer parallelt via `make gen-plantuml`)
     — vurder om PlantUML-diagrammet (som alt finst i `diagrams/`-katalogen)
     kan promoterast som primærdiagram i staden for mermaid, eller om
     PlantUML-diagrammet allereie har korrekte per-attributt-lenkjer og
     berre treng betre synlegheit på sida.
9. Implementer valt tilnærming og verifiser (lokalt `make docs-build` +
   stikkprøve på `adresse.md` og minst éi anna klasse-side).

## Handlingsliste

- [ ] Reproduser Problem A med fersk `make gen-doc` for `cpsv-ap-no` OG `samt-bu` (ikkje lokale rester)
- [ ] Stadfest hypotesen: lokalt omdefinert type → eiga side, importert-uendra type → ingen side
- [ ] Diagnostiser om manglande enkelttype-sider er tilsikta LinkML-åtferd eller ein upstream-bug, dokumenter i `bugs/`
- [ ] Vel og implementer fiks for Problem A (avklar alternativ med brukaren om usikkert)
- [ ] Kartlegg fullt omfang av Problem A **mot produksjonssida sitt `sitemap.xml`** på tvers av alle domene/skjema
- [ ] Verifiser fiks med `make docs-publish` og stikkprøve på `adresse.md` og `rektor.md`
- [ ] Legg til/utvid regresjonstest i `tests/test_make.sh` for målfil-eksistens
- [ ] Avklar tilnærming (a/b/c) for Problem B med brukaren
- [ ] Implementer og verifiser valt tilnærming for Problem B
