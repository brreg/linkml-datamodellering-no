# Plan: Konsekvent DOMAIN/NAME-rekkjefølgje

## Bakgrunn

`make new-modell` og `make remove-modell` viser argumenta sine som
`NAME=<namn> DOMAIN=<domene>` (NAME først), medan `make new-begrepssamling`
viser `DOMAIN=<domain> NAME=<namn>` (DOMAIN først) — inkonsekvent
rekkjefølgje for same to variabelnamn på tvers av target. Brukaren ønskjer
at DOMAIN alltid skal stå før NAME, konsekvent overalt argumentparet
opptrer — i `make help`-output (dvs. `## `-kommentarane som styrer det, jf.
[[make-help-argument-og-farge]]), i feilmeldingar frå scaffolding-skripta,
og i dokumentasjonen (`COMMANDS.md`, `README.md`, mkdocs-rettleiingane).

Kartlegging av alle stader `NAME=` og `DOMAIN=` opptrer saman (utanom
`specs/done/`, som er arkivert og urørt per CLAUDE.md):

| Fil | Kva | Noverande rekkjefølgje |
|---|---|---|
| `make/70-scaffolding.mk` | `new-modell` `## `-kommentar + `Bruk:`-feilmelding | NAME, DOMAIN |
| `make/70-scaffolding.mk` | `remove-modell` `## `-kommentar + `Bruk:`-feilmelding | NAME, DOMAIN |
| `make/70-scaffolding.mk` | `new-begrepssamling` `## `-kommentar + `Bruk:`-feilmelding | DOMAIN, NAME (alt korrekt) |
| `src/assets/scripts/scaffolding/new-modell.sh` | `Bruk: make new-modell ...`-feilmelding | NAME, DOMAIN |
| `src/assets/scripts/scaffolding/remove-modell.sh` | To `Bruk:`/`Køyr med CONFIRM=1`-meldingar | NAME, DOMAIN |
| `COMMANDS.md` | `new-modell`-tabellrad | NAME, DOMAIN |
| `README.md` | `new-modell`-eksempel | NAME, DOMAIN |
| `mkdocs/docs/kom-i-gang/build-config.md` | Løpande tekst | NAME, DOMAIN |
| `mkdocs/docs/kom-i-gang/kommandoar.md` | Kommandotabell | NAME, DOMAIN |
| `mkdocs/docs/kom-i-gang/ny-domenemodell.md` | 4 stader (kodeblokker + løpande tekst) | NAME, DOMAIN |
| `mkdocs/docs/kom-i-gang/ny-org.md` | Kodeblokk | NAME, DOMAIN |
| `mkdocs/docs/automasjon/readme-tabellgenerering.md` | Løpande tekst | NAME, DOMAIN |

**Viktig avgrensing:** Berre den **menneskelesbare** visinga av argumenta
(kommentarar, feilmeldingar, dokumentasjon) endrast. Den **interne**
posisjonelle kallet frå Makefile-oppskrifta til scaffolding-skripta
(`bash .../new-modell.sh "$(NAME)" "$(DOMAIN)"`) og skripta sin eigen
`$1`/`$2`-parsing rørast **ikkje** — det er ei implementasjonsdetalj som
ikkje er synleg for brukaren og uavhengig av `make`-variabelnamn (`NAME=`,
`DOMAIN=`) sin rekkjefølgje på kommandolinja (som uansett ikkje har
betydning for `make`).

## Handlingsliste

1. [x] `make/70-scaffolding.mk`: byt om NAME/DOMAIN i `## `-kommentar og
   `Bruk:`-feilmelding for `new-modell` og `remove-modell`
2. [x] `src/assets/scripts/scaffolding/new-modell.sh`: byt om i
   `Bruk:`-feilmelding
3. [x] `src/assets/scripts/scaffolding/remove-modell.sh`: byt om i dei to
   meldingane
4. [x] `COMMANDS.md`: byt om i `new-modell`-tabellraden
5. [x] `README.md`, mkdocs-rettleiingane (`build-config.md`,
   `kommandoar.md`, `ny-domenemodell.md`, `ny-org.md`,
   `readme-tabellgenerering.md`): byt om alle `new-modell`/`remove-modell`
   NAME/DOMAIN-førekomstar
6. [x] Verifiser med `make help` at `new-modell`/`remove-modell` no viser
   DOMAIN før NAME, og at `new-begrepssamling` er uendra

## Utført

Alle 12 stader kartlagde i «Bakgrunn» er retta til `DOMAIN=<domene> NAME=<namn>`
(unntatt `new-begrepssamling`, som alt var korrekt). `specs/done/` er
medvite urørt (arkivert, jf. CLAUDE.md). `make help` verifisert:

```
make new-modell (DOMAIN=<domene> NAME=<namn>)
make remove-modell (DOMAIN=<domene> NAME=<namn>) [CONFIRM=1]
make new-begrepssamling (DOMAIN=<domain> NAME=<begrepssamling-namn>)
```

Den interne posisjonelle `bash new-modell.sh "$(NAME)" "$(DOMAIN)"`-kallet og
skripta sin `$1`/`$2`-parsing er urørt — berre menneskelesbar tekst
(kommentarar, feilmeldingar, dokumentasjon) vart endra.
