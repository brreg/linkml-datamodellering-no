# Skill: ny-rule

## Bakgrunn

Brukaren spør om det er mogleg å lage ein skill som kan opprette nye
Claude Code-rules for oss, med det siste tilfellet ("Trygg fjerning av ein
import" i `.claude/rules/linkml-schema.md`,
`specs/done/rule-unngå-lokal-duplisering-ved-import-fjerning.md`) som
eksempel. Denne økta har alt gjennomført prosessen fleire gonger (dei to
"evaluering av rules/skills"-rundene, pluss denne siste enkeltrula) —
mønsteret er repeterbart nok til å pakkast som ein skill, analogt med
`.claude/skills/ny-domenemodell/`.

## Steg

1. Opprett `.claude/skills/ny-rule/SKILL.md` som orkestrerer:
   - Krav om konkret grunngjeving (aldri ei spekulativ rule)
   - Avgjerdstreet rule vs. skill vs. CLAUDE.md (frå
     `specs/done/evaluering-nye-skills-og-rules.md`)
   - Val av fil/scope: utvid eksisterande rule vs. ny fil (frå
     `specs/done/evaluering-spissa-rules-runde-2.md` sin grunngjeving for
     Jinja2-templates-splitting)
   - Innhaldsstruktur som har vist seg å fungere i eksisterande rules
   - Standard spec-arbeidsflyt (jf. CLAUDE.md)
2. Bruk "Trygg fjerning av ein import" som konkret, gjennomarbeidd eksempel
   i sjølve skill-fila.

## Prioritert handlingsliste

| # | Steg | Fil | Merknad |
|---|---|---|---|
| 1 | Opprett skill | `.claude/skills/ny-rule/SKILL.md` | |

## Avgjerder

- **Bygde skillen som ei orkestrering av eit alt gjentatt, manuelt mønster
  i denne økta, ikkje som ny prosess-oppfinning.** Grunngjeving: dei to
  "evaluering"-spec-ane og denne siste enkeltrula utgjer alt tre
  gjennomførte, konsistente iterasjonar av same flyt — nøyaktig kriteriet
  ein skill skal pakke (jf. `ny-domenemodell`-skillen sin grunngjeving).
- **Bakte inn eit fullt, konkret eksempel i skill-fila (ikkje berre ei
  abstrakt oppskrift).** Grunngjeving: brukaren bad eksplisitt om å bruke
  det siste tilfellet som eksempel — eit konkret, gjennomarbeidd eksempel
  gjer skillen meir robust for framtidige, nye tilfelle enn reint
  abstrakte steg.

## Utført

- `.claude/skills/ny-rule/SKILL.md`: ny.
