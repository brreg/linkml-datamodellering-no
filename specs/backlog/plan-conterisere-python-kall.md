# Plan for å containerisere direkte Python-kall i Makefile

## Føremål

Målet er å fjerne direkte kall til `python3` og `python` frå GitHub-runneren/hosten, slik at all Python-køyring skjer i definerte Podman-containerar. Dette gir meir reproducerbar CI, færre avhengigheiter på runneren og mindre risiko for at lokale/host-baserte Python-versjonar påverkar bygginga.

Basert på Makefile-en som vart delt, finst det fleire kategoriar av Python-kall:

1. Kall som allereie brukar container via `$(PYTHON_RUN)` eller `$(LINKML_RUN)`.
2. Kall som køyrer Python direkte på hosten.
3. Kall som køyrer Python direkte via inline `python3 -c`.
4. Kall der Python kallast indirekte frå shell-script. Desse må undersøkast separat.

Denne planen fokuserer på kategori 2 og 3: direkte Python-kall i Makefile.

---

## Eksisterande container-wrapperar

Makefile-en har allereie to relevante wrapperar:

- `PYTHON_RUN := podman run --rm -v "$(CURDIR):/work" -w /work -e PYTHONWARNINGS=ignore $(PYTHON_IMAGE)`
- `LINKML_RUN := podman run --rm -v "$(CURDIR):/work" -w /work -e PYTHONWARNINGS=ignore -e HOME=/tmp --user root $(LINKML_IMAGE)`

Anbefalt hovudregel:

- Bruk `$(PYTHON_RUN)` for eigne Python-script som ikkje treng LinkML CLI eller LinkML-spesifikke bibliotek.
- Bruk `$(LINKML_RUN)` for script som krev LinkML, SchemaView, linkml-runtime eller andre LinkML-avhengigheiter.
- Bruk absolute container-stiar med `/work/...` når script eller argument skal lesast inne i containeren.

---

## Funn: direkte Python-kall som bør endrast

### 1. `gen-begrepskatalog-instance`

Noverande kall:

`python3 .github/scripts/collect-concepts.py`

Problem:

- Køyrer direkte på GitHub-runneren.
- Avheng av at `.github/scripts` finst i arbeidskatalogen.
- Er årsaka til den aktuelle feilen dersom `.github/` ikkje følgjer med artifacten.
- Scriptet ligg i ein skjult katalog, noko som er sårbart i artifact-basert workflow.

Anbefalt endring på kort sikt:

`$(PYTHON_RUN) python3 /work/.github/scripts/collect-concepts.py`

Anbefalt endring på sikt:

- Flytt scriptet til `src/assets/scripts/makefile/collect-concepts.py`.
- Endre targetet til å køyre:

`$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/collect-concepts.py`

Prioritet: Høg.

---

### 2. `gen-modellkatalog-instance`

Noverande kall:

`python3 src/assets/scripts/makefile/generate-modellkatalog.py`

Problem:

- Køyrer direkte på hosten.
- Inkonsistent med resten av Makefile-en, der mange Python-script under `src/assets/scripts/makefile/` køyrer via container.

Anbefalt endring:

`$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/generate-modellkatalog.py`

Dersom scriptet krev LinkML-bibliotek, bruk heller:

`$(LINKML_RUN) python3 /work/src/assets/scripts/makefile/generate-modellkatalog.py`

Prioritet: Høg.

---

### 3. `update-modellkatalog`

Noverande kall:

`python3 src/assets/scripts/makefile/update-modellkatalog.py`

Problem:

- Køyrer direkte på hosten.
- Kan gi ulik oppførsel lokalt og i CI dersom Python-pakkar eller versjonar skil seg.

Anbefalt endring:

`$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/update-modellkatalog.py`

Dersom scriptet brukar LinkML-funksjonalitet, bruk:

`$(LINKML_RUN) python3 /work/src/assets/scripts/makefile/update-modellkatalog.py`

Prioritet: Middels til høg.

---

### 4. `gen-modelldcat-elements`

Noverande kall:

`$(LINKML_RUN) python3 src/assets/scripts/makefile/gen-modelldcat-elements.py ...`

Vurdering:

- Dette brukar allereie container.
- Kommentaren seier at targetet krev SchemaView, og derfor skal bruke `$(LINKML_RUN)`.
- Men scriptstien er relativ inne i containeren.

