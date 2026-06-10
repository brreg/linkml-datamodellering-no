Modellere opp BR modell fra MagicDraw (bvrinn)

teste ut anna publiseringsløsning enn mkdocs

automatisk publisering av modell til felles datakatalog (må testes)

(importere begreper fra felles begrepskatalog)
automatisk publisere begreper til felles begrepskatalog (må testes)

sette eigerksap til domener/modeller i .codeowners

modellere generiske kodelister/kodeverk

generate workflow skal ha en matrix job pr domene

generer OpenAPI/AsyncAPI spesifikasjon 
integrere mot custom schemaregistry (apicur.io)

integrere mot custom datakatalog (gcp data catalog)

conventional commits for versjonering av modeller (plan laga)

generere xml (vurdere avrotize mot andre alternativer)

validere br krav til metadata

lage CODEOWNERS.md der kvar modell får sin egen owner. I generering av modellkataloger src/assets/scripts/update-modellkatalog.py må vi ta hensymn til modelleigerskap i CODEOWNERS og gruppere modeller som eiges av samme organisasjon i samme modellkatalog. Det skal altså lages en modellkatalog pr organisasjon som eiger modeller i CODEOWNERS.md. Lag dokumentasjon som forklarer kva som skal til for at ein ny organisasjon skal ta ibruk repoet.