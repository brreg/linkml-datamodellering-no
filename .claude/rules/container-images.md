---
name: container-images
description: Container-invokeringsmønster i make/01-containers.mk, make/60-mcp.mk, Makefile og Dockerfile*/requirements*.txt under src/assets/containers/ — WORK_MOUNT, eksplisitt env-vidareføring, stdin-fella (BUG-10), attribution-plikt for nye verktøy, full kartlegging av monteringsstader for nye delte moduler. Lastast automatisk ved arbeid med desse filene.
paths:
  - "src/assets/containers/**"
  - "make/01-containers.mk"
  - "make/60-mcp.mk"
  - "Makefile"
  - "src/assets/scripts/scaffolding/**"
---

## WORK_MOUNT-mønsteret

Alle container-wrapparar i `make/01-containers.mk` mountar repoet som
`/work` og køyrer med `-w /work` via delt
`WORK_MOUNT := -v "$(CURDIR):/work" -w /work`. **Unntak:** `DOCS_RUN`
(mkdocs) bryt mønsteret medvite — mountar berre `mkdocs/docs`,
`mkdocs/mkdocs.yml`, `mkdocs/overrides`, `mkdocs/.cache` og `mkdocs/site`
som separate delmonteringar, for å unngå unødvendig I/O av resten av
repoet. Følg same mønster (heile repoet via `WORK_MOUNT`, eller selektive
delmonteringar dersom containeren berre treng ein avgrensa del) når du legg
til ein ny container-wrapper.

## Miljøvariablar må vidareførast eksplisitt

`-e <NAVN>` (utan verdi) i eit `podman run`-kall vidarefører variabelen frå
den kallande prosessen sitt `os.environ` inn i containeren — dette er
**ikkje** det same som å hardkode ein verdi, og variabelen forsvinn stille
dersom `-e`-linja manglar. Container-wrapparane vidarefører i dag:

| Variabel | Kvifor |
|---|---|
| `LOGLVL` | Styrer detaljnivå i batch-scripta (DEBUG/INFO/ERROR) |
| `CLR_STEP`/`CLR_RST`/`CLR_OK`/`CLR_ERR` | Fargekodar for terminaloutput i batch-generate.py/check-import-duplicates.py |
| `BATCH_GENERATE_WORKERS` | Talet på `ProcessPoolExecutor`-workers for parallelle generatorar (defaultar til 6 om usett) |
| `GITHUB_REPOSITORY` | GitHub Actions sin automatisk sette owner/repo-variabel — trygt no-op lokalt |

Legg til ein ny `-e <NAVN>` når eit script under `src/assets/scripts/`
byrjar lese ein ny miljøvariabel — elles ser scriptet han aldri, sjølv om
han er sett i den kallande shellen.

## BUG-10: `podman run -i` et stdin frå omsluttande `while read`-løkker

`PYTHON_RUN` brukar `-i` (interaktiv stdin) for å støtte kallarar som
pipar/heredoc-ar inn data. Dette har ei alvorleg fallgruve: eit
`$(PYTHON_RUN)`-kall inni ei
`while IFS= read -r x; do ... done < <(...)`-løkke (prosess-substitusjon)
**konsumerer resten av løkka sin fd 0** — berre det *første* elementet vert
prosessert, deretter avsluttar løkka **stille**, utan feilmelding og utan
ikkje-null exit code. Sjå
`bugs/podman-interactive-stdin-konsumerer-while-lokke.md` (BUG-10) for full
diagnose — retta i `validate-examples`/`validate-bronze`, men mønsteret kan
reintroduserast i eit nytt target.

**Regel:** eit `$(PYTHON_RUN)`-kall (eller anna `podman run -i`) inni ei
`while read < <(...)`-løkke **må** omdirigere sin eigen stdin:

