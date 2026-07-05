# Importhierarki

Dette dokumentet viser det komplette importhierarkiet for alle skjema i repoet.

## Korleis lese diagramma

**Viktig:** Diagramma må lesast **frå høgre til venstre**.

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
        │   └── dcat-ap-no-schema  ← importerer dqv-core-schema
        ├── dqv-ap-no-schema  ← importerer dcat-ap-no-schema (sirkulær via dqv-core-schema)
        ├── skos-ap-no-schema
        ├── xkos-ap-no-schema
        ├── cpsv-ap-no-schema
        └── modelldcat-modell-schema
            └── modelldcat-katalog-schema
                └── modelldcat-ap-no-schema
```

**Reglane:**
- `common-ap-no-schema` er det einaste AP-NO-skjemaet som importerer direkte frå `linkml:types`
- Domenemodell-skjema importerer AP-NO-profilene, **ikkje** `common-ap-no-schema` direkte
- `dqv-core-schema` er eit bridge-skjema for å bryte sirkulær import mellom `dcat-ap-no-schema` og `dqv-ap-no-schema`

**Sjå òg:**
- [AP-NO Arkitektur](ap-no-arkitektur.md) — arkitektoniske val og avvik i AP-NO-profilane

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

## Offentlege register (oreg)

Skjema for offentlege register (Enhetsregisteret, aksjeeierregister m.m.).

```
linkml:types
    └── enhetsregisteret-bvrinn-schema
    └── register-over-aksjeeiere-schema
```

**Reglane:**
- Oreg-skjema importerer berre `linkml:types` (ingen felles base-skjema)
- Kan importere AP-NO-profil(er) etter behov (t.d. `dcat-ap-no-schema` for metadata)

---

## Domenemodell-skjema

Domenemodell-skjema (t.d. SAMT, NGR) importerer AP-NO-profilene.

**Eksempel — SAMT-BU:**

```
linkml:types
    └── common-ap-no-schema
        ├── dqv-core-schema
        │   └── dcat-ap-no-schema
        │       ├── dqv-ap-no-schema
        │       └── samt-bu-schema  ← domenemodell
        └── dcat-ap-no-schema
```

`samt-bu-schema` importerer `dcat-ap-no-schema` og `dqv-ap-no-schema`, som igjen gir transitive avhengigheiter til `common-ap-no-schema` og `linkml:types`.

---

## FAIR-metadata

FAIR-metadata kan importerast av alle domenemodeller for å legge til FAIR-prinsipp-støtte.

```
linkml:types
    └── fair-metadata-schema
```

FAIR-skjemaet er standalone og kan kombinerast med både AP-NO, FINT og oreg-skjema.

---

## Kvifor importhierarki?

Importhierarkiet er repoets primære DRY-mekanisme for skjema: klasser og slots definerast éin stad og importerast nedover.

**Døme:**
- `Datasett`, `Katalog`, `Distribusjon` er definerte i `dcat-ap-no-schema`
- Alle domenemodell-skjema som importerer `dcat-ap-no-schema` får tilgang til desse klassane
- Ingen duplikasjon av klassedefinisjonar

Sjå `specs/done/avvik-modelldcat-ap-no.md` (MC8-MC11) for eit praktisk døme på korleis duplikate klasser vart fjerna ved å importere `dcat-ap-no-schema`.
