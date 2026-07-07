# Motseiiande tekst i Avhengigheiter-seksjonen

## Bakgrunn

Avhengigheiter-seksjonen i `index.md` per skjema viser **fullstendig importkjede** (direkte og transitive importar) som eit tre-diagram. Likevel avsluttar seksjonen med teksten:

> *Sjå [Importhierarki](../../importhierarki.md) for fullstendig importkjede.*

Dette er motseiiande, fordi den fullstendige importkjeda **allereie er vist** i diagrammet ovanfor.

**Eksempel frå `dcat-ap-no/index.md`:**

```
## Avhengigheiter

### Imports

Dette skjemaet importerer følgjande skjema (direkte og transitivt):

```
linkml:types  # direkte import
└── common-ap-no-schema  # direkte import
    └── dqv-core-schema  # direkte import
```

!!! note "Leseretning"
    Diagrammet ovanfor viser avhengigheiter **frå høgre til venstre**. Dette skjemaet
    importerer dei skjemaa som står lengst til høgre, som igjen automatisk inkluderer
    alle sine avhengigheiter lengre til venstre i treet.

*Sjå [Importhierarki](../../importhierarki.md) for fullstendig importkjede.*
```

Diagrammet viser `linkml:types` → `common-ap-no-schema` → `dqv-core-schema` — det **er** den fullstendige importkjeda.

## Problem

1. **Motseiiande tekst:** Seksjonen seier brukaren skal sjå `importhierarki.md` for noko som allereie er vist
2. **Uklar verdi av lenka:** Kva får brukaren ved å klikke på lenka som dei ikkje alt har?
3. **Duplisert informasjon:** `importhierarki.md` inneheld same importkjede, berre i kontekst av alle andre skjema i repoet

## Løysing

### Alternativ 1: Fjern lenka heilt

**Rasjonale:** Fullstendig importkjede er allereie vist — lenka er overflødig.

**Implementering:**
- Fjern siste linje `*Sjå [Importhierarki](../../importhierarki.md) for fullstendig importkjede.*`
- Behald Leseretning-boksen

### Alternativ 2: Endre teksten til å forklare verdien av lenka

**Rasjonale:** `importhierarki.md` har verdi som oversikt over **heile repoet sitt importhierarki** — ikkje berre dette skjemaet.

**Implementering:**
- Endre teksten til: `*Sjå [Importhierarki](../../importhierarki.md) for oversikt over heile repoet sitt importhierarki.*`

### Alternativ 3: Endre teksten til å skilje mellom "dette skjemaet" og "alle skjema"

**Rasjonale:** Presisere at diagrammet viser **dette skjemaet** sin importkjede, medan lenka viser **alle skjema** sitt importhierarki.

**Implementering:**
- Endre teksten til: `*Sjå [Importhierarki](../../importhierarki.md) for oversikt over alle skjema i repoet.*`

## Anbefaling

**Alternativ 3** er best — det presiserer kva lenka gir som **tilleggsverdi** utan å hevde at noko manglar i noverande diagram:

> *Sjå [Importhierarki](../../importhierarki.md) for oversikt over alle skjema i repoet.*

Dette kommuniserer:
- Noverande diagram er komplett for **dette skjemaet**
- Lenka gir **breiare kontekst** — heile repoet sitt importhierarki

## Handlingsliste

1. [x] Finn kor teksten vert generert i `mkdocs/lib/sections/*.sh` → `dependencies.sh:46`
2. [x] Endre teksten frå `"for fullstendig importkjede"` til `"for oversikt over heile repoet sitt importhierarki"`
3. [x] Kjør `make docs-publish`
4. [x] Verifiser endringa i minst 2 skjema (`dcat-ap-no`, `ngr-adresse`, `fint-administrasjon`)

## Utført

Alternativ 2 er implementert. Alle skjema som har Avhengigheiter-seksjonen viser no:

> *Sjå [Importhierarki](../../importhierarki.md) for oversikt over heile repoet sitt importhierarki.*

Dette presiserer verdien av lenka — den gir oversikt over **heile repoet**, ikkje berre dette skjemaet — utan å hevde at noverande diagram er ufullstendig.
