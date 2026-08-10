# Vurdering: Code-to-Knowledge-Graph-kompatibilitet med repoet

**Kjelde:** [github.com/Bevel-Software/code-to-knowledge-graph](https://github.com/Bevel-Software/code-to-knowledge-graph)
**Dato vurdert:** 2026-08-10
**Konklusjon:** Ikkje kompatibelt i praksis — tilrådd ikkje adoptert (av andre grunnar enn lisens)

---

## Bakgrunn

Code-to-Knowledge-Graph er eit Kotlin/JVM-bibliotek som parsar kjeldekode og byggjer ein
rik, spørjbar kunnskapsgraf (entitetar, relasjonar, arkitekturinnsikt) ved å bruke
**VS Code sin Language Server Protocol (LSP)** for fleirspråkleg parsing. Det er kjernen
i "Bevel"-økosystemet (VS Code-utviding, Neo4j-visualisering, testgenerator). Brukaren ba
om ei tilsvarande vurdering som for SocratiCode, med eksplisitt vurdering av lisensen.

## Funn

### 1. Distribusjonsform: JVM-bibliotek, ikkje eit ferdig verktøy/MCP-tenar

I motsetnad til SocratiCode er dette **ikkje** ein MCP-tenar eller CLI ein installerer og
brukar direkte. Dei to offisielle bruksmåtane er:

- **Pre-bygd VS Code-utviding ("Bevel")** — installerast frå VS Code Marketplace. Dette er
  eit personleg IDE-verktøyval for den enkelte utviklaren, ikkje repo-infrastruktur, og
  gjev ikkje AI-assistenten (Claude Code) direkte tilgang.
- **Direkte integrasjon via Gradle** — `implementation("software.bevel:code-to-knowledge-graph:1.1.3")`
  i eit Kotlin/Java-prosjekt, med eigen kode som kallar `Parser`/`Graphlike`-API-et. Dette
  krev at nokon **skriv og byggjer eit heilt nytt JVM-program** rundt biblioteket for at
  det skal gjere noko nyttig — det finst ingen ferdig CLI eller server å køyre.

### 2. Krev eit nytt byggøkosystem (JVM/Kotlin/Gradle) repoet ikkje har

Repoet sin eksisterande verktøystack er Python (LinkML, MCP-tenarar), Bash/Make og
podman-containerar — ingen Java/Kotlin/Gradle-infrastruktur finst i dag. Å ta i bruk
dette biblioteket ville krevje å byggje heilt ny tooling frå botnen: eit Gradle-prosjekt,
eigen Kotlin/Java-kode mot API-et, og ein eigen `Dockerfile` for å pakke det inn i ein
podman-køyrbar container (i motsetnad til SocratiCode finst det her ingen publisert
container-image eller MCP-integrasjon å lene seg på — alt måtte skrivast sjølv).

### 3. Avhengig av VS Code sine LSP-serverar

Kjernefunksjonaliteten ("robust, multi-language parsing") er bygd på VS Code sine
språkserverar (LSP), ikkje ein sjølvstendig parser. Dette betyr at nøyaktig parsing i
praksis føreset anten ein køyrande VS Code-instans/extension host, eller manuell oppsett
av dei aktuelle LSP-serverane for kvart språk som skal analyserast — ein tungvekt,
IDE-kopla avhengigheit som ikkje let seg reprodusere reint med `pip install`/`podman run`
slik dei andre MCP-verktøya i repoet gjer.

### 4. Domenemismatch: repoet har lite tradisjonell kjeldekode å analysere

Verktøyet sin kjerneverdi er entitetar/relasjonar/kallgrafar mellom funksjonar og klasser
i tradisjonell programvare. Dette repoet består i hovudsak av LinkML-skjema (YAML) —
deklarative datamodellar utan funksjonar, klassar eller kallgrafar i tradisjonell
forstand. Den vesle mengda faktisk kjeldekode som finst (Python i
`src/mcp-linkml-*/`, shell/Make-skript) dekkjer eit for lite volum til å rettferdiggjere
ny byggeinfrastruktur, og importhierarkiet mellom LinkML-skjema er allereie dokumentert
manuelt (`mkdocs/docs/arkitektur/importhierarki.md`) — det finst ikkje eit tilsvarande
udekt behov for "kunnskapsgraf over kjeldekode" i dette repoet.

## Lisensvurdering

**Lisens:** [Mozilla Public License 2.0 (MPL-2.0)](https://github.com/Bevel-Software/code-to-knowledge-graph/blob/main/LICENSE) — stadfesta i GitHub-metadata og `LICENSE`-fila.

MPL-2.0 er ein **fil-nivå ("weak") copyleft**-lisens, vesentleg mindre restriktiv enn
SocratiCode sin AGPL-3.0:

- Endringar i **MPL-lisensierte filer** frå dette biblioteket må framleis distribuerast
  under MPL-2.0 dersom dei vert distribuerte.
- Biblioteket kan derimot **kombinerast fritt med anna kode** (t.d. proprietær eller
  NLOD-lisensiert kode) i eit "Larger Work" utan at resten av verket vert smitta av
  copyleft-krava — i motsetnad til AGPL-3.0, som krev at *heile* det avleia verket
  vert opna dersom det tilbys som nettverksteneste.
- Ingen krav om å opne eige, urelatert kjeldekode berre fordi biblioteket vert brukt som
  ein uendra avhengigheit.
- Repoet sitt `NOTICE`-oppslag viser at dei transitive avhengigheitene (Jackson, hash4j
  m.fl.) i hovudsak er Apache License 2.0 — ingen kjende problematiske transitive lisensar.

**Konklusjon lisens:** MPL-2.0 er **kompatibelt** og utgjer **ikkje** eit hinder for bruk
i dette repoet. Dersom biblioteket nokon gong vart bunta inn i eit publisert
containerbilete eller mkdocs-portalen, ville CLAUDE.md sitt krav om å sjekke
attribution-behov ved nye verktøyavhengigheiter gjelde (sjå «Nye verktøyavhengigheiter» i
CLAUDE.md og attributions-tabellen i `mkdocs/docs/om.md`) — MPL-2.0 krev at
lisensmerknader/kjeldekode-tilgjenge for *biblioteket sjølv* vert bevart, noko ei
attribution-oppføring ville dekkje. Dette er ei rein formalitet, ikkje eit reelt hinder.

## Konklusjon

I motsetnad til SocratiCode er **ikkje lisensen** problemet her — MPL-2.0 er godt
kompatibelt. Verktøyet er likevel **ikkje kompatibelt i praksis** med repoet, av andre
grunnar:

- Det er eit JVM/Kotlin-**bibliotek**, ikkje eit ferdig verktøy — krev at nokon byggjer
  eit heilt nytt program rundt det, inkludert eigen containerisering for podman-samsvar
- Krev eit byggøkosystem (Gradle/Kotlin) repoet ikkje har og ikkje elles treng
  (jf. DRY-/minimal-endring-prinsippet i CLAUDE.md — å innføre eit nytt språkøkosystem for
  eitt verktøy er disproporsjonalt)
- Kjernefunksjonaliteten er avhengig av VS Code sine LSP-serverar, ein tungvekt
  IDE-kopla avhengigheit utan eit reint containerbart installasjonsspor
- Den analytiske verdien (kallgrafar/kodeentitetar) har lita relevans for eit repo som i
  hovudsak inneheld deklarative LinkML-skjema, ikkje tradisjonell programvarekode med
  funksjonar/klassar å analysere

**Tilråding:** Ikkje adopter Code-to-Knowledge-Graph i dette repoet. Dersom nokon
individuelt ønskjer kodenavigering i eigen editor, er "Bevel"-VS Code-utvidinga eit
personleg IDE-verktøyval utanfor repoets infrastruktur, og krev inga endring i repoet.

## Utført

Vurderinga er fullført basert på gjennomgang av repoet sin README (Quick Start,
Key Features), `LICENSE`- og `NOTICE`-filene, og samanlikning med repoets eksisterande
verktøystack (Python/Make/podman) og førande prinsipp (CLAUDE.md). Ingen kodeendringar
er gjort — dette er ei rein kartleggings-/vurderingsoppgåve.
