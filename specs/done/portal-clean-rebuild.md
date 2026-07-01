# Plan: Alltid rein gjenoppbygging av GitHub Pages-portal

## Bakgrunn

`publish.sh` regenererer `mkdocs/docs/$domain/$schema/` frå `generated/`-artefaktar.
Men to strukturelle problem gjer at utdaterte sider overlever i portalen:

1. **Generert innhald er committa til git.**  
   Heile `mkdocs/docs/ap-no/`, `mkdocs/docs/oreg/` osb. ligg i git-historia.
   Når eit skjema vert sletta eller omdøypt, ligg dei gamle sidene att i git og
   vert distribuerte til GitHub Pages fordi CI plukkar dei opp frå `source`-artefaktet.

2. **`publish.sh` steg 1 ryddar berre aktive domene.**  
   Steg 1 itererer over `generated/*/` og slettar tilsvarande `mkdocs/docs/$domain/`
   — men berre for domene som *finst* i `generated/`. Eit fjerna eller omdøypt domene
   vert aldri rydda frå `mkdocs/docs/`.

3. **`mkdocs-build`-cache kan servere utdatert bygg.**  
   Cache-nøkkelen inkluderer `mkdocs/docs/**` frå git — ved cache-treff hoppar CI
   over heile bygget med potensielt gammalt innhald.

Konsekvensen: sider som `oreg/enhetsregisteret-bvrinn` (gamalt namn) eller
domene som er fjerna frå kjelda, kan bli ståande i portalen i lang tid.

## Mål

GitHub Pages-portalen speglar alltid og berre noverande kjeldeskjema.
Ingen manuelle cache-bump (`v2-`, `v3-`) skal vere nødvendige for å rydde
opp gamle sider.

## Rotårsaker og løysing

| Rotårsak | Løysing |
|---|---|
| Generert innhald committa til git | Gitignore domene-katalogar og `mkdocs.yml`; fjern frå git-tracking |
| `publish.sh` ryddar ikkje forsvunne domene | Legg til steg i `publish.sh` som slettar stale `mkdocs/docs/$domain/`-katalogar |
| `mkdocs-build`-cache basert på git-innhald | Fjern eller avgrensar mkdocs-build-cachen |

---

## Steg

### Steg 1 ✓ — Gitignore generert portaltinnhald

Legg til i `.gitignore`:

```
# Genererte portalsider — alltid regenerert av publish.sh / CI
mkdocs/docs/ap-no/
mkdocs/docs/begrepskatalog/
mkdocs/docs/fair/
mkdocs/docs/fint/
mkdocs/docs/modellkatalog/
mkdocs/docs/ngr/
mkdocs/docs/oreg/
mkdocs/docs/samt/
mkdocs/docs/index.md
mkdocs/mkdocs.yml
```

Behold i git (ikkje gitignore):
- `mkdocs/docs/stylesheets/` — statisk CSS
- `mkdocs/docs/javascripts/` — statisk JS
- `mkdocs/docs/ny-domenemodell.md`, `ny-begrepsmodell.md`, `ny-org.md` — rettleiingssider
- `mkdocs/docs/ekstern-bruk.md`, `manifest-config.md`, `valideringregler.md`
- `mkdocs/docs/publisering-begrep.md`, `publisering-modell.md`

**Kvifor `mkdocs.yml` òg?**  
`publish.sh` steg 4 regenererer `mkdocs.yml` frå scratch ved kvar køyring.
Å committe den skaper falsk tryggleik (den lokale versjonen er alltid utdatert)
og legg støy til git-historikken.

---

### Steg 2 ✓ — Avregistrere committa innhald frå git (`git rm --cached`)

```bash
git rm -r --cached \
  mkdocs/docs/ap-no/ \
  mkdocs/docs/begrepskatalog/ \
  mkdocs/docs/fair/ \
  mkdocs/docs/fint/ \
  mkdocs/docs/modellkatalog/ \
  mkdocs/docs/ngr/ \
  mkdocs/docs/oreg/ \
  mkdocs/docs/samt/ \
  mkdocs/docs/index.md \
  mkdocs/mkdocs.yml
```

Filene vert verande lokalt (nødvendige for `make docs-build`), men er ikkje
lenger ein del av git-historia.

---

### Steg 3 ✓ — Oppdater `publish.sh` steg 1 til å rydde forsvunne domene

Noverande steg 1 ryddar berre domene som *finst* i `generated/`. Legg til:

