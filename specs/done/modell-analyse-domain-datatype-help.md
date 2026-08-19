# Plan: `DOMAIN=`-filter, datatype i slot-rapport, og synleggjering i `make help`

## Bakgrunn

Tre relaterte tiltak for `make/91-modell-analyse.mk`
(`analyse-similar-classes-domain`, `analyse-similar-slots-domain` m.fl.,
skriptet `src/assets/scripts/makefile/find-similar-names.py`):

1. Innfør eit `DOMAIN=`-flagg i **alle** `make analyse-*`-kall
2. Slot-rapporten skal i tillegg liste datatypen (`range:`) for kvart
   identifisert slot
3. Legg `modell-analyse`-targeta til i `help.sh` (dei manglar heilt i
   `make help`-output i dag)

**Merk om punkt 1 — oppdatert etter avklaring:** opphavleg omfang var berre
`analyse-similar-classes-domain`/`analyse-similar-slots-domain`. Brukaren
utvida til **alle** `analyse-*`-kall. Kartlegginga under viser at 5 av dei
6 targeta faktisk skannar skjema sjølve og kan få eit meiningsfullt
`DOMAIN=`-filter; det siste (`analyse-sammendrag`) skannar ikkje skjema i
det heile og har difor ingen naturleg implementasjon — sjå eige avsnitt.

## 1 — `DOMAIN=`-filter for alle `analyse-*`-kall

**Kartlegging — kva av dei 6 `analyse-*`-targeta skannar faktisk skjema?**

| Target | Skript | Skannar skjema sjølv? | `DOMAIN=` meiningsfullt? |
|---|---|---|---|
| `analyse-similar-classes-domain` | `find-similar-names.py --kind class --scope domain` | Ja (`discover_schemas()`) | Ja |
| `analyse-similar-classes-all` | `find-similar-names.py --kind class --scope all` | Ja | Ja (avgrensar kandidatmengda før kryss-domene-samanlikning) |
| `analyse-similar-slots-domain` | `find-similar-names.py --kind slot --scope domain` | Ja | Ja |
| `analyse-similar-slots-all` | `find-similar-names.py --kind slot --scope all` | Ja | Ja |
| `analyse-iri-resolution` | `check-iri-resolution.py` | Ja (eiga `discover_schemas()`, identisk mønster) | Ja |
| `analyse-sammendrag` | `summarise-modell-analyse.py` | **Nei** — les berre dei fem ferdiggenererte rapportfilene (faste filnamn: `similar-classes-domain-report.md` osv.) frå disk, ingen eigen `src/linkml`-skanning | **Nei, ingen naturleg implementasjon** |

**Noverande åtferd (dei 5 skjema-skannande targeta):** `--scope domain`/
`--scope all` styrer **kva par** som vert rapporterte (berre par innanfor
same domene, vs. par på tvers av alle domene) — men `discover_schemas()`
skannar **alltid heile repoet** (`src/linkml/*/*/*-schema.yaml`),
uavhengig av `--scope`. Det finst i dag **ingen** måte å avgrense
analysen til berre ÉIN spesifikk domene.

**Ønskt åtferd:** `DOMAIN=<domene>` skal avgrense alle 5 skjema-skannande
targeta til å berre analysere skjema **innanfor det gitte domenet**. Utan
`DOMAIN=` oppfører targeta seg som i dag (uendra, bakoverkompatibelt med
`.github/workflows/modell-analyse.yml`, som kallar dei utan `DOMAIN`).

**Implementasjon:**
- `find-similar-names.py`: nytt valfritt `--domain <domene>`-flagg.
  `discover_schemas()` filtrerer til `src/linkml/<domain>/*/*-schema.yaml`
  når sett, elles uendra. Gjeld alle fire `analyse-similar-*`-target (både
  `-domain`- og `-all`-variantane).
- `check-iri-resolution.py`: same nye `--domain <domene>`-flagg og same
  filtrering av `discover_schemas()` — skriptet har i dag **ingen**
  argparse i det heile (`main()` tek ingen argument), så dette er eit nytt,
  isolert tillegg, ikkje ei endring av eksisterande flagg.
- `make/91-modell-analyse.mk`: alle 5 target sender `--domain $(DOMAIN)`
  vidare når `DOMAIN` er sett (`$(if $(DOMAIN),--domain $(DOMAIN))`-mønster,
  alt brukt fleire stader i repoet). `## `-kommentarane oppdaterast til
  `[DOMAIN=<domene>]` (jf. den etablerte plasshaldarkonvensjonen frå
  denne økta sine tidlegare harmoniseringstiltak).
