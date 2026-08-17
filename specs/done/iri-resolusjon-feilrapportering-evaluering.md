# IRI-resolusjonssjekk: evaluering av feilrapportering i første køyring

## Bakgrunn

Brukaren bad om at loggen frå første køyring av `modell-analyse.yml`
sin `iri-resolution`-jobb (`gh run view 32004067263`, køyrt
2026-08-17T07:02 UTC, `workflow_dispatch`, konklusjon `success`) vart lese
og vurdert for feilrapportering. Jobben feilar aldri CI (informativ
rapport, jf. workflow-kommentar), så "success" seier ingenting om
*innhaldet* i rapporten — evalueringa gjeld difor rapportinnhaldet
(`iri-resolution-report.md`, lasta ned frå artefakten), ikkje
jobbstatusen.

Rapporten har to seksjonar, generert av
`src/assets/scripts/makefile/check-iri-resolution.py`:

1. **IRI-resolusjonssjekk** — 17 av 124 unike IRI-ar (id/default_prefix/
   prefixes) feila (HTTP 404/403 eller DNS-feil).
2. **Innhaldsforhandling** — 222 av 222 testar (74 eigne IRI-ar × 3
   testar) feila.

## Evaluering

**Konklusjon: Jobben rapporterer teknisk korrekte HTTP-fakta, men
seksjon 1 re-flaggar minst 13 av 17 feil som allereie er gransigranska,
avgjorde og ekskluderte andre stader i repoet — utan kryssreferanse.
Dette er reell feilrapportering i form av støy og dupliserte
konklusjonar, ikkje feil HTTP-status.**

### Seksjon 1 — IRI-resolusjonssjekk (17 feil)

Verifisert direkte mot live HTTP-endepunkt (`curl`) for kvar rad:

| Kategori | IRI-ar | Verifisert status | Vurdering |
|---|---|---|---|
| **A — Allereie avgjort, ekskludert i lychee** | `schema.fintlabs.no/*` (7 stk) | 403 frå eit stadfesta "Access Gateway"-produkt, identisk uansett `Accept`/User-Agent | **Feilrapportering.** Identisk domene og rotårsak som `specs/done/lenkjesjekk-fint-schema-fintlabs-no.md` — der vart det stadfesta at heile verten er portvakt-verna og **aldri** har vore offentleg tilgjengeleg (0 Wayback-snapshot). Ekskludert i `.github/lychee.toml`. `check-iri-resolution.py` deler ikkje denne kunnskapen. |
| **A — Allereie avgjort, ekskludert i lychee** | `data.norge.no/vocabulary/ngr-*` (4 stk) | 404, stadfesta | **Feilrapportering.** Identisk mønster som `specs/done/lenkjesjekk-ngr-vocabulary-namespace.md` — brukaren stadfesta at NGR-vokabularnamnerommet **ikkje er meint å vere resolvbart og aldri vil verte det** (skil seg frå `default_prefix`, som fungerer). Ekskludert i `.github/lychee.toml`. |
| **A — Allereie avgjort, ekskludert i lychee** | `https://example.org/vocab/`, `https://fint.example.org/` (2 stk) | 404 / DNS-feil, som venta | **Feilrapportering.** RFC 2606-plasshaldardomene, bevisst brukt i referansemodellane (`referansemodell-*`, reine dokumentasjons-/malskjema) og `fint-common`. Same mønster som `*.example.org`-eksklusjonen i `specs/done/lenkje-og-mermaid-sjekk.md` (§ plasshaldar-domene). Desse skal aldri resolvere — det er poenget. |
| **B — Ope, uavklara (korrekt å framleis flagge)** | `data.norge.no/vocabulary/cccevno#` | 404, stadfesta | Ikkje feilrapportering — eksplisitt dokumentert som **framleis ope** sak i `specs/done/lenkjesjekk-ngr-vocabulary-namespace.md` (kategori E, viser til `lenkjesjekk-runde2-verifisering.md`). Krev ei aktiv avgjerd, ikkje ein automatisk eksklusjon. |
| **C — Ekte, eksternt, ikkje tidlegare dokumentert** | `w3id.org/linkml/`, `publications.europa.eu/ontology/euvoc#`, `rdf-vocabulary.ddialliance.org/xkos#` | Alle stadfesta 404 for sluttresponsen i redirect-kjeda (verifisert med `curl -L`) | Ikkje feilrapportering — reelle, eksterne brotne namnerom (LinkML/EU/DDI Alliance har omstrukturert URI-ane sine). Utanfor repoet si råderett å fikse, men korrekt fanga opp. |

