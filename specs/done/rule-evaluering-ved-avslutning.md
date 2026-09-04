# Rule-evaluering som fast steg ved avslutning

## Bakgrunn

Denne økta har fleire gonger vist at utført arbeid avdekker mønster som
bør fangast som Claude Code-rules (t.d. "Trygg fjerning av ein import" i
`.claude/rules/linkml-schema.md`, og utvidingane av `ci-workflows.md`
etter workflow-refaktoreringa) — men dette har til no skjedd berre når
brukaren eksplisitt bad om det i etterkant, ikkje som ein fast del av
avslutningsrutinen. Brukaren ønskjer at denne evalueringa skal skje
**automatisk**, rett før commit-meldinga vert generert, med eit spørsmål
til brukaren dersom noko konkret vert funne.

## Steg

1. Utvid CLAUDE.md § "Arbeidsflyt", steg 5 ("Avslutning") med eit nytt
   delsteg (a), rett før commit-melding-generering: evaluer om arbeidet
   avslører eit konkret, ikkje-spekulativt mønster/lærdom som bør
   fangast som ny/endra rule — same krav til konkret grunngjeving som
   `.claude/skills/ny-rule/SKILL.md` steg 1 — og spør brukaren om dei
   ønskjer å leggje til/endre rula.
2. Nummerer om dei attverande delstega (commit-melding, Utført-seksjon,
   flytt til done) frå (a)-(c) til (b)-(d).

## Prioritert handlingsliste

| # | Steg | Fil | Merknad |
|---|---|---|---|
| 1 | Legg til rule-evalueringsdelsteg i Avslutning | `CLAUDE.md` (Arbeidsflyt, steg 5) | |

## Avgjerder

- **Kravde same "konkret grunngjeving"-terskel som `ny-rule`-skillen, i
  staden for å definere eit nytt, separat kriterium.** Grunngjeving:
  unngår at denne automatiske evalueringa foreslår rules for kvar minste
  detalj (spekulativ "beste praksis") — same disiplin som alt er
  etablert og verifisert fungerande for skill-baserte rule-forslag i
  denne økta.
- **Spør brukaren, utfør ikkje automatisk.** Grunngjeving: brukaren bad
  eksplisitt om at eg skal spørje, ikkje handle på eiga hand — matchar
  òg CLAUDE.md sitt generelle prinsipp om at nye rules skal grunngjevast
  og godkjennast, ikkje innførast stilltiande.

## Utført

- `CLAUDE.md` § "Arbeidsflyt": steg 5 utvida med rule-evalueringsdelsteg
  (a), attverande delsteg nummerert om til (b)-(d).