- **`analyse-sammendrag` får ikkje `DOMAIN=`** — han les ferdige
  rapportfilar med faste filnamn, ikkje skjema, så det finst ingen
  meiningsfull ting å filtrere. Dersom eit av dei andre targeta køyrer med
  `DOMAIN=`, vil `analyse-sammendrag` berre summere kva som faktisk ligg i
  rapportfilene (t.d. eit domene-avgrensa funn), utan å måtte vite om det
  sjølv. Dette er nemnt eksplisitt her sidan brukaren bad om `DOMAIN=` på
  **alle** kall — dersom dette unntaket ikkje er ønskt, må ein i så fall
  først avklare kva «DOMAIN på analyse-sammendrag» skal *bety* (t.d.
  domene-spesifikke rapportfilnamn i staden for faste namn, som er ei
  større, separat omlegging).

## 2 — Datatype i slot-rapporten

**Noverande åtferd:** `load_names()` returnerer berre `name`-lista frå
`classes:`/`slots:`-blokka — ingen typeinformasjon.

**Ønskt åtferd:** For `--kind slot` skal rapporttabellen i tillegg vise
`range:`-verdien (datatypen) for kvart identifisert slot — nyttig for å
vurdere om eit likskapsfunn er eit reelt duplikat (same type = sterkare
signal) eller berre eit namnesamantreff (ulik type).

**Implementasjon:**
- `find-similar-names.py`: byt `load_names()` til `load_entries()` som
  returnerer `(namn, range)`-par. For `--kind class` er `range` alltid
  `None` (klassar har ikkje eit `range`-omgrep) og tabellen held fram
  uendra (5 kolonnar). For `--kind slot` hentast `range:`-feltet frå kvar
  slot-definisjon.
- **Avgrensing (medvite forenkling, dokumentert i skriptet sin
  docstring):** viser `range:`-verdien **slik ho står skriven** i
  slot-definisjonen, utan å løyse LinkML sin fulle arve-/default_range-
  logikk (slot_usage-overstyring i klassar, `default_range:` på
  skjemanivå når `range:` manglar). Eit slot utan eksplisitt `range:` vert
  vist som `(default)` i staden for å prøve å rekne ut det faktiske
  resultatet — å gjere dette fullstendig korrekt ville kravd å laste heile
  `SchemaView`-arvegrafen per skjema, noko som endrar skriptet sin
  ytingsprofil monaleg (i dag reint `yaml.safe_load`, ingen LinkML-runtime).
- Ny tabellform for slot-rapporten:
  `| Likskap | Namn A | Type A | Skjema A | Namn B | Type B | Skjema B |`
  (klasse-rapporten er uendra: `| Likskap | Namn A | Skjema A | Namn B | Skjema B |`)

## 3 — Synleggjer `modell-analyse`-targeta i `make help`

**Rotårsak:** `help.sh` sin `categories`-array har ingen mønster som
matchar `analyse-`-prefikset:
```
"Vanleg bruk|(test|roundtrip|clean|help)"
"Generering (per domene eller skjema)|(gen-|domain-|convert-)"
"Validering|(validate|lint)"
"Dokumentasjon|docs-"
"Container images|build-docker-"
"MCP-serverar|mcp-"
"Vedlikehald|(update-|new-|remove-|check-)"
```
Sidan eit target må matche **minst éin** kategori for i det heile å verte
vist (jf. den doble løkka i `help.sh`), fell `analyse-similar-classes-domain`,
`analyse-similar-classes-all`, `analyse-similar-slots-domain`,
`analyse-similar-slots-all`, `analyse-iri-resolution` og
`analyse-sammendrag` **heilt bort** frå `make help`-output i dag — trass i
at dei alle har gyldige `## `-kommentarar. Dei er dokumenterte i
`COMMANDS.md` § «Modell-analyse», men usynlege i CLI-verktøyet sjølv.

**Tiltak:** legg til ein ny kategori i `help.sh`:
```
"Modell-analyse|analyse-"
```
Ingen kollisjon med eksisterande mønster (verifisert: `analyse-` matchar
ingen av dei 7 andre kategoripatterna).

## Filer som vert påverka

- `src/assets/scripts/makefile/find-similar-names.py` (tiltak 1, 2)
- `src/assets/scripts/makefile/check-iri-resolution.py` (tiltak 1 — nytt
  `--domain`-flagg, skriptet har ingen argparse frå før)
