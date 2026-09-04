---
name: ny-domenemodell
description: Orkestrerer heile flyten for å opprette ein ny LinkML-domenemodell — scaffolding, modellering, validering og spec-avslutning. Bruk når brukaren ber om å opprette/lage/legge til ein ny domenemodell, eit nytt skjema for eit domene, eller ein ny profil under src/linkml/.
---

## Føremål

Denne skillen pakkar saman heile arbeidsflyten for å opprette ein ny
LinkML-domenemodell — frå scaffolding via `make new-modell`, gjennom
modellering, til validering og avslutning etter CLAUDE.md sin standard
spec-arbeidsflyt. Full bakgrunn for kandidaturet: sjå
`specs/done/evaluering-nye-skills-og-rules.md` (flytta frå `backlog/` ved
avslutning).

## Steg

### 1. Avklar parametrar

Spør brukaren (dersom ikkje alt oppgitt i `args`):

- `DOMAIN` — kva domene modellen høyrer til (t.d. `ngr`, `oreg`, `samt`). Sjå
  `src/linkml/` for eksisterande domene, eller avklar om det er eit nytt.
- `NAME` — modellnavn i `kebab-case`.
- Skal skjemaet genererast frå ei eksisterande JSON Schema-fil
  (`JSON_SCHEMA=<sti>`), eller som tomt stub-skjema?
- Følg CLAUDE.md sin arbeidsflyt-regel 1-2 (les tilbake instruksjonen, avklar
  antakelsar) før du går vidare.

### 2. Opprett ein spec

Følg CLAUDE.md sin standard arbeidsflyt: opprett
`specs/backlog/<kortnavn>.md` med bakgrunn, nummererte steg og
handlingsliste for den konkrete modellen — med mindre brukaren eksplisitt
ber om å hoppe over dette.

### 3. Scaffolding

```bash
make new-modell DOMAIN=<domene> NAME=<modell> [JSON_SCHEMA=<sti>]
```

Dette oppretter `src/linkml/<domain>/<modell>/<modell>-schema.yaml`,
`build.yaml` og ei rikt syntetisk eksempelfil. Sjå `COMMANDS.md` § "Ny
modell/begrepskatalog/modellkatalog" for fullstendig flaggreferanse
(`SKIP_EXAMPLE=1` for offline scaffolding utan nettverksavhengig
importoppløysing).

### 4. Modeller skjemaet

Rediger `<modell>-schema.yaml` etter dei modelleringsprinsippa som lastar
automatisk frå `.claude/rules/linkml-schema.md` når du redigerer filer under
`src/linkml/` (slots vs. attributes, lenking framfor inlining,
containerklasse-mønster, Los-tema, navnekonvensjonar, silver-annotasjonar).
For steg-for-steg-rettleiing og importhierarki-val, sjå
`mkdocs/docs/kom-i-gang/ny-domenemodell.md` og
`mkdocs/docs/arkitektur/importhierarki.md`.

### 5. Valider

```bash
make lint SCHEMA=src/linkml/<domain>/<modell>/<modell>-schema.yaml
make roundtrip SCHEMA=src/linkml/<domain>/<modell>/<modell>-schema.yaml
make mcp-linkml-valider-modell SCHEMA=src/linkml/<domain>/<modell>/<modell>-schema.yaml
```

`mcp-linkml-valider-modell` autodetekterer `validation_policy` frå
`build.yaml` (overstyr med `POLICY=<bronze|silver|gold>` ved behov). Rett
eventuelle feil og gjenta til alt er grønt.

### 6. Avslutt

Følg CLAUDE.md sin avslutningsrutine: (a) generer eit kompakt utkast til
commit-melding i conventional commits-format, (b) legg til `## Utført`-seksjon
i specen frå steg 2, (c) flytt specen til `specs/done/`.

## Merknad

Denne skillen erstattar **ikkje** `.claude/rules/linkml-schema.md` — den
rula lastar framleis automatisk så snart du rører filer under `src/linkml/`,
uavhengig av om denne skillen er kalla eksplisitt. Skillen sitt bidrag er
**orkestreringa** av heile flyten, ikkje modelleringsreglane sjølve.
