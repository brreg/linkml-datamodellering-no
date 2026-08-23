# Ny modellanalyse-sjekk: liknande navn på LinkML `types:` (eigendefinerte scalar-typar)

## Bakgrunn

Brukaren ønskjer ein ny modellanalyse-job som avdekkjer om det finst
skjema som definerer eigne LinkML `types:`-scalar-typar (t.d.
`Versjonsnummer`, `Orgnummer`) med matchande/liknande navn, på tvers av
domene og på tvers av heile repoet.

### Kva finst frå før

`src/assets/scripts/makefile/find-similar-names.py` (kalla av
`make/91-modell-analyse.mk` og køyrt vekentleg i
`.github/workflows/modell-analyse.yml`, jf. `specs/done/modell-analyse-workflow.md`)
finn allereie liknande **klassenavn** og **slotnavn**, både innanfor same
domene (`--scope domain`) og på tvers av alle domene (`--scope all`):

| Target | `--kind` | `--scope` |
|---|---|---|
| `analyse-similar-classes-domain` | `class` | `domain` |
| `analyse-similar-classes-all` | `class` | `all` |
| `analyse-similar-slots-domain` | `slot` | `domain` |
| `analyse-similar-slots-all` | `slot` | `all` |

`find-similar-names.py` sitt `--kind`-flagg støttar i dag **berre**
`class`/`slot` (`choices=["class", "slot"]`) — eigendefinerte scalar-typar
under kvart skjema sin toppnivå `types:`-blokk vert **ikkje** samanlikna.
8 skjema definerer i dag ein eigen `types:`-blokk:

```
src/linkml/ap-no/common-ap-no/common-ap-no-schema.yaml
src/linkml/oreg/enhetsregisteret-bvrbekreftelse/
src/linkml/oreg/enhetsregisteret-bvrettersendingavvedlegg/
src/linkml/oreg/enhetsregisteret-bvrfriv/
src/linkml/oreg/enhetsregisteret-bvrinn/
src/linkml/oreg/enhetsregisteret-bvrinnfelles/
src/linkml/oreg/enhetsregisteret-bvrstiftelsesdokument/
src/linkml/oreg/enhetsregisteret-frivilligorganisasjonapi/
```

Kvar type-oppføring har forma (jf.
`enhetsregisteret-bvrinn-schema.yaml`):

```yaml
types:
  Versjonsnummer:
    uri: xsd:string
    base: str
    description: 'TODO: beskriv typen'
    pattern: ^(\d+\.)?(\d+\.)?(\*|\d+)$
```

`base` er type-blokka sin strukturelle analog til `range` på eit slot —
begge fortel kva den fuzzy-matcha namnelikskapen faktisk representerer
(same grunntype vs. berre eit namnesamantreff).

## Avklart med brukar

Spurt om «typer» i førespurnaden meiner LinkML `types:`-scalar-typar eller
klasser i vid forstand — brukaren stadfesta **`types:`-blokka**. Klasse- og
slot-sjekkane finst alt (tabellen over) og er ikkje del av denne spec-en.

## Design

Følgjer nøyaktig det etablerte mønsteret for `class`/`slot` — **ingen ny
arkitektur**, berre ein tredje `--kind`-verdi kopla gjennom dei same laga.

### 1. `find-similar-names.py`

- Legg `"types"` til `--kind`-choices: `choices=["class", "slot", "types"]`
- `load_entries()`: `key = {"class": "classes", "slot": "slots", "types": "types"}[kind]`.
  For `slot` og `types` er dataforma identisk — `(navn, ein valfri
  strengverdi, skjema)` — så begge kan dele éin gren: hent `range` for
  `slot`, `base` for `types`
- `main()`: legg `"types"` til `label`/`name_label`-oppslaget (`"typer"` /
  `"typenamn"`)
- Tabell-utskrift: `slot` og `types` deler same kolonnestruktur
  (namn/grunntype/skjema × 2) — berre kolonneoverskriftene skil seg
  (`Slot`/`Type` vs. `Type`/`Grunntype`, for å unngå at ordet «Type» tyder
  to ulike ting i same tabell)
- Oppdater modulens docstring til å nemne `types:` i tillegg til
  `classes:`/`slots:`

### 2. `make/91-modell-analyse.mk`

Nye target, same mønster som `analyse-similar-classes-*`:

```make
analyse-similar-types-domain: ## Finn typar (types:) med liknande navn innanfor same domene [DOMAIN=<domene>] [NAME=<modell>] [SIMILARITY_THRESHOLD=0.8]
	$(call print_header,analyse-similar-types-domain) 1>&2
	@$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/find-similar-names.py \
	  --kind types --scope domain --threshold $(SIMILARITY_THRESHOLD) $(if $(DOMAIN),--domain $(DOMAIN)) $(if $(NAME),--name $(NAME))

analyse-similar-types-all: ## Finn typar (types:) med liknande navn på tvers av alle domene [DOMAIN=<domene>] [NAME=<modell>] [SIMILARITY_THRESHOLD=0.8]
	$(call print_header,analyse-similar-types-all) 1>&2
	@$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/find-similar-names.py \
	  --kind types --scope all --threshold $(SIMILARITY_THRESHOLD) $(if $(DOMAIN),--domain $(DOMAIN)) $(if $(NAME),--name $(NAME))
```

Legg dei til i `.PHONY`-lista øvst i fila.

### 3. `.github/workflows/modell-analyse.yml`

To nye jobbar, kopi av `similar-classes-domain`/`similar-classes-all`
(same steg-mønster: sjekk ut, bygg python-container, køyr, skriv til
`$GITHUB_STEP_SUMMARY`, last opp artefakt):

- `similar-types-domain` → `analyse-similar-types-domain` →
  `similar-types-domain-report.md`
- `similar-types-all` → `analyse-similar-types-all` →
  `similar-types-all-report.md`

Legg begge til i `sammendrag`-jobbens `needs:`-liste.

### 4. `summarise-modell-analyse.py`

Legg to nye rader til `CHECKS`:

```python
("Liknande typenamn (same domene)", "similar-types-domain-report.md", "similar"),
("Liknande typenamn (alle domene)", "similar-types-all-report.md", "similar"),
```

Oppdater docstringen sitt «dei seks rapportfilene» → «dei åtte
rapportfilene» (og lista under).

### 5. `COMMANDS.md` § «Modell-analyse»

Legg til dei to nye targeta i target-tabellen, same rad-format som
`analyse-similar-classes-*`/`analyse-similar-slots-*`.

### 6. Per-skjema embedding i `index.md`

`## Modellanalyse`-seksjonen i kvar modell sin genererte `index.md`
(jf. `specs/done/modellanalyse-per-skjema-index-md.md`) viser i dag dei to
`domain`-scopa sjekkane for klasse- og slotnamn, køyrt per skjema med
`NAME=<skjema>` og skrive til `generated/<domain>/<schema>/model-analyse/`.
Same cache-korrektheitsgrunngjeving frå den arkiverte spec-en gjeld
uendra for `types` — berre `domain`-scope (aldri `all`) skal embeddast
per skjema, sidan `generated/<domain>/` er cacha på ein nøkkel utleia av
`hashFiles('src/linkml/<domain>/**')` og difor berre trygt kan spegle
funn **innanfor** same domene.

Konkret, to endringar i det etablerte per-skjema-laget:

- **`.github/workflows/generate.yml`** — steget «Køyr modellanalyse per
  skjema for `${{ matrix.domain }}`» får ei tredje linje i loopen, same
  mønster som dei to eksisterande:

  ```yaml
  make analyse-similar-types-domain DOMAIN=${{ matrix.domain }} NAME="$schema_name" \
    > "$out/similar-types-domain-report.md" \
    || echo "::warning::analyse-similar-types-domain feila for $schema_name"
  ```

  Ingen endring i cache-nøkkel eller `on.push.paths` er naudsynt her —
  `find-similar-names.py` og `make/91-modell-analyse.mk` er alt del av
  kallgrafen sidan den arkiverte spec-en (steg 2-3 der), og denne endringa
  legg berre til eit tredje `--kind`-kall på same, alt inkluderte script.

- **`mkdocs/lib/scripts/generate-modellanalyse-md.py`** — legg ei tredje
  oppføring til `REPORTS`-lista, og legg samstundes til eit tredje
  tuppel-element (`objekttype`, brukt til den nye per-seksjons-fotnoten,
  sjå punkt 7): `REPORTS` vert då

  ```python
  REPORTS = [
      ("similar-classes-domain-report.md", "Liknande klassenamn (same domene)", "klassenamn"),
      ("similar-slots-domain-report.md", "Liknande slotnamn (same domene)", "slotnamn"),
      ("similar-types-domain-report.md", "Liknande typenamn (same domene)", "typenamn"),
  ]
  ```

  Ingen andre endringar i sjølve rapport-innhentinga er naudsynte — loopen
  over `REPORTS` handterer den nye fila automatisk, inkludert graceful
  fallback («Rapport ikkje tilgjengeleg for denne bygginga») for skjema
  som manglar fila, og — via `find-similar-names.py` sin eksisterande
  «Ingen typer over terskelen vart funne (0 typer sjekka)»-utskrift — for
  dei mange skjemaa som ikkje definerer nokon eigen `types:`-blokk i det
  heile. Ingen spesialhandtering trengst for skjema utan `types:`.