- `make/91-modell-analyse.mk` (tiltak 1, `## `-kommentarar for alle 5
  skjema-skannande target)
- `src/assets/scripts/makefile/help.sh` (tiltak 3)

## Handlingsliste

1. [x] Legg til `--domain`-flagg i `find-similar-names.py`, filtrer
   `discover_schemas()`
2. [x] Legg til `--domain`-flagg (ny argparse) i `check-iri-resolution.py`,
   filtrer `discover_schemas()`
3. [x] Byt `load_names()` → `load_entries()` med `(namn, range)`-par,
   utvid slot-tabellen med Type-kolonnar
4. [x] Oppdater alle 5 skjema-skannande target i `make/91-modell-analyse.mk`:
   `DOMAIN=`-vidaresending + `## `-kommentar (`analyse-similar-classes-domain`,
   `analyse-similar-classes-all`, `analyse-similar-slots-domain`,
   `analyse-similar-slots-all`, `analyse-iri-resolution`)
5. [x] Legg til `"Modell-analyse|analyse-"`-kategorien i `help.sh`
6. [x] Verifiser: `make analyse-similar-slots-domain DOMAIN=<eit domene>`
   viser berre det domenet sine slots, med Type-kolonne synleg;
   `make analyse-iri-resolution DOMAIN=<eit domene>` testar berre det
   domenet sine IRI-ar; `make help` viser no ein «Modell-analyse»-bolk med
   alle 6 target; `.github/workflows/modell-analyse.yml` sine eksisterande
   kall (utan `DOMAIN`) er uendra i åtferd

## Utført

**Skript:** `find-similar-names.py` og `check-iri-resolution.py` fekk
begge nytt `--domain <domene>`-flagg som filtrerer `discover_schemas()`
til `src/linkml/<domene>/*/*-schema.yaml` når sett (`check-iri-resolution.py`
hadde ingen argparse frå før — lagt til frå botnen). Slot-rapporten i
`find-similar-names.py` fekk nye `Type A`/`Type B`-kolonner
(`load_names()` → `load_entries()`, returnerer no `(namn, range)`-par;
klasse-rapporten er uendra 5-kolonne-format). Manglande `range:` vert
vist som `(default)`, som dokumentert avgrensing.

**`make/91-modell-analyse.mk`:** alle 5 skjema-skannande target
(`analyse-similar-classes-domain/-all`, `analyse-similar-slots-domain/-all`,
`analyse-iri-resolution`) sender no `--domain $(DOMAIN)` vidare via
`$(if $(DOMAIN),--domain $(DOMAIN))` når `DOMAIN` er sett, elles uendra
åtferd. `analyse-sammendrag` urørt (grunngjeving i spec-teksten over —
les berre ferdige rapportfiler, skannar ikkje skjema).

**`help.sh`:** ny `"Modell-analyse|analyse-"`-kategori. Alle 6
`analyse-*`-target var tidlegare **heilt usynlege** i `make help`
sjølv om dei hadde gyldige `## `-kommentarar (matcha ingen av dei 7
eksisterande kategoripatterna) — no viste i ein eigen «Modell-analyse»-bolk.

**Verifisert med reelle køyringar:**
- `make analyse-similar-slots-domain DOMAIN=oreg` → 163 slots sjekka (mot
  1199 for heile repoet utan filter) — stadfestar at `DOMAIN=` faktisk
  avgrensar skanninga, ikkje berre visinga. Type-kolonnene avslørte eit
  reelt funn: `navn`/`navn` (100 % namnelikskap) har ulik type
  (`Virksomhetsnavn` vs. `string`) — nett den typen signal tiltaket var
  meint å gje.
- `make analyse-similar-classes-domain DOMAIN=oreg` → 61 klassar sjekka,
  klasse-tabellen framleis 5 kolonner (ingen utilsikta Type-kolonne)
- `make analyse-similar-classes-all` (utan `DOMAIN`) → 191 par/527 klassar,
  uendra format
- `make analyse-iri-resolution DOMAIN=fair` → testa berre 1 skjema/6 IRI-ar
  (mot heile repoet utan filter)
- `make -n analyse-similar-classes-domain` (utan `DOMAIN`) stadfestar at
  `--domain`-flagget vert korrekt utelate når `DOMAIN` ikkje er sett —
  identisk kommandolinje som før, ingen regresjon for
  `.github/workflows/modell-analyse.yml` sine eksisterande kall
