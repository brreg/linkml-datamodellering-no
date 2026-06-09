# Oppdater referansar til sletta bash-skript

## Bakgrunn

`tests/lint_schema.bash` og `tests/validate_schema.bash` er sletta og erstatta med
`make lint` og `make validate-instance`. Tre aktive filer refererer framleis til dei
sletta skriptane og må oppdaterast.

Referansar i `specs/done/` er historisk dokumentasjon og skal ikkje endrast.

---

## Tiltak

### 1. `CLAUDE.md` — linje 31

Instruksjonen i «Valider arbeidet ditt»-blokka brukar `validate_schema.bash` med eit
konkret eksempel. Erstatt med `make validate-instance`.

**Før:**
```bash
# Lint og valider eksempel etter kvar endring i eit skjema:
./tests/validate_schema.bash ./src/linkml/samt/samt-bu/samt-bu-schema.yaml ./src/linkml/samt/samt-bu/examples/samt-bu-eksempel.yaml
```

**Etter:**
```bash
# Lint og valider eksempel etter kvar endring i eit skjema:
make validate-instance SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml INSTANCE=src/linkml/samt/samt-bu/examples/samt-bu-eksempel.yaml
```

Legg òg til `make lint` som eigen linje før `validate-instance` sidan CLAUDE.md-kommentaren
seier «lint og valider»:

```bash
# Lint og valider eksempel etter kvar endring i eit skjema:
make lint SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml
make validate-instance SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml INSTANCE=src/linkml/samt/samt-bu/examples/samt-bu-eksempel.yaml
```

---

### 2. `CONTRIBUTING.md` — linje 28

Valideringseksempelet brukar `validate_schema.bash` og `<domene>` (skal vere `<domain>`).
Erstatt med `make validate-instance` og rett plasshaldrane.

**Før:**
```bash
./tests/validate_schema.bash src/linkml/<domene>/<modell>/<modell>-schema.yaml examples/<domene>/<modell>-eksempel.yaml
```

**Etter:**
```bash
make validate-instance SCHEMA=src/linkml/<domain>/<modell>/<modell>-schema.yaml INSTANCE=src/linkml/<domain>/<modell>/examples/<modell>-eksempel.yaml
```

Merk: eksempelstien i originalen (`examples/<domene>/...`) er feil — eksempelfiler ligg
under `src/linkml/<domain>/<modell>/examples/`, ikkje i ein rot-`examples/`-katalog.

---

### 3. `mkdocs/docs/ny-domenemodell.md` — linje 47

Hurtigvalideringseksempelet i steg 3 brukar `lint_schema.bash` og `<domene>`.
Erstatt med `make lint` og rett plasshaldrane.

**Før:**
```
`./tests/lint_schema.bash src/linkml/<domene>/<modell>/<modell>-schema.yaml`
```

**Etter:**
```
`make lint SCHEMA=src/linkml/<domain>/<modell>/<modell>-schema.yaml`
```

---

## Prioritert tiltaksliste

| # | Fil | Endring | Prioritet |
|---|---|---|---|
| 1 | `CLAUDE.md` | Erstatt `validate_schema.bash` med `make lint` + `make validate-instance` | Høg |
| 2 | `CONTRIBUTING.md` | Erstatt `validate_schema.bash` med `make validate-instance`; rett stiformat og `<domene>` → `<domain>` | Høg |
| 3 | `mkdocs/docs/ny-domenemodell.md` | Erstatt `lint_schema.bash` med `make lint`; rett `<domene>` → `<domain>` | Høg |
