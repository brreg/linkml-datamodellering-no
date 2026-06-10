# Plan: Fiks release-please-feil

## Utført

Utført 2026-06-10. Alle tiltak gjennomførte.

**Kva som vart gjort:**
- `issues: write` lagt til i `permissions:`-blokka i `.github/workflows/release-please.yml` — nødvendig fordi `release-please-action@v5` set alle ulistad scope til `none` når `permissions:` er eksplisitt spesifisert, noko som gav HTTP 401 ved etikettering av release-PR-ar
- `samt-bu` lagt til i `release-please-config.json` og `.release-please-manifest.json` med versjon `1.0.0`
- 22 bootstrap-taggar oppretta lokalt (`cpsv-ap-no-v1.0.0` … `samt-bu-v1.0.0`) — må pushast med `git push origin --tags`

**Avvik frå plan:**
- Bootstrap-tagg for `samt-bu` (tiltak 4) vart oppretta samstundes med dei andre 21 taggane i tiltak 2 — ikkje som eit separat steg
- Verifisering (tiltak 5) avheng av at brukaren pushar taggane og triggar workflowen manuelt

---

## Bakgrunn

`release-please`-workflowen feiler med to uavhengige rotårsaker:

```
⚠ Could not find releases.
⚠ Expected 21 releases, only found 0
...
Error: release-please failed: Requires authentication - https://docs.github.com/rest
```

**Verifisert:** Repository Settings → Actions → General → Workflow permissions er
allereie sett til «Read and write permissions» — det er ikkje årsaka til feilen.

---

### Rotårsak 1 — Manglande `issues: write`-tilgong i job-permissions-blokka

Noverande `release-please.yml` har berre:

```yaml
permissions:
  contents: write
  pull-requests: write
```

`googleapis/release-please-action@v5` kallar GitHub Issues API for å setje
etiketter på release-PR-ar (t.d. `autorelease: pending`). Etiketter på PR-ar
er ein del av Issues API i GitHub — `pull-requests: write` dekkjer ikkje dette.
Utan `issues: write` returnerer GitHub API **HTTP 401** («Requires authentication»),
ikkje 403 («Insufficient permissions»), fordi den eksplisitte `permissions:`-blokka
i jobben effektivt set alle ulistad scope til **none** (ikkje berre read).

Når `permissions:` er eksplisitt spesifisert i ein GitHub Actions-jobb, vert alle
scope som *ikkje* er lista opp sett til `none`. Utan `issues: write` kan jobben
ikkje nå Issues API i det heile — derav 401 i staden for 403.

**Fix:** Legg til `issues: write` i `permissions:`-blokka.

---

### Rotårsak 2 — Manglande bootstrap-taggar

`.release-please-manifest.json` inneheld versjonar for 21 pakkar (t.d.
`dcat-ap-no: 2.0.0`), men ingen tilsvarande git-taggar finst i repoet. Release-please
leitar etter taggar på forma `<component>-v<version>` (t.d. `dcat-ap-no-v2.0.0`)
for å avgjere kva commits som allereie er med i ein release.

Finn det ingen taggar, skannar det alle 500 siste commits og prøver å opprette
release-PR-ar for alle 21 pakkar samstundes — sjølv når rotårsak 1 er løyst.

---

## Steg 1 — Legg til `issues: write` i workflow-permissions ✓

Lagt til `issues: write` i `.github/workflows/release-please.yml`.

**Fil:** `.github/workflows/release-please.yml`

```yaml
    permissions:
      contents: write
      pull-requests: write
      issues: write        # ← nødvendig for PR-etikettar (autorelease: pending)
```

---

## Steg 2 — Bootstrap git-taggar for alle 21 pakkar

Køyr følgjande kommandoar lokalt for å opprette lette taggar som peikar på gjeldande
HEAD. Desse fortel release-please at dei noverande versjonane allereie er «releasede»
og at berre framtidige commits skal genere nye release-PR-ar.

```bash
git tag cpsv-ap-no-v1.0.0
git tag dcat-ap-no-v2.0.0
git tag dqv-ap-no-v1.0.0
git tag modelldcat-ap-no-v1.0.0
git tag skos-ap-no-v2.0.0
git tag brreg-begrepskatalog-v1.0.0
git tag fair-metadata-v1.0.0
git tag fint-administrasjon-v4.0.20
git tag fint-arkiv-v4.0.20
git tag fint-common-v4.0.20
git tag fint-okonomi-v4.0.20
git tag fint-personvern-v4.0.20
git tag fint-ressurs-v4.0.20
git tag fint-utdanning-v4.0.20
git tag brreg-modellkatalog-v1.0.0
git tag referanse-v1.0.0
git tag ngr-adresse-v1.0.0
git tag ngr-eiendom-v1.0.0
git tag ngr-person-v1.0.0
git tag ngr-virksomhet-v1.0.0
git tag register-over-aksjeeiere-v1.0.0

git push origin --tags
```

---

## Steg 3 — Legg til `samt-bu` i release-please-konfigurasjonen ✓

`release-please-config.json` og `.release-please-manifest.json` oppdaterte med `samt-bu` (`1.0.0`).

`samt-bu`-skjemaet manglar i `release-please-config.json` og
`.release-please-manifest.json`. Legg det til samstundes som steg 1 og 2.

**`release-please-config.json`** — legg til i `packages`-objektet:
```json
"src/linkml/samt/samt-bu": {
  "component": "samt-bu",
  "release-type": "simple",
  "extra-files": [
    {
      "type": "yaml",
      "path": "src/linkml/samt/samt-bu/samt-bu-schema.yaml",
      "jsonpath": "$.version"
    }
  ]
}
```

**`.release-please-manifest.json`** — legg til:
```json
"src/linkml/samt/samt-bu": "1.0.0"
```

Bootstrap-tagg etter steg 2: ✓ `samt-bu-v1.0.0` oppretta lokalt saman med dei andre 21 taggane i steg 2.

---

## Steg 4 — Verifiser

Trigge workflowen manuelt via «Run workflow» i GitHub Actions.

Forventa utfall når begge rotårsakene er løyste:
```
✔ Building releases
✔ Building pull requests
ℹ No changes to release
```

(Ingen PR-ar oppretta sidan alle commits er merka som releasede via bootstrap-taggane.)

---

## Prioritert handlingsliste

| # | Steg | Fil | Avhengigheit |
|---|---|---|---|
| 1 | Legg til `issues: write` i workflow | `.github/workflows/release-please.yml` | — |
| 2 | Opprett og push 21 bootstrap-taggar | Git lokalt | — |
| 3 | Legg til `samt-bu` i release-please-config | `release-please-config.json`, `.release-please-manifest.json` | — |
| 4 | Bootstrap-tagg for `samt-bu` | Git lokalt | Steg 3 | ✓ |
| 5 | Verifiser at workflowen passerer | GitHub Actions | Steg 1+2 |

Steg 1, 2 og 3 er uavhengige og kan utførast i kva rekkjefølgje som helst.

---

## Avhengigheiter

- Ingen ekstern infrastruktur — alt kan løysast med endringar i repoet og lokale git-kommandoar
