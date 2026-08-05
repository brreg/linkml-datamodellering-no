# Fjern avhengigheita til `git`-binæren i manifestgenerering

## Bakgrunn

Under `make domain-ap-no` (og tilsvarande `make domain-<domene>`-mål for alle domene) dukkar denne åtvaringa opp for kvart skjema, t.d.:

```
⚠️  Kunne ikkje hente git remote-URL ([Errno 2] No such file or directory: 'git') — brukar fallback-URL
```

**Årsak:** `get_github_raw_base_url()` i `src/assets/scripts/makefile/generate-informasjonsmodell.py` (linje 188-223) kallar `subprocess.run(['git', 'remote', 'get-url', 'origin'], ...)` for å utleie GitHub raw-URL-basen dynamisk. Scriptet køyrer via `gen-informasjonsmodell-instance`-målet (`make/30-instances.mk:26`) inne i `$(PYTHON_RUN)`-containeren (`make/01-containers.mk:29`), som byggjer på `python:3.13-alpine` (`src/assets/containers/Dockerfile.python`) — eit minimalt testimage utan `git` installert. Kallet feilar difor alltid med `FileNotFoundError`.

**Er dette alvorleg i dag?** Nei. Feilen fangast av eit `except Exception`, loggast synleg til stderr (i tråd med "Ingen stille feil"-regelen i CLAUDE.md) og scriptet fell tilbake til ein hardkoda URL: `https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/main/`. Denne verdien er *tilfeldigvis* korrekt for dette repoet (stadfesta mot `.git/config`: `url = git@github.com:brreg/linkml-datamodellering-no.git`), så genererte manifest (`metadata/<skjema>-manifest.yaml`) får riktig URL i praksis.

**Kvifor likevel fikse det?**
- Åtvaringa dukkar opp for **kvart** skjema i **kvart** `make domain-*`-kall (9 domene × fleire skjema) — rein logg-støy som gjer det vanskelegare å oppdage *reelle* feil i byggeloggen.
- Korrektheita kviler i dag på at fallback-verdien tilfeldigvis er rett, ikkje på at koden faktisk reknar ut riktig verdi. Dersom repoet ein gong vert flytta/omdøypt (org- eller repo-namn), vil manifesta stille (men synleg-logga) peike feil, sidan fallback-strengen er hardkoda.

## Metode

Grep etter `git`-subprocess-kall i `src/assets/scripts/` og `mkdocs/lib/scripts/` fann to treff:

| Fil | Bruk | Køyrekontekst | Råka av same feil? |
|---|---|---|---|
| `src/assets/scripts/makefile/generate-informasjonsmodell.py` | `git remote get-url origin` — utleier raw-URL-base | `$(PYTHON_RUN)`-container (`python:3.13-alpine`, ingen git) | **Ja** — denne specen |
| `src/assets/scripts/utils/release_helpers.py` | `git show HEAD~1:.release-please-manifest.json` — les fil frå førre commit | Køyrer direkte i `.github/workflows/release-please.yml`-steget, på GitHub-runneren (ikkje via `PYTHON_RUN`) | Nei — GitHub-runnarar har `git` installert, og bruken (les fil frå commit-historikk) kan ikkje erstattast med enkel fil-parsing. Utanfor scope. |

Berre `generate-informasjonsmodell.py` er råka, og berre denne treng endring.

## Steg

