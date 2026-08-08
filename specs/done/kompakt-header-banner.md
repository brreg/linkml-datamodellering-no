# Kompakt header-banner (éi linje i staden for tre)

## Bakgrunn

`print_header`-makroen i `make/03-output.mk` skriv i dag ei tre-linjers banner
rundt kvart make-target-namn:

```
************************************************************
*** make domain-ap-no  (PARALLEL=16)
************************************************************
```

Brukaren ønskjer dette komprimert til éi linje, med stjerner (20 stk) på
kvar side av teksten i staden for over/under-linjer:

```
******************** make domain-ap-no  (PARALLEL=16) ********************
```

Stjernene skal behalde gul farge (`CLR_SEP`). Sidan `print_header` er delt av
alle make-target ("make gen-*", "make domain-*", "make test", "make clean"
osv.), gjeld endringa automatisk alle desse — det finst ingen separat
banner-logikk berre for `gen-*`.

## Steg

1. Endre `SEP` i `make/00-settings.mk` frå 60 stjerner til 20 stjerner.
2. Endre `print_header` i `make/03-output.mk` til å skrive éi linje med
   `$(CLR_SEP)$(SEP)$(CLR_RST) $(CLR_HDR)make ...$(CLR_RST) $(CLR_SEP)$(SEP)$(CLR_RST)`
   i staden for tre `@echo`-linjer.
3. Test med eit par make-target (t.d. `make gen-shacl DOMAIN=ap-no`) for å
   verifisere visuelt resultat.

## Handlingsliste

- [x] Oppdater `SEP` til 20 stjerner
- [x] Komprimer `print_header` til éi linje
- [x] Verifiser output visuelt

## Utført

Verifisert med `make gen-shacl DOMAIN=ap-no` og `make domain-ap-no PARALLEL=16`
— begge skriv no éi linje med gule stjerner rundt kvit header-tekst.
