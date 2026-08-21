# Plan: omdøyp `<model>-schema.yaml` → `<model>.linkml.yaml`

## Bakgrunn og motivasjon

Noverande konvensjon: `ngr-adresse-schema.yaml`
Ny konvensjon: `ngr-adresse.linkml.yaml`

**For ny konvensjon:**
- Filnavnet identifiserer teknologien tydleg utan at ein må opne fila. `.linkml.yaml`
  er utydeleg — analogt med `*.test.ts`, `*.d.ts`, `*.spec.js`
- `schema` er eit generisk ord — nesten alle datafiler er "skjema" av eit slag.
  `.linkml` er spesifikt.
- Redaktørar og verktøy kan gjevast spesiell filhandtering for `*.linkml.yaml`
  (syntaxhighlighting, linting) utan å kollidere med andre YAML-filer.
- `name:`-feltet i skjemaet forblir *uendra* (`ngr-adresse`); berre filendinga endrar seg.

**Mot ny konvensjon:**
- `-schema.yaml` er konvensjonen i LinkML-prosjektdokumentasjonen og i mesteparten
  av LinkML-fellesskapet — nye brukarar vil kjenne det att.
- Brot for eksterne repo som refererer skjema via GitHub Raw URL (importar,
  `reusable-validate.yml`-input og `bootstrap.sh`-genererte konfigurasjonar).
- Høg endringskost: ~150 referansar i ~25 filer — omfanget er stort, men
  kan automatiserast nesten fullt ut.

**Vurdering:** Endringen er meiningsfull og gjennomførbar. Kostanden ligg i
eingangsarbeidet, ikkje i varig kompleksitet. Bryt med ekstern bruk og bør
difor koordinerast med ei versjonsbump.

---

## Omfang

### Schemafiler som skal omdøypast (29 filer)

**`src/linkml/` (27 filer):**

| Gamalt | Nytt |
|---|---|
| `ap-no/common/common-ap-no-schema.yaml` | `ap-no/common/common-ap-no.linkml.yaml` |
| `ap-no/cpsv-ap-no/cpsv-ap-no-schema.yaml` | `ap-no/cpsv-ap-no/cpsv-ap-no.linkml.yaml` |
| `ap-no/dcat-ap-no/dcat-ap-no-schema.yaml` | `ap-no/dcat-ap-no/dcat-ap-no.linkml.yaml` |
| `ap-no/dqv-ap-no/dqv-ap-no-schema.yaml` | `ap-no/dqv-ap-no/dqv-ap-no.linkml.yaml` |
| `ap-no/modelldcat-ap-no/modelldcat-ap-no-schema.yaml` | `ap-no/modelldcat-ap-no/modelldcat-ap-no.linkml.yaml` |
| `ap-no/skos-ap-no/skos-ap-no-schema.yaml` | `ap-no/skos-ap-no/skos-ap-no.linkml.yaml` |
| `ap-no/xkos-ap-no/xkos-ap-no-schema.yaml` | `ap-no/xkos-ap-no/xkos-ap-no.linkml.yaml` |
| `begrepskatalog/brreg-begrepskatalog/brreg-begrepskatalog-schema.yaml` | `…/brreg-begrepskatalog.linkml.yaml` |
| `fair/fair-metadata/fair-metadata-schema.yaml` | `fair/fair-metadata/fair-metadata.linkml.yaml` |
| `fint/fint-common/fint-common-schema.yaml` | `fint/fint-common/fint-common.linkml.yaml` |
| `fint/fint-administrasjon/fint-administrasjon-schema.yaml` | `…/fint-administrasjon.linkml.yaml` |
| `fint/fint-arkiv/fint-arkiv-schema.yaml` | `…/fint-arkiv.linkml.yaml` |
| `fint/fint-okonomi/fint-okonomi-schema.yaml` | `…/fint-okonomi.linkml.yaml` |
| `fint/fint-personvern/fint-personvern-schema.yaml` | `…/fint-personvern.linkml.yaml` |
| `fint/fint-ressurs/fint-ressurs-schema.yaml` | `…/fint-ressurs.linkml.yaml` |
| `fint/fint-utdanning/fint-utdanning-schema.yaml` | `…/fint-utdanning.linkml.yaml` |
| `modellkatalog/brreg-modellkatalog/brreg-modellkatalog-schema.yaml` | `…/brreg-modellkatalog.linkml.yaml` |
| `ngr/ngr-adresse/ngr-adresse-schema.yaml` | `ngr/ngr-adresse/ngr-adresse.linkml.yaml` |
| `ngr/ngr-eiendom/ngr-eiendom-schema.yaml` | `ngr/ngr-eiendom/ngr-eiendom.linkml.yaml` |
| `ngr/ngr-person/ngr-person-schema.yaml` | `ngr/ngr-person/ngr-person.linkml.yaml` |
| `ngr/ngr-virksomhet/ngr-virksomhet-schema.yaml` | `ngr/ngr-virksomhet/ngr-virksomhet.linkml.yaml` |
| `oreg/register-over-aksjeeiere/register-over-aksjeeiere-schema.yaml` | `…/register-over-aksjeeiere.linkml.yaml` |
| `referanse/referanse-schema.yaml` | `referanse/referanse.linkml.yaml` |
| `referanse/referanse-schema-bronze.yaml` | `referanse/referanse-bronze.linkml.yaml` |
| `referanse/referanse-schema-silver.yaml` | `referanse/referanse-silver.linkml.yaml` |
| `referanse/referanse-schema-gold.yaml` | `referanse/referanse-gold.linkml.yaml` |
| `samt/samt-bu/samt-bu-schema.yaml` | `samt/samt-bu/samt-bu.linkml.yaml` |

