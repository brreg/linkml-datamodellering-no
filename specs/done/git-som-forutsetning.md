# Git som dokumentert føresetnad

## Bakgrunn

Repoet listar i dag Podman (rootless) og GNU make som føresetnader for lokalt
oppsett (README.md § «Kom i gang», COMMANDS.md, fleire mkdocs-sider), og
`make check-prereqs` (`src/assets/scripts/makefile/check-prereqs.bash`)
verifiserer at Podman og GNU make er installert. Git er implisitt naudsynt
(repoet er eit git-repo, `CONVENTIONS.md` og CLAUDE.md føreset commits,
`gource-preview`-targetet i `make/90-tools.mk` bruker git direkte), men er
verken nemnt som føresetnad i dokumentasjonen eller sjekka av
`check-prereqs.bash`.

Denne specen legg til Git som ei eksplisitt dokumentert føresetnad, og ein
tilsvarande sjekk i `make check-prereqs`, etter same mønster som den
eksisterande Podman/GNU make-sjekken.

**Avklart med brukar:** manglande Git skal gje **FAIL** (blokkerer, likt
Podman/GNU make) — ikkje berre WARN — sidan Git er naudsynt for å klone,
committe og jobbe med repoet i det heile.

## Steg

1. **`src/assets/scripts/makefile/check-prereqs.bash`** — legg til ein
   Git-sjekk (`command -v git`) rett før eller etter GNU make-sjekken, som
   `fail`-ar med installasjonshint dersom Git ikkje er tilgjengeleg, elles
   `ok`-ar med versjonsnummer (`git --version`). Følg eksisterande stil
   (`ok`/`warn`/`fail`-funksjonane, ingen andre endringar i scriptet).

2. **`README.md`** — utvid «Føresetnader»-lina (§ «Kom i gang», linje 57) til
   å inkludere Git, t.d.:
   `**Føresetnader:** linux eller windows med WSL2, [Git](https://git-scm.com/), [Podman](https://podman.io/) (rootless) og GNU make.`

3. **`COMMANDS.md`** og **`mkdocs/docs/kommandoar.md`** — oppdater
   tabellraden for `make check-prereqs` (linje 9 i begge filer) til å nemne
   Git saman med Podman, GNU make, user namespace og diskplass.

4. **`mkdocs/docs/kom-i-gang/index.md`** — utvid den parentetiske lista
   «(WSL2, Podman, GNU make)» (linje 24) til å inkludere Git.

5. **Ikkje rør:** `mkdocs/docs/index.md` er generert (kopiert) frå
   `README.md` av `mkdocs/publish.sh` steg 3 — ikkje rediger direkte. Andre
   sider som berre viser til `make check-prereqs` utan å liste verktøy
   eksplisitt (`ny-domenemodell.md`, `ny-begrepsmodell.md`, `ny-org.md`,
   `publisering-modell.md`, `publisering-begrep.md`) treng ingen endring —
   dei arvar den nye sjekken automatisk. `PRINCIPLES.md` § 5 («Ingen lokale
   avhengigheiter») handlar om verktøybruk i containerar, ikkje om
   føresetnader for å ha repoet i det heile — ikkje i scope her.

## Handlingsliste

- [x] Legg til Git-sjekk (FAIL ved manglande) i `check-prereqs.bash`
- [x] Oppdater `README.md` § «Føresetnader»
- [x] Oppdater `COMMANDS.md` og `mkdocs/docs/kommandoar.md` (check-prereqs-rad)
- [x] Oppdater `mkdocs/docs/kom-i-gang/index.md` (parentetisk verktøyliste)
- [x] Verifiser: køyr `make check-prereqs` lokalt og stadfest at Git vert rapportert OK

## Utført

Alle tiltak er gjennomførte og verifiserte — `bash src/assets/scripts/makefile/check-prereqs.bash`
rapporterer no `✓ Git tilgjengeleg (git version 2.43.0)` saman med dei andre sjekkane.
