---
name: container-images
description: Container-invokeringsmønster i make/01-containers.mk og Dockerfile*/requirements*.txt under src/assets/containers/ — WORK_MOUNT, eksplisitt env-vidareføring, stdin-fella (BUG-10), attribution-plikt for nye verktøy. Lastast automatisk ved arbeid med desse filene.
paths:
  - "src/assets/containers/**"
  - "make/01-containers.mk"
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

## Attribution-plikt for nye verktøyavhengigheiter

Legg du til eit nytt verktøy i `Dockerfile*` eller `requirements*.txt` som
endar opp bundla i eit publisert containerbilete: sjekk om lisensen krev
attribution (typisk MIT, BSD, Apache-2.0, EPL) og oppdater
attributions-tabellen i `mkdocs/docs/om.md` ved behov. Sjå `CONTRIBUTING.md`
§ "Nye verktøyavhengigheiter" og `specs/done/verktoy-lisensoversikt.md` for
metode og eksisterande klassifisering.