1. **Bytt datakjelde frå `git remote get-url` til direkte lesing av `.git/config`.** Repoet er alltid fullt tilgjengeleg i containeren (`WORK_MOUNT` mountar heile `$(CURDIR)`, inkludert `.git/`), så `.git/config` finst utan at `git`-binæren treng vere installert. `.git/config` er eit standard INI-format og kan lesast med `configparser` frå standardbiblioteket (ingen ny avhengigheit):

   ```python
   import configparser

   def get_github_raw_base_url() -> str:
       config = configparser.ConfigParser()
       git_config_path = Path.cwd() / ".git" / "config"

       try:
           if not git_config_path.exists():
               raise FileNotFoundError(f"{git_config_path} finst ikkje")
           config.read(git_config_path)
           remote_url = config.get('remote "origin"', 'url')

           if remote_url.startswith('git@github.com:'):
               parts = remote_url.split(':')[1].replace('.git', '').split('/')
           elif remote_url.startswith('https://github.com/'):
               parts = remote_url.replace('https://github.com/', '').replace('.git', '').split('/')
           else:
               raise ValueError(f"Ukjent remote-URL-format: {remote_url}")

           owner, repo = parts[0], parts[1]
           return f"https://raw.githubusercontent.com/{owner}/{repo}/main/"
       except Exception as e:
           print(f"⚠️  Kunne ikkje lese git remote-URL frå {git_config_path} ({e}) — brukar fallback-URL", file=sys.stderr)

       return "https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/main/"
   ```

   URL-parsing-logikken for `git@`- og `https://`-format vert gjenbrukt uendra frå eksisterande kode — berre kjelda til `remote_url` (subprocess-output → configparser-verdi) og feiltypen som fangast (`subprocess.CalledProcessError`/`FileNotFoundError` → generell parse-feil) endrar seg.

2. **Behald mjuk fallback + synleg stderr-åtvaring.** `except Exception` → `print(..., file=sys.stderr)` → hardkoda fallback-verdi skal framleis vere der, i tråd med CLAUDE.md sitt krav om at mjuke fallback-val skal loggast. Dette dekkjer framleis reelle edge-case (t.d. skallow clone utan `.git/config`, eller ein `origin`-remote med anna namn).

3. **Ingen Dockerfile-endring.** Løysinga krev ikkje at `git` vert installert i `Dockerfile.python` — det held frå at biblioteket `configparser` alt er ein del av Python sitt standardbibliotek. Dette er i tråd med prinsippet om minimale containerimage (unngår å leggje til ein binær-avhengigheit i eit image som elles berre inneheld pytest).

4. **Test:** køyr `make domain-ap-no` (eller eit anna domene) og stadfest at:
   - Åtvaringa `Kunne ikkje hente git remote-URL (...)` **ikkje** lenger dukkar opp i normal køyring
   - `metadata/<skjema>-manifest.yaml` for eit vilkårleg skjema (t.d. `xkos-ap-no`) framleis inneheld korrekte `https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/main/...`-URL-ar (uendra verdi, no utleia dynamisk i staden for hardkoda)
   - Fallback-stien framleis fungerer: mellombels flytt/rename `.git/config` (eller køyr scriptet frå ein katalog utan `.git/`) og stadfest at åtvaringa då **framleis** vert vist, med oppdatert feilmelding

## Handlingsliste

- [x] Erstatt `subprocess.run(['git', 'remote', ...])` i `get_github_raw_base_url()` med `configparser`-basert lesing av `.git/config`
- [x] Behald try/except-fallback med synleg stderr-åtvaring (oppdater meldingsteksten til å referere fil-lesing, ikkje subprocess)
- [x] Køyr `make domain-ap-no` og stadfest at åtvaringa er borte og manifest-URL-ar er uendra
- [x] Stadfest fallback-stien framleis fungerer ved manglande `.git/config`

## Utført

`get_github_raw_base_url()` i `src/assets/scripts/makefile/generate-informasjonsmodell.py` les no `.git/config` direkte via `configparser` (stdlib) i staden for å shelle ut til `git remote get-url origin`. URL-parsing-logikken for `git@`- og `https://`-format er uendra, berre kjelda til `remote_url` og feiltypen som fangast er bytta ut.

Verifisert:
- `make domain-ap-no` (168s, exit 0) — ingen git-relaterte åtvaringar i loggen
- `metadata/xkos-ap-no-manifest.yaml` har framleis korrekte `https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/main/...`-URL-ar, no utleia dynamisk
- Normalsti testa isolert (repo-katalog): ingen åtvaring, korrekt URL
- Fallback-sti testa isolert (katalog utan `.git/`): åtvaring vises korrekt med oppdatert feilmelding, fallback-URL er identisk med den dynamisk utleia verdien

Ingen Dockerfile-endring var nødvendig.
