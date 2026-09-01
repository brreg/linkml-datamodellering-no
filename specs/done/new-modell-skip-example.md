# Plan: `SKIP_EXAMPLE`-flagg for `make new-modell`

## Bakgrunn

`make new-modell` (via `new-modell.sh`) genererer alltid syntetisk
eksempeldata for den nye modellen ved å køyre
`mcp-linkml-modell-utkast/validator.py` i ein podman-container. Dette
steget må laste heile importkjeda til skjemaet (transitivt via
`SchemaView`) — for eit nyoppretta skjema med det vanlege
versjonslåste `raw.githubusercontent.com`-importet av `dcat-ap-no-schema`
(sjå `mkdocs/docs/arkitektur/importhierarki.md`) krev det **nettverk**.

`javazone-demo-script.sh` er eksplisitt meint å vere offline-sikker (sjå
tittelen "10-minutters demo av repoet (offline-sikker)" i
`javazone-demo-plan.md`), men steg 3 (`make new-modell`, kalla både frå
den interaktive greina og frå `QUICK=true`-greina) trigga likevel eit
nettverkskall via dette steget. Utan nettverk feilar kallet med
`socket.gaierror`, og scriptet fell tilbake til ein minimal stub — funksjonelt
ufarleg (fanga, ikkje-fatalt), men viser ein stygg Python-traceback midt i
demoen og bryt "offline-sikker"-lovnaden i praksis (feilen skjer, han vert
berre ikkje fatal).

Brukaren ønskjer å **droppe** eksempeldatagenereringa heilt i demoen for å
fjerne denne feilkjelda ved rota, ikkje berre halde fram med å fange
feilen.

## Design

**Opt-in flagg, ikkje ny standardåtferd.** `make new-modell` er
repo-omfattande, brukt til reell modellering (ikkje berre demoen), der den
rike syntetiske eksempeldatafila er verdifull (sjå eksisterande skildring
i `COMMANDS.md`). Løysinga skal difor **ikkje** endre standardåtferda for
noverande brukarar av `make new-modell` — berre gje eit nytt, eksplisitt
`SKIP_EXAMPLE=1`-flagg (same "presence-based boolean"-mønster som
`CONFIRM=1` på `remove-modell`) som `javazone-demo-script.sh` kan setje på
sine to `make new-modell`-kall (steg 3 interaktivt, og den stille
`QUICK=true`-greina).

Ved `SKIP_EXAMPLE=1` skriv `new-modell.sh` direkte den same minimale
éin-linje-stubben som i dag berre vert brukt som **fallback** ved feila
generering — ingen podman-kall til `validator.py`, ingen nettverksavhengd
kode-veg i det heile.

## Steg

1. **`new-modell.sh`**: legg til 4. positional-arg `SKIP_EXAMPLE_FLAG`
   (`--skip-example`/tom), same mønster som `remove-modell.sh` sitt
   `--confirm`-flagg. Vikle det eksisterande podman/validator.py-kallet +
   fallback-logikken i eit `if [[ "$SKIP_EXAMPLE_FLAG" == "--skip-example"
   ]]; then <skriv stub direkte> else <eksisterande generering +
   fallback> fi`.
2. **`make/70-scaffolding.mk`**: legg til `SKIP_EXAMPLE`-støtte i
   `new-modell`-targetet (hjelpetekst, `print_header`-linje, send
   `$(if $(SKIP_EXAMPLE),--skip-example)` som 4. arg til scriptet).
3. **`javazone-demo-script.sh`**: legg `SKIP_EXAMPLE=1` til begge
   `make new-modell`-kalla (steg 3 sin `step boxes "3. ..."`-kommandolinje
   + faktiske kall, og `QUICK=true`-greina sin kommandolinje + kall).
4. **`COMMANDS.md`**: oppdater `make new-modell`-rada med det nye
   valfrie flagget og kva det gjer.
5. **`specs/backlog/javazone-demo-plan.md`**: legg til ei kort linje om
   at demoen sitt `new-modell`-kall brukar `SKIP_EXAMPLE=1` for å halde
   seg fullstendig offline (kryssreferanse til denne specen).