```bash
# Slett mkdocs/docs/$domain/ for domene som ikkje lenger finst i generated/
for docs_domain_dir in "$DOCS"/*/; do
    [ -d "$docs_domain_dir" ] || continue
    domain=$(basename "$docs_domain_dir")
    # Hopp over statiske katalogar
    case "$domain" in
        stylesheets|javascripts) continue ;;
    esac
    if [ ! -d "$GEN/$domain" ]; then
        echo "Ryddar forsvunne domene: $domain"
        rm -rf "$docs_domain_dir"
    fi
done
```

Dette sikrar at eit omdøypt eller fjerna domene vert rydda frå `mkdocs/docs/`
sjølv om det ikkje lenger finst i `generated/`.

---

### Steg 4 ✓ — Juster nøkkelen for `mkdocs-build`-cache i CI

Noverande cache-nøkkel inkluderer `mkdocs/docs/**`:

```yaml
key: mkdocs-build-${{ hashFiles('src/linkml/**', ..., 'mkdocs/docs/**', ...) }}
```

Etter steg 1-2 er `mkdocs/docs/$domain/` ikkje lenger i git, så
`hashFiles('mkdocs/docs/**')` vil berre hashe statiske filer (stylesheets,
javascripts, rettleiingssider). Nøkkelen bør oppdaterast til berre å inkludere
det som faktisk styrer portalen sin utsjånad og innhald:

```yaml
- name: Cache mkdocs-build-cache
  uses: actions/cache@v5
  with:
    path: mkdocs/.cache/
    key: mkdocs-build-${{ hashFiles('src/linkml/**', 'src/assets/containers/Dockerfile.linkml', 'src/assets/templates/**', 'mkdocs/docs/stylesheets/**', 'mkdocs/docs/javascripts/**', 'mkdocs/overrides/**') }}
    restore-keys: mkdocs-build-
```

`mkdocs/docs/**` (med alt generert innhald) er ute av nøkkelen. Cache-treff
tyder no faktisk at kjelda, templatat og statiske filer er uendra — ikkje at
gamalt generert innhald er cachet.

---

### Steg 5 ✓ — Commit og verifiser

1. Commit `.gitignore`-endringar og `git rm --cached`-resultata
2. Commit oppdatert `publish.sh`
3. Commit oppdatert `generate.yml` (fjerna/endra mkdocs-build-cache)
4. Push og sjekk at neste CI-køyring:
   - Genererer portalen frå scratch (ingen stale domene i `source`-artefaktet)
   - Deplayer korrekt nav med berre eksisterande skjema

---

## Prioritert handlingsliste

| # | Tiltak | Fil | Avhengigheit |
|---|---|---|---|
| 1 | Legg til gitignore-reglar for generert innhald | `.gitignore` | — |
| 2 | `git rm --cached` for committa generert innhald | (git-operasjon) | Steg 1 |
| 3 | Oppdater `publish.sh` steg 1 med stale-rydding | `mkdocs/publish.sh` | — |
| 4 | Fjern/avgrens `mkdocs-build`-cache i CI | `.github/workflows/generate.yml` | — |
| 5 | Commit + verifiser CI-køyring | — | Steg 1-4 |

---

## Avhengigheiter

- Steg 2 krev at `.gitignore` (steg 1) er på plass fyrst — elles vil git
  umiddelbart registrere filene att som untracked
- Steg 3 og 4 er uavhengige av kvarandre og kan utførast i same commit som steg 1-2
- Etter steg 2 vil lokalt `mkdocs/docs/` mangle generert innhald inntil
  `make publish` vert køyrd — dette er tilsikta

## Utført

Alle steg er utførte 2026-06-14:

- **Steg 1**: La til gitignore-reglar for `mkdocs/docs/ap-no/`, `begrepskatalog/`,
  `fair/`, `fint/`, `modellkatalog/`, `ngr/`, `oreg/`, `samt/`, `index.md` og
  `mkdocs/mkdocs.yml` i `.gitignore`.
- **Steg 2**: Køyrde `git rm -r --cached` på 3111 filer (alle committa genererte
  portalsider og `mkdocs.yml`). Filene ligg att lokalt og vert aldri meir committa.
- **Steg 3**: La til stale-ryddeløkke i `publish.sh` steg 1: itererer over
  `mkdocs/docs/*/` og slettar katalogar som ikkje lenger finst i `generated/`
  (unntatt `stylesheets/` og `javascripts/`).
- **Steg 4**: Justerte cache-nøkkel i `generate.yml` — fjerna `mkdocs/docs/**`
  og `mkdocs/mkdocs.yml` frå nøkkelen; behalde `stylesheets/**`, `javascripts/**`,
  `overrides/**`, `src/linkml/**` og `src/assets/templates/**`.
- **Steg 5**: Commit-melding generert nedst i svaret. Verifisering skjer ved
  neste CI-køyring.
