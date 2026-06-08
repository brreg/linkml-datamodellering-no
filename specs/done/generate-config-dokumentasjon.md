# Dokumentasjon av generate.yaml — plan

## Bakgrunn

`generate.yaml` er no implementert: kvar modell under `src/linkml/<domene>/<modell>/`
har ei eiga fil som styrer kva artefaktar som vert genererte og med kva flagg.
Makefile-en les desse via `config.mk` (generert av `src/assets/scripts/gen-config.sh`).

Dokumentasjonen er enno ikkje oppdatert til å reflektere dette. Planen under
skildrar kva filer som skal opprettast eller oppdaterast, og kva som skal stå kvar.

---

## Kva skal dokumenterast

| # | Fil | Endring |
|---|---|---|
| 1 | `mkdocs/docs/generate-config.md` | Ny side — komplett referanse for `generate.yaml` |
| 2 | `mkdocs/mkdocs.yml` | Legg til ny side under «Rettleiingar» |
| 3 | `mkdocs/docs/ny-domenemodell.md` | Legg til `generate.yaml`-seksjon i arbeidsflyta |
| 4 | `README.md` | Oppdater «Unntak»-noten under «Genererte artefakter» |

---

## Steg 1 — `mkdocs/docs/generate-config.md` (ny fil)

**Tittel:** `Generatorkonfigurasjon (generate.yaml)`

**Seksjonar:**

### Kva er `generate.yaml`?
Kort forklaring: fila styrer kva artefaktar som vert genererte frå modellen og med
kva flagg. Ein modell utan fila brukar standardkonfigurasjonen (alle generatorar på,
ingen flagg). `make new-model` oppretter fila automatisk.

### Plassering
```
src/linkml/<domene>/<modell>/generate.yaml
```

### Feltliste

Dei boolske felta svarar 1:1 til artefaktkolonnen i README-tabellen «Genererte artefakter»
— sjå den for filnamn og brukstilfelle per generator. I tillegg kjem to flagg-felt:

| Felt | Type | Standard | Skildring |
|---|---|---|---|
| `shacl_flags` | streng | `""` | Ekstra flagg til `gen-shacl`, t.d. `"--exclude-imports"` |
| `owl_flags` | streng | `""` | Ekstra flagg til `gen-owl`, t.d. `"--log_level ERROR"` |

Alle boolske felt har standardverdi `true`.

### Tre eksempel

**Standardkonfig (NGR, OREG):**
```yaml
generators:
  jsonld_context: true
  shacl: true
  shacl_flags: ""
  python: true
  json_schema: true
  owl: true
  owl_flags: ""
  rdf: true
  protobuf: true
  erdiagram: true
  docs: true
  plantuml: true
  example_rdf: true
```

**FINT (`rdf: false`, flagg for SHACL og OWL, `example_rdf: false` der eksempelfila
har FINT-stile CURIEs som ikkje er gyldige URI-ar):**
```yaml
generators:
  jsonld_context: true
  shacl: true
  shacl_flags: "--exclude-imports"
  python: true
  json_schema: true
  owl: true
  owl_flags: "--log_level ERROR"
  rdf: false
  protobuf: true
  erdiagram: true
  docs: true
  plantuml: true
  example_rdf: false
```

**AP-NO / FAIR (`example_rdf: false` — ingen `tree_root`, kan ikkje konverterast):**
```yaml
generators:
  ...
  example_rdf: false
```

### Korleis `config.mk` vert generert

`config.mk` er eit Makefile-fragment som vert automatisk regenerert når ei
`generate.yaml` endrar seg:

```bash
make config.mk   # regenerer manuelt ved behov
```

Fila er generert og skal ikkje redigerast for hand. Ho er lagd til `.gitignore`
(eller bør leggjast til).

### Nye modellar

`make new-model NAME=... DOMAIN=...` oppretter ei standard `generate.yaml` saman
med skjemafila. Juster henne etterpå viss domenet krev det (t.d. for FINT-modellar).

---

## Steg 2 — `mkdocs/mkdocs.yml`

Legg til `generate-config.md` under `Rettleiingar`-seksjonen:

```yaml
nav:
  - Heim: index.md
  - Rettleiingar:
      - Ny domenemodell: ny-domenemodell.md
      - Generatorkonfigurasjon: generate-config.md   # ← ny linje
```

---

## Steg 3 — `mkdocs/docs/ny-domenemodell.md`

Legg til ein ny seksjon **etter** «Genererte artefakter» (linje ~145):

**`## Tilpass generatorane`**

Kort intro: kvar modell har ei `generate.yaml` som styrer kva artefaktar som vert
genererte. `make new-model` oppretter standardkonfigen automatisk.

Vis korleis ein endrar ein generator og køyrer `make config.mk` etterpå.

Lenk til den nye referansesida: `[Generatorkonfigurasjon](generate-config.md)`.

---

## Steg 4 — `README.md`

Erstatt den hardkoda «Unntak»-noten under «Genererte artefakter»:

**Før:**
```
**Unntak:** FINT-domenemodellane genererer ikkje `schema.ttl` eller SHACL shapes med full import-kjede.
```

**Etter:**
```
Kva artefaktar som vert genererte per modell er konfigurert i `generate.yaml` ved sida av skjemaet.
```

---

## Rekkjefølgje

1. Lag `mkdocs/docs/generate-config.md`
2. Oppdater `mkdocs/mkdocs.yml`
3. Oppdater `mkdocs/docs/ny-domenemodell.md`
4. Oppdater `README.md`
