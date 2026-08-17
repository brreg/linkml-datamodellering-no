# Evaluering: fleire skjema i éin modellkatalog (submodels-mekanismen)

## Bakgrunn

Brukaren ber om ei evaluering av at fleire skjema ligg i same modellkatalog:
`modelldcat-ap-no` (3 skjema: `modelldcat-ap-no`, `modelldcat-katalog`,
`modelldcat-modell`) og `dqv-ap-no` (2 skjema: `dqv-ap-no`, `dqv-core`).
Spørsmåla er:

1. Bryt dette med konvensjonen om éin modell per modellkatalog, og er det greit?
2. Fører spesialbehandlinga dette medfører til unødig kompleksitet/feilrisiko?
3. Treng vi eit tredje grupperingsnivå (mellom domene og modell) for betre gruppering?

Dette er ei rein evaluering — ingen kodeendring er bestilt.

## Funn

### 1. Er dette eit brot på ein dokumentert konvensjon?

Det finst **ingen eksplisitt regel** i PRINCIPLES.md, SCOPE.md eller
CONVENTIONS.md som seier "éin modell per katalog". Konvensjonen er implisitt,
avleidd frå katalogmønsteret `src/linkml/<domain>/<modell>/<modell>-schema.yaml`
(CONVENTIONS.md § Fil- og mappenavn) og frå at `make new-modell` skaper éin
katalog per modell.

Repoet har derimot eit **eksplisitt, dokumentert unntaksfelt**: `submodels:` i
`build.yaml` (dokumentert i `mkdocs/docs/kom-i-gang/build-config.md` §
`submodels`). Feltet dekkjer to legitime bruksområde, verifisert i skjemaa:

