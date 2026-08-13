# Fiks include-component-in-tag-inversjon i release-please

## Bakgrunn

`release-please` abortar kvar køyring med «There are untagged, merged release
PRs outstanding — aborting», og har gjort det sidan PR #50 vart merga
2026-08-02.

Rotårsak: `.github/release-please-config.json` har
`"include-component-in-tag": false`. Denne verdien er inverterte i høve til
det opphavlege spec-et (`specs/done/release-please-scope-mapping.md`) sitt
uttrykte mål — dei ønskte tag-format `<schema>-v<version>`, men i
release-please gir `false` faktisk berre bart `v<version>` (utan
komponentnamn), medan `true` gir `<component>-v<version>`.

Konsekvens:
- release-please søkjer etter tagnamn som `v1.10.0`, `v1.6.0` — men dei
  faktiske git-tagane (oppretta av «Opprett per-schema git-tags»-steget i
  `release-please.yml`) heiter `cpsv-ap-no-v1.10.0`, `ngr-adresse-v1.6.0` osv.
- release-please finn difor 0 av 22 forventa releases kvar gong, og trur
  PR #50 aldri vart fullstendig tagga → permanent abort.
- Med bart `v<version>`-format ville release-please i tillegg prøvd å
  oppretta kolliderande tagar for pakkar som deler versjonsnummer (5 pakkar
  på 1.6.0, 5 pakkar på 4.5.0 i dag).

Sekundært avvik oppdaga under feilsøking: `cpsv-ap-no` sin faktiske
git-tag/release er `cpsv-ap-no-v1.10.1` (frå commit `da84ce8`, som aldri nådde
`main` — eit orphan-forsøk på å omgå immutable-releases-blokkering av det
tidlegare `1.10.0`-tagnamnet), medan `main` sitt manifest og schema framleis
seier `1.10.0`.

## Steg

1. Sett `include-component-in-tag: true` i `.github/release-please-config.json`
2. Oppdater `.github/release-please-manifest.json`: `cpsv-ap-no` frå `1.10.0`
   til `1.10.1` (samkøyr med faktisk publisert tag/release)
3. Oppdater `version`-feltet i
   `src/linkml/ap-no/cpsv-ap-no/cpsv-ap-no-schema.yaml` frå `"1.10.0"` til
   `"1.10.1"` (same grunngjeving)
4. Verifiser JSON-syntaks på begge endra filer

## Handlingsliste

- [x] Steg 1: `include-component-in-tag: true`
- [x] Steg 2: manifest `cpsv-ap-no` → `1.10.1`
- [x] Steg 3: schema `version` → `"1.10.1"`
- [x] Steg 4: JSON-syntaksverifisering

## Utført

Alle fire steg utført og verifisert (`jq` validerer begge JSON-filene).
Neste `release-please`-køyring bør no finna dei 21 eksisterande
komponent-prefikserte tagane (`<component>-v<version>`) og slutta å
abortera på PR #50.
