# Plan: `namn`→`navn`-konsistens mellom `make help` og `COMMANDS.md`
# (+ CLAUDE.md-oppdatering: dokumenter unntak frå nynorsk-regelen)

## Bakgrunn

Brukaren merka fleire førekomstar av plasshaldarordet **`namn`** (nynorsk)
i `make help`-output, og bad om ei kartlegging av alle førekomstar i
`help.sh` og `COMMANDS.md`, samt ein plan for å erstatte med **`navn`**.

### Kartlegging

`help.sh` sjølv inneheld ikkje `namn` som plasshaldartekst — han er ein
reint generisk renderar som les `## `-kommentarane frå `make/*.mk` direkte.
Førekomstane av `namn` i `help.sh` er difor utelukkande i skriptet sine
**eigne interne kodekommentarar** (utviklarvendte, ikkje CLI-output):
`targetnamn`, `filnamn`, `namnekolonna` osv. — samansette nynorskord som
korrekt følgjer CLAUDE.md sin dokumentasjonskonvensjon, og som **ikkje**
er del av det brukaren ser i terminalen. Desse er difor **utanfor
omfanget** til denne specen.

Dei faktiske `namn`-førekomstane brukaren har sett i `make help`-**output**
kjem frå `NAME=`-plasshaldarane i `## `-kommentarane i `make/70-scaffolding.mk`
(kjelda `help.sh` renderer frå). Samanlikna med tilsvarande rader i
`COMMANDS.md`:

| Target | `make help` (kjelde: `make/70-scaffolding.mk`) | `COMMANDS.md` | Status |
|---|---|---|---|
| `new-modell` | `NAME=<namn>` | `NAME=<modell>` | **Ulikt ord**, ikkje berre ulik skrivemåte |
| `remove-modell` | `NAME=<namn>` | `NAME=<modell>` | **Ulikt ord** |
| `new-begrepssamling` | `NAME=<begrepssamling-namn>` | `NAME=<begrepssamling-navn>` | Same ord, ulik skrivemåte (nynorsk/bokmål) |
| `new-begrepskatalog` | `NAME=<katalognavn>` | `NAME=<katalognavn>` | Alt konsistent (bokmål «navn» begge stader) |

`mkdocs/docs/kom-i-gang/{kommandoar,ny-domenemodell,ny-org,ny-begrepsmodell}.md`
stadfestar same biletet — dei nyttar konsekvent `<modell>`/`<katalognavn>`,
aldri `<namn>`. `COMMANDS.md` + mkdocs-laget er difor alt internt
konsistent på «navn/modell»-sida; det er **berre kjeldekommentarane i
`make/70-scaffolding.mk`** (og dermed `make help`-output) som avvik, med
nynorskforma `namn`.

**Avklart — CLAUDE.md skal oppdaterast, ikkje berre kodetilfelle:**
`namn` er den korrekte nynorskforma, `navn` er bokmål. CLAUDE.md sitt
språkkapittel (§ Skriftspråk) seier dokumentasjon skal vere nynorsk, utan
unntak nemnde. Brukaren har stadfesta at «navn» (ikkje «namn») skal brukast
i dokumentasjon, og at dette unntaket skal **dokumenterast i CLAUDE.md
sjølv** — ikkje berre rettast stilltiande i enkelttilfelle.

Det finst alt eitt presedens for nett dette mønsteret: eit tidlegare,
brukarstyrt tiltak bytte ordet **«artefaktar» → «artefakter»** (bokmål)
**overalt i levande dokumentasjon** — inkludert i nynorsk-filer som
CLAUDE.md, GOVERNANCE.md, PRINCIPLES.md, SCOPE.md — sjå
`specs/done/erstatt-artefaktar-med-artefakter.md`. Det tiltaket vart
gjennomført (67 filer retta), men **konklusjonen vart aldri skriven inn i
CLAUDE.md sitt språkkapittel** — sjølve unntaket frå nynorsk-regelen
finst difor berre implisitt, som eit spor i `specs/done/`, ikkje som ein
gjeldande, lesbar regel. Stadfesta via `grep`: CLAUDE.md brukar i dag
«artefakter» 3 gonger, aldri «artefaktar» — men CLAUDE.md sin eigen tekst
seier ingenting om at dette er eit medvite unntak.