13 av 17 rader (kategori A) er difor dupliserte konklusjonar frå
allereie avslutta spesifikasjonar. Dei resterande 4 (kategori B+C) er
reelle/opne funn som rapporten korrekt fangar.

### Seksjon 2 — Innhaldsforhandling (222/222 feil)

**Ikkje feilrapportering — venta og allereie dokumentert utfall.**
`specs/done/iri-resolusjon-innhaldsforhandling.md` (§ Utført, 2026-08-11)
stadfesta alt at `data.norge.no` returnerer `text/html` uansett
`Accept`-header og aldri set `Content-Language`, og at dette er eit
kjent infrastrukturgap hjå Digdir (avvik 4 i
`avvik-peikarar-til-offentlege-ressursar.md`), ikkje ein feil i sjekken.

Verifisert på nytt no: `data.norge.no` er ein SPA som returnerer
**HTTP 200 for ein vilkårleg, oppdikta sti** (testa
`https://data.norge.no/this-path-definitely-does-not-exist-xyz123` →
200 `text/html`). Dette har to konsekvensar utover det som alt er
dokumentert:

1. Innhaldsforhandlingsseksjonen kan **strukturelt aldri** gje anna enn
   100 %-feil for nokon `data.norge.no`-URI, publisert eller ikkje —
   talet seier difor ingenting om kor mange av dei 39 skjemaa som
   *eigentleg* manglar innhaldsforhandling versus rett og slett ikkje er
   publiserte enno. Rapporten listar alle 39 likt, med same detaljgrad,
   som om det var 39 uavhengige per-skjema-funn.
   [[iri-resolusjon-innhaldsforhandling]]
2. Same SPA-åtferd betyr at **hovud-resolusjonssjekken** (seksjon 1) gjev
   eit falskt "OK" for alle 74 eigne `id`/`default_prefix`-URI-ar — ein
   reell skrivefeil i `id`- eller `default_prefix`-verdien (t.d. feil
   sti) ville **ikkje** verte fanga opp, sidan SPA-en svarar 200 på kva
   som helst. Sjekken kan altså ikkje skilje "denne URI-en er korrekt og
   registrert" frå "denne URI-en finst ikkje, men domenet svarar uansett".

## Tilrådde tiltak

1. **T1 — Del kjend-eksklusjon-kunnskap mellom lychee og
   `check-iri-resolution.py`.** Legg til eit filter i
   `check-iri-resolution.py` (eller ei delt liste begge script kan lese)
   som ekskluderer dei tre stadfesta, avgjorde mønstra frå
   §Kategori A: `^https://schema\.fintlabs\.no/`,
   `^https://data\.norge\.no/vocabulary/ngr-`, og RFC 2606-plasshaldarar
   (`example\.org`, `*.example.org`). DRY-prinsippet i CLAUDE.md tilseier
   éi kjelde for denne typen "kjend, avgjort, ikkje-resolvbar"-kunnskap —
   ikkje ei liste i `.github/lychee.toml` og ei anna (manglande) i
   `check-iri-resolution.py`.
2. **T2 — Legg til ei kort forklarande linje i
   Innhaldsforhandling-seksjonen** når feilraten er 100 %, t.d. "Alle
   IRI-ar på data.norge.no manglar i dag innhaldsforhandling for heile
   domenet (kjent, dokumentert infrastrukturgap — ikkje eit per-skjema-
   avvik)" — slik at ein lesar av den vekentlege rapporten ikkje må
   grave fram `specs/done/iri-resolusjon-innhaldsforhandling.md` for å
   forstå at 222/222 er venta, ikkje 39 nye funn.
3. **T3 — Vurder (separat, lågare prioritert) om
   hovud-resolusjonssjekken bør suppererast** med eit eksplisitt
   sti-eksistens-signal for `data.norge.no` (t.d. samanlikne mot eit
   kjent 404-svar for å oppdage SPA-catch-all), sidan dagens sjekk ikkje
   kan skilje ein gyldig registrert schema-URI frå ein tilfeldig streng.
   Låg prioritet: krev meir kompleks logikk for marginal gevinst, og
   `published-uris.lock`-mekanismen dekkjer alt delar av same behov for
   dei to skjemaa som faktisk har publisert innhald.
