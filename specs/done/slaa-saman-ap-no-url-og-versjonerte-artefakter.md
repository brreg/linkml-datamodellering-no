# Slå saman "AP-NO-skjema-URL-ar" og "Versjonerte artefakter" i ekstern-bruk.md

## Bakgrunn

Brukaren peika på at overskriftene "AP-NO-skjema-URL-ar" og "Versjonerte
artefakter" i `mkdocs/docs/arkitektur/ekstern-bruk.md` er delvis
overlappande, og bad om eit forslag til samanslåing. Dette er eit
**forslag til review** — ikkje utført enno.

## Funn — konkret overlapp

Samanlikna dei to seksjonane (`ekstern-bruk.md` linje 35-87) direkte:

1. **Identisk kodeblokk duplisert ordrett.** Begge seksjonane har eit
   "Døme på import"-eksempel med **nøyaktig same** YAML (linje 58-62 og
   75-79):
   ```yaml
   imports:
     - linkml:types
     - https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/dcat-ap-no-v2.8.0/src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema
   ```
2. **Same URL-mønster forklart to gonger** — `raw.githubusercontent.com/
   {versjon}/{sti}`-mønsteret vert introdusert i "AP-NO-skjema-URL-ar"
   (linje 39-41) og igjen omtala i "Versjonerte artefakter" (linje 71,
   `raw.githubusercontent.com-URL med tag`).
3. **Sidefunn — stale versjonstag i begge duplikat-eksempla:**
   AP-NO-profil-tabellen (linje 45) brukar no `dcat-ap-no-v2.13.0` (denne
   er tydelegvis oppdatert automatisk av eit CI-steg sidan sist denne fila
   vart lest i denne samtalen), men **begge** "Døme på import"-blokkane
   framleis viser den eldre `dcat-ap-no-v2.8.0`. Verdt å rette samstundes.

**Kva som er genuint distinkt (må bevarast, ikkje slåast bort):**

- "AP-NO-skjema-URL-ar" eig: sjølve profil-tabellen (6 AP-NO-profilar med
  brukstilfelle), og notatet om at `.yaml`-ending er valfri.
- "Versjonerte artefakter" eig: distinksjonen GitHub Pages (alltid siste
  `main`) vs. GitHub Releases/raw.githubusercontent.com-med-tag (stabilt),
  tilrådinga om å alltid bruke skjema-spesifikk versjon-tag, og åtvaringa
  om at generelle release-taggar ikkje garanterer at alle skjemafiler
  finst i commiten.

**Kryssreferanse å ta omsyn til:** `mkdocs/docs/publisering/
publisering-oversikt.md` linje 107 lenkjer eksplisitt til
`ekstern-bruk.md#versjonerte-artefakter`. Ein rein overskrift-omdøyping
ville brote denne lenkja. `attr_list` er alt aktivert i
`markdown_extensions` (`mkdocs/publish.sh` Steg 4), så ein kan feste den
gamle ankeret til den nye overskrifta eksplisitt (`{: #versjonerte-
artefakter }`) i staden for å endre den andre fila.

## Forslag til samanslått seksjon

Erstatt **begge** seksjonane (linje 35-87, inkl. dei tre `---`-skiljelinjene
som omkransar dei) med éin seksjon:

````markdown
## Skjema-URL-ar og versjonering {: #versjonerte-artefakter }

Alle skjema i dette repoet er tilgjengelege via GitHub Raw med ein
versjon-tag eller `main`:

```
https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/{versjon}/{sti}
```

GitHub Pages-URL-ar (`https://brreg.github.io/linkml-datamodellering-no/...`)
peikar alltid til siste versjon på `main`. For ein **stabil, versjonert
adresse** til ein historisk versjon — t.d. for import frå eit eksternt
repo — bruk i staden:

