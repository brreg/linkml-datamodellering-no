# Plan: Integrasjon mot GCP Data Catalog

## Avvist

**Avvist 2026-06-10.** Integrasjonslogikk mot GCP Data Catalog høyrer heime i konsumentens eige repo — ikkje her. Dette repoet har ansvar for å modellere og publisere artefaktar; orchestrering av registrering i ein ekstern datakatalog er ein operasjonell oppgåve som er tett knytt til konsumentens GCP-miljø, infrastruktur og tilgangsstyring.

Å plassere scriptet her ville dessutan trekkje inn GCP-avhengigheiter (`google-cloud-datacatalog`) og testoppsett som ikkje høyrer heime i eit modelleringsrepo. Konsumenten bør heller referere til `catalog.json` frå GitHub Pages og implementere registreringslogikken i sin eigen integrasjonspipeline.

---

## Bakgrunn

GCP Data Catalog (no ein del av Dataplex Universal Catalog) er ein fullt forvalta
metadatakatalogtjeneste i Google Cloud. Integrasjonen gjer det mogleg for verksemder
som bruker GCP å registrere LinkML-skjema frå dette repoet som søkbare og tagga
oppslag i sin eigen GCP-katalog, med lenke attende til dokumentasjonsportalen.

---

## Arkitekturprinsipp: pull, ikkje push

Dette repoet pusher aldri artefaktar til eksterne kjelder (sjå `CLAUDE.md`).
GCP Data Catalog er eit push-API: konsumenten kallar APIet for å registrere
oppslag. **Løysinga er at koden lever i dette repoet, men køyrer i
konsumentens eige GCP-miljø** — ikkje i CI-pipeline-en her.

```
Dette repoet           Konsumenten sitt GCP-miljø
───────────────────    ─────────────────────────────────────────────────
GitHub Pages      ──pull──→  register-gcp-catalog.py (skript frå dette repoet)
(openapi.yaml,                     │
 schema.json,                      ▼
 schema.ttl,              GCP Data Catalog API
 catalog.json)                  (push frå konsumentens script)
```

Konsumenten kloner eller boostrapper dette repoet og køyrer scriptet sjølv,
med sine eigne GCP-credentials. Alternativt kan scriptet køyrast som ein
Cloud Function eller Cloud Run Job i konsumentens infrastruktur.

---

## Teknisk tilnærming

### GCP Data Catalog-konsept

| GCP-konsept | Bruk |
|---|---|
| **Entry Group** | Éin per domene — t.d. `fint`, `samt`, `ngr`, `ap-no` |
| **Entry** | Éin per LinkML-skjema — representerer skjemaet som ein ressurs |
| **Tag Template** | Felles mal for LinkML-spesifikke metadata — oppretta éin gong |
| **Tag** | Instans av tag template per entry — version, policy, publisher, status |

### Mapping: LinkML-skjema → Data Catalog Entry

| LinkML-felt | Data Catalog-felt |
|---|---|
| `name` | `entry_id` (innanfor entry group) |
| `title` | `display_name` |
| `description` | `description` |
| Dokumentasjons-URL på GitHub Pages | `linked_resource` |
| `schema`-klasser → flata feltliste | `schema.columns` (valfri) |

### Tag Template: `linkml_schema_metadata`

| Feltnavn | Type | Kjelder |
|---|---|---|
| `version` | string | `version:` i YAML-skjemaet |
| `data_policy` | enum | `manifest.yaml` (`bronze`/`silver`/`gold`/…) |
| `publisher` | string | `annotations.utgiver` |
| `status` | string | `annotations.status` (ADMS-URI → lesbar label) |
| `endringsdato` | timestamp | `annotations.endringsdato` |
| `schema_url` | string | URL til `*-schema.yaml` på `raw.githubusercontent.com` |
| `openapi_url` | string | URL til `*-openapi.yaml` på GitHub Pages (viss `openapi: true`) |

### Catalog manifest

For å unngå at scriptet må klone heile repoet, publiserer CI eit maskinlesbart
`catalog.json` til GitHub Pages med metadata om alle skjema. Scriptet les dette
fila og registrerer alle skjema i GCP Data Catalog.

```json
{
  "generated": "2026-06-10T12:00:00Z",
  "base_url": "https://brreg.github.io/linkml-datamodellering-no",
  "schemas": [
    {
      "name": "samt-bu",
      "domain": "samt",
      "title": "SAMT – Skular og barnehagar",
      "version": "1.0.0",
      "data_policy": "silver",
      "publisher": "https://data.norge.no/organizations/974760673",
      "status": "Completed",
      "endringsdato": "2026-06-10",
      "docs_url": "https://brreg.github.io/linkml-datamodellering-no/samt/samt-bu/",
      "schema_yaml_url": "https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/main/src/linkml/samt/samt-bu/samt-bu-schema.yaml",
      "artifacts": {
        "openapi": "https://brreg.github.io/linkml-datamodellering-no/samt/samt-bu/samt-bu-openapi.yaml",
        "json_schema": "...",
        "shacl": "..."
      }
    }
  ]
}
```

