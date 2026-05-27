# Verifisering av .github/workflows/

## Resultat

Seks workflowfiler er gjennomgått. Fem er utan funn:

| Fil | Status |
|---|---|
| `generate.yml` | OK — domainmatrise, stiar og `manifest.yaml`-bruk er korrekt |
| `validate.yml` | OK — domainmatrise korrekt (`begrepskatalog`, `modellkatalog`) |
| `reusable-generate.yml` | OK — brukar `manifest.yaml` gjennomgåande |
| `reusable-validate.yml` | OK |
| `release.yml` | OK — har jobb for alle fire image (`linkml-local`, `mcp-linkml-validator`, `mcp-linkml-modell-utkast`, `mcp-linkml-begrep-utkast`) |

---

## Funn

### 1. `trivy.yml` — manglar skanning av `mcp-linkml-begrep-utkast/requirements.txt`

`scan-requirements`-jobben skannar tre filer for CVE-ar:

```yaml
src/mcp-linkml-validator/requirements.txt
src/mcp-linkml-modell-utkast/requirements.txt
src/assets/containers/requirements-python-test.txt
```

`src/mcp-linkml-begrep-utkast/requirements.txt` eksisterer men er ikkje med.
Alle tre MCP-containerane byggjer på Python-avhengigheiter — manglande skanning
betyr at CVE-ar i begrep-utkast ikkje vert rapporterte til GitHub Security.

---

## Tiltaksliste

| # | Fil | Endring | Prioritet |
|---|---|---|---|
| 1 | `trivy.yml` | Legg til skanning av `src/mcp-linkml-begrep-utkast/requirements.txt` | Medium |
