# Importhierarki

!!! note "Beskrivelse"

    Dette dokumentet viser det komplette importhierarkiet for alle skjema i repoet.

## Korleis lese diagramma

**Viktig:** Importhierarki må lesast **frå høgre til venstre**.

Når du importerer eit skjema vil det automatisk inkludere alle avhengigheiter det har til venstre for seg i treet.

**Eksempel:**

Dersom du importerer `dcat-ap-no-schema`:

```
linkml:types
    └── common-ap-no-schema
        └── dcat-ap-no-schema  ← du importerer dette
```

...så får du automatisk med deg både `common-ap-no-schema` og `linkml:types` (alle avhengigheiter til venstre).

---

## AP-NO-hierarki

Norske applikasjonsprofil (AP-NO) for offentleg sektor.

```
linkml:types
    └── common-ap-no-schema
        ├── dqv-core-schema
        │   ├── dcat-ap-no-schema
        │   │   ├── dqv-ap-no-schema
        │   │   └── xkos-ap-no-schema
        │   └── skos-ap-no-schema
        ├── cpsv-ap-no-schema
        └── modelldcat-modell-schema
            └── modelldcat-katalog-schema
                └── modelldcat-ap-no-schema
```

**Reglane:**
- `common-ap-no-schema` er det einaste AP-NO-skjemaet som importerer direkte frå `linkml:types`
- Domenemodell-skjema importerer AP-NO-profilene, **ikkje** `common-ap-no-schema` direkte
- `dqv-core-schema` definerer felles DQV-klasser (`Kvalitetsmerknad`, `Kvalitetsmaaling` osv.)
- `dcat-ap-no-schema` importerer `dqv-core-schema` for å legge DQV-slots på `Datasett`
- `skos-ap-no-schema` importerer `dqv-core-schema` for DQV-støtte på SKOS-klasser
- `dqv-ap-no-schema` og `xkos-ap-no-schema` importerer `dcat-ap-no-schema` (og får dermed også `dqv-core-schema`)

**Sjå òg:**
- [AP-NO Arkitektur](ap-no-arkitektur.md) — arkitektoniske val og avvik i AP-NO-profilane

---

## FAIR-metadata

FAIR-metadata kan importerast av alle domenemodeller for å legge til FAIR-prinsipp-støtte.

```
linkml:types
    └── fair-metadata-schema
```

FAIR-skjemaet er standalone og kan kombinerast med både AP-NO, FINT og oreg-skjema.

---

## FINT-hierarki

FINT-domenemodellane for utdanning, administrasjon, arkiv m.m.

```
linkml:types
    └── fint-common-schema
        ├── fint-administrasjon-schema
        ├── fint-arkiv-schema
        ├── fint-okonomi-schema
        ├── fint-personvern-schema
        ├── fint-ressurs-schema
        └── fint-utdanning-schema
```

**Reglane:**
- `fint-common-schema` er det einaste FINT-skjemaet som importerer direkte frå `linkml:types`
- FINT-domenemodellane importerer `fint-common-schema`, **ikkje** `linkml:types` direkte
- FINT-skjema brukar `camelCase` for slots (arva frå FINT API-spesifikasjonen), ikkje `snake_case`

---

## Domenemodell-skjema

Domenemodell-skjema (t.d. SAMT, NGR) importerer AP-NO-profilene.

**Eksempel — SAMT-BU:**

```
linkml:types
    └── common-ap-no-schema
        └── dqv-core-schema
            └── dcat-ap-no-schema
                └── dqv-ap-no-schema
                    └── samt-bu-schema  ← domenemodell
```

`samt-bu-schema` importerer `dqv-ap-no-schema`, som igjen gir transitive avhengigheiter til `dcat-ap-no-schema`, `dqv-core-schema`, `common-ap-no-schema` og `linkml:types`.

---

## Import på tvers av domenemodeller

**Import mellom domenemodeller er tillate**, men krev varsomheit:

⚠️ **Alltid lås til ein konkret versjon** når du importerer ein domenemodell frå ein annan domenemodell. Dette er naudsynt fordi domenemodeller kan endre seg på måtar som bryt bakoverkompatibilitet (klasser/slots vert endra eller fjerna).

**Eksempel — korrekt versjonslåsing:**

```yaml
imports:
  - linkml:types
  - ../../ap-no/dcat-ap-no/dcat-ap-no-schema  # AP-NO-profil (stabil, relativ sti)
  - https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/v2.1.0/src/linkml/ngr/ngr-adresse/ngr-adresse-schema.yaml  # domenemodell (versjonslåst via git tag)
```

**Kvifor versjonslåse?**
- **AP-NO/FINT/FAIR-skjema** følgjer standardar og endrar seg sjeldan — treng ikkje versjonslåsing
- **Domenemodeller** (SAMT, NGR, oreg osv.) kan endre seg aktivt — versjonslåsing hindrar uventa brot

**Alternativ til import:**
- Dersom du berre treng ein eller to klasser, vurder å **kopiere klassedefinisjonane** i staden for å importere heile skjemaet
- Dette reduserer avhengigheiter og gir meir kontroll, men bryt DRY-prinsippet. Bruk med varsomhet!

---

## Kvifor importhierarki?

Importhierarkiet er repoets primære DRY-mekanisme for skjema: klasser og slots definerast éin stad og importerast nedover.

**Døme:**
- `Datasett`, `Katalog`, `Distribusjon` er definerte i `dcat-ap-no-schema`
- Alle domenemodell-skjema som importerer `dcat-ap-no-schema` får tilgang til desse klassane
- Ingen duplikasjon av klassedefinisjonar

Sjå `specs/done/avvik-modelldcat-ap-no.md` (MC8-MC11) for eit praktisk døme på korleis duplikate klasser vart fjerna ved å importere `dcat-ap-no-schema`.
