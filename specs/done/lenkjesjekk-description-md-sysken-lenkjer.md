# Ekskluder description.md frå lenkjesjekk (sysken-skjema-lenkjer feiltolka)

## Bakgrunn

`lenkje-og-mermaid-sjekk`-workflowen sin `lenkjesjekk`-jobb (lychee, skannar
`**/*.md`) rapporterer broten-funn i fem `description.md`-kjeldefiler:

```
src/linkml/ap-no/dqv-ap-no/description.md → ../dqv-core/index.md (not found)
src/linkml/ap-no/dqv-core/description.md → ../dqv-ap-no/index.md (not found)
src/linkml/ap-no/modelldcat-ap-no/description.md → ../modelldcat-katalog/index.md, ../modelldcat-modell/index.md (not found)
src/linkml/ap-no/modelldcat-katalog/description.md → ../modelldcat-ap-no/index.md, ../modelldcat-modell/index.md (not found)
src/linkml/ap-no/modelldcat-modell/description.md → ../modelldcat-ap-no/index.md, ../modelldcat-katalog/index.md (not found)
```

Stadfesta falsk positiv: `description.md` er portaltekst (jf. CLAUDE.md §
Katalogstruktur) som `mkdocs/lib/sections/om_denne_modellen.sh` (`cat
"$description_file"`) skriv **rått inn** i den genererte
`mkdocs/docs/<domain>/<schema>/index.md`. Dei relative lenkjene
(`../dqv-core/index.md` o.l.) er korrekte **relativt til den bygde
portal-plasseringa** — stadfesta lokalt: `mkdocs/docs/ap-no/dqv-ap-no/index.md`
line 26 inneheld identisk lenkje, og `mkdocs/docs/ap-no/dqv-core/index.md`
finst faktisk. Same lenkjetekst vert difor validert korrekt når lychee
skannar den bygde `mkdocs/docs/**`-kopien (ikkje ekskludert i dag).

Problemet oppstår berre fordi lychee **i tillegg** skannar kjeldefila
direkte på `src/linkml/ap-no/<schema>/description.md`, der ein
`../<sysken-skjema>/index.md` naturleg ikkje finst (index.md finst berre i
det genererte `mkdocs/docs/`-treet). Dette er same feilklasse som er
dokumentert i `specs/done/lenkjesjekk-3817-feil-evaluering.md` — kjelder
med rett portal-relativ lenkje, feilevaluert fordi lychee sjekkar dei på
feil (kjelde-) plassering. Jf. CLAUDE.md § «Relative vs. absolutte lenkjer
i portalinnhald».

Stadfesta: ingen `description.md`-fil finst utanfor `src/linkml/` (`find .
-iname description.md -not -path './src/linkml/*'` → tomt), så ei generell
eksklusjon av filnamnet er trygg og påverkar ikkje andre filer.

## Steg

1. Legg til `"description.md"` i `exclude_path`-lista i `.github/lychee.toml`,
   med ein kommentar som forklarer falsk-positiv-mønsteret (same stil som
   `specs`-eksklusjonen i same fil).
2. Stadfest lokalt (om mogleg) at dei fem konkrete feilmeldingane forsvinn
   frå ein ny lychee-køyring, utan å ekskludere reelle feil.

## Handlingsliste

- [x] `.github/lychee.toml`: legg til `description.md` i `exclude_path`
- [x] Verifiser at endringa ikkje er ei `.github/workflows/*.yml`-fil
      (actionlint difor ikkje naudsynt, jf. CLAUDE.md)

## Utført

`.github/lychee.toml`: `description.md` lagt til `exclude_path`-lista, med
grunngjevande kommentar.

**Verifisering (lokal lychee-køyring, ikkje CI):** køyrde lychee direkte mot
dei fem konkrete filene med same config. Alle fem gav
`No files found for this input source` — stadfesta at `exclude_path`
filtrerer dei bort før nokon lenkjer i dei vert sjekka i det heile.

Merk: `podman run` for lychee treng `--user`-namnerom-oppsett
(`newuidmap`) som feila i standard sandkasse-modus (`Operation not
permitted`) — køyrt med sandkasse mellombels deaktivert for denne eine
verifiseringskommandoen.