`mkdocs/lib/sections/modellanalyse.sh` og `get_model_analyse_dir()` i
`metadata_parsers.sh` treng **ingen** endring — dei er alt kind-agnostiske
(dei peikar berre til katalogen, formateringa skjer i
`generate-modellanalyse-md.py`).

### 7. Per-seksjon-fotnote til den vekentlege cross-domain-jobben

I dag (jf. `specs/done/modellanalyse-per-skjema-index-md.md`) har heile
`## Modellanalyse`-seksjonen **éin** avsluttande fotnote nedst, som dekkjer
IRI-dereferering, innhaldsforhandling **og** cross-domain-samanlikning
samla:

```python
lines += [
    "",
    f"*For IRI-dereferering, innhaldsforhandling og samanlikning på tvers av *"
    f"*alle domene sjå *"
    f"*[Modell-analyse]({MODELL_ANALYSE_WORKFLOW_URL})-workflowen. *",
]
```

Brukaren ønskjer i staden at **kvar `###`-underseksjon** (klassenamn,
slotnamn, typenamn) får sin **eigen** kursiv fotnote som peikar til den
vekentlege, tverrgåande `modell-analyse.yml`-workflowen for akkurat den
objekttypen — ikkje éin delt fotnote nedst for alle tre. Endringa gjeld
difor **alle tre** `REPORTS`-oppføringane (klasse/slot var alt der; ikkje
berre den nye types-rada), sidan dette er éi omforming av det eksisterande
loop-mønsteret, ikkje eit types-spesifikt tillegg.

I loopen over `REPORTS`, etter at rapport-body (eller fallback-teksten) er
lagt til `lines`, legg til éi ny fotnote-linje per iterasjon:

```python
for filename, heading, objekttype in REPORTS:
    report_path = analyse_dir / filename
    lines += ["", f"### {heading}", ""]
    if not report_path.is_file():
        ...
        lines.append("*Rapport ikkje tilgjengeleg for denne bygginga.*")
    else:
        ...
        lines.append(body)
    lines += [
        "",
        f"*For fullstendig analyse av {objekttype} på tvers av domene sjå "
        f"[Modell-analyse]({MODELL_ANALYSE_WORKFLOW_URL})-workflowen.*",
    ]
```

Den avsluttande, delte fotnoten nedst i fila **held fram**, men innsnevra
til berre det ho framleis er einaste kjelde til — IRI-dereferering og
innhaldsforhandling, som ikkje har noka eiga `###`-underseksjon å hekte
ei per-seksjon-fotnote på:

```python
lines += [
    "",
    f"*For IRI-dereferering og innhaldsforhandling sjå "
    f"[Modell-analyse]({MODELL_ANALYSE_WORKFLOW_URL})-workflowen.*",
]
```

**Ordval `domene` vs. `domener`:** brukaren sitt utkast til fotnoteteksten
brukte «domener», men resten av same fil (og heile modellanalyse-laget
elles, t.d. `find-similar-names.py` sine «på tvers av alle domene»/«same
domene»-etikettar) brukar konsekvent **`domene`** som ubunden fleirtalsform
(nynorsk bøyer ikkje «domene» i ubunden fleirtal). Den nye fotnoteteksten
følgjer denne etablerte, konsekvente forma — «på tvers av domene», ikkje
«domener» — for å ikkje innføre ein grammatisk inkonsekvens i same fil.

## Ikkje i scope

- **Endring av `SIMILARITY_THRESHOLD`-default** — held fram som 0.8.
- **Full LinkML-arve-/import-oppløysing for `types:`** — same medvitne
  forenkling som for `slot`/`range` i dag: berre lokalt definerte
  `types:`-oppføringar per skjema vert samanlikna, ikkje typar arva via
  `imports:`.

## Steg

1. Utvid `src/assets/scripts/makefile/find-similar-names.py`: legg til
   `types` i `--kind`-choices, `load_entries()`, label-oppslag og
   tabell-utskrift (design i punkt 1).
2. Legg `analyse-similar-types-domain`/`analyse-similar-types-all` til
   `make/91-modell-analyse.mk` (`.PHONY` + target-body, design i punkt 2).
3. Legg `similar-types-domain`/`similar-types-all`-jobbar til
   `.github/workflows/modell-analyse.yml`, og til `sammendrag` sin
   `needs:`-liste (design i punkt 3).
