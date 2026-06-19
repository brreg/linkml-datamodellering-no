# Plan: DRY-prinsipp i CLAUDE.md og repoet

**Kortnamn:** `dry-prinsipp-claude-md`  
**Dato:** 2026-06-19  

---

## Bakgrunn

DRY (Don't Repeat Yourself) tyder at kvar bit av kunnskap skal ha éi, eintydleg
kjelde i systemet. Duplikat betyr to stader å oppdatere — og to stader å gløyme.

Repoet har allereie DRY innbakt i LinkML-importhierarkiet (klasser og slots vert
importerte, ikkje kopierte), men prinsippet er ikkje eksplisitt formulert i
`CLAUDE.md`. Utan ei formulert regel er det uklårt for AI-assistenten kva
abstraksjonsnivå som er rett, og risikoen for at innhald vert duplisert aukar.

---

## Kva DRY tyder i dette repoet

DRY er eit prinsipp, ikkje ein absoluttverdi. Det skal brukast med skjøn:

| Domene | DRY-regel | Unntak |
|--------|-----------|--------|
| **LinkML-skjema** | Klasser og slots definerast éin stad; andre importerer | Range-overridar i `slot_usage` er tillatne lokalt |
| **Makefile** | Kommandoar som vert repeterte 3+ gongar vert Make-variablar eller -makroar | Eingangskommandoar treng inga abstraksjon |
| **CLAUDE.md** | Reglar formulerast éin stad; kryssreferansar til specs/docs framfor gjentak | Korte døme som gjer regelen klar er tillatne |
| **specs/** | Bakgrunn som allereie er dokumentert i CLAUDE.md eller docs/ vert referert, ikkje kopiert | Spesifikasjonar treng nok kontekst til å stå åleine |
| **mkdocs/docs/** | Same innhald vert ikkje duplisert mellom fleire portalsider | Korte samanfatningar som lenkar vidare er OK |

**Grense:** Tre like linjer er betre enn ei for tidleg abstraksjon. DRY skal
ikkje trigge refaktorering av to-tre liknande tilfelle — berre klare, reelle
duplikat med vedlikehaldskostnad.

---

## Konsekvensar av å innføre DRY som eksplisitt regel

### Positive konsekvensar

1. **Éi sannkjelde per regel.** Endringar i t.d. prefix-tabellar, annotasjons-
   krav eller slotnamn-konvensjonar krev berre éi oppdatering — ikkje fleire stader i CLAUDE.md.
2. **Mindre risiko for inkonsekvens.** I dag kan ei oppdatering i éin del av
   CLAUDE.md overstyrast av ei gløymt duplisering lenger ned.
3. **Klarare forventning til AI-assistenten.** Eksplisitt regel gjer det mogleg
   å gi konkret instruksjon om kva som skal importerast kontra definerast lokalt
   i LinkML-kontekst.
4. **Lågare kognitiv last.** Brukar og AI treng ikkje halde to stader i hovudet
   samstundes.

### Negative konsekvensar og risikoar

1. **Import = kopling = potensielle brotande endringar.**  
   DRY i LinkML-skjema tyder at ei endring i eit delt skjema (t.d. `common-ap-no`)
   propagerer ned til alle importerande domenemodeller. Risikoen er reell:
   ein navneendring på ein slot kan krevje oppdatering i 10+ skjema.  
   **Mottak:** Bevar eksisterande importhierarki og stabiliser grensesnitt
   — ikkje flytt klasser til delt skjema utan tydeleg gevinst.

2. **Over-abstraksjon av Makefile.**  
   Make-makroar er vanskelege å feilsøkje samanlikna med eksplisitte kommandoar.
   Innføring av DRY her kan gjere `Makefile` vanskelegare å lese.  
   **Mottak:** Berre abstraher kommandoar som er repeterte 3+ gongar og
   som aldri bør divergere.

3. **specs/ treng nok kontekst til å stå åleine.**  
   Spesifikasjonar vert leste isolert og treng bakgrunn sjølv om han finst i
   CLAUDE.md. Streng DRY ville gi kryptiske specs som berre seier «sjå CLAUDE.md».  
   **Mottak:** Regelen gjeld ikkje specs/ som står åleine — berre
   CLAUDE.md-intern duplisering og mkdocs-portalen.

4. **Risiko for at AI-assistenten over-tolkar regelen.**  
   Utan presisering kan ein DRY-instruksjon få AI-assistenten til å refaktorere
   fungerande kode unødig («DRY-patrol»).  
   **Mottak:** Formuler regelen med eksplisitt terskel («3+ identiske tilfelle»)
   og knytt han til domenene det gjeld.

5. **CLAUDE.md vert eit knutepunkt med mange peikarar.**  
   Viss CLAUDE.md vert full av «sjå X», kan det vere vanskelegare å orientere
   seg enn om innhaldet er gjenteke.  
   **Mottak:** Berre bruk kryssreferanse der dokumentet det vert peika til
   er autoritativt og stabilt (t.d. `specs/done/`, `src/mcp-linkml-validator/policies/README.md`).

---

## Konkrete funn: kvar er DRY-problem i dag?

### F1 — prefix-tabellen er nær duplisert

Prefix-tabellen i CLAUDE.md (`## Standardprefix`) og prefix-blokka som
genererast av `mcp-linkml-modell-utkast` er semantisk like. Ei endring
i CLAUDE.md vert ikkje automatisk reflektert i generatoren.

**Tilråding:** Dokumenter i CLAUDE.md at generatoren er sannkjelda for
genererte prefix, og at CLAUDE.md-tabellen gjeld menneskeskrivne skjema.

### F2 — silver-annotasjonar er dokumenterte to stader

`## Silver-annotasjonar` i CLAUDE.md og `src/mcp-linkml-validator/policies/README.md`
overlapper. Tabellane er ikkje identiske, men omhandlar same tema.

**Tilråding:** CLAUDE.md-seksjonen behaldar brukarvenleg oversikt;
README.md i validator er sannkjelda for presise feltnamn og gyldige verdiar.
Legg til kryssreferanse i CLAUDE.md.

### F3 — containerklasse-konvensjon er forklart to stader

Containerklasse-konvensjonen er dokumentert både under `## Modelleringsprinsipper`
og i `mkdocs/docs/ny-domenemodell.md`. Avvik mellom desse er ein potensiell kilde
til forvirring.

**Tilråding:** `mkdocs/docs/ny-domenemodell.md` er normativ kjelde for
steg-for-steg-prosedyren for å opprette ein ny domenemodell. CLAUDE.md skal
ikkje duplisere dette innhaldet — berre lenke til sida.

### F4 — LinkML-skjema: duplikate klasser er allereie løyste

MC8-MC11 (sjå `specs/done/avvik-modelldcat-ap-no.md`) fjerna dupliserte klasser
og slots mellom AP-NO-profil-skjemaa. Dette er eit døme på vellukka DRY i praksis.

**Tilråding:** Ingen ny handling — bruk dette som referanseeksempel i CLAUDE.md.

---

## Steg

### DRY1 — Formuler DRY-prinsippet i CLAUDE.md

**Fil:** `CLAUDE.md`

Legg til ein ny regel under `## Førande prinsipper`:

```
- **DRY — ikkje gjenta deg sjølv:** Kvar regel, klasse, slot og kommando skal
  ha éi kjelde. I LinkML-skjema: definer klasser/slots éin stad og importer.
  I CLAUDE.md: ikkje gjenta forklåringar som finst i `mkdocs/docs/` — legg til
  kryssreferanse i staden. Terskel: tre eller fleire identiske tilfelle. To like
  tilfelle krev ingen abstraksjon. `specs/done/` er unntatt — arkiverte
  spesifikasjonar skal stå urørte og treng ikkje konsoliderast. Omskriv aldri
  eksisterande kode eller konfigurasjon med DRY som einaste grunngjeving utan
  å spørje brukaren om løyve først.
```

### DRY2 — Legg til kryssreferanse til validator-README frå silver-seksjonen

**Fil:** `CLAUDE.md` (seksjonen `## Silver-annotasjonar`)

Legg til ei linje under tabellen:

```
Sjå `src/mcp-linkml-validator/policies/README.md` for komplett feltliste og gyldige verdiar.
```

### DRY3 — Presiser ansvarsfordeling mellom CLAUDE.md og mkdocs

**Fil:** `CLAUDE.md` (seksjonen `## Dokumentasjonsportal`)

Legg til ei setning som klargjerer at CLAUDE.md er normativ kjelde for
modelleringsreglar, og at `mkdocs/docs/` er brukarvendt dokumentasjon som
kan samanfatte men ikkje erstatte reglane i CLAUDE.md.

### DRY4 — Legg til referanseeksempel for DRY i LinkML-skjema

**Fil:** `CLAUDE.md` (under ny DRY-regel eller `## LinkML Importhierarki`)

Vis til MC8-MC11-arbeidet som praktisk døme på kva som skjer når DRY vert brote
(duplikate klasser) og korleis det vert løyst (import).

### DRY5 — Flytt README-innhald til dokumentasjonsportalen, erstatt med lenker

**Filer:** `mkdocs/docs/ny-domenemodell.md`, `mkdocs/docs/ny-begrepsmodell.md`, `README.md`

**Rekkjefølgje:**
1. Legg til «Rask start»-seksjon øvst i `ny-domenemodell.md` med innhaldet frå `### Datamodellering` i README
2. Legg til «Rask start»-seksjon øvst i `ny-begrepsmodell.md` med innhaldet frå `### Begrepsmodellering` i README
3. Erstatt seksjonsinnhaldet i README med éi lenkjelinje til kvar side

---

#### Slik vil `ny-domenemodell.md` sjå ut (etter)

```markdown
# Rettleiing: ny domenemodell

## Rask start

> Bytt ut **`domene`** og **`modellnavn`** med dine aktuelle namn.

```bash
# 1. Lag eit nytt tomt LinkML-skjema (skjema + filstruktur)
make new-model NAME=modellnavn DOMAIN=domene

# 1b. (om ønskjeleg) Generer frå eksisterande JSON Schema
# Legg JSON Schema-filen i tmp/, t.d. tmp/modellnavn.json
make mcp-generate SCHEMA=tmp/modellnavn.json
# → genererer tmp/modellnavn-schema.yaml. Flytt ho til src/linkml/domain/modellnavn/
```
```bash
# 2. Rediger modellfila etter behov
#    → src/linkml/domain/modellnavn/modellnavn-schema.yaml
```
```bash
# 3. Valider skjema
make mcp-validate \
  SCHEMA=src/linkml/domene/modellnavn/modellnavn-schema.yaml \
  POLICY=felles-datakatalog
```
```bash
# 4. Generer artefakter og publiser til dokumentasjonsportal
make <domain> && make publish && make docs-serve   # → http://localhost:8000
```

Nye skjema under `src/linkml/<domain>/<modellnavn>/` vert oppdaga automatisk.

Sjå òg [Publiser til Felles Datakatalog](https://brreg.github.io/linkml-datamodellering-no/publisering-modell/).

---

## Arbeidsflyt

### 0 — Sjekk føresetnader og bygg images (éin gong)
...
```

---

#### Slik vil `ny-begrepsmodell.md` sjå ut (etter)

```markdown
# Rettleiing: ny begrepskatalog

## Rask start

> Bytt ut **`katalognavn`** med ditt aktuelle namn.

```bash
# 1. Opprett ny begrepskatalog (skjema + filstruktur)
make new-model NAME=katalognavn DOMAIN=begrepskatalog
```
```bash
# 2. Rediger datafila med reelle begrep
#    → src/linkml/begrepskatalog/katalognavn/data/katalognavn/katalognavn.yaml
```
```bash
# 3. Valider skjema og datafil
make mcp-validate \
  SCHEMA=src/linkml/begrepskatalog/katalognavn/katalognavn-schema.yaml \
  POLICY=felles-begrepskatalog \
  INSTANCE=src/linkml/begrepskatalog/katalognavn/data/katalognavn/katalognavn.yaml
```
```bash
# 4. Generer og publiser til dokumentasjonsportal
make begrepskatalog && make publish && make docs-serve   # → http://localhost:8000
```

Sjå òg [Publiser til Felles Begrepskatalog](https://brreg.github.io/linkml-datamodellering-no/publisering-begrep/).

---

Denne rettleiinga viser korleis du oppretter ein ny begrepskatalog i repoet —
frå filstruktur til RDF-eksport klar for Felles Begrepskatalog.

!!! note "Skil seg frå ny domenemodell"
    ...
```

---

#### Slik vil `README.md` sjå ut (etter)

```markdown
### Datamodellering

Sjå [Datamodellering](https://brreg.github.io/linkml-datamodellering-no/ny-domenemodell/) i dokumentasjonsportalen.

### Begrepsmodellering

Sjå [Begrepsmodellering](https://brreg.github.io/linkml-datamodellering-no/ny-begrepsmodell/) i dokumentasjonsportalen.

### Bruk frå eksternt repo

Sjå [Bruk frå eksternt repo](https://brreg.github.io/linkml-datamodellering-no/ekstern-bruk/) i dokumentasjonsportalen.
```

---

## Prioritert handlingsliste

| # | Tiltak | Fil | Avheng av |
|---|--------|-----|-----------|
| 1 | ✓ DRY1: Formuler DRY-prinsippet i CLAUDE.md | `CLAUDE.md` | — |
| 2 | ✓ DRY2: Kryssreferanse til validator-README | `CLAUDE.md` | DRY1 |
| 3 | ✓ DRY3: Ansvarsfordeling CLAUDE.md vs mkdocs | `CLAUDE.md` | DRY1 |
| 4 | ✓ DRY4: Referanseeksempel i CLAUDE.md | `CLAUDE.md` | DRY1 |
| 5 | ~~DRY5~~: Forkasta — sjå vurdering under tabellen | `README.md` | — |

**DRY5 — vurdering (forkasta):**

1. `ny-begrepsmodell.md` motseier README-innhaldet direkte: sida seier eksplisitt at
   `make new-model` **ikkje** gjeld for begrepskatalogar, medan README viser nettopp
   det kommandoen. Å flytte README-innhaldet inn i portalsida ville skape konflikt.
2. README og portaldokumenta tener ulike formål: README er ein kjapt oversyn for
   GitHub-besøkande; portalsidene er detaljerte rettleiingar. Dette er ulike
   målgrupper og kontekstar — ikkje utilsikta duplikasjon.
3. DRY-terskelen («tre eller fleire identiske tilfelle») er ikkje nådd — det er to
   stader med ulik funksjon.

---

## Avhengigheiter

- Ingen tekniske avhengigheiter — alle stega er dokumentasjonsoppdateringar.
- DRY i LinkML-skjema er allereie praktisert (importhierarkiet). Denne planen
  handlar berre om å formulere prinsippet eksplisitt og rette opp kjende
  dokumentasjonsduplikat.

---

## Utført

DRY1–DRY4 utførte 2026-06-19. DRY5 forkasta etter evaluering.

- **DRY1:** Ny regel `**DRY — ikkje gjenta deg sjølv:**` lagt til under `## Førande prinsipper` i CLAUDE.md. Inkluderer terskel (3+ tilfelle), unntak for `specs/done/` og krav om brukarløyve før omskriving.
- **DRY2:** Kryssreferanse til `src/mcp-linkml-validator/policies/README.md` lagt til etter silver-annotasjonstabellen i CLAUDE.md.
- **DRY3:** Setning om ansvarsfordeling mellom CLAUDE.md (modelleringsprinsipp/AI-instruksjonar) og `mkdocs/docs/` (brukarvendt/steg-for-steg) lagt til under `## Dokumentasjonsportal`.
- **DRY4:** Referanseeksempel (MC8–MC11, `specs/done/avvik-modelldcat-ap-no.md`) lagt til under `## LinkML Importhierarki`.
- **DRY5:** Forkasta — README og portaldokument tener ulike formål; `ny-begrepsmodell.md` motseier README-kommandoane direkte.
