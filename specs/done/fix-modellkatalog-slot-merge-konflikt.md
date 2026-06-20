# Fix: `make modellkatalog` krasjar med «Conflicting URIs» for duplikatslots

## Bakgrunn

`make modellkatalog` feiler i `gen-jsonld-context`-steget for
`brreg-modellkatalog-schema.yaml`:

```
ValueError: Conflicting URIs (https://data.norge.no/ap-no/dcat-ap-no, https://data.norge.no/ap-no/modelldcat-ap-no/katalog) for item: tema
```

Dette er **same rotårsak som BUG-6** (`specs/bugs/dqv-standard-class-override.md`),
men på slot-nivå i stedet for klasse-nivå: `linkml/utils/mergeutils.py::merge_dicts`
kastar `ValueError` så snart eit element-namn (klasse ELLER slot) finst i meir
enn eitt skjema i importgrafen med ulik `from_schema` — **uavhengig av om
definisjonane er identiske**. Dette gjelder for `gen-jsonld-context`,
`gen-python`, `gen-rdf` og `linkml-convert` (alle SchemaLoader-baserte
generatorar), og dermed òg `make roundtrip`.

Verifisert empirisk (testa lokalt, endringane er reverterte før denne specen
blei skrive): det finst **to separate forekomstar** av dette mønsteret i
importkjeda til `brreg-modellkatalog-schema.yaml` →
`modelldcat-ap-no-schema.yaml` → (`modelldcat-katalog-schema.yaml` +
`modelldcat-modell-schema.yaml`) → `dcat-ap-no-schema.yaml`:

### Forekomst 1: `modelldcat-katalog-schema.yaml` redeklarerer 4 slots frå `dcat-ap-no-schema.yaml`

`modelldcat-katalog-schema.yaml` importerer `dcat-ap-no-schema.yaml` (sidan
MC8, commit `4b4bad4f`), men har samtidig sin **eigen** globale deklarasjon
av 4 slotnamn som òg finst i `dcat-ap-no-schema.yaml`:

| Slot | Range i `dcat-ap-no` | Range i `modelldcat-katalog` (lokal) |
|---|---|---|
| `tema` | `Konsept` | `Konsept` (no identisk — sjå nedanfor) |
| `lisens` | `string` | `Lisensdokument` |
| `har_del` | `Katalog` | `KatalogisertRessurs` |
| `erstatter` | `Datasett` | `Informasjonsmodell` |

Kommentarane i fila (`# tema: range er Konsept (ikkje uriorcurie som i
dcat-ap-no)`) er **forelda**: `dcat-ap-no-schema.yaml` sin `tema`-range blei
endra frå `uriorcurie` → `Konsept` i commit `f93510f3`, slik at den no er
byte-identisk med den lokale overstyringa. Men identisk innhald hjelper
ikkje — `merge_dicts` ser kun på `from_schema`, ikkje innhald, så krasjen
inntreffer uansett.

Truleg har dette vore eit latent brot sidan MC8 (`4b4bad4f`), og blei først
synleg no fordi `make modellkatalog` ikkje er dekt av `tests/test_make.sh`
sine roundtrip-/lint-testar i dag (sjå Referanse-seksjonen).

### Forekomst 2: `modelldcat-modell-schema.yaml` og `dcat-ap-no-schema.yaml` deklarerer begge `begrep` — ulik semantikk

```yaml
# dcat-ap-no-schema.yaml
begrep:
  slot_uri: dct:subject
  range: string
  description: Fagomgrep som datasettet handlar om.

# modelldcat-modell-schema.yaml
begrep:
  slot_uri: dct:subject
  range: Konsept
  description: Fagomgrep ressursen handlar om (dct:subject).
```

Dette er strukturelt vanskelegare enn forekomst 1: ingen av desse to skjemaa
importerer det andre — dei er **søsken** som begge blir importerte av
`modelldcat-katalog-schema.yaml`. `slot_usage` på importør-nivå kan derfor
ikkje løyse konflikten (det er ikkje ei lokal redeklarering i importøren,
men ein kollisjon mellom to importerte skjema).

`begrep` (range `Konsept`) brukast av 4 klassar: `Modellelement`, `Egenskap`
(begge i `modelldcat-modell-schema.yaml`) og `Informasjonsmodell` (i
`modelldcat-katalog-schema.yaml`). Per CLAUDE.md («`dct:subject`
(`begrep`-slot) peikar til fagomgrep i begrepskatalog — ikkje til Los») og
prinsippet «Lenking fremfor inlining» skal `begrep` peike til ein `Konsept`,
ikkje vere ein fri streng — så `dcat-ap-no` sin `range: string`-variant ser
ut til å vere den utdaterte/avvikande, ikkje motsatt (same mønster som
`tema` før commit `f93510f3`).

