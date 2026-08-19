# Plan: 10-minutters demo av repoet (offline-sikker)

## Bakgrunn

Brukaren skal halde ein 10-minutters demo av repoet (JavaZone-kontekst),
og kan **ikkje stole på nettverket** der demoen vert halden — alt må
køyre lokalt. Brukaren la fram eit forslag til kommandosekvens og bad om
evaluering av pedagogisk verdi, tekniske feil, og om mkdocs-portalen
(køyrd lokalt) bør refererast undervegs.

Evalueringa vart gjort i to rundar. Første runde avdekte at to av dei
opphavleg føreslåtte kommandoane var **broten** (peika på ein katalog der
`SCHEMA=` krev ei enkelt fil):

```
make validate SCHEMA=src/linkml/oreg/
→ [ERROR] File 'src/linkml/oreg/' is a directory.

make gen-informasjonsmodell-instance SCHEMA=src/linkml/oreg/
→ [ERROR] [Errno 21] Is a directory: 'src/linkml/oreg'
```

Brukaren oppdaterte planen til å peike på den konkrete, nyoppretta
skjemafila i staden. Andre runde stadfesta at heile den oppdaterte
sekvensen fungerer, og fann eitt konkret forbetringsforslag: kva namn
demo-klassen bør få for å gje eit sjølvoppdaga, personleg relevant funn i
similarity-analysen (i staden for eit funn frå ein urelatert del av
repoet).

## Steg-for-steg demo-script

`src/assets/scripts/demo/javazone-demo-script.sh` skriptar heile sekvensen under
slik at kvart steg vert vist (tittel + kommando) og deretter ventar på
Enter før han faktisk køyrer — gjev kontroll over tempo under
sjølve presentasjonen. Steg 4 (live-redigeringa) har ingen kommando,
berre ein pause. Skriptet krasjar ikkje heile demoen om eitt steg skulle
feile (ikkje `set -e`) — feilen vert vist, du vel sjølv om du held fram.
Avsluttar med eit valfritt oppryddingssteg (j/N-spørsmål).

`DOMAIN`/`NAME` er parameteriserte som `ARG=verdi`-argument — same stil
som resten av repoet sine `make`-kommandoar, i staden for reine
posisjonsargument (fyrste utkast brukte posisjonsargument, som viste seg
misvisande: å skrive `DOMAIN=oreg` som fyrste argument — heilt naturleg
gitt konvensjonen elles — vart då tolka bokstaveleg som verdien
«DOMAIN=oreg», ikkje «oreg»). Rekkjefølgje er valfri, ukjende argument
gjev ei tydeleg feilmelding:

```bash
# Køyr frå repo-rota, med standardverdiar (oreg/javazonetalk):
bash src/assets/scripts/demo/javazone-demo-script.sh

# ... eller med eigne verdiar (rekkjefølgje spelar inga rolle):
bash src/assets/scripts/demo/javazone-demo-script.sh DOMAIN=<domain> NAME=<namn>
```

Vel du eit anna domene enn `oreg`, skriv scriptet automatisk ut ei åtvaring
om at «Aktivitet»-tipset i steg 5 (sjå under) var funne spesifikt for
`oreg` — med eit anna domene bør du finne eit tilsvarande, alt-eksisterande
klassenamn sjølv (t.d. ved å køyre
`make analyse-similar-classes-domain DOMAIN=<domain>` på ein tom modell
på førehand, eller berre sjå gjennom klassenamna i domenet sine skjema).

## Det verifiserte demo-scriptet

Alle kommandoane under er testa live og fungerer (og er dei same som
`javazone-demo-script.sh` køyrer). Rekkjefølgja er medvite:
`gen-jsonschema` **før** `gen-informasjonsmodell-instance` gjer at
`finnes_i_format`-feltet i sluttresultatet faktisk vert fylt ut med ei
ekte lenkje, i staden for å stå tomt.

