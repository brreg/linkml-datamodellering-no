# `analyse-isolerte-klasser`: flagg klassar kun tilkopla via containerklassen

## Bakgrunn

Brukaren ønskjer at `make analyse-isolerte-klasser` (og dermed
`isolerte-klasser-report.md`, delen av `## Modellanalyse`-seksjonen i
genererte skjema-sider) òg skal flagge lokale klassar der **einaste**
tilkoplinga til resten av modellen er at containerklassen (`tree_root`)
listar dei som eit attributt — dvs. klassen har ingen slot-/attributtrange-
eller `is_a`/`mixins`-tilkopling til/frå NOKA anna lokal klasse.

**Dagens åtferd** (`find_isolated_classes()` i
`src/assets/scripts/makefile/find-unused-local-definitions.py`):
containerklassen sine eigne tilkoplingar (attributta som listar kva
klassar ho refererer) tel som reell tilkopling for måla — ein klasse som
BERRE er referert av containeren vert difor aldri flagga i dag, sjølv om
ho ikkje har noka anna tilkopling. Dette skjuler nett den situasjonen
brukaren no vil fange: ein klasse som er registrert som eit
container-inngangspunkt, men som ikkje er integrert i resten av
modellgrafen (moglegvis eit stillstand scaffold, feilplassert attributt,
eller ei klasse som burde vore nesta ein annan stad).

## Design

To distinkte kategoriar i staden for éin:

1. **Heilt isolert** (uendra semantikk) — klassen har ingen tilkopling i
   det heile, ikkje eingong via containerklassen (verken containeren eller
   noka anna klasse peikar på henne, og ho peikar sjølv ikkje på noka
   anna lokal klasse).
2. **Kun tilkopla via containerklassen** (ny) — containerklassen peikar
   på klassen, MEN klassen har ingen andre tilkoplingar: ho peikar ikkje
   sjølv på noka anna lokal klasse, og ingen ANNA (ikkje-container) lokal
   klasse peikar på henne.

Ei klasse som har minst éi reell (ikkje-container) tilkopling — anten
utgåande (ho peikar på ei anna klasse) eller innkomande frå ei anna
ikkje-container-klasse — er framleis IKKJE flagga, uendra frå i dag.

**Algoritme-endring:** når `connected_names` vert bygd opp, skal
containerklassen sine EIGNE utgåande tilkoplingar IKKJE lenger telje som
"målet er tilkopla" — containeren sine mål vert i staden sporsa separat
(`container_targets`) og brukt til å skilje dei to kategoriane over for
klassar som elles endar utanfor `connected_names`.

**Rapportformat:** éi samla tabell (ikkje to separate tabellar) med ny
`Grunn`-kolonne (`Heilt isolert` / `Kun tilkopla via containerklassen`) —
held fram med berre éin header-/skiljerad i rapportkroppen, slik at
`count_table_rows()` i `mkdocs/lib/scripts/generate-modellanalyse-md.py`
(som tel ALLE `|`-linjer minus 2, utan omsyn til fleire tabellar) framleis
tel korrekt utan endringar der. Kolonnerekkjefølgje: `Klasse | Grunn |
Skildring`. Summeringslinja skil dei to tala:
`**Totalt: N isolerte/underintegrerte klassar av T lokale klassar** (X
heilt isolert, Y kun tilkopla via containerklassen).`

## Tiltak

1. `src/assets/scripts/makefile/find-unused-local-definitions.py`:
   - `find_isolated_classes()`: skil containeren sine eigne utgåande
     tilkoplingar frå resten av `connected_names`-oppbygginga, spor
     `container_targets`, returner `(name, description, reason)` i staden
     for `(name, description)`.
   - `format_report()` (kind == "class"): ny `Grunn`-kolonne, oppdatert
     summeringslinje med kategori-oppdeling.
   - Docstring (modul-nivå, linje 22-28) oppdatert til å skildre dei to
     kategoriane.
2. Verifiser med eit eksisterande skjema som har minst éin container-only
   kandidat (eller eit midlertidig testskjema) at begge kategoriane vert
   korrekt skilde, og at ei klasse med reell tilkopling til ei anna klasse
   (via containeren ELLER direkte) framleis ikkje vert flagga.