Verifisert: ingen andre skjema i repoet importerer
`modelldcat-ap-no-schema.yaml` (eller delfilene direkte) utanom
`brreg-modellkatalog-schema.yaml`, så blastradiusen for forekomst 2 er
avgrensa til denne kjeda — **men** ei endring av `dcat-ap-no-schema.yaml`
sin `begrep`-range påvirkar potensielt alle domenemodellar som importerer
`dcat-ap-no-schema.yaml` (svært mange, via AP-NO-importhierarkiet).

**Avgjort:** `dcat-ap-no-schema.yaml` skal definere `begrep` med
`range: Konsept` (Alternativ A nedanfor). `range: string` var avviket, ikkje
motsatt — konsistent med korleis `tema` allereie blei migrert til `Konsept`
i `f93510f3`, og med CLAUDE.md-prinsippet om lenking fremfor inlining for
fagomgrep.

## Alternativ

### For forekomst 1 (verifisert løysing)

Fjern dei 4 globale slot-redeklarasjonane frå `modelldcat-katalog-schema.yaml`
sin `slots:`-blokk, og flytt range-overstyringa inn i `slot_usage` på dei
klassane som trenger avvikande range frå `dcat-ap-no` sin versjon (same
mønster som allereie brukast for `er_del_av`/`har_del` på `Informasjonsmodell`
i fila i dag):

```yaml
# Modellkatalog.slot_usage
lisens:
  range: Lisensdokument
  in_subset: [Anbefalt]
har_del:
  range: KatalogisertRessurs
  in_subset: [Anbefalt]

# Informasjonsmodell.slot_usage
lisens:
  range: Lisensdokument
  in_subset: [Anbefalt]
erstatter:
  range: Informasjonsmodell
  in_subset: [Valgfri]
# tema: ingen range-overstyring nødvendig — identisk med dcat-ap-no sin Konsept-range
```

Testa lokalt: dette løyser krasjen for `tema`/`lisens`/`har_del`/`erstatter`
heilt (verifisert at heile `make modellkatalog`-pipelinen kjem forbi disse
4 og treffer forekomst 2 sin `begrep`-konflikt som neste feil).

### For forekomst 2 — avgjort: Alternativ A

**Alternativ A (vald):**
Harmoniser `dcat-ap-no-schema.yaml` sin `begrep`-range frå `string` → `Konsept`
(speil av korleis `tema` allereie blei migrert i `f93510f3`), og fjern den
lokale `begrep`-deklarasjonen i `modelldcat-modell-schema.yaml` heilt (rein
duplikat etter harmonisering). Risiko: påvirkar `Datasett.begrep` og alle
domenemodellar som importerer `dcat-ap-no-schema.yaml` — eksisterande
eksempel-/datafiler med `begrep: "fritekst"` må migrere til
`Konsept`-objekt/URI-referansar. Krev grep gjennom alle eksempel- og
produksjonsdatafiler for `begrep:`-bruk under `Datasett` før gjennomføring.

**Alternativ B (forkasta):**
Behalde `dcat-ap-no` sin `begrep` uendra (`range: string`) og gje
`modelldcat-modell-schema.yaml` sin variant eit eige, ikkje-kolliderande
slotnamn. Forkasta fordi det bryter med at `begrep` skal vere det kanoniske
namnet for `dct:subject` per CLAUDE.md.

## Prioritert tiltaksliste

