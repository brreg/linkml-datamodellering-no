# Plan: 404 på elementære datatypar og misvisande attributtklikk i mermaid-klassediagram

**Kortnamn:** `mermaid-diagram-elementaere-typar-og-attributtklikk`
**Eksempel:** `mkdocs/docs/ap-no/cpsv-ap-no/klasser/adresse.md`,
`mkdocs/docs/samt/samt-bu/klasser/rektor.md`,
`mkdocs/docs/ap-no/cpsv-ap-no/klasser/offentligorganisasjon.md` (`uri`-typen,
sjå tillegg 2026-08-13)
**Dato:** 2026-08-12 (oppdatert 2026-08-13)
**Vedtak (2026-08-13):** både Problem A og Problem B skal dokumenterast som
BUGS i `bugs/`/`BUGS.md` — begge har stadfesta rotårsak i eit **eksternt**
verktøy (LinkML sin `docgen.py` for A, Mermaid sin `classDiagram`-syntaks for
B), ikkje i dette repoet sin eigen kode, og fylgjer difor same mønster som
BUG-6/BUG-7/BUG-9. Dette gjeld **uavhengig** av kva for intern
workaround/mitigering som til slutt vert vald og implementert for kvart
problem (jf. steg 3-4 for A og alternativ a/b/c for B under) — sjølve
bug-dokumentasjonen er ikkje betinga av valet, berre "Workaround"-seksjonen
i den enkelte bug-fila er det. Neste ledige ID-ar i `BUGS.md` sin indeks er
**BUG-13** (Problem A) og **BUG-14** (Problem B) — stadfest at desse framleis
er ledige når bug-filene faktisk vert oppretta, sidan andre bugs kan ha vorte
lagt til i mellomtida.

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

**`uri` stadfesta som fjerde råka elementærtype, og stadfesta framleis 404 i
gjeldande produksjon (2026-08-13):**
`mkdocs/docs/ap-no/cpsv-ap-no/klasser/offentligorganisasjon.md` vart
undersøkt som referansefil for klassen `OffentligOrganisasjon`
(`heimeside`-sloten sin range er `uri`, `id`-sloten sin range er
`uriorcurie`). Den **lokale disk-kopien** av denne fila (datert 2026-08-11
22:52, altså **før** fiksen i `25bb4321` vart commit 2026-08-12 18:40) har
den opphavlege, pre-fiks korrupsjonen:

```
click Uri href "../http://www.w3.org/2001/XMLSchema#anyURI/"
click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
```

Dette er **ikkje** ein gjeldande feil — det stadfestar at fila er ein
utdatert lokal byggartefakt frå før `copy_artifacts.sh` sin
href-ombygging vart innført. `mkdocs/docs/**/klasser/*.md` vart
deregistrert frå git i `986a5630` (2026-06-14), så slike lokale filer kan
liggje att uendra i mange veker/månadar og feilaktig sjå ut som ein
gjeldande bug.

Verifisert direkte mot **gjeldande produksjonsside**
(`https://brreg.github.io/linkml-datamodellering-no/ap-no/cpsv-ap-no/klasser/offentligorganisasjon/`)
at gjeldande scriptversjon **har fiksa nett denne korrupsjonen** — href vert
no korrekt bygd frå click-namnet, ikkje frå ein innbaka XSD-URI:

```
click Uri href "../uri/"
click Uriorcurie href "../uriorcurie/"
click String href "../string/"
```

Men alle tre målsider **404-ar framleis** i produksjon (stadfesta
2026-08-13 med direkte `curl`):

```bash
$ for p in uri uriorcurie string; do
    curl -s -o /dev/null -w "%s -> HTTP %{http_code}\n" \
      "https://brreg.github.io/linkml-datamodellering-no/ap-no/cpsv-ap-no/klasser/$p/"
  done
uri -> HTTP 404
uriorcurie -> HTTP 404
string -> HTTP 404
```

`sitemap.xml` har **null** treff for `klasser/uri/`, `klasser/uriorcurie/`
eller `klasser/string/` på tvers av **heile** portalen (alle domene, ikkje
berre `cpsv-ap-no`/`samt-bu`):

