# Stale stiar etter strukturendring: `data/` og `examples/`

## Bakgrunn

`data/` og `examples/` ligg no **inne i skjemakatalogen**:

```
src/linkml/<domene>/<modell>/
├── <modell>-schema.yaml
├── manifest.yaml
├── published-uris.lock        ← berre for publiserte katalogar
├── description.md             ← valfri
├── examples/
│   └── <modell>-eksempel.yaml
└── data/                      ← berre for publiserte katalogar
    └── <datafil-katalog>/
        ├── <datafil-katalog>.yaml
        └── manifest.yaml
```

Fleire filer dokumenterer framleis den gamle strukturen der `data/` og `examples/` låg andre stader.

---

## Funn per fil

### 1. `README.md` og `mkdocs/docs/index.md`

**Status:** Krev retting — brukarvendt.

`mkdocs/docs/index.md` vert generert frå `README.md` av `publish.sh` (steg 3). Begge filer har same feil.

**Katalogstruktur-treeet** (README linje 183–184, index.md linje 147–148) viser:

```
└── data/          # Produksjonsdata (berre for publiserte katalogar)
```

Men den faktiske strukturen er:

```
└── data/                      ← berre for skjema med produksjonsdata
    └── <datafil-katalog>/
        ├── <datafil-katalog>.yaml
        └── manifest.yaml      ← datafil-manifest
```

Treet manglar dessutan `published-uris.lock` og `description.md` (valfri).

---

### 2. `mkdocs/docs/ny-domenemodell.md`

**Status:** Krev retting — brukarvendt.

Linje 12 seier:

```
- `examples/oreg/mitt-register-eksempel.yaml` — eksempelfil med minimal instans
```

Men `new-model.sh` legg fila på:

```
src/linkml/oreg/mitt-register/examples/mitt-register-eksempel.yaml
```

Rett linje:

```
- `src/linkml/oreg/mitt-register/examples/mitt-register-eksempel.yaml` — eksempelfil med minimal instans
```

---

### 3. `mkdocs/docs/ny-begrepsmodell.md`

**Status:** Krev retting — brukarvendt.

**Linje 33–35** (bash-blokk):

```bash
mkdir -p src/linkml/begrepskatalog/<katalognavn>
# examples/begrep/ finst allereie
```

Kommentaren er feil på to måtar:
- `examples/` er ikkje delt på tvers av katalogar — kvar katalog har sin eigen `examples/`-underkatalog
- Mappa heiter `src/linkml/begrepskatalog/<katalognavn>/examples/`, ikkje `examples/begrep/`

Rett:

```bash
mkdir -p src/linkml/begrepskatalog/<katalognavn>/examples
```

**Linje 171**:

```
(`examples/begrep/<katalognavn>-eksempel.yaml`) under dei tilsvarande listene.
```

Gamalt rotkatalogtilvisande mønster. Rett:

```
(`src/linkml/begrepskatalog/<katalognavn>/examples/<katalognavn>-eksempel.yaml`)
```

---

### 4. `mkdocs/docs/begrep/` og `mkdocs/docs/modell/`

**Status:** Automatisk retta ved neste `make publish` — ingen kjeldekodeendring nødvendig.

Desse katalogane inneheld genererte artefakter frå dei gamle domenenamna (`begrep`, `modell`). `publish.sh` steg 1 slettar alle tidlegare genererte domenekatalogar frå `docs/` ved kvar køyring. Dei forsvinn så snart `make <domene> && make publish` køyrer.

---

### 5. `specs/`-filer med rot-nivå `data/begrep/`-stiar

**Status:** Historiske designdokument — lav prioritet. Ikkje brukarvendte.

Desse filene dokumenterer tilstanden *før* `data/` vart flytt inn i skjemakatalogen. Dei treng ikkje rettast for å gjere kodebasen korrekt, men er misvisande som referanse.

| Fil | Gamalt mønster |
|---|---|
| `specs/dokumentasjon-publisering-begrep.md` | `data/begrep/brreg-begrep.yaml` |
| `specs/publisering-felles-begrepskatalog.md` | `data/begrep/brreg-begrep.yaml` |
| `specs/publiserings-flagg.md` | `src/linkml/begrep/brreg-begrep/data/brreg-begrep/` |
| `specs/readme-kom-i-gang.md` | `data/begrep/katalognavn.yaml` |
| `specs/oppdater-validator-readme.md` | `data/begrep/<katalog>.yaml` |
| `specs/mcp-server-namngjeving.md` | `data/begrep/<katalog>.yaml` |

---

## Prioritert tiltaksliste

| # | Fil | Endring | Prioritet |
|---|---|---|---|
| 1 | `README.md` | Utvid `data/`-innslaget i katalogtreet med nested struktur + `published-uris.lock` | Høg |
| 2 | `mkdocs/docs/ny-domenemodell.md` linje 12 |Rett `examples/oreg/...` → `src/linkml/oreg/.../examples/...` | Høg |
| 3 | `mkdocs/docs/ny-begrepsmodell.md` linje 34, 171 | Fjern `# examples/begrep/ finst allereie`-kommentar; rett linje 171 | Høg |
| 4 | `mkdocs/docs/index.md` | Generert frå README — rettast automatisk når README er oppdatert og `make publish` køyrer | Automatisk |
| 5 | `mkdocs/docs/begrep/` + `mkdocs/docs/modell/` | Slettas automatisk ved neste `make publish` | Automatisk |
| 6 | `specs/`-filer | Historisk kontekst — ikkje kritisk | Lav |
