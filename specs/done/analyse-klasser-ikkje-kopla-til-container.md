# Ny modellanalyse: klasser ikkje kopla til containerklassen

## Bakgrunn

Under arbeid med `javazonetalk-schema.yaml` vart det oppdaga at
`gen-eksempeldata` berre genererte data for éin klasse (`Javazonetalk`),
sjølv om skjemaet har 8 lokale klasser. Årsaka: `JavazonetalkContainer`
(containerklassen) har berre eitt attributt (`javazonetalker`, range
`Javazonetalk`), og `Javazonetalk` sjølv har berre `slots: [id]` — ingen
slot på han peikar vidare til nokon annan klasse. Resten av modellen
(`Konferanse` → `Timeplan` → `Sesjon` → `Foredrag` →
`Foredragsholder`/`Sesjonslokale`/`InnsendingStatus`) er derimot **fullt
samanhengande internt** — kvar klasse i den kjeda er kopla til minst éi
anna klasse i kjeda — men heile denne kjeda er **aldri nådd frå
containerklassen**.

**Det finst alt ein modellanalyse-jobb som ser liknande ut, men som ikkje
fangar dette:** `make analyse-isolerte-klasser`
(`src/assets/scripts/makefile/find-unused-local-definitions.py`,
`--kind class`) sjekkar om ei klasse har **minst éi parvis** tilkopling
til **ei anna lokal klasse** (i kva retning som helst). Sidan
`Konferanse`/`Timeplan`/`Sesjon`/`Foredrag`/`Foredragsholder`/
`Sesjonslokale`/`InnsendingStatus` alle er kopla til **kvarandre**,
har kvar av dei minst éi reell tilkopling — og vert difor **ikkje**
flagga av denne sjekken. Verifisert direkte:

```bash
make analyse-isolerte-klasser SCHEMA=src/linkml/oreg/javazonetalk/javazonetalk-schema.yaml
```

gjev berre:

```
| Klasse | Grunn | Skildring |
|---|---|---|
| `Javazonetalk` | Kun tilkopla via containerklassen | TODO: beskriv klassen |

**Totalt: 1 isolerte/underintegrerte klasser av 8 lokale klasser** (0 heilt isolert, 1 kun tilkopla via containerklassen).
```

— heile den 7-klassar store, fullt samanhengande, men container-orphana
under-grafen (`Konferanse` og resten) er usynleg for denne sjekken. Han
er **konseptuelt ein annan sjekk** enn det brukaren spør etter:
`analyse-isolerte-klasser` svarer «har denne klassa NOKA tilkopling til
noka anna klasse?», ikkje «kan denne klassa faktisk nåast frå
containerklassen, modellen sitt eintydige inngangspunkt?». Det andre
spørsmålet er det som avgjer om t.d. `gen-eksempeldata`,
JSON-serialisering via containeren, eller andre container-drivne verktøy
faktisk ser klassa i det heile.

**Konklusjon: ja, det er grunnlag for ein ny, komplementær
modellanalyse-jobb** — ikkje ei erstatning for `analyse-isolerte-klasser`,
men eit nytt kriterium som fangar akkurat denne typen «velforma, men
foreldrelaus under-graf»-feil som den eksisterande sjekken systematisk
går glipp av.

## Målbilete

Ein ny analyse (`--kind unreachable` i
`find-unused-local-definitions.py`, same fil og mønster som dei fem
eksisterande kindane) som:

1. Bygg ein **udirigert** graf over alle lokale klasser, med kantar frå
   `class_connections()` (allereie eksisterande hjelpefunksjon — slot-/
   attributtrange og is_a/mixins) i **begge retningar** (A→B gjev både
   A-B og B-A som kant, sidan «kopla til» skal tolkast symmetrisk her,
   i motsetnad til container-spesialtilfellet i `find_isolated_classes`).
2. Køyr BFS/DFS frå containerklassen (`tree_root: true`) over denne grafen.
3. Rapporter alle lokale klasser (unnateke containeren sjølv) som **ikkje**
   vert nådd av traverseringa.

## Presist skilje frå `analyse-isolerte-klasser` (viktig å dokumentere)

| Klasse-tilstand | `analyse-isolerte-klasser` | Ny `analyse-ikkje-tilkopla-container` |
|---|---|---|
| Heilt isolert (ingen tilkopling i det heile) | ✅ Flagga («Heilt isolert») | ✅ Flagga (trivielt uoppnåeleg) |
| Kun referert av containeren, ingen vidare tilkopling (t.d. `Javazonetalk`) | ✅ Flagga («Kun tilkopla via containerklassen») | ❌ Ikkje flagga — han ER jo nådd frå containeren |
| Del av ein fullt samanhengande klynge som sjølv ikkje er kopla til containeren (t.d. `Konferanse`-kjeda) | ❌ **Ikkje flagga** — kvar klasse i klynga har jo ei reell tilkopling til ei anna | ✅ Flagga — heile klynga er uoppnåeleg frå containeren |
| Normalt integrert (nådd frå container, direkte eller transitivt) | ❌ Ikkje flagga | ❌ Ikkje flagga |