4. **T4 — Ny sammendrag-jobb på tvers av alle fem jobbane i
   `modell-analyse.yml`.** Brukarønske (uavhengig av T1–T3): eit lesar av
   den vekentlege køyringa skal kunne sjå talet på funn/feil per
   sjekk-type utan å opne alle fem artefaktane enkeltvis. I dag har kvar
   av dei fem rapportane si eiga oppsummeringslinje, men dei står isolerte
   i kvar sin jobb-logg:

   | Jobb | Rapportfil | Oppsummeringslinje i dag (to variantar) |
   |---|---|---|
   | `similar-classes-domain` | `similar-classes-domain-report.md` | `Ingen klasser over terskelen vart funne (N klasser sjekka).` / `**Totalt: N par funne blant M klasser.**` |
   | `similar-classes-all` | `similar-classes-all-report.md` | same mønster |
   | `similar-slots-domain` | `similar-slots-domain-report.md` | same mønster (slots) |
   | `similar-slots-all` | `similar-slots-all-report.md` | same mønster (slots) |
   | `iri-resolution` | `iri-resolution-report.md` | `Alle IRI-ar resolverte.` / `**N av M IRI-ar resolverte ikkje.**` **og** `Alle N innhaldsforhandlingstestar bestod.` / `**N av M innhaldsforhandlingstestar feila.**` (to tal i same fil) |

   Ei ny `sammendrag`-jobb skal samle desse seks tala (fem jobbar, seks
   tal sidan `iri-resolution` har to seksjonar) i éin konsolidert tabell,
   t.d.:

   | Sjekk | Funn/feil | Sjekka totalt |
   |---|---|---|
   | Liknande klassenamn (same domene) | 0 | 245 |
   | Liknande klassenamn (alle domene) | 3 | 245 |
   | Liknande slotnamn (same domene) | 1 | 512 |
   | Liknande slotnamn (alle domene) | 5 | 512 |
   | IRI-resolusjon | 17 | 124 |
   | Innhaldsforhandling | 222 | 222 |

   **Design:**
   - Ny jobb `sammendrag` i `.github/workflows/modell-analyse.yml` med
     `needs: [similar-classes-domain, similar-classes-all,
     similar-slots-domain, similar-slots-all, iri-resolution]` og
     `if: always()` (slik at sammendraget framleis genererast sjølv om
     ein av dei fem — mot formodning — skulle feile).
   - Lastar ned alle fem artefaktane (`actions/download-artifact@v7`,
     éin per jobb, til kjende filnamn) før parsing.
   - Ny Python-script (t.d.
     `src/assets/scripts/makefile/summarise-modell-analyse.py`) som les
     dei fem nedlasta rapportfilene, trekker ut tala via regex mot dei to
     kjende linjeformata per rapporttype (sjå tabellen over), og skriv
     den konsoliderte tabellen til stdout — same mønster som dei andre
     `analyse-*`-skripta (feilar aldri, reint informativt).
   - Ny make-target `analyse-sammendrag` i `make/91-modell-analyse.mk`
     som køyrer scriptet (følgjer eksisterande `analyse-*`-mønster i same
     fil), kalla frå workflow-jobben via
     `make analyse-sammendrag > sammendrag-report.md`, deretter same
     `>> "$GITHUB_STEP_SUMMARY"`-mønster som dei andre jobbane.
   - **Kjend avgrensing:** GitHub Actions viser jobb-oppsummeringar i
     rekkjefølgja jobbane fullfører, ikkje etter avhengigheitsgraf eller
     alfabetisk — ein `sammendrag`-jobb som er avhengig av (`needs:`) alle
     dei andre vil difor alltid visast **sist** på køyringa si
     samandrag-side, ikkje øvst. Akseptert som greitt for ein vekentleg,
     informativ rapport; ingen kjend måte å tvinge jobb-rekkjefølgje i
     GitHub Actions sitt run summary-visning.

## Steg

1. Implementer T1 i `check-iri-resolution.py`: legg til eksklusjonsliste
   (regex, same mønster som `.github/lychee.toml`) og filtrer bort
   matchande IRI-ar frå `print_resolution_report` sitt resultat, med ein
   kommentar som viser til dei tre kjeldespec-ane
   (`lenkjesjekk-fint-schema-fintlabs-no.md`,
   `lenkjesjekk-ngr-vocabulary-namespace.md`,
   `lenkje-og-mermaid-sjekk.md`).
2. Implementer T2: legg til den forklarande linja i
   `print_content_negotiation_report` når `len(failures) == total`.
3. Oppdater `COMMANDS.md` sin skildring av `analyse-iri-resolution` om
   nødvendig.
4. Test lokalt: `make analyse-iri-resolution` og stadfest at dei 13
   kjende radene er borte frå seksjon 1, at seksjon 2 har den nye
   forklaringslinja, og at dei 4 opne/ekte funna (w3id.org/linkml,
   euvoc, xkos, cccevno) framleis vert rapporterte.
