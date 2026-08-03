# Debug: Referanse-domene manglar i NAV-meny på GitHub Pages

## Problem

"Referanse"-domenet vert ikkje vist i navigasjonsmenyen på GitHub Pages-portalen, sjølv om domenet finst i `generated/referanse/` og skal inkluderast i `mkdocs.yml`.

## Hypotesar

1. **`mkdocs/publish.sh` hoppar over referanse-domenet** — skriptet filterer vekk domene basert på krav (t.d. berre domene med skjema, berre domene med `generated/`-katalog)
2. **`mkdocs.yml` vert ikkje regenerert** — fila er manuelt redigert og `publish.sh` skriv ikkje over ho
3. **Referanse-domenet har ikkje genererte artefaktar** — `generated/referanse/` er tom eller manglar `index.md`
4. **NAV-struktur i `publish.sh` har hardkoda domeneliste** — referanse er ikkje i lista
5. **Case-sensitivity-problem** — "Referanse" vs "referanse" i filnamn/katalognamn
6. **MkDocs-cache-problem** — `mkdocs/.cache/` har utdatert state

## Debugging-steg

### Steg 1: Verifiser at referanse-domenet finst i `generated/`

```bash
# Sjekk om katalogen finst
ls -la generated/referanse/

# Sjekk om det finst skjema i katalogen
find generated/referanse -name "*-schema.yaml" -o -name "index.md"

# Sjekk storleiken
du -sh generated/referanse/
```

**Forventa:** Katalogen skal finne og innehalde genererte artefaktar (`.ttl`, `.json`, `docs/index.md` osv.)

**Dersom katalogen manglar eller er tom:**
- Køyr `make domain-referanse` for å regenerere artefaktar
- Sjekk `src/linkml/referanse/` — finst det skjema der?
- Sjekk om `referanse` er i `DOMAINS`-lista i `make/02-schema-discovery.mk`

### Steg 2: Sjekk om `mkdocs/docs/referanse/` vert oppretta av `publish.sh`

```bash
# Køyr publish.sh
make docs-publish

# Sjekk om katalogen vart oppretta
ls -la mkdocs/docs/referanse/

# Sjekk innhald
find mkdocs/docs/referanse -type f | head -20
```

**Forventa:** `mkdocs/docs/referanse/` skal innehalde kopierte artefaktar frå `generated/referanse/`.

**Dersom katalogen manglar:**
- Sjekk `mkdocs/publish.sh` — korleis filtrerer den domene?
- Sjekk om referanse-domenet hoppar over ein pre-check (t.d. "berre domene med skjema")

### Steg 3: Sjekk `mkdocs.yml` — er referanse i NAV-strukturen?

```bash
# Les mkdocs.yml
cat mkdocs/mkdocs.yml | grep -A 30 "nav:"

# Søk spesifikt etter referanse
grep -i "referanse" mkdocs/mkdocs.yml
```

**Forventa:** `mkdocs.yml` skal ha ein seksjon som dette:

```yaml
nav:
  - Heim: index.md
  - Rettleiingar:
      - ...
  - Referanse:
      - referanse/index.md
      - Skjema:
          - referanse/<skjema>/index.md
```

**Dersom referanse manglar i `mkdocs.yml`:**
- Sjekk om `publish.sh` hardkodar domenelista (leit etter `nav:` i heredoc-blokka)
- Sjekk om `publish.sh` genererer NAV dynamisk frå `generated/`-struktur

### Steg 4: Sjekk `mkdocs/publish.sh` — korleis genererer han NAV?

```bash
# Finn NAV-genereringa i publish.sh
grep -n "nav:" mkdocs/publish.sh -A 50 | head -100

# Finn domene-loop
grep -n "for domain in" mkdocs/publish.sh
```

**Forventa:** `publish.sh` skal ha ein loop som dette:

```bash
for domain in $(ls -1 generated/ | sort); do
  # Generer NAV-seksjon for kvar domene
  echo "  - ${domain^}:" >> mkdocs.yml
  ...
done
```

**Dersom NAV er hardkoda:**
- Oppdater `publish.sh` til å dynamisk generere NAV frå `generated/`-katalogane
- Eller legg til `referanse` manuelt i hardkoda liste

### Steg 5: Test lokalt med `mkdocs serve`

```bash
# Bygg dokumentasjon
make docs-publish

# Start lokal server
make docs-serve

# Opne http://localhost:8000 og sjekk NAV-menyen
```

**Forventa:** Referanse-domenet skal vise i venstre sidebar.

**Dersom referanse ikkje viser:**
- Sjekk nettlesarkonsollen for feil
- Sjekk MkDocs-loggen for åtvaringar
- Sjekk om det er feil i `mkdocs.yml` (t.d. ugyldig YAML-syntaks)

### Steg 6: Sjekk GitHub Actions-loggar

```bash
# Last ned generate-workflow-loggen frå siste køyring
# Søk etter "referanse" i loggen

grep -i "referanse" workflow.log

# Sjekk om "Steg 1: Rens tidlegare genererte domene-katalogar" sletta referanse
grep "Ryddar forsvunne domene: referanse" workflow.log
```

