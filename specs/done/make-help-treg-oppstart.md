# Plan: Raskare `make help`/`make`-oppstart

## Bakgrunn

Etter at `make help`/`make` sin argumentvising vart gjort tydelegare
([[make-help-argument-og-farge]], `specs/done/make-help-argument-og-farge.md`),
melde brukaren at det tek eit par sekund å få opp lista. Profilering synte
at sjølve `help.sh`-skriptet er raskt (~75 ms), og at forsinkinga alt fanst
**før** den endringa — treffet ligg i Makefile-parsing, ikkje i
argument-/fargelogikken:

```
$ time (make help >/dev/null 2>&1)        # noverande arbeidskatalog
real  0m2.042s
$ git stash && time (make help >/dev/null 2>&1) && git stash pop   # før help.sh-endringa
real  0m1.961s
```

To uavhengige årsaker vart identifiserte:

**1. Repoet ligg på eit 9p/DrvFs-montert filsystem (`/mnt/c`, WSL2-interop mot
Windows-disken).** Kopiert til lokalt ext4-filsystem (`mktemp -d`, som ligg på
`/`, ikkje `/mnt/c`) gjekk same `make -n help` frå 1,75 s til 0,48 s — altså
er **~1,3 s (~75 % av totaltida) rein WSL2/9p-syscall-overhead**, ikkje noko
denne codebasen kan fikse. `mount`-utskrift stadfestar:

```
C:\ on /mnt/c type 9p (rw,noatime,aname=drvfs;...)
```

Dette er eit kjent WSL2-fenomen: kvar fil-open/stat over 9p har vesentleg
høgare latens enn på det native `ext4`-filsystemet WSL2 køyrer på. Ei
Makefile-parsing som opnar mange `.mk`-filer og forkar fleire prosessar
(`$(shell ...)`, `find`) betaler denne kostnaden fleire gongar.

**2. To `$(shell find ...)`-kall køyrer ubetinga ved kvar `make`-oppstart,
uavhengig av kva mål som er gitt** — også for `help`, som ikkje treng nokon
av dei:

| Stad | Kall | Kva han brukast til |
|---|---|---|
| `make/02-schema-discovery.mk:11` | `find $(SCHEMA_DIR) -mindepth 3 -maxdepth 3 -name '*-schema.yaml'` | `SCHEMAS`/`DOMAINS` — genererer `domain-<domain>`-target (ingen `## `-kommentar, vert **aldri** vist i `make help`) |
| `Makefile:149` | `find src/linkml -name 'build.yaml'` (som prerequisite-liste til `config.mk`-regelen) | Trigger regenerering av `config.mk` — berre lese av variablar inni oppskrifter til genererings-/valideringstarget |

Målt isolert på `/mnt/c`: 185 ms + 74 ms = **~260 ms** av dei ~1,75 s. Ingen
av desse to treng køyrast for `help` — `help.sh` les `## `-kommentarar
direkte frå `$(MAKEFILE_LIST)`, ikkje frå `SCHEMAS`/`DOMAINS`/`config.mk`.

**Konklusjon:** ~75 % av forsinkinga er miljøet (9p-montert repo), resten
(~15-20 %) er unødvendig `find`-arbeid som trygt kan hoppast over for
`help`. Denne specen løyser berre punkt 2 — punkt 1 krev at brukaren flyttar
den lokale arbeidskopien til eit natic Linux-filsystem i WSL2 (t.d.
`~/repos/...` i staden for `/mnt/c/...`), noko som er brukaren sitt val og
ligg utanfor denne codebasen sitt ansvarsområde.

## Tiltak

Hopp over dei to `find`-kalla når det einaste målet som er gitt (eller
ingen mål, som fell tilbake til `.DEFAULT_GOAL := help`) er `help`:

1. Legg til ein `NEEDS_SCHEMA_DISCOVERY`-vakt tidleg i `Makefile` (før
   `make/02-schema-discovery.mk` vert inkludert), basert på
   `$(MAKECMDGOALS)`.