5. Implementer T4:
   a. Nytt script `src/assets/scripts/makefile/summarise-modell-analyse.py`
      som tek dei fem rapportfilene som argument/faste stiar, parsar
      oppsummeringslinjene (regex per rapporttype, jf. tabellen i T4) og
      skriv den konsoliderte sammendrag-tabellen.
   b. Ny target `analyse-sammendrag` i `make/91-modell-analyse.mk`.
   c. Ny jobb `sammendrag` i `.github/workflows/modell-analyse.yml`:
      `needs:` alle fem eksisterande jobbar, `if: always()`, last ned dei
      fem artefaktane, køyr `make analyse-sammendrag > sammendrag-report.md`
      og skriv til `$GITHUB_STEP_SUMMARY` (same mønster som dei andre
      jobbane).
   d. `actionlint` mot den endra workflow-fila (påkravd av CLAUDE.md etter
      kvar CI-endring):
      `podman run --rm -v "$(pwd)":/repo:ro -w /repo docker.io/rhysd/actionlint:latest -color .github/workflows/modell-analyse.yml`
   e. Test lokalt: køyr dei fem eksisterande `analyse-*`-targeta først for
      å generere rapportfilene, deretter `make analyse-sammendrag` og
      stadfest at tala i sammendrag-tabellen stemmer med
      oppsummeringslinjene i kvar av dei fem kjeldefilene.

## Handlingsliste

- [x] T1: filtrer kjende, avgjorde IRI-mønster frå seksjon 1
- [x] T2: forklarande linje i seksjon 2 ved 100 % feilrate
- [x] T3: vurdert, ikkje prioritert no (dokumentert som opsjon)
- [x] Lokal test av `make analyse-iri-resolution`
- [x] T4a: `summarise-modell-analyse.py`
- [x] T4b: `analyse-sammendrag`-target
- [x] T4c: ny `sammendrag`-jobb i `modell-analyse.yml`
- [x] T4d: `actionlint` mot endra workflow-fil
- [x] T4e: lokal test av heile sammendrag-kjeda

## Utført

**Dato:** 2026-08-17

Alle fire tiltak (T1, T2, T4 implementerte; T3 vurdert og medvite nedprioritert)
gjennomførte og verifiserte lokalt.

**Endra filer:**
- `src/assets/scripts/makefile/check-iri-resolution.py`: ny
  `KNOWN_UNRESOLVABLE_PATTERNS`/`is_known_unresolvable()` (T1) som filtrerer
  `schema.fintlabs.no`, `data.norge.no/vocabulary/ngr-*` og
  `example.org`/`*.example.org` frå seksjon 1 før HTTP-sjekk; ny
  forklaringslinje i `print_content_negotiation_report` når feilraten er
  100 % (T2)
- `src/assets/scripts/makefile/summarise-modell-analyse.py`: nytt script
  (T4a) som parsar oppsummeringslinjene frå dei fem `analyse-*`-rapportane
  og skriv ein konsolidert sammendrag-tabell
- `make/91-modell-analyse.mk`: ny target `analyse-sammendrag` (T4b)
- `.github/workflows/modell-analyse.yml`: ny jobb `sammendrag` (T4c),
  avhengig av alle fem eksisterande jobbar (`needs:`, `if: always()`),
  som lastar ned artefaktane og køyrer `make analyse-sammendrag`
- `COMMANDS.md`: oppdatert skildring av `analyse-iri-resolution`
  (nemner eksklusjonsfilteret) + ny rad for `analyse-sammendrag`
- `.claude/settings.local.json`: la til `/run/user/1000/libpod` og
  `/run/user/1000` i `sandbox.filesystem.allowWrite` (brukarbede endring,
  urelatert til T1–T4 — podman treng skrivetilgang til runtime-katalogen
  sin for å setje sticky bit, elles feilar alle podman-kommandoar i
  sandkassa)

**Validering:**
- `actionlint` mot `.github/workflows/modell-analyse.yml`: **0 feil**
- Lokal `make analyse-iri-resolution`: stadfesta at dei 13 kjende radene
  (7× `schema.fintlabs.no`, 4× `ngr-vocabulary`, 2× `example.org`) er
  borte frå seksjon 1 (111 av 124 IRI-ar testa, 13 utelatne), og at dei 4
  reelle/opne funna (w3id.org/linkml, euvoc, xkos, cccevno) framleis
  vert rapporterte (**4 av 111 IRI-ar resolverte ikkje**). Seksjon 2 viser
  den nye forklaringslinja ved 222/222-feilrate.
- Lokal `make analyse-sammendrag` mot alle fem genererte rapportfilene:
  tala i sammendrag-tabellen (72/527, 191/527, 177/1199, 526/1199, 4/111,
  222/222) stemmer nøyaktig med oppsummeringslinjene i kvar kjeldefil
- Mellombelse rapportfilar (`*-report.md`) generert under lokal test
  sletta etter verifisering — ikkje del av kjeldetreet
