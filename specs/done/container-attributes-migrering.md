# Containerklasse: migrer frå globale slots til attributes

## Bakgrunn

CLAUDE.md har i dag ein intern inkonsistens:

- **«Slots, ikke attributes»-regelen** (linje 43-44) seier at alle eigenskapar skal modellerast som globale slots — *aldri* som `attributes:`.
- **«Containerklasse»-seksjonen** (linje 86-90) brukar omgrepet «attributter» utan å presisere om det gjeld YAML-nøkkelen `attributes:` eller globale slots.

I praksis er repoet delt i to:

| Mønster | Brukast av |
|---|---|
| `attributes:` i containerklassen | NGR-skjema (4), `converter.py` (generator), `specs/developer-onboarding.md` |
| Globale slots i containerklassen | FINT (6), `samt-bu`, `register-over-aksjeeiere`, alle 4 referanseskjema |

Endringa klargjerer at containerklassen er eit *strukturelt/serialiseringsankerpunkt*, ikkje ein semantisk klasse, og at berre domenemodellklassar skal bruke globale slots.

---

## Ny regel i CLAUDE.md

### Erstatt seksjonen «Slots, ikke attributes» (linje 43-75) med:

```markdown
### Slots, ikke attributes

Alle domenemodellklassar modellerer eigenskapane sine som globale slots under
`slots:` på toppnivå i skjemaet. Klasser refererer til slots via `slots:`-lista.
Klassespesifikke innskrenkingar (`required`, `in_subset` o.l.) ligg i `slot_usage`.

**Unntaket er containerklassen** (`tree_root: true`): her skal kvar klasse-referanse
modellerast som eit inline `attribute` direkte under containerklassen — ikkje som ein
global slot. Containerklassen er eit serialiseringsankerpunkt, ikkje ein semantisk
klasse, og attributtane hennar treng ikkje `slot_uri`.

# Riktig — domeneklasse brukar globale slots
slots:
  tittel:
    slot_uri: dct:title
    range: string

classes:
  Datasett:
    slots:
      - tittel

# Riktig — containerklassen brukar attributes
classes:
  Containerklasse:
    tree_root: true
    attributes:
      datasett:
        range: Datasett
        multivalued: true
        inlined: true
        inlined_as_list: true

# Feil — domeneklasse brukar attributes
classes:
  Datasett:
    attributes:
      tittel:
        slot_uri: dct:title
        range: string

# Feil — containerklassen brukar globale slots
slots:
  datasett:
    range: Datasett
    slot_uri: ex:datasett        ← unødvendig og forvirrande
    multivalued: true
    inlined: true
    inlined_as_list: true
```

### Oppdater «Containerklasse»-seksjonen (linje 86-94) med:

```markdown
### Containerklasse

Alle toppnivå domenemodeller skal ha éin containerklasse med `tree_root: true`.
Containerklassen er inngangspunktet for validering og serialisering.

Containerklassen brukar **`attributes:`** (ikkje `slots:`) for å referere til
kvar klasse som kan serialiserast i tilhøyrande datafil:

```yaml
Containerklasse:
  tree_root: true
  attributes:
    datasett:          # attributtnamn i fleirtal
      range: Datasett
      multivalued: true
      inlined: true
      inlined_as_list: true
```

- Attributtnamna skrives alltid i **fleirtal** (t.d. `datasett`, `katalogar`, `aktørar`)
- `range` må peike på ein klasse definert i skjemaet eller importerte skjema
- Ingen `slot_uri` — containerattributtar er strukturelle, ikkje semantiske
- Containerklassen treng ikkje `class_uri` (unntatt frå kravet per bronze-policy)
- AP-NO-modellar og fair-modellar skal ikkje ha eigen containerklasse
```

---

## Påverka filer

### Skjemafiler som MÅ endrast (brukar `slots:` i containerklassen)

| Fil | Containerklasse | Ant. containerslots |
|---|---|---|
| `src/linkml/fint/fint-administrasjon/fint-administrasjon-schema.yaml` | `AdministrasjonContainer` | ~199 |
| `src/linkml/fint/fint-arkiv/fint-arkiv-schema.yaml` | `ArkivContainer` | ~288 |
| `src/linkml/fint/fint-okonomi/fint-okonomi-schema.yaml` | `OkonomiContainer` | ~100 |
| `src/linkml/fint/fint-personvern/fint-personvern-schema.yaml` | `PersonvernContainer` | ~33 |
| `src/linkml/fint/fint-ressurs/fint-ressurs-schema.yaml` | `RessursContainer` | ~115 |
| `src/linkml/fint/fint-utdanning/fint-utdanning-schema.yaml` | `UtdanningContainer` | ~443 |
| `src/linkml/oreg/register-over-aksjeeiere/register-over-aksjeeiere-schema.yaml` | `Containerklasse` | ~6 + identifikator |
| `src/linkml/samt/samt-bu/samt-bu-schema.yaml` | `Containerklasse` | ~69 |
| `src/linkml/referanse/referanse-schema.yaml` | `Ressurskatalog` | 1 |
| `src/linkml/referanse/referanse-schema-bronze.yaml` | `Katalog` | 1 |
| `src/linkml/referanse/referanse-schema-silver.yaml` | `Containerklasse` | 10 |
| `src/linkml/referanse/referanse-schema-gold.yaml` | `Containerklasse` | 10 |

