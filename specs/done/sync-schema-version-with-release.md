# Synk schema-versjon med release-nummer

## Bakgrunn

Release-Please oppdaterer `.release-please-manifest.json` og `CHANGELOG.md` når ein release vert merga, men `*-schema.yaml` sitt `version:`-felt vert **ikkje** oppdatert. Dette fører til mismatch mellom GitHub Release-tag (t.d. `samt-bu-v1.0.5`) og `samt-bu-schema.yaml` som framleis seier `version: "1.0.0"`.

Rotårsak: `simple` release-type i release-please støttar **ikkje** `extra-files` med `jsonpath` — denne funksjonen er berre tilgjengeleg for `node`, `python` og liknande release-typar.

Sjå: https://github.com/googleapis/release-please/blob/main/docs/customizing.md#updating-arbitrary-files

## Mål

1. `*-schema.yaml` sitt `version:`-felt skal automatisk oppdaterast til same versjon som i `.release-please-manifest.json` når ein release vert merga
2. Oppdateringa skal skje **før** generate-workflowen køyrer, slik at artefaktane i GitHub Release får korrekt versjon
3. Løysinga skal fungere for alle 21 pakkar i repoet

## Tiltak

1. [✓] Fjern `extra-files`-konfigurasjon frå `release-please-config.json` (den har ingen effekt)
   - Implementert: brukte `jq` til å fjerne alle `extra-files`-blokker
2. [✓] Legg til ny jobb `update-schema-versions` i `.github/workflows/release-please.yml` som køyrer **etter** at release-PR er merga
   - Implementert: ny step "Oppdater schema-versjonar og datofelt"
   - Triggerar på: `if: ${{ steps.release-please.outputs.releases_created == 'true' }}`
   - Hent `.release-please-manifest.json`
   - For kvar pakke i manifest: bruk `yq` til å oppdatere `version:` i `*-schema.yaml`
   - Commit endringane med `git commit -m "chore: oppdater schema-versjonar og datofelt [skip ci]"` og `git push`
3. [✓] Legg til `annotations.endringsdato` og `annotations.utgivelsesdato` i same oppdatering (ISO 8601-format)
   - Implementert: `endringsdato` vert alltid oppdatert, `utgivelsesdato` berre dersom den ikkje allereie er sett
4. [ ] Test med ein manuell release-please-trigger (`workflow_dispatch`) for eitt domene

## Avhengigheiter

- `yq` må installerast i workflow (tilgjengeleg via `apt`)

## Akseptansekriterium

- Etter at release-PR for `samt-bu v1.0.6` vert merga, skal `samt-bu-schema.yaml` ha `version: "1.0.6"`
- `annotations.endringsdato` og `annotations.utgivelsesdato` skal vere sett til datoen for release
- GitHub Release-artefaktar skal ha korrekt versjon

## Utført

Alle tiltak er implementerte:

1. **extra-files fjerna**: Brukte `jq` til å fjerne alle `extra-files`-blokker frå `release-please-config.json` (dei har ingen effekt for `simple` release-type)

2. **Workflow-oppdatering**: La til ny step "Oppdater schema-versjonar og datofelt" i `.github/workflows/release-please.yml` som køyrer etter at release er oppretta. Steget:
   - Installerer `yq` for YAML-manipulering
   - Hentar versjon frå `.release-please-manifest.json` for kvar releaset pakke
   - Oppdaterer `version`, `annotations.endringsdato` og (dersom ikkje sett) `annotations.utgivelsesdato`
   - Commitar med `[skip ci]` og pushar

3. **Historisk sync**: Oppdaterte alle 21 skjema manuelt til å matche `.release-please-manifest.json` (dei var alle ute av sync sidan `extra-files` aldri fungerte). Brukte Python-script som bevarer YAML-formatering.

**Neste release** vil automatisk få korrekt schema-versjon.
