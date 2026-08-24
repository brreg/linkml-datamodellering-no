# Plan: effektiviser tidsbruken til modellanalyse-steget i generate-workflowen

## Bakgrunn

Brukaren observerer at "Køyr modellanalyse per skjema"-steget (og det nyare
"Køyr modellanalyse på tvers av domene"-steget) no tek klart mest tid i
heile `generate.yml`-workflowen, og ber om ein plan for å effektivisere
tidsbruken.

Dette er **same rotårsaksklasse** som `specs/done/effektiviser-generate-
workflow-koyretid.md` alt diagnostiserte og fiksa for generatorstega
(gen-shacl, gen-owl, gen-doc m.fl.): éin `podman run`-kontainar per
(skjema × sjekk)-kombinasjon, der import av `linkml`/`linkml_runtime`
(og for `find-similar-names.py` sin del: full re-parsing av alle skjema i
domenet) vert betalt på nytt for **kvart einaste** kontainarkall. Denne
specen brukar same metodikk (kvantifiser → batch → verifiser) på
modellanalyse-steget spesifikt — eit steg som ikkje fanst då den førre
specen vart skriven (det vart lagt til i
`specs/done/modellanalyse-per-skjema-index-md.md` og utvida monaleg i
`specs/done/modellanalyse-ubrukte-lokale-definisjonar.md`, begge etter at
den førre effektiviseringsspecen vart arkivert).

**Kva steget gjer i dag** (`.github/workflows/generate.yml`):

