# Fiks v1.0.0-referansar til skjema-spesifikke taggar

## Bakgrunn

Dokumentasjonen og bootstrap-scriptet brukar `v1.0.0` som eksempel på versjonert import av AP-NO-skjema:

```
https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/v1.0.0/src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema
```

Men `v1.0.0`-taggen (commit f22c1702) vart oppretta tidleg i prosjektet, **før** dei fleste skjemafilene vart laga. Taggen inneheld difor ikkje `common-ap-no-schema.yaml`, `dcat-ap-no-schema.yaml` eller andre AP-NO-skjema → 404-feil når nokon prøver å importere desse URL-ane.

**Skjema-spesifikke taggar** (t.d. `common-ap-no-v1.0.0`, `dcat-ap-no-v2.0.0`) peikar til korrekte committar der filene faktisk finst.

## Problem

| Fil | Feil |
|---|---|
| `README.md` | Import-døme brukar `v1.0.0` utan å spesifisere skjema-spesifikk tag |
| `mkdocs/docs/ekstern-bruk.md` | Bootstrap-døme og import-døme brukar `v1.0.0` |
| `bootstrap.sh` | Kommentarar viser `v1.0.0`-eksempel |

Brukaren som følgjer desse døma vil få 404-feil når dei prøver å importere skjema.

## Løysing

**Strategi:** Bruk alltid **skjema-spesifikke taggar** i import-døme, ikkje den generelle `v1.0.0`-taggen.

| Gammelt døme (feil) | Nytt døme (korrekt) |
|---|---|
| `.../v1.0.0/src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema` | `.../dcat-ap-no-v2.0.0/src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema` |
| `.../v1.0.0/src/linkml/ap-no/common-ap-no/common-ap-no-schema.yaml` | `.../common-ap-no-v1.0.0/src/linkml/ap-no/common-ap-no/common-ap-no-schema.yaml` |
| `AP_NO_VERSION=v1.0.0` | `AP_NO_VERSION=dcat-ap-no-v2.0.0` (eller `main` for siste) |

**Generell rettesnor:**
- I bootstrap-script og dokumentasjon: bruk `main` for å alltid få siste versjon
- I import-døme: vis **skjema-spesifikk tag** og forklar kvifor det er viktig
- Legg til advarsel om at generelle release-taggar (`v1.0.0`, `v1.1.0`) **ikkje garanterer** at alle skjemafiler finst

## Steg

1. **README.md:** Endre import-døme frå `v1.0.0` til `dcat-ap-no-v2.0.0` (eller `main`)
2. **mkdocs/docs/ekstern-bruk.md:**
   - Bootstrap-døme: endre frå `v1.0.0` til `main` (eller fjern versjonert variant og bruk berre `main`)
   - Import-døme (linje 61): endre frå `v1.0.0` til `dcat-ap-no-v2.0.0`
   - Import-døme (linje 78): endre frå `v2.0.0` til `dcat-ap-no-v2.1.0` (eller bruk faktisk skjema-tag)
   - `linkml-datamodellering.yaml`-døme (linje 141): endre frå `v1.0.0` til `main` eller forklår at `v1.0.0` ikkje er ein skjema-tag
   - Tabell (linje 148-151): legg til advarsel om skjema-spesifikke taggar
3. **bootstrap.sh:**
   - Kommentar (linje ~3): endre frå `AP_NO_VERSION=v1.0.0` til `AP_NO_VERSION=main` eller fjern versjonert døme
   - Kommentar (linje ~5): endre frå `v1.0.0` til `main`
4. **CONVENTIONS.md:** Sjekk at døma er korrekte (dei ser OK ut allereie)
5. **Legg til advarsel i ekstern-bruk.md:**
   ```markdown
   !!! warning "Skjema-spesifikke taggar"
       Generelle release-taggar (`v1.0.0`, `v1.1.0`) peikar til ein spesifikk commit, men garanterer **ikkje** at alle skjemafiler finst i den commiten. Bruk **skjema-spesifikke taggar** (t.d. `dcat-ap-no-v2.0.0`, `common-ap-no-v1.0.0`) for stabile import-URL-ar.
   ```

## Handlingsliste

- [x] Endre import-døme i README.md
- [x] Endre bootstrap-døme og import-døme i mkdocs/docs/ekstern-bruk.md
- [x] Endre kommentarar i bootstrap.sh
- [x] Legg til advarsel om skjema-spesifikke taggar i ekstern-bruk.md
- [x] Verifiser at alle døme no fungerer (sjekk URL-ar mot GitHub raw)

## Utført

**Oppdaga detalj under implementasjonen:**
Katalogstrukturen for `common-ap-no` endra seg mellom `v1.0.0` (som hadde `src/linkml/ap-no/common/`) og seinare versjonar (som har `src/linkml/ap-no/common-ap-no/`). Dette er ein ekstra grunn til å **alltid bruke skjema-spesifikke taggar** — dei garanterer både at fila finst og at stien er korrekt.

**Endringar gjort:**
1. **bootstrap.sh** (linje 3-7): Endra døme frå `v1.0.0` til `main`
2. **README.md** (linje 151): Endra import-døme frå `v1.0.0` til `dcat-ap-no-v2.8.0`
3. **mkdocs/docs/ekstern-bruk.md**:
   - Bootstrap-døme (linje 22-23): Endra frå `v1.0.0` til `main` med `AP_NO_VERSION=dcat-ap-no-v2.8.0`
   - Import-døme (linje 61): Endra frå `v1.0.0` til `dcat-ap-no-v2.8.0`
   - Import-døme (linje 78): Endra frå `v2.0.0` til `dcat-ap-no-v2.8.0`
   - `ap-no-version`-tabell (linje 140-151): Endra frå `v1.0.0` til `latest` og `dcat-ap-no-v2.8.0`
   - Advarselsboks (linje 86-89): Lagt til advarsel om skjema-spesifikke taggar
   - Image-taggar (linje 213): Oppdatert beskrivelse

**Verifisert:**
- `dcat-ap-no-v2.8.0`-URL: ✅ 200 OK
- `common-ap-no-v1.0.0`-URL: ✅ 200 OK
- `v1.0.0` med ny katalogstruktur: ❌ Feil sti (årsak til buggen)
