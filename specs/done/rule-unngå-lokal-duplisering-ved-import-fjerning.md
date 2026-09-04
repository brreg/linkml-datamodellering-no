# Rule: unngå lokal duplisering ved import-fjerning

## Bakgrunn

Under P4a i `specs/done/evaluering-gjentakande-monster-backlog.md` fjerna
eg ein tilsynelatande ubrukt `dcat-ap-no`-import frå fem skjema (basert på
at 0 av 29 klassar var i bruk). Dette braut alle fem, sidan dei transitivt
trong globale slots (`id`, `tittel`) og typen `LangString` frå
`common-ap-no-schema`, nådd via AP-NO-profil-importen. Første forsøk på
fiks var å kopiere desse definisjonane inn **lokalt** i kvart skjema — noko
som braut importhierarkiet sitt DRY-føremål (duplikate parallelle
definisjonar av noko som skal ha éi kjelde). Retta ved å behalde importen
i staden. Brukaren ønskjer no ei rule som hindrar at dette mønsteret
(fjern import → kopier inn manglande definisjonar lokalt) gjentek seg.

## Steg

1. Legg til ein ny subseksjon i `.claude/rules/linkml-schema.md` (scopa til
   `src/linkml/**`, alt lasta automatisk ved skjemaredigering) som
   eksplisitt åtvarar mot mønsteret, med ein konkret 4-stegs
   framgangsmåte for trygg import-fjerning (fjern → `make lint`/`make
   roundtrip` → feilar det, set attende, ikkje dupliser lokalt → berre
   fjern permanent dersom grøn).
2. Referer det konkrete tilfellet (P4a) som grunngjeving.

## Prioritert handlingsliste

| # | Steg | Fil | Merknad |
|---|---|---|---|
| 1 | Legg til subseksjon om trygg import-fjerning | `.claude/rules/linkml-schema.md` | Plassert etter "Containerklasse"/"Los-tema", før "Ny profil eller domenemodell" |

## Avgjerder

- **Ny subseksjon i eksisterande `linkml-schema.md`, ikkje ei eiga ny
  rule-fil.** Grunngjeving: emnet (importhandtering i LinkML-skjema) høyrer
  naturleg heime i den eksisterande, alt automatisk lasta rula for
  `src/linkml/**` — inga ny filsti-scoping trengst, og ei eiga fil ville
  vore unødvendig oppsplitting av tett relatert innhald (i motsetnad til
  t.d. Jinja2-malar, som hadde eit heilt anna filsti-scope enn resten av
  mkdocs-portal.md).

## Utført

- `.claude/rules/linkml-schema.md`: ny subseksjon lagt til.