Dei to sjekkane svarer på **ulike spørsmål** og skal difor **begge**
haldast ved like — ikkje slåast saman. Merk at «Heilt isolert»-klassar vil
dukke opp i **begge** rapportane (venta, ikkje ein feil — sjå
«Opne vurderingar»).

## Design

### Ny funksjon i `find-unused-local-definitions.py`

```python
def find_classes_unreachable_from_container(sv) -> list[tuple[str, str]]:
    """Finn lokale klasser (unnateke containeren) som IKKJE er nåbare frå
    containerklassen (tree_root) via BFS over ein udirigert graf bygd frå
    class_connections() (slot-/attributtrange, is_a/mixins).

    I motsetnad til find_isolated_classes() (som spør om ei klasse har
    NOKA parvis tilkopling til noka anna lokal klasse, uavhengig av
    containeren) spør denne om klassa faktisk kan NÅAST frå containeren
    — modellen sitt eintydige inngangspunkt. Ein heil, internt
    samanhengande klynge av klassar som sjølv ikkje er kopla til
    containeren (t.d. eit gløymt/scaffold-underrte) vert ikkje fanga av
    find_isolated_classes() (kvar klasse i klynga har jo ei reell
    tilkopling til ei anna klasse i klynga), men FANGAST her."""
    all_local = local_classes(sv, include_root=True)
    container = next((c for c in all_local if c.tree_root), None)
    if container is None:
        return []  # no_container_class-sjekken fangar dette separat

    by_name = {c.name: c for c in all_local}

    # Udirigert graf: A->B gjev kant begge vegar (i motsetnad til
    # class_connections() sin eigen retning, som berre er A sine
    # UTGÅANDE referansar).
    graph: dict[str, set[str]] = {c.name: set() for c in all_local}
    for c in all_local:
        for target in class_connections(sv, c):
            graph[c.name].add(target)
            graph.setdefault(target, set()).add(c.name)

    visited: set[str] = {container.name}
    queue = list(graph.get(container.name, ()))
    while queue:
        name = queue.pop()
        if name in visited:
            continue
        visited.add(name)
        queue.extend(graph.get(name, ()))

    unreachable = []
    for c in all_local:
        if c.tree_root or c.name in visited:
            continue
        description = (c.description or "").strip()
        unreachable.append((c.name, description))
    return sorted(unreachable)
```

### Wiring inn i eksisterande infrastruktur

- **`ALL_KINDS`**: legg til `"unreachable"`. Dette gjev automatisk
  batch-støtte via `process_schema_all_kinds`/`process_domain` — **ingen
  endring naudsynt** i `.github/workflows/generate.yml` sitt «Køyr
  modellanalyse per skjema»-steg, sidan det allereie kallar
  `make analyse-lokal-modellanalyse-domene DOMAIN=...`, som itererer
  `ALL_KINDS` internt.
- **`KIND_TO_REPORT_FILENAME["unreachable"]`**:
  `"ikkje-tilkopla-container-report.md"`.
- **`KIND_LABELS["unreachable"]`**: `"klasser ikkje kopla til
  containerklassen"` (brukt i evt. framtidige samla tal-linjer — sjølve
  rapporten treng eigen tittel-logikk, sjå under).
- **`compute_items_and_total()`**: legg til ei grein for
  `kind == "unreachable"` som kallar
  `find_classes_unreachable_from_container(sv)` og returnerer
  `(items, len(local_classes(sv, include_root=True)) - 1)` (containeren
  sjølv trekt frå nemnaren, same konvensjon som `"class"`-greina).
- **`format_report()`**: legg til ei tredje grein (etter `class`-greina,
  før den generiske `else`), sidan verken tittel- eller
  tomt-resultat-teksten passar dei to eksisterande formata:

  ```python
  elif kind == "unreachable":
      title = f"# Klasser ikkje kopla til containerklassen ({schema_path})"
      empty_msg = (
          f"Ingen klasser utan tilkopling til containerklassen funne "
          f"({total} klasser sjekka)."
      )
      col_a = "Klasse"
  ```

  og i tabell-delen, same 2-kolonne-format som `slot`/`enum`/`type`/
  `subset` (namn + skildring) — kan delast med den greina direkte sidan
  formatet er identisk, berre tittel-/tomt-tekst skil seg.
