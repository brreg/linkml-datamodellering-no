# Fiks `make validate-examples` for skjema utan tree_root

## Bakgrunn

`make validate-examples DOMAIN=<domain>` (`make/40-validation.mk:96-140`,
brukt av `.github/workflows/validate.yml` sitt steg "Valider eksempelfiler
mot skjema") pre-filtrerer skjemalista mot ein hardkoda sjekk før løkka
i det heile startar:

```bash
done < <(find src/linkml/$(DOMAIN) -mindepth 2 -maxdepth 2 -name '*-schema.yaml' \
	| grep -v common | sort | xargs grep -l "tree_root: true"); \
```

Per `CLAUDE.md` ("Containerklasse") skal **AP-NO-profilskjema
(og fair-modellar) ikkje ha eigen containerklasse** — dei har difor aldri
`tree_root: true`. Resultatet er at `xargs grep -l "tree_root: true"`
filtrerer vekk **alle 9** ap-no-skjema før `while read`-løkka får sjå éin
einaste linje, sjølv om 6 av dei faktisk har eksempelfiler:

```
$ find src/linkml/ap-no -mindepth 2 -maxdepth 2 -name '*-schema.yaml' | grep -v common | sort
src/linkml/ap-no/cpsv-ap-no/cpsv-ap-no-schema.yaml
src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml
src/linkml/ap-no/dqv-ap-no/dqv-ap-no-schema.yaml
src/linkml/ap-no/dqv-ap-no/dqv-core-schema.yaml
src/linkml/ap-no/modelldcat-ap-no/modelldcat-ap-no-schema.yaml
src/linkml/ap-no/modelldcat-ap-no/modelldcat-katalog-schema.yaml
src/linkml/ap-no/modelldcat-ap-no/modelldcat-modell-schema.yaml
src/linkml/ap-no/skos-ap-no/skos-ap-no-schema.yaml
src/linkml/ap-no/xkos-ap-no/xkos-ap-no-schema.yaml
```

Ingen av desse har `tree_root: true`. Seks har likevel ei eksempelfil
(`examples/<namn>-eksempel.yaml`): `cpsv-ap-no`, `dcat-ap-no`, `dqv-ap-no`,
`modelldcat-ap-no`, `skos-ap-no`, `xkos-ap-no`. CI-steget "Valider
eksempelfiler mot skjema" for `DOMAIN=ap-no` fullfører difor på 0 sekund
utan noka logglinje — ikkje fordi det ikkje er noko å validere, men fordi
filteret ekskluderer alt før løkka rekk å konstatere det. Ap-no-eksempelfiler
har i praksis **null CI-valideringsdekning** i dag.

**Løysinga finst alt i repoet, berre ikkje kopla til dette targetet.**
`tests/test_make.sh` har akkurat same problem og løyser det med eit
fixture-mønster: `tests/fixtures/<namn>-fixture.yaml` er små hjelpeskjema
som importerer det ekte profilskjemaet og legg til ein mellombels
`Container`/`tree_root: true`-klasse, brukt utelukkande til å gi
`linkml validate` eit gyldig ankerpunkt:

```yaml
# tests/fixtures/dcat-ap-no-fixture.yaml
imports:
  - linkml:types
  - ../../src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema
classes:
  Container:
    tree_root: true
    attributes:
      katalogar:
        range: Katalog
        multivalued: true
        inlined_as_list: true
      datasett:
        range: Datasett
        ...
```

`test_make.sh` sin `test_linkml_validate()` vel fixture i staden for det
ekte skjemaet når `lacks_tree_root("$domain")` (hardkoda
`ap-no`/`fair`-sjekk) er sann, og hoppar stille over dersom fixture
manglar. Fixtures finst alt for alle 6 ap-no-modellane med eksempelfiler
(pluss `fair-metadata-fixture.yaml`) — sjå `tests/fixtures/`.

Denne speccen kopla same mekanisme inn i `make validate-examples`, slik at
CI faktisk validerer ap-no-eksempelfilene, i staden for å stole på at
`tests/test_make.sh` (som ikkje køyrer i `validate.yml`) fangar opp feil.

## Design

Framfor å kopiere `test_make.sh` sin hardkoda `lacks_tree_root()`
(domenenamn-liste), sjekkar den nye logikken **per skjema** om
`tree_root: true` finst i sjølve skjemafila. Dette er meir robust (ny
domenetype utan tree_root krev ikkje ei ny hardkoda liste éin stad til) og
unngår å duplisere domenenamn-kunnskapen som alt finst i
`test_make.sh:48`.

- **Med `tree_root: true`:** valider mot skjemaet direkte (uendra åtferd
  for domene som `fint`, `oreg`, `samt` m.fl.)
- **Utan `tree_root: true`:** slå opp `tests/fixtures/<namn>-fixture.yaml`.
  Finst fixture: valider mot fixture i staden. Finst ikkje fixture: skriv
  synleg `::warning`-annotasjon (ikkje stille skip, jf. CLAUDE.md "Ingen
  stille feil") og hopp over.
- `save-validation-log.py --schema` skal framleis peike på det **ekte**
  skjemaet (ikkje fixture-fila), sidan valideringsloggen skal liggje under
  det ekte skjemaet sin `validation/<versjon>/`-katalog.

## Steg

### 1. Fjern `xargs grep -l "tree_root: true"`-forfilteret

I `make/40-validation.mk`, `validate-examples`-targetet: fjern
`| xargs grep -l "tree_root: true"` frå `find`-pipa, slik at løkka ser
**alle** `*-schema.yaml` i domenet (minus `common`), ikkje berre dei med
tree_root:

```bash
done < <(find src/linkml/$(DOMAIN) -mindepth 2 -maxdepth 2 -name '*-schema.yaml' \
	| grep -v common | sort); \
```

### 2. Legg til per-skjema tree_root-sjekk med fixture-fallback

Rett etter den eksisterande "Ingen eksempelfil"-sjekken (linje 105-108),
før `log_info "→ validate-examples ..."`:

```bash
validate_schema="$$schema"; \
if ! grep -q "tree_root: true" "$$schema"; then \
	fixture="tests/fixtures/$$name-fixture.yaml"; \
	if [ -f "$$fixture" ]; then \
		validate_schema="$$fixture"; \
	else \
		log_info "$(CLR_WARN)::warning file=$$schema::Ingen tree_root og ingen fixture funne ($$fixture) — hoppar over$(CLR_RST)"; \
		continue; \
	fi; \
fi; \
```

### 3. Bruk `$$validate_schema` i staden for `$$schema` i sjølve valideringskallet

Oppdater `log_debug`-linja og `podman run ... linkml validate`-kallet til
å bruke `"$$validate_schema"` som `--schema`-argument. **NB:**
`save-validation-log.py --schema "$$schema"` (linja etter) skal **ikkje**
endrast — den skal framleis peike på det ekte skjemaet, ikkje fixture-fila.

### 4. Test lokalt

```bash
make validate-examples DOMAIN=ap-no
```

Forventa resultat:
- 6 skjema (`cpsv-ap-no`, `dcat-ap-no`, `dqv-ap-no`, `modelldcat-ap-no`,
  `skos-ap-no`, `xkos-ap-no`) validerer no faktisk via fixture, med
  synleg `→ validate-examples ap-no/<namn>`-loggline per skjema
- 3 skjema utan eiga eksempelfil (`dqv-core`, `modelldcat-katalog`,
  `modelldcat-modell`) hoppar framleis over med den eksisterande
  "Ingen eksempelfil funne"-åtvaringa (uendra)
- Injiser ein bevisst feil i eit ap-no-eksempel (t.d. fjern eit
  `required`-felt sitt verdi) og stadfeste at `::error`-annotasjonen
  dukkar opp og at targetet feilar (`exit 1`)

Køyr òg regresjonstest for eit domene **med** tree_root (t.d.
`make validate-examples DOMAIN=fint` eller `DOMAIN=samt`) for å stadfeste
at eksisterande åtferd er uendra der.

## Utanfor scope

- `tests/test_make.sh` sin hardkoda `lacks_tree_root()`-funksjon vert
  **ikkje** endra i denne speccen, sjølv om han no overlappar med den nye,
  meir generelle per-skjema-sjekken i `make/40-validation.mk`. Å
  konsolidere desse til éin delt mekanisme er eit legitimt oppfølgingsarbeid
  (DRY, jf. `specs/done/dry-opprydding.md`), men er ikkje del av denne
  konkrete bugfiksen.
- `validate-data`-targetet er **ikkje** affisert av denne speccen —
  0 sekund køyretid der er korrekt åtferd (ap-no-profilskjema har ingen
  `data/`-katalogar, jf. `CLAUDE.md` "Katalogstruktur").
- Ingen `.github/workflows/*.yml`-fil vert endra — `validate.yml` kallar
  berre `make validate-examples DOMAIN=...` og treng difor ikkje
  `actionlint`-køyring for denne speccen.

## Handlingsliste

- [ ] Fjern `xargs grep -l "tree_root: true"`-forfilteret i `validate-examples` (`make/40-validation.mk`)
- [ ] Legg til per-skjema tree_root-sjekk med fixture-fallback og synleg åtvaring ved manglande fixture
- [ ] Bruk `$$validate_schema` i valideringskallet, behald `$$schema` i `save-validation-log.py`-kallet
- [ ] Test `make validate-examples DOMAIN=ap-no` lokalt — stadfest at 6 skjema no validerer via fixture
- [ ] Regresjonstest `make validate-examples DOMAIN=<domene med tree_root>` — stadfest uendra åtferd
- [ ] Injiser ein feil i eit ap-no-eksempel og stadfest at `::error`-annotasjon og `exit 1` fungerer