- **Sirkulær-import-unngåing** (`dqv-core`): `dcat-ap-no-schema.yaml` importerer
  `../dqv-ap-no/dqv-core-schema`, og `dqv-ap-no-schema.yaml` importerer
  `../dcat-ap-no/dcat-ap-no-schema`. Utan eit nøytralt tredjeskjema ville dette
  vore ein direkte sirkulær import mellom `dcat-ap-no` og `dqv-ap-no`, som
  PRINCIPLES.md §3 eksplisitt forbyr ("Skjema importerer frå eit klart
  hierarki — aldri på tvers eller nedover ... Grunngiving: Hindrar sirkulær
  import"). `dqv-core` er difor ei arkitektonisk naudsynt løysing, ikkje ei
  bekvemmelegheit.
- **Logisk separasjon av spesifikasjonsdelar** (`modelldcat-modell` /
  `modelldcat-katalog`): importkjeda her er lineær
  (`modelldcat-ap-no` → `modelldcat-katalog` → `modelldcat-modell` →
  `dcat-ap-no`), ikkje sirkulær. Splitten følgjer den offisielle
  ModelDCAT-AP-NO-spesifikasjonen sin eigen Modell-del/Katalog-del-struktur,
  og er difor eit organisatorisk val i tråd med modularitetsprinsippet
  (PRINCIPLES.md §3), ikkje eit påtvinga unntak.

**Konklusjon:** Dette er ikkje eit brot på ein formell regel (fordi regelen
ikkje finst formelt), men det er lett å *oppfatte* det som eit brot fordi
"éin modell per katalog" berre kan lesast ut av katalogstrukturen, ikkje av
noko dokument. `submodels:`-mekanismen er sjølv den dokumenterte
unntaksregelen.

### 2. Kva kostnad har spesialbehandlinga?

**Der ho ikkje kostar noko:** Byggverktøy (`make lint`, `make test`, `make
roundtrip`, `make mcp-linkml-valider-modell` osv.) tek alle `SCHEMA=<sti til
enkeltfil>`, ikkje katalog — dei er difor heilt upåverka av at fleire skjema
deler katalog. `.github/valid-scopes.txt` listar `dqv-core`,
`modelldcat-katalog` og `modelldcat-modell` som eigne, sjølvstendige
commit-scope på lik linje med toppnivåmodellar. `make remove-modell` har ein
eigen blokkerande sjekk mot `submodels:`-referansar, så deling av katalog kan
ikkje utilsikta bryte ein delmodell.

**Der ho kostar noko:** Spesialbehandlinga er konsentrert til
dokumentasjonsgenereringa (`mkdocs/publish.sh`,
`mkdocs/lib/sections/delmodellar.sh`, `generate_index.sh`,
`generated_artifacts.sh`, `datamodell.sh`) og til
`generate-informasjonsmodell.py` (`har_del`-felt). Historikken viser fleire
separate retterundar knytte direkte til denne handteringa:
`delmodell-spesialtilpassing.md`, `delmodell-dokumentasjon.md`,
`nye-host-python-kall-batching.md`, `reduser-podman-kall-docs-publish.md`,
`stille-feil-batching-regresjon.md`. Minst éin av desse (`
delmodell-spesialtilpassing.md`) dokumenterer ein bug som oppstod "per
tilfeldigheit" — `description.md` frå hovudmodellen vart vist på
delmodellsida fordi eit `find`-oppslag søkte i heile domenekatalogen i staden
for berre skjemaets eigen katalog.

**Vurdering:** Kostnaden er reell, men avgrensa i omfang — 3 av ca. 41 skjema
(~7 %) er delmodellar, og alle spesialtilfelle er isolerte til
dokumentasjonslaget. Kjernefunksjonalitet (lint, validering, versjonering,
build) er urørt.

### 3. Treng vi eit tredje grupperingsnivå (domene → modellgruppe → modell)?

**Vurdering: Nei, ikkje no.**

- Berre 1 av 20 domenekatalogar (`ap-no`) har dette behovet i dag, og berre 3
  skjema totalt er involverte.
- Eit generelt tredje nivå ville krevje å endre katalogstien
  (`<domain>/<modell>/` → `<domain>/<modellgruppe>/<modell>/`) for **alle**
  ~41 skjema, ikkje berre dei 3 som treng gruppering i dag — det påverkar
  `new-modell`-scaffolding, `valid-scopes.txt`-generering, mkdocs
  nav-menyoppbygging, gen-doc-stiar og alle Makefile-targets som i dag
  antek `<domain>/<modell>/` som fast dybde.
- Kostnaden ved å innføre eit generelt nivå for eit behov som i dag gjeld 7 %
  av skjemaa er difor vesentleg større enn kostnaden ved dagens punktvise
  `submodels:`-mekanisme, som løyser akkurat det volumet som finst.

## Tilråding

1. **Behald `submodels:`-mekanismen som ho er.** Ikkje innfør eit tredje
   grupperingsnivå — det løyser eit problem som i dag berre gjeld to
   modellkatalogar, til ein kostnad som råkar alle.
2. **Gjer den implisitte konvensjonen eksplisitt** i CONVENTIONS.md: legg til
   ei kort formulering om at éin katalog normalt svarar til éin modell, med
   `submodels:` (kryssreferanse til `build-config.md`) som det einaste
   dokumenterte unntaket, avgrensa til sirkulær-import-unngåing og logisk
   spesifikasjonsseparasjon. Dette fjernar tvitydigheita som truleg er kjelda
   til at spesialbehandlinga vert opplevd som eit brot.
3. **Ingen refaktorering av `publish.sh`/`mkdocs/lib/` no.** Churnen i
   historikken er reell, men volumet (3 skjema) rettferdiggjer ikkje ei
   konsolidering per no. Bør revurderast dersom talet på delmodellar veks
   utover eit fjerde–femte tilfelle.

## Handlingsliste

- [x] Legg til eksplisitt formulering i CONVENTIONS.md om
      éin-modell-per-katalog-konvensjonen og `submodels:`-unntaket
- Ingen andre kodeendringar tilrådd

## Utført

Evalueringa er fullført (funn og tilråding over). CONVENTIONS.md § "Fil- og
mappenavn" er utvida med eit avsnitt "Éin modell per katalog" som gjer den
tidlegare implisitte konvensjonen eksplisitt, med kryssreferanse til
`submodels:`-feltet i `build-config.md` og dei to godkjende bruksområda
(sirkulær-import-unngåing og logisk spesifikasjonsseparasjon).