`namn`→`navn` er difor **det andre tilfellet av same mønster**: eit
ord-nivå-unntak frå den generelle nynorsk-for-dokumentasjon-regelen, som
bør dokumenterast eksplisitt i CLAUDE.md på same måte som
artefaktar/artefakter burde vore det.

**Biprodukt oppdaga under kartlegginga:** `mkdocs/docs/arkitektur/arkitektur-oversikt.md`
har enno eitt attverande `artefaktar`-tilfelle, gøymt i samansettinga
«skjema**artefaktar**» (linje 242) — truleg forbigått av det opphavlege
tiltaket sitt ordgrense-søk (`\bartefaktar\b` matchar ikkje inni ei
samansetjing utan bindestrek). Ikkje del av kjerneomfanget her (gjeld
`artefakter`, ikkje `namn`/`navn`), men nemnt sidan det dukka opp i same
gjennomgang — kan takast som eit lite tillegg i steg 4.

## Plan

**Steg 1 — `new-begrepssamling`: rein skrivemåte-retting**
`make/70-scaffolding.mk` sitt `<begrepssamling-namn>` → `<begrepssamling-navn>`,
3 førekomstar (## kommentar + 2×`log_error`). Ingen ordskifte, berre
nynorsk→bokmål-skrivemåte, gjer `make help`-output identisk med
`COMMANDS.md` sitt alt eksisterande `<begrepssamling-navn>`.

**Steg 2 — `new-modell`/`remove-modell`: to alternativ**

| Alternativ | Endring | Fordel | Ulempe |
|---|---|---|---|
| **A — berre skrivemåte** (minimal) | `<namn>` → `<navn>` i `make/70-scaffolding.mk` (4 førekomstar) | Minst mogleg diff, løyser presist det brukaren peika på (namn→navn) | `make help` viser framleis eit **anna ord** (`<navn>`) enn `COMMANDS.md`/mkdocs (`<modell>`) — løyser ikkje heile inkonsistensen |
| **B — full harmonisering (anbefalt)** | `<namn>` → `<modell>` i `make/70-scaffolding.mk` (4 førekomstar) — matchar det alt etablerte, meir presise ordet frå `COMMANDS.md`/mkdocs | `make help` og `COMMANDS.md`/mkdocs vert **heilt identiske** for desse to targeta — same mønster som `SCHEMA`/`ORG`-harmoniseringane gjort tidlegare i denne økta | Litt større endring enn ei rein staveretting; `<modell>` er ikkje bokstaveleg «namn→navn» |

**Steg 3 — `new-begrepskatalog`: ingen endring** — alt konsistent.

**Steg 4 — Oppdater CLAUDE.md § Skriftspråk**
Legg til eit eksplisitt unntaks-avsnitt rett under skriftspråk-tabellen i
CLAUDE.md, som dokumenterer at desse to ordpara er unntekne frå den
generelle nynorsk-for-dokumentasjon-regelen, og alltid skal skrivast i
bokmålsforma sjølv i elles nynorsk tekst:

| Nynorsk (IKKJE bruk) | Bokmål (BRUK) | Grunngjeving |
|---|---|---|
| namn | navn | Stadfesta av brukaren; alt de-facto-standard i `COMMANDS.md`/mkdocs |
| artefaktar | artefakter | Tidlegare brukarstyrt tiltak, `specs/done/erstatt-artefaktar-med-artefakter.md` — aldri innskrive i CLAUDE.md sjølv, før no |

Formuleringsforslag (kan justerast ved utføring):

```markdown
**Unntak — enkeltord i bokmålsform:** Desse orda skal alltid skrivast i
bokmålsforma, sjølv i elles nynorsk dokumentasjonstekst (README, mkdocs,
`COMMANDS.md`, spec-filer i `specs/backlog/`):

| Nynorsk (unngå) | Bruk i staden |
|---|---|
| namn | navn |
| artefaktar | artefakter |

Desse er historiske, brukarstadfesta unntak — ikkje eit generelt skifte til
bokmål. `specs/done/` er urørt (arkivert, jf. DRY-unntaket over).
```

## Filer som vert påverka

- `make/70-scaffolding.mk` — `## `-kommentarar + `log_error "Bruk: ..."`-meldingar
  for `new-modell`, `remove-modell`, `new-begrepssamling`
- `CLAUDE.md` — nytt unntaks-avsnitt i § Skriftspråk (steg 4)
- Valfritt: `mkdocs/docs/arkitektur/arkitektur-oversikt.md` (linje 242,
  «skjemaartefaktar» → «skjemaartefakter» — biprodukt, ikkje kjerneomfang)
- Ingen endring naudsynt i `COMMANDS.md`, mkdocs kom-i-gang-sidene eller
  `src/assets/scripts/scaffolding/*.sh` (dei brukar alt korrekt
  ord/skrivemåte, eller bryr seg ikkje om plasshaldarteksten i det heile —
  skripta les berre `$1`/`$2` posisjonelt, uavhengig av kva `##`-kommentaren
  syner)

## Handlingsliste

1. [x] Vel alternativ A eller B for `new-modell`/`remove-modell` — **B** valt
   (full harmonisering til `<modell>`, konsistent med SCHEMA/ORG-mønsteret
   frå resten av økta)
2. [x] Rett `new-begrepssamling` (`<begrepssamling-namn>` → `<begrepssamling-navn>`)
3. [x] Rett `new-modell`/`remove-modell` etter valt alternativ
4. [x] Legg til unntaks-avsnittet i CLAUDE.md § Skriftspråk (namn/artefaktar)
5. [x] Vurder «skjemaartefaktar» → «skjemaartefakter» i
   `arkitektur-oversikt.md` (biprodukt frå kartlegginga)
6. [x] Verifiser med `make help` at alle fire NAME-target no viser same
   ord/skrivemåte som tilsvarande rad i `COMMANDS.md`

## Utført

- `make/70-scaffolding.mk`: `new-modell`/`remove-modell` sitt
  `NAME=<namn>` → `NAME=<modell>` (## kommentar + `log_error`, 4
  førekomstar), `new-begrepssamling` sitt `<begrepssamling-namn>` →
  `<begrepssamling-navn>` (## kommentar + 2×`log_error`, 3 førekomstar).
  `new-begrepskatalog` urørt (alt konsistent).
- `CLAUDE.md` § Skriftspråk: nytt unntaks-avsnitt rett under
  «Unntak for Modellmetadata-tabellen», med tabell (namn→navn,
  artefaktar→artefakter) og kryssreferanse til denne specen +
  `erstatt-artefaktar-med-artefakter.md`.
- `mkdocs/docs/arkitektur/arkitektur-oversikt.md`: «skjemaartefaktar» →
  «skjemaartefakter» (biprodukt frå kartlegginga).
- **Verifisert** med `make help`: `new-modell`, `remove-modell`,
  `new-begrepssamling`, `new-begrepskatalog` viser no plasshaldarar som
  er ordrett identiske med tilsvarande rader i `COMMANDS.md`.
- **Verifisert** at ingen `artefaktar`-førekomstar attstår utanfor
  `specs/done/` — dei to attverande treffa (`CLAUDE.md`, denne specen)
  er begge legitime: ordet nemnt *som eksempel på kva som skal unngåast*
  i unntakstabellen, ikkje faktisk bruk.
