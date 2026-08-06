# Dokumenter make-target som er wrapparar rundt andre make-target

## Bakgrunn

`COMMANDS.md` dokumenterer alle make-target i repoet, men gjer i dag ikkje
tydeleg kva target som **wrappar** eit anna target — altså target der
oppskrifta sitt hovudarbeid er å kalle `$(MAKE) <anna-target>` i staden for
å gjere arbeidet sjølv. Dette gjer det vanskeleg for lesaren å forstå:

1. Kva som faktisk skjer når eit target køyrer (t.d. at
   `mcp-linkml-valider-modell` ikkje validerer sjølv, men delegerer til det
   interne targetet `_mcp-valider-modell-with-header`)
2. At det finst **to ulike mønster** i kodebasen for "bygg container-image
   berre viss det manglar": eit rekursivt `$(MAKE)`-kall bak ein
   `podman image exists`-sjekk (brukt 4 stader), og ein vanleg Make-
   prerequisite (`target: build-docker-*`, brukt ~7 stader) — som **alltid**
   køyrer biletbygginga på nytt sidan `build-docker-*`-targeta er `.PHONY`.
   Dette er ein reell åtferdsskilnad (rebuild kvar gong vs. berre ved behov),
   ikkje berre ein stilskilnad.
3. At to target i dagens `COMMANDS.md` alt er merkte "**Convenience
   wrapper**" (`validate-informasjonsmodell-instance` og
   `validate-modellkatalog-instance`) — men denne merkelappen er misvisande:
   ingen av dei to kallar `make validate-instance` via `$(MAKE)`. Dei
   gjenbruker berre same underliggande `linkml validate`-logikk med
   auto-utleia SCHEMA/INSTANCE-stiar. Presiser merkelappen slik at lesaren
   ikkje trur det er eit rekursivt make-kall.

Kartlegging gjort ved `grep -rn '\$(MAKE)' make/*.mk Makefile` og lesing av
`make/40-validation.mk`, `make/60-mcp.mk`, `make/70-scaffolding.mk`,
`make/90-tools.mk`, `make/30-instances.mk` og `Makefile`.

### Funne wrapper-target (reelle `$(MAKE)`-kall)

| Target | Kallar | Kvifor |
|---|---|---|
| `mcp-linkml-valider-modell` | `_mcp-valider-modell-with-header` (internt) | Detekterer POLICY frå build.yaml (eller bruker eksplisitt `POLICY=`), sender så vidare til det interne targetet som gjer sjølve valideringa |
| `gource-preview` | `_gource-render` (internt) | Set `GOURCE_OUTFILE/EXTRA_FLAGS/FPS/FFMPEG_PRESET` for rask 720p-preview, kallar så delt render-oppskrift |
| `gource-video` | `_gource-render` (internt) | Same mønster som over, men 1080p full kvalitet |
| `mcp-linkml-modell-utkast` | `roundtrip-json-schema` (betinga) | Etter generering av eit JSON Schema-utkast køyrer targetet automatisk ein roundtrip-test dersom `SCHEMA` er ei `.json`-fil |

### Funne "bygg-image-berre-viss-manglar"-vakt (same `$(MAKE)`-mønster)

| Target | Kallar (viss image manglar) |
|---|---|
| `_mcp-valider-modell-with-header` | `build-docker-mcp-validator` |
| `validate-capture` | `build-docker-mcp-validator` |
| `mcp-linkml-begrep-utkast-list-profiles` | `build-docker-mcp-begrep-utkast` |
| `new-modell` | `build-docker-mcp-modell-utkast` |

### Kontrasterande mønster (vanleg Make-prerequisite, IKKJE `$(MAKE)`-wrapper)

Desse target listar `build-docker-*` som ein vanleg prerequisite
(`target: build-docker-x`). Sidan `build-docker-*`-target er `.PHONY`,
tyder dette at biletet **vert bygd på nytt kvar einaste gong**, ikkje berre
når det manglar:

