# Plan: Nedlasting og versjonering av eksterne kodeverk for LinkML-modellering

**Kortnamn:** `ekstern-kodeverk-versjonering`  
**Eksempel:** Los (https://psi.norge.no/los/all.rdf)  
**Dato:** 2026-06-19  
**Revidert:** 2026-06-19 (etter evalueringsrunde — sjå nedanfor)

---

## Bakgrunn

Fleire AP-NO-slot brukar URI-ar frå kontrollerte vokabular som er forvalta eksternt:

| Slot | Vokabular | Eigar |
|------|-----------|-------|
| `dcat:theme` (`tema`) | Los | Digdir |
| `dct:language` (`spraak`) | EuroVoc / EU MDR | EU Publications Office |
| `dct:format` (`format`) | EU MDR Media Types | EU Publications Office |
| `dct:accrualPeriodicity` (`frekvens`) | EU MDR Frequencies | EU Publications Office |
| `adms:status` (`status`) | ADMS Status | W3C |

I dag brukar skjemaa `range: uriorcurie` eller `range: Konsept` for desse slotsa,
utan maskinkontroll av om verdiane faktisk finst i vokabularet.

Målet er å:
1. Laste ned snapshots av eksterne vokabular til repoet
2. Versjonere snapshotsa i git med dato og sjekksum
3. Generere URI-lister og LinkML-enum-typar frå SKOS-data
4. Bruke enumane til **dokumentasjon** (gyldige verdiar i portalen) og som
   opt-in-validering i domenemodeller — **ikkje** i AP-NO-profilene

**Prinsipp:** Pull, ikkje push. Repoet hentar frå eksterne kjelder — aldri omvendt.
All nedlasting skjer i containrar (ingen lokal installasjon).

---

## Kjende avgrensingar (evalueringsnotat 2026-06-19)

### Los har ingen offisiell versjonering

Los er eit levande vokabular — Digdir publiserer ingen versjonsnummer. Ein
SHA256-sjekksum + dato er det einaste vi kan bruke til å identifisere ein snapshot.
Det er umogleg å seie «dette datasettet vart validert mot Los v2.3» — berre
«per 2026-06-19». Dette er ein mangel hos Digdir og kan ikkje løysast i repoet.
`manifest.yaml` skal dokumentere dette eksplisitt.

### Riktig nivå for integrasjon er domenemodellen, ikkje AP-NO

DCAT-AP-NO seier at `dcat:theme` *kan* bruke Los — det er anbefalt, ikkje
obligatorisk. Ein domenemodell for helsesektoren vil gjerne bruke eit
sektorvokabular i tillegg. Los-validering i `dcat-ap-no-schema.yaml` ville
ramme *alle* importerande domenemodeller feil.

**Vedteke val:** Enum-typar og validering er opt-in per domenemodell, ikkje
innbakt i AP-NO-skjemaa.

### SHACL `sh:in` er ikkje standard LinkML-output

LinkML sin SHACL-generator produserer ikkje `sh:in`-lister frå enum-definisjonar
utan tilpassingar. Støtte for dette må verifiserast (EK0) før SHACL-integrasjon
vert planlagt.

### Koplingsrisiko ved import

Viss `LosTema`-enumet inngår i ein importkjede, arvar alle nedstrøms skjema
enumerasjonen. Ei Los-oppdatering kan då vere ei brotendring for alle. Difor
skal enum-typar ligge i eigne, valgfrie schemafiler — ikkje i kjerne-AP-NO-skjemaa.

### Primærverdien er dokumentasjon, ikkje runtime-validering

Den vanlegaste feilen med Los-URI-ar er mangel på kunnskap om at Los *skal*
brukast — ikkje skrivefeil i URI-ar. Den største nytten av EK1–EK3 er å vise
gyldige verdiar i den genererte portalen, ikkje å stoppe instansvalidering.

---

## Arkitektur

### Katalogstruktur

```
src/
  external/
    README.md                  ← oversikt over alle registrerte kjelder
    los/
      manifest.yaml            ← kjelde-URL, nedlasta dato, SHA256-sjekksum
      los.ttl                  ← rå nedlasting (Turtle, ikkje RDF/XML — sjå EK0)

generated/
  external/
    los/
      los-tema.yaml            ← generert liste: berre tema-URI-ar med prefLabel
      los-alle.yaml            ← generert liste: tema + undertema + ord
      los-tema-enum.yaml       ← LinkML-enum: LosTema (importerbar i domenemodeller)
```

**Kva som committast i git:**
- `src/external/` — kjeldedata og manifest ✓ (committast)
- `generated/external/` — byggoutput ✗ (i `.gitignore`, regenererast med `make build`)

### Manifest-format (`src/external/los/manifest.yaml`)

```yaml
name: los
title: Los – Lenka offentlege servicekatalogar
source_url: https://psi.norge.no/los/all.rdf
downloaded: "2026-06-19"
sha256: <sjekksum av los.ttl>
format: turtle
license: https://data.norge.no/nlod/no/2.0
maintainer: https://data.norge.no/organizations/991825827
versioning_note: >-
  Los har ingen offisiell versjonering. SHA256 + nedlastingsdato er einaste
  identifikator for denne snapshoten. Kjelder som refererer til denne snapshoten
  kan ikkje garantere stabilitet over tid.
```

### Generert enum-format (`generated/external/los/los-tema-enum.yaml`)

```yaml
id: https://data.norge.no/external/los-tema
name: los-tema
description: >-
  Gyldige Los-hovudtema (generert frå src/external/los/los.ttl,
  snapshot 2026-06-19). Importerbar opt-in i domenemodeller.

enums:
  LosTema:
    description: Los hovudtema — https://psi.norge.no/los/tema/<namn>
    permissible_values:
      arbeid:
        meaning: https://psi.norge.no/los/tema/arbeid
        description: "Arbeid"
      barn_og_familie:
        meaning: https://psi.norge.no/los/tema/barn-og-familie
        description: "Barn og familie"
      # ... alle ~80 hovudtema
```

Domenemodeller som ynskjer Los-validering importerer denne fila og set
`tema.range: LosTema` i sin eigen `slot_usage`.

---

## Steg

### EK0 — Avklar tilgjengeleg format og SHACL-støtte (forarbeid)

To ting må verifiserast før implementering startar:

**a) Kva format er Los tilgjengeleg i?**
Sjekk om Digdir tilbyr Turtle-nedlasting i tillegg til RDF/XML (`all.rdf`).
Turtle er 3–4× meir kompakt og raskare å parse med rdflib. Viss ikkje Turtle
er tilgjengeleg, konverter med rdflib etter nedlasting og lagre `.ttl`.