4. Køyr `actionlint` mot den endra `modell-analyse.yml`
   (`podman run --rm -v "$(pwd)":/repo:ro -w /repo docker.io/rhysd/actionlint:latest -color .github/workflows/modell-analyse.yml`)
   — obligatorisk etter CI-endring per CLAUDE.md.
5. Legg dei to nye rapportfilene til `CHECKS` i
   `src/assets/scripts/makefile/summarise-modell-analyse.py` (design i
   punkt 4).
6. Oppdater `COMMANDS.md` § «Modell-analyse» med dei to nye targeta, og
   noter at `analyse-similar-types-domain` no også køyrer automatisk per
   skjema i `generate.yml` (jf. steg 9-10), analogt med
   `analyse-similar-classes-domain`/`analyse-similar-slots-domain`.
7. Test lokalt: `make analyse-similar-types-domain` og
   `make analyse-similar-types-all` (evt. avgrensa med `DOMAIN=oreg`) —
   stadfest at rapporten finn kjende namnelikskapar mellom dei 8 skjemaa
   sine `types:`-blokker (t.d. samanlikn `Versjonsnummer` på tvers av
   `enhetsregisteret-bvr*`-skjemaa), og at `--kind class`/`--kind slot`
   framleis fungerer uendra (regresjonssjekk på delt kode).
8. Test `NAME=`-avgrensinga for éin modell med `types:` (t.d.
   `make analyse-similar-types-all NAME=enhetsregisteret-bvrinn`).
9. Legg det tredje `analyse-similar-types-domain`-kallet til i
   «Køyr modellanalyse per skjema»-steget i `.github/workflows/generate.yml`
   sin `generate`-jobb (design i punkt 6). Køyr `actionlint` på nytt mot
   den endra `generate.yml` etter denne endringa.
10. Oppdater `REPORTS`-lista i
    `mkdocs/lib/scripts/generate-modellanalyse-md.py` til 3-tuppel-forma
    (legg til `objekttype` for dei to eksisterande radene og den nye
    types-rada), og oms om den avsluttande fotnoten til éi
    per-seksjons-fotnote per `###`-underseksjon pluss éi innsnevra,
    framleis delt fotnote for IRI-dereferering/innhaldsforhandling
    (design i punkt 7).
11. Test per-skjema-laget lokalt (same framgangsmåte som steg 8 i
    `specs/done/modellanalyse-per-skjema-index-md.md`): køyr
    `make analyse-similar-types-domain DOMAIN=oreg
    NAME=enhetsregisteret-bvrinn` og legg resultatet i
    `generated/oreg/enhetsregisteret-bvrinn/model-analyse/similar-types-domain-report.md`,
    køyr så `generate_modell_analyse` direkte og stadfest at
    «### Liknande typenamn (same domene)» dukkar opp korrekt under
    `## Modellanalyse` — både for eit skjema med `types:`-funn og for eit
    skjema utan nokon `types:`-blokk (t.d.
    `enhetsregisteret-bvrbekreftelse`, forvent «Ingen typer over terskelen
    vart funne»-fallback, ikkje ein feil). Stadfest samstundes at **alle
    tre** `###`-underseksjonar (klassenamn, slotnamn, typenamn) kvar har si
    eiga «For fullstendig analyse av `<objekttype>` på tvers av domene
    sjå …»-fotnote rett under seg, og at éi innsnevra
    IRI-dereferering/innhaldsforhandling-fotnote framleis står nedst i
    heile `## Modellanalyse`-seksjonen. Slett testfilene i `generated/`
    att etter verifisering (byggoutput, `.gitignore`-dekt).

## Utført

Alle elleve steg gjennomførte som planlagt, inkludert dei to
tilleggsomfanga (per-skjema embedding og per-seksjons-fotnotar) lagt til
undervegs.

1. `find-similar-names.py`: `--kind`-choices utvida med `"types"`.
   `load_entries()` bruker no eit `key`-oppslag (`class`→`classes`,
   `slot`→`slots`, `types`→`types`) og deler `range`/`base`-grenen mellom
   `slot`/`types`. Label-oppslaga (`label`, `name_label`) og
   tabellheadinga (`slot`/`types` deler kolonnestruktur, ulik
   kolonneoverskrift: `Slot`/`Type` vs. `Type`/`Grunntype`) utvida
   tilsvarande. Docstring og `--name`-hjelpeteksten oppdatert til å nemne
   `types:`.