```bash
# 1. Sjå tilgjengelege kommandoar
make help

# 2. Sjekk at miljøet er klart (~2 s)
make check-prereqs

# 3. Opprett ein ny, tom modell (~10 s)
make new-modell DOMAIN=oreg NAME=javazonetalk

# 4. Lint skjemaet (~1 s)
make lint SCHEMA=src/linkml/oreg/javazonetalk/javazonetalk-schema.yaml

# 5. LIVE-REDIGERING: legg til klassane «Aktivitet»/«Foredragsholder»/
#    «Konferanse» — sjå grunngjeving under. Scriptet skriv ut komplette,
#    ferdig-testa klassedefinisjonar klare til å lime inn — ikkje
#    naudsynt å skrive live.

# 6. Valider skjemaet — no med det utvida innhaldet frå steg 5 (~1 s)
make mcp-linkml-valider-modell SCHEMA=src/linkml/oreg/javazonetalk/javazonetalk-schema.yaml

# 7. Finn liknande klassenamn i domenet (~5 s)
make analyse-similar-classes-domain DOMAIN=oreg

# 8. Finn liknande slotnamn i domenet (~5 s)
make analyse-similar-slots-domain DOMAIN=oreg

# 9. Generer JSON Schema frå den redigerte modellen (~1 s)
make gen-jsonschema SCHEMA=src/linkml/oreg/javazonetalk/javazonetalk-schema.yaml

# 10. Generer PlantUML-diagram (~2 s)
make gen-plantuml SCHEMA=src/linkml/oreg/javazonetalk/javazonetalk-schema.yaml

# 11. Generer ModelDCAT-metadata — finnes_i_format er no fylt ut (~0.1 s)
make gen-informasjonsmodell-instance SCHEMA=src/linkml/oreg/javazonetalk/javazonetalk-schema.yaml
```

**Merk rekkjefølgja lint -> live-redigering -> valider:** lint (steg 4)
køyrer på det ferske, uendra stub-skjemaet — rask, strukturell sjekk.
Valider (steg 6) køyrer derimot **etter** at Aktivitet/Foredragsholder/
Konferanse er limt inn, slik at den rikare policy-baserte valideringa
(metadata, namnekonvensjonar, Digdir-reglar) faktisk har noko meiningsfullt
å seie noko om, i staden for å validere eit tomt stub-skjema.

Resten av dei 10 minutta går til prat, live-redigeringa i steg 5, og éin
mkdocs-sidevising (sjå under).

### Kvifor klassenamnet «Aktivitet» (steg 5)

Testa begge alternativ direkte:

| Namn | Resultat i `analyse-similar-classes-domain DOMAIN=oreg` |
|---|---|
| Eit vilkårleg namn (t.d. «Foredrag») | Ingen treff — trygt, men ingenting å vise fram |
| **«Aktivitet»** | **To treff**, begge involverer klassen du nett har vist fram: |

```
| Likskap | Namn A        | Slots A                         | Namn B      | Slots B                     |
| 100%    | Aktivitet     | aktivitet, datoGyldigFra, id     | Aktivitet   | foredragsholder, id, tittel |
| 82%     | TypeAktivitet | aktivitetskode, id, ..., tekst   | Aktivitet   | foredragsholder, id, tittel |
```

Eit 100 %-namnetreff med **tydeleg ulikt** innhald (openbert ikkje eit
reelt duplikat) pluss eit 82 %-fuzzy-treff — begge involverer noko
tilskuarane nett har sett bli laga, i staden for eit abstrakt eksempel dei
ikkje har kontekst for. `Aktivitet` finst frå før i
`src/linkml/oreg/enhetsregisteret-bvrinn/enhetsregisteret-bvrinn-schema.yaml`.

### Ferdig kopierbar klassedefinisjon (steg 5)

`javazone-demo-script.sh` skriv no ut ein komplett klassedefinisjon i
steg 5, klar til å lime rett inn — ingen live-skriving naudsynt. Tre
klasser, knytt saman via referansar, slik at PlantUML-diagrammet i steg
10 (`make gen-plantuml`) viser reelle relasjonar i staden for éin isolert
boks:

```yaml
  Aktivitet:
    description: Eit foredrag på ein konferanse.
    class_uri: javazonetalk:Aktivitet
    slots:
    - id
    - tittel
    - foredragsholder_ref
    - konferanse_ref

  Foredragsholder:
    description: Ein person som held eit foredrag.
    class_uri: javazonetalk:Foredragsholder
    slots:
    - id
    - navn
    - organisasjon

  Konferanse:
    description: Konferansen ein aktivitet høyrer til.
    class_uri: javazonetalk:Konferanse
    slots:
    - id
    - tittel
    - sted
```

pluss fem nye slots under `slots:`:

```yaml
  foredragsholder_ref:
    description: Referanse til foredragshaldaren for aktiviteten.
    range: Foredragsholder

  konferanse_ref:
    description: Referanse til konferansen aktiviteten høyrer til.
    range: Konferanse

  navn:
    description: Namnet på foredragshaldaren.
    range: string

  organisasjon:
    description: Organisasjonen foredragshaldaren representerer.
    range: string

  sted:
    description: Staden konferansen vert halden.
    range: string
```