**b) Støttar LinkML SHACL-generator `sh:in` frå enum?**
Test om eit skjema med `range: LosTema` (enum) produserer `sh:in`-liste i
generert SHACL. Dersom ikkje: SHACL-integrasjon (opsjonelt steg) krev
manuell SHACL-skriving eller patch i generator — planlegg dette separat.

### EK1 — Opprett katalogstruktur og nedlastingstarget for Los

**Filar:** `src/external/README.md`, `src/external/los/manifest.yaml`, `Makefile`

Last ned `https://psi.norge.no/los/all.rdf` med curl i ein `python:3-slim`-container.
Konverter til Turtle med rdflib om Turtle ikkje er direkte tilgjengeleg.
Rekn ut SHA256. Fyll manifest.yaml.

```makefile
download-external-los:
	mkdir -p src/external/los
	podman run --rm -v "$(PWD):/work" -w /work python:3-slim \
	    sh -c "pip install -q rdflib && python src/external/los/download.py"
```

`download.py` hentar RDF/XML, konverterer til Turtle, skriv `los.ttl` og
oppdaterer `sha256` i `manifest.yaml`.

### EK2 — Lag Python-skript for å trekke ut Los-URI-ar

**Fil:** `src/external/los/extract.py`

Skriptet les `src/external/los/los.ttl` med rdflib, finn alle `skos:Concept`-ar,
og skriv to YAML-filer til `generated/external/los/`:

- `los-tema.yaml` — URI-ar der stien inneheld `/los/tema/`
- `los-alle.yaml` — alle URI-ar (tema + undertema + ord + hendelse)

