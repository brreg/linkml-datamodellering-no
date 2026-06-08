# Containerklasse: konsistent namngjeving med «Container»-suffiks

## Bakgrunn

CLAUDE.md krev at alle toppnivå domenemodeller skal ha éin containerklasse med
`tree_root: true`. Repoet har likevel ingen einsarta namnegjeving av desse klassane:

| Mønster | Eksempel | Brukast av |
|---|---|---|
| `<Domene>Container` | `AdministrasjonContainer`, `AdresseContainer` | FINT (6), NGR (4) — **10 skjema** |
| `Containerklasse` | — | `samt-bu`, `register-over-aksjeeiere`, `referanse-schema-silver`, `referanse-schema-gold` — **4 skjema** |
| Domenenamn utan «Container» | `Ressurskatalog`, `Katalog` | `referanse-schema`, `referanse-schema-bronze` — **2 skjema** |

Den generiske `Containerklasse`-varianten er problematisk:

- Klassen er usynleg i verktøy som Ontodia og gen-erdiagram som viser klassenamn.
- Saman med `tree_root: true` og `class_uri`-fritak ser klassen ut som ein anonym
  internstruktur, ikkje ein del av domenemodellen.
- Ein importert skjema med `Containerklasse` skapar namnekonflikt om eit anna importert
  skjema òg heiter `Containerklasse`.

`Ressurskatalog` og `Katalog` er i tillegg villfarne fordi dei lèt containerklassen framstå
som ein semantisk klasse med eigen identitet — noko den *ikkje* er.

---

## Ny regel

Containerklassen skal alltid namngjevast etter mønsteret **`<Domene>Container`**:

- Suffikset `Container` er alltid til stades og alltid til slutt.
- Prefikset `<Domene>` er eit PascalCase-ord avleidd av det primære domenet eller
  modellenamnet (t.d. `Administrasjon`, `Adresse`, `Aksjeeier`).
- Prefikset skal **ikkje** gjenta informasjon som allereie er i suffikset
  (t.d. `ContainerContainer` → feil).

### Oppdater «Containerklasse»-seksjonen i CLAUDE.md

Legg til ei ny punktliste-linje under eksisterande krav:

```markdown
- Klassenamnet følgjer mønsteret `<Domene>Container` i PascalCase
  (t.d. `AdresseContainer`, `AksjeeierContainer`) — aldri berre `Containerklasse`
```

---

## Påverka filer

### Skjemafiler som MÅ endrast

| Fil | Noverande namn | Nytt namn |
|---|---|---|
| `src/linkml/oreg/register-over-aksjeeiere/register-over-aksjeeiere-schema.yaml` | `Containerklasse` | `AksjeeierContainer` |
| `src/linkml/samt/samt-bu/samt-bu-schema.yaml` | `Containerklasse` | `SamtBuContainer` |
| `src/linkml/referanse/referanse-schema.yaml` | `Ressurskatalog` | `ReferanseContainer` |
| `src/linkml/referanse/referanse-schema-bronze.yaml` | `Katalog` | `ReferanseBronseContainer` |
| `src/linkml/referanse/referanse-schema-silver.yaml` | `Containerklasse` | `ReferanseSølvContainer` |
| `src/linkml/referanse/referanse-schema-gold.yaml` | `Containerklasse` | `ReferanseGullContainer` |

### Eksempelfiler som MÅ endrast

Containerklassenamnet er toppnivånøkkel i alle eksempel-YAML-filer:

| Fil | Toppnivånøkkel som må endrast |
|---|---|
| `examples/oreg/register-over-aksjeeiere-eksempel.yaml` | `Containerklasse` → `AksjeeierContainer` |
| `examples/samt/samt-bu-eksempel.yaml` | `Containerklasse` → `SamtBuContainer` |
| `examples/referanse/referanse-eksempel.yaml` | `Ressurskatalog` → `ReferanseContainer` |

### Filer som allereie er korrekte (ingen endring)

