# Fiks svart bakgrunn i mermaid-diagram (arkitektur-oversikt.md)

## Bakgrunn

Dei to mermaid-diagramma i `mkdocs/docs/arkitektur/arkitektur-oversikt.md`
(Del 1 og Del 2) brukar hardkoda `#000000`-bakgrunn med kvit tekst for både
`classDef default` og alle `style <subgraph>`-linjer. Dette gjer diagramma
vanskelege å lese mot resten av sideinnhaldet, og skil seg frå fargestilen i
dei andre handskrivne mermaid-diagramma i dokumentasjonsportalen
(`automasjon/monitorering.md`, `publisering/publisering-oversikt.md`), som
brukar lyse pastellfargar med mørk tekst.

Brukaren har valt å bytte til lyse pastellfargar, i tråd med resten av sida,
og behalde den semantiske fargekodinga (raud=ekstern, blå=CI, grøn=MCP,
lilla=konsument).

## Steg

1. I Del 1 (`flowchart TB`, line ~113-126): erstatt `classDef default`,
   `classDef ekstern`, `classDef ci`, `classDef mcp` sine svarte
   `fill`/`color`-verdiar med lyse pastellfargar + mørk tekst. Erstatt
   `style KILDE/MCP/CI/PUBLISERT fill:#000000...` med ein lys, nøytral
   subgraph-bakgrunn.
2. I Del 2 (`flowchart BT`, line ~186-198): same type endring for
   `classDef default`, `classDef ekstern`, `classDef ci`, `classDef konsument`,
   og `style KATALOGAR/EKSTERNREPO/KONSUMENTER`.
3. Gjenbruk fargeverdiar som alt finst i `monitorering.md` /
   `publisering-oversikt.md` der det passar (t.d. blå `#e3f2fd`/`#2196f3`,
   grøn `#e1f5e1`/`#4caf50`) for konsistens på tvers av sida.
4. Verifiser visuelt (les gjennom den endra mermaid-koden) at kontrasten
   mellom node-fill, subgraph-fill og tekst er god i lys modus.

## Handlingsliste

- [x] Oppdater fargane i Del 1
- [x] Oppdater fargane i Del 2
- [x] Flytt spec til `specs/done/`

## Utført

Erstatta svart `#000000`-bakgrunn/kvit tekst med lyse pastellfargar
(gjenbrukte blå `#e3f2fd`/`#2196f3` og grøn `#e1f5e1`/`#4caf50` frå
`monitorering.md`) for `classDef default/ekstern/ci/mcp/konsument` og
subgraph-bakgrunnane (`style KILDE/MCP/CI/PUBLISERT/KATALOGAR/EKSTERNREPO/KONSUMENTER`)
i begge diagramma i `arkitektur-oversikt.md`.