**`tests/` (2 filer):**

| Gamalt | Nytt |
|---|---|
| `tests/ap-no-catalog-bestatt-schema.yaml` | `tests/ap-no-catalog-bestatt.linkml.yaml` |
| `tests/ap-no-catalog-manglar-schema.yaml` | `tests/ap-no-catalog-manglar.linkml.yaml` |

> `tmp/person-schema.yaml` er auto-generert av `mcp-generate` og slettpast ved neste
> køyring. Ingen manuell handtering nødvendig.

### Import-referansar inne i schemafiler (16 filer, 17 krysskoplingar)

LinkML-importar skriv stien *utan* `.yaml`-endinga — loaderen legg til `.yaml` sjølv.
Importar må oppdaterast frå `-schema`-suffiks til `.linkml`:

```yaml
# Gamalt
imports:
  - ../common/common-ap-no-schema

# Nytt
imports:
  - ../common/common-ap-no.linkml
```

Alle 17 importar er mellom skjema i `src/linkml/` og gjeld følgjande par:

| Importerande skjema | Importert skjema (suffix) |
|---|---|
| cpsv-ap-no, dcat-ap-no, dqv-ap-no, modelldcat-ap-no, skos-ap-no, xkos-ap-no | `../common/common-ap-no.linkml` |
| dcat-ap-no | `../dqv-ap-no/dqv-ap-no.linkml` |
| dqv-ap-no | `../dcat-ap-no/dcat-ap-no.linkml` |
| fint-administrasjon, fint-arkiv, fint-okonomi, fint-personvern, fint-ressurs, fint-utdanning | `../fint-common/fint-common.linkml` |
| brreg-modellkatalog | `../../ap-no/modelldcat-ap-no/modelldcat-ap-no.linkml` |
| brreg-begrepskatalog | `../../ap-no/skos-ap-no/skos-ap-no.linkml` |
| samt-bu, referanse | `../../ap-no/dcat-ap-no/dcat-ap-no.linkml`, `../ap-no/dcat-ap-no/dcat-ap-no.linkml` |

### Konfigurasjon og skript (13 filer)