6. **Verifiser**: `bash -n` på begge script, live-køyring av
   `make new-modell DOMAIN=oreg NAME=<test> SKIP_EXAMPLE=1` (stadfest
   ingen podman-kall til `mcp-linkml-modell-utkast`, ingen
   nettverksforsøk, korrekt minimal eksempelfil), og ein full
   `QUICK=true`-demo-køyring som stadfestar at Python-tracebacken er
   borte. Stadfest òg at `make new-modell` **utan** `SKIP_EXAMPLE`
   framleis fungerer akkurat som før (ingen regresjon for eksisterande
   brukarar).

## Handlingsliste

| # | Tiltak | Fil |
|---|---|---|
| 1 | `--skip-example`-flagg + gren i scriptet | `new-modell.sh` |
| 2 | `SKIP_EXAMPLE`-støtte i Makefile-target | `make/70-scaffolding.mk` |
| 3 | `SKIP_EXAMPLE=1` på begge `make new-modell`-kall | `javazone-demo-script.sh` |
| 4 | Dokumenter nytt flagg | `COMMANDS.md` |
| 5 | Kryssreferanse i demo-planen | `specs/backlog/javazone-demo-plan.md` |
| 6 | Syntakssjekk + live-verifisering (med og utan flagget) | — |

---

## Utført

Alle seks steg gjennomførte 2026-09-01:

- **Steg 1**: `new-modell.sh` tek no 4. positional-arg
  `SKIP_EXAMPLE_FLAG` (`--skip-example`). Heile eksempeldata-blokka vikla
  i `if [[ "$SKIP_EXAMPLE_FLAG" == "--skip-example" ]]; then <skriv stub
  direkte, ingen podman-kall> else <eksisterande generering + fallback>
  fi`.
- **Steg 2**: `make/70-scaffolding.mk` sitt `new-modell`-target tek imot
  `SKIP_EXAMPLE=1`, viser han i `print_header`, sender
  `--skip-example` vidare til scriptet.
- **Steg 3**: begge `make new-modell`-kalla i `javazone-demo-script.sh`
  (steg 3 interaktivt, `QUICK=true`-greina) har no `SKIP_EXAMPLE=1`,
  synleg i den farga kommandolinja (`CLR_WARN`, sidan det er eit valfritt
  flagg).
- **Steg 4**: `COMMANDS.md` sin `new-modell`-rad oppdatert med det nye
  flagget.
- **Steg 5**: `specs/backlog/javazone-demo-plan.md` sitt køyreeksempel
  oppdatert med `SKIP_EXAMPLE=1` + forklarande kommentar og
  kryssreferanse.
- **Steg 6 — verifisert live**:
  - `bash -n` OK for begge script.
  - `make new-modell DOMAIN=oreg NAME=quicktest9` (**utan** flagget):
    uendra åtferd — full generering, ingen "Hoppar over"-melding,
    exit 0 (regresjonstest — stadfestar ingen endring for eksisterande
    brukarar).
  - `make new-modell DOMAIN=oreg NAME=quicktest10 SKIP_EXAMPLE=1`:
    "Hoppar over eksempeldatagenerering (SKIP_EXAMPLE=1) — skriv minimal
    stub i staden.", ingen podman-kall til `validator.py`, minimal
    eitt-instans-stub skriven korrekt, `check-import-duplicates`/`lint`
    OK, exit 0.
  - Full `QUICK=true DOMAIN=oreg NAME=quicktest11`-demo-køyring:
    kommandolinja viser `SKIP_EXAMPLE=1` i gult, ingen Python-traceback
    (`Traceback`/`socket.gaierror`-treff: 0), demoen held fram normalt.
  - Testartefakt (`quicktest9`, `quicktest10`, `quicktest11`) rydda opp
    etterpå.

Ingen avvik frå planen. Den pre-eksisterande, urelaterte lokale
`javazonetalk`-tilstanden (nemnd i tidlegare spec-ar denne økta) er
framleis urørt av desse endringane.
