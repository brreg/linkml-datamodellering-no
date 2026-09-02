# Plan: Fiks CodeQL-funn py/illegal-raise i linkml_relative_import_patch.py

**Kortnavn:** `codeql-illegal-raise-last-exc`
**Dato:** 2026-09-02

---

## Bakgrunn

CodeQL flaggar `py/illegal-raise` på
`src/assets/scripts/utils/linkml_relative_import_patch.py:259`
(`raise last_exc` i `hbopen_with_retry()`, del av tiltak 3 —
gjenforsøksfunksjonen kring `hbreader.hbopen()`, sjå modulens
toppkommentar punkt 3).

`last_exc` vert deklarert som `None` (linje 243) og berre tilordna ein
`Exception`-instans inne i `except`-blokka (linje 250). CodeQL kan ikkje
statisk prove at `except`-blokka faktisk vert nådd før `raise last_exc` på
linje 259 — dersom `retries <= 0` køyrer `for attempt in range(1, retries
+ 1)` null gongar, `last_exc` forblir `None`, og `raise None` fører til
`TypeError: exceptions must derive from BaseException` i staden for den
tiltenkte nettverksfeilen. Alle noverande kallarar brukar
`apply()`/`_apply_retry_patch()` med standardverdien `retries=3`, så
feilen slår ikkje inn i praksis i dag — men CodeQL sitt statiske
typesystem ser `last_exc: Exception | None` og flaggar det korrekt som
eit potensielt illegalt `raise`.

Dette er i tråd med prosjektets prinsipp «Ingen stille feil» (CLAUDE.md)
— ein utilsikta `TypeError` ved `retries=0` er ei forvirrande feilmelding
som skjuler den reelle årsaka (misbruk av funksjonen), ikkje ei tydeleg
logga feil.

## Tiltak

1. **Skil dei to utfalla eksplisitt** i `hbopen_with_retry()`
   (`src/assets/scripts/utils/linkml_relative_import_patch.py`, linje
   241-259):
   - Etter løkka: dersom `last_exc is not None`, `raise last_exc` (uendra
     åtferd for det normale tilfellet — nettverksfeil etter uttømde
     forsøk).
   - Elles (`last_exc is None`, altså `retries <= 0`): `raise
     RuntimeError(...)` med ei tydeleg feilmelding som forklarer at
     `hbopen_with_retry` vart kalla med `retries <= 0` og difor aldri
     gjorde noko forsøk. Løyser CodeQL-funnet, sidan begge
     `raise`-greinene no statisk garantert kastar ein gyldig
     `Exception`-instans.
2. **Verifiser** — `python3 -m py_compile
   src/assets/scripts/utils/linkml_relative_import_patch.py` for å
   stadfeste syntaks. Ingen eksisterande test dekker
   `hbopen_with_retry()` direkte (retry-patchen er eit tynt lag rundt eit
   nettverkskall) — ingen ny test er naudsynt sidan `retries=0` aldri vert
   brukt av nokon kallar i dag; endringa er ei rein type-/robustheitsfiks.
3. **Stadfest i CodeQL** — etter push til `main`, sjekk at funnet vert
   automatisk lukka:
   `gh api repos/brreg/linkml-datamodellering-no/code-scanning/alerts --jq '.[] | select(.rule.id=="py/illegal-raise" and .state=="open")'`
   bør ikkje lenger vise treff for denne fila/linja.

## Utført

Tiltak 1-2 gjennomførte 2026-09-02:

1. `hbopen_with_retry()` skiller no dei to utfalla: `raise last_exc` når
   `last_exc is not None` (uendra åtferd), elles `raise RuntimeError(...)`
   som forklarer at `retries <= 0` gjorde at ingen forsøk vart gjort.
2. Verifisert med `python3 -m py_compile
   src/assets/scripts/utils/linkml_relative_import_patch.py` — OK.

Tiltak 3 (stadfesting i CodeQL) attstår til etter commit/push av
brukaren — ikkje utført av LLM, jf. prinsippet om at LLM aldri kjører
commit/push/add.
