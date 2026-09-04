---
name: ny-rule
description: Orkestrerer oppretting eller utviding av ein Claude Code-rule (.claude/rules/) frå eit konkret, observert åtferdsmønster eller feil. Bruk når brukaren ber om å lage/opprette ei ny rule, hindre at ein feil gjentek seg, eller spør om noko bør vere ei rule/skill/CLAUDE.md-tillegg.
---

## Føremål

Ei rule i dette repoet er auto-lasta kontekst, scopa til ein filsti
(`paths:` i frontmatter), som skal hindre ein **konkret, alt observert**
feilklasse frå å gjenta seg. Denne skillen orkestrerer prosessen frå
"dette skjedde" til ei ferdig, riktig plassert rule — same flyt som er
gjennomført fleire gonger i dette repoet (sjå
`specs/done/evaluering-nye-skills-og-rules.md`,
`specs/done/evaluering-spissa-rules-runde-2.md`, og
`specs/done/rule-unngå-lokal-duplisering-ved-import-fjerning.md`, som
gjennomgåande brukast som eksempel under).

## Steg

### 1. Krev konkret grunngjeving

Ei rule skal **aldri** vere spekulativ eller "beste praksis" i abstrakt
forstand. Krev eitt av:

- Ein registrert bug (`bugs/<fil>.md`)
- Eit spec-funn (`specs/done/<fil>.md`)
- Ei konkret hending frå denne økta (brukaren peikar på ho, eller du
  observerte ho sjølv)

Manglar dette — spør brukaren om eit konkret tilfelle før du går vidare.

**Eksempel:** "Trygg fjerning av ein import" vart **ikkje** skriven som ei
generell åtvaring om DRY. Ho vart grunngjeven i eit reelt hendingsforløp:
under P4a i `specs/done/evaluering-gjentakande-monster-backlog.md` vart
ein tilsynelatande ubrukt `dcat-ap-no`-import fjerna frå fem skjema
(basert på 0/29 klassar i bruk), noko som braut alle fem — dei trong
transitivt `id`/`tittel`/`LangString` frå `common-ap-no-schema`. Første
fikseforsøk (kopiere definisjonane inn lokalt) braut sjølv importhierarkiet
sitt DRY-føremål. Denne heile hendinga er sitert direkte i rula.

### 2. Avgjer mekanisme: rule, skill eller CLAUDE.md?

Bruk avgjerdstreet frå `specs/done/evaluering-nye-skills-og-rules.md`:

| Kva krevst? | Mekanisme |
|---|---|
| Skal gjelde **ubetinga**, uansett filsti (t.d. commit-meldingsformat, spec-arbeidsflyt) | CLAUDE.md direkte |
| Skal lastast **automatisk** når spesifikke filer vert rørte | Rule (`.claude/rules/`) |
| Skal berre køyrast ved **eksplisitt kall** (kommando/oppgåve-treff) | Skill (`.claude/skills/`) |

Stopp her og fortel brukaren dersom mønsteret ikkje passar ei rule (t.d.
dersom det er ubetinga — då høyrer det heime i CLAUDE.md i staden).

### 3. Finn rett fil og scope

- Sjekk om ein eksisterande rule alt dekker filstien saka gjeld
  (`.claude/rules/*.md`, sjå `paths:` i kvar fil sin frontmatter).
- **Legg til som ny subseksjon i ein eksisterande rule** dersom emnet
  naturleg høyrer saman med resten av innhaldet der (same filsti-scope).
  Eksempel: "Trygg fjerning av ein import" vart lagt til i
  `.claude/rules/linkml-schema.md` — emnet (importhandtering i
  LinkML-skjema) delte scope (`src/linkml/**`) med alt eksisterande
  innhald, så inga ny fil var nødvendig.
- **Opprett ei ny rule-fil** berre dersom filsti-scopet skil seg frå alle
  eksisterande rules. Eksempel: `.claude/rules/jinja2-templates.md` vart
  splitta ut av `mkdocs-portal.md` nettopp fordi Jinja2-whitespace-reglane
  berre gjeld `src/assets/templates/docgen/**`, ikkje resten av
  `mkdocs/**` (sjå `specs/done/evaluering-spissa-rules-runde-2.md`, C1).
- Frontmatter for ei ny fil:
  ```yaml
  ---
  name: <kortnavn>
  description: <kva rula dekker>. Lastast automatisk ved arbeid med <kva filer>.
  paths:
    - "<glob>"
  ---
  ```

### 4. Skriv innhaldet

Struktur som har vist seg å fungere i eksisterande rules (jf. "Trygg
fjerning av ein import"):

1. **Kort problemomtale** — kva skjer, kvifor er det feil. Ikkje berre
   "gjer X", men **kvifor** X er feil (så framtidig dømmekraft kan
   generalisere utover akkurat dette tilfellet).
2. **Eksplisitt forbod** — "Fell aldri tilbake til …", "Aldri …" — namngje
   det konkrete feilmønsteret direkte.
3. **Konkret, nummerert framgangsmåte** for korrekt åtferd i staden.
4. **Referanse til det konkrete tilfellet** (`bugs/<fil>.md` eller
   `specs/done/<fil>.md`) som grunngjeving — ikkje berre eit prinsipp,
   men eit sitat/oppslag til kva som faktisk skjedde.

### 5. Følg spec-arbeidsflyten

Per CLAUDE.md sin standard arbeidsflyt:

1. Opprett `specs/backlog/<kortnavn>.md` (bakgrunn, nummererte steg,
   handlingsliste, tom `## Avgjerder`-seksjon) — med mindre du alt jobbar
   frå ein eksisterande spec.
2. Utfør — skriv/utvid rula.
3. Logg ikkje-trivielle val (t.d. kvifor ny fil vs. eksisterande) i
   `## Avgjerder`.
4. Legg til `## Utført`, flytt specen til `specs/done/`.
5. Generer utkast til commit-melding (kompakt, presens, ingen
   `Co-Authored-By`).

## Merknad

Denne skillen orkestrerer **prosessen** for å lage ei rule — han
overstyrer ikkje det konkrete innhaldet i noka eksisterande rule, og
skriv ikkje rules for hypotetiske/spekulative mønster (jf. steg 1).
