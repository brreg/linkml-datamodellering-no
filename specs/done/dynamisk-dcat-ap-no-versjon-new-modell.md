# Les dcat-ap-no-versjon dynamisk frå manifest i make new-modell

## Bakgrunn

`new-modell.sh` hardkodar tag-namnet `dcat-ap-no-v2.13.0` i det versjonslåste
importet han set inn i genererte skjema (jf.
`specs/done/gjeninnfor-dcat-ap-no-import-doc-new-modell.md`). Brukaren
oppdaga at ein nygenerert modell (`src/linkml/oreg/kafferegisteret/`) fekk
importlinke til `dcat-ap-no-v2.13.0`, medan `.github/release-please-manifest.json`
alt viser `2.14.0` — hardkodinga hadde gått ut på dato etter release-runda
dokumentert i `specs/done/fiks-release-please-multi-pr-bug.md`.

Dette er nøyaktig det DRY-mønsteret CLAUDE.md § «DRY — ikkje gjenta deg
sjølv» krev retta systematisk: hardkoda verdiar skal erstattast med
dynamisk oppslag mot sannkjelda. Sannkjelda for kva versjon av `dcat-ap-no`
som er sist releasa er `.github/release-please-manifest.json` sin nøkkel
`src/linkml/ap-no/dcat-ap-no` — akkurat den same fila
`release-please.yml` sjølv brukar til å avgjere versjonar.

Utan denne fiksen vil **kvar einaste** framtidige `make new-modell`-køyring
generere ein import som er stalig frå fødselen av, og som må rettast
manuelt i etterkant (slik `designregisteret` og no `kafferegisteret` begge
har vorte råka av).

## Steg

1. Legg til eit steg i `new-modell.sh` som les gjeldande `dcat-ap-no`-versjon
   frå `.github/release-please-manifest.json` via `jq` (feiler tydeleg,
   ikkje stille, dersom nøkkelen manglar — jf. CLAUDE.md § «Ingen stille feil»)
2. Bruk den innlesne versjonen til å byggje tag-namnet i staden for det
   hardkoda `dcat-ap-no-v2.13.0`
3. Rett den allereie feilaktige importen i det nygenererte
   `src/linkml/oreg/kafferegisteret/kafferegisteret-schema.yaml` til å
   matche faktisk manifest-versjon (2.14.0), sidan den alt har gått stalig
4. Verifiser Bash-syntaks (`bash -n`)

## Handlingsliste

- [x] Steg 1: dynamisk versjonsoppslag lagt til
- [x] Steg 2: hardkoda tag-namn erstatta
- [x] Steg 3: kafferegisteret-schema.yaml retta
- [x] Steg 4: syntaks verifisert

## Utført

Alle fire steg utført. `new-modell.sh` les no
`.github/release-please-manifest.json` sin `src/linkml/ap-no/dcat-ap-no`-nøkkel
via `jq` ved kvar køyring (feiler tydeleg — ikkje stille — dersom nøkkelen
manglar), og byggjer importtaggen dynamisk. Ingen framtidig `make new-modell`-
køyring vil generere ein stalig dcat-ap-no-import igjen. `bash -n` stadfestar
gyldig syntaks. `kafferegisteret-schema.yaml` sin allereie-genererte import
er retta til `dcat-ap-no-v2.14.0` for å matche manifestet.
