# Monitorering av automasjon

Denne sida forklarar korleis du kan monitorere at generering og publisering av artefaktar fungerer som forventa.

---

## GitHub Actions-loggar (primær monitorering)

I PoC-fasen er **GitHub Actions-loggar** den primære monitoreringsmekanismen.

### Kvar finn eg loggane?

**Hovudoversikt over alle workflows:**
```
https://github.com/brreg/linkml-datamodellering-no/actions
```

**Spesifikke workflows:**

| Workflow | URL | Kva det gjer |
|---|---|---|
| `generate.yml` | [actions/workflows/generate.yml](https://github.com/brreg/linkml-datamodellering-no/actions/workflows/generate.yml) | Validerer, genererer artefaktar og publiserer til GitHub Pages |
| `validate.yml` | [actions/workflows/validate.yml](https://github.com/brreg/linkml-datamodellering-no/actions/workflows/validate.yml) | Validerer skjema og datafiler ved PR |
| `release-please.yml` | [actions/workflows/release-please.yml](https://github.com/brreg/linkml-datamodellering-no/actions/workflows/release-please.yml) | Opprettar release-PR og publiserer releases |
| `release.yml` | [actions/workflows/release.yml](https://github.com/brreg/linkml-datamodellering-no/actions/workflows/release.yml) | Byggjer og pushar container-images ved release |

### Kva viser loggane?

**`generate.yml` (viktigaste workflow):**

1. **Validering:**
   - `make lint` — LinkML-schema lint
   - `make mcp-validate` — Policy-validering (bronze/silver/gold/felles-begrepskatalog/felles-datakatalog)
   - `make validate-instance` — Instansvalidering av eksempelfiler

2. **Generering:**
   - `make <domain>` — Genererer SHACL, JSON Schema, OWL, Python, Protobuf, dokumentasjon, diagram
   - `make convert-data` — Konverterer YAML til SKOS/Turtle og ModelDCAT-AP-NO

3. **Publisering:**
   - `make publish` — Regenererer mkdocs-portal
   - `actions/deploy-pages@v1` — Publiserer til GitHub Pages

**Eksempel på vellukka køyring:**
```
✓ lint (ngr-virksomhet)
✓ mcp-validate POLICY=bronze
✓ generate ngr
✓ publish
✓ Deploy to GitHub Pages
```

**Eksempel på feila køyring:**
```
✗ mcp-validate POLICY=felles-begrepskatalog
  Error: Missing required field: dct:publisher
```

### Kor lenge vert loggar lagra?

GitHub lagrar workflow-loggar i **90 dagar**. Etter det vert dei automatisk sletta.

### Korleis filtere loggar?

**Filter på branch:**
- Klikk på "Branch"-dropdown og vel `main`, `feature/mi-branch`, osv.

**Filter på status:**
- "Success" (grøn): Alt gjekk bra
- "Failure" (raud): Validering eller generering feila
- "Cancelled" (grå): Køyringa vart avbroten manuelt

**Filter på dato:**
- "Event" → "Push" / "Pull request" / "Schedule"

**Søk på commit-melding:**
- Bruk søkefeltet øvst: `feat(ngr-adresse): legg til postnummer`

### Eksempel: Sjekke siste publisering

1. Gå til https://github.com/brreg/linkml-datamodellering-no/actions/workflows/generate.yml
2. Sjekk at øvste køyringa er grøn (✓)
3. Klikk på køyringa for å sjå detaljert logg
4. Sjekk "Deploy to GitHub Pages"-steget — vellukka dersom grøn hake

---

## Verifisere publisering til GitHub Pages

Etter at `generate.yml` har køyrt vellukka, verifiser at artefaktane faktisk er publiserte til GitHub Pages.

### Hovudportal

**URL:** https://brreg.github.io/linkml-datamodellering-no/

**Kva som skal vere der:**
- MkDocs-dokumentasjonsportal
- Navigasjonsmeny med domener (AP-NO, NGR, FINT, osv.)
- Genererte skjema-sider med dokumentasjon og diagram

### Genererte artefaktar

**Eksempel — SHACL shapes for ngr-virksomhet:**
```
https://brreg.github.io/linkml-datamodellering-no/ngr/ngr-virksomhet/ngr-virksomhet-shapes.ttl
```

**Eksempel — JSON Schema:**
```
https://brreg.github.io/linkml-datamodellering-no/ngr/ngr-virksomhet/ngr-virksomhet-schema.json
```

**Eksempel — Begrepskatalog (SKOS/Turtle):**
```
https://brreg.github.io/linkml-datamodellering-no/begrepskatalog/brreg-begrepskatalog/brreg-begrepskatalog.ttl
```

### Verifisere at fila er oppdatert

**Manuell sjekk:**

```bash
curl -I https://brreg.github.io/linkml-datamodellering-no/ngr/ngr-virksomhet/ngr-virksomhet-schema.json
```

Sjekk `Last-Modified`-headeren:
```
Last-Modified: Sun, 29 Jun 2026 14:32:15 GMT
```

**Alternativ — sjekk i nettlesar:**
1. Opne URL-en i nettlesar
2. Høgreklikk → "Inspiser" → "Network"-fanen
3. Refresh (F5)
4. Sjekk `Last-Modified` eller `Date`-headeren

### Verifisere at høstingsendepunkt er tilgjengelege eksternt

**Test at TTL-filer er tilgjengelege for Felles Begrepskatalog/Datakatalog:**

```bash
curl -H "Accept: text/turtle" https://brreg.github.io/linkml-datamodellering-no/begrepskatalog/brreg-begrepskatalog/brreg-begrepskatalog.ttl
```

Dersom du får tilbake Turtle-data (startar med `@prefix`), fungerer høstingsendepunktet.

---

## Framtidige monitoreringsalternativ

Desse alternativa kan leggjast til etter behov, men er **ikkje nødvendige i PoC-fasen**.

### 1. GoatCounter (besøksstatistikk)

**Kva:** Privacy-venleg, GDPR-compliant, open source web analytics  
**Kostnad:** Gratis for open source-prosjekt  
**Implementering:** ~30 minutt

**Fordeler:**
- ✅ Ingen cookies — treng ikkje samtykke-banner
- ✅ GDPR-compliant — perfekt for offentleg sektor
- ✅ Open source
- ✅ Viser: besøk per side, referrers, land, nettlesar

**Korleis implementere:**

1. Registrer på https://www.goatcounter.com/
2. Lag ein "site" (t.d. `brreg-linkml`)
3. Legg til script-tag i MkDocs:

   **Opprett `mkdocs/docs/overrides/main.html`:**
   ```html
   {% extends "base.html" %}
   
   {% block analytics %}
     <script data-goatcounter="https://brreg-linkml.goatcounter.com/count"
             async src="//gc.zgo.at/count.js"></script>
   {% endblock %}
   ```

   **Oppdater `mkdocs/mkdocs.yml`:**
   ```yaml
   theme:
     name: material
     custom_dir: docs/overrides
   ```

4. Push til `main` og vent på at GitHub Pages oppdaterar seg

**Dashboard:** https://brreg-linkml.goatcounter.com/

### 2. UptimeRobot (uptime-monitorering)

**Kva:** Overvaker at GitHub Pages er oppe og tilgjengeleg  
**Kostnad:** Gratis tier (50 monitors, 5-minutts intervall)

**Fordeler:**
- ✅ E-postvarsel dersom sida går ned
- ✅ Historikk over uptime (99.9%, osv.)
- ✅ Gratis for grunnleggjande behov

**Korleis implementere:**

1. Registrer på https://uptimerobot.com/
2. Legg til ny monitor:
   - **Monitor Type:** HTTP(s)
   - **Friendly Name:** LinkML Datamodellering Portal
   - **URL:** `https://brreg.github.io/linkml-datamodellering-no/`
   - **Monitoring Interval:** 5 minutt
3. Legg til e-postadresse for varsel

**Bruk:** Automatisk varsel dersom GitHub Pages er nede

### 3. RSS-feed for releases

**Kva:** GitHub genererer automatisk RSS-feed for releases

**URL:**
```
https://github.com/brreg/linkml-datamodellering-no/releases.atom
```

**Bruk:**
- Abonner i RSS-lesar (Feedly, Inoreader, osv.)
- Få varsel når ny versjon vert publisert

---

## Avgrensingar

### Kva repoet IKKJE kan monitorere

1. **Om Felles Begrepskatalog/Datakatalog faktisk høstar data**
   - Høsting skjer eksternt (Digitaliseringsdirektoratet sitt ansvar)
   - Repoet har ingen API-tilgang til data.norge.no
   - Må sjekkas manuelt på https://data.norge.no/concepts eller https://data.norge.no/models

2. **Besøksstatistikk på data.norge.no**
   - Statistikk frå data.norge.no er ikkje tilgjengeleg for oss
   - Krev tilgang til Digitaliseringsdirektoratet sine analyseverkty

3. **Feilloggar frå eksterne system**
   - Dersom Felles Begrepskatalog feiler under høsting, får vi ikkje varsel
   - Må kontakte Digitaliseringsdirektoratet ved mistanke om problem

### Kva du må gjere manuelt

**Verifisere at data faktisk er synleg på data.norge.no:**

1. **Begrepskatalogar:**
   - Gå til https://data.norge.no/concepts
   - Søk på eit begrep frå din katalog (t.d. "foretaksnavn")
   - Verifiser at det visast med rett utgjevar og definisjon

2. **Modellkatalogar:**
   - Gå til https://data.norge.no/models
   - Søk på din modell (t.d. "Nasjonale grunndata – Virksomhet")
   - Verifiser at den visast med rett metadata

**Kontakt Digitaliseringsdirektoratet dersom:**
- Data er publisert til GitHub Pages (verifisert)
- Men ikkje visast på data.norge.no etter 24-48 timar
- E-post: dataopen@digdir.no

---

## Sjå òg

- [Publiser til Felles Begrepskatalog](publisering-begrep.md) — rettleiing for begrepskatalogar
- [Publiser til Felles Datakatalog](publisering-modell.md) — rettleiing for modellkatalogar
- [Arkitektur-oversikt](arkitektur-oversikt.md) — publiseringsflyt frå repo til eksterne katalogar
- [GOVERNANCE.md](https://github.com/brreg/linkml-datamodellering-no/blob/main/GOVERNANCE.md) — publiseringspolicy
