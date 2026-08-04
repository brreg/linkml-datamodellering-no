# Rest-fiks: fleire relative COMMANDS.md-lenker som 404-ar på portalen

## Bakgrunn

Følgjer opp `specs/done/generator-lenker-404-fiks.md` (Generator-kolonnene).
På oppfølgingssjekk fann eg to fleire stader med same rotårsak — relativ
`COMMANDS.md`-lenke som 404-ar på den publiserte mkdocs-portalen, sidan
`COMMANDS.md` aldri vert kopiert til `mkdocs/docs/`:

1. **`README.md:141`** — `[CLAUDE.md](CLAUDE.md)` og `[COMMANDS.md](COMMANDS.md)`.
   Denne var til no "løyst" ved at `mkdocs/publish.sh` (Steg 3) sletta heile
   linja frå den publiserte `index.md` med ein sed-regel — eit workaround som
   skjulte problemet i staden for å fikse det, og fjerna linja frå portalen
   heilt.
2. **`mkdocs/docs/modellmanifest-generering.md:233`** — `[COMMANDS.md](../../COMMANDS.md)`
   i "Relaterte dokument"-seksjonen. Same seksjon har to tilsvarande broten
   lenker til `specs/done/*.md` (same rotårsak — `specs/` er heller ikkje
   publisert), men brukar valde å avgrense denne rettinga til berre
   COMMANDS.md-lenka.

`mkdocs/docs/index.md` (linje 231-247, 262, 276-281) har same broten mønster,
men er eit build-artefakt generert frå README.md — vert automatisk retta ved
neste `make docs-publish` og krev ingen eigen endring.

## Steg

### 1. `README.md:141`

Endre til absolutte GitHub-URL-ar, same mønster som resten av README.md:

```
Sjå [CLAUDE.md](https://github.com/brreg/linkml-datamodellering-no/blob/main/CLAUDE.md) for modelleringsprinsipp og [COMMANDS.md](https://github.com/brreg/linkml-datamodellering-no/blob/main/COMMANDS.md) for alle tilgjengelege kommandoar.
```

### 2. `mkdocs/publish.sh` — fjern sed-workaround i Steg 3

Sidan lenkja no fungerer på portalen, treng linja ikkje lenger fjernast.
Erstatt sed-filtreringa med ein enkel kopi:

**Før:**
```bash
sed \
  -e '/Sjå.*CLAUDE\.md.*COMMANDS\.md/d' \
  "$REPO_ROOT/README.md" > "$DOCS/index.md"
```

**Etter:**
```bash
cp "$REPO_ROOT/README.md" "$DOCS/index.md"
```

### 3. `mkdocs/docs/modellmanifest-generering.md:233`

Endre `[COMMANDS.md](../../COMMANDS.md)` til absolutt GitHub-URL. Dei to
`specs/done/*.md`-lenkene i same seksjon er **ikkje** ein del av denne
rettinga (brukar valde å avgrense scope).

## Handlingsliste

- [x] Rett README.md:141 til absolutte URL-ar
- [x] Fjern sed-workaround i `publish.sh` Steg 3
- [x] Rett COMMANDS.md-lenka i `modellmanifest-generering.md`
- [x] Regenerer README.md og verifiser at ingenting anna vart påverka

## Utført

- `README.md`: linje 141 — `CLAUDE.md`/`COMMANDS.md`-lenker endra til absolutt GitHub-URL
- `mkdocs/publish.sh`: fjerna sed-filtrering i Steg 3 (linja treng ikkje lenger fjernast frå portalen), erstatta med `cp`
- `mkdocs/docs/modellmanifest-generering.md`: COMMANDS.md-lenka endra til absolutt GitHub-URL — dei to `specs/done/*.md`-lenkene i same seksjon er urørte (same rotårsak, men utanfor valt scope)
