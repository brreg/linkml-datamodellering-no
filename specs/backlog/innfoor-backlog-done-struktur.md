# Plan: innfør backlog/ og done/ i specs/

## Mål

Rydde `specs/` ved å skilje mellom specs som er aktive (backlog) og specs som er
avslutta (done). Gjer det umiddelbart tydeleg kva som er ope arbeid.

## Ny struktur

```
specs/
├── README.md               ← oppdaterast med forklaring på strukturen
├── backlog/                ← aktive specs: framtidig arbeid, opne forslag
└── done/                   ← avslutta specs: implementert, avgjort eller forelda
```

## Filer → backlog/

Åpne forslag, pågåande initiativ eller arbeid som ikkje er starta:

| Fil | Grunn |
|---|---|
| `developer-onboarding.md` | Fleire taktikkar, berre éi gjennomført |
| `developer-onboarding-tiltak1-evaluering.md` | Peikar på manglande dokumentasjon som framleis manglar |
| `dx-prof-linkml-modell.md` | Tidleg forslag, ikkje starta |
| `flytt-templates-til-mkdocs.md` | Ope spørsmål, inga avgjerd teken |
| `ny-domenemodell-pedagogisk-evaluering.md` | Tilrådde endringar er ikkje gjennomførte enno |
| `nynorsk-oversetting.md` | Pågåande omsetjingsarbeid |
| `public-repo-klargjering.md` | Sjekkliste med opne punkt for offentleg release |
| `readme-forslag.md` | README-omstrukturering ikkje implementert |
| `readme-kom-i-gang.md` | Splitting av «Kom i gang» ikkje gjennomført |
| `rename-schema-til-linkml-yaml.md` | Ope forslag, inga avgjerd |
| `vegkart.md` | Overordna vegkart — løpande referanse |
| `alternativ-b-detaljert.md` | Detaljert alternativ som framleis er under vurdering |

## Filer → done/

Implementerte features, avslutta analysar og gjennomførte avgjerder:

```
assets-scripts-stale.md
begrep-modellering.md
claude-md-stale.md
commands-md-stale.md
container-attributes-migrering.md
container-namngjeving.md
distribusjonsmodell.md
docker-image-storleik.md
dokumentasjon-begrep-og-mcp-begrep-generator.md
dokumentasjon-publisering-begrep.md
domenenamn-begrep-modell.md
examples-vs-data-publisering-stale.md
flytt-templates-til-mkdocs.md          ← (dersom avgjerd er teken)
gen-doc-eksempel-integrasjon.md
gen-plantuml-proto.md
generate-config-dokumentasjon.md
generate-config.md
generate-workflow-hastigheit.md
generate-workflow-parallelisering.md
generate-workflow-per-domain.md
generate-workflow-per-schema.md
generate-yaml-til-manifest-yaml.md
github-actions-caching.md
gource-video.md
harmonisering-make-kommandoar.md
image-build-optimering.md
json2linkml.md
katalogstruktur-stale-stiar.md
makefile-stale.md
mcp-linkml-begrep-generator.md
mcp-linkml-begrep-validator.md
mcp-server-namngjeving.md
namngjeving-konvensjonar.md
nasjonal-datamesh-arkitektur.md
nynorsk-oversetting.md                 ← (dersom ferdig)
omdoeyp-modelkatalog-modellkatalog.md
oppdater-validator-readme.md
portal-oppdatering.md
public-repo-status.md
publisering-felles-begrepskatalog.md
publisering-felles-datakatalog.md
publiserings-flagg.md
rename-schema-til-linkml-yaml.md       ← (dersom avvist)
scaffold-filer.md
security-pipeline-og-sbom.md
validate-workflow-parallelisering.md
workflows-stale.md
```

## Gjennomføring

```bash
mkdir -p specs/backlog specs/done

# Flytt backlog-filer
mv specs/developer-onboarding.md                     specs/backlog/
mv specs/developer-onboarding-tiltak1-evaluering.md  specs/backlog/
mv specs/dx-prof-linkml-modell.md                    specs/backlog/
mv specs/flytt-templates-til-mkdocs.md               specs/backlog/
mv specs/ny-domenemodell-pedagogisk-evaluering.md    specs/backlog/
mv specs/nynorsk-oversetting.md                      specs/backlog/
mv specs/public-repo-klargjering.md                  specs/backlog/
mv specs/readme-forslag.md                           specs/backlog/
mv specs/readme-kom-i-gang.md                        specs/backlog/
mv specs/rename-schema-til-linkml-yaml.md            specs/backlog/
mv specs/vegkart.md                                  specs/backlog/
mv specs/alternativ-b-detaljert.md                   specs/backlog/

# Flytt done-filer (alt som ikkje er i backlog/ og ikkje er README.md)
for f in specs/*.md; do
  [ "$(basename $f)" = "README.md" ] && continue
  mv "$f" specs/done/
done
```

## Oppdatering av README.md

Legg til forklaring på strukturen i `specs/README.md`:

```markdown
## Struktur

- `backlog/` — aktive specs: framtidig arbeid, opne forslag, pågåande vurderingar
- `done/` — avslutta specs: implementerte features, gjennomførte analysar, forkasta forslag

Nye specs opprettast alltid i `backlog/`. Når arbeidet er avslutta, flyttast fila til `done/`.
```

## Usikre klassifiseringar

Desse filene bør brukaren stadfeste før dei vert flytta:

| Fil | Spørsmål |
|---|---|
| `alternativ-b-detaljert.md` | Er dette alternativet avvist, eller framleis aktuelt? |
| `flytt-templates-til-mkdocs.md` | Er avgjerda teken? |
| `nasjonal-datamesh-arkitektur.md` | Referansedokument eller aktivt forslag? |
| `gource-video.md` | Gjennomført, eller framleis ønskjeleg? |
