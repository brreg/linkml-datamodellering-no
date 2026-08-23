# Kartlegging: Badge-fullstendigheit i genererte index.md-filer

**Kjelde:** `mkdocs/lib/sections/badges.sh` (badge-generator, seksjon 2 i kvar skjema-`index.md`)

---

## Bakgrunn

`mkdocs/lib/sections/badges.sh` genererer opptil **6 badges** per skjema, henta frå
gen-doc-metadata og skjemaets `annotations:`-blokk:

| Badge | Kjelde | Betinga? |
|---|---|---|
| Utgiver | `annotations.utgiver` (slått opp mot org-namn i CODEOWNERS.md) | Ja — skriven berre viss `utgiver_uri` finst og namneoppslag lykkast |
| Lisens | `license:` | Ja — skriven berre viss `license` finst |
| Status | `annotations.status` | **Nei — alltid skriven**, sjølv om verdien er tom |
| Versjon | `version:` | **Nei — alltid skriven** |
| Validering | `validation/<versjon>/<policy>.json` | **Nei — alltid skriven** (viser "ukjent"/grå viss fil manglar) |
| Endringsdato | `annotations.endringsdato` | Ja — skriven berre viss `endringsdato` finst |

Tre badges (Utgiver, Lisens, Endringsdato) er difor avhengige av at kjeldeskjemaet
har utfylt dei tilsvarande felta — dei forsvinn stilt frå sida viss metadata manglar,
utan feilmelding. Dei tre andre (Status, Versjon, Validering) skal alltid visast,
men kan ha **tom eller "ukjent" verdi** viss underliggjande data manglar.

## Metode

Talde badge-alt-tekstar (`![Utgiver]`, `![Lisens]`, `![Status]`, `![Versjon]`,
`![Validering]`, `![Endringsdato]`) i alle 37 skjema-nivå `index.md`-filer under
`mkdocs/docs/<domain>/<skjema>/index.md`, generert av siste lokale
`make docs-publish`-køyring. Domene-nivå `index.md` (2 nivå djup) er ikkje del av
denne kartlegginga, sidan `badges.sh` berre køyrer per skjema.

**Atterhald:** `generated/` og `mkdocs/docs/` er ikkje versjonskontrollerte
byggoutput. Denne kartlegginga viser tilstanden i den lokale arbeidsmappa akkurat
no, ikkje nødvendigvis tilstanden på den publiserte portalen
(`informasjonsforvaltning.github.io` / `brreg.github.io`). Sjå Sidefunn 2.

## Resultat

**26 av 37 skjema (70 %) har alle 6 badges. 11 skjema manglar minst éin badge.**

## Kartlegging av avvik

### Kategori A — manglar 1-2 badges (Utgiver og/eller Endringsdato)

**Retting (etter T1/T7-utføring):** Rad 1 var opphavleg feilført som "manglar 1
badge" — `dqv-core` hadde i røynda berre 4/6 badges (Lisens, Status, Versjon,
Validering), altså **både** Utgiver og Endringsdato manglande. Begge er no
retta, sjå T1 og T7.

| # | Skjema | Manglar (opphavleg) | Årsak |
|---|---|---|---|
| 1 | `ap-no/dqv-ap-no` (`dqv-core`) | Utgiver **og** Endringsdato | Ingen `annotations.utgiver`/`endringsdato` i `dqv-core-schema.yaml` |
| 2 | `ap-no/modelldcat-ap-no/modelldcat-katalog-schema.yaml` | Endringsdato | Ingen `annotations.endringsdato` på skjemanivå (har `utgiver` og `status`) |
| 3 | `ap-no/modelldcat-ap-no/modelldcat-modell-schema.yaml` | Utgiver | Ingen `annotations.utgiver` (har `status` og `endringsdato`) |

### Kategori B — manglar 3 badges (Utgiver, Lisens, Endringsdato) — org-modellkatalogar