- Line 315-393, "Køyr modellanalyse per skjema for `${{ matrix.domain
  }}`": for kvart skjema i domenet, ein bash `for`-løkke som køyrer **8
  sekvensielle `make`-kall** — 3× `analyse-similar-*-domain` (`PYTHON_RUN`,
  `find-similar-names.py`) + 5× `analyse-ubrukte-*`/`analyse-isolerte-
  klasser` (`LINKML_RUN`, `find-unused-local-definitions.py`). Køyrer
  **før** "Generer alle artefakter for domenet" (line 394), heilt
  sekvensielt, ingen overlapp.
- Line 461+, "Køyr modellanalyse på tvers av domene" (i `publish`-jobben,
  éin gong for heile repoet): 3× `analyse-similar-*-all`-kall
  (`PYTHON_RUN`), same script, `--scope all` i staden for `--scope
  domain`.

## Funn — kvantifiserte målingar

Målt lokalt (WSL2/podman, varme image-lag, `localhost/linkml-local:latest`,
`localhost/python-pytest:latest`).

### 1) Kontainar-startup og import-skatt, isolert (same mønster som førre spec)

| Steg | Tid | Kommentar |
|---|---|---|
| Bar `linkml-local`-oppstart | ~1,0 s | |
| + `from linkml_runtime import SchemaView` | ~1,9 s | ~0,9 s importskatt |
| + `SchemaView(dcat-ap-no-schema.yaml).all_classes()` | ~2,2 s | ~0,3 s for sjølve import-oppløysinga |
| Bar `python-pytest`-oppstart | ~1,2 s | |

### 2) Full `make`-kall, dagens arkitektur

| Kommando | Tid | Rotårsak |
|---|---|---|
| 5× `analyse-ubrukte-*`/`analyse-isolerte-klasser` sekvensielt, `samt-bu` (lite skjema) | **9,8 s** | 5× (kontainaroppstart + import + SchemaView), same SchemaView-data burda vore delt |
| Same 5, `enhetsregisteret-bvrinn` (138 slots) | **13,2 s** | same |
| 3× `analyse-similar-*-domain` sekvensielt, `enhetsregisteret-bvrinn` (domene `oreg`, 9 skjema) | **15,8 s** | kvart kall les og `yaml.safe_load`-parsar **alle 9 skjema i domenet på nytt** — betalt 3× per skjema, altså 3×9=27× per domene |
| Éin isolert `analyse-similar-classes-domain`-invokering, same | **4,3 s** | ~1,2 s oppstart + ~3,1 s reindyrka O(N)-reparsing av domenet |

### 3) Rotårsak, splitta i to uavhengige problem

**A) `find-unused-local-definitions.py` (5 kindar) byggjer 5 separate
`SchemaView`-objekt for **same** skjema** — éin per `--kind`-kall, sjølv
om alle fem sjekkane kunne delt éitt `SchemaView`-objekt bygd éin gong.
Reint bortkasta ~4× (import + import-oppløysing) per skjema.

**B) `find-similar-names.py --scope domain` re-les og re-parsar **alle**
skjema i domenet via `yaml.safe_load` for **kvart** `--kind`- ×
`--name`-kall** — for eit domene med N skjema og 3 kindar, det gjev
**O(3N²)** yaml-parsingar totalt (ikkje O(3N) som talet på rapportfiler
skulle tilseie), sidan kvart kall diskoverer og lastar heile domenet på
nytt uavhengig av `--name`-filteret. For `oreg` (N=9) er det **243
skjema-innlastingar** for å produsere 27 rapportfiler.

Container-startup (problem, men mindre enn A/B) kjem i tillegg til begge.

## Kartlegging — kontainar-kall i dag, skalert til heile repoet

43 skjema fordelt på 9 domene:

| Domene | Skjema | `analyse-ubrukte-*`/`isolerte-klasser`-kall (5×N) | `similar-*-domain`-kall (3×N) | Sum kontainarkall |
|---|---|---|---|---|
| ap-no | 10 | 50 | 30 | 80 |
| oreg | 9 | 45 | 27 | 72 |
| fint | 7 | 35 | 21 | 56 |
| modellkatalog | 6 | 30 | 18 | 48 |
| ngr | 4 | 20 | 12 | 32 |
| referanse | 4 | 20 | 12 | 32 |
| begrepskatalog | 1 | 5 | 3 | 8 |
| fair | 1 | 5 | 3 | 8 |
| samt | 1 | 5 | 3 | 8 |
| **Sum** | **43** | **215** | **129** | **344** |

Pluss 3 kontainarkall for `--scope all`-steget (éin gong, ikkje per
domene). **347 sekvensielle `podman run`-kall totalt**, spreidd på 9
domene-matrisejobbar (parallelle med kvarandre, men strengt sekvensielle
**innanfor** kvar jobb). Verste enkelt-jobb: `ap-no` (80 kall) og `oreg`
(72 kall, og dei desidert tyngste skjemaa — `enhetsregisteret-bvrinn` har
138 slots).

Estimert dagens tidsbruk for `oreg` sitt modellanalyse-steg åleine (basert
på målingane over, midla over 9 skjema av varierande storleik): grovt
**5-8 minutt**, heilt sekvensielt, **før** sjølve artefaktgenereringa i
det heile har starta.

## Tiltak (prioritert etter forventa gevinst / risiko)

### Tiltak 1 — Del eitt `SchemaView` mellom dei fem `--kind`-sjekkane per skjema

**Omfattar:** `find-unused-local-definitions.py`.

`main()` (line 238+) og `render_report()` (line 210+) må endrast slik at
`render_report` **returnerer** ein streng i staden for å `print()`e
direkte, og ein ny funksjon (t.d. `run_all_kinds(schema_path, out_dir)`)
bygg **eitt** `SchemaView` og kallar dei alt-eksisterande, reint
funksjonelle `find_unused(sv, kind)`/`find_isolated_classes(sv)` for alle
fem kindane, og skriv kvart resultat til si eiga fil i `out_dir` med
**akkurat dei same filnamna** generate.yml alt brukar
(`ubrukte-slots-report.md` osv., sjå line 315-393) — slik at
`generate-modellanalyse-md.py`/`mkdocs/publish.sh` ikkje treng endrast i
det heile.

CLI: legg til `--kind all --out-dir <sti>` som eit nytt, valfritt modus
(dei eksisterande `--kind <kind> --schema <sti>`-kalla, som skriv til
stdout, skal halde fram uendra for manuell/enkelt-sjekk-bruk).

**Makefile:** nytt target (t.d. `analyse-lokal-modellanalyse SCHEMA=<sti>
OUT_DIR=<sti>`) som wrappar `--kind all --out-dir`. Behald dei fem
eksisterande `analyse-ubrukte-*`/`analyse-isolerte-klasser`-targeta
uendra for utviklarar som vil køyre éin enkelt sjekk lokalt.

**`generate.yml`:** dei fem `make analyse-ubrukte-*`/`analyse-isolerte-
klasser SCHEMA=...`-kalla i "Køyr modellanalyse per skjema"-steget (line
315-393) vert til **eitt** `make analyse-lokal-modellanalyse SCHEMA=...
OUT_DIR=...`-kall. **Køyr `actionlint` mot `generate.yml`** etter
endringa.

**Forventa gevinst:** ~13 s → ~2,5 s per skjema (målt: import+SchemaView
~2,2 s + fem billige in-memory-sjekkar). For heile repoet (43 skjema):
frå ~215 kontainarkall/~9-10 min CPU-tid til 43 kontainarkall/~1,8 min.

**Risiko:** Låg. Alle fem sjekk-funksjonane (`find_unused`,
`find_isolated_classes`) er alt reint funksjonelle og tek `sv` som
parameter — ingen ny algoritme, berre gjenbruk av eit alt bygd
`SchemaView`-objekt.

### Tiltak 2 — Batch `find-similar-names.py --scope domain` til éin prosess per domene

**Omfattar:** `find-similar-names.py`.

I dag diskoverer/lastar scriptet **heile domenet på nytt** for kvart
`--name`-filtrert kall. Refaktorer slik at domenet sine `entries` (for
kvar av dei tre kindane: class/slot/types) vert lasta **éin gong**, og
scriptet deretter løkkjer over **alle** skjema i domenet internt og
skriv **éi rapportfil per skjema** (same filnamn/format som i dag),
i staden for å bli kalla éin gong per (skjema × kind).

Konkret: eit nytt modus, t.d. `--scope domain --domain <domene> --out-dir
<sti> --write-per-schema`, som for kvar av dei tre kindane (1) lastar
`entries` éin gong (alt eksisterande `discover_schemas()`+`load_entries()`
frå line 44-75), (2) reknar ut matches éin gong (alt eksisterande
løkke, line 165-179), og (3) for kvart skjema i domenet, filtrerer
`matches` til dei som gjeld nett det skjemaet og skriv
`<domain-dir>/<schema>/similar-<kind>-domain-report.md` — **same
filnamn/sti-mønster** `generate.yml` alt forventar. Dei eksisterande
`--kind/--scope/--domain/--name`-flagga (stdout-modus) skal halde fram
uendra for manuell bruk og for `modell-analyse.yml` (som framleis brukar
`--scope all` per kind, sjå Tiltak 4).

**`generate.yml`:** dei tre × N `make analyse-similar-*-domain DOMAIN=...
NAME=...`-kalla i "Køyr modellanalyse per skjema"-steget vert til **tre**
kall totalt (éin per kind, ikkje per skjema) —
`make analyse-similar-classes-domain-batch DOMAIN=${{ matrix.domain }}
OUT_DIR=generated/${{ matrix.domain }}` (og tilsvarande for slots/types).

**Forventa gevinst:** størst for domene med mange skjema. `oreg` (N=9):
frå 27 kall/~116 s (målt) til 3 kall/~5-8 s (import+parse 9 skjema éin
gong per kind, ikkje 27 gongar). Domene med berre 1 skjema (samt,
begrepskatalog, fair) har ikkje O(N²)-problemet i utgangspunktet, men
sparar framleis kontainar-oppstart (3 kall → framleis 3 kall, men utan
gevinst der — sjå Tiltak 4 for korleis dette likevel kan slåast saman på
tvers av kind seinare om ønskt).

**Risiko:** Moderat. Matching-algoritmen (line 165-179) er uendra —
einaste endring er **kva som skjer med resultatet** (skriv N filer i
staden for å filtrere til éin `--name` og printe). Verifiser at
per-skjema-utdataen er **identisk** (byte-for-byte) mot dagens
`--name`-filtrerte kall for eit representativt utval skjema, særleg eit
domene med mange skjema (`oreg`) og eit med berre eitt (`samt`).

### Tiltak 3 — Konsolider heile "Køyr modellanalyse per skjema"-steget til to batch-kall per domene

Byggjer direkte på Tiltak 1 + 2: erstatt heile bash `for`-løkka (line
315-393) med **to** kall totalt per domene (eitt `LINKML_RUN`, eitt
`PYTHON_RUN` — kan ikkje slåast saman til éitt sidan dei krev ulike
kontainarbilete):

```
make analyse-lokal-modellanalyse-domene DOMAIN=${{ matrix.domain }}   # LINKML_RUN, alle skjema × 5 kindar
make analyse-similar-domene            DOMAIN=${{ matrix.domain }}   # PYTHON_RUN, alle skjema × 3 kindar
```

Reduserer kontainarkall per domene frå opptil **80** (ap-no) til
**nøyaktig 2**, uavhengig av domenestorleik. Dei to kan køyrast som
bakgrunnsprosessar (`&`/`wait`) sidan dei er heilt uavhengige av kvarandre
(ulike script, ulike bilete, ulike output-filer) — enkel, låg-risiko
parallellitetsgevinst attpå batching-gevinsten, same mønster som
`mkdocs/publish.sh` alt brukar fleire stader.

**Risiko:** Låg, gitt at Tiltak 1+2 er verifiserte kvar for seg først —
dette er berre samankopling av dei to, pluss `&`/`wait`.

### Tiltak 4 — Batch `--scope all`-steget (3 kall) med same refaktorering

Gjenbruk funksjonen frå Tiltak 2 (berre med `--scope all` i staden for
`--domain <x>`) for "Køyr modellanalyse på tvers av domene"-steget i
`publish`-jobben (line 461+). Låg isolert gevinst (berre 3 kall totalt,
køyrer éin gong for heile repoet) — teke med for konsistens og fordi
refaktoreringa frå Tiltak 2 gjer det nesten gratis.

**Risiko:** Låg.

### Tiltak 5 (vurder etter måling, ikkje eit umiddelbart tiltak) — Køyr modellanalyse-steget parallelt med artefaktgenerering

I dag køyrer "Køyr modellanalyse per skjema" (line 315-393) **før**
"Generer alle artefakter for domenet" (line 394), heilt sekvensielt,
sjølv om dei er uavhengige (modellanalyse les berre `src/linkml/`,
artefaktgenereringa les òg berre `src/linkml/` — ingen av dei er
avhengige av kvarandre sin output). Etter Tiltak 1-3 er modellanalyse-
steget venteleg langt kortare enn artefaktgenereringa (som i seg sjølv
tek fleire minutt per domene, jf. `specs/done/effektiviser-generate-
workflow-koyretid.md`), så den attverande gevinsten ved å bakgrunne
modellanalyse-steget bak artefaktgenereringa kan vere marginal.
**Anbefaling:** mål reell CI-tid etter Tiltak 1-3 er på plass. Berre
invester i denne omlegginga (bakgrunnsprosess + wait, med tydeleg
logging så steg-rekkjefølgja framleis er lesbar i CI-loggen) dersom
modellanalyse framleis er synleg på den kritiske stien.

## Handlingsliste (implementeringsrekkjefølgje)

1. Tiltak 1 — størst isolert gevinst per skjema, lågast risiko, rører
   berre `find-unused-local-definitions.py` + eitt nytt Makefile-target
2. Tiltak 2 — størst gevinst for store domene (`ap-no`, `oreg`), krev
   forsiktig refaktorering av `find-similar-names.py` med eksplisitt
   byte-for-byte-verifisering
3. Tiltak 3 — konsolider til to kall per domene, bygg direkte på 1+2,
   legg til `&`/`wait`
4. Tiltak 4 — gjenbruk Tiltak 2 sin refaktorering for `--scope all`
5. Tiltak 5 — **berre** etter måling i reell CI viser at steget framleis
   er synleg tungt

**Verifiseringsdisiplin for kvart tiltak** (same krav som referansespecen):
samanlikn genererte rapportfiler **innhaldsmessig identiske** (ikkje
berre "ser fornuftige ut") mot dagens sekvensielle køyring, for minst eitt
lite domene (samt/fair/begrepskatalog) og eitt stort (ap-no/oreg), før
neste tiltak byggjer vidare. `make gen-schema-docs` + `make docs-publish`
+ `make docs-build` skal framleis produsere identisk `## Modellanalyse`-
innhald i genererte `index.md`-sider (inkl. funntala frå
`specs/done/modellanalyse-antal-i-deloverskrifter.md`).

