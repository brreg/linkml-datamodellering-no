# Dokumenter WSL2 mirrored-modus-fiks for `make docs-serve` og legg til prereq-sjekk

## Bakgrunn

Under feilsøking av `make docs-serve` (sjå samtalehistorikk) vart det stadfesta at
`http://localhost:8000/...`/`http://127.0.0.1:8000/...` kan feile i ein nettlesar
på Windows-verten sjølv om `docs-serve`-containeren køyrer heilt fint — dette
skjer i WSL2 + rootless podman (`pasta`-nettverksbakend) pga. eit
samspelsproblem mellom podman sin IPv4-only pasta-lyttar og WSL2 sin
NAT-baserte `localhostForwarding` (asymmetrisk IPv4/IPv6-handtering).
Windows-brannmuren vart utelukka som årsak (loopback-trafikk vert aldri
filtrert av Windows Firewall). Verifisert fiks: aktiver WSL2 sin **mirrored**
nettverksmodus (`networkingMode=mirrored` i `.wslconfig`), som løyste
problemet fullstendig for brukaren i denne økta.

**Mål:** Dokumenter denne kjende fallgruva og fiksen i `COMMANDS.md` (der
`make docs-serve` er dokumentert), og legg til ein automatisk sjekk i
`src/assets/scripts/makefile/check-prereqs.bash` som varslar brukaren om
mirrored-modus ikkje er aktiv i eit WSL2-miljø, med veiledning om korleis
aktivere det.

**Avgrensing:** Ingen ny fil i `bugs/` — konvensjonen for `bugs/`-filer i
CLAUDE.md er knytt til skip-betingelsar i `tests/test_make.sh`, som ikkje er
relevant her. Dokumentasjonen held seg til `COMMANDS.md` + `check-prereqs.bash`,
slik brukaren spesifikt bad om.

## Steg

### 1. Legg til forklarande avsnitt i COMMANDS.md
Under "Dokumentasjonsportal"-seksjonen (etter `docs-serve`-tabellen og det
eksisterande avsnittet om `make docs-publish`), legg til eit nytt avsnitt som:
- Forklarer symptomet (`localhost`/`127.0.0.1:8000` fungerer ikkje i
  nettlesaren på Windows-verten, sjølv om containeren køyrer og svarar OK
  internt i WSL2)
- Forklarer rotårsaka kort (pasta lyttar berre IPv4, WSL2 sin NAT-baserte
  `localhostForwarding` handterer IPv4/IPv6 asymmetrisk)
- Presiserer at Windows-brannmuren **ikkje** er årsaka (loopback er unnateke
  brannmurfiltrering)
- Gir fiksen: legg til `networkingMode=mirrored` under `[wsl2]` i
  `C:\Users\<brukar>\.wslconfig`, køyr `wsl --shutdown` frå Windows
  PowerShell, start WSL2 og containeren på nytt
- Nemner at `make check-prereqs` no varslar om dette (jf. steg 2)

### 2. Legg til mirrored-modus-sjekk i check-prereqs.bash
Legg til eit nytt sjekk-blokk rett etter den eksisterande WSL2-deteksjonen
(linje ~63-68):
- Berre relevant når WSL2 er oppdaga (same `grep -qi microsoft /proc/version`-
  gate som den eksisterande sjekken)
- Bruk `wslinfo --networking-mode` (tilgjengeleg i nyare WSL2-versjonar) for
  å avgjere aktiv modus
- `mirrored` → `ok`
- Anna verdi (typisk `nat`) → `warn` med kort forklaring + peikar til
  `COMMANDS.md`
- `wslinfo` ikkje funne (eldre WSL2-versjon) → `warn` om at modus ikkje kan
  avgjerast automatisk, med peikar til `COMMANDS.md`
- **Ikkje** `fail` — dette blokkerer ikkje resten av verktøykjeda, berre
  nettlesar-tilgang til `make docs-serve`/`docs-build` sin lokale server

### 3. Verifiser
- Køyr `bash src/assets/scripts/makefile/check-prereqs.bash` og stadfest at
  det nye sjekk-punktet viser `ok` (miljøet har alt mirrored-modus aktivert
  frå tidlegare i denne økta)
- Les gjennom det nye avsnittet i `COMMANDS.md` for å stadfeste at det følgjer
  eksisterande stil og språk (nynorsk, kompakt)

## Prioritert handlingsliste

1. Legg til forklarande avsnitt i `COMMANDS.md` (Dokumentasjonsportal-seksjonen)
2. Legg til mirrored-modus-sjekk i `check-prereqs.bash`
3. Verifiser begge endringane

## Avhengigheiter

- Ingen avhengigheiter til andre specs.

## Utført

Alle 3 steg gjennomførte:

1. **COMMANDS.md**: nytt avsnitt lagt til rett etter `make docs-publish`-
   forklaringa i "Dokumentasjonsportal"-seksjonen — symptom, rotårsak,
   avkrefting av brannmur-teorien, og steg-for-steg-fiks (`.wslconfig` →
   `wsl --shutdown` → omstart).
2. **check-prereqs.bash**: nytt sjekk-blokk rett etter den eksisterande
   WSL2-deteksjonen. Bruker `wslinfo --networking-mode` når tilgjengeleg
   (`ok` for `mirrored`, `warn` elles med fiks-instruksjon); `warn` utan
   blokkering når `wslinfo` manglar (eldre WSL2). Ingen `fail` — påverkar
   berre nettlesar-tilgang til `docs-serve`/`docs-build`, ikkje resten av
   verktøykjeda.
3. **Verifisert**: `bash -n check-prereqs.bash` (syntaks OK) og full køyring
   — nytt punkt viser `✓ WSL2 nettverksmodus er 'mirrored'` sidan miljøet alt
   hadde mirrored-modus aktivert frå tidlegare i same økt (9 OK, 0 åtvaringar,
   0 feil).

**Avvik frå opphavleg plan:** Ingen.
