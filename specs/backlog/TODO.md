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
I tillegg må konseptet legge tilrette for at det skal være enkelt å kunne samarbeide om modellutvikling på tvers av organisasjoner. Vurder om vi må oppdatere CONTRIBUTING.md og om vi treng ei GOVERNANCE.md fil. Skriv til ./specs/backlog

Eit av måla med dette repoet er å realisere Digdirs Rammeverk for informasjonsforvaltning som eit nasjonalt verktøy.
Lag en spesifikasjon som kartlegger hvor godt dette repoet stemmer overens med Digdirs Rammeverk for informasjonsforvaltning:
https://www.digdir.no/informasjonsforvaltning/rammeverk-informasjonsforvaltning/3626
Vurder overensstemmelse med kvar av kildene under. For kvar kilde skriv oversikt over gap og tiltak som må utføres for å tette gapet.
Tilgjengeliggjøring av åpne daga: https://data.norge.no/guide/veileder-apne-data
Beskrivelse av kvalitet på datasett - kvantifiserbar kvalitet: https://data.norge.no/guide/veileder-kvantifiserbar-kvalitet
Veileder for beskrivelse av informasjonsmodeller: https://data.norge.no/guide/veileder-modelldcat-ap-no
Standard for beskrivelse av datasett, datatjenester og datakataloger: https://data.norge.no/specification/dcat-ap-no/
Forvaltningsstandard for begrepsbeskrivelser: https://www.digdir.no/standarder/forvaltningsstandard-omgrepsbeskrivingar-skos-ap-no-begrep/1682
Termlosen: standard for begrepsanalyse og terminologiarbeid: https://www.digdir.no/standarder/termlosen/1733
Forvaltningsstandard for begrepsharmonisering og begrepsdifferensiering: https://data.norge.no/specification/forvaltningsstandard-begrepskoordinering
Retningslinjer ved tilgjengeliggjøring av offentlige data: https://www.regjeringen.no/no/dokumenter/retningslinjer-ved-tilgjengeliggjoring-av-offentlige-data/id2536870/
Spesifikasjon for beskrivelse av kvalitet på datasett: https://data.norge.no/specification/dqv-ap-no/
Spesifikasjon for beskrivelse av informasjonsmodeller: https://data.norge.no/specification/modelldcat-ap-no/
Los - Felles vokabular for klassifisering av offentlige tjenester og ressurser: https://www.digdir.no/informasjonsforvaltning/los-felles-vokabular-klassifisering-av-offentlige-tjenester-og-ressurser/2434
Pekere til offentlige ressurser på nett: https://www.digdir.no/standarder/peikarar-til-offentlege-ressursar-pa-nett/1492
Spesifikasjon for klassifikasjonsbeskrivelser: https://informasjonsforvaltning.github.io/xkos-ap-no/
Prinsipper for informasjonsmodeller: https://www.digdir.no/informasjonsforvaltning/prinsipper-informasjonsmodeller/3030
Felles modelleringsregler: https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029

Skriv specen til ./specs/backlog
