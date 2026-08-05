# Plan: Rett Dependabot pip-konfig for mcp-linkml-*

**Kortnamn:** `rett-dependabot-pip-konfig`
**Dato:** 2026-08-05

---

## Bakgrunn

Dependabot-jobben for `mcp-linkml-modell-utkast` feilar med:

```
ERROR Error during file fetching; aborting: No files found in /src/mcp-linkml-modell-utkast
```

Årsak: `.github/dependabot.yml` har `package-ecosystem: pip`-oppføringar for
`/src/mcp-linkml-validator` og `/src/mcp-linkml-modell-utkast`. Ingen av desse
katalogane inneheld ein `requirements.txt`/`pyproject.toml`/`Pipfile` —
Python-avhengigheitene deira (`linkml`, `linkml-runtime`, `pyyaml`, `pytest`)
er i staden pinna direkte i `pip install`-linjer i den delte
`src/assets/containers/Dockerfile.mcp-linkml`. Dependabot sin pip-skannar
finn dermed ingen manifestfil å lese, og jobben feilar heilt (0 kjørte
oppdateringar).

`package-ecosystem: docker` sporar `FROM`-taggar i Dockerfile (t.d.
`python:3.11-alpine`), men **ikkje** versjonspinningar inni `RUN pip install`-
linjer. Å leggje til ein docker-oppføring gjev difor berre delvis dekning
(base-image), men er framleis nyttig sidan base-image i dag ikkje er sporra
av Dependabot i det heile.

**Val (avklart med brukar):** Gjer begge deler —
1. Fjern dei to feilkonfigurerte pip-oppføringane
2. Legg til ei ny `docker`-oppføring for `/src/assets/containers`

## Steg

1. Fjern `pip`-oppføringane for `/src/mcp-linkml-validator` og
   `/src/mcp-linkml-modell-utkast` frå `.github/dependabot.yml`
2. Legg til `package-ecosystem: docker`, `directory: /src/assets/containers`
   med same schedule/limit-mønster som resten av fila
3. Køyr actionlint (dependabot.yml er ikkje ein workflow-fil, så dette steget
   gjeld ikkje — verifiser i staden med ein enkel YAML-syntakssjekk)
4. Oppdater denne specen med "Utført"-seksjon og generer commit-melding

## Handlingsliste

- [x] `.github/dependabot.yml`: fjern dei to pip-oppføringane
- [x] `.github/dependabot.yml`: legg til docker-oppføring for `/src/assets/containers`
- [x] Verifiser YAML-syntaks

## Utført

Fjerna dei to feilkonfigurerte `pip`-oppføringane (peika på katalogar utan
requirements.txt/pyproject.toml) og erstatta med éi `docker`-oppføring for
`/src/assets/containers`, som no sporar `FROM python:3.11-alpine`-taggen i
dei delte Dockerfile-ane. YAML-syntaks verifisert med `yaml.safe_load`.
