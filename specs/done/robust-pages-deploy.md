# Gjer GitHub Pages deployment meir robust

## Bakgrunn

GitHub Pages deployment feiler intermittent med "Deployment failed, try again later" under `actions/deploy-pages@v5`-steget. Dette er eit kjent GitHub-infrastrukturproblem som ikkje har med koden vår å gjere.

Feilmeldinga frå siste køyring:
```
Getting Pages deployment status...
Current status: syncing_files
Getting Pages deployment status...
Error: Deployment failed, try again later.
```

## Mål

Gjere `publish`-jobben i `generate.yml` meir robust ved å legge til retry-logikk rundt GitHub Pages deployment.

## Prioritert handlingsliste

1. ✓ **Legg til retry-logikk for deploy-pages**
   - Valde enkel løysing: `continue-on-error: true` på forsøk 1 og 2
   - Tre forsøk totalt: 0 sek → 30 sek → 60 sek pause mellom forsøk
   - Dersom forsøk 1 lukkast, hopp over forsøk 2 og 3
   - Dersom forsøk 2 lukkast, hopp over forsøk 3
   - Dersom forsøk 3 feiler, feiler heile `publish`-jobben

2. **Test løysinga**
   - Commit endringane og push til `main`
   - Sjekk at publish-steget køyrer og lukkast på første eller andre forsøk
   - (Simulering av feil er ikkje mogleg — må vente på naturleg GitHub-feil)

3. **Dokumenter endringane**
   - Oppdater spesifikasjonen med implementeringsdetaljar
   - Generer commit-melding

## Avhengigheiter

Ingen — dette er ein isolert robustheitsforbetring.

## Utført

Implementerte retry-logikk med tre forsøk:

```yaml
- name: Deploy til GitHub Pages (forsøk 1)
  id: deploy-attempt-1
  uses: actions/deploy-pages@v5
  continue-on-error: true

- name: Vent før retry (dersom forsøk 1 feila)
  if: steps.deploy-attempt-1.outcome == 'failure'
  run: sleep 30

- name: Deploy til GitHub Pages (forsøk 2)
  id: deploy-attempt-2
  if: steps.deploy-attempt-1.outcome == 'failure'
  uses: actions/deploy-pages@v5
  continue-on-error: true

- name: Vent før siste retry (dersom forsøk 2 feila)
  if: steps.deploy-attempt-1.outcome == 'failure' && steps.deploy-attempt-2.outcome == 'failure'
  run: sleep 60

- name: Deploy til GitHub Pages (forsøk 3 — siste)
  id: deploy
  if: steps.deploy-attempt-1.outcome == 'failure' && steps.deploy-attempt-2.outcome == 'failure'
  uses: actions/deploy-pages@v5
```

**Oppførsel:**
- Normale køyringar: forsøk 1 lukkast, forsøk 2 og 3 vert hoppa over
- Intermittent feil: forsøk 1 feiler, vent 30 sek, forsøk 2 lukkast
- Vedvarande feil: alle tre forsøk feiler → jobben feiler (som den skal)

## Notater

- Valde `continue-on-error` over `nick-fields/retry@v3` for enkelhets skuld
- `actions/deploy-pages@v5` er siste versjon (per 2026-01)
- Retry-logikk påverkar **ikkje** normale køyringar — stega vert hoppa over med `if`-betingingar
