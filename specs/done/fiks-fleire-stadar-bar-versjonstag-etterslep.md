# Fiks fleire stadar med bar versjonstag-etterslep (v2.0.0 → dcat-ap-no-v2.0.0)

## Bakgrunn

Oppfølging av `specs/done/gjeninnfor-dcat-ap-no-import-doc-new-modell.md` og
`specs/done/fiks-include-component-in-tag-inversjon.md`: dokumentasjon som
viser bar `v<versjon>`-tag (utan komponentprefiks) i
`raw.githubusercontent.com`-importURL-ar peikar på tagnamn som ikkje finst —
komponent-spesifikke tagar (`<component>-v<versjon>`) er den einaste
fungerande forma sidan `include-component-in-tag` vart retta til `true`.
`mkdocs/docs/arkitektur/ekstern-bruk.md` åtvarar allereie eksplisitt mot
nett dette mønsteret («Generelle release-taggar … garanterer ikkje at alle
skjemafiler finst i den commiten»).

Søk gjennom heile repoet (utanom `specs/done/`, som er arkivert og skal stå
urørt) fann to aktive stadar med same etterslep — begge brukar bar `v2.0.0`,
eit tagnamn som aldri har eksistert (verifisert med `git tag -l`):

- `SCOPE.md` (line 144)
- `specs/backlog/plan-demo-repo-dcat-ap-no.md` (6 stader: line 57, 62, 88, 90,
  135, 332)

Verifisert at `dcat-ap-no-v2.0.0` (komponent-prefiksert) faktisk finst som
git-tag — minimal fiks er å leggje til prefikset, ikkje byte versjonsnummer.

Andre treff frå søket var enten allereie korrekte (`CONVENTIONS.md`,
`mkdocs/docs/arkitektur/ekstern-bruk.md`, `README.md` — alle brukar
komponent-prefikserte tagar) eller i `specs/done/` (arkivert, urørt per
CLAUDE.md).

## Steg

1. `SCOPE.md`: `v2.0.0` → `dcat-ap-no-v2.0.0` i import-URL-eksempelet
2. `specs/backlog/plan-demo-repo-dcat-ap-no.md`: alle 6 førekomstar av
   `v2.0.0` → `dcat-ap-no-v2.0.0` (import-URL, `ap-no-version:`-felt,
   `AP_NO_VERSION`-env-var, bootstrap-URL, prosatekst, sjekklistetabell)

## Handlingsliste

- [x] Steg 1: SCOPE.md retta
- [x] Steg 2: plan-demo-repo-dcat-ap-no.md retta (6 stader)

## Utført

Alle 7 førekomstar retta (1 i SCOPE.md, 6 i plan-demo-repo-dcat-ap-no.md).
I same slengen retta eit uavhengig, tilstøytande shell-skopingsproblem i
same fil (line 88): `AP_NO_VERSION=... curl ... | bash` set miljøvariabelen
på `curl`, ikkje `bash` — bootstrap.sh ville aldri sett verdien. Bytt til
same mønster som det verifisert-korrekte eksempelet i
`mkdocs/docs/arkitektur/ekstern-bruk.md`
(`curl ... | AP_NO_VERSION=... bash`, henta frå `main` i staden for ein
skjema-tag). Verifisert med grep at ingen bar `vX.Y.Z`-tag-referansar står
att i aktive (ikkje-arkiverte) filer.