```bash
$ grep -oE "klasser/(uri|uriorcurie|string)/</loc>" sitemap.xml | sort | uniq -c
# (ingen treff)
```

**Konklusjon (2026-08-13, tidlegare versjon — sjå korrigering under):**
dette vart først vurdert som **same rotårsak** som Problem A over (importert,
ikkje lokalt omdefinert `linkml:types`-type manglar eiga side), og
href-korrupsjonen brukaren opphavleg mistenkte (`../` limt saman med ein
absolutt XSD-URI) vart vurdert som **fullstendig retta** av
`copy_artifacts.sh` sin href-ombygging (`25bb4321`), slik at det attverande
symptomet ("lenkja er borte") vart forklart som utelukkande 404-en frå
Problem A. **Denne konklusjonen er ufullstendig — sjå ny hovudhypotese
under, som endrar kva "retta" faktisk betyr her.**

**Ny hovudhypotese (2026-08-13) — `../http://www.w3.org/2001/XMLSchema#anyURI/`
er den korrekte, tilsikta verdien frå `gen-doc`, og det er vårt eige
`copy_artifacts.sh` som fjernar/øydelegg han:**

Strippar ein `../`-prefikset frå href-en i den stale fila, resolverer resten
til ein ekte, gyldig URL — `https://www.w3.org/2001/XMLSchema#anyURI` — som
peikar til den faktiske W3C XSD-spesifikasjonen for typen. Dette er ikkje
ein tilfeldig streng; det er nøyaktig slik LinkML sin eigen `DocGenerator`
lenkjer til elementære typar som er importerte, ikkje lokalt omdefinerte.
Stadfesta ved å lese kjeldekoden til den lokalt installerte `linkml`-pakken
(`linkml==1.10.0rc4`,
`site-packages/linkml/generators/docgen.py`):

```python
# docgen.py:537-543 — _is_external()
def _is_external(self, element: Element) -> bool:
    if element is None:
        return False
    if element.from_schema == "https://w3id.org/linkml/types" and not self.genmeta:
        return True
    else:
        return False

# docgen.py:480-481 — link(), for TypeDefinition-element som er "eksterne"
if self._is_external(e):
    return self.uri_link(e)
    # → uri_link() returnerer f"[{curie}]({uri})", der `uri` er den fullt
    #   ekspanderte URI-en, t.d. "http://www.w3.org/2001/XMLSchema#anyURI"

# docgen.py:446-459 — link_mermaid(), brukt av class_diagram.md.jinja2
def link_mermaid(self, e):
    md_link = self.link(e)                       # "[xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI)"
    if not md_link.endswith(")"):
        return md_link
    link = md_link.rsplit("(")[-1][:-1]           # "http://www.w3.org/2001/XMLSchema#anyURI"
    link = link.removesuffix(".md")               # ingen endring (endar ikkje på .md)
    return f"../{link}/"                          # "../http://www.w3.org/2001/XMLSchema#anyURI/"
```

`element.from_schema == "https://w3id.org/linkml/types"` er nøyaktig det
same skiljet som vart identifisert i den (tidlegare) rotårsaksanalysen for
Problem A ("lokalt definert vs. importert-uendra") — men det viser seg at
LinkML **har** ei eiga, medvite grein for desse typane: dei skal lenkjast
**eksternt** til W3C/XSD sin definisjon, ikkje til ei lokal side. `gen-doc`
genererer altså **ikkje** eit hol her — han genererer eit fullverdig,
meiningsfullt lenkjemål. Feilen ligg i `link_mermaid()` sitt siste steg:
metoden føreset ukritisk at *alt* han pakkar ut frå ei markdown-lenkje er ein
lokal, relativ filsti, og limer på `../` + `/` uansett — også når verdien
alt er ein absolutt URL. Dette er ein **upstream LinkML-bug** i
`link_mermaid()` (ikkje i vårt repo), og han produserer nettopp den nøyaktige
strengen (`../http://www.w3.org/2001/XMLSchema#anyURI/`) me ser i den stale
`offentligorganisasjon.md`-fila — **frå ein rein `make gen-doc`-køyring,
før noko av vår eigen etterprosessering i `copy_artifacts.sh` har rørt ved
han.**