## Opne spørsmål (avklar ved implementering, ikkje i denne specen)

- Eksakt namngjeving på dei nye Makefile-targeta/CLI-flagga (`--kind all`,
  `analyse-lokal-modellanalyse-domene` osv.) — forslaga over er
  arbeidsnamn, juster ved implementering for konsistens med
  `make/91-modell-analyse.mk` sin eksisterande namnekonvensjon.
- Skal dei fem/tre eksisterande **per-skjema**-Makefile-targeta
  (`analyse-ubrukte-slots SCHEMA=...` osv.) behaldast som dokumenterte,
  brukarvendte kommandoar (jf. `COMMANDS.md`) sjølv etter at CI sluttar å
  bruke dei direkte, eller bør dei markerast som "intern/utvikling-berre"?
  Anbefaling: behald dei — dei er framleis nyttige for ein utviklar som
  vil sjekke berre éitt skjema/éin kind lokalt utan å køyre heile
  domene-batchen.

## Utført

Tiltak 1-4 gjennomførte i éin samla omgang (ikkje landa stegvis med
CI-måling mellom kvart, sidan alt vart verifisert lokalt med reelle
tidsmålingar før/etter — sjå under). Tiltak 5 er **ikkje** gjort, i tråd
med spec-en sin eigen anbefaling om å vente på CI-måling.