- **[GitHub Releases](https://github.com/brreg/linkml-datamodellering-no/releases)** (anbefalt) — kanonisk adresse for eldre versjonar
- **`raw.githubusercontent.com`-URL med tag**, som over

!!! tip "Anbefaling"
    Bruk alltid ein **skjema-spesifikk versjon-tag** (t.d. `dcat-ap-no-v2.13.0`, `common-ap-no-v1.0.0`) i imports — aldri `main` eller `latest` — for å unngå overraskande endringer når dette repoet vert oppdatert.

!!! warning "Skjema-spesifikke taggar"
    Generelle release-taggar (`v1.0.0`, `v1.1.0`) peikar til ein spesifikk commit, men garanterer **ikkje** at alle skjemafiler finst i den commiten. Bruk **skjema-spesifikke taggar** (t.d. `dcat-ap-no-v2.13.0`, `common-ap-no-v1.0.0`) for stabile import-URL-ar.

### AP-NO-profilar

| Profil | Import-URL (`versjon`) | Brukstilfelle |
|---|---|---|
| `dcat-ap-no` | `https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/dcat-ap-no-v2.13.0/src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema` | Datakatalogar og datasett |
| `skos-ap-no` | `https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/skos-ap-no-v2.16.0/src/linkml/ap-no/skos-ap-no/skos-ap-no-schema` | Omgrepsamlingar |
| `modelldcat-ap-no` | `https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/modelldcat-ap-no-v1.10.0/src/linkml/ap-no/modelldcat-ap-no/modelldcat-ap-no-schema` | Informasjonsmodellar |
| `dqv-ap-no` | `https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/dqv-ap-no-v1.15.0/src/linkml/ap-no/dqv-ap-no/dqv-ap-no-schema` | Datakvalitet |
| `cpsv-ap-no` | `https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/cpsv-ap-no-v1.10.0/src/linkml/ap-no/cpsv-ap-no/cpsv-ap-no-schema` | Offentlege tenester og hendingar |
| `xkos-ap-no` | `https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/xkos-ap-no-v1.0.0/src/linkml/ap-no/xkos-ap-no/xkos-ap-no-schema` | Utvida klassifikasjon |

!!! note "`.yaml`-ending er valfri"
    LinkML løyser importer utan filending — begge variantar fungerer:
    `...dcat-ap-no-schema` og `...dcat-ap-no-schema.yaml`

Døme på importdel i eit eksternt skjema:

```yaml
imports:
  - linkml:types
  - https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/dcat-ap-no-v2.13.0/src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema
```
````

**Kva som er fjerna/endra frå originalen:**

- Den duplikate "Døme på import"-kodeblokka (var to identiske, no éin).
- URL-mønster-forklaringa slått saman til éin introduksjon i staden for to.
- Versjonstag i eksempla oppdatert frå stale `dcat-ap-no-v2.8.0` til
  `dcat-ap-no-v2.13.0` (matchar no tabellen).
- Overskrift-hierarkiet endra: profil-tabellen vert no ein `###`-
  underseksjon ("AP-NO-profilar") av den samanslåtte `##`-seksjonen, i
  staden for sin eigen `##`-seksjon.
- **Ingenting av det faktiske sakleg innhaldet er fjerna** — tabellen,
  begge admonition-boksane (tip + warning) og `.yaml`-notatet er alle
  bevart uendra.

## Steg (dersom brukaren godkjenner forslaget)

1. Erstatt linje 35-87 i `ekstern-bruk.md` med den samanslåtte seksjonen
   over.
2. Verifiser at `attr_list`-syntaksen (`{: #versjonerte-artefakter }`) gjev
   nøyaktig same heading-id som før, slik at
   `publisering-oversikt.md#versjonerte-artefakter`-lenkja framleis
   fungerer — sjekk generert HTML (`make docs-build` eller tilsvarande)
   om mogleg, elles verifiser `attr_list`-syntaksen sin dokumenterte
   åtferd.
3. Sjekk om andre filer lenkjer til `#ap-no-skjema-url-ar` (ikkje funne i
   denne evalueringa, men verdt ein siste `grep` før endringa vert gjort).
4. Oppdater specen med `## Utført` og flytt til `specs/done/`.

## Akseptansekriterium

- Éin samanslått seksjon, ingen duplisert kodeblokk.
- `publisering-oversikt.md`-lenkja til `#versjonerte-artefakter` verifisert
  framleis fungerande.
- Alt sakleg innhald (tabell, tip, warning, `.yaml`-notat) bevart.
- Versjonstag i eksempelet matchar tabellen (ikkje lenger stale).

## Handlingsliste

- [x] Brukar godkjenner forslaget (eller ber om justeringar)
- [x] Steg 1: seksjonane slått saman i `ekstern-bruk.md`
- [x] Steg 2: heading-id/anker verifisert uendra
- [x] Steg 3: ingen andre lenkjer til den gamle `#ap-no-skjema-url-ar`-ankeret

## Utført

Seksjonane "AP-NO-skjema-URL-ar" og "Versjonerte artefakter" i
`ekstern-bruk.md` (linje 35-87) erstatta med éin samanslått seksjon
`## Skjema-URL-ar og versjonering {: #versjonerte-artefakter }`, nøyaktig
som skissert i forslaget over — ingen justeringar bedne om.

**Verifisert:**

1. **Heading-id/anker** — testa direkte med `python3 -c "import markdown;
   ..."` (python-markdown med `attr_list`, same extensions som
   `mkdocs/publish.sh` konfigurerer): `## Skjema-URL-ar og versjonering
   {: #versjonerte-artefakter }` renderer til
   `<h2 id="versjonerte-artefakter">...</h2>` — nøyaktig same id som før.
   `publisering-oversikt.md#versjonerte-artefakter`-lenkja er difor
   uendra fungerande.
2. **Ingen andre lenkjer til `#ap-no-skjema-url-ar`** — stadfesta med
   `grep -rn "ap-no-skjema-url" mkdocs/docs/ README.md CLAUDE.md
   CONTRIBUTING.md` — null treff, trygt å fjerne denne overskrifta.
3. **Duplikat kodeblokk fjerna** — var to identiske "Døme på import"-
   blokker, no éin.
4. **Stale versjonstag retta** — begge dupliserte eksempla brukte
   `dcat-ap-no-v2.8.0` medan profil-tabellen alt hadde vorte automatisk
   oppdatert til `dcat-ap-no-v2.13.0`; eksempelet matchar no tabellen.
5. **Sakleg innhald uendra** — profil-tabellen (6 rader), begge
   admonition-boksane (tip + warning) og `.yaml`-ending-notatet er alle
   bevart, berre flytta/omorganisert (tabellen er no ein `###`-
   underseksjon "AP-NO-profilar" i staden for sin eigen `##`-seksjon).

**Notert, ikkje endra (utanfor scope):** tre andre stader i same fil
(`ekstern-bruk.md` linje 23, 147, 232 før denne endringa) brukte framleis
den eldre `dcat-ap-no-v2.8.0`-taggen som illustrativt eksempel — desse var
ikkje del av dei to seksjonane brukaren bad om å slå saman, og vart difor
ikkje rørte i fyrste omgang.

### Oppfølging: alle tre retta til v2.13.0

Brukaren bad om å oppdatere desse tre gjenverande stadene òg. Alle tre
(Bootstrap-eksempel linje 22-23, `ap-no-version`-tabell linje 147,
image-tagg-notat linje 232) retta frå `dcat-ap-no-v2.8.0` til
`dcat-ap-no-v2.13.0`. Stadfesta med `grep -c "dcat-ap-no-v2.8.0"
mkdocs/docs/arkitektur/ekstern-bruk.md` → 0 treff att i heile fila.

Status: ferdig. Flytta til `specs/done/`.

## Relaterte filer

- `mkdocs/docs/arkitektur/ekstern-bruk.md` — hovudmål
- `mkdocs/docs/publisering/publisering-oversikt.md` — ekstern lenkje til `#versjonerte-artefakter`, må ikkje brytast
- `mkdocs/publish.sh` — stadfesting av at `attr_list` er aktivert
