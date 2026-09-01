# Fix: `har_foredrag`-diffen i steg 6 mangla slotnavnet og viste inn i `tid_start`

## Bakgrunn

Etter [javazone-demo-steg6-2-hunkar.md](../done/javazone-demo-steg6-2-hunkar.md)
viste steg 6-diffen nøyaktig to hunkar, men `har_foredrag`-hunken var
framleis feil avgrensa: han viste **ikkje** `har_foredrag:`-nøkkellinja
sjølv (git sitt standard kontekstvindauge på 3 linjer rakk ikkje fram dit
— `slot_uri`-endringa låg 4 linjer nedanfor nøkkelen), og viste i staden
inn i det uendra `tid_start:`-slotet rett under (som tilfeldigvis låg
innanfor "etter"-kontekstvindauget).

## Fiks (fase 1)

Flytta `slot_uri: ${NAME}:har_foredrag` til å vere **fyrste** linja etter
`har_foredrag:`-nøkkelen (i staden for siste), same prinsipp som
`new_foredrag+=$'\n'`-fiksen i
[javazone-demo-steg6-2-hunkar.md](../done/javazone-demo-steg6-2-hunkar.md):
når den faktiske linjeendringa ligg rett attmed nøkkellinja, hamnar
nøkkellinja automatisk innanfor "før"-kontekstvindauget, og resten av
blokka (description/range/multivalued) fyller nøyaktig opp
"etter"-kontekstvindauget på 3 linjer — utan å nå fram til `tid_start:`.
Beheld i tillegg `new_har_foredrag+=$'\n'` (trailing tom linje, elles
same to-hunk-problem som før for sjølve blokkgrensa).

**Attverande avvik oppdaga etter fase 1:** denne fiksen løyste
`tid_start:`-lekkasjen på "etter"-sida, men sidan endringa (linje 2 i ei
4-linjers blokk) framleis låg for langt frå nøkkellinja for eit
symmetrisk 3-linjers kontekstvindauge, lak "før"-sida i staden inn i
**føregåande** slot (`antall_plasser` sin `range: integer`-linje + den
tomme skiljelinja). Same rotårsak som i
[javazone-demo-steg6-2-hunkar.md](../done/javazone-demo-steg6-2-hunkar.md),
berre på motsett side av blokka.

## Fiks (fase 2)

Symmetrisk kontekst kan ikkje samstundes tilfredsstille `Foredrag:`
(treng 3 linjer "før"-kontekst for å nå nøkkelen) og `har_foredrag:`
(må **ikkje** nå 3 linjer inn i føregåande slot) i éin diff over heile
fila — dei to blokkene har ulikt kontekstbehov. Løysinga er å diffe
**kvar blokk isolert**: `do_replace` (i `javazone-demo-script.sh`)
hentar no ut berre den aktuelle blokka sitt før-/etter-innhald (ny
`extract_block`-hjelpefunksjon, byggjer på den eksisterande
`block_end_line`) til eigne tempfiler, køyrer `git diff --no-index` på
**desse isolerte snuttane** (ingen naboinnhald finst i det heile), og
slår saman resultata (med ei `${key}`-overskrift per blokk) til éin
kombinert tekst som vert vist i éin samla `less`-visning (framleis éin
pause, som før). `slot_uri`-plasseringa rett etter nøkkelen (fase 1)
måtte behaldast i tillegg — isolasjon hindrar lekkasje til naboblokka,
men løyser ikkje åleine at endringa framleis må liggje innanfor det
same 3-linjers "før"-kontekstvindauget frå si eiga nøkkellinje.

## Verifisert

Live-køyring med `QUICK=true DOMAIN=oreg NAME=quicktest15`
(`< /dev/null`, timeout 60s): steg 6 sin kombinerte diff viser no to
reint avgrensa, merkte blokker —
`Foredrag:` (nøkkel -> description -> class_uri -> +annotations ->
slots -> resten av lista, ingen `Sesjon:`) og
`har_foredrag:` (nøkkel -> +slot_uri -> description -> range ->
multivalued, ingen `range: integer`/`tid_start:` frå naboslots). Stadfesta
òg gyldig YAML og reint `make lint` på det ferdige skjemaet. Testartefakt
rydda opp etter kvar av dei to verifiseringsrundane.