| Fil | Kva som endrar seg |
|---|---|
| `Makefile` | `find ... -name '*-schema.yaml'` → `'*.linkml.yaml'`; `basename "$s" -schema.yaml` → strip `.linkml.yaml`; alle hardkoda `$$profil-schema.yaml`-mønster; genererte filnavn (sjå nedanfor) |
| `tests/test_make.sh` | `find ... -name '*-schema.yaml'`; `basename "$schema" -schema.yaml` |
| `src/assets/scripts/scaffolding/new-modell.sh` | `SCHEMA_FILE="$SCHEMA_DIR/$NAME-schema.yaml"` → `$NAME.linkml.yaml` |
| `src/assets/scripts/migreringsscript/migrate-all-containers.sh` | `basename ... -schema.yaml`; `find ... -name '*-schema*.yaml'` |
| `src/mcp-linkml-validator/flatten-and-validate.bash` | Kommentarar med eksempelstiar |
| `.github/workflows/reusable-validate.yml` | Eksempel i `description:` |
| `.github/workflows/reusable-generate.yml` | Eksempel i `description:`; `NAME}-schema.ttl` |
| `bootstrap.sh` | Eksempel-config med `MODELL-schema.yaml` |
| `.mcp.json` | Eventuelle hardreferansar |

### Dokumentasjon (9 filer, ~80 referansar)

`CLAUDE.md`, `README.md`, `COMMANDS.md`, `mkdocs/docs/index.md`,
`mkdocs/docs/kom-i-gang/ny-domenemodell.md`, `mkdocs/docs/kom-i-gang/ny-begrepsmodell.md`,
`mkdocs/docs/publisering/publisering-begrep.md`, `mkdocs/docs/publisering/publisering-modell.md`,
`mkdocs/docs/arkitektur/ekstern-bruk.md`

### Genererte artefakter

Makefile genererer i dag `<name>-schema.ttl`, `<name>-schema.json`,
`<name>-schema.proto`. Desse er under `generated/` og er ikkje sjekka inn.
Med ny konvensjon bør dei heite `<name>.linkml.ttl` / `<name>.linkml.json` /
`<name>.linkml.proto` — elles er filnavna misvisande. Alternativt kan ein
beholde gamalt artefaktnavn og berre endre kjeldefilnavnet — dette er eit
separat val og har ingen ekstern effekt sidan generated/ ikkje er versjonskontrollert.

**Tilråding:** Endre genererte artefaktnavn konsekvent (`.linkml.ttl` etc.)
for at `generated/` reflekterer kjeldestruktur.

---

## Konvensjonsdokumentasjon som må oppdaterast

`CLAUDE.md` seier i dag:

> `name` | `kebab-case`, same som filnavnet utan `-schema.yaml` | `ngr-adresse`

Oppdaterast til:

> `name` | `kebab-case`, same som filnavnet utan `.linkml.yaml` | `ngr-adresse`

`name:`-verdiane i dei 27 skjemafilene er *uendra* — dei sluttar allereie
på modellnavnet utan suffiks.

---

## Ekstern brukarpåverknad

Dette er ei **brot-endring** for eksterne repo som:
1. Importerer AP-NO-skjema via GitHub Raw URL (hardkoda `-schema`-suffiks i URL)
2. Kallar `reusable-validate.yml` med `schema: src/linkml/.../<name>-schema.yaml`
   (dette er DEIRA eigne skjemafiler, ikkje filer i dette repoet — ikkje brot)
3. Har køyrt `bootstrap.sh` og fått generert konfig med `<name>-schema.yaml`

**Avbøtingstiltak:**
- Koordiner med ein semantisk versjonsbump (t.d. `v2.0.0`)
- Oppdater `bootstrap.sh` og `ekstern-bruk.md` med ny konvensjon
- Legg eit eingangs-kompatibilitets-notat i `CHANGELOG.md` / release notes

---

## Migrasjonsplan

Heile migrasjonen bør gjerast i éin PR — del-migrering vil brekke skjema-grafen
sidan importar er krysskoplingar (eit skjema med ny konvensjon som importerer eit
med gamal konvensjon vil feile).