---

## Opne spørsmål

| # | Spørsmål | Alternativ |
|---|---|---|
| 1 | **GCP-prosjekt og entry group** | ✓ **Avklart:** éin entry group per domene (`fint`, `samt`, `ngr`, `ap-no` osb.). Scriptet oppretter entry groups automatisk basert på domenenamnet frå `catalog.json`. |
| 2 | **Autentisering i scriptet** | (a) Application Default Credentials (`gcloud auth`). (b) Service account JSON-nøkkel via miljøvariabel. |
| 3 | **Tag Template-eigarskap** | (a) Scriptet oppretter tag template automatisk viss ho ikkje finst. (b) Konsumenten oppretter manuelt frå medfølgjande Terraform-modul. |
| 4 | **Skjema-seleksjon** | (a) Alle skjema i `catalog.json`. (b) Berre skjema med `publish_external: true`. (c) Konfigurerbart via CLI-argument. |
| 5 | **Catalog manifest-format** | (a) Nytt `catalog.json` generert av CI. (b) Bruk eksisterande `modelldcat-ap-no` RDF-data frå portalen direkte. |

---

## Steg 1 — Definer catalog manifest-format og generer `catalog.json`

Legg til eit nytt CI-steg i `generate.yml` (eller `publish`) som samlar
metadata frå alle `manifest.yaml` + YAML-skjema og skriv `catalog.json`
til `mkdocs/docs/catalog.json` slik at han vert publisert til GitHub Pages.

Fil: `src/assets/scripts/gen-catalog-manifest.py`

---

## Steg 2 — Skriv `register-gcp-catalog.py`

`src/assets/scripts/register-gcp-catalog.py` — Python 3.12, køyrer i
`python-pytest`-container eller direkte i konsumentens miljø.

Avhengigheiter: `google-cloud-datacatalog` (legg til i eiga
`requirements-gcp.txt` — ikkje `requirements-python-test.txt`).

Argumentar:
```
register-gcp-catalog.py
  --catalog-url <url til catalog.json på GitHub Pages>
  --project <gcp-project-id>
  --location <region, t.d. europe-north1>
  [--filter-policy silver,gold]
  [--dry-run]
```

Scriptet:
1. Hentar `catalog.json` frå `--catalog-url`
2. Oppretter entry group og tag template viss dei ikkje finst
3. For kvart skjema som passar filteret:
   - Oppretter eller oppdaterer Data Catalog Entry
   - Set eller oppdaterer Tag med LinkML-metadata

---

## Steg 3 — Test manuelt mot lokal GCP-emulator

`google-cloud-datacatalog` støttar `DATACATALOG_EMULATOR_HOST`.
Dokumenter test-prosedyre mot emulatoren.

---

## Steg 4 — Dokumenter integrasjonen i portalen

Ny side `mkdocs/docs/gcp-data-catalog.md` med:
- Krav (GCP-prosjekt, `gcloud` CLI, ADC-oppsett)
- Steg-for-steg-rettleiing
- Døme på `register-gcp-catalog.py`-kommando
- Forklaring av tag template-feltane

---

## Steg 5 — Valfri: Terraform-modul for tag template

`src/assets/terraform/gcp-data-catalog/` — modul som oppretter
tag template og entry group. Gjer det enklare å integrere i
konsumentens eige Terraform-oppsett.

---

## Prioritert handlingsliste

| # | Steg | Fil | Avhengigheit |
|---|---|---|---|
| 1 | Svar på opne spørsmål 1–5 | — | Brukarval |
| 2 | Definer og generer `catalog.json` | `gen-catalog-manifest.py`, `generate.yml` | Svar på sp. 5 |
| 3 | Skriv `register-gcp-catalog.py` | `src/assets/scripts/` | Steg 2, svar sp. 1–4 |
| 4 | Test mot emulator | — | Steg 3 |
| 5 | Portaldokumentasjon | `mkdocs/docs/gcp-data-catalog.md` | Steg 3 |
| 6 | Terraform-modul (valfri) | `src/assets/terraform/` | Steg 3 |

---

## Avhengigheiter

- `google-cloud-datacatalog` Python-pakke — i separat `requirements-gcp.txt`
- GCP-prosjekt med Data Catalog API aktivert
- Konsumentens eigne GCP-credentials (ADC eller service account)
- `catalog.json` publisert til GitHub Pages (Steg 1)
- Ingen ny container nødvendig for `catalog.json`-generering (køyrer i `python-pytest`)
