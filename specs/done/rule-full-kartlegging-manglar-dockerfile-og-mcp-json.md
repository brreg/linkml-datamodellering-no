# Utvid rule: full kartlegging av monteringsstader for delte moduler manglar Dockerfile/flatten-and-validate.bash/.mcp.json

## Bakgrunn

Under `specs/backlog/evaluer-bootstrap-verktoy-separasjon.md` (Funn 2) vart det oppdaga at commit
`9f240e49` — som konsoliderte JSON-RPC-dispatch-koden til dei tre MCP-serverane til ein delt modul
`src/assets/scripts/utils/mcp_jsonrpc_stdio.py` — oppdaterte nokre, men ikkje alle, kontainarinvokeringar
som treng modulen. Feilen vart **verifisert reprodusert** i denne økta:

```bash
podman build --format docker -f src/assets/containers/Dockerfile.mcp-linkml --target validator -t mcp-linkml-validator .
echo '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{}}' | podman run -i --rm mcp-linkml-validator
```

```
Traceback (most recent call last):
  File "/app/server.py", line 19, in <module>
    from mcp_jsonrpc_stdio import dispatch, run_stdio_loop  # noqa: E402
ModuleNotFoundError: No module named 'mcp_jsonrpc_stdio'
```

Det bemerkelsesverdige: same commit la **alt** til ei rule om nøyaktig dette temaet —
`.claude/rules/container-images.md` § «Ein ny påkravd delt modul krev full kartlegging av alle
monteringsstader» — med ei 5-punkts sjekkliste. Men sjekklista sjølv er ikkje komplett: han listar
make-variablar, `-test`-oppskrifter, scaffolding-script, `tests/test_make.sh` og CI-cache-nøklar — men
**ikkje** (a) `Dockerfile*` sine `COPY`-lister (det faktisk bygde/publiserte biletet), (b)
frittståande orkestreringsskript som `flatten-and-validate.bash` (brukt av
`.github/workflows/reusable-validate.yml`, den eksterne bootstrap-valideringsvegen), eller (c)
`.mcp.json` (kontributørane sitt eige lokale Claude Code MCP-oppsett). Alle tre var faktisk råka av akkurat
denne bugen. Brukaren har bekrefta (via spørsmål i denne økta) at dei ønskjer rula utvida.

## Steg

1. Utvid sjekklista i `.claude/rules/container-images.md` § «Ein ny påkravd delt modul krev full
   kartlegging av alle monteringsstader» med dei tre manglande punkta.
2. Utvid `paths:`-scopet i same rule sin frontmatter slik at han faktisk lastar ved arbeid med
   `flatten-and-validate.bash` og `.mcp.json` (i dag dekt av verken `container-images.md` eller
   `mcp-server-python.md` for `.mcp.json`).
3. Logg avgjerder undervegs.

## Handlingsliste

- [x] Legg til punkt om `Dockerfile*` sine `COPY`-lister i sjekklista
- [x] Legg til punkt om frittståande orkestreringsskript (namngje `flatten-and-validate.bash` som
      konkret eksempel, generaliser mønsteret)
- [x] Legg til punkt om `.mcp.json`
- [x] Utvid `paths:` i frontmatter
- [x] Oppdater `description` i frontmatter om nødvendig

## Avgjerder

- **Utvida eksisterande rule i staden for å opprette ny fil.** Grunngjeving: emnet (full kartlegging av
  monteringsstader for delte moduler) er nøyaktig det same som den eksisterande seksjonen i
  `container-images.md` alt dekker — dette er ei utviding/retting av ei ufullstendig sjekkliste, ikkje eit
  nytt emne. Følgjer skillen sitt eige steg 3 («legg til som ny subseksjon i ein eksisterande rule dersom
  emnet naturleg høyrer saman»).
- **Fiksar ikkje sjølve bugen (Dockerfile/flatten-and-validate.bash/.mcp.json) i denne specen.** Grunngjeving:
  brukaren sitt eksplisitte spørsmål gjaldt berre om ei rule skulle leggjast til; sjølve bug-fiksen er alt
  fanga som handlingsliste-punkt 1 i `specs/backlog/evaluer-bootstrap-verktoy-separasjon.md` og bør handterast
  som eiga oppgåve/spec for å halde endringane til denne specen fokuserte og lett reviderbare.
- **Verifiserte hendinga med ein reell `podman build` + `podman run` i staden for berre statisk lesing.**
  Grunngjeving: skillen sitt steg 1 krev konkret grunngjeving — ei faktisk reproduksjon er sterkare
  dokumentasjon enn ei utleiing frå kodelesing åleine, og var billig å gjennomføre.

## Utført

`.claude/rules/container-images.md` er utvida:

- `paths:` i frontmatter fekk to nye oppføringar: `src/mcp-*/flatten-and-validate.bash` og `.mcp.json`,
  slik at rula lastar automatisk ved arbeid med desse filene (ho gjorde det ikkje frå før).
- Sjekklista i § «Ein ny påkravd delt modul krev full kartlegging av alle monteringsstader» fekk to nye
  punkt (6: `Dockerfile*` sine `COPY`-lister, 7: `.mcp.json`), og punkt 3 vart utvida til eksplisitt å nemne
  `flatten-and-validate.bash` som eksempel på eit frittståande orkestreringsskript.
- Eit nytt avsnitt siterer den konkrete, reproduserte hendinga (feil sjekkliste-versjon dekte ikkje sine
  eigne punkt 6/7, som var nøyaktig punkta som feila) som grunngjeving.

Verifisert ved reell reproduksjon i denne økta (ikkje berre kodelesing): `podman build --format docker -f
src/assets/containers/Dockerfile.mcp-linkml --target validator -t mcp-linkml-validator .` etterfølgt av
`echo '...' | podman run -i --rm mcp-linkml-validator` gav
`ModuleNotFoundError: No module named 'mcp_jsonrpc_stdio'`, som stadfestar at biletet manglar modulen og at
`flatten-and-validate.bash` (som ikkje monterer `utils/`) ville feila likt via
`.github/workflows/reusable-validate.yml`.

Sjølve bug-fiksen (leggje `COPY`/`-v`-linjer til dei tre stadene) er **ikkje** gjort her — det er dekt av
handlingsliste-punkt 1 i `specs/backlog/evaluer-bootstrap-verktoy-separasjon.md`, som held fram som eiga
vurdering/handlingsliste i backlog.