**Endra filar:**

1. `src/assets/scripts/makefile/find-unused-local-definitions.py`
   (Tiltak 1+3, LINKML_RUN-sida): `render_report()` → `format_report()`
   (returnerer streng), ny `compute_items_and_total()` (delt kode), ny
   `process_schema_all_kinds()` (eitt SchemaView, alle fem kindar) og
   `process_domain()` (diskoverer skjema, løkkjer, per-skjema
   feilisolasjon). Nytt CLI-modus `--domain <d> --out-dir <sti>`. Det
   eksisterande `--kind <k> --schema <sti>`-stdout-moduset er **uendra**
   (ingen ny "éin-skjema-alle-kindar"-mellomting vart lagt til — Tiltak 3
   sitt domene-batch-modus dekte CI-behovet fullt ut åleine, så eit
   ekstra CLI-lag ville vore ubrukt overflate).
2. `src/assets/scripts/makefile/find-similar-names.py` (Tiltak 2+3+4,
   PYTHON_RUN-sida): kjernematching (`compute_matches()`) og formatering
   (`build_report()`, `_fmt_schema/_fmt_range/_fmt_slots`) trekt ut til
   modulnivå-funksjonar (var før inline/lokale closures i `main()`).
   `main()` sitt eksisterande `--kind --scope [--domain] [--name]`-
   stdout-modus er **uendra åtferd**, berre omskrive til å kalle dei
   delte funksjonane. Nytt CLI-modus `--out-dir <sti> [--domain <d>]`
   (batch, skriv fil(er) i staden for stdout).