Kvar oppføring inneheld `uri` og `label_nb` (frå `skos:prefLabel@nb`).

```makefile
gen-external-los:
	mkdir -p generated/external/los
	podman run --rm -v "$(PWD):/work" -w /work localhost/linkml-local:latest \
	    python src/external/los/extract.py
```

### EK3 — Generer LinkML-enum frå los-tema.yaml

**Fil:** `src/external/los/gen_enum.py` → `generated/external/los/los-tema-enum.yaml`

Les `generated/external/los/los-tema.yaml` og skriv ein LinkML-enum-fil
`LosTema` med alle gyldige URI-ar som `permissible_values`. Inkluder
snapshot-dato i `description` slik at brukaren veit kva versjon enumet gjeld.

```makefile
gen-external-los-enum:
	podman run --rm -v "$(PWD):/work" -w /work localhost/linkml-local:latest \
	    python src/external/los/gen_enum.py
```

### EK4 — Dokumentasjon i mkdocs-portalen

**Fil:** `mkdocs/docs/ekstern-kodeverk.md`, oppdater `publish.sh`

Sida viser:
- Alle registrerte kjelder med nedlastingsdato og lenkje
- Korleis ein oppdaterer eit kodeverk (`make download-external-los && make gen-external-los-enum`)
- Ei tabell over gyldige Los-tema-URI-ar med norske namn (generert frå `los-tema.yaml`)
- Korleis ein domenemodell importerer `los-tema-enum.yaml` for opt-in-validering

### EK5 — Samla oppdateringsflyt

```makefile
update-external-los: download-external-los gen-external-los gen-external-los-enum
	@echo "Los oppdatert — commit src/external/los/ med dato i commit-meldinga"
```

Brukaren køyrer `make update-external-los`, kontrollerer endringar i
`git diff src/external/los/`, og committar med dato i meldinga:

```
chore(external): oppdater Los-snapshot 2026-MM-DD

- los.ttl: <N> nye URI-ar, <M> sletta URI-ar (jf. git diff)
- manifest.yaml: sha256 oppdatert
```

---

## Prioritert handlingsliste

| # | Tiltak | Fil(ar) | Avheng av |
|---|--------|---------|-----------|
| 1 | EK0: Avklar Turtle-tilgang og SHACL sh:in-støtte | — | — |
| 2 | EK1: `src/external/los/` + download.py + Makefile-target | `src/external/`, `Makefile` | EK0a |
| 3 | EK2: `extract.py` + `make gen-external-los` | `src/external/los/extract.py`, `Makefile` | EK1 |
| 4 | EK3: `gen_enum.py` + `make gen-external-los-enum` | `src/external/los/gen_enum.py`, `Makefile` | EK2 |
| 5 | EK4: Portaldokumentasjon med Los-tabell | `mkdocs/docs/ekstern-kodeverk.md`, `publish.sh` | EK2 |
| 6 | EK5: Samla `update-external-los`-target | `Makefile` | EK1–EK4 |

**Utsette steg (avheng av EK0b):**

| # | Tiltak | Merknad |
|---|--------|---------|
| EK6 | SHACL-integrasjon (`sh:in`-lister) | Berre aktuelt om LinkML støttar det (EK0b) |
| EK7 | Los-enum i domenemodell (t.d. `dcat-ap-no`-eksempel) | Etter EK3 — opt-in, ikkje AP-NO-kjerne |

---

## Avhengigheiter

- rdflib er allereie i `linkml-local`-containeren
- `src/external/` committast; `generated/external/` er i `.gitignore`
- EK6 (SHACL) er berre aktuelt etter positiv EK0b-verifisering
- Fleire vokabular (EU MDR, ADMS) følgjer same mønster etter EK1–EK5 er etablert

## Framtidig utvidingar (ikkje del av denne planen)

- EU MDR: språk, format, filtype, frekvens
- ADMS Status-vokabular
- Diff-rapport ved oppdatering (nye URI-ar, sletta URI-ar)
- GitHub Actions: åtvarsle når SHA256 på kjeldenettstaden endrar seg
