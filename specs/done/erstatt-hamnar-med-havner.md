# Plan: erstatt «hamnar» med «havner» i dokumentasjon

## Bakgrunn

Brukaren ønskjer å byte ut nynorskforma **«hamnar»** (presens av verbet
«å hamne») med bokmålsforma **«havner»** i all dokumentasjon. Same
oppgåve står notert i `specs/backlog/TODO.md` linje 73 («hamnar -> havner»).

Dette er tredje tilfellet av same mønster som allereie er dokumentert i
CLAUDE.md § Navngjeving → «Unntak — enkeltord i bokmålsform»: eit
brukarstadfesta ord-nivå-unntak frå den generelle nynorsk-for-
dokumentasjon-regelen. Presedens: `namn`→`navn`
(`specs/done/namn-navn-konsistens-make-help.md`) og `artefaktar`→
`artefakter` (`specs/done/erstatt-artefaktar-med-artefakter.md`).

### Kartlegging

`grep -rIn -w "hamnar\|hamne\|hamna" .` (utanom `.git/` og `specs/done/`)
gir 5 treff, alle i verbforma «hamnar» («endar opp i»):

| Fil | Linje | Kontekst |
|---|---|---|
| `COMMANDS.md` | 331 | «Output-filer hamnar i `tmp/`.» |
| `mkdocs/docs/kom-i-gang/kommandoar.md` | 185 | same setning (manuelt vedlikehalden duplikat av COMMANDS.md, ikkje autogenerert) |
| `bugs/avrotize-falsk-circular-dependency-warning.md` | 62 | «Kva klassenavn som hamnar i åtvaringsmeldinga …» |
| `src/assets/scripts/makefile/help.sh` | 8 | kodekommentar: «hamnar berre under "Container images" …» |
| `specs/backlog/TODO.md` | 73 | sjølve TODO-notatet — fjernast når utført |

Ingen treff i `src/linkml/**` (modellering, bokmål) — som venta, sidan
«hamnar» er ei nynorsk verbform som berre finst i dokumentasjonslaget.
`mkdocs/site/` (build-output) er utanfor omfang — regenererast av
`make docs-publish`.

## Steg

1. **CLAUDE.md** — legg til rad `hamnar` → `havner` i tabellen under
   § Navngjeving → «Unntak — enkeltord i bokmålsform», med kryssreferanse
   til denne specen (etter flytting til `specs/done/`).
2. **COMMANDS.md:331** — «hamnar» → «havner».
3. **mkdocs/docs/kom-i-gang/kommandoar.md:185** — «hamnar» → «havner».
4. **bugs/avrotize-falsk-circular-dependency-warning.md:62** — «hamnar» → «havner».
5. **src/assets/scripts/makefile/help.sh:8** — kodekommentar «hamnar» → «havner».
6. **specs/backlog/TODO.md** — fjern linje 73 (oppgåva er utført).
7. Verifiser med `grep -rIn -w "hamnar" .` (utanom `.git/` og `specs/done/`) — skal gi null treff.

## Utført

Alle 7 steg gjennomførte. `hamnar` → `havner` retta i `COMMANDS.md`,
`mkdocs/docs/kom-i-gang/kommandoar.md`, `bugs/avrotize-falsk-circular-dependency-warning.md`
og `src/assets/scripts/makefile/help.sh`. CLAUDE.md-tabellen for
bokmålsforms-unntak utvida med `hamnar`/`havner`-rada. TODO.md-notatet
fjerna. Verifisert med `grep -rIn -w "hamnar" .` — ingen treff utanom
denne specen sjølv og CLAUDE.md-tabellrada (begge dokumenterer ordet, ikkje
brot på regelen).