Anbefalt presisering:

`$(LINKML_RUN) python3 /work/src/assets/scripts/makefile/gen-modelldcat-elements.py ...`

Prioritet: Låg til middels. Dette er ikkje eit host-Python-problem, men det er betre å vere konsekvent med `/work/...`.

---

### 5. `run_gen_informasjonsmodell_instance`

Noverande kall:

`python3 src/assets/scripts/makefile/generate-informasjonsmodell.py "$$schema" >/dev/null 2>&1`

Problem:

- Køyrer direkte på hosten.
- Dette targetet blir kalla frå alle `domain-*`-target til slutt.
- Potensielt stor flate for inkonsistent Python-miljø.

Anbefalt endring:

`$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/generate-informasjonsmodell.py "/work/$$schema" >/dev/null 2>&1`

Alternativ dersom scriptet forventar repo-relative stiar:

`$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/generate-informasjonsmodell.py "$$schema" >/dev/null 2>&1`

Anbefaling:

- Start med repo-relativ sti dersom scriptet i dag forventar repo-relative stiar.
- Bruk `/work/$$schema` berre dersom scriptet toler absolute stiar.

Prioritet: Høg.

---

### 6. `validate-bronze`

Noverande inline-kall:

`python3 src/assets/scripts/makefile/save-validation-log.py --schema "$$schema" --type bronze --result "$$result" 2>/dev/null || true`

Noverande inline JSON-kall:

`SCHEMA="$$schema" python3 -c "import json,sys,os; ..." <<< "$$result"`

Problem:

- Begge køyrer direkte på hosten.
- `python3 -c` gjer Makefile-en vanskelegare å lese og meir sårbar for quoting-feil.
- Dette targetet køyrer i valideringsflyt og bør vere deterministisk.

Anbefalt endring for save-validation-log:

`$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/save-validation-log.py --schema "$$schema" --type bronze --result "$$result" 2>/dev/null || true`

Anbefalt endring for inline JSON-parsing:

- Flytt inline-koden til eit eige script, til dømes:

`src/assets/scripts/makefile/emit-github-validation-annotations.py`

- Kall det via container:

`$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/emit-github-validation-annotations.py --schema "$$schema" <<< "$$result"`

Prioritet: Middels.

---

### 7. `validate-data`

Noverande kall:

`python3 src/assets/scripts/makefile/save-validation-log.py --schema "$$schema" --type "data-$$catalog" --result "$$result" 2>/dev/null || true`

Problem:

- Køyrer direkte på hosten.

Anbefalt endring:

`$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/save-validation-log.py --schema "$$schema" --type "data-$$catalog" --result "$$result" 2>/dev/null || true`

Prioritet: Middels.

---

### 8. `validate-examples`

Noverande kall:

`python3 src/assets/scripts/makefile/save-validation-log.py --schema "$$schema" --type examples --result "$$result_json" 2>/dev/null || true`

Problem:

- Køyrer direkte på hosten.

Anbefalt endring:

`$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/save-validation-log.py --schema "$$schema" --type examples --result "$$result_json" 2>/dev/null || true`

Prioritet: Middels.

---

### 9. `mcp-linkml-modell-utkast`

Noverande kall 1:

`python3 -c "import json; content = open('$(SCHEMA)').read(); ..." | $(LINKML_MOD_RUN) ...`

Noverande kall 2:

`... | python3 -c "import json, sys, pathlib; ..."`

Problem:

- Begge køyrer direkte på hosten.
- Inline Python i Makefile er vanskeleg å vedlikehalde.
- Første inline-kall les input og byggjer JSON-RPC-meldingar.
- Andre inline-kall les JSON-RPC-respons og skriv generert schemafil.

Anbefalt endring:

Lag to små script:

1. `src/assets/scripts/makefile/mcp-build-modell-utkast-request.py`
2. `src/assets/scripts/makefile/mcp-write-modell-utkast-response.py`

Køyr dei via `$(PYTHON_RUN)` eller eventuelt eit eige lettvekts Python-image.

Føreslått flyt:

`$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/mcp-build-modell-utkast-request.py --schema "$(SCHEMA)" --format "$(or $(FORMAT),json-schema)" --profile "$(or $(PROFILE),bronze)" | $(LINKML_MOD_RUN) $(LINKML_MOD_IMAGE) | $(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/mcp-write-modell-utkast-response.py --schema "$(SCHEMA)"`

