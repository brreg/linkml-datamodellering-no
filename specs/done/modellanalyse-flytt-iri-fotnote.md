# Flytt IRI-dereferering-fotnota til rett etter Modellanalyse-intro

## Bakgrunn

I `mkdocs/lib/scripts/generate-modellanalyse-md.py` sin `main()` (linje
136–200) vert linja *"For IRI-dereferering og innhaldsforhandling sjå
Modell-analyse-workflowen."* i dag lagt til heilt til slutt (linje 191–195),
etter for-løkka over alle åtte `REPORTS`-oppføringar. Sidan "Liknande
typenavn" no er siste deloverskrift i den nye rekkjefølga (jf.
`specs/done/modellanalyse-rekkjefolge-og-filtrering.md`), hamnar denne
generelle merknaden visuelt inne i/rett under den siste deloverskrifta og
kan lett mistolkast som spesifikk for "Liknande typenavn" i staden for eit
generelt notat om heile Modellanalyse-seksjonen.

**Vedteke løysing:** flytt desse linjene til rett etter intro-blokkquoten
(linje 152–162), før for-løkka over `REPORTS` startar. Teksten og lenkja
er uendra — berre plasseringa i `lines`-lista.

## Steg

1. I `main()`: flytt blokka
   ```python
   lines += [
       "",
       f"*For IRI-dereferering og innhaldsforhandling sjå "
       f"[Modell-analyse]({MODELL_ANALYSE_WORKFLOW_URL})-workflowen.*",
   ]
   ```
   frå etter for-løkka (noverande linje 191–195) til rett etter
   intro-blokkquoten (etter noverande linje 162), før
   `any_report_found = False`-linja og for-løkka startar.

2. Verifiser med `python3 mkdocs/lib/scripts/generate-modellanalyse-md.py
   generated/samt/samt-bu/model-analyse samt samt-bu` (direkte, utan
   `make`/podman) — forvent: IRI-fotnota vist rett etter intro-avsnittet,
   før `### Isolerte klassar`; ingen duplisering; resten av innhaldet
   (alle åtte deloverskrifter, funntal, cross-domain-fotnotar) uendra.

3. Verifiser same kommando mot
   `generated/ap-no/dcat-ap-no/model-analyse ap-no dcat-ap-no` for å
   stadfeste at plasseringa held også når nokre rapportar manglar
   (dei tre "Liknande ..."-rapportane finst ikkje for dette domenet).

## Handlingsliste

- [x] Flytt IRI-dereferering-fotnota til rett etter intro-blokkquoten
- [x] Verifiser mot `generated/samt/samt-bu/model-analyse`
- [x] Verifiser mot `generated/ap-no/dcat-ap-no/model-analyse`

## Utført

Flytta blokka med IRI-dereferering-fotnota frå slutten av `lines`
(etter for-løkka over `REPORTS`) til rett etter intro-blokkquoten i
`main()` i `mkdocs/lib/scripts/generate-modellanalyse-md.py`. Teksten og
lenkja er uendra.

Verifisert med direkte scriptkøyring (`python3
generate-modellanalyse-md.py <dir> <domain> <schema>`, utan
`make`/podman) mot `generated/samt/samt-bu/model-analyse` (alle åtte
rapportar finst) og `generated/ap-no/dcat-ap-no/model-analyse` (tre
"Liknande ..."-rapportar manglar) — fotnota vert i begge tilfelle vist
rett etter intro-avsnittet, før `### Isolerte klassar`, med resten av
innhaldet (deloverskrifter, funntal, cross-domain-fotnotar) uendra.
