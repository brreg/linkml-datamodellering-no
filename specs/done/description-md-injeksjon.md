# Injiser `description.md` i modell-`index.md` på mkdocs-portalen

## Bakgrunn

Noverande `index.md`-generering i `mkdocs/publish.sh` produserer ei teknisk oversikt:
- Metadata-tabell (name, title, version, license, imports osv.)
- ER-diagram (PlantUML SVG — filtrert og full versjon)
- Klasseliste (Obligatorisk, Anbefalt, Valgfri, Andre)
- Slot-liste
- Artefakt-tabell (TTL, JSON Schema, SHACL osv.)
- Valideringsresultat (frå MCP-validator)
- Versjonslog (CHANGELOG.md)

Enkelte modellar (`dcat-ap-no`, `modelldcat-ap-no`, `skos-ap-no`, `brreg-begrepskatalog`, `enhetsregisteret-bvrinn`, `register-over-aksjeeiere`) har allereie oppretta ein **`description.md`** i `src/linkml/<domain>/<modell>/` som gjev brukarorientert kontekst:

- Kva er modellen og kvifor finst ho?
- Kven er typiske brukarar?
- Relasjon til andre modellar i repoet
- Avvik frå referansespesifikasjonar

Desse beskrivingane vert **ikkje** inkluderte i den genererte `index.md`-fila — brukaren må opne modellmappa i GitHub for å finne dei.

## Noverande gap

| Modell | `description.md` finst? | Injisert i portal? |
|---|---|---|
| `dcat-ap-no` | ✅ | ❌ |
| `modelldcat-ap-no` | ✅ | ❌ |
| `skos-ap-no` | ✅ | ❌ |
| `brreg-begrepskatalog` | ✅ | ❌ |
| `enhetsregisteret-bvrinn` | ✅ | ❌ |
| `register-over-aksjeeiere` | ✅ | ❌ |
| Andre 27 modellar | ❌ | ❌ |

Resultat: portalbrukarar får berre metadata og diagram — inga brukarorientert kontekst.

## Foreslått innhaldsstruktur for `index.md` (etter injeksjon)

1. **Hovudoverskrift** (`# <schema>`)
2. **`description.md`-innhald** (dersom fila finst) — **NY SEKSJON**
3. **Metadata-tabell** (`## Metadata` frå gen-doc)
4. **Publiseringsinfo** (boks dersom `published-uris.lock` finst)
5. **ER-diagram** (`## ER-diagram`)
6. **Klasseliste** (`## Classes`, `## Slots`, `## Enumerations`, `## Types`)
7. **Artefaktabell** (`## Generated artifacts`)
8. **Valideringsresultat** (`## Valideringsresultat`)
9. **Versjonslog** (`## Versjonslog` frå `CHANGELOG.md`)

**Plassering:** `description.md` kjem **etter** hovudoverskrifta og **før** metadata-tabellen, slik at brukarar møter konteksten fyrst.

## Innhaldsstruktur for `description.md` (rettleiing)

Kvar `description.md` bør følgje dette mønsteret (sjå `dcat-ap-no/description.md` som referanse):

1. **Hovudparagraf** — Kva er modellen, kva problem løyser ho?
2. **Typisk brukar** — Kven er målgruppa?
3. **Nøkkelklasser** — Korte lister (3–7 klasser)
4. **Relasjon til andre modellar** — Avhengigheiter og importstruktur
5. **Avvik/spesielle grep** (valfritt) — Referansar til `specs/done/avvik-*.md`

**Lengde:** 10–20 liner (ca. 150–300 ord). Ikkje dokumenter intern API-detalj — det gjer klassedokumentasjonen.

## Steg

1. ✅ Dokumenter noverande `index.md`-struktur (gjort over)
2. ✅ Utvid `mkdocs/publish.sh` (linje 142–151) med `description.md`-injeksjon:
   ```bash
   description_file="$REPO_ROOT/src/linkml/$domain/$schema/description.md"
   if [ -f "$description_file" ]; then
       cat "$description_file"
       echo ""
       echo ""
   fi
   ```
3. ✅ Oppdater `mkdocs/docs/ny-domenemodell.md` — endra linje 27 frå "etter ER-diagrammet" til "før metadata-tabellen"
4. ✅ Regenerert portalen (`make docs-publish`) og verifisert at `description.md` vert injisert korrekt for:
   - `ap-no/dcat-ap-no` — 17 liner brukarorientert introduksjon
   - `ap-no/modelldcat-ap-no` — 21 liner med skjemastruktur-forklaring
   - `ap-no/skos-ap-no` — 16 liner med typisk brukar og relasjonar
   - Modellar utan `description.md` (t.d. `samt-bu`) startar direkte med metadata-tabellen (som før)
5. ⬜ (Valfritt, låg prioritet) Skriv `description.md` for dei 27 andre modellane — kan gjerast inkrementelt

## Prioritert handlingsliste

| Steg | Handling | Prioritet | Estimat | Status |
|---|---|---|---|---|
| 2 ✓ | Injiser `description.md` i `publish.sh` før metadata-tabell | Høg | 5 min | ✅ Utført |
| 3 ✓ | Oppdater `ny-domenemodell.md` med korrekt plassering | Høg | 2 min | ✅ Utført |
| 4 ✓ | Regenerer portal og verifiser injeksjon | Høg | 3 min | ✅ Utført |
| 5 ⬜ | Skriv `description.md` for resterande 27 modellar | Låg | 10–15 min per modell | ⬜ Valfritt |

## Avhengigheiter

- Ingen — `publish.sh` har allereie logikk for å handtere valfrie filer (`CHANGELOG.md`, `published-uris.lock`)

## Suksesskriterium

Når brukaren navigerer til https://brreg.github.io/linkml-datamodellering-no/ap-no/dcat-ap-no/, skal `index.md` vise:
1. Hovudoverskrift (`# dcat-ap-no`)
2. **Brukarorientert introduksjon** (frå `description.md`) — **NY**
3. Metadata-tabell
4. ER-diagram
5. (resten som før)

## Utført

Implementert alle tre hovudstega (2-4) med vellykka verifisering:

**Steg 2 — `mkdocs/publish.sh` (linje 145-151):**
```bash
# Injiser description.md dersom det finst (brukarorientert introduksjon)
description_file="$REPO_ROOT/src/linkml/$domain/$schema/description.md"
if [ -f "$description_file" ]; then
    cat "$description_file"
    echo ""
    echo ""
fi
```

**Steg 3 — `mkdocs/docs/ny-domenemodell.md` (linje 27):**
Oppdatert dokumentasjon til å reflektere at `description.md` vert injisert **før** metadata-tabellen (ikkje etter ER-diagrammet som tidlegare dokumentert).

**Steg 4 — Verifisering:**
Regenerert portalen og verifisert at `description.md` vert injisert korrekt for:
- `ap-no/dcat-ap-no` — 17 liner brukarorientert introduksjon med typisk brukar, nøkkelklasser og relasjonar
- `ap-no/modelldcat-ap-no` — 21 liner med skjemastruktur-forklaring (hovudskjema + to moduler)
- `ap-no/skos-ap-no` — 16 liner med typisk brukar, nøkkelklasser og relasjonar

Modellar utan `description.md` (t.d. `samt-bu`, `fint-administrasjon`) startar direkte med metadata-tabellen som før — ingen regresjon.

**Avvik frå opphavleg plan:** Ingen.

**Steg 5 (valfritt):** Å skrive `description.md` for dei resterande 27 modellane er markert som låg prioritet og kan gjerast inkrementelt etter kvart som modellar modnar.