Prioritet: Middels.

---

### 10. `mcp-linkml-begrep-utkast`

Noverande inline-kall:

`python3 -c "import json; args=json.load(open('$(INPUT)')); print(json.dumps(...))"`

Problem:

- Køyrer direkte på hosten.
- Inline Python i shell quoting blir fort skjørt.

Anbefalt endring:

Lag script:

`src/assets/scripts/makefile/mcp-build-begrep-utkast-request.py`

Køyr via container:

`$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/mcp-build-begrep-utkast-request.py --input "$(INPUT)" | $(LINKML_BEGREP_RUN) $(LINKML_BEGREP_IMAGE)`

Prioritet: Middels.

---

### 11. `mcp-linkml-validate`

Noverande inline-kall:

`python3 -c "import yaml, sys; manifest_path = '$(dir $(SCHEMA))build.yaml'; ..." 2>/dev/null || echo "bronze"`

Problem:

- Køyrer direkte på hosten.
- Brukar `yaml`, som ikkje nødvendigvis er installert i host-Python.
- Dette er eit typisk eksempel på kvifor Python bør køyrast i container.

Anbefalt endring:

Lag script:

`src/assets/scripts/makefile/detect-validation-policy.py`

Køyr via container:

`DETECTED_POLICY=$$($(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/detect-validation-policy.py --schema "$(SCHEMA)" 2>/dev/null || echo "bronze")`

Prioritet: Høg.

---

### 12. `validate-capture`

Noverande kall:

Ved enkelt schema:

`python3 src/assets/scripts/makefile/run-schema-validation.py --schema $(SCHEMA)`

Ved alle schema:

`python3 src/assets/scripts/makefile/run-schema-validation.py --parallel $(PARALLEL)`

Problem:

- Køyrer direkte på hosten.
- Targetet byggjer først MCP-image, men sjølve orchestration-scriptet køyrer på hosten.

Anbefalt endring:

Ved enkelt schema:

`$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/run-schema-validation.py --schema $(SCHEMA)`

Ved alle schema:

`$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/run-schema-validation.py --parallel $(PARALLEL)`

Merk:

- Dersom `run-schema-validation.py` sjølv startar Podman-containerar, må du vurdere om containeren treng tilgang til Podman socket eller om dette scriptet framleis bør køyre på hosten.
- Dersom scriptet berre les filer og køyrer validering via andre shell-script, kan `$(PYTHON_RUN)` vere nok.

Prioritet: Middels, men krev teknisk verifikasjon.

---

## Kall som allereie er containeriserte

Desse ser i hovudsak greie ut:

- `$(PYTHON_RUN) python3 src/assets/scripts/makefile/gen-docgen-examples.py ...`
- `$(PYTHON_RUN) python -u src/assets/scripts/makefile/filter_erdiagram.py ...`
- `$(PYTHON_RUN) python -u src/assets/scripts/makefile/filter_plantuml.py ...`
- `$(PYTHON_RUN) python3 src/assets/scripts/makefile/gen-openapi.py ...`
- `$(PYTHON_RUN) openapi-spec-validator ...`
- `$(PYTHON_RUN) python3 src/assets/scripts/makefile/gen-asyncapi.py ...`
- `$(LINKML_RUN) python3 src/assets/scripts/makefile/gen-modelldcat-elements.py ...`
- `podman run --rm --entrypoint python3 -v "$(CURDIR):/work" $(AVROTIZE_IMAGE) /work/src/assets/scripts/makefile/fix-xsd-dates.py ...`
- `podman run --rm -v "$$PWD:/work" -w /work ... $(LINKML_IMAGE) linkml validate ...`
- `podman run --rm -v "$(CURDIR)/$(LINKML_MOD_DIR):/app/..." ... python -m pytest ...`
- `podman run --rm -v "$(CURDIR):/work:ro" ... $(MCP_IMAGE) python3 /work/tests/test_mcp_policies.py -v`

Anbefaling:

- Desse treng ikkje akutt endring.
- For konsistens kan de etter kvart endre scriptstiar frå repo-relative til `/work/...` i containerkall, men dette er ikkje nødvendig for å løyse host-Python-problemet.

---

## Kall som bør vurderast indirekte

Makefile-en kallar fleire Bash-script:

