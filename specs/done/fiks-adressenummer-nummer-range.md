# Fiks Adressenummer.nummer sin range (CURIE-feil i linkml-convert)

## Bakgrunn

`make domain-oreg` feila i `linkml-convert`-steget for
`enhetsregisteret-bvrinn-eksempel.yaml`:

```
ValueError: File "enhetsregisteret-bvrinn-eksempel.yaml", line 44, col 13: Unknown CURIE prefix: @base
```

**Rotårsak, stadfesta ved kodelesing og isolert testkøyring:**

Den globale sloten `nummer` (`enhetsregisteret-bvrinn-schema.yaml:1745-1748`,
`range: Adressenummer`) vert brukt av to klassar med to ulike tydingar:

- `Vegadresse.nummer` (linje 453/468) — **korrekt** brukt som ei lenkje (URI-referanse)
  til ein `Adressenummer`-instans, i tråd med "lenking fremfor inlining"-prinsippet.
  Eksempelfila stadfestar dette: `nummer: https://example.org/adressenummer/1`.
- `Adressenummer.nummer` (linje 483-499) — skal halde **sjølve talet** (t.d. `"42"`),
  men manglar `range`-overstyring i `slot_usage`, og arvar difor same
  `range: Adressenummer` som `Vegadresse.nummer`. Eksempelfila har korrekt
  `nummer: "42"` (ein bar streng), men skjemaet forventar ein klassereferanse.

Skjemaet har alt ein føremålsbygd type `Husnummer` (`xsd:string`-subtype, linje 93)
som ikkje vert brukt nokon stad — parallell til `Husbokstav`, som
`Adressenummer.bokstav` korrekt brukar via `range: Husbokstav` (linje 1756).

Når `linkml-convert` serialiserer `Adressenummer.nummer: "42"` til RDF, tolkar
`rdflib_dumper` verdien som ein identifikator som må URI-oppløysast (sidan sloten sin
`range` peikar til ein klasse). `"42"` har korkje `://` eller `:`, så oppløysinga fell
tilbake til eit "base"-namnerom som ikkje er definert — difor
`Unknown CURIE prefix: @base`.

**Verifisert fiks:** legg til `range: Husnummer` i `Adressenummer` sin eksisterande
`slot_usage.nummer`-blokk (linje 493-496), analogt med `bokstav: range: Husbokstav`.
Testa isolert med `linkml-convert` mot ein patcha kopi av skjemaet — konverteringa
lukkast, og resulterande Turtle er korrekt:
- `Adressenummer.nummer` → literal `"42"`
- `Vegadresse.nummer` → uendra URI-referanse til `Adressenummer`-instansen

## Steg

1. **Legg til** `range: Husnummer` i `slot_usage.nummer` under `Adressenummer`-klassen
   i `src/linkml/oreg/enhetsregisteret-bvrinn/enhetsregisteret-bvrinn-schema.yaml`.
2. **Lint og valider:**
   ```
   make lint SCHEMA=src/linkml/oreg/enhetsregisteret-bvrinn/enhetsregisteret-bvrinn-schema.yaml
   make validate-instance SCHEMA=src/linkml/oreg/enhetsregisteret-bvrinn/enhetsregisteret-bvrinn-schema.yaml INSTANCE=src/linkml/oreg/enhetsregisteret-bvrinn/examples/enhetsregisteret-bvrinn-eksempel.yaml
   ```
3. **Køyr** `make roundtrip SCHEMA=src/linkml/oreg/enhetsregisteret-bvrinn/enhetsregisteret-bvrinn-schema.yaml`
   og stadfest at TTL-roundtrip lukkast utan `Unknown CURIE prefix`-feil.
4. **Køyr** `make domain-oreg` (eller `make convert-rdf`) og stadfest at
   `linkml-convert`-steget for `oreg/enhetsregisteret-bvrinn` no lukkast.

## Handlingsliste

- [x] Legg til `range: Husnummer` i `Adressenummer.slot_usage.nummer`
- [x] `make lint` og `make validate-instance` grønt
- [x] `make roundtrip` — `Unknown CURIE prefix`-feilen er borte (sjå "Utført")
- [x] Stadfest `linkml-convert`-steget lukkast (verifisert direkte, sjå "Utført")

## Utført

Lagt til `range: Husnummer` i `Adressenummer` sin `slot_usage.nummer`
(`enhetsregisteret-bvrinn-schema.yaml:493-496`).

Verifisert:
- `make validate-instance` — "No issues found"
- `make lint` — same eine åtvaring (`dct` vs. `dcterms`) som fanst før endringa
  (stadfesta med `git stash` + re-køyring), ikkje knytt til denne fiksen
- Direkte `linkml-convert`-kall (yaml→ttl) mot det retta skjemaet lukkast (exit 0,
  tidlegare `ValueError: Unknown CURIE prefix: @base`). Kontrollert resulterande
  Turtle: `Adressenummer.nummer` → literal `"42"`, `Vegadresse.nummer` → uendra
  URI-referanse til `Adressenummer`-instansen
- `make roundtrip SCHEMA=...` — `roundtrip-json` OK. `roundtrip-ttl` kjem no forbi
  CURIE-feilen (som tidlegare stoppa heile konverteringa) og feilar i staden på eit
  **separat, urelatert** avvik: `innsendingstidspunkt` (dateTime-felt) roundtrippar
  `2026-07-04T10:30:00` → `2026-07-04 10:30:00` (mellomrom i staden for `T`) via
  TTL. Stadfesta uavhengig av denne fiksen ved manuell yaml→json/yaml→ttl→yaml→json-
  samanlikning — diff-en gjeld berre dette eine datetime-feltet, ingenting knytt til
  `nummer`/`Husnummer`. Ikkje handtert her, ikkje dokumentert i `bugs/` frå før
  (sjekka) — rapportert til brukar, avventar eiga avklaring/spec.

**Ekstra følgjefunn (utanfor scope, rapportert til brukar):** `linkml-convert`-løkka
i både `Makefile:98-112` (`convert-rdf`), `Makefile:115-139` (`convert-data`) og
`make/20-domain-targets.mk:46-58` (`domain_target`) sjekkar ikkje exit code frå
`linkml-convert`-kallet og bruker ikkje `run_logged` — ein feilande konvertering (som
CURIE-bugen over) skriv full traceback til stdout, men løkka held fram og skriv
likevel ei "→ linkml-convert ... (Xs)"-fullført-linje for den feila fila, og heile
`make`-målet feilar ikkje. Dette er eit brot på CLAUDE.md sin "Ingen stille
feil"-regel (feilen er synleg i loggen, men vert ikkje handsama som ein feil — CI
ville ikkje raud-merke bygget). Ikkje retta her.
