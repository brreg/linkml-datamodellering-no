# Om dette repoet

!!! note "Bakgrunn"

    Dette repoet er utvikla av Brønnøysundregistrene med mål om å bli ein nasjonal ressurs for arbeid med informasjonsmodellering, i tråd med
    [Digdirs Rammeverk for informasjonsforvaltning](https://www.digdir.no/informasjonsforvaltning/rammeverk-informasjonsforvaltning/3626).

    Det skal gjere det enklare for offentlege verksemder og næringsliv å modellere, validere og publisere begreps- og informasjonsmodellar etter norske og europeiske standardar (DCAT-AP-NO, SKOS-AP-NO m.fl.), og å dele felles verktøy og applikasjonsprofilar på tvers av organisasjonar. 

Dette repoet stimulerer samarbeid og deling gjennom standardiserte formater, felles verktøy og en felles infrastruktur etter prinsippet "Lett å gjere rett!"

Ikkje minst legges det tilrete for å eksportere modeller og data på W3C-semantiske format som saman med bruk av offentlige ontologiar og felles begrep gjer at dataene blir innebygd lenkbare på tvers av datasett.

## Kontakt

**Repo-administrator:** Audun Vindenes Egge ([ave@brreg.no](mailto:ave@brreg.no))

## Bidra og gje tilbakemelding

- [GOVERNANCE.md](https://github.com/brreg/linkml-datamodellering-no/blob/main/GOVERNANCE.md) —
  roller, myndigheit og korleis avgjerder vert tekne
- [CONTRIBUTING.md](https://github.com/brreg/linkml-datamodellering-no/blob/main/CONTRIBUTING.md) —
  korleis du bidrar med modellar, feilretting eller verktøyutvikling
- [Opne eit GitHub Issue](https://github.com/brreg/linkml-datamodellering-no/issues) —
  for feilrapportering, spørsmål eller forslag til nye modellar/funksjonalitet
- [SECURITY.md](https://github.com/brreg/linkml-datamodellering-no/blob/main/SECURITY.md) —
  korleis du rapporterer sikkerheitssårbarheiter

## Lisens

Dette repoet er lisensiert under [MIT-lisens](https://github.com/brreg/linkml-datamodellering-no/blob/main/LICENSE).
Dei enkelte modellane har egne lisensar for bruk — sjå `license`-feltet i det einskilde skjemaet.

## Attribusjoner

Dette repoet bygger og publiserer containerbilete
(`ghcr.io/brreg/linkml-local`, `mcp-linkml-validator`, `mcp-linkml-modell-utkast`,
`mcp-linkml-begrep-utkast` m.fl.) og denne dokumentasjonsportalen ved hjelp av
følgjande tredjepartsverktøy. Verktøy som berre brukast internt i CI eller
lokalt byggesteg — og aldri bundlast i eit publisert containerbilete eller i
den publiserte portalen — er utelatne.

| Verktøy | Lisens | Brukt til |
|---|---|---|
| [LinkML](https://github.com/linkml/linkml) | Apache License 2.0 | Skjemavalidering og -generering |
| [rdflib](https://github.com/RDFLib/rdflib) | BSD 3-Clause License | RDF-prosessering |
| [Graphviz](https://gitlab.com/graphviz/graphviz) | Eclipse Public License 2.0 | ER-diagramgenerering |
| [PyYAML](https://github.com/yaml/pyyaml) | MIT License | YAML-prosessering |
| [pytest](https://github.com/pytest-dev/pytest) | MIT License | Testing |
| [openapi-spec-validator](https://github.com/python-openapi/openapi-spec-validator) | Apache License 2.0 | OpenAPI-validering |
| [avrotize](https://github.com/clemensv/avrotize) | MIT License | Skjemakonvertering (Avro/XSD m.fl.) |
| [AsyncAPI CLI](https://github.com/asyncapi/cli) | Apache License 2.0 | AsyncAPI-spesifikasjonsgenerering |
| [Python](https://www.python.org/) | PSF License 2.0 | Køyretidsmiljø i containerbileta |
| [mkdocs-material](https://github.com/squidfunk/mkdocs-material) | MIT License | Tema for denne dokumentasjonsportalen |

Fullstendig oversikt over alle verktøy som er vurdert — inkludert dei som
ikkje krev attribution, og kvifor — finst i
[`specs/done/verktoy-lisensoversikt.md`](https://github.com/brreg/linkml-datamodellering-no/blob/main/specs/done/verktoy-lisensoversikt.md).
