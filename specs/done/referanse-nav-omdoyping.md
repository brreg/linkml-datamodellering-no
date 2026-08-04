# Omdøyp NAV-menypunkt REFERANSE og uppercase Domener-tabellen

## Bakgrunn

NAV-menypunktet for `referanse`-domenet i mkdocs-portalen viser i dag "REFERANSE"
(store bokstavar av mappenamnet). Ønskt namn: "REF - Referansemodeller".

**Rotårsak:** `domain_label()` i `mkdocs/lib/utils/formatters.sh` har eksplisitte
case for dei fleste domena (`ap-no`, `ngr`, `fint`, `samt`, `fair`, `oreg`,
`begrepskatalog`, `modellkatalog`), men **ikkje** for `referanse`. Domenet fell
difor til default-casen som berre gjer mappenamnet til store bokstavar.

I tillegg skal Domener-tabellen i README.md (manuelt vedlikehalden, ikkje
auto-generert — jf. `generate-schema-table`-markøren lenger ned i fila) endrast:
lenkjeteksten i "Domene"-kolonna skal vere `REF` for referanse-rada, og
uppercase mappenamn (`FAIR`, `AP-NO`, `NGR`, `OREG`, `FINT`, `SAMT`,
`BEGREPSKATALOG`, `MODELLKATALOG`) for alle andre rader. Lenkje-URL-ane
(mappenamn i småbokstavar) skal ikkje endrast.

## Steg

### 1. Legg til case for `referanse` i `domain_label()`

`mkdocs/lib/utils/formatters.sh`:

```bash
referanse) echo "REF - Referansemodeller" ;;
```

Plassert saman med dei andre eksplisitte casane, før default-casen.

### 2. Uppercase lenkjetekst i Domener-tabellen i README.md

Endre "Domene"-kolonna (linje ~172-180) frå småbokstavar-lenkjetekst til
store bokstavar, med `REF` som spesialtilfelle for referanse:

| Før | Etter |
|---|---|
| `[referanse](referanse/)` | `[REF](referanse/)` |
| `[fair](fair/)` | `[FAIR](fair/)` |
| `[ap-no](ap-no/)` | `[AP-NO](ap-no/)` |
| `[ngr](ngr/)` | `[NGR](ngr/)` |
| `[oreg](oreg/)` | `[OREG](oreg/)` |
| `[fint](fint/)` | `[FINT](fint/)` |
| `[samt](samt/)` | `[SAMT](samt/)` |
| `[begrepskatalog](begrepskatalog/)` | `[BEGREPSKATALOG](begrepskatalog/)` |
| `[modellkatalog](modellkatalog/)` | `[MODELLKATALOG](modellkatalog/)` |

### 3. Merk at `mkdocs/mkdocs.yml` ikkje skal endrast manuelt

`mkdocs.yml` vert regenerert av `mkdocs/publish.sh` ved neste `make docs-publish`
og vil då plukke opp den nye labelen automatisk frå `domain_label()`. Manuell
endring i `mkdocs.yml` vert overskriven og skal difor ikkje gjerast som del av
denne oppgåva.

## Handlingsliste

- [x] Legg til `referanse`-case i `domain_label()` i `mkdocs/lib/utils/formatters.sh`
- [x] Uppercase alle lenkjetekstar i Domener-tabellen i README.md, `REF` for referanse

## Utført

- `mkdocs/lib/utils/formatters.sh`: la til `referanse) echo "REF - Referansemodeller" ;;` i `domain_label()`
- `README.md`: uppercase lenkjetekst i Domener-tabellen sin "Domene"-kolonne for alle rader (`REF`, `FAIR`, `AP-NO`, `NGR`, `OREG`, `FINT`, `SAMT`, `BEGREPSKATALOG`, `MODELLKATALOG`); lenkje-URL-ane er uendra
- NAV-menyen i `mkdocs/mkdocs.yml` vert oppdatert automatisk ved neste `make docs-publish` (ikkje endra manuelt, jf. steg 3 i spec)