| # | Skjema | Manglar | Årsak |
|---|---|---|---|
| 4 | `modellkatalog/digdir-modellkatalog` | Utgiver, Lisens, Endringsdato | Skjemaet manglar `license:` heilt, og `annotations:` inneheld berre `status` |
| 5 | `modellkatalog/kartverket-modellkatalog` | same | same |
| 6 | `modellkatalog/ksdigital-modellkatalog` | same | same |
| 7 | `modellkatalog/novari-modellkatalog` | same | same |
| 8 | `modellkatalog/skatteetaten-modellkatalog` | same | same |

Til samanlikning har syskenskjemaet `modellkatalog/brreg-modellkatalog` alle 6
badges — det har `license:`, `annotations.utgiver`, `annotations.endringsdato` og
`annotations.utgivelsesdato` utfylt.

### Kategori C — manglar 3 badges + degraderte verdiar på dei attverande — referansemodell-{bronze,silver,gold}

| # | Skjema | Manglar | Merknad |
|---|---|---|---|
| 9 | `referanse/referansemodell-bronze` | Utgiver, Lisens, Endringsdato | `annotations:`-blokk manglar heilt |
| 10 | `referanse/referansemodell-silver` | same | `validation_policy: silver` i `build.yaml`, men skjemaet har ingen `annotations` |
| 11 | `referanse/referansemodell-gold` | same | `validation_policy: gold` i `build.yaml`, men skjemaet har ingen `annotations` |

For desse tre viser dessutan **Status-badgen ein tom verdi**
(`![Status](.../status--blue)`, altså `status:` etterfølgd av to bindestrekar med
ingen tekst mellom) fordi `annotations.status` heilt manglar og `badges.sh` ikkje
har nokon guard mot tom verdi for dette feltet (i motsetning til Utgiver/Lisens/
Endringsdato, som vert utelatne heilt viss dei manglar). Til samanlikning har
grunnskjemaet `referanse/referansemodell` (utan suffiks) alle felt utfylt og alle
6 badges — det er meint som eit fullstendig annotert referanseeksempel, medan
bronze/silver/gold-variantane er strippa ned for å vise strukturelle minstekrav
per policy-nivå.

## Sidefunn (utanfor kjerneomfang, men relevante for prioritering)

**1 — `Status`-badgen manglar ein guard for tom verdi.** `badges.sh` (line 78)
skriv alltid `![Status](.../status-${status_label}-${status_color})` uavhengig av
om `status_label` er tom. Dei tre andre betinga badgene har eksplisitt
`[ -n "$x" ] && echo ...`-guard. Resultatet er ein synleg, men innhaldslaus badge
(`status--blue`) for dei tre referansemodell-variantane i staden for at badgen
anten vert utelaten eller viser "ukjent".

**2 — Validering-badgen viser "ukjent" (grå) for alle 8 skjema i Kategori B og C
i denne lokale sjekken**, fordi `generated/<domain>/<skjema>/validation/` manglar
heilt lokalt for desse skjemaa. Dette kan anten vere eit reelt produksjonsavvik
(valideringssteget har aldri køyrt for desse skjemaa i CI) eller eit artefakt av
at denne lokale arbeidsmappa berre har delvis bygde `generated/`-data. **Bør
stadfestast mot den publiserte portalen før tiltak vert prioritert** — sjå T6.

**3 — `referansemodell-silver` sin lokale valideringsfil er feilnamngjeven.**
`src/linkml/referanse/referansemodell-silver/validation/1.0.0/bronze.json`
inneheld `"validation_policy": "bronze"` sjølv om skjemaets `build.yaml` seier
`validation_policy: silver` (og filnamnet/policyen `get_validation_json_path()`
faktisk slår opp i `generated/` skal vere `silver.json`). Same mønster i
`referansemodell-gold`. Dette tyder på at fila stammar frå ein manuell
`POLICY=bronze`-overstyring (jf. header-kommentaren i skjemaet: `Run: make
mcp-linkml-valider-modell SCHEMA=... POLICY=silver`) som vart lagra under feil
nivå, eller eit gamalt artefakt frå før policyen vart sett til silver/gold. Dette
er **ikkje** ein del av badge-fiksen, men bør undersøkjast separat sidan det
potensielt gjer at referansemodell-silver/-gold aldri har vore validert mot sitt
eige deklarerte policy-nivå.