`mcp-linkml-valider-modell-smoke`, `mcp-linkml-valider-modell-test`,
`mcp-linkml-modell-utkast-smoke`, `mcp-linkml-modell-utkast-test`,
`mcp-linkml-begrep-utkast-smoke`, `gource-preview`, `gource-video`

(Merk: `gource-preview`/`gource-video` opptrer i **begge** tabellane — dei
har `build-docker-gource` som vanleg prerequisite, OG kallar
`_gource-render` via `$(MAKE)`.)

### Konseptuelle wrapparar (ikkje `$(MAKE)`-kall, men merkte "wrapper" i dag)

| Target | Noverande merkelapp i COMMANDS.md | Faktisk åtferd |
|---|---|---|
| `validate-informasjonsmodell-instance` | "Convenience wrapper for `make validate-instance`" | Kallar **ikkje** `make validate-instance`. Køyrer sitt eige script `validate-modelldcat.py` via `$(LINKML_RUN)`, med auto-utleia sti til `metadata/modelldcat.yaml` |
| `validate-modellkatalog-instance` | "Convenience wrapper for `make validate-instance`" | Kallar **ikkje** `make validate-instance`. Køyrer same underliggande `linkml validate`-kommando direkte, med SCHEMA/INSTANCE auto-utleia frå `ORG=` |

## Steg

1. Legg til eit nytt avsnitt `## Wrapper-target` i `COMMANDS.md` (rett etter
   `## Logging`, før `## Container-image-bygging`) med dei tre tabellane
   over (reelle `$(MAKE)`-wrapparar, bygg-berre-viss-manglar-vakt,
   kontrasterande vanleg-prerequisite-mønster), pluss ei kort forklarande
   avsnitt om skilnaden mellom dei.
2. Rett dei to eksisterande "Convenience wrapper"-setningane i
   `COMMANDS.md` (linje ~173 og ~176, i tabellen under "Vedlikehald") slik
   at dei presist skildrar at target **gjenbruker same underliggande
   valideringslogikk med auto-utleia stiar**, ikkje at dei kallar
   `make validate-instance` via `$(MAKE)`.
3. Legg inn ei kort tverreferanse-linje i `make/README.md` sitt
   "Konvensjonar"-avsnitt som peikar til det nye `## Wrapper-target`-
   avsnittet i `COMMANDS.md` (unngå duplisering, jf. CLAUDE.md § DRY).
4. Ingen kodeendringar — reint dokumentasjonsarbeid, ingen `make lint`/
   `make test` naudsynt.

## Handlingsliste

- [x] Steg 1: nytt `## Wrapper-target`-avsnitt i `COMMANDS.md`
- [x] Steg 2: rett dei to misvisande "Convenience wrapper"-setningane
- [x] Steg 3: tverreferanse i `make/README.md`
- [x] Steg 4: sjølvsjekk — les gjennom `COMMANDS.md` og `make/README.md` for
      konsistens

## Utført

- `COMMANDS.md`: nytt avsnitt `## Wrapper-target` (etter `## Logging`, før
  `## Container-image-bygging`) med tre tabellar — reelle `$(MAKE)`-
  wrapparar, "bygg-image-berre-viss-manglar"-vakt, og forklaring av det
  kontrasterande vanleg-prerequisite-mønsteret som rebyggjer image kvar
  gong. Pluss eit avsnitt om dei to konseptuelle wrapparane.
- `COMMANDS.md`: retta dei misvisande "Convenience wrapper for
  `make validate-instance`"-setningane for `validate-informasjonsmodell-instance`
  og `validate-modellkatalog-instance` (dei kallar ikkje `validate-instance`
  via `$(MAKE)`) — lenkjer no til `§ Wrapper-target`.
- `make/README.md`: kort tverreferanse til `COMMANDS.md § Wrapper-target` i
  "Konvensjonar"-avsnittet.
- Ingen kodeendringar — reint dokumentasjonsarbeid.
