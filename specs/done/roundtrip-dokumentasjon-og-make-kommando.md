# Roundtrip-dekning: dokumentasjon og eigen make-kommando

## Bakgrunn

Roundtrip-testar for JSON og TTL vart implementerte i `specs/done/roundtrip-testar.md`
og køyrer som del av `make test`. Det er to ting som manglar:

1. **Dokumentasjon av dekning** — det finst ingen plass der ein raskt kan sjå
   kva format kvart skjema støttar, kvifor nokre er hoppet over, og kva som
   krevst for å aktivere dei. Status ligg implisitt i skip-lista i `test_make.sh`.

2. **Isolert make-kommando** — `make test SCHEMA=...` køyrer alle 17 testar (~3 min).
   Det finst ingen måte å køyre berre roundtrip-testane raskt (10-30 sek) under
   utvikling.

---

## Del 1 — Dokumentasjon av roundtrip-dekning

### Kva som manglar

Skip-betingelsane i `test_make.sh` seier *kva* som er hoppet over, men ikkje:
- Kva format som er *aktivt testa* for kvart skjema
- Kvifor TTL-roundtrip er deaktivert for eit domene
- Kva som krevst for å aktivere eit format (skjema-endringar? upstream-fix?)

### Kvar dokumentasjonen bør liggje

Roundtrip-dekning er ikkje ein feil — det er ein oversikt over kva testsuiten
dekker. Han høyrer naturleg heime i `tests/README.md`, som i dag berre har to
linjer. Ein ny brukar som utforskar `tests/`-mappa finn dette umiddelbart.

`specs/bugs/` er for sporing av konkrete feil med workarounds. Å leggje
test-dekningstabellar der blandar to ulike ansvarsområde og gjev feil forventning
til kva bugs-mappa inneheld.

### Løysing — utvid `tests/README.md`

Erstatt det minimale innhaldet i `tests/README.md` med ei fullstendig
testoversikt:

```markdown
# tests/

Oversikt over kva testane dekker, korleis dei køyrer, og status per skjema.

## Testsuite (`test_make.sh`)

`make test [SCHEMA=<sti>]` køyrer alle testar via `tests/test_make.sh`.
Kvar skjema-køyring utfører 17 testar parallelt (generatorar, lint, roundtrip).

| Test | Kva det sjekkar |
|---|---|
| validate | gen-linkml kan lese skjemaet |
| gen-jsonld / gen-python / gen-jsonschema / … | generator produserer gyldig artefakt |
| linkml-lint | skjema følgjer LinkML best practices |
| linkml-validate | eksempelfil er gyldig mot skjema |
| roundtrip-json | yaml→json→yaml→json er informasjonstap-fri |
| roundtrip-ttl | yaml→ttl→yaml→json er informasjonstap-fri |

## Roundtrip-dekning

«✓» = passerer. «skip» = hoppet over (sjå årsak). Lenker peikar til bugdokumentasjon.

| Skjema | JSON | TTL | Årsak til skip |
|---|---|---|---|
| samt-bu | ✓ | ✓ | |
| brreg-begrepskatalog | ✓ | skip | [BUG-1](../specs/bugs/langstring-rdflib-roundtrip.md) |
| brreg-modellkatalog | ✓ | skip | [BUG-1](../specs/bugs/langstring-rdflib-roundtrip.md) |
| fint-arkiv | ✓ | ✓ | |
| fint-ressurs | ✓ | ✓ | |
| fint-administrasjon | skip | skip | URI/CURIE-bug i eksempeldata |
| fint-okonomi | skip | skip | same |
| fint-personvern | skip | skip | same |
| fint-utdanning | skip | skip | same |
| ngr-adresse | ✓ | skip | [BUG-2](../specs/bugs/inlined-as-list-rdflib-roundtrip.md) |
| ngr-eiendom | ✓ | skip | [BUG-2](../specs/bugs/inlined-as-list-rdflib-roundtrip.md) |
| ngr-virksomhet | ✓ | skip | [BUG-2](../specs/bugs/inlined-as-list-rdflib-roundtrip.md) |
| ap-no, fair (alle) | skip | skip | manglar `tree_root` |

Tabellen skal haldast oppdatert når skip-lista i `test_make.sh` endrar seg.
```

### Alternativ vurdering: per-skjema `manifest.yaml`-flagg

```yaml
roundtrip:
  json: true
  ttl: skip-bug-1
```

**Vurdering:** For mykje overhead — `manifest.yaml` er for generatorkonfig, ikkje
test-status. Krev endring i 12+ filer ved kvar statusoppdatering.
**→ Forkasta. Bruk sentral tabell i `tests/README.md`.**

---

## Del 2 — `make roundtrip SCHEMA=...`

### Motivasjon

Under utvikling er det typisk å ville verifisere at ein skjema-endring ikkje bryt
roundtrip. `make test` tek 3-5 minutt per skjema (alle 17 testar, fleire podman-kall).
Roundtrip-testane åleine tek 10-30 sekund.

Ein dedikert `make roundtrip SCHEMA=...` gjev rask feedback i same arbeidsflyt
som `make lint` og `make validate-instance`.

### Implementasjonsalternativ

**Alternativ A — `--only`-flagg i `test_make.sh` (anbefalt)**