| Fil | Containerklassenamn |
|---|---|
| `src/linkml/fint/fint-administrasjon/fint-administrasjon-schema.yaml` | `AdministrasjonContainer` ✓ |
| `src/linkml/fint/fint-arkiv/fint-arkiv-schema.yaml` | `ArkivContainer` ✓ |
| `src/linkml/fint/fint-okonomi/fint-okonomi-schema.yaml` | `OkonomiContainer` ✓ |
| `src/linkml/fint/fint-personvern/fint-personvern-schema.yaml` | `PersonvernContainer` ✓ |
| `src/linkml/fint/fint-ressurs/fint-ressurs-schema.yaml` | `RessursContainer` ✓ |
| `src/linkml/fint/fint-utdanning/fint-utdanning-schema.yaml` | `UtdanningContainer` ✓ |
| `src/linkml/ngr/ngr-adresse/ngr-adresse-schema.yaml` | `AdresseContainer` ✓ |
| `src/linkml/ngr/ngr-eiendom/ngr-eiendom-schema.yaml` | `EiendomContainer` ✓ |
| `src/linkml/ngr/ngr-person/ngr-person-schema.yaml` | `PersonContainer` ✓ |
| `src/linkml/ngr/ngr-virksomhet/ngr-virksomhet-schema.yaml` | `VirksomhetContainer` ✓ |

---

## Migrasjonsoppgåver per fil

### Generelt mønster

For kvart skjema:

1. Byt klassenamnet under `classes:`:
   ```yaml
   # FØR
   classes:
     Containerklasse:
       tree_root: true
   
   # ETTER
   classes:
     AksjeeierContainer:
       tree_root: true
   ```

2. Byt alle referansar til klassen i same skjemafil (t.d. i `range:` eller kommentarar).

3. Byt toppnivånøkkelen i tilhøyrande eksempelfil:
   ```yaml
   # FØR
   Containerklasse:
     aksjeselskaper:
       - ...
   
   # ETTER
   AksjeeierContainer:
     aksjeselskaper:
       - ...
   ```

Ingen av containerklassane vert importert av andre skjema (dei har `tree_root: true`
og er sluttnoden i importkjeda), så endringa har ingen ringverknad utanfor kvart enkelt par
av `*-schema.yaml` + `*-eksempel.yaml`.

### `referanse-schema.yaml` — `Ressurskatalog` → `ReferanseContainer`

`Ressurskatalog` dukkar opp tre stader i fila:

- Klassedefinisjonen under `classes:`.
- Kommentaren rett over definisjonen (`# Containerklassen er inngangspunktet …`).
- Som toppnivånøkkel i `examples/referanse/referanse-eksempel.yaml`.

### `referanse-schema-bronze.yaml` — `Katalog` → `ReferanseBronseContainer`

`Katalog` er i dag *berre* containerklasse i dette skjemaet, utan `class_uri`.
Domenemodellklassar i andre skjema kan heite `Katalog` med `class_uri: dcat:Catalog` —
dei to er uavhengige. Endringa skapar ingen konflikt.

### Referanseskjema (`silver`, `gold`) — `Containerklasse` → `Referanse{Sølv|Gull}Container`

Desse er reine test-/dokumentasjonsskjema utan eksempelfiler, så endringa er
avgrensa til klassedefinisjonen i kvar YAML-fil.

---

## Validatorimplikasjonar

Bronze-policyen sjekkar ikkje klassenamn. Det er ikkje nødvendig å leggje til ein
eigen navnsjekk i MCP-validatoren — konvensjonen handhevas via CLAUDE.md og
ved gjennomgang av PR-ar.

Dersom ein ønskjer automatisk kontroll, kan ein leggje til ei enkel sjekk i
`_check_tree_root` (eller ein ny funksjon) i `src/mcp-linkml-validator/server.py`:

```python
# Forslag til warning-regel (ikkje krav for nokon policy-nivå)
for name, cls in schema.classes.items():
    if getattr(cls, "tree_root", False) and "container" not in name.lower():
        issues.append(SchemaIssue(
            level="warning",
            rule="container_class_name",
            message=f"Containerklassen '{name}' bør ha 'Container' i namnet",
        ))
```

---

## Teststrategi

For kvart skjema:

```bash
# 1. Lint (strukturvalidering)
make validate SCHEMA=src/linkml/<domene>/<modell>/<modell>-schema.yaml

# 2. Instansvalidering
./tests/validate_schema.bash src/linkml/<domene>/<modell>/<modell>-schema.yaml \
                             examples/<domene>/<modell>-eksempel.yaml

# 3. Full testsuite etter alle endringar
bash tests/test_make.sh
```

Fordi containerklassenamnet er toppnivånøkkelen i eksempel-YAML-filene, vil steg 2
fange opp om eksempelfila ikkje er oppdatert i takt med skjemaet.
