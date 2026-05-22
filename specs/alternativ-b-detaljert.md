# Alternativ B – detaljert utbygging

Utdjuping av «Alternativ B – Eige repo med URL-importer» frå [distribusjonsmodell.md](distribusjonsmodell.md).
Målet er at ein ekstern utviklar kan leggje til LinkML-modellering i eit eksisterande repo og bruke
AP-NO-profilene og verktøya herifrå utan å bu i dette monorepoet.

---

## Grunnføresetnad

Reusable workflows (GitHub Actions) køyrer på GitHub sine runnerar — dei har alltid nettverkstilgang.
Det eliminerer behovet for lokal vendor-caching av AP-NO-skjema. På same måten kan den reusable
workflowen sjølv hente genererte artefaktar frå dette repoet i staden for at det eksterne repoet
må kopiere eller lagre dei.

---

## Dei fem ulempene og forslag til løysing

### Ulempe 1 – AP-NO-profilene har ikkje stabile, publiserte URL-ar

**Rot-årsak:** Importane brukar relative stiar (`../../ap-no/...`) som berre fungerer inne i dette repoet.

**Løysing: GitHub raw-URL med semantisk versjon-tag**

GitHub Raw-tenesta serverer filer frå kva som helst commit, branch eller tag:

```
https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/<tag>/src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml
```

Alle skjema-ID-ar har allereie `https://data.norge.no/linkml/<namn>` som `id:` — det er den semantiske
identifikatoren. GitHub Raw er *transport-URL-en*. Desse to er uavhengige.

**Korleis eksterne skjema ser ut:**

```yaml
imports:
  - linkml:types
  - https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/v1.0.0/src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema
```

LinkML løyser relative importer inni `dcat-ap-no-schema` (t.d. `../common/common-ap-no-schema`)
relativt til base-URL-en — det fungerer korrekt med GitHub Raw.

**Kva som krevst i dette repoet:**
- Semantiske versjon-taggar (`v1.0.0`, `v1.1.0` osv.) — sjå Ulempe 2.

---

### Ulempe 2 – Container-imagene må publiserast og vedlikehaldast

**Rot-årsak:** `ensure-images`-jobben i `generate.yml` pushar allereie imagene til GHCR, men med
content-hash-taggar. Desse er ikkje brukarvennlege frå eksterne repo.

**Løysing: Release-workflow med semantisk versjonering**

`release.yml` (allereie implementert) re-taggar eksisterande GHCR-imagene på kvar `v*.*.*`-tagg:

```
ghcr.io/brreg/linkml-local:v1.0.0          ← pinned
ghcr.io/brreg/linkml-local:latest          ← alltid siste release
ghcr.io/brreg/mcp-linkml-validator:v1.0.0
ghcr.io/brreg/mcp-linkml-generator:v1.0.0
```

**Vedlikehald:** Imagene må merkast som `public` i GitHub Packages-innstillingane slik at
`podman pull` fungerer utan innlogging frå eksterne repo.

---

### Ulempe 3 – Nettverkstilgang under generering

**Ikkje eit reelt problem i dette oppsettet.**

Reusable workflows køyrer på GitHub Actions-runnerar som alltid har nettverkstilgang. LinkML
hentar URL-baserte importer under køyring — det fungerer utan ekstra oppsett.

For lokal utvikling er nettverkstilgang tilgjengeleg i alle praktiske tilfelle. Utviklaren
køyrer generering via `podman run` med det publiserte imaget:

```bash
podman run --rm -v "$(pwd):/work" -w /work \
  ghcr.io/brreg/linkml-local:v1.0.0 \
  gen-jsonschema src/linkml/mitt-domene/min-modell/min-modell-schema.yaml
```

---

### Ulempe 4 – Risiko for versjonsdrift

**Rot-årsak:** Ein domenemodell som vert sjeldan oppdatert kan sakke etter og importere ein
AP-NO-versjon som er utdatert eller inkompatibel.

**Løysing A: Versjonsfil `linkml-datamodellering.yaml`**

Ei lita YAML-fil i rota av det eksterne repoet pinnar AP-NO-versjonen eksplisitt:

```yaml
# linkml-datamodellering.yaml
ap-no-version: v1.0.0
```

Den reusable workflowen les denne fila og brukar rett image-versjon og rett URL for AP-NO-importer.
Alle som klonar repoet brukar automatisk same versjon.

**Løysing B: Automatiske oppgraderingsvarslar med Renovate**