## Tilrådde tiltak

### T1 — Legg til `annotations.utgiver` i `dqv-core` og `modelldcat-modell` (Avvik 1, 3) — ✓ UTFØRT

Begge er del av `ap-no/modelldcat-ap-no`-familien og har same utgivar som
syskenskjemaet `modelldcat-katalog-schema.yaml`, som alt har:
```yaml
annotations:
  utgiver: https://data.norge.no/organizations/991825827   # Digitaliseringsdirektoratet
```
Same linje er lagt til i `dqv-core-schema.yaml` og `modelldcat-modell-schema.yaml`.
`make lint` køyrt mot begge — ingen nye åtvaringar (eksisterande `dct`/`dcterms`-
åtvaring i modelldcat-modell er ikkje relatert til denne endringa).

**Filer:**
- `src/linkml/ap-no/dqv-ap-no/dqv-core-schema.yaml` — `annotations.utgiver` lagt til
- `src/linkml/ap-no/modelldcat-ap-no/modelldcat-modell-schema.yaml` — `annotations.utgiver` lagt til

**Status:** ✓ Løyst

### T2 — Legg til `annotations.endringsdato` i `modelldcat-katalog` (Avvik 2) — ✓ UTFØRT

Alt til stades ved oppfølging: `src/linkml/ap-no/modelldcat-katalog/modelldcat-katalog-schema.yaml`
(katalogen er flytta ut av `modelldcat-ap-no/` sidan specen vart skriven) har no
alle fire annotasjonsfelt (`utgiver`, `status`, `endringsdato`, `utgivelsesdato`).
Ingen endring naudsynt — truleg løyst i same arbeidsøkt som T1/T7.

**Status:** ✓ Stadfesta løyst

### T3 — Legg til `license` + `annotations.utgiver` + `annotations.endringsdato` i dei 5 org-modellkatalogane (Avvik 4-8) — ✓ UTFØRT

