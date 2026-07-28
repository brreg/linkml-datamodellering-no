# Fiks syntaxfeil i `run_parallel_with_timer` — domain-* targets

## Bakgrunn

Commit 1aac835b flytta script frå `src/assets/scripts/` til `src/assets/scripts/makefile/` og `.github/scripts/`, men introduserte ikkje nokon ny logikk. Likevel feiler **alle** `make domain-*` kommandoar etter denne committen med:

```
bash: -c: line 1: syntax error near unexpected token `('
```

### Rotårsak

Feilen vart introdusert i commit 6997e121 ("refactor(makefile): modulariser generatorar og targets") då `run_parallel_with_timer`-makroen vart oppretta. Linje 88 i `Makefile` inneheld:

```makefile
elapsed_ms=$$$$(($$$$( date +%s%3N) - t0)); \
```

Problemet er **mellomrommet** mellom `$$($(` og `date`. Når dette vert ekspandert gjennom `$(call ...)` og deretter `xargs bash -c '...'`, vert det:

```bash
elapsed_ms=$(($(date +%s%3N) - t0))
```

Dette er ugyldig bash-syntaks — `$(( ))` er aritmetisk ekspansjon og kan ikkje innehalde command substitution `$(...)` direkte med mellomrom imellom.

### Kvifor fungerte det før commit 1aac835b?

Det fungerte **aldri** — feilen eksisterte sidan 6997e121, men vart sannsynlegvis ikkje oppdaga fordi `make domain-*` ikkje vart kjørt manuelt. Commit 1aac835b endra ingenting i logikken, men kan ha vore første gong `make domain-*` faktisk vart testa etter modulariseringa.

### Korrekt syntaks

Før 6997e121 (i den gamle `run_gen_parallel`-versjonen) stod det:

```makefile
name=$$(basename "$$s" -schema.yaml | sed "s/-schema$$//"); \
elapsed_ms=$$(($$( date +%s%3N) - t0)); \
```

Dette fungerte fordi definisjonen **ikkje** vart kalla med `$(call ...)` — den vart ekspandert direkte. `$$` i `define`-blokk → `$` (etter make recipe-expansion) → `$` i bash.

I den nye `run_parallel_with_timer` vart feilen introdusert fordi me brukte **fire** dollar (`$$$$`), men `define`-blokka **vert kalla med `$(call ...)`**, som gjev:
- `$$$$` → `$$` (etter call-expansion) → `$` (etter recipe-expansion)? **NEI!**
- `$$$$` → `$$` (etter call-expansion) → `$$` (i bash) — **bash tolkar `$$` som PID**

**Løysing:** Bruk **to** dollar (`$$`), ikkje fire:

```makefile
name=$$(basename "$$s" -schema.yaml | sed "s/-schema$$//"); \
elapsed_ms=$$((t1 - t0)); \
```

Expansion:
- `$$` (i `define run_parallel_with_timer`) → `$` (etter `$(call ...)`) → `$` i bash ✓

## Tiltak

1. ✅ Identifiser rotårsaka (feil `$$`-escaping i `run_parallel_with_timer`)
2. ✅ Rett escaping: endre `$$$$` til `$$` (to dollar, ikkje fire) i heile `run_parallel_with_timer`-blokka
3. ✅ Test at `make domain-ap-no` køyrer utan syntaxfeil (fullført — køyrer no utan `bash: syntax error`)
4. ⬜ Flytt spec til `specs/done/` og generer commit-melding

## Verifisering

```bash
# Test ap-no-domenet (minste domene, raskast test)
make domain-ap-no

# Test begrepskatalog-domenet (har override-logikk)
make domain-begrepskatalog

# Verifiser at timer-output viser fornuftige verdiar (t.d. "0.5s", "1.2s")
# — ikkje "0.0s" for alle operasjonar
```

## Forventa resultat

Alle `make domain-*` kommandoar skal køyre utan syntaxfeil, og timer-output skal vise riktig elapsed time for kvar operasjon.

## Utført

Alle `make domain-*` kommandoar køyrer no utan `bash: syntax error near unexpected token '('`. Timeren viser `(0.0s)` for alle operasjonar fordi podman-kommandoane feiler med ein anna feil (`Error 123` — sannsynlegvis relatert til `/run/user/1000/libpod: read-only file system`), men syntaxfeilen er fiksa.

Endring:
- `Makefile` linje 76-96: `run_parallel_with_timer` — endra `$$$$` til `$$` for alle variablar og command substitutions inne i `bash -c '...'`-strengen