**Konsekvens for `copy_artifacts.sh` sin fiks (`25bb4321`):** sed-regelen

```bash
find "$out/klasser" -maxdepth 1 -name "*.md" \
    -exec sed -i -E 's|click ([A-Za-z0-9_]+) href "[^"]*"|click \1 href "../\L\1\E/"|g' {} +
```

bryr seg ikkje om kva den opphavlege href-verdien var — han byggjer **alltid**
ei ny, lokal `../<namn-i-lowercase>/`-lenkje frå click-namnet åleine. For
genuint lokale klasse-/enum-/slot-lenkjer er dette korrekt (og løyste den
opphavlege feilkasusen i `mermaid-klikkbare-lenker-404.md`, der href-verdien
var feilkasa, ikkje feil type). Men for eksterne `linkml:types`-typar
**kastar denne regelen bort den ekte, fungerande eksterne URI-en** LinkML
gav oss, og erstattar han med ei lenkje til ei lokal side som **strukturelt
aldri kan finnast** (fordi `gen-doc` med vilje ikkje genererer ei slik side
for desse typane — jf. `_is_external()` over). Med andre ord: fiksen bytta
éin type feil (syntaktisk broten, men semantisk gjenkjennande URL) mot ein
annan (syntaktisk gyldig, men semantisk umogleg lokal lenkje) — og gjorde
det umogleg å attreise den opphavlege, korrekte informasjonen frå den
rebygde href-en åleine.

**Dette er no hovudhypotesen som skal utforskast vidare, i staden for at
Problem A vert forklart utelukkande som "manglande lokal side":** den rette
fiksen bør truleg **bevare** eksterne, absolutte URL-ar (berre fjerne det
feilaktige `../`-prefikset LinkML sjølv legg til), og berre rebygge frå
click-namnet for href-verdiar som faktisk var meint å vere lokale
sti-referansar. Følgjeimplikasjonar som må handterast saman med ein slik
fiks:

- `mkdocs/lib/scripts/check-mermaid-click-hrefs.py` (frå `25bb4321`) sjekkar
  i dag **alle** href-ar mot `known_paths` henta frå den lokale
  `sitemap.xml` (`normalize()` + mengd-medlemskap, `check-mermaid-click-hrefs.py:35-40,89-91`)
  — ei ekte ekstern absolutt-URL (t.d. `http://www.w3.org/2001/XMLSchema#anyURI`)
  vil aldri finnast i `known_paths` og vert difor feilaktig flagga som
  `IKKJE FUNNE`, sjølv om lenkja er fullt gyldig. Scriptet må utvidast til
  å handtere absolutte `http(s)://`-hrefar annleis enn portal-interne
  relative hrefar (t.d. eige HTTP-oppslag mot ekstern URL, eller ei
  medviten kvitliste/skip for kjende eksterne vokabular-domene som
  `w3.org`).
- `tests/test_make.sh::test_copy_artifacts_click_href` (frå `25bb4321`,
  sjå `tests/test_make.sh:1285-1299`) hardkodar i dag forventinga om at
  **alle** click-hrefar (inkludert `Uriorcurie`) skal rebyggjast til
  `../<lowercase-namn>/` — testfixturen sitt eige kommentar
  (`tests/test_make.sh:1254-1255`) inneheld nettopp
  `click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"` som
  input. Denne assertion-en er den kodifiserte forma av den **no
  reviderte** hypotesen, og må oppdaterast til å forvente at eksterne
  URL-ar vert bevart (berre `../`-prefikset fjerna), ikkje omskrivne til
  ei lokal lenkje.
- `link_mermaid()`-oppførselen skal dokumenterast som **BUG-13** i `bugs/`
  (jf. steg 2 og "Vedtak"-lina i toppen av specen) uavhengig av kva fiks som
  vert vald her — sidan feilen ligg i `linkml`-pakken sin eigen `docgen.py`,
  ikkje i noko fil i dette repoet. Vurder i tillegg å melde saka oppstraums
  til LinkML (GitHub-issue) og lenkje til han frå bug-fila sitt
  "Løysing"-avsnitt.

