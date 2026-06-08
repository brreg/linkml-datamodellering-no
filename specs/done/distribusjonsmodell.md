# Distribusjonsmodell for LinkML-verktøya

## Problemstilling

Ein ny utviklar som vil modellere ein datamodell i LinkML og få genererte artefakter (JSON Schema, RDF, diagram, dokumentasjon) treng i dag å jobbe direkte i dette repoet. Er det den beste modellen, eller finst det betre alternativ?

---

## Noverande situasjon: monorepo

Alle domenemodeller ligg under `src/linkml/<domene>/` i dette repoet. AP-NO-profilene importerast med relative stiar:

```yaml
imports:
  - ../../ap-no/dcat-ap-no/dcat-ap-no-schema
```

Container-imagene (`linkml-local`, `python-pytest`, `mcp-linkml-validator`, `mcp-linkml-generator`) bygges berre lokalt og ligg ikkje i noko container-registry.

---

## Alternativ

### Alternativ A – Monorepo (status quo)

Alle domenemodeller bur i dette repoet. Kvar ny modell kjem inn som ein PR mot `main`.

**Fordelar:**
- Null ekstra oppsett — relative importer fungerer ut av boksen.
- Felles CI/CD og dokumentasjonsportal.
- AP-NO-profilene og verktøya er alltid i sync med kvarandre.
- Éin stad for all modellerings-governance.

**Ulemper:**
- Utviklaren må sende PR til eit repo dei ikkje eig, og vente på godkjenning frå andre.
- Eigenarskap og versjonering av domenemodellen er kopla til dette repoets release-rytme.
- Repoet veks utan naturleg grense — alle domener, alle team, alt på éin stad.
- Dersom ein domenemodell er sensitiv (t.d. ikkje klar for open publisering), er det vanskeleg å halde han privat medan verktøya er her.
- Governance-spørsmål: kven godkjenner PR-ar for kva domener?

**Vurdering:** Eignar seg godt for eit lite, tett team som eig alle modellane. Skalerast dårleg når fleire uavhengige team skal bidra.

---

### Alternativ B – Eige repo med URL-importer

LinkML støttar URL-baserte importer. AP-NO-profilene publiserast med stabile URL-ar (t.d. frå GitHub raw eller ein dedikert schema-server), og domenemodellen importerer dei direkte:

```yaml
imports:
  - https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/main/src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema
```

Container-imagene publiserast til eit registry (t.d. `ghcr.io/brreg/linkml-local`). Makefile-mal og GitHub Actions-workflows tilbyst som ein startpakke (template-repo eller nedlastbart skript).

**Fordelar:**
- Utviklaren eig sitt eige repo og har full kontroll over versjonering og tilgang.
- Uavhengig release-rytme.
- AP-NO-profilene kan versjonerast med git-tag i URL-en (`/refs/tags/v1.2/...`).

**Ulemper:**
- Krev at AP-NO-profilene har stabile, publiserte URL-ar — i dag er dei berre tilgjengelege via relativ stiimport.
- Container-imagene må publiserast og vedlikehaldast i eit registry.
- Nettverkstilgang under generering (LinkML laster importer ved kjøretid).
- Risiko for versjonsdrift: ein domenemodell kan kome ut av sync med AP-NO-profilene.
- Meir oppsett for ny utviklar (hente Makefile-mal, konfigurere registry-tilgang).

**Vurdering:** Det rette langsiktige målet dersom mange uavhengige team skal bruke AP-NO-profilene. Krev ein del infrastrukturinvestering fyrst (registry, stabile URL-ar, versjoneringsrutine).

---

### Alternativ C – Git submodule

Utviklaren oppretter sitt eige repo og legg dette repoet inn som ein git submodul under t.d. `vendor/linkml-datamodellering-no/`. Relative importer fungerer framleis fordi filstrukturen er bevart.

**Fordelar:**
- Relative importer fungerer utan endringar.
- Utviklaren eig eige repo.
- Submodulen kan peike på ein spesifikk commit/tag for reproduserbarheit.