- `bash tests/test_make.sh "$(SCHEMA)"`
- `bash src/assets/scripts/makefile/gen-config.sh > config.mk`
- `bash src/assets/scripts/makefile/generate-readme-tables.sh README.md`
- `bash mkdocs/publish.sh`
- `bash src/assets/scripts/new-model.sh ...`
- `bash src/assets/scripts/new-modellkatalog.sh ...`
- `bash src/assets/scripts/new-begrepssamling.sh ...`
- `bash src/assets/scripts/new-begrepskatalog.sh ...`
- `bash src/mcp-linkml-validator/flatten-and-validate.bash ...`
- `bash src/assets/scripts/run-validation.sh ...`

Desse kan sjølve innehalde direkte `python3`-kall. Det bør gjerast ein eigen gjennomgang med:

`grep -R "python\|python3" src tests mkdocs .github -n`

Prioritet: Middels.

---

## Foreslått gjennomføringsplan

### Fase 1: Stabiliser CI-feilen

1. Endre `gen-begrepskatalog-instance` til å bruke `$(PYTHON_RUN)`.
2. Samstundes legg til `include-hidden-files: true` i `actions/upload-artifact`, sidan `.github/` framleis må vere med dersom scriptet blir liggande der.
3. Legg inn eit kort debug-steg i `generate` som verifiserer at `.github/scripts/collect-concepts.py` finst etter `download-artifact`.

Resultat:

- Den aktuelle CI-feilen bør forsvinne.
- De får stadfesta om artifacten inneheld `.github/scripts`.

### Fase 2: Flytt byggescript ut frå `.github`

1. Flytt `.github/scripts/collect-concepts.py` til `src/assets/scripts/makefile/collect-concepts.py`.
2. Oppdater Makefile.
3. Oppdater eventuelle referansar i dokumentasjon eller workflows.
4. Behald `.github/` til CI-policy, workflows og GitHub-spesifikke filer.

Resultat:

- Mindre coupling mellom GitHub Actions og byggelogikk.
- Mindre sårbarheit for hidden-file-reglar i artifact.

### Fase 3: Containeriser enkle direkte scriptkall

Endre desse targeta først:

1. `gen-modellkatalog-instance`
2. `update-modellkatalog`
3. `run_gen_informasjonsmodell_instance`
4. `validate-data`
5. `validate-examples`
6. `validate-bronze` for `save-validation-log.py`

Resultat:

- Dei fleste direkte host-Python-kall er borte.

### Fase 4: Rydd opp inline Python

Flytt inline `python3 -c` til eigne script:

1. `emit-github-validation-annotations.py`
2. `mcp-build-modell-utkast-request.py`
3. `mcp-write-modell-utkast-response.py`
4. `mcp-build-begrep-utkast-request.py`
5. `detect-validation-policy.py`

Resultat:

- Mindre quoting-kompleksitet i Makefile.
- Betre testbarheit.
- Enklare lokal og CI-lik køyring.

### Fase 5: Gå gjennom shell-script

Køyr grep etter direkte Python-kall i shell-script og flytt desse til container der det gir meining.

Resultat:

- Heile byggeløpet blir meir deterministisk.

---

## Forslag til prioritering

Høg prioritet:

1. `gen-begrepskatalog-instance`
2. `gen-modellkatalog-instance`
3. `run_gen_informasjonsmodell_instance`
4. `mcp-linkml-validate` sin policy-deteksjon

Middels prioritet:

1. `update-modellkatalog`
2. `validate-bronze`
3. `validate-data`
4. `validate-examples`
5. `validate-capture`
6. MCP request/response inline Python

Låg prioritet:

1. Gjere allereie containeriserte kall meir konsistente med `/work/...`.
2. Reformatere lange Makefile-inline-uttrykk når dei likevel blir flytta til script.

---

## Anbefalt sluttmål

Sluttmålet bør vere at Makefile-en ikkje inneheld direkte `python3` eller `python -c` som køyrer på hosten. All Python bør gå via ein av desse:

- `$(PYTHON_RUN)` for generell prosjekt-Python.
- `$(LINKML_RUN)` for LinkML-avhengig Python.
- Eigne spesialcontainerar berre der det er nødvendig.

I tillegg bør byggescript ligge under `src/assets/scripts/makefile/`, ikkje under `.github/scripts/`, dersom dei er del av ordinær byggelogikk.
