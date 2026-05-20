# Evaluering: Tiltak 1 mot eksisterande portalsider

## Samanstilling

| | `index.md` (Heim) | `ny-domenemodell.md` | Tiltak 1 (forslag) |
|---|---|---|---|
| Føresetnader (Podman, WSL2, make) | Nemnt, ikkje rettleia | Ikkje nemnt | Steg 1 |
| Bygg images (`linkml-build-docker`) | **Manglar** | **Manglar** | Steg 2 |
| Scaffold nytt schema | Første kommando | Steg 1 (Scaffold) | Steg 3 |
| Rediger schema | Ikkje nemnt | Steg 2 (Rediger) | Steg 4 |
| Valider mot bronze | Éin kommando | Steg 3 (Valider) | Steg 5 |
| Generer artefaktar | Éin kommando | Steg 4 (Full testsuite) | Steg 6 |
| Sjå resultatet (`docs-serve`) | Éin kommando | Ikkje nemnt | Steg 7 |

---

## Problem

### 1 — Kritisk mangel: image-bygging er ikkje dokumentert

Verken `index.md` eller `ny-domenemodell.md` seier at images må byggast før ein kan gjere noko som helst. Ein ny brukar som følgjer `ny-domenemodell.md` vil feile på steg 1 (`make new-model`) fordi scriptet kallar podman-kommandoar som krev at imaget finst.

### 2 — Duplication viss Tiltak 1 implementerast naivt

`ny-domenemodell.md` har allereie ein sekvensiell arbeidsflyt (steg 1–4) som dekkjer steg 3–7 i Tiltak 1. Å legge det same narrativet i `index.md` gir to nesten-identiske sider.

### 3 — `index.md` gir feil inntrykk av inngangspunktet

`index.md` har løyste kommandoar utan klar rekkefølge. Noverande første kommando er `make new-model` — men det er ikkje det aller første ein gjer. Hjem-sida bør vere ei kortfatta orientering, ikkje ein parallell full arbeidsflyt.

---

## Tilråding

Tiltak 1 bør ikkje implementerast som ein kopi av `ny-domenemodell.md` inn i `index.md`. I staden:

### `index.md` (Heim) — kort orientering med eitt manglande steg

Behold "Kom i gang"-seksjonen, men:
1. Legg til image-bygging som **aller første steg** (dette manglar overalt)
2. Gjer kommandoane sekvensielle med nummerering
3. Legg til ei tydeleg lenke til `ny-domenemodell.md` for full rettleiing

```markdown
## Kom i gang

**Føresetnadar:** [Podman](https://podman.io/) (rootless), WSL2 og GNU make.

```bash
# 1. Bygg container-images (éin gong)
make linkml-build-docker && make python-build-docker && make mcp-val-build
```
```bash
# 2. Lag eit nytt schema
make new-model NAME=mitt-register DOMAIN=oreg
```
```bash
# 3. Valider mot minimumskrav
make mcp-validate SCHEMA=src/linkml/oreg/mitt-register/mitt-register-schema.yaml POLICY=bronze
```
```bash
# 4. Generer artefaktar og sjå resultatet
make oreg && make publish && make docs-serve
```

For full rettleiing om modellering, validering og importar: [Ny domenemodell](ny-domenemodell.md).
```

### `ny-domenemodell.md` — legg til manglande oppsett-steg

Legg til eit steg 0 før "Scaffold":

```markdown
### 0 — Bygg images (éin gong)

```bash
make linkml-build-docker && make python-build-docker && make mcp-val-build
```

Validatoren (`mcp-val-build`) byggast automatisk ved første `make mcp-validate`, men eksplisitt bygging her sikrar at alt er klart.
```

---

## Konklusjon

Tiltak 1 frå `developer-onboarding.md` er i hovudsak allereie implementert i `ny-domenemodell.md`. Det einaste som faktisk manglar overalt er **image-byggesteg**. Rett tiltak er:

1. Legg til image-bygging som steg 0 i `ny-domenemodell.md`
2. Gjer `index.md` sin "Kom i gang" sekvensiell med image-bygging som steg 1
3. Legg til lenke frå `index.md` til `ny-domenemodell.md`

Ikkje lag ein tredje full arbeidsflyt — bruk lenking mellom sidene.