**Verifisert 2026-08-13 mot det faktiske podman-containermiljøet** (via
`make gen-docs`, ikkje manuell podman/linkml-kommando) — sjå steg 1 under.
Containerbiletet sin `linkml`-versjon produserer nøyaktig same
`../http://www.w3.org/2001/XMLSchema#anyURI/`-mønster som den lokalt
installerte `1.10.0rc4`-pakken kjeldekodesporinga over er basert på.
Hypotesen står difor stadfesta både ved kjeldekodelesing og ved reell
byggkøyring — ikkje berre teoretisk utleiing.

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

**Rekkjefølgja under følgjer den nye hovudhypotesen (2026-08-13, sjå
Bakgrunn): at `gen-doc` med vilje lenkjer eksterne `linkml:types`-typar til
W3C/XSD, og at det er vår eiga `copy_artifacts.sh`-etterprosessering som
kastar bort denne lenkja. Steg 1-2 stadfestar hypotesen mot ein fersk
container-køyring (ikkje berre lokal kjeldekodelesing); steg 3-6 implementerer
og verifiserer ein fiks som **bevarer** eksterne URL-ar i staden for å
generere lokale stub-sider.**

1. Reproduser med ein **fersk** `make gen-doc SCHEMA=src/linkml/ap-no/cpsv-ap-no/cpsv-ap-no-schema.yaml`
   (ikkje stol på eksisterande filer i `generated/` — dei kan vere
   utdaterte lokale rester, jf. funnet over) og sjekk
   `generated/ap-no/cpsv-ap-no/docs/*.md` (altså **før** `copy_artifacts.sh`
   har rørt filene) for det rå `click`-direktivet for `string`, `uri` og
   `uriorcurie`. **Forventa funn** (jf. kjeldekodesporing av
   `linkml/generators/docgen.py:link_mermaid()` i Bakgrunn):
   `click Uri href "../http://www.w3.org/2001/XMLSchema#anyURI/"` — altså at
   containerbiletet sin `linkml`-versjon oppfører seg likt den lokalt
   installerte (`1.10.0rc4`) som vart brukt til kjeldekodesporinga. Gjenta
   for `samt-bu` sitt `rektor`-diagram. **Gjort 2026-08-13, stadfesta i det
   faktiske podman-containermiljøet** (`make gen-docs SCHEMA=src/linkml/ap-no/cpsv-ap-no/cpsv-ap-no-schema.yaml`
   og tilsvarande for `samt-bu`): `generated/ap-no/cpsv-ap-no/docs/OffentligOrganisasjon.md`
   inneheld nøyaktig `click Uri href "../http://www.w3.org/2001/XMLSchema#anyURI/"`,
   `click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"` og
   `click String href "../http://www.w3.org/2001/XMLSchema#string/"`;
   `generated/samt/samt-bu/docs/Rektor.md` viser same mønster for
   `Uriorcurie`/`String`. Hypotesen er difor stadfesta mot reell
   container-køyring, ikkje berre kjeldekodelesing.
2. Dersom steg 1 stadfestar hypotesen: dokumenter at dette **ikkje** er eit
   hol i `gen-doc` (han genererer ingen side for `string`/`uri`/`uriorcurie`
   fordi dei er meint å lenkjast eksternt til XSD, ikkje fordi han "gløymer"
   dei), men ein **upstream-bug i `link_mermaid()`** som limer `../` framanpå
   ein allereie absolutt URL. **Gjort 2026-08-13:** oppretta
   `bugs/mermaid-link-ekstern-uri-prefiks.md` som **BUG-13** (status `open` —
   vert `upstream` når intern workaround i steg 3-4 er implementert),
   komponent `linkml` (`docgen.py:link_mermaid()`), etter malen frå
   `bugs/avrotize-falsk-circular-dependency-warning.md` (BUG-9) — symptom,
   rot-årsak (kjeldekodesitat frå Bakgrunn-seksjonen over), status på
   workaround, og føreslått løysing (`link_mermaid()` manglar eit
   `startswith(("http://", "https://"))`-sjekk før `../`-prefikset vert
   limt på). Lagt til rad i `BUGS.md` sin indekstabell og i
   "Generatorar"-lista. **Attverande:** oppdater BUG-13 sin
   "Workaround"-seksjon og `Status` til `upstream` når fiksen i steg 3-4
   under er implementert.