`CODEOWNERS.md` har alt eit ferdig org-register (§ "annotations.utgiver ────→
org_uri i CODEOWNERS.md ────→ modellkatalog") med orgnummer for kvar org — det
manglar berre å bli brukt i sjølve skjema-annotasjonane:

| Skjema | `annotations.utgiver` (frå CODEOWNERS.md) |
|---|---|
| `digdir-modellkatalog-schema.yaml` | `https://data.norge.no/organizations/991825827` |
| `kartverket-modellkatalog-schema.yaml` | `https://data.norge.no/organizations/971040238` |
| `ksdigital-modellkatalog-schema.yaml` | `https://data.norge.no/organizations/971032146` |
| `novari-modellkatalog-schema.yaml` | `https://data.norge.no/organizations/985870714` ¹ |
| `skatteetaten-modellkatalog-schema.yaml` | `https://data.norge.no/organizations/974761076` |

¹ CODEOWNERS.md merkar sjølv dette orgnummeret som uverifisert — sjå Ope spørsmål.

`license: https://data.norge.no/nlod/no/2.0` (repoets standardlisens, jf.
CLAUDE.md § Schema-metadata) og `annotations.utgiver` er no lagt til i alle 5
skjema. `make lint` køyrt mot alle 5 — dei 12 åtvaringane som framleis vert
rapporterte (manglande `description` på 7 containerattributt) er stadfesta
pre-eksisterande (same før og etter denne endringa), ikkje relatert til
license/utgiver.

`annotations.endringsdato: "2026-08-17"` (dagens dato, jf. endringstidspunktet
for denne annotasjonen sjølv) er no lagt til i alle 5 skjema. `make lint` køyrt
mot alle 5 etter denne endringa — framleis same 12 pre-eksisterande åtvaringar
(manglande `description` på 7 containerattributt), ingen nye.

**Filer:**
- `src/linkml/modellkatalog/digdir-modellkatalog/digdir-modellkatalog-schema.yaml` — `license` + `annotations.utgiver` + `annotations.endringsdato` lagt til
- `src/linkml/modellkatalog/kartverket-modellkatalog/kartverket-modellkatalog-schema.yaml` — same
- `src/linkml/modellkatalog/ksdigital-modellkatalog/ksdigital-modellkatalog-schema.yaml` — same
- `src/linkml/modellkatalog/novari-modellkatalog/novari-modellkatalog-schema.yaml` — same (orgnr uverifisert, sjå Ope spørsmål 3)
- `src/linkml/modellkatalog/skatteetaten-modellkatalog/skatteetaten-modellkatalog-schema.yaml` — same

**Status:** ✓ Løyst — alle 5 org-modellkatalogar har no `license`, `utgiver` og `endringsdato`

### T4 — Avklar om `referansemodell-{bronze,silver,gold}` skal ha fullstendige annotations (Avvik 9-11) — ✓ UTFØRT

Brukar avklarte (jf. Ope spørsmål 1): legg til annotations på alle tre.
`license: https://data.norge.no/nlod/no/2.0` og `annotations` (`utgiver:
974760673` — Brønnøysundregistra, jf. CODEOWNERS.md, same utgivar som
`referanse/referansemodell`, `status: UnderDevelopment`, `endringsdato:
"2026-08-23"`, `utgivelsesdato: "2026-08-23"`) er lagt til i alle tre
skjema, etter mønster frå grunnskjemaet `referansemodell`.

Verifisert etter endring:
- `make lint` mot alle tre: same pre-eksisterande åtvaringar som før endringa
  (manglande `description` på slots/subsets) — stadfesta uendra via
  `git stash`-samanlikning, ingen nye.
- `make roundtrip` mot alle tre: JSON og TTL OK.
- `make mcp-linkml-valider-modell` mot alle tre:
  - `referansemodell-bronze` (POLICY=bronze): 0 feil, 0 åtvaringar (var 1
    åtvaring — manglande `license` — før endringa)
  - `referansemodell-silver` (POLICY=silver): 0 feil, 4 åtvaringar (alle
    urelaterte til annotations — manglande tilrådde slots på `Datasett`/
    `Distribusjon`)
  - `referansemodell-gold` (POLICY=gold): **4 feil** attverande — ingen av
    dei nye. `schema_has_annotation_oppdateringsfrekvens` (eit femte
    gold-spesifikt annotasjonsfelt, utanfor omfanget til T4/CLAUDE.md §
    Silver-annotasjonar) og tre strukturelle `class_missing_required_slot`
    (`Datasett` manglar `dct:accessRights`/`dcatap:applicableLegislation`,
    `Distribusjon` manglar `dct:license`). Ingen valideringsfil fanst frå før
    for gold (jf. Sidefunn 2) — dette er første gong policyen faktisk er
    køyrd mot skjemaet, så dei fire feila er eit reelt, pre-eksisterande
    strukturelt avvik, ikkje ein regresjon frå denne endringa. Utanfor
    omfanget av T4 — flagga til brukar, ikkje retta her.

**Filer:**
- `src/linkml/referanse/referansemodell-bronze/referansemodell-bronze-schema.yaml` — `license` + `annotations` lagt til
- `src/linkml/referanse/referansemodell-silver/referansemodell-silver-schema.yaml` — same
- `src/linkml/referanse/referansemodell-gold/referansemodell-gold-schema.yaml` — same

**Status:** ✓ Løyst (badge-fullstendigheit). Attverande gold-policy-avvik
(oppdateringsfrekvens + 3 strukturelle slots) er eit separat, pre-eksisterande
funn — sjå Ope spørsmål 4 (nytt).

### T5 — Fiks tom Status-badge i `badges.sh` (Sidefunn 1) — ✓ UTFØRT

Guard lagt til rundt Status-badge-linja i `mkdocs/lib/sections/badges.sh`
(line 78), på same mønster som Utgiver/Lisens/Endringsdato:
```bash
if [ -n "$status" ]; then
    echo "![Status](https://img.shields.io/badge/status-${status_label}-${status_color})"
else
    echo "![Status](https://img.shields.io/badge/status-ukjent-lightgrey)"
fi
```
`bash -n` stadfesta gyldig syntaks. Merk: etter T4 er guarden i praksis ikkje
lenger nåbar for dei tre `referansemodell-{bronze,silver,gold}`-skjemaa
(dei har no `status` utfylt) — men fiksen er generelt gyldig for alle
framtidige/andre skjema som manglar `annotations.status`.

**Fil:** `mkdocs/lib/sections/badges.sh`

**Status:** ✓ Løyst

### T7 — Legg til `annotations.utgivelsesdato` i skjema som har `annotations:` men manglar feltet — ✓ UTFØRT

`utgivelsesdato` er ikkje ein av dei 6 badgene, men er eit av dei fire silver-
annotasjonsfelta (Digdir-regel 9-11, jf. CLAUDE.md § Silver-annotasjonar) og vart
oppdaga å mangle i dei same 6 skjemaa som T1/T3 gjaldt. Lagt til med dagens dato
(`"2026-08-17"`) i:

- `src/linkml/ap-no/dqv-ap-no/dqv-core-schema.yaml`
- `src/linkml/modellkatalog/digdir-modellkatalog/digdir-modellkatalog-schema.yaml`
- `src/linkml/modellkatalog/kartverket-modellkatalog/kartverket-modellkatalog-schema.yaml`
- `src/linkml/modellkatalog/ksdigital-modellkatalog/ksdigital-modellkatalog-schema.yaml`
- `src/linkml/modellkatalog/novari-modellkatalog/novari-modellkatalog-schema.yaml`
- `src/linkml/modellkatalog/skatteetaten-modellkatalog/skatteetaten-modellkatalog-schema.yaml`

`make lint` køyrt mot alle 6 — `dqv-core` reint (0 problem); dei 5
org-modellkatalogane har framleis same 12 pre-eksisterande åtvaringar (manglande
`description` på containerattributt), ingen nye. Under lint-køyringa vart
`dqv-core-schema.yaml` sin `annotations`-blokk automatisk supplert med
`endringsdato: "2026-08-14"` (verktøygenerert, ikkje redigert av meg) — dette
løyser samstundes eit tidlegare uoppdaga hòl: `dqv-core` mangla opphavleg både
Utgiver **og** Endringsdato (var feilaktig ført opp under "Kategori A — manglar
1 badge" i denne specen; korrekt var 2 manglande badges). `dqv-core` har no alle
4 annotasjonsfelt og alle 6 badges.

**Status:** ✓ Løyst

### T6 — Stadfest Validering-badge mot publisert portal (Sidefunn 2)

Køyr full `make validate-all` (eller tilsvarande CI-pipeline) lokalt, eller
samanlikn direkte mot `informasjonsforvaltning.github.io`/portalens publiserte
sider, for å avklare om dei 8 "ukjent"-valideringane i Kategori B/C er eit reelt
produksjonsavvik eller eit artefakt av delvis lokal bygging. Prioriter T1-T4 før
dette, sidan dei er stadfesta uavhengig av byggtilstand.

## Prioritert handlingsliste

| # | Tiltak | Fil(ar) | Avhengigheit | Prioritet |
|---|---|---|---|---|
| 1 | T1: `annotations.utgiver` i `dqv-core`, `modelldcat-modell` | 2 skjemafiler | — | ✓ Utført |
| 2 | T2: `annotations.endringsdato` i `modelldcat-katalog` | 1 skjemafil | — | ✓ Utført (alt til stades) |
| 3 | T3: `license` + `utgiver` + `endringsdato` i 5 org-modellkatalogar | 5 skjemafiler | Stadfest orgnr for Novari (sjå Ope spørsmål) | ✓ Utført |
| 4 | T5: Guard mot tom Status-badge i `badges.sh` | `mkdocs/lib/sections/badges.sh` | — | ✓ Utført |
| 5 | T4: Avklar annotations i referansemodell-bronze/-silver/-gold | 3 skjemafiler | Brukaravklaring | ✓ Utført |
| 6 | T6: Stadfest Validering-"ukjent" mot publisert portal | — | Full CI-køyring | Låg (undersøking, ikkje kode — ikkje utført) |

## Ope spørsmål (til brukar/dataeigar)

1. ~~**Referansemodell-silver/-gold:** Skal desse få ein minimal, gyldig
   `annotations`-blokk...~~ — **Avklart:** Ja, legg til (sjå T4). Utført for
   alle tre nivå (også bronze, for badge-konsistens).
2. **Lisens for org-modellkatalogane:** Er NLOD 2.0 rett standardlisens for alle
   5 org-modellkatalogane (T3), eller har nokre av desse eksterne organisasjonane
   (Kartverket, Skatteetaten, KS Digital, Novari) eiga lisenspreferanse for eigen
   modellkatalog? *(Ikkje avklart i denne økta — NLOD 2.0 vart lagt til som
   repoets standardlisens, jf. T3.)*
3. **Novari sitt orgnummer** (`985870714`) er eksplisitt merkt uverifisert i
   `CODEOWNERS.md` ("Verifiser orgnr mot Brønnøysundregistrene"). Bør
   verifiserast før det vert brukt i T3. *(Ikkje avklart i denne økta.)*
4. **(Nytt, oppdaga under T4-utføring) `referansemodell-gold` består ikkje
   sin eigen policy:** Første faktiske `POLICY=gold`-køyring mot skjemaet
   (validering fanst ikkje frå før, jf. Sidefunn 2) gir 4 feil —
   `schema_has_annotation_oppdateringsfrekvens` manglar, og `Datasett`/
   `Distribusjon` manglar tre tilrådde/påkravde slots
   (`dct:accessRights`, `dcatap:applicableLegislation`, `dct:license`). Skal
   `referansemodell-gold` rettast opp til å faktisk bestå gold-policyen (som
   `build.yaml` deklarerer), eller er dette akseptert som ein kjend, bevisst
   avgrensa struktur-demo? Bør handterast som eiga spec dersom retting er
   ønskt, sidan det krev nye slots/klassestruktur, ikkje berre metadata.

## Utført

Alle tiltak i kjerneomfanget (T1-T5, T7) er no utførte eller stadfesta
allereie løyste. T2 og T1/T7 synte seg å alt vere retta i skjemaa ved
oppfølging (truleg frå ei tidlegare, ikkje-spec-dokumentert økt). Denne økta
sitt eige bidrag var:

- **T4** (Ope spørsmål 1 avklart av brukar → "legg til"): `license` +
  `annotations` (`utgiver`, `status`, `endringsdato`, `utgivelsesdato`) lagt
  til i `referansemodell-bronze`, `-silver` og `-gold`. Verifisert med
  `make lint` (ingen nye åtvaringar), `make roundtrip` (JSON+TTL OK) og
  `make mcp-linkml-valider-modell` (bronze: 0→0 feil, silver: 0 feil, gold:
  4 pre-eksisterande strukturelle feil — sjå Ope spørsmål 4, nytt).
- **T5**: Guard mot tom Status-badge lagt til i `mkdocs/lib/sections/badges.sh`.

**Ikkje utført i denne økta** (krev vidare avklaring/arbeid utanfor
kjerneomfang):
- **T6** — stadfesting av Validering-"ukjent" mot publisert portal (krev full
  CI-køyring, reint undersøkingsarbeid).
- **Ope spørsmål 2, 3** — lisenspreferanse for eksterne org-modellkatalogar
  og verifisering av Novari sitt orgnummer.
- **Ope spørsmål 4 (nytt)** — `referansemodell-gold` består ikkje sin eigen
  gold-policy (strukturelt avvik, oppdaga under T4-verifisering). Krev eiga
  spec dersom retting er ønskt.

**Filer endra:**
- `mkdocs/lib/sections/badges.sh` — Status-badge-guard (T5)
- `src/linkml/referanse/referansemodell-bronze/referansemodell-bronze-schema.yaml` — `license` + `annotations` (T4)
- `src/linkml/referanse/referansemodell-silver/referansemodell-silver-schema.yaml` — same
- `src/linkml/referanse/referansemodell-gold/referansemodell-gold-schema.yaml` — same
- `src/linkml/referanse/referansemodell-{bronze,silver,gold}/validation/*/`  — ferske valideringsresultat frå `make mcp-linkml-valider-modell`-køyringane over