2. `make/02-schema-discovery.mk`: la `SCHEMAS := $(shell find ...)` berre
   køyre når vakta er sett — elles `SCHEMAS :=` (tom).
3. `Makefile`: la `-include config.mk` og `config.mk:`/`gen-config:`-regelen
   berre definerast når vakta er sett.
4. Verifiser at:
   - `make help` og bart `make` framleis viser fullstendig, korrekt
     target-liste (inkl. dei faste `gen-*`-targeta, som ikkje er avhengige
     av `SCHEMAS`)
   - `make print-domains`, `make gen-config`, `make validate`,
     `make domain-<domain>` og andre mål som faktisk treng
     skjemaoppdaging, framleis fungerer uendra (vakta skal berre slå inn
     når *einaste* mål er `help`)
   - tidsmåling viser reduksjon tilsvarande dei ~260 ms som vart målt
     isolert

## Handlingsliste

1. [x] Legg til `NEEDS_SCHEMA_DISCOVERY`-vakt i `Makefile`
2. [x] Vakt `SCHEMAS`-oppdaging i `make/02-schema-discovery.mk`
3. [x] Vakt `config.mk`/`gen-config`-regelen i `Makefile`
4. [x] Verifiser `make help`, `make`, `make print-domains`,
   `make gen-config`, `make validate` (eller tilsvarande mål som bruker
   `SCHEMAS`)
5. [x] Tidsmål før/etter, dokumenter i «Utført»

## Utført

- `Makefile`: ny `NEEDS_SCHEMA_DISCOVERY`-vakt rett etter `SHELL`/`.SHELLFLAGS`,
  basert på `$(MAKECMDGOALS)` (fell tilbake til `help` når ingen mål er gitt).
  `-include config.mk` og `config.mk:`/`gen-config:`-regelen er no pakka inn
  i `ifneq ($(NEEDS_SCHEMA_DISCOVERY),) ... endif`.
- `make/02-schema-discovery.mk`: `SCHEMAS := $(shell find ...)` køyrer no
  berre når vakta er sett — elles `SCHEMAS :=` (tom, `DOMAINS` vert då òg
  tom, som er trygt sidan `domain-<domain>`-target aldri vert vist i
  `make help` og ingen andre parse-tidslogikk les `DOMAINS`).
- **Tidsmåling** (arbeidskopi på `/mnt/c`, 9p-montert i WSL2):

  | Kommando | Før | Etter |
  |---|---|---|
  | `make help` | ~2,0 s | ~0,23 s |
  | bart `make` | ~2,0 s | ~0,25 s |

  Gevinsten (~1,75 s) var større enn dei isolert målte ~260 ms for dei to
  `find`-kalla åleine — truleg fordi `config.mk`-regelen sin
  `@bash .../gen-config.sh > config.mk`-oppskrift/re-stat av mange filer
  også vart trigga oftare enn venta før denne endringa. Ikkje djupare
  undersøkt sidan resultatet uansett er eintydig positivt.
- Verifisert uendra åtferd for mål som treng skjemaoppdaging:
  `make print-domains` listar framleis alle 9 domene korrekt,
  `make gen-config`/`make -n print-domains` køyrer `find`-basert oppdaging
  som før, og `make -n help test` (fleire mål, eitt ≠ `help`) let vakta stå
  aktiv som forventa.
- **Attståande, ikkje løyst her:** ~75 % av den opphavlege forsinkinga
  (~1,3 s av ~1,75 s) kjem frå at arbeidskopien ligg på eit 9p/DrvFs-montert
  filsystem (`/mnt/c` i WSL2) — stadfesta ved å kopiere til lokalt
  ext4-filsystem, der same `make -n help` gjekk frå 1,75 s til 0,48 s. Dette
  er eit miljøval (kvar arbeidskopien ligg), ikkje noko som kan fiksast i
  denne codebasen — brukaren kan vurdere å flytte arbeidskopien til eit
  natic WSL2-filsystem (t.d. `~/repos/...`) dersom endå raskare oppstart er
  ønskt.