3. **Gjort 2026-08-13.** Design fiks i `copy_artifacts.sh`: erstatt den
   blanke navnebaserte sed-regelen med logikk som skil på om den
   **opphavlege** href-verdien (før ombygging) er ein absolutt URL
   (`^https?://`) eller ein lokal sti:
   - **Absolutt URL** (typisk etter eit feilaktig `../`-prefiks limt på av
     `link_mermaid()`, jf. steg 1-2): fjern berre det innleiande
     `../`-prefikset og eit ev. avsluttande `/` limt til slutten av URL-en av
     same feil — behald resten av URL-en uendra (ikkje lowercase, ikkje
     namnebasert ombygging).
   - **Lokal sti** (klasse/enum/slot-referansar, typar med eiga side): behald
     dagens åtferd frå `25bb4321` (rebygg `../<lowercase-namn>/` frå
     click-namnet) — dette løyste den opphavlege feilkasus-bugen i
     `mermaid-klikkbare-lenker-404.md` og skal ikkje endrast for desse.
   **Implementert som to sekvensielle `sed`-passeringar** (ikkje Python —
   løyste seg reint med regex, sidan steg 2 sin sed-erstatning på ekstern
   URL fjernar `../`-prefikset og gjer at pass 2 sin uendra `\.\./`-krav
   automatisk utelèt allereie fikse eksterne URL-ar frå namnebasert
   ombygging — sjølvavgrensande rekkjefølgje, ingen betinga logikk trengst):
   ```bash
   # Steg 1: eksterne URL-ar — fjern feilaktig ../-prefiks og avsluttande /
   sed -i -E 's|click ([A-Za-z0-9_]+) href "\.\./(https?://[^"]+)/"|click \1 href "\2"|g'
   # Steg 2: attverande (lokale) hrefar — framleis ../-prefiksa — bygg om frå namnet
   sed -i -E 's|click ([A-Za-z0-9_]+) href "\.\./[^"]*"|click \1 href "../\L\1\E/"|g'
   ```
   Verifisert isolert (`/tmp/.../test-hrefs.md`) og direkte mot
   `copy_schema_artifacts()` med ein fixture som inneheld begge href-typane
   — lokale hrefar rebygde korrekt, eksterne URL-ar bevart uendra utan
   `../`-prefiks.
4. **Gjort 2026-08-13.** Oppdatert følgjeavhengige filer frå `25bb4321` som
   kodifiserte den tidlegare hypotesen:
   - `mkdocs/lib/scripts/check-mermaid-click-hrefs.py`: `check_page()` skil
     no på `urlsplit(resolved).netloc` mot portalen sin eigen netloc — same
     netloc vert sjekka mot lokal `sitemap.xml` som før, annan netloc (ekstern
     absolutt URL) vert validert med eit direkte `HEAD`-oppslag mot
     målserveren via ny `check_external_url()` (med ein delt cache +
     `threading.Lock` for å unngå gjentekne oppslag mot same URL på tvers av
     mange sider). Verifisert både med mocka `fetch()` (lokal 404 framleis
     fanga, gyldig ekstern URL ikkje flagga, broten ekstern URL korrekt
     flagga `EKSTERN LENKJE FEILA`) og med reelle HTTP-kall mot
     `w3.org` (`#anyURI`/`#string` → sanne, ein oppdikta anker → usann).
   - `tests/test_make.sh::test_copy_artifacts_click_href`: fixturen har no
     også ein `String`-klikk med same mønster som `Uriorcurie`; assertion-en
     brukar eit eksplisitt `expected_hrefs`-oppslag (assosiativt array) i
     staden for éin generisk namnebasert formel, sidan lokale og eksterne
     hrefar no har ulik forventa form. Køyrd isolert (funksjonen ekstrahert
     og køyrd standalone, sidan heile `test_make.sh` startar heile
     testsuiten ved `source`) — alle assertions passerer.
