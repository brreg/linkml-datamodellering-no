# Bytt separate-pull-requests til false i release-please

## Bakgrunn

Under feilsøkinga dokumentert i `specs/done/fiks-release-please-multi-pr-bug.md`
vart det klart at `separate-pull-requests: true` (innført i commit `0dd152ab`,
sjå `specs/done/release-please-scope-mapping.md`) gjer at release-please lagar
éin release-PR **per komponent** (22 stk. ved siste køyring, #61–#82) i staden
for éin kombinert PR for heile monorepoet.

Dette har reell driftskostnad:
- 22 PR-ar å følgje opp, godkjenne og la auto-merge handtere per release-runde,
  i staden for éin
- Fleire samstundes opne PR-ar aukar overflata for race-tilstandar
  (jf. den forbigåande «Pull Request is not mergeable»-feilen på PR #62)
- Workflow-koden må løkke over `outputs.prs` (fleirtal) i staden for å lese
  eit enkelt `outputs.pr` — meir kompleksitet å halde ved like

Motsvarande fordel med `true` (per-komponent-uavhengigheit — éin pakke med
raude sjekkar blokkerer ikkje at andre pakkar sine releasar går gjennom) har
i praksis ikkje vore verdt kostnaden, gitt at feilsøkinga i dag var direkte
forårsaka av multi-PR-kompleksiteten.

**Git-tags/GitHub Releases er upåverka av denne innstillinga** — dei er
framleis éin per komponent (styrt av `component:`/`packages:`), uavhengig av
om PR-en som utløyste dei var kombinert eller separat.

## Steg

1. **Vent til dei 22 opne PR-ane (#61–#82) er avgjort** — merga eller lukka.
   Å byte denne innstillinga medan PR-ar frå det gamle regimet står i
   flight risikerer at release-please ikkje klarer å forsone dei mot ny
   PR-grupperingslogikk ved neste køyring.
2. Sett `separate-pull-requests: false` (eller fjern nøkkelen — same som
   standardverdien) i `.github/release-please-config.json`
3. Verifiser JSON-syntaks
4. Trigger release-please (push eller `workflow_dispatch`) og stadfest at
   han no lagar **éin** kombinert PR med tittel i stil `chore: release main`
   for alle pakkar med utståande endringar
5. Stadfest at «Oppdater schema-versjonar i release-PR»- og
   «Informer om release-PR og aktiver auto-merge»-stega (no løkkande over
   `outputs.prs`) framleis fungerer korrekt med berre éin PR i arrayen —
   koden frå `fiks-release-please-multi-pr-bug.md` treng **ikkje** endrast
   tilbake, han handterer begge tilfelle

## Handlingsliste

- [x] Steg 1: dei 22 PR-ane er avgjort — alle 22 (#61–#82) merga 2026-08-14, ingen opne PR-ar attståande
- [x] Steg 2: separate-pull-requests sett til false
- [x] Steg 3: JSON-syntaks verifisert
- [ ] Steg 4: release-please trigga og stadfesta éin kombinert PR
- [ ] Steg 5: dei to løkke-stega stadfesta framleis korrekte med éin PR