- **`main()`**: `--kind` sin `choices=list(ALL_KINDS)` plukkar opp
  `"unreachable"` automatisk sidan han er lagt til `ALL_KINDS`.

### Nytt make-target (single-schema, matchar dei fem søsken-måla)

I `make/91-modell-analyse.mk`, rett etter `analyse-isolerte-klasser`:

```make
analyse-ikkje-tilkopla-container: ## Finn lokale klasser som ikkje er nåbare frå containerklassen (tree_root), sjølv om dei er kopla til kvarandre [SCHEMA=<sti>]
	$(call print_header,analyse-ikkje-tilkopla-container,SCHEMA=$(SCHEMA)) 1>&2
	@$(LINKML_RUN) python3 src/assets/scripts/makefile/find-unused-local-definitions.py \
	  --kind unreachable --schema $(SCHEMA)
```

Legg han òg til i `.PHONY`-lista øvst i fila, og i
`analyse-lokal-modellanalyse-domene` sin hjelpetekst dersom den listar
kindane eksplisitt (verifiser ved implementering — per no delegerer det
targetet berre til `--domain`-modus i scriptet, som ikkje treng
oppdaterast utover `ALL_KINDS`).

### Per-skjema dokumentasjonsside (`## Modellanalyse`)

Legg til ein ny tuppel i `REPORTS`-lista i
`mkdocs/lib/scripts/generate-modellanalyse-md.py`, same mønster som
`isolerte-klasser-report.md` (ingen cross-domain-motpart, `None, None`):

```python
(
    "ikkje-tilkopla-container-report.md",
    "Klasser ikkje kopla til containerklassen",
    "klasser ikkje kopla til containerklassen",
    None,
    None,
),
```

Utan denne oppføringa vert rapportfila generert (batch-modus skriv han
alltid), men **aldri vist** i den publiserte dokumentasjonssida sin
`## Modellanalyse`-seksjon.

### Dokumentasjon

`find-unused-local-definitions.py` sin modul-docstring skildrar i dag
`--kind class` som «ein heilt ny, femte analyse». Oppdater innleiinga til
å nemne den nye sjette kinden og det presise skiljet frå `--kind class`
(kopier resonnementet frå tabellen over, kortare).

## Opne vurderingar

1. **Skal «Heilt isolert»-klassar (frå `find_isolated_classes`) også
   dukke opp i den nye `unreachable`-rapporten?** Dei vil gjere det
   naturleg med designet over (ei heilt isolert klasse er per definisjon
   uoppnåeleg frå containeren òg). Tilråding: **behald overlappet** —
   ein lesar som berre opnar `ikkje-tilkopla-container-report.md` skal få
   det fulle biletet av «kva er uoppnåeleg», utan å måtte krysjekke den
   andre rapporten. Legg heller til ei kort forklarande linje i
   `format_report()` sin `unreachable`-gjein som nemner at nokre av desse
   òg kan vere heilt isolerte (ikkje berre del av ein orphana klynge) —
   sjå `specs/backlog/...` (denne specen) for grunngjeving, dersom det er
   ønskt presisjon i sjølve rapportteksten.
2. **Namn på `--kind`-verdien og rapportfila** (`unreachable` /
   `ikkje-tilkopla-container-report.md`) er forslag — juster fritt ved
   implementering dersom eit anna namn passar betre inn i eksisterande
   norsk terminologi i fila.

## Steg

1. Legg til `find_classes_unreachable_from_container()` i
   `find-unused-local-definitions.py`.
2. Legg `"unreachable"` til `ALL_KINDS`, `KIND_TO_REPORT_FILENAME` og
   `KIND_LABELS`.
3. Utvid `compute_items_and_total()` og `format_report()` med
   `unreachable`-greiner.
4. Oppdater modul-docstringen med den nye sjette kinden og skiljet frå
   `--kind class`.
5. Legg til `analyse-ikkje-tilkopla-container`-targetet i
   `make/91-modell-analyse.mk` (+ `.PHONY`).
6. Legg til ny tuppel i `REPORTS`-lista i
   `mkdocs/lib/scripts/generate-modellanalyse-md.py`.
7. Verifiser mot `javazonetalk-schema.yaml` — forvent at rapporten listar
   `Konferanse`, `Foredrag`, `Sesjon`, `Timeplan`, `Sesjonslokale`,
   `Foredragsholder`, `InnsendingStatus` (7 klasser), og **ikkje**
   `Javazonetalk` (han er nådd via containeren).
8. Verifiser mot minst to velforma skjema utan kjent gap (t.d.
   `samt-bu-schema.yaml`, `dcat-ap-no-schema.yaml`) — forvent **0 funn**
   (ingen falske positivar).