5. Kartlegg full omfang **mot produksjonssida sitt `sitemap.xml`** (ikkje
   lokale artefaktar) på tvers av **alle** domene/skjema for elementærtypar
   som framleis manglar eiga side etter fiksen (t.d. typar som *ikkje* er
   `linkml:types`-eksterne, men likevel manglar side av andre grunnar) — bruk
   `check-mermaid-click-hrefs.py` (oppdatert i steg 4) eller ein tilsvarande
   grep mot `sitemap.xml`. **Gjort 2026-08-13:** grep av **rå**
   `generated/ap-no/cpsv-ap-no/docs/*.md` og `generated/samt/samt-bu/docs/*.md`
   (fersk `make gen-docs`-køyring, pre-`copy_artifacts.sh`) for alle unike
   `click <Namn> href`-typenamn stadfestar at same `../http://www.w3.org/...`
   -mønster (`_is_external()`-greina, BUG-13) gjeld **generisk** for **alle**
   testa elementærtypar frå `linkml:types`, ikkje berre `uri`/`uriorcurie`/`string`:
   `boolean`, `date`, `double`, `float` viser identisk mønster
   (`click Boolean href "../http://www.w3.org/2001/XMLSchema#boolean/"` osv.).
   Fiksen frå steg 3 er **generisk** (matchar på `https?://`-prefiks, ikkje på
   typenamn), så han dekkjer desse automatisk utan justering. Til kontrast:
   lokalt omdefinerte typar (`Duration`, `GYear`, `NonNegativeInteger` i
   `cpsv-ap-no-schema.yaml`) har **ikkje** dette mønsteret
   (`click Duration href "../Duration/"`) og har verifisert eigne lokale sider
   (`Duration.md` m.fl. finst i `generated/.../docs/`) — stadfestar den
   opphavlege "lokalt definert vs. importert-uendra"-hypotesen frå Bakgrunn,
   no forklart av `_is_external()`-greina i staden for eit hol i `gen-doc`.
   Ingen attverande "ekte manglar lokal side"-feilklasse er funne blant dei
   elementærtypane som faktisk er i bruk i desse to skjema.
6. Verifiser fiksen: `make docs-publish`, stadfest at `offentligorganisasjon.md`,
   `adresse.md` og `rektor.md` sine `click Uri`/`click String`/`click Uriorcurie`-hrefar
   no peikar til gyldige, resolverbare `https://www.w3.org/...`-URL-ar (ikkje
   `../uri/` osv.), og at genuint lokale click-hrefar (klassar, enums) framleis
   fungerer som før. **Gjort 2026-08-13** (via direkte kall til
   `copy_schema_artifacts` mot dei faktiske `generated/`-katalogane for
   `ap-no/cpsv-ap-no` og `samt/samt-bu` — full multi-domene `make docs-publish`
   vart ikkje køyrt, sidan `copy_artifacts.sh` sin `copy_schema_artifacts` er
   den einaste funksjonen fiksen endra, og han vart verifisert direkte):
   `mkdocs/docs/ap-no/cpsv-ap-no/klasser/offentligorganisasjon.md`,
   `adresse.md` og `mkdocs/docs/samt/samt-bu/klasser/rektor.md` har no
   `click Uri href "http://www.w3.org/2001/XMLSchema#anyURI"`,
   `click Uriorcurie href "http://www.w3.org/2001/XMLSchema#anyURI"`,
   `click String href "http://www.w3.org/2001/XMLSchema#string"` — reine,
   resolverbare eksterne URL-ar, ingen `../`-prefiks. Lokale klasse-lenkjer
   (`../adresse/`, `../aktor/`, `../langstring/`, `../konsept/`,
   `../deltagelse/`, `../person/`, `../skole/`, `../rektor/` osv.) er uendra
   korrekte. Stadfesta både ved direkte HTTP-oppslag mot dei to reelle XSD-URL-ane
   (`http://www.w3.org/2001/XMLSchema#anyURI` og `#string`, begge 2xx/3xx) og
   ved oppdatert regresjonstest (steg 4).

### Problem B — misvisande attributtklikk (avgrensing, ikkje enkel fiks)

