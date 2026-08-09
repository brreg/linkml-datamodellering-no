# Modellmetadata-tabellen skal ikkje omsetjast til nynorsk

**Bakgrunn:** Brukaren presiserte at "Modellmetadata"-tabellen i `index.md` for kvar modell (name, title, description, versjon, lisens, utgjevar, status, endringsdato, utgivelsesdato) skal gjengi verdiane nøyaktig slik dei er skrivne i skjemaet — **ikkje** omsetjast til nynorsk, sjølv om resten av dokumentasjonssida elles følgjer nynorsk-konvensjonen (jf. CLAUDE.md § Skriftspråk: modellering = bokmål, dokumentasjon = nynorsk).

**Verifisert status:** Ingen kodefeil funne. `src/assets/templates/docgen/index.md.jinja2` hentar `schema.title`/`schema.description`/`schema.version` osv. direkte frå skjemaet utan noka omsetjing (`{{ schema.description }}`), og ein programmatisk samanlikning av alle `*-schema.yaml`-filer mot tilhøyrande genererte `index.md` viste **0 avvik**. `mkdocs/docs/automasjon/index-md-struktur.md` dokumenterer allereie at `<schema>-schema.yaml` er "SANNKJELDE for metadata" og at `index.md` "skal aldri redigerast manuelt".

**Problemet dette specen løyser:** Regelen finst i praksis (pipelinen er allereie korrekt), men er **ikkje eksplisitt uttalt** nokon stad at Modellmetadata-tabellen er eit unntak frå nynorsk-konvensjonen for dokumentasjon. Utan eit skriftleg unntak er det ein risiko for at ein framtidig LLM-økt eller bidragsytar — i eit forsøk på å gjere doc-sida "konsekvent nynorsk" — manuelt "rettar" title/description-verdiane i ein generert `index.md`, eller (verre) endrar jinja2-malen/scriptet til å omsetje verdiane. Dette ville bryte sannkjelde-prinsippet (skjemaet er autoritativt for metadataverdiar) og gjere dokumentasjonen usamd med kjeldekoden.

**Mål:** Skriv ned regelen eksplisitt slik at han er handhevbar og synleg for framtidige økter, utan å endre eksisterande (allereie korrekte) genereringslogikk.

**Planlagde steg:**
1. Legg til eit eksplisitt unntak i CLAUDE.md § Skriftspråk: presiser at Modellmetadata-tabellen i genererte `index.md`-sider er eit direkte sitat frå skjemaet (name, title, description m.fl.) og at desse verdiane **aldri** skal omsetjast til nynorsk ved redigering, sjølv om sida elles er nynorsk.
2. Legg til ei tilsvarande presisering i `mkdocs/docs/automasjon/index-md-struktur.md`, seksjon 7 (Modellmetadata) — utdjup det eksisterande "SANNKJELDE for metadata"-punktet med at verdiane skal vere ordrette, ikkje omsette.
3. Ingen kodeendring i `index.md.jinja2` eller `metadata.sh` — begge hentar allereie verdiar direkte utan omsetjing; verifisert i forkant (0 avvik ved samanlikning skjema vs. generert index.md).

**Handlingsliste:**
- [ ] Oppdater CLAUDE.md § Skriftspråk med unntaket for Modellmetadata-tabellen
- [ ] Oppdater `mkdocs/docs/automasjon/index-md-struktur.md` seksjon 7 med presisering om ordrette verdiar
- [ ] Verifiser at ingen kodeendring er naudsynt (allereie gjort — sjå "Verifisert status" ovanfor)

## Tillegg: konkret avvik funne (feltnamnet sjølv)

**Oppdaga:** Brukaren peika på at *feltnamnet* i tabellen — ikkje verdien — var omsett: rada var skriven `| Utgjevar | ... |` (nynorsk stavemåte), medan det underliggjande skjemafeltet er `annotations.utgiver` (bokmål, jf. CLAUDE.md § Silver-annotasjonar). Inkonsistent med nabofeltet `Utgivelsesdato` som allereie brukar bokmål-forma. Dette var altså ikkje berre ein potensiell risiko, men eit reelt avvik i sjølve malen.

**Retta i:**
- `src/assets/templates/docgen/index.md.jinja2` (linje 26): `Utgjevar` → `Utgiver`
- `mkdocs/lib/sections/badges.sh` (linje 21): grep/sed-mønster oppdatert til å matche `Utgiver` i staden for `Utgjevar`
- `CLAUDE.md` (§ Dokumentasjonsportal, to stader): feltlista i skildringa av Modellmetadata-seksjonen oppdatert til `utgiver`
- `mkdocs/docs/automasjon/index-md-struktur.md` (seksjon 7-rada i oversiktstabellen): same retting

**Regenerert:** `make gen-docs` (alle skjema) + `make docs-publish` køyrt. Verifisert at feltnamnet no viser `Utgiver` i badge-rad og Modellmetadata-tabell for alle modellar (t.d. samt-bu). Attverande treff på "Utgjevar" i repoet er urelaterte: ein eigen slot `utgjevar` i `cpsv-ap-no-schema.yaml` (CPSV-AP-NO-domenemodellering, ikkje `annotations.utgiver`-feltet) og tekst i `policies/README.md` — begge utanfor scope for denne retting.

**Status:** Det konkrete avviket (feltnamnet `Utgjevar` → `Utgiver`) er retta og verifisert. Den generelle, føre-var-regelen i "Planlagde steg" 1-2 (eksplisitt unntak i CLAUDE.md § Skriftspråk og index-md-struktur.md) står framleis ope — brukaren har bedt om å berre få specen, ikkje utføring, for den delen.