3. `make lint`/`make analyse-isolerte-klasser SCHEMA=...` køyrt mot minst
   to-tre eksisterande skjema for å stadfeste at rapportformatet framleis
   er gyldig Markdown og at `count_table_rows()`-talet i den genererte
   `### Isolerte klassar (N)`-overskrifta stemmer med tabellradene.

**Utanfor scope:** endring av `class_connections()` sjølv (korleis
tilkopling vert definert via slot-range/is_a/mixins) — berre korleis
containeren sine EIGNE utgåande kantar tel mot måla sin tilkoplingsstatus
vert endra.

## Akseptansekriterium

- [x] Klasse med KUN containertilkopling vert flagga med
      `Grunn = Kun tilkopla via containerklassen`
- [x] Klasse utan noka tilkopling i det heile vert framleis flagga med
      `Grunn = Heilt isolert`
- [x] Klasse med reell (ikkje-container) tilkopling — anten via containeren
      OG ein annan slot, eller berre ein annan slot — vert IKKJE flagga
- [x] `count_table_rows()` i `generate-modellanalyse-md.py` uendra, stemmer
      framleis med tabellradetalet i den nye eittabell-rapporten
- [x] `make analyse-isolerte-klasser SCHEMA=...` køyrt mot fleire
      eksisterande skjema utan feil

## Relaterte filer

- `src/assets/scripts/makefile/find-unused-local-definitions.py` —
  `find_isolated_classes()`, `class_connections()`, `format_report()`
- `mkdocs/lib/scripts/generate-modellanalyse-md.py` — `count_table_rows()`
  (uendra, men åtferd verifisert framleis korrekt)
- `specs/done/modellanalyse-ubrukte-lokale-definisjonar.md` — opphavleg
  spec som innførte `--kind class`/isolerte-klasser-sjekken

## Utført

**Endra filer:**

- `src/assets/scripts/makefile/find-unused-local-definitions.py`:
  - `find_isolated_classes()`: sporsar no `container_targets` (containeren
    sine eigne mål) separat frå resten av `connected_names`-oppbygginga —
    containeren sine EIGNE utgåande kantar tel ikkje lenger som reell
    tilkopling for måla. Returnerer `(name, description, reason)`, med
    `reason` = `REASON_ISOLATED` ("Heilt isolert") eller
    `REASON_CONTAINER_ONLY` ("Kun tilkopla via containerklassen").
  - `format_report()` (kind == "class"): ny `Grunn`-kolonne i tabellen,
    oppdatert summeringslinje som skil dei to kategoriane
    (`N isolerte/underintegrerte klassar ... (X heilt isolert, Y kun
    tilkopla via containerklassen)`).
  - `compute_items_and_total()`/`format_report()` sine typehint oppdatert
    til `list[tuple]` (både 2- og 3-tuple-former via same signatur).
  - Modul-docstring (linje 22-38) oppdatert til å skildre dei to
    kategoriane.

**Verifisering:**

- `make analyse-isolerte-klasser SCHEMA=.../enhetsregisteret-bvrinn-schema.yaml`:
  fann eit reelt container-only-tilfelle (`TypeAktivitet`, tidlegare
  usynleg) — stadfestar at endringa fangar det brukaren etterspurde.
- Same target køyrt mot `dcat-ap-no`, `ngr-adresse`, `samt-bu`,
  `fint-common`: alle rapporterer "Ingen isolerte lokale klassar funne" —
  stadfestar at klassar med reell (ikkje-container) tilkopling framleis
  ikkje vert flagga (ingen falske positive introdusert).
- Batch-modus (`make analyse-lokal-modellanalyse-domene DOMAIN=oreg
  OUT_DIR=generated/isolert-test-out`, mellombels katalog sletta etterpå
  — `generated/` er gitignora): identisk resultat som enkelt-skjema-kallet,
  stadfestar at CI-kjeftpaden (som brukar batch-modus) fungerer likt.
- `count_table_rows()` i `mkdocs/lib/scripts/generate-modellanalyse-md.py`
  testa direkte mot den nye rapporten: talet (1) stemmer med den eine
  tabellrada, og `### Isolerte klassar (1)`-overskrifta i den fullt
  rendra `## Modellanalyse`-seksjonen viser korrekt tal — ingen endring
  trengst i det forbrukande scriptet, som forventa i design-seksjonen.
- Python-syntaks verifisert med `ast.parse()`.