`renovate.json` i det eksterne repoet ser etter nye GitHub-releasar frå dette repoet:

```json
{
  "customManagers": [{
    "customType": "regex",
    "fileMatch": ["^linkml-datamodellering\\.yaml$"],
    "matchStrings": ["ap-no-version: (?<currentValue>[^\\n]+)"],
    "depNameTemplate": "brreg/linkml-datamodellering-no",
    "datasourceTemplate": "github-releases"
  }]
}
```

Renovate opnar automatisk ein PR kvar gong det kjem ein ny release her. Teamet bestemmer
sjølv når dei vil oppgradere.

**Løysing C: Semantisk versjonering av dette repoet**

- **PATCH** (`v1.0.1`): Feilrettingar som ikkje påverkar eksisterande skjema.
- **MINOR** (`v1.1.0`): Nye slots/klasser. Bakover-kompatibelt — eksisterande importerande skjema fungerer utan endring.
- **MAJOR** (`v2.0.0`): Brot-endring — slot eller klasse fjerna/omdøypt. Krev oppdatering i importerande skjema.

`CHANGELOG.md` dokumenterer brot-endringar eksplisitt.

---

### Ulempe 5 – Meir oppsett for ny utviklar

**Rot-årsak:** Utviklaren jobbar i eit eksisterande repo. Komplekse workflow-filer eller
Makefile-malar er vanskelege å leggje til utan å forstyrre eksisterande oppsett.

**Løysing: Reusable workflows + minimalt fotavtrykk**

Det eksterne repoet treng berre **to filer**:

**1. `linkml-datamodellering.yaml`** (versjonsfil, 2 linjer):
```yaml
ap-no-version: v1.0.0
```

**2. `.github/workflows/linkml.yml`** (kallefil, ~10 linjer):
```yaml
name: LinkML
on: [push, pull_request]
jobs:
  validate:
    uses: brreg/linkml-datamodellering-no/.github/workflows/reusable-validate.yml@v1.0.0
    with:
      schema: src/linkml/mitt-domene/min-modell/min-modell-schema.yaml
      policy: bronze
```

All kompleks logikk (image-pulling, validering, generering, artefakt-publisering) bur i dei
reusable workflowene i dette repoet. Eksisterande `Makefile`, `src/`-struktur og CI-oppsett
i det eksterne repoet rørast ikkje.

**Bootstrap: legg til i eksisterande repo på eitt minutt**

```bash
curl -sSL https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/v1.0.0/scripts/bootstrap.sh | bash
```

`bootstrap.sh` skriv dei to filene med rett versjon fylt inn og skriv ut neste steg.

---

## Samla bilete av Alternativ B

```
dette repoet (brreg/linkml-datamodellering-no)
│
├── src/linkml/ap-no/**                        ← tilgjengeleg via GitHub Raw + versjon-tag
├── ghcr.io/brreg/linkml-local:v1.0.0          ← publisert via release-workflow
├── .github/workflows/reusable-validate.yml    ← kallbar frå alle repo
├── .github/workflows/reusable-generate.yml    ← kallbar frå alle repo
└── scripts/bootstrap.sh                       ← legg til støtte i eksisterande repo
        │
        ▼ (bootstrap.sh — to filer)
eksternt repo (t.d. kommune/mitt-fagsystem)
├── linkml-datamodellering.yaml     ← pinnar v1.0.0
├── src/linkml/mitt-domene/         ← eige skjema (URL-import av AP-NO)
└── .github/workflows/
    └── linkml.yml                  ← 10-linja kallefil
```

---

## Kva som må gjerast for å aktivere Alternativ B

| # | Tiltak | Status | Kompleksitet |
|---|---|---|---|
| 1 | Semantisk versjonering — `v1.0.0`-tag oppretta | ✅ Gjort | — |
| 2 | `release.yml` re-taggar GHCR-imagene | ✅ Gjort | — |
| 3 | GHCR-imagene merkast som `public` | ⏳ Krev org-admin | Minimal |
| 4 | `reusable-validate.yml`, `reusable-generate.yml` og `scripts/bootstrap.sh` | ○ Ikkje starta | Medium |
| 5 | Dokumenter schema-URL-ar og bootstrap-prosessen i README/docs | ○ Ikkje starta | Låg |
| 6 | `scripts/renovate.json`-mal | ○ Ikkje starta | Låg |

Tiltak 3 og 4 er dei gjenverande kritiske stega.