3. `make/91-modell-analyse.mk`: tre nye target —
   `analyse-lokal-modellanalyse-domene`,
   `analyse-similar-domene-batch`, `analyse-similar-alle-domene-batch`.
   Dei ni eksisterande targeta (tre `similar-*-domain`/`-all`, fem
   `ubrukte-*`/`isolerte-klasser`) er **uendra**.
4. `.github/workflows/generate.yml`: "Køyr modellanalyse per skjema"-
   steget (var ein bash-løkke med opptil 8×N `make`-kall) er no to
   batch-kall (`analyse-similar-domene-batch` +
   `analyse-lokal-modellanalyse-domene`) køyrde parallelt via `&`/`wait`
   (Tiltak 3). "Køyr modellanalyse på tvers av domene"-steget er no eitt
   kall (`analyse-similar-alle-domene-batch`, Tiltak 4). `actionlint`
   køyrd og godkjend (reint, ingen funn) etter begge endringane.

**Verifisert reelt** (sandbox deaktivert for podman, same grunn som dei
to førre spec-ane i denne serien):

- **Byte-for-byte identisk output** stadfesta for begge script sitt
  eksisterande stdout-CLI (uendra flagg): `find-unused-local-
  definitions.py` sine fem kindar for eit stort skjema (`enhetsregisteret-
  bvrinn`, 138 slots), og `find-similar-names.py` for både
  target_path-grena (`--name`) og heile-repoet-grena (`--scope all`, ingen
  `--name`).
