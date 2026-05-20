# Klargjering for public GitHub-repository

## Vurdering

Repoet inneheld inga hardkoda nøklar, passord eller ekte persondata. Eksempeldata brukar syntetiske namn og `example.no`-domene. Workflow-permissions er fornuftig avgrensa. Hovudproblemma er av typen "gløymt lokal konfig", mangel på lisens og upinna avhengigheiter.

---

## Tiltak i prioritert rekkefølge

### 1. Gjer `.mcp.json` portabel med dynamisk repo-rot

**Problem:** `.mcp.json` inneheld absolutte lokale stiar (`/mnt/c/dev/github/linkml-w3c-no-profiles/...`) som er maskin-spesifikke for utviklaren og ikkje fungerer for andre.

**Løysing:** Bytt `command` frå `podman` til `bash -c` og la skallet finne repo-rota dynamisk med `git rev-parse --show-toplevel`. Krev null konfigurasjon frå brukaren og fungerer uansett kor repoet er sjekka ut.

```json
{
  "mcpServers": {
    "linkml-generator": {
      "command": "bash",
      "args": [
        "-c",
        "REPO=$(git rev-parse --show-toplevel) && podman run -i --rm -v \"$REPO/src/...\" mcp-linkml-generator"
      ]
    }
  }
}
```

**Status:** Implementert — `.mcp.json` er no trygg å committe.

---

### 2. Legg til LICENSE-fil

**Problem:** Eit repository utan lisens er ikkje open kjeldekode i juridisk forstand. Andre kan sjå koden, men har ikkje lov til å bruke, kopiere eller distribuere han.

**Tilråding:** For norske offentlege data og API-spesifikasjonar er **NLOD 2.0** (Norsk lisens for offentlege data) vanleg og anbefalt av Digitaliseringsdirektoratet. For rein programvare er **Apache 2.0** eit godt val som òg vern patentrettar.

Lag fila `LICENSE` i rota av repoet med passande innhald. GitHub tilbyr lisensveiviser i UI-et.

---

### 3. Pin container image-tagg i Dockerfile.linkml

**Problem:** `Dockerfile.linkml` brukar `FROM docker.io/linkml/linkml:latest`. `latest`-taggen endrar seg ved kvar ny release oppstraums — dette kan bryte CI uforutsigbart og er eit potensielt supply chain-problem.

```dockerfile
# Noverande (ustabilt):
FROM docker.io/linkml/linkml:latest

# Bør vere (stabilt):
FROM docker.io/linkml/linkml:1.8.6
```

**Framgangsmåte:**
1. Finn gjeldande stabil versjon: `podman pull docker.io/linkml/linkml:latest && podman inspect docker.io/linkml/linkml:latest | grep -i version`
2. Pin til den konkrete tag-en
3. Oppdater manuelt ved behov (Dependabot støttar Docker-avhengigheiter)

**Biverknad:** Eliminnerer òg det at noverande CI alltid rebuildar imaget sjølv om ingenting er endra — med ein fast tag kan ein køyre `podman pull` og samanlikne digest.

---

### 4. Legg til SECURITY.md med ansvarleg varslingsprosess

**Problem:** Eit public repo bør ha ein tydeleg politikk for korleis sikkerheitssårbarheiter skal rapporterast. Utan dette veit ikkje externe bidragsytarar om dei skal opne ein public issue (uheldig for sårbarheiter) eller kontakte direkte.

GitHub viser automatisk `SECURITY.md` ved forsøk på å opne ein issue.

**Minimumsinnhald:**
```markdown
# Sikkerheit

For å rapportere ein sikkerheitssårbarheit, ikkje bruk public GitHub Issues.
Send e-post til [din e-post] med beskriving av problemet.
Vi svarer innan 5 arbeidsdagar.
```

---

### 5. Suppler `.gitignore` og pin pip-avhengigheiter

**Problem A — .gitignore:** Noverande `.gitignore` dekkjer genererte artefaktar og Python cache, men manglar:
- `.mcp.json` (jf. Tiltak 1)
- `.env` og `.env.*` (førebygging av framtidige lekkasjar)
- `.DS_Store` og IDE-mapper (`.vscode/`, `.idea/`)

```gitignore
# Legg til:
.mcp.json
.env
.env.*
.DS_Store
.vscode/
.idea/
```

**Problem B — krav utan versjon:** `requirements.txt`-filene i `src/mcp-linkml-validator/`, `src/mcp-linkml-generator/` og `src/assets/containers/` har upinna avhengigheiter:
```
linkml          # → kva versjon?
linkml-runtime  # → kva versjon?
pytest          # → kva versjon?
```

Upinna avhengigheiter gjer at nye installasjonar kan få inkompatible versjonar. Legg til minsteversjonar:
```
linkml>=1.8.0,<2.0.0
linkml-runtime>=1.8.0,<2.0.0
pytest>=8.0.0
```

---

## Oppsummering

| Prioritet | Tiltak | Innsats | Risiko utan tiltak |
|-----------|--------|---------|-------------------|
| 1 | Ignorer `.mcp.json` + fjern frå historikk | Lav | Avslører lokal infra |
| 2 | Legg til LICENSE | Svært lav | Juridisk uklar status |
| 3 | Pin `linkml:latest` i Dockerfile | Lav | Ustabilt CI / supply chain |
| 4 | Legg til SECURITY.md | Svært lav | Ingen varslingsprosess |
| 5 | Utvid `.gitignore` + pin pip-krav | Lav | Framtidige lekkasjar / ustabilt |
