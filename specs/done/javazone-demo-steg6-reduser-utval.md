# Plan: Reduser steg 6 sitt rettingsutval til éin klasse/éin slot

## Bakgrunn

Steg 6 (`Adresser funn frå valideringa`) i `javazone-demo-script.sh`
retta i dag **to** klassar (`Foredrag`, `Sesjon` — begrepsidentifikator)
og **to** slots (`har_foredrag`, `tid_start` — slot_uri) som eit
"representativt utval" av dei seks nye klassane/atten nye slotsa. Brukaren
ønskjer å fjerne `Sesjon`- og `tid_start`-oppdateringa, slik at steget
berre viser mønsteret éin gong per funntype (`Foredrag` for
begrepsidentifikator, `har_foredrag` for slot_uri).

## Steg

1. Fjern `new_sesjon`- og `new_tid_start`-heredoc-tildelingane
   (`javazone-demo-script.sh`).
2. Fjern `"  Sesjon:" "$new_sesjon"` og `"  tid_start:" "$new_tid_start"`
   frå `do_replace`-kallet.
3. Oppdater narrativteksta rett over (`cat <<EOF` mellom funnoppsummeringa
   og `new_foredrag=`): fjern referansane til `Sesjon:`/`tid_start:`,
   juster "dei fire andre klassane" til "dei fem andre klassane" (fem
   attverande urørte av seks totalt, sidan berre éin no vert retta).
4. Oppdater `specs/backlog/javazone-demo-plan.md` sin tilsvarande
   skildring ("Steget viser retteinga for eit representativt utval — to
   klasser … to slots …") til éin klasse/éin slot.
5. Verifiser: `bash -n`, live-køyring med `QUICK=true` som stadfestar at
   `do_replace`-diffen i steg 6 no berre endrar `Foredrag`/`har_foredrag`
   — `Sesjon`/`tid_start` skal vere uendra (vises berre som kontekst,
   ikkje som +/- i diffen).

## Handlingsliste

| # | Tiltak | Fil |
|---|---|---|
| 1-3 | Fjern Sesjon/tid_start frå heredocs, `do_replace`-kall og narrativtekst | `javazone-demo-script.sh` |
| 4 | Oppdater skildring av representativt utval | `specs/backlog/javazone-demo-plan.md` |
| 5 | Syntakssjekk + live-verifisering | — |

---

## Utført

Gjennomført 2026-09-01. `bash -n` OK. Live-verifisert med
`QUICK=true DOMAIN=oreg NAME=quicktest6` (`< /dev/null`, timeout 60s) —
`git diff --no-index`-utsnittet i steg 6 viser no berre `Foredrag`
(ny `annotations.begrepsidentifikator`) og `har_foredrag` (ny `slot_uri`)
som endra; `Sesjon`/`tid_start` opptrer uendra, berre som kontekstlinjer.
Testartefakt rydda opp etterpå. Ingen avvik frå planen.
