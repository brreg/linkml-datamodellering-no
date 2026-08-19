# Plan: `log-mcp-validate` — ulik alternasjons-notasjon i `make help`/`COMMANDS.md`

## Bakgrunn

Brukaren peika på at `make log-mcp-validate` er ulikt dokumentert i
`COMMANDS.md` og `make help` (kjelde: `make/40-validation.mk`).

**Noverande `make help`** (frå `## `-kommentaren):
```
make log-mcp-validate (MANIFEST=<sti> eller SCHEMA=<sti> POLICY=<policy>)
```
Bruker det norske ordet **«eller»** for alternasjon.

**Noverande `COMMANDS.md`:**
```
make log-mcp-validate SCHEMA=<sti> POLICY=<policy>
```
med `MANIFEST=<sti>` nemnt berre i prosa («Alternativt `MANIFEST=<sti>` i
staden for `SCHEMA=`/`POLICY=`»).

To ulike avvik samstundes:

1. **`## `-kommentaren er sjølv inkonsekvent** med resten av repoet:
   `log-mcp-validate` er den **einaste** staden av 17 alternasjons-tilfelle
   som brukar ordet «eller» — dei 16 `gen-*`/`gen-informasjonsmodell-instance`-
   targeta brukar konsekvent `|`-teikn (t.d.
   `[DOMAIN=<domene>|SCHEMA=<sti>]`).
2. **COMMANDS.md viser berre éin av dei to gyldige måtane** å kalle
   kommandoen på i sjølve kommandosyntaksen — `MANIFEST`-alternativet er
   heilt utelate frå kommandocella, berre nemnt i prosa. Dette skil seg
   frå `DOMAIN`/`SCHEMA`-alternasjonen andre stader, der COMMANDS.md viser
   **begge** alternativa (om enn med annan hakeparentes-stil enn
   `make help`) — jf. den medvitne aksepterte stilskilnaden dokumentert i
   [[make-help-argument-og-farge]].

## Plan

1. `make/40-validation.mk`: byt `eller` → `|` i `log-mcp-validate` sin
   `## `-kommentar, for konsistens med dei 16 andre alternasjons-tilfella:
   ```
   log-mcp-validate: ## Policy-validering med full JSON-logg (MANIFEST=<sti>|SCHEMA=<sti> POLICY=<policy>)
   ```
2. `COMMANDS.md`: oppdater kommandocella til å vise same alternasjon,
   ikkje berre éin av dei to vegane:
   ```
   `make log-mcp-validate (MANIFEST=<sti>|SCHEMA=<sti> POLICY=<policy>)`
   ```
   Kort ned den overlappande prosa-forklaringa («Alternativt
   `MANIFEST=<sti>`…») sidan ho no er redundant med sjølve
   kommandosyntaksen.

## Filer som vert påverka

- `make/40-validation.mk`
- `COMMANDS.md`

## Handlingsliste

1. [x] Rett `## `-kommentaren i `make/40-validation.mk`
2. [x] Rett kommandocella i `COMMANDS.md`, kort ned redundant prosa
3. [x] Verifiser med `make help` at linja renderer korrekt (heile gruppa
   framleis fargelagt grøn som éin blokk, sidan ho er parentes-omslutta)

## Utført

`eller` → `|` i `make/40-validation.mk` sin `## `-kommentar for
`log-mcp-validate`, no einaste konsistente notasjon med dei 16 andre
alternasjons-tilfella. `COMMANDS.md` sin kommandocelle oppdatert til å
vise heile alternasjonen (`(MANIFEST=<sti>\|SCHEMA=<sti> POLICY=<policy>)`,
`\|` escapa for å ikkje bryte tabellcella), prosaen korta ned sidan
MANIFEST-alternativet no er synleg direkte i kommandosyntaksen.

`log_error`-meldinga i sjølve oppskrifta («Oppgi anten MANIFEST=<sti>
eller både SCHEMA=<sti> og POLICY=<policy>») er urørt — det er naturleg
norsk prosa i ei feilmelding, ikkje ein plasshaldar-notasjon, og fell
difor utanfor omfanget.

**Verifisert:** `make help` viser
`make log-mcp-validate (MANIFEST=<sti>|SCHEMA=<sti> POLICY=<policy>)`,
heile gruppa farga grøn som éin blokk (parentes = obligatorisk, som
venta). `COMMANDS.md` sin rad har framleis 4 gyldige tabellceller.