**Ulemper:**
- Git submoduler er kjende for å skape friksjon (gløymer `--recurse-submodules`, vanskeleg å oppdatere, dårleg støtte i mange GUI-verktøy).
- Makefile-variablar (`CURDIR`, volum-mount-stiar) må tilpassast den nye katalogstrukturen.
- Utviklaren dreg med seg heile dette repoet inkludert alt innhald som ikkje er relevant.

**Vurdering:** Teknisk mogleg, men git submoduler er ein kjend kilde til brukarfriksjon. Anbefales ikkje som hovudveg.

---

### Alternativ D – GitHub template-repo

Dette repoet (eller ein destillert versjon) gjerast til eit GitHub template-repo. Ny utviklar klikkar «Use this template» og får sin eigen kopi med heile strukturen. AP-NO-profilene følgjer med som kopierte filer.

**Fordelar:**
- Svært låg starttryning — eitt klikk.
- Utviklaren eig sin instans frå dag éin.
- Ingen nettverksavhengigheit under generering.

**Ulemper:**
- AP-NO-profilene dupliserast inn i kvart repo — ingen automatisk oppdatering når profilene endrast.
- Template-repoet er i prinsippet ein fork utan upstream-kopling.
- Ikkje eigna for modeller som skal importere AP-NO med garanti om at dei er oppdaterte.

**Vurdering:** Eignar seg for rask prototyping eller undervisning, men ikkje for produksjonsmodeller som skal halde seg i sync med AP-NO-profilene.

---

## Samanfatting og tilråding

| | Monorepo (A) | URL-importer (B) | Submodule (C) | Template (D) |
|---|---|---|---|---|
| Eigenarskap | Delt | Eige | Eige | Eige |
| AP-NO alltid oppdatert | Ja | Ja (med pin) | Ja (med pin) | Nei |
| Oppsett-friksjon | Låg | Medium | Høg | Svært låg |
| Krev infrastruktur | Nei | Ja (registry, URL) | Nei | Nei |
| Skalerbarheit | Låg | Høg | Medium | Låg |
| Eigna for produksjon | Ja | Ja | Med atterhald | Nei |

**Tilråding:**

Hald monorepo-modellen (A) for modeller som tilhøyrer dette repoets naturlege domene (AP-NO, FAIR, FINT, NGR, OREG, SAMT). Det gir minimal friksjon og full kontroll.

Invester i alternativ B (URL-importer + publisert container-registry) som eit parallelt spor for eksterne team som vil bruke AP-NO-profilene i sine eigne repo. Dei to trinna er:

1. **Publiser container-imagene** til `ghcr.io/brreg/` via ein GitHub Actions-workflow som bygger og pushar ved kvar release-tag.
2. **Gi AP-NO-profilene stabile URL-ar** — anten via GitHub raw med tag-baserte URL-ar, eller via ein dedikert `id`-basert schema-server.

Eit enkelt Makefile-mal og ein GitHub Actions-workflow-mal (`.github/workflows/linkml-generate.yml`) kan tilbystast i dette repoet under `templates/` som startpakke for eksterne repo.

---

## Konvensjonar for eksternt repo (når alternativ B er på plass)

Dersom ein utviklar vil modellere i sitt eige repo, bør følgjande konvensjonar gjelde:

```
<mitt-repo>/
├── src/linkml/<domene>/<modell>/<modell>-schema.yaml
├── examples/<domene>/<modell>-eksempel.yaml
├── Makefile                  # kopiert/tilpassa frå templates/
└── .github/workflows/
    └── linkml-validate.yml   # kopiert frå templates/
```

- **Importer** peikar på tag-baserte GitHub raw-URL-ar for AP-NO-profilene.
- **Container-imagene** refererast som `ghcr.io/brreg/linkml-local:latest` (eller pinned tag).
- **Validering** køyrast i CI med same policy-nivå (bronze/silver/gold) som her.
- Skjemastrukturen (`src/linkml/<domene>/<modell>/`) følgjer same konvensjon som dette repoet slik at verktøya fungerer utan tilpassing.
