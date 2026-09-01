# Fix: Steg 6-diffen viste 3 hunkar i staden for 2

## Bakgrunn

Etter [javazone-demo-steg6-reduser-utval.md](../done/javazone-demo-steg6-reduser-utval.md)
skal steg 6 sin `do_replace`-diff vise nøyaktig to endringar: `Foredrag`
(ny `annotations.begrepsidentifikator`) og `har_foredrag` (ny
`slot_uri`). Brukaren observerte at diffen faktisk viste **tre** `@@`-
hunkar.

**Årsak:** `block_end_line` reknar den tomme linja rett før neste
klassenøkkel (`  Sesjon:`) som del av `Foredrag:`-blokka som
`replace_block` byter ut. `new_foredrag`-heredocen (fanga via
`$(cat <<EOF … EOF)`) har ingen tilsvarande tom linje på slutten — `$()`
strip automatisk alle linjeskift til slutt uansett kor mange tomme linjer
heredocen sjølv inneheld. Nettoresultatet: den tomme linja vart borte i
staden for bytt ut, ei endring som ligg 8 uendra linjer (heile
`slots:`-lista) unna den nye `annotations:`-blokka nær toppen av same
blokk. Git sitt standard kontekstvindauge (3 linjer) er for smalt til å
slå desse to endringane saman til éin hunk, så dei vart viste som to
separate — pluss den forventa tredje hunken for `har_foredrag`.

`har_foredrag`-erstattinga hadde ikkje same problem: den nye
`slot_uri:`-linja hamnar nøyaktig der den tapte tomme linja var (begge
blokker er 5 linjer), så endringa vert eitt samanhengande hunk.

## Fiks

Lagt til `new_foredrag+=$'\n'` rett etter heredoc-fangsten, som gjenskaper
den tapte tomme linja eksplisitt (sidan ho ikkje kan uttrykkjast via ein
tom linje i sjølve heredocen, jf. `$()` sin stripping).

## Verifisert

Live-køyring med `QUICK=true DOMAIN=oreg NAME=quicktest8`
(`< /dev/null`, timeout 60s): diffen i steg 6 viser no nøyaktig to `@@`-
hunkar (Foredrag, har_foredrag). Stadfesta òg at den tomme linja framfor
`Sesjon:` er bevart i det ferdige skjemaet (ingen formateringsregresjon).
Testartefakt rydda opp etterpå.