9. Køyr `make analyse-lokal-modellanalyse-domene DOMAIN=oreg` (batch-modus)
   og stadfest at `ikkje-tilkopla-container-report.md` vert skriven saman
   med dei fem eksisterande rapportane, utan å endre
   `.github/workflows/generate.yml`.

## Handlingsliste

- [x] Steg 1: `find_classes_unreachable_from_container()`
- [x] Steg 2: `ALL_KINDS`/`KIND_TO_REPORT_FILENAME`/`KIND_LABELS`
- [x] Steg 3: `compute_items_and_total()`/`format_report()`-utviding
- [x] Steg 4: Oppdater modul-docstring
- [x] Steg 5: Nytt make-target
- [x] Steg 6: Ny `REPORTS`-tuppel i `generate-modellanalyse-md.py`
- [x] Steg 7: Verifiser mot `javazonetalk-schema.yaml`
- [x] Steg 8: Verifiser mot velforma skjema (ingen falske positivar)
- [x] Steg 9: Verifiser batch-modus (`analyse-lokal-modellanalyse-domene`)

## Utført

**Dato:** 2026-08-31

Alle ni steg gjennomførte som planlagt, med begge dei opne vurderingane
avgjorde slik tilrådd i specen (overlapp med heilt-isolert-klassar
behalde; namna `unreachable`/`ikkje-tilkopla-container-report.md`
brukte uendra).

**Endringar:**

- **`find-unused-local-definitions.py`:** ny funksjon
  `find_classes_unreachable_from_container()` (BFS over ein udirigert
  graf bygd frå `class_connections()`); `"unreachable"` lagt til
  `ALL_KINDS`, `KIND_TO_REPORT_FILENAME`, `KIND_LABELS`;
  `compute_items_and_total()` og `format_report()` utvida med ei
  `unreachable`-grein; modul-docstring oppdatert med den nye sjette
  kinden og det presise skiljet frå `--kind class`.
- **`make/91-modell-analyse.mk`:** nytt `analyse-ikkje-tilkopla-container`-
  target (+ `.PHONY`), same mønster som dei fem søskena.
- **`mkdocs/lib/scripts/generate-modellanalyse-md.py`:** ny tuppel i
  `REPORTS`-lista, ingen cross-domain-motpart (same mønster som
  `isolerte-klasser-report.md`); docstring oppdatert til «seks».

**Verifisering:**

- **`javazonetalk-schema.yaml` (motiverande case):** flaggar korrekt 6
  klasser (`Foredrag`, `Foredragsholder`, `Konferanse`, `Sesjon`,
  `Sesjonslokale`, `Timeplan`) av 7 ikkje-container lokale klasser. Merk:
  specen sitt opphavlege overslag på «7 klasser inkl. InnsendingStatus»
  var feil — `InnsendingStatus` er ein **enum**, ikkje ei klasse (fanga
  opp av ein unøyaktig `grep` i forkant, ikkje av sjølve
  implementasjonen). Verktøyet sitt faktiske resultat (6 av 7) er
  korrekt stadfesta mot skjemaet sin reelle klassegraf.
- **Ingen falske positivar:** `samt-bu-schema.yaml` (10 klasser) og
  `dcat-ap-no-schema.yaml` (16 klasser) gjev begge «Ingen klasser utan
  tilkopling til containerklassen funne».
- **Batch-modus:** `make analyse-lokal-modellanalyse-domene DOMAIN=samt`
  skriv korrekt 6 rapportar (inkl. den nye) utan endring i
  `.github/workflows/generate.yml`, som planlagt. Tilsvarande køyring
  for `DOMAIN=oreg` feila på grunn av eit **nettverksmiljø-avgrensa**
  problem (DNS-oppløysing av eit versjonslåst
  `raw.githubusercontent.com`-import i eit av dei andre oreg-skjemaa
  feila i denne økta sitt sandkasse-miljø — urelatert til denne
  endringa; single-schema-modus mot nettopp `javazonetalk-schema.yaml`
  fungerte feilfritt, som stadfesta over).
- **Biverknad rydda opp:** batch-forsøket mot `DOMAIN=oreg` skreiv ved
  eit uhell over `src/linkml/oreg/javazonetalk/validation/0.1.0/silver.json`
  med eit falskt `validation_error`-funn frå nettverksfeilen over —
  tilbakestilt til committa tilstand (`git checkout --`) før avslutning.
  `src/linkml/oreg/javazonetalk/examples/javazonetalk-eksempel.yaml` var
  alt endra frå brukaren sin eigen tidlegare `make gen-eksempeldata`-
  køyring (urelatert til denne specen) og er ikkje rørt.
