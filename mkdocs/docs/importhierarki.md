# Importhierarki

Dette dokumentet viser det komplette importhierarkiet for alle skjema i repoet.

## Korleis lese diagramma

**Viktig:** Diagramma må lesast **frå høgre til venstre**.

Når du importerer eit skjema vil det automatisk inkludere alle avhengigheiter det har til venstre for seg i treet.

**Eksempel:**

Dersom du importerer `dcat-ap-no`:

```
linkml:types
    └── common-ap-no
        └── dcat-ap-no  ← du importerer dette
```

...så får du automatisk med deg både `common-ap-no` og `linkml:types` (alle avhengigheiter til venstre).

---

## AP-NO-hierarki

Norske applikasjonsprofil (AP-NO) for offentleg sektor.

```
linkml:types
    └── common-ap-no
        ├── dqv-core
        │   └── dcat-ap-no  ← importerer dqv-core
        ├── dqv-ap-no  ← importerer dcat-ap-no (sirkulær via dqv-core)
        ├── skos-ap-no
        ├── xkos-ap-no
        ├── cpsv-ap-no
        └── modelldcat-modell
            └── modelldcat-katalog
                └── modelldcat-ap-no
```

**Reglane:**
- `common-ap-no` er det einaste AP-NO-skjemaet som importerer direkte frå `linkml:types`
- Domenemodell-skjema importerer AP-NO-profilene, **ikkje** `common-ap-no` direkte
- `dqv-core` er eit bridge-skjema for å bryte sirkulær import mellom `dcat-ap-no` og `dqv-ap-no`

**Sjå òg:**
- [AP-NO Arkitektur](ap-no-arkitektur.md) — arkitektoniske val og avvik i AP-NO-profilane

---

## FINT-hierarki

FINT-domenemodellane for utdanning, administrasjon, arkiv m.m.

```
linkml:types
    └── fint-common
        ├── fint-administrasjon
        ├── fint-arkiv
        ├── fint-okonomi
        ├── fint-personvern
        ├── fint-ressurs
        └── fint-utdanning
```

**Reglane:**
- `fint-common` er det einaste FINT-skjemaet som importerer direkte frå `linkml:types`
- FINT-domenemodellane importerer `fint-common`, **ikkje** `linkml:types` direkte
- FINT-skjema brukar `camelCase` for slots (arva frå FINT API-spesifikasjonen), ikkje `snake_case`

---

## Offentlege register (oreg)

Skjema for offentlege register (Enhetsregisteret, aksjeeierregister m.m.).

```
linkml:types
    └── enhetsregisteret-bvrinn
    └── register-over-aksjeeiere
```

**Reglane:**
- Oreg-skjema importerer berre `linkml:types` (ingen felles base-skjema)
- Kan importere AP-NO-profil(er) etter behov (t.d. `dcat-ap-no` for metadata)

---

## Domenemodell-skjema

Domenemodell-skjema (t.d. SAMT, NGR) importerer AP-NO-profilene.

**Eksempel — SAMT-BU:**

```
linkml:types
    └── common-ap-no
        ├── dqv-core
        │   └── dcat-ap-no
        │       ├── dqv-ap-no
        │       └── samt-bu  ← domenemodell
        └── dcat-ap-no
```

`samt-bu` importerer `dcat-ap-no` og `dqv-ap-no`, som igjen gir transitive avhengigheiter til `common-ap-no` og `linkml:types`.

---

## FAIR-metadata

FAIR-metadata kan importerast av alle domenemodeller for å legge til FAIR-prinsipp-støtte.

```
linkml:types
    └── fair-metadata
```

FAIR-skjemaet er standalone og kan kombinerast med både AP-NO, FINT og oreg-skjema.

---

## Kvifor importhierarki?

Importhierarkiet er repoets primære DRY-mekanisme for skjema: klasser og slots definerast éin stad og importerast nedover.

**Døme:**
- `Datasett`, `Katalog`, `Distribusjon` er definerte i `dcat-ap-no`
- Alle domenemodell-skjema som importerer `dcat-ap-no` får tilgang til desse klassane
- Ingen duplikasjon av klassedefinisjonar

Sjå `specs/done/avvik-modelldcat-ap-no.md` (MC8-MC11) for eit praktisk døme på korleis duplikate klasser vart fjerna ved å importere `dcat-ap-no`.
