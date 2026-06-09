# Oppdater COMMANDS.md med make roundtrip

## Bakgrunn

`make roundtrip` vart lagt til i `Makefile` (sjå `specs/done/roundtrip-dokumentasjon-og-make-kommando.md`), men er ikkje dokumentert i `COMMANDS.md`. Ein ny brukar som les `COMMANDS.md` veit ikkje om kommandoen.

## Endring

Legg til to nye rader i tabellen under `## Validering` i `COMMANDS.md`, plassert mellom `make validate-instance` og `make test`:

```markdown
| `make roundtrip SCHEMA=<sti>` | Køyrer berre roundtrip-testane (JSON og TTL) for eitt skjema. Raskare enn full testsuite — nyttig etter skjema-endringar som kan påverke serialisering. | Testrapport for `roundtrip-json` og `roundtrip-ttl` til stdout; avsluttar med kode 1 ved feil |
| `make roundtrip` | Køyrer roundtrip-testar for alle skjema i repoet. | Testrapport til stdout; avsluttar med kode 1 ved feil |
```

## Tiltaksliste

| # | Tiltak | Fil |
|---|---|---|
| 1 | Legg til `make roundtrip`-radene i `## Validering`-tabellen | `COMMANDS.md` |

## Utført

To rader lagt til i `## Validering`-tabellen mellom `make validate-instance` og `make test`.