Legg til støtte for `TEST_FILTER`-miljøvariabel i `test_make.sh` som filtrerer
kva testar `_run_one` køyrer:

```bash
# I _run_one:
_run_one() {
    local tname="$1"; shift
    # Hopp over om TEST_FILTER er sett og tname ikkje startar med filteren
    if [[ -n "$TEST_FILTER" && "$tname" != ${TEST_FILTER}* ]]; then
        return 0
    fi
    ...
}
```

`make roundtrip` set `TEST_FILTER=roundtrip` og kallar `test_make.sh`:

```makefile
roundtrip:
	@echo "$(CLR_HDR)*** make roundtrip$(if $(SCHEMA),  SCHEMA=$(SCHEMA),)$(CLR_RST)"
	TEST_FILTER=roundtrip bash tests/test_make.sh "$(SCHEMA)"
```

Fordel: eitt kodestedstad for all testkjøring; ingen duplikering.
Ulempe: `test_make.sh` startar framleis alle bakgrunnsprosessar, men dei fleste
testfunksjonane returnerer tidleg — overhead er liten.

**Alternativ B — eiga `tests/test_roundtrip.sh`**

Eige skript som berre importerer og køyrer roundtrip-funksjonane:

```bash
source tests/test_roundtrip_lib.sh   # delt bibliotekar
run_roundtrip "$SCHEMA"
```

Fordel: ingen risiko for å treffe andre testar.
Ulempe: duplisert logikk for schema-oppdaging, logging og skip-betingelser.
**→ Forkastet. Alternativ A er enklare og tryggare.**

**Alternativ C — kall `test_make.sh` og grep ut berre roundtrip-linjer**

```makefile
roundtrip:
	bash tests/test_make.sh "$(SCHEMA)" 2>&1 | grep -E "roundtrip|Resultat"
```

Fordel: ingen endringar i `test_make.sh`.
Ulempe: køyrer framleis alle 17 testar (ingen tidsvinst); output er berre filtrert.
**→ Forkastet. Gjev ikkje tidsvinst.**

### Val: Alternativ A

`TEST_FILTER`-tilnærminga er minimal, gjenbrukbar og kan utvidast — t.d.
`TEST_FILTER=gen-` for å køyre berre generatortestar, eller
`TEST_FILTER=linkml-` for linting.

### Brukargrensesnitt

```bash
# Køyr alle roundtrip-testar for eitt skjema:
make roundtrip SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml

# Køyr berre roundtrip for alle skjema (heile repoet):
make roundtrip
```

Output følgjer same format som `make test` — grøne OK / raude FEIL.

### CLAUDE.md-oppdatering

Legg til `make roundtrip` i «Valider arbeidet ditt»-seksjonen i `CLAUDE.md`:

```bash
# Rask roundtrip-verifisering etter skjema-endringar:
make roundtrip SCHEMA=src/linkml/<domain>/<modell>/<modell>-schema.yaml
```

---

## Tiltaksliste

| # | Tiltak | Fil | Prioritet |
|---|---|---|---|
| 1 | Legg til `TEST_FILTER`-støtte i `_run_one` i `test_make.sh` | `tests/test_make.sh` | Høg |
| 2 | Legg til `roundtrip`-target i `Makefile` | `Makefile` | Høg |
| 3 | Verifiser at `make roundtrip SCHEMA=...` berre køyrer roundtrip-testar og gjev rett resultat | — | Høg |
| 4 | Erstatt `tests/README.md` med fullstendig testoversikt og roundtrip-dekningstabell | `tests/README.md` | Medium |
| 5 | Legg til `make roundtrip` i «Valider arbeidet ditt» i `CLAUDE.md` | `CLAUDE.md` | Medium |

## Utført

Alle tiltak gjennomførte. Avvik frå opphavleg plan er dokumentert under.

### Kva som vart gjort

**Tiltak 1-2:** `TEST_FILTER`-støtte lagt til i `_run_one` og `roundtrip`-target lagt til i `Makefile`. `make roundtrip` køyrer no berre dei to roundtrip-testane (~30 sek) framfor alle 17 (~3 min).

**Tiltak 3:** Verifisert at `make roundtrip SCHEMA=...` berre viser `roundtrip-json` og `roundtrip-ttl` i output. `TEST_FILTER` er gjenbrukbar for andre prefiks (t.d. `TEST_FILTER=linkml-` for lint-testar).

**Tiltak 4:** `tests/README.md` erstatta med fullstendig testoversikt og roundtrip-dekningstabell. Tabellen vart bygd på faktiske testresultat frå `make roundtrip` (full suite), ikkje berre spec-en sine estimat.

**Avvik frå spec — ny bug oppdaga:** Under gjennomføring av tiltak 3 vart ein tredje ukjend TTL-roundtrip-feil avdekka: `MappingError: No pred for <domene-URI>` i `fint-administrasjon`, `fint-okonomi`, `fint-personvern`, `fint-utdanning` og `samt-bu`. Desse er ikkje i skip-lista — dei køyrer og feiler. Ny bugfil `specs/bugs/mappingerror-rdflib-roundtrip.md` (BUG-3) oppretta og lagt til i `specs/bugs/README.md` og `tests/README.md`.

**Tiltak 5:** `make roundtrip` lagt til i «Valider arbeidet ditt» i `CLAUDE.md`.
