# Dokumenter README-tabellgenerering

## Bakgrunn

README.md inneheld fire auto-genererte tabellar:
1. **Domenetabell** — oversikt over alle domene med skildringar
2. **Skjematabell** — alle LinkML-skjema per domene
3. **Artefakttabell** — genererte artefakter og deira brukstilfelle
4. **Modellkatalogtabell** — automatisk genererte modellkatalogar per organisasjon

Desse tabellane vert genererte av `src/assets/scripts/generate-readme-tables.sh` og sett inn mellom HTML-kommentarar (`<!-- BEGIN AUTO-GENERATED: ... -->` / `<!-- END AUTO-GENERATED: ... -->`).

Scriptet vert køyrt automatisk av CI (`.github/workflows/update-readme.yml`) ved endringar i `src/linkml/`, men kan også køyrast manuelt med `make readme-tables`.

Det er viktig å dokumentere korleis dette fungerer, slik at framtidige bidragsytarar forstår:
- Kvar tabellane kjem frå
- Korleis ein legg til nye domene/skjema
- Kvar ein redigerer skildringar og dokumentasjonslenkjer
- Kva som er hardkoda vs. auto-oppdaga

## Handlingsliste

- [x] Opprett ny dokumentasjonsfil `mkdocs/docs/readme-tabellgenerering.md`
- [x] Dokumenter dei fire tabellane og korleis dei vert genererte
- [x] Forklar hardkoda vs. auto-oppdaga innhald
- [x] Legg til døme på korleis ein legg til nytt domene/skjema
- [x] Lenk til relevante script og CI-workflows
- [x] Legg til lenkje til den nye dokumentasjonsfila i `README.md` under "For bidragsytarar"
- [x] Generer commit-melding

## Steg

### 1. Les eksisterande bidragsytardokumentasjon

Sjå på `CONTRIBUTING.md` og andre bidragsytardokument for stil og tone.

### 2. Skriv dokumentasjon

Opprett `mkdocs/docs/readme-tabellgenerering.md` med desse seksjonane:

**Hovudoverskrift:** `# README-tabellgenerering`

**Innleiing:**
- Kort forklaring av kvifor tabellane er auto-genererte (konsistens, redusert vedlikehald)
- Oversikt over dei fire tabellane

**Tabelloversikt og kjelder** (inspirert av `index-md-struktur.md`):
- Tabell med kolonnane: `#`, `Tabell`, `Innhald`, `Kjelde`, `Funksjon i generate-readme-tables.sh`
- Viser kvar tabell, kva kjelde den har (hardkoda vs. auto-oppdaga) og kva funksjon som genererer han

**Seksjon per tabell:**

For kvar tabell:
- **Kva tabellen inneheld** — formål og struktur
- **Korleis han vert generert** — hardkoda vs. auto-oppdaga
- **Korleis ein legg til nye entries** — konkrete steg med filstiar
- **Døme** — kodeblokk som viser korleis ein legg til nytt domene/skjema

**CI-integrasjon:**
- Forklar at `update-readme.yml` køyrer scriptet automatisk
- Korleis ein køyrer scriptet manuelt (`make readme-tables`)

**Feilsøking:**
- Kva ein gjer dersom eit skjema ikkje dukkar opp
- Korleis ein oppdaterer skildringar og lenkjer

### 3. Strukturér dokumentasjonen

Følg desse prinsippa:
- Bruk **nynorsk** (som i resten av dokumentasjonen)
- Konsistent overskriftsnivå (`##` for hovudseksjonar, `###` for underseksjonar)
- Kodeblokkar med syntax highlighting (`bash`, `yaml`)
- Lenkjer til relaterte filer (`generate-readme-tables.sh`, `update-readme.yml`)

### 4. Oppdater README.md

Legg til lenkje til den nye dokumentasjonsfila under "For bidragsytarar"-seksjonen i `README.md`:

```markdown
## For bidragsytarar

Dersom du skal bidra til repoet, les desse dokumenta:

- **[PRINCIPLES.md](PRINCIPLES.md)** — designprinsipp for modellering
- **[CONVENTIONS.md](CONVENTIONS.md)** — namnekonvensjonar, manifestformat og commit-meldingar
- **[CONTRIBUTING.md](CONTRIBUTING.md)** — korleis bidra (PR-prosess, kodegjennomgang)
- **[GOVERNANCE.md](GOVERNANCE.md)** — roller, eigarskap og RFC-prosess
- **[README-tabellgenerering](https://brreg.github.io/linkml-datamodellering-no/readme-tabellgenerering/)** — korleis README-tabellane vert genererte
```

### 5. Generer commit-melding

Kompakt commit-melding i conventional commits-format:
```
docs(README,mkdocs): dokumenter README-tabellgenerering
  - mkdocs/docs/readme-tabellgenerering.md: ny rettleiing for auto-genererte tabellar
  - README.md: lenk til ny dokumentasjonsside under "For bidragsytarar"
```

## Utført

Alle steg er fullførte:

1. ✅ Les eksisterande bidragsytardokumentasjon — leste `CONTRIBUTING.md` for stil og tone
2. ✅ Skriv dokumentasjon — oppretta `mkdocs/docs/readme-tabellgenerering.md` med alle seksjonar
3. ✅ Strukturér dokumentasjonen — følgde nynorsk, overskriftsnivå, kodeblokkar med syntax highlighting, lenkjer til relaterte filer
4. ✅ Oppdater README.md — la til lenkje under "For bidragsytarar"
5. ✅ Generer commit-melding — sjå under

### Endra filer

- `mkdocs/docs/readme-tabellgenerering.md` — ny rettleiing som dokumenterer:
  - Kvifor tabellane er auto-genererte
  - **Tabelloversikt og kjelder** (inspirert av `index-md-struktur.md`) — tabell som viser kvar tabell, kjelde (hardkoda vs. auto-oppdaga) og funksjon
  - Kva kvar av dei fire tabellane inneheld
  - Korleis tabellane vert genererte (hardkoda vs. auto-oppdaga)
  - Steg-for-steg-instruksjonar for å leggje til nye domene/skjema/modellkatalogar
  - CI-integrasjon og manuell køyring
  - Feilsøkingstips
  - Lenkjer til relaterte filer og dokumentasjon

- `README.md` — la til lenkje til ny dokumentasjonsside under "For bidragsytarar"

- `specs/done/dokumenter-readme-tabellgenerering.md` — oppdatert med "Tabelloversikt og kjelder"-tabell inspirert av `index-md-struktur.md`
