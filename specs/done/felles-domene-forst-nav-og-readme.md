# FELLES-domenet først i NAV-meny og README-tabellar

## Bakgrunn

Domenet `src/linkml/felles/` (`brreg-felles-adresse`, `brreg-felles-aktoer`,
`brreg-felles-tid`, `brreg-felles-typer`) vart oppretta i commit
`ae3467d4` ("feat(felles): opprett brreg-felles-*-modellar og migrer
enhetsregisteret-*"), men er ikkje lagt inn i dei tre stadene som held
hardkoda domene-rekkefølgje/-lister:

1. **`mkdocs/publish.sh`** (`DOMAIN_ORDER`, linje ~269) — styrer
   rekkefølgja i NAV-menyen i mkdocs-portalen. `felles` manglar i lista.
   Sidan scriptet har ein alfabetisk fallback for domene som ikkje er i
   `DOMAIN_ORDER`, hamnar `felles` i praksis **sist** i NAV-menyen i dag
   (einaste domenet utanfor den hardkoda lista).
2. **`README.md`** — `## Domener`-tabellen (manuelt vedlikehalden,
   linje ~184-189) manglar heilt ein rad for FELLES.
3. **`src/assets/scripts/makefile/generate-readme-tables.sh`**
   (`DOMAIN_ORDER` i `generate_schema_table()`, linje 38) — styrer
   rekkefølgje og *filter* for den autogenererte Skjema-tabellen i
   README.md. Denne lista har **ingen** alfabetisk fallback (i motsetnad
   til `publish.sh`) — domene som ikkje står i lista vert filtrert heilt
   bort. Dette betyr at dei fire FELLES-modellane i dag **ikkje** dukkar
   opp i Skjema-tabellen i README.md.

**Ønska sluttilstand** (avklart med brukar):

- FELLES skal visast **først** i NAV-menyen i mkdocs-portalen.
- FELLES skal leggjast til **først** i Domener-tabellen i README.md.
- Modellane i FELLES skal inkluderast i den autogenererte
  Skjema-tabellen i README.md, med **same rekkefølgje** (FELLES først)
  som i NAV-menyen og Domener-tabellen, for konsistens.

## Steg

1. `mkdocs/publish.sh`: legg `"felles"` **først** i `DOMAIN_ORDER`-arrayen
   (linje ~269), slik at NAV-menyen viser FELLES før REFERANSE, AP-NO osv.
2. `src/assets/scripts/makefile/generate-readme-tables.sh`: legg
   `"felles"` **først** i `DOMAIN_ORDER`-arrayen inni
   `generate_schema_table()` (linje 38), slik at dei fire
   brreg-felles-*-modellane kjem med i Skjema-tabellen, plassert først.
3. `README.md`: legg til ein ny rad for **FELLES** **først** i
   `## Domener`-tabellen (før REFERANSE-rada), med skildring:
   > Gjenbrukbare felleskomponentar (adresse, aktør, tid, typer) utleia
   > frå Brønnøysundregistrene (BR) sine interne referansemodellar. Kan
   > importerast av domenemodellar.
   Lenkje til `https://github.com/brreg/linkml-datamodellering-no/tree/main/src/linkml/felles/`
   som for dei andre domena. Ingen ekstern standard-lenkje (tredje
   kolonne let stå tom, som for OREG).
4. Regenerer dokumentasjonsportalen og README-tabellane via
   `make docs-publish` (eller relevant delmål som regenererer nav og
   README-tabellar) og verifiser at:
   - FELLES ligg først i NAV-menyen i `mkdocs/mkdocs.yml`.
   - FELLES ligg først i Domener-tabellen i README.md.
   - Alle fire brreg-felles-*-modellane ligg først (i alfabetisk
     undersortering) i Skjema-tabellen i README.md, mellom
     `<!-- BEGIN AUTO-GENERATED -->`/`<!-- END AUTO-GENERATED -->`.
5. Diff README.md og mkdocs.yml for å stadfeste at berre forventa
   endringar (FELLES-relaterte) er gjort — ingen utilsikta reordering av
   andre domene.

## Handlingsliste

- [x] Steg 1: `mkdocs/publish.sh` — `felles` først i `DOMAIN_ORDER`
- [x] Steg 2: `generate-readme-tables.sh` — `felles` først i `DOMAIN_ORDER`
- [x] Steg 3: `README.md` — ny FELLES-rad først i Domener-tabellen
- [x] Steg 4: Regenerer og verifiser NAV-meny + README-tabellar
- [x] Steg 5: Diff-kontroll av utilsikta endringar

## Utført

- `mkdocs/publish.sh`: `"felles"` lagt først i `DOMAIN_ORDER` (linje 269).
- `src/assets/scripts/makefile/generate-readme-tables.sh`: `"felles"` lagt
  først i `DOMAIN_ORDER` i `generate_schema_table()` (linje 38).
- `README.md`: ny FELLES-rad lagt til først i `## Domener`-tabellen.
- `make docs-publish` køyrd: README-tabellane vart regenererte (FELLES
  først i Domener-tabellen og med alle fire brreg-felles-*-modellane
  først i Skjema-tabellen, med alfabetisk undersortering), og
  `mkdocs/mkdocs.yml` (gitignora, generert) fekk `- 'FELLES':` som
  første domene-seksjon i nav-menyen, før REFERANSE, AP-NO osv.
- Verifisert med `git status`/`grep` at ingen andre domene vart
  reordna, og at `mkdocs.yml` ikkje er sporbart av git (sannkjelda er
  `publish.sh`).

**Oppfølging 1:** `src/linkml/felles/description.md` oppretta (manglande
portaltekst for domenet — same struktur/stil som `oreg/`, `ngr/`,
`samt/description.md`: kort intro, oversikt over dei fire modellane i
importrekkjefølgje, "Typisk brukar"-avsnitt). `make docs-publish`
kjørt på nytt og verifisert at teksten dukkar opp i
`mkdocs/docs/felles/index.md`.

**Oppfølging 2:** `mkdocs/lib/utils/formatters.sh` — lagt til
`felles) echo "FELLES - Fellesmodellar" ;;` i `domain_label()`, same
mønster som dei andre domena (`REFERANSE - Referansemodellar` osv.).
Utan dette fall `felles` gjennom til default-casen (berre uppercasa
domenenamn, ingen " - "-forklaring). Verifisert i regenerert
`mkdocs/mkdocs.yml`: `- 'FELLES - Fellesmodellar':`.
