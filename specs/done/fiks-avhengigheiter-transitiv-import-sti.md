# Fiks manglande transitive importar i Avhengigheiter-seksjonen

## Bakgrunn

`## Avhengigheiter`-seksjonen på kvar skjemaside (t.d.
`mkdocs/docs/samt/samt-bu/index.md`) skal vise eit ASCII-tre med både
direkte og transitive importar, kvar linje merkt med kommentaren
`# direkte import` eller `# transitiv import`. I dag viser seksjonen berre
ei flat liste av dei direkte importane, utan tre-struktur og utan
kommentarar.

**Rotårsak:** Commit `9016962a` ("flytt rettleiingssider til
seksjonskatalogar") flytta `mkdocs/docs/importhierarki.md` til
`mkdocs/docs/arkitektur/importhierarki.md`, men `parse-dependency-tree.py`
har **to** hardkoda referansar til fila:

- `main()` sin `--format flat`-gren (linje ~452): oppdatert til
  `mkdocs/docs/arkitektur/importhierarki.md` ✅
- `build_dependency_tree()` (linje 358) — funksjonen `avhengigheiter.sh`
  faktisk kallar via standard `tree`-format — **ikkje oppdatert**, peikar
  framleis på `mkdocs/docs/importhierarki.md` ❌

Commit-meldinga hevdar "2 stadar" vart retta, men diffen viser berre éi
linje endra. Sidan fila ikkje finst på den gamle stien, går
`build_dependency_tree()` inn i fallback-grena
(`if not hierarchy_file.exists(): return '\n'.join(imports)`), som
returnerer ei flat liste av kun direkte importar — utan feilmelding.

Denne fallback-en manglar i tillegg logging, i strid med CLAUDE.md-regelen
"Ingen stille feil" — dersom han hadde logga til stderr, ville denne
regresjonen vore synleg i byggeloggen med det same.

## Steg

1. Rett `hierarchy_file`-stien i `build_dependency_tree()`
   (`mkdocs/lib/scripts/parse-dependency-tree.py`, linje ~358) frå
   `mkdocs/docs/importhierarki.md` til
   `mkdocs/docs/arkitektur/importhierarki.md`, i tråd med den allereie
   korrekte stien i `--format flat`-grena.
2. Legg til éi logglinje til stderr i begge fallback-grenene i
   `parse-dependency-tree.py` (`hierarchy_file.exists()`-sjekken i
   `build_dependency_tree()` og i `main()` sin `flat`-gren, samt
   `if not hierarchies:`-fallbacka) som forklarer kvifor flat liste vert
   brukt i staden for tre, jf. `specs/done/ingen-stille-feil.md`.
3. Regenerer dokumentasjonsportalen (`make docs-publish` eller tilsvarande
   målretta regenerering) og verifiser at `mkdocs/docs/samt/samt-bu/index.md`
   igjen viser eit ASCII-tre med `# direkte import` / `# transitiv import`-
   kommentarar i Avhengigheiter-seksjonen.
4. Stikkprøve minst éin AP-NO-modell (t.d. `dcat-ap-no` eller `cpsv-ap-no`)
   for å stadfeste at treet og kommentarane er korrekte også der importkjeda
   er lengre enn éitt nivå.
5. Oppdater specen med `## Utført`-seksjon og flytt til `specs/done/`.

## Akseptansekriterium

- Avhengigheiter-seksjonen viser eit hierarkisk ASCII-tre (ikkje flat liste)
  for alle skjema med transitive importar.
- Kvar linje i treet er merkt `# direkte import` eller `# transitiv import`.
- Fallback-grenene i `parse-dependency-tree.py` logg éi linje til stderr
  når dei triggast, slik at framtidige stibrot vert synlege i byggelogg.

## Utført

1. Retta `hierarchy_file`-stien i `build_dependency_tree()`
   (`mkdocs/lib/scripts/parse-dependency-tree.py`, linje 358) til
   `mkdocs/docs/arkitektur/importhierarki.md`.
2. La til éi `WARN`-logglinje til stderr i alle fem fallback-grenene som
   returnerer flat importliste (`build_dependency_tree()`: fil finst ikkje,
   ingen hierarki-blokker, ingen relevante hierarki, ingen filtrert tre;
   `main()` sin `--format flat`-gren: same fire tilfelle).
3. Køyrde `make docs-publish` og verifiserte i byggeloggen at fallback-en
   for manglande fil (`fann ikkje ... importhierarki.md`) ikkje lenger
   triggast for noko skjema.
4. Stadfesta at `mkdocs/docs/samt/samt-bu/index.md` no viser eit
   5-nivås ASCII-tre (`linkml:types → common-ap-no-schema → dqv-core-schema
   → dcat-ap-no-schema → dqv-ap-no-schema`) med korrekt merking av direkte
   (`linkml:types`, `dqv-ap-no-schema`) og transitive importar.
5. Stadfesta same oppførsel for `mkdocs/docs/ap-no/cpsv-ap-no/index.md`
   (2-nivås tre, begge merkt direkte import).
6. Verifiserte at skjema utan transitive importar (t.d. `common-ap-no`, som
   berre importerer `linkml:types` direkte) framleis viser korrekt
   éi-linjes liste — uendra åtferd, ingen regresjon.

Status: ferdig. Flytta til `specs/done/`.
