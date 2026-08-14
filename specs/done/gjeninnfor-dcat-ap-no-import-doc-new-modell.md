# Gjeninnfør absolutt versjonslåst dcat-ap-no-import i dokumentert new-modell-eksempel

## Bakgrunn

`make new-modell` (via `src/assets/scripts/scaffolding/new-modell.sh`) genererer
allereie eit skjema med absolutt versjonslåst import av `dcat-ap-no` (git-tag
`dcat-ap-no-v2.13.0`) — dette vart bytta frå eit tidlegare `common-ap-no`-import
i commit `b60e2d84`.

`mkdocs/docs/kom-i-gang/ny-domenemodell.md` sitt dokumenterte skjema-eksempel
vart derimot ikkje oppdatert i same commit til å visa dette — det viser
framleis det gamle `common-ap-no-v1.0.0`-importet med ein TODO om å byte til
`dcat-ap-no`, og forklaringsteksten under (id-slot-arv, TODO-tabellen) referer
til `common-ap-no` som det direkte importet. Dokumentasjonen er dermed ute av
synk med det skriptet faktisk genererer.

## Steg

1. Oppdater importlina i det dokumenterte eksempelet (linje 81) frå
   `common-ap-no-v1.0.0/.../common-ap-no-schema` (med TODO "byt til ein reell
   AP-NO-profil") til `dcat-ap-no-v2.13.0/.../dcat-ap-no-schema` (med TODO
   "endre/legg til imports etter behov" — identisk med kommentaren skriptet
   faktisk genererer)
2. Oppdater prosaen under kodeblokka (linje 121-127) som forklarar at
   `id`-sloten vert arva frå `common-ap-no` sitt importerte slot — presiser at
   arven no går via `dcat-ap-no` (som sjølv importerer `common-ap-no`)
3. Oppdater TODO-tabellraden (linje 138) som refererer til
   `common-ap-no`-importet, til å matche det faktiske genererte TODO-et og
   presisere at `dcat-ap-no` alt er standardimportet

## Handlingsliste

- [x] Steg 1: importline oppdatert til dcat-ap-no-v2.13.0
- [x] Steg 2: prosa om id-slot-arv oppdatert
- [x] Steg 3: TODO-tabellrad oppdatert

## Utført

`src/assets/scripts/scaffolding/new-modell.sh` genererte alt korrekt
(dcat-ap-no-v2.13.0, absolutt versjonslåst) — ingen kodeendring var
naudsynt der. Retta berre den etterslepande dokumentasjonen i
`mkdocs/docs/kom-i-gang/ny-domenemodell.md` slik at ho stemmer med det
skriptet faktisk genererer.