- **Byte-for-byte identisk output** stadfesta for dei NYE batch-modusa
  sine skrivne filer mot tilsvarande gamle enkelt-kall, for fleire skjema
  i `oreg` (både `find-unused-local-definitions.py` sine fem
  kind-rapportar og `find-similar-names.py` sine tre kind-rapportar).
- **Målt tidsbruk, `oreg`-domenet** (9 skjema, det klart tyngste domenet):
  - Lokal-analyse (5 kindar): **~13 s/skjema sekvensielt** (målt i
    "Funn"-seksjonen over) → **11,4 s for heile domenet batcha** (eitt
    kall, 45 kombinasjonar).
  - Similar-domain (3 kindar): **73,2 s** for 27 sekvensielle kall (målt
    direkte) → **14,7 s batcha** (eitt kall).
  - Sidan dei to batch-kalla no køyrer **parallelt** (`&`/`wait`) i staden
    for etter kvarandre, er den reelle veggklokke-gevinsten for heile
    "Køyr modellanalyse per skjema"-steget på `oreg` estimert til
    **~190 s sekvensielt (før) → ~15 s parallelt batcha (etter)**, ein
    ~12-13× reduksjon for det verste enkeltdomenet.
  - Cross-domain `--scope all` (Tiltak 4, 43 skjema, alle tre kindar i
    éin prosess): **31,8 s**, korrekt innhald stadfesta mot stdout-modus.
- **Full pipeline**: `make docs-publish` + `make docs-build` køyrd med
  reelt genererte rapportar for `samt`- og `oreg`-domena (inkl. tidlegare
  `dcat-ap-no`-data) — genererte `index.md`-sider viser korrekte funntal
  (t.d. `enhetsregisteret-bvrinn` fekk reelle `(61)`/`(252)`/`(63)`-
  namnelikskapstal og `(1)` ubrukt subset, `dcat-ap-no` sitt tidlegare
  stadfesta `(2)` ubrukte slots uendra). `docs-build` sin
  `validation.links`-sjekk framleis grøn, ingen nye åtvaringar.
  `make roundtrip SCHEMA=dcat-ap-no-schema.yaml` — 2 OK, 0 feil (ingen
  regresjon i sjølve skjemagenereringa, som venta sidan ingen av desse
  endringane rører generatorpipelinen).

**Avvik frå opphavleg plan:**
- Tiltak 1 vart implementert direkte som del av Tiltak 3 sitt
  domene-batch-modus (`process_domain()`), utan eit separat
  mellomsteg-CLI for "éin skjema, alle fem kindar" — sjå punkt 1 over.
  Ingen funksjonell skilnad frå planen, berre eitt mindre steg i
  implementeringsrekkjefølgja.
- Tiltak 5 (parallelt med artefaktgenerering) er **ikkje** gjort, per
  spec-en sin eigen instruks om å vente på CI-måling. Modellanalyse-
  steget køyrer framleis før "Generer alle artefakter"-steget, men er no
  sjølv internt parallellisert (dei to batch-kalla).