**Viktig funn (opphavleg éin-klasse-utkast):** `id` og `tittel` treng
**ikkje** definerast lokalt — dei finst alt som globale slots via
`common-ap-no-schema` (transitivt importert via `dcat-ap-no-schema`).
Fyrste utkast freista å definere ein ny, lokal `tittel:`-slot med
`range: string` — det ville kollidert med den alt eksisterande globale
`tittel`-sloten (`slot_uri: dct:title`, `range: LangString`,
`multivalued: true`), same feilklasse som BUG-6/BUG-7
(`bugs/dqv-standard-class-override.md`,
`bugs/duplicate-slot-merge-konflikt.md`). Retta ved å **gjenbruke** den
importerte `tittel`-sloten i staden for å skugge han — stadfesta
kollisjonsfritt med ein reell `mcp-linkml-valider-modell`-køyring (dei
einaste attverande feila var pre-eksisterande DCAT-krav frå
silver-profilen, urelatert til Aktivitet-klassa).

**Utviding til tre relaterte klasser:** `navn`, `organisasjon`, `sted`,
`foredragsholder_ref` og `konferanse_ref` er stadfesta kollisjonsfrie
mot heile den transitive import-kjeda `dcat-ap-no-schema` ->
`common-ap-no-schema` + `dqv-core-schema` (statisk grep etter
tilsvarande slot-/klassenamn — **ikkje** ein reell
`mcp-linkml-valider-modell`-køyring denne gongen, sidan podman rootless
var utilgjengeleg i verktøymiljøet på verifiseringstidspunktet). Køyr
`make mcp-linkml-valider-modell SCHEMA=...` på det utvida skjemaet før
sjølve demo-dagen for å stadfeste kollisjonsfritt fullt ut.

### Fargelegging i scriptet

Kommandolinjene i `javazone-demo-script.sh` er no farga etter same
konvensjon som `make help` (jf. `src/assets/scripts/makefile/help.sh`):
`make <target>` i cyan (`CLR_STEP`), obligatoriske argument i grønt
(`CLR_OK`), valfrie argument i gult (`CLR_WARN`). T.d. viser steg 3
`DOMAIN`/`NAME` i grønt (begge obligatoriske for `new-modell`), medan
steg 7-10 sitt `DOMAIN=`/`SCHEMA=` er gult (valfrie for dei respektive
`analyse-*`/`gen-*`-targeta, sjølv om scriptet alltid oppgir dei).

## Offline-sjekkliste (køyr dagen før, medan nettverk er tilgjengeleg)

```bash
make check-prereqs                 # cacher alpine-imaget (podman rootless-testen)
make build-docker-linkml
make build-docker-python
make build-docker-mcp-modell-utkast
bash src/assets/scripts/demo/javazone-demo-script.sh  # byggjer demo-fun-tools automatisk (figlet/toilet/cowsay/lolcat/boxes) fyrste gong
make docs-publish && make docs-serve # test mkdocs OFFLINE etterpå (slå av nett, sjekk sidelasting)
# docs-publish (ikkje docs-build) er rett kombinasjon med docs-serve — han
# kopierer generated/-artefaktar inn i mkdocs/docs/ og genererer mkdocs.yml
# på nytt, slik at portalen faktisk viser noverande innhald. docs-serve
# renderer deretter direkte frå mkdocs/docs/ (treng ikkje docs-build først
# — det er eit alternativ til docs-serve, ikkje eit forsteg til han).
# publish.sh er reint lokale filoperasjonar, ingen nettverkskall.
```

Deretter: **kopla frå nettet**, og køyr heile det verifiserte scriptet
over éin gong til frå botnen, for å stadfeste at ingenting prøver å nå ut
på demo-maskina.

## mkdocs-portalen

Vis **éin** side, rett etter steg 3 (`new-modell`):
`mkdocs/docs/kom-i-gang/ny-domenemodell.md` — forklarer nett den
filstrukturen du har vist fram live. Ikkje fleire sidevekslingar — 10
minutt er stramt, og resten av demoen kretsar rundt kommandolinja.

## Opprydding etter demoen

Scriptet skriv til repoet tre stader:

```bash
rm -rf src/linkml/oreg/javazonetalk generated/oreg/javazonetalk
make update-valid-scopes
```

## Handlingsliste (brukaren sin eigen sjekkliste før demo-dagen)

1. [ ] Køyr offline-sjekklista (byggje/cache alle image, testa mkdocs offline)
2. [ ] Øv på steg 5 (live-redigering) — bestem eksakt kva slots som skal
   leggjast til under «Aktivitet», så det går raskt å skrive live
3. [ ] Øv på heile sekvensen med `javazone-demo-script.sh`, med klokke,
   heilt offline (kopla frå nettet)
4. [ ] Bestem om «Ny domenemodell»-sida skal opnast i ein ferdig fane på
   førehand (unngår tid brukt på å navigere live)
5. [ ] Etter demoen: bruk oppryddingsspørsmålet på slutten av
   `javazone-demo-script.sh`, eller køyr opprydding-kommandoane manuelt