2. `analyse-similar-types-domain`/`analyse-similar-types-all` lagt til
   `make/91-modell-analyse.mk` (`.PHONY` + target-body), identisk mønster
   som `analyse-similar-classes-*`.
3. `similar-types-domain`/`similar-types-all`-jobbar lagt til
   `.github/workflows/modell-analyse.yml`, begge i `sammendrag` sin
   `needs:`-liste.
4. `actionlint` køyrt mot `modell-analyse.yml` — ingen funn.
5. To rader lagt til `CHECKS` i `summarise-modell-analyse.py`, docstring
   oppdatert frå «seks» til «åtte» rapportfiler.
6. `COMMANDS.md` § «Modell-analyse» oppdatert: nye rader for dei to
   targeta, per-skjema-avsnittet nemner no `analyse-similar-types-domain`,
   `analyse-sammendrag`-rada oppdatert til «åtte» rapportfiler.
7. Testa lokalt: `make analyse-similar-types-domain DOMAIN=oreg` (115 par
   funne av 108 typer — m.a. `Versjonsnummer`/`Organisasjonsnummer`
   dupliserte på tvers av `enhetsregisteret-bvr*`) og
   `make analyse-similar-types-all` (115 par av 112 typer). Regresjon
   stadfesta: `analyse-similar-classes-domain`/`analyse-similar-slots-domain`
   DOMAIN=oreg gav framleis korrekte, uendra resultat (90 klassepar,
   390 slotpar).
8. `make analyse-similar-types-all NAME=enhetsregisteret-bvrinn` testa —
   63 par funne av 112 typer, korrekt avgrensa til éin modell mot resten.
9. Tredje kall (`analyse-similar-types-domain`) lagt til i
   «Køyr modellanalyse per skjema»-loopen i `generate.yml`, same
   `::warning::`-mønster som dei to eksisterande. `actionlint` køyrt på
   nytt mot endra `generate.yml` — ingen funn.
10. `REPORTS`-lista i `generate-modellanalyse-md.py` omforma til
    3-tuppel (`filnamn`, `###-overskrift`, `objekttype`) for alle tre
    radene (klasse/slot/types). Loopen skriv no éi
    «*For fullstendig analyse av `<objekttype>` på tvers av domene sjå
    …*»-fotnote per `###`-underseksjon (uavhengig av om rapportfila
    finst eller har funn). Den tidlegare eine, delte fotnoten er
    innsnevra til å berre dekkje IRI-dereferering/innhaldsforhandling
    (flytta til etter loopen, ikkje lenger nemner cross-domain-
    samanlikning sidan det no er dekt av per-seksjons-fotnotane).
    Intro-sitatblokka oppdatert til å nemne «klasse-, slot- og typenamn».
11. Testa per-skjema-laget lokalt: genererte reelle rapportfiler
    (`analyse-similar-classes-domain`/`-slots-domain`/`-types-domain`,
    DOMAIN=oreg NAME=enhetsregisteret-bvrinn) i
    `generated/oreg/enhetsregisteret-bvrinn/model-analyse/`, kalla
    `generate_modell_analyse oreg enhetsregisteret-bvrinn` direkte —
    stadfesta at alle tre `###`-underseksjonane vert rett rendra, kvar
    med si eiga per-seksjons-fotnote, og éi innsnevra
    IRI-/innhaldsforhandling-fotnote nedst. Testa òg fallback-stien for
    `register-over-aksjeeiere` (**avvik frå plan:** brukte dette skjemaet
    i staden for det planlagde `enhetsregisteret-bvrbekreftelse`, sidan
    sistnemnde faktisk *har* ein eigen `types:`-blokk — verifisert med
    grep før testen; `register-over-aksjeeiere` har korkje `types:`,
    `similar-classes-domain-report.md` eller `similar-slots-domain-report.md`
    i testoppsettet) — stadfesta korrekt «Rapport ikkje tilgjengeleg for
    denne bygginga»-fallback for klasse/slot og «Ingen liknande typenamn
    funne»-fallback for types, alle med korrekt per-seksjons-fotnote.
    Testfilene i `generated/oreg/{enhetsregisteret-bvrinn,
    register-over-aksjeeiere}/model-analyse/` sletta att etter
    verifisering (byggoutput, `.gitignore`-dekt).

Ingen filer utover dei planlagde vart endra. Ei sandkasse-avgrensing
(podman rootless `newuidmap`: "Operation not permitted") vart trefft ved
første `make analyse-similar-types-domain`-kjøring — løyst ved å køyre
påfølgjande `make`/`podman`-kommandoar utan sandkasse, slik gjeldande
verktøyinstruksjon føreskriv for stadfesta sandkasse-feil.