7. **Gjort 2026-08-13:** oppretta `bugs/mermaid-classdiagram-eitt-click-per-boks.md`
   som **BUG-14** (status `open`, komponent `mermaid` (`classDiagram`-syntaks))
   — symptom (klikk på ein medlemsrad utløyser same href som klassenamnet),
   rot-årsak (Mermaid sin `classDiagram` støttar kun eitt `click`-mål per
   klasseboks, ingen eigen click-mekanisme per medlemsrad — jf.
   Bakgrunn-avsnittet over). Lagt til rad i `BUGS.md` sin indekstabell og i
   "Generatorar"-lista. Bug-dokumentasjonen er gjort **uavhengig** av kva
   mitigeringsalternativ (a/b/c) under som til slutt vert vald. **Attverande:**
   oppdater BUG-14 sin "Workaround"-seksjon når eit alternativ er vald og
   implementert (steg 9).
8. Avklar med brukaren kva for **mitigeringstilnærming** som er ønskt (fylles
   inn i BUG-14 si "Workaround"-seksjon), sidan dette ikkje er ein rein
   kodefeil i vårt repo:
   - **(a) Aksepter som kjend avgrensing** — ingen mitigering utover
     BUG-14-dokumentasjonen frå steg 7, men legg til ei kort forklarande
     linje ved diagramma i mkdocs (eller i `mkdocs/docs/index.md` sine
     "Kjende avgrensingar") om at `## Eigenskapar`-tabellen under
     diagrammet er fasiten for slot-spesifikke lenkjer.
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
9. Implementer valt mitigeringstilnærming, oppdater BUG-14 sin
   "Workaround"-seksjon tilsvarande, og verifiser (lokalt `make docs-build` +
   stikkprøve på `adresse.md` og minst éi anna klasse-side).

## Handlingsliste

- [x] Reproduser Problem A med fersk `make gen-doc` for `cpsv-ap-no` OG `samt-bu` — stadfest at rå (pre-`copy_artifacts.sh`) output i `generated/.../docs/*.md` inneheld `click Uri href "../http://www.w3.org/2001/XMLSchema#anyURI/"` (jf. kjeldekodespora `linkml/generators/docgen.py:link_mermaid()`) — gjort 2026-08-13
- [x] Opprett `bugs/mermaid-link-ekstern-uri-prefiks.md` som **BUG-13** (status `open` → `upstream`, intern workaround implementert), legg til rad i `BUGS.md` — gjort 2026-08-13
- [x] Design og implementer fiks i `copy_artifacts.sh` som **bevarer** absolutte eksterne URL-ar (berre fjernar `../`-prefikset), og berre rebygger namnebasert for genuint lokale hrefar — gjort 2026-08-13
- [x] Oppdater `check-mermaid-click-hrefs.py` til å handtere absolutte `http(s)://`-hrefar korrekt (ikkje slå opp mot lokal sitemap) — gjort 2026-08-13
- [x] Oppdater `tests/test_make.sh::test_copy_artifacts_click_href` sin `Uriorcurie`-fixture-forventing til bevart ekstern URL — gjort 2026-08-13
- [x] Kartlegg om attverande elementærtypar (`integer`, `boolean`, `float`, `date` m.fl.) er `linkml:types`-eksterne (→ same fiks) eller ei anna, ekte "manglar lokal side"-feilklasse — gjort 2026-08-13, alle testa (`boolean`, `date`, `double`, `float`) er `linkml:types`-eksterne, dekt av same generiske fiks
- [x] Verifiser fiks med reell `copy_schema_artifacts`-køyring og stikkprøve på `offentligorganisasjon.md`, `adresse.md` og `rektor.md` — gjort 2026-08-13 (full multi-domene `make docs-publish` ikkje køyrt, ikkje naudsynt for denne verifiseringa)
- [x] Oppdater BUG-13 sin "Workaround"-seksjon og `Status` basert på implementert fiks — gjort 2026-08-13
- [x] Opprett `bugs/mermaid-classdiagram-eitt-click-per-boks.md` som **BUG-14** (status `open`), legg til rad i `BUGS.md` — gjort 2026-08-13
- [ ] Avklar mitigeringstilnærming (a/b/c) for Problem B med brukaren
- [ ] Implementer valt mitigeringstilnærming for Problem B, oppdater BUG-14 sin "Workaround"-seksjon, og verifiser