**Dersom referanse vart sletta i Steg 1:**
- `generated/referanse/` finst ikkje lenger (vart sletta fordi `src/linkml/referanse/` manglar)
- Sjekk om `src/linkml/referanse/` finst i repoet
- Sjekk om `referanse` er i `.gitignore`

### Steg 7: Sjekk `src/linkml/referanse/` — finst det skjema?

```bash
# Sjekk om katalogen finst
ls -la src/linkml/referanse/

# Sjekk om det finst skjema
find src/linkml/referanse -name "*-schema.yaml"
```

**Forventa:** Katalogen skal innehalde minst eitt skjema (t.d. `referanse-schema.yaml`).

**Dersom katalogen manglar:**
- Referanse-domenet er ikkje lenger del av repoet
- Sjekk git-historikk: `git log --all --full-history -- src/linkml/referanse/`
- Sjekk om det vart sletta i ein commit

**Dersom katalogen finst men er tom:**
- Referanse-skjemaet vart sletta eller flytta
- Opprett eit nytt referanse-skjema eller gjenopprett det frå git-historikk

### Steg 8: Sjekk `make/02-schema-discovery.mk` — er referanse i DOMAINS?

```bash
# Sjekk korleis DOMAINS vert oppdaga
grep -A 10 "DOMAINS :=" make/02-schema-discovery.mk

# Sjekk om referanse er i lista
make -p | grep "^DOMAINS ="
```

**Forventa:** `DOMAINS` skal innehalde `referanse` dersom `src/linkml/referanse/` finst.

**Dersom referanse manglar:**
- Schema discovery-logikken hoppar over referanse-domenet
- Sjekk om `src/linkml/referanse/` har eit skjema med korrekt namngiving (`*-schema.yaml`)

## Løysingsforslag

### Løysing 1: Referanse-domenet finst ikkje lenger i repoet

**Problem:** `src/linkml/referanse/` vart sletta eller flytta.

**Løysing:**
1. Gjenopprett katalogen frå git-historikk: `git checkout <commit> -- src/linkml/referanse/`
2. Eller opprett eit nytt referanse-skjema: `make scaffold DOMAIN=referanse SCHEMA=referanse-schema`
3. Køyr `make domain-referanse` for å regenerere artefaktar
4. Køyr `make docs-publish` for å oppdatere mkdocs

### Løysing 2: `publish.sh` hoppar over referanse fordi det manglar skjema

**Problem:** `publish.sh` filtrerer vekk domene utan skjema.

**Løysing:**
1. Sjekk `mkdocs/publish.sh` for pre-check-logikk (t.d. `if [ ! -d "generated/$domain" ]; then continue; fi`)
2. Fjern eller juster filtreringa for å inkludere referanse
3. Eller legg til eit dummy-skjema i `src/linkml/referanse/` dersom referanse skal vere eit tomt domene

### Løysing 3: NAV-struktur i `mkdocs.yml` er hardkoda

**Problem:** `publish.sh` har ein hardkoda domeneliste i NAV-seksjonen.

**Løysing:**
1. Finn heredoc-blokka i `publish.sh` som genererer `mkdocs.yml`
2. Legg til `referanse` i listen, eller gjer NAV-generering dynamisk:

```bash
# Dynamisk NAV-generering
for domain in $(ls -1 generated/ | sort); do
  [ "$domain" = "mkdocs" ] && continue  # Hopp over mkdocs-katalog
  echo "  - ${domain^}:" >> mkdocs.yml
  # ... generer undermeny for skjema ...
done
```

### Løysing 4: MkDocs-cache-problem

**Problem:** `mkdocs/.cache/` har utdatert state.

**Løysing:**
```bash
rm -rf mkdocs/.cache/
make docs-build
```

## Akseptansekriterier

- [ ] `generated/referanse/` finst og inneheld genererte artefaktar
- [ ] `mkdocs/docs/referanse/` finst og inneheld kopierte artefaktar
- [ ] `mkdocs.yml` inneheld referanse i NAV-struktur
- [ ] `make docs-serve` viser referanse-domenet i venstre sidebar
- [ ] GitHub Pages viser referanse-domenet i NAV-menyen
- [ ] `make domain-referanse` fullførar utan feil

## Neste steg

1. Køyr debugging-stega 1-8 i rekkjefølgje
2. Dokumenter funna i denne spec-en (legg til `## Funna`-seksjon)
3. Implementer løysingsforslag basert på funna
4. Test lokalt med `make docs-serve`
5. Push og verifiser på GitHub Pages

## Relaterte filer

- `mkdocs/publish.sh` — genererer `mkdocs.yml` og kopierer artefaktar til `mkdocs/docs/`
- `mkdocs/mkdocs.yml` — MkDocs-konfigurasjon (auto-generert)
- `src/linkml/referanse/` — referanse-skjema (dersom det finst)
- `generated/referanse/` — genererte artefaktar for referanse-domenet
- `mkdocs/docs/referanse/` — kopierte artefaktar til mkdocs-portal
- `make/02-schema-discovery.mk` — oppdagar domene og skjema
- `.github/workflows/generate.yml` — CI-workflow som genererer artefaktar