### Dokumentasjon som MÅ endrast

| Fil | Kva som skal endrast |
|---|---|
| `CLAUDE.md` | «Slots, ikke attributes»-regelen og «Containerklasse»-seksjonen (sjå over) |

### Filer som allereie er korrekte (ingen endring nødvendig)

| Fil | Status |
|---|---|
| `src/linkml/ngr/ngr-adresse/ngr-adresse-schema.yaml` | Brukar `attributes:` ✓ |
| `src/linkml/ngr/ngr-eiendom/ngr-eiendom-schema.yaml` | Brukar `attributes:` ✓ |
| `src/linkml/ngr/ngr-person/ngr-person-schema.yaml` | Brukar `attributes:` ✓ |
| `src/linkml/ngr/ngr-virksomhet/ngr-virksomhet-schema.yaml` | Brukar `attributes:` ✓ |
| `src/mcp-linkml-generator/converter.py` | Genererer `attributes:` ✓ |
| `specs/developer-onboarding.md` | Viser `attributes:`-mønsteret ✓ |

---

## Migrasjonsoppgåver per fil

### Generelt mønster

For kvar slot `<slotnamn>` under containerklassen:

1. **Finn** den globale slotdefinisjonen i `slots:`-seksjonen.
2. **Flytt** `range`, `multivalued`, `inlined`, `inlined_as_list` til eit inline attributt under containerklassen.
3. **Drop** `slot_uri`, `description` og `identifier` frå containerattributtet — desse høyrer ikkje heime her.
4. **Slett** den globale slotdefinisjonen frå `slots:`-seksjonen.
5. **Bytt** `slots:` under containerklassen til `attributes:`.

Døme (before/after):

```yaml
# FØR
classes:
  Containerklasse:
    tree_root: true
    slots:
      - datasett

slots:
  datasett:
    description: Datasetta i containeren.
    range: Datasett
    multivalued: true
    inlined: true
    inlined_as_list: true
    slot_uri: ex:datasett

# ETTER
classes:
  Containerklasse:
    tree_root: true
    attributes:
      datasett:
        range: Datasett
        multivalued: true
        inlined: true
        inlined_as_list: true
```

### Spesialtilfelle: `register-over-aksjeeiere`

Containerklassen har i dag `slots: [identifikator, aksjeselskaper, ...]` der `identifikator`
er ein `identifier: true`-slot. Containerklasser er ikkje semantiske einingar og bør ikkje
ha ein identifikator. To alternativ:

- **A (anbefalt)**: Fjern `identifikator`-sloten frå containerklassen og behold han berre
  i domenemodellklassane der han faktisk er definert.
- **B**: Behold `identifikator` som ein global slot referert via `slots:` på containerklassen
  (dvs. blanda `attributes:` og `slots:` — teknisk lovleg, men forvirrande).

Alternativ A er klart og ryddigast.

### FINT-skjema (store skjema)

FINT-skjema har svært mange containerslots (opp til 443 for fint-utdanning). Ingen
av desse har semantisk meining — dei er reine serialiseringsreferansar. Migreringa
er mekanisk og godt eigna for automatisering med eit skript.

Nokre FINT-containerslots har kommentarar (`# seksjon-namn`) som strukturerer lista.
Desse kan behaldast som kommentarar under `attributes:`-blokka.

---

## Validatorimplikasjonar

`_check_container_has_class` i `src/mcp-linkml-validator/server.py` er allereie
oppdatert til å sjekke **begge** mønster (attributtar *og* globale slots). Dette
tyder at migreringa kan gjerast gradvis — skjema som ikkje er migrerte enno,
fungerer framleis med sølv-policy-sjekkar.

Etter at alle skjema er migrerte kan validatoren forenklast til å berre sjekke
`cls.attributes` (fjerne global-slot-oppslaget), men dette er ikkje strengt nødvendig.

---

## Teststrategi

For kvart skjema som vert migrert:

```bash
# 1. Lint og instansvalidering (uendra etter migrering)
./tests/validate_schema.bash src/linkml/<domene>/<modell>/<modell>-schema.yaml \
                             examples/<domene>/<modell>-eksempel.yaml

# 2. Bronze-policy (skal vere uendra — ingen containerslots i global slots-sjekk lenger)
make mcp-validate SCHEMA=src/linkml/<domene>/<modell>/<modell>-schema.yaml POLICY=bronze

# 3. Full testsuite etter alle endringar
bash tests/test_make.sh
```

Det er viktig å køyre `test_make.sh` etter alle endringane sidan fleire testar
(gen-jsonschema, gen-python, gen-shacl o.a.) genererer artefakter frå skjemaet.