### Steg 1 — Køyr migrasjonsskript

```bash
# 1a. Omdøyp alle schemafiler (git-sporbart)
find src/linkml tests -name '*-schema.yaml' | while read f; do
  new="${f%-schema.yaml}.linkml.yaml"
  git mv "$f" "$new"
done

# 1b. Oppdater import-referansar inne i skjema
find src/linkml -name '*.linkml.yaml' | xargs \
  sed -i 's|\(- \.\./[^/]*/[^/]*\)-schema$|\1.linkml|g; \
          s|\(- \.\./\.\./[^/]*/[^/]*/[^/]*\)-schema$|\1.linkml|g'

# 1c. Oppdater referansar i tests/
git mv tests/ap-no-catalog-bestatt-schema.yaml tests/ap-no-catalog-bestatt.linkml.yaml
git mv tests/ap-no-catalog-manglar-schema.yaml tests/ap-no-catalog-manglar.linkml.yaml
# Oppdater innhald i testfiksturar som refererer skjema med -schema
find tests -name '*.yaml' | xargs sed -i 's/-schema\.yaml$/.linkml.yaml/g'
```

### Steg 2 — Oppdater Makefile

Fire typar mønster:

| Gamalt mønster | Nytt mønster |
|---|---|
| `find ... -name '*-schema.yaml'` | `find ... -name '*.linkml.yaml'` |
| `basename "$s" -schema.yaml` | Krev ny logikk: `basename "$s" .yaml \| sed 's/\.linkml$//'` |
| `$$profil-schema.yaml` (dynamisk sti) | `$$profil.linkml.yaml` |
| generert artefaktnavn (`-schema.ttl`) | `.linkml.ttl` (om ein vel konsistente artefaktnavn) |

### Steg 3 — Oppdater test_make.sh

Same mønster som Makefile:
- `find ... -name '*-schema.yaml'` → `*.linkml.yaml`
- `basename "$schema" -schema.yaml` → strip `.linkml.yaml`

### Steg 4 — Oppdater skript og verktøy

- `src/assets/scripts/scaffolding/new-modell.sh`: `$NAME-schema.yaml` → `$NAME.linkml.yaml`
- `src/assets/scripts/migreringsscript/migrate-all-containers.sh`: same
- `bootstrap.sh`: eksempel-config

### Steg 5 — Oppdater dokumentasjon

`find . -name '*.md' | xargs sed -i 's/<name>-schema\.yaml/<name>.linkml.yaml/g'`
+ manuelle gjennomgangar for kontekst-avhengige formuleringar (t.d. avsnittstitlar
som "Skriv `<katalognavn>-schema.yaml`").

### Steg 6 — Oppdater CLAUDE.md

`name:`-konvensjonen: `-schema.yaml` → `.linkml.yaml`.

### Steg 7 — Verifiser

```bash
# Ingen gjenverande -schema.yaml (unntatt tmp/ og generated/):
find src tests -name '*-schema.yaml' | grep -v '^tmp/'

# Køyr full testsuite:
bash tests/test_make.sh

# Verifiser at import-grafen løyser seg:
make validate DOMAIN=ap-no
make validate DOMAIN=fint
```

---

## Risikopunkt

| Risiko | Sannsynlegheit | Tiltak |
|---|---|---|
| Import-sti ikkje oppdatert atomisk | Høg (16 filer) | Migrasjonsskript + test heile grafen umiddelbart |
| `basename`-logikk i Makefile knekk `schema_name` | Medium | Dedikert teststeg etter Makefile-endring |
| Ekstern repo-brot via GitHub Raw URL | Høg | Versjonsbump + migrasjonsrettleiing |
| LinkML-verktøy som hardkoder `-schema` suffix internt | Lav | Ikkje observert i codebase; `gen-*` bryr seg ikkje om filnavn |
| Referansar i `generated/` peikar på gamal fil | Ingen (generated/ ikkje versjonskontrollert) | Køyr `make clean && make <domain>` etter migrering |
