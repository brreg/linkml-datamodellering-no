# Oppdatering av dokumentasjonsportalen

To statiske sider er utdaterte: `mkdocs/docs/index.md` og `mkdocs/docs/ny-domenemodell.md`.
Begge er handskrivne og vert ikkje rørte av `make publish`.

---

## Konkrete feil i dag

### `index.md` (portalen si framside)

| Feil | Korrekt |
|---|---|
| `POLICY=fair` finst ikkje | Skal vere `POLICY=bronze`, `silver` eller `gold` |
| Manglar `ngr-adresse` i oversikta | Skjemaet eksisterer |
| Manglar `samt-bu` i oversikta | Skjemaet eksisterer |
| Ingen omtale av `make new-model` | Primærkommandoen for å kome i gang |
| Ingen omtale av bronze/silver/gold-policyar | Sentralt i validerings-arbeidsflyten |

### `ny-domenemodell.md` (rettleiing for nye modellarar)

| Feil | Korrekt |
|---|---|
| Steg 1: "Opprett skjemafilen manuelt" | `make new-model NAME=… DOMAIN=…` gjer dette |
| Steg 2: "Legg til modellnamn i Makefile" | Auto-oppdaging, ingen Makefile-endring nødvendig |
| Steg 3: "Lag eksempel-datasett manuelt" | `make new-model` oppretter eksempelfila automatisk |
| `POLICY=fair` i alle eksempel | Finst ikkje; bruk `bronze`, `silver` eller `gold` |
| Sjekkliste: `POLICY=fair` | Same feil |

---

## Forslag til strategi

### `index.md` — auto-generer frå README.md

`publish.sh` skriv allereie om `mkdocs.yml` og alle domain- og schema-index-sider.
Det naturlege er å la den òg generere rot-`index.md` frå `README.md`,
slik at portalen sin framside alltid er i sync med repo-forsida.

Nødvendig transformasjon i `publish.sh`:
- Strip `[CLAUDE.md](CLAUDE.md)`- og `[COMMANDS.md](COMMANDS.md)`-lenkjer
  (desse finst ikkje i portalen — erstatt med klartekst)
- Behold alt anna som-er

```bash
# Legg til i publish.sh, etter at mkdocs/docs/ er oppretta:
sed \
  -e 's|\[CLAUDE.md\](CLAUDE.md)|`CLAUDE.md`|g' \
  -e 's|\[COMMANDS.md\](COMMANDS.md)|`COMMANDS.md`|g' \
  "$REPO_ROOT/README.md" > "$DOCS/index.md"
```

**Fordel:** `index.md` kan ikkje drifta frå README igjen.
**Ulempe:** Portalen får ikkje eigen, meir utfyllande framside utan at README vert lenger.

### `ny-domenemodell.md` — omskriv manuelt

Denne sida er ei utfyllande rettleiing og er naturleg ulik README.
Den skal ikkje auto-genererast, men oppdaterast til å reflektere arbeidsflyten slik han er i dag.

Konkrete endringar:

**Del opp i to spor:**

```
Spor A — Kome raskt i gang (make new-model)
Spor B — Forstå strukturen (manuell oppsett)
```

Dei fleste brukarar treng berre spor A. Spor B er for dei som vil forstå kva `make new-model` faktisk gjer, eller lage noko utanfor konvensjonane.

**Oppdatert steg-for-steg (spor A):**

```
1. make new-model NAME=<namn> DOMAIN=<domene>
   → oppretter src/linkml/<domene>/<namn>/<namn>-schema.yaml
   → oppretter examples/<domene>/<namn>-eksempel.yaml
   → passerer bronze utan redigering

2. Rediger skjemaet: legg til klasser, slots og importar etter behov

3. Valider underveis:
   make mcp-validate SCHEMA=<sti> POLICY=bronze
   make mcp-validate SCHEMA=<sti> POLICY=silver
   make mcp-validate SCHEMA=<sti> POLICY=gold

4. make test   ← lint + validering + alle generatorar
```

**Policyane** (erstatt omtalen av `POLICY=fair`):

| Policy | Sjekkar |
|---|---|
| `bronze` | `id`, `name`, `description`; alle klasser har identifikator og begrepsreferanse |
| `silver` | Bronze + importerer DCAT-AP-NO og DQV-AP-NO |
| `gold` | Silver + FAIR F1–R1.3: `class_uri`, lisens, proveniens m.m. |

**Fjern heilt:**
- "Steg 2 — Legg til i Makefile" (auto-oppdaging)
- All omtale av `POLICY=fair`
- "tests/fixtures/"-seksjon (ikkje relevant for nye modellarar)

**Behald:**
- Importhierarkiet (framleis korrekt)
- "Kva får du frå AP-NO-profilene"-tabellen
- FAIR-konformitetsseksjonen (men rett opp `POLICY=fair` → `POLICY=gold`)
- Modelleringsprinsippa (framleis korrekte)
- Sjekklista (men fjern `POLICY=fair`)

---

## Rekkefølge

1. Oppdater `publish.sh` med `sed`-transformasjonen (éi linje)
2. Omskriv `mkdocs/docs/ny-domenemodell.md`
3. Slett den gamle statiske `mkdocs/docs/index.md` (publish.sh vil generere ny)
4. Køyr `make publish && make docs-serve` og verifiser begge sidene