```bash
$(PYTHON_RUN) python3 /work/src/assets/scripts/... < /dev/null
# eller, dersom kallet faktisk treng input frå ein variabel:
$(PYTHON_RUN) python3 /work/src/assets/scripts/... <<< "$$var"
```

Alternativt: bygg om til `for x in $$(...)`-mønsteret, som ikkje deler fd 0
mellom iterasjonar (uegna for svært store lister, sidan heile ordlista må
evaluerast i minnet før løkka startar). `validate-data` brukar dette
mønsteret og er ikkje råka av same feil.

## Ein ny påkravd delt modul krev full kartlegging av alle monteringsstader

Ei fil under `src/assets/scripts/utils/` som eit `server.py`/script **ikkje
kan starte utan** (i motsetnad til ein valfri bug-workaround med mjuk
try/except-fallback, t.d. `linkml_relative_import_patch.py`) må vere
tilgjengeleg i **kvar einaste** kontainarinvokering av det scriptet — ikkje
berre det opplagte `-run`/`-smoke`-make-targetet. Same fallgruve som
env-variabel-vidareføringa over («forsvinn stille dersom `-e`-linja
manglar»), berre for filmonteringar: mankar mounten éin stad, feilar akkurat
den kodevegen med `ModuleNotFoundError` — gjerne først i CI eller hos ein
ekstern brukar, lenge etter at dei "opplagte" targeta er verifiserte.

**Framgangsmåte** (jf. konsolideringa av `mcp_jsonrpc_stdio.py` på tvers av
dei tre MCP-serverane, `specs/done/mcp-server-python-tiltak.md`): grep heile
repoet etter **alle** stader det aktuelle scriptet vert køyrt i ein
kontainer, ikkje berre Makefile-targeta:

1. Make-variablar for interaktiv køyring (t.d. `MCP_RUN`, `LINKML_MOD_RUN`
   i `Makefile`/`make/60-mcp.mk`)
2. `-test`-oppskrifter som monterer kjeldekatalogen separat frå
   `-run`/`-smoke` (ofte ein annan monteringssti/`PYTHONPATH`, difor ikkje
   automatisk dekt av (1))
3. Scaffolding-script som byggjer sine eigne `podman run`-kall direkte
   (t.d. `src/assets/scripts/scaffolding/new-modell.sh`) — desse duplekserer
   make-variablane sine monteringar manuelt og må oppdaterast separat
4. `tests/test_make.sh` sine direkte `podman run`-kall (skil seg frå
   make-targeta sine, søk spesifikt etter scriptnamnet)
5. CI-cache-nøklar i `.github/workflows/*.yml` som eksplisitt listar
   avhengige filer (`hashFiles(...)`) — ei ny transitiv avhengigheit må
   leggjast til der, elles gjev ei framtidig endring i modulet eit stille
   cache-hit i staden for reell re-køyring

For sjølve scriptet: prøv fleire kandidat-`sys.path`-oppføringar (éin per
kjend monteringsmønster: flatt i same katalog som scriptet, `/repo/...` for
heile-repo-monteringar, repo-relativ sti for direkte git-checkout-køyring)
— men **ikkje** legg til ein mjuk try/except-fallback slik
`linkml_relative_import_patch.py` gjer. Den fallbacken er trygg berre fordi
patchen er ein valfri bug-workaround; ein hard avhengigheit skal krasje
høgt med ein naturleg `ImportError` dersom ingen kandidat finn fila.

## Attribution-plikt for nye verktøyavhengigheiter

Legg du til eit nytt verktøy i `Dockerfile*` eller `requirements*.txt` som
endar opp bundla i eit publisert containerbilete: sjekk om lisensen krev
attribution (typisk MIT, BSD, Apache-2.0, EPL) og oppdater
attributions-tabellen i `mkdocs/docs/om.md` ved behov. Sjå `CONTRIBUTING.md`
§ "Nye verktøyavhengigheiter" og `specs/done/verktoy-lisensoversikt.md` for
metode og eksisterande klassifisering.