| # | Tiltak | Prioritet |
|---|---|---|
| 1 | ✓ Fjern duplikat-slots `tema`, `lisens`, `har_del`, `erstatter` frå `modelldcat-katalog-schema.yaml` sin `slots:`-blokk | Høg |
| 2 | ✓ Legg til `range`-overstyring i `slot_usage` for `lisens` (begge klassar), `har_del` (Modellkatalog) og `erstatter` (Informasjonsmodell) | Høg |
| 3 | ✓ Køyr `make modellkatalog` og verifiser at feilen flyttar seg til `begrep`-konflikten (forventa, sjå forekomst 2) | Høg |
| 4 | ✓ Endre `dcat-ap-no-schema.yaml.begrep.range` frå `string` → `Konsept` | Høg |
| 5 | ✓ Grep gjennom alle eksempel- og produksjonsdatafiler for `begrep:`-bruk under `Datasett` (og andre dcat-ap-no-klassar) og migrer fritekst-verdiar til `Konsept`-objekt/URI-referansar — verifisert: ingen eksempel- eller produksjonsdatafiler brukar `Datasett.begrep` i dag, ingen migrering nødvendig | Høg |
| 6 | ✓ Fjern den lokale `begrep`-deklarasjonen i `modelldcat-modell-schema.yaml` (rein duplikat etter harmonisering i steg 4) | Høg |
| 7 | ✓ Køyr `make modellkatalog` fullt ut til alle generatorar (`shacl`, `python`, `json-schema`, `owl`, `rdf`, `docs`, `erdiagram`, `proto`, `openapi`) lukkast | Høg |
| 8 | ✓ Køyr `make validate-instance` mot `brreg-modellkatalog-eksempel.yaml` og produksjonsdatafila (begge: «No issues found»), samt mot `samt-bu-eksempel.yaml` (downstream-konsument av `dcat-ap-no-schema`, «No issues found») — ingen valideringsbrot frå range-endringa. (`dqv-ap-no`/`dcat-ap-no` sine eigne eksempel kan ikkje køyrast med `validate-instance` då dei er AP-NO-profilskjema utan `tree_root`-container, uavhengig av denne endringa) | Høg |
| 9 | ✓ Køyr `make roundtrip SCHEMA=src/linkml/modellkatalog/brreg-modellkatalog/brreg-modellkatalog-schema.yaml` for å verifisere at JSON/TTL-roundtrip fungerer — `roundtrip-json` og `roundtrip-ttl` begge OK | Medium |
| 10 | ✓ Vurder å leggje `modellkatalog`-domenet til i `tests/test_make.sh` sine generate-/roundtrip-testar — verifisert: `brreg-modellkatalog-schema.yaml` blir allereie auto-oppdaga (`find -mindepth 3 -maxdepth 3`, ingen skip-betingelse) og dekt av alle 17 testar (inkl. `gen-jsonld`, `roundtrip-json/ttl`); køyrt på nytt etter fiksen — 17 OK, 0 feil. Ingen tilleggsendring nødvendig i `test_make.sh` | Medium |
| 11 | ✓ Dokumenter det generelle mønsteret («unngå duplikate globale slot-namn på tvers av importerte skjema, same regel som BUG-6 for klassar») i `specs/bugs/README.md` som ny BUG-post, og lenk til denne specen — lagt til som `specs/bugs/duplicate-slot-merge-konflikt.md` (BUG-7) | Lav |

## Referanse

Relatert kjend feil: `specs/bugs/dqv-standard-class-override.md` (BUG-6) —
same `merge_dicts`-mekanisme, men for klasse-redeklarering. Generell regel
derifrå gjeld òg her: «unngå å redeklarere eit element som er definert i eit
importert skjema».

**Korrigering etter tiltak 10:** `brreg-modellkatalog-schema.yaml` var
allereie auto-oppdaga og dekt av `tests/test_make.sh` (ingen skip-betingelse).
Kvifor regresjonen frå `f93510f3` (`dcat-ap-no.tema.range` → `Konsept`)
likevel ikkje blei fanga opp tidligere, er ikkje fullstendig klarlagt — truleg
har ikkje den fulle testsuiten vore køyrt mot dette skjemaet sidan MC8
(`4b4bad4f`) før no.

## Utført

Alle 11 tiltak gjennomførte som planlagt, ingen avvik frå planen:

- `modelldcat-katalog-schema.yaml`: fjerna duplikat-deklarasjonane `tema`,
  `lisens`, `har_del`, `erstatter` frå `slots:`-blokka; range-overstyringa
  for `lisens` (Modellkatalog + Informasjonsmodell), `har_del`
  (Modellkatalog) og `erstatter` (Informasjonsmodell) flytta inn i
  `slot_usage`. `tema` trengte ingen overstyring (allereie identisk range
  via import).
- `dcat-ap-no-schema.yaml`: `begrep.range` endra frå `string` → `Konsept`.
  Verifisert at ingen eksempel- eller produksjonsdatafiler brukar
  `Datasett.begrep` i dag, så ingen instansdata-migrering var nødvendig.
- `modelldcat-modell-schema.yaml`: fjerna den no-duplikate `begrep`-deklarasjonen.
- `make modellkatalog` (alle 14 generatorar), `make validate-instance`
  (brreg-modellkatalog-eksempel, produksjonsdatafil, samt-bu-eksempel) og
  `make roundtrip` for `brreg-modellkatalog-schema.yaml` køyrer alle grønt.
- `tests/test_make.sh src/linkml/modellkatalog/brreg-modellkatalog/brreg-modellkatalog-schema.yaml`
  (17 testar, inkl. `gen-jsonld`, `roundtrip-json`, `roundtrip-ttl`):
  17 OK, 0 feil. Domenet var allereie auto-dekt av testsuiten — ingen
  endring i `test_make.sh` var nødvendig.
- Ny `specs/bugs/duplicate-slot-merge-konflikt.md` (BUG-7) dokumenterer det
  generelle mønsteret (slot-variant av BUG-6) og lenkar tilbake til denne
  specen; lagt til i `specs/bugs/README.md`-indeksen.
