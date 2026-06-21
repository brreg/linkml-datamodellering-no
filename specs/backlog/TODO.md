Modellere opp BR modell fra MagicDraw (bvrinn) (må testes meir)

teste ut anna publiseringsløsning enn mkdocs

automatisk publisering av modell til felles datakatalog (må testes)

(importere begreper fra felles begrepskatalog)
automatisk publisere begreper til felles begrepskatalog (må testes)

modellere generiske kodelister/kodeverk

generate workflow skal ha en matrix job pr domene

integrere mot custom schemaregistry (apicur.io). Avvist. Må utføres i eit anna repo.

integrere mot custom datakatalog (gcp data catalog) Avvist. Må utføres i eit anna repo.

validere br krav til metadata (har laga validering av Digdir krav til metadata)

teste fra-magicdraw-xmi til-linkml-yaml til-magicdraw-xmi for å verifisere om vi kan produsere gyldig magicdraw xmi-fil

Eit av måla med dette repoet er å realisere Digdirs Rammeverk for informasjonsforvaltning som eit nasjonalt verktøy.
Lag en spesifikasjon som kartlegger hvor godt dette repoet stemmer overens med Digdirs Rammeverk for informasjonsforvaltning:
https://www.digdir.no/informasjonsforvaltning/rammeverk-informasjonsforvaltning/3626

Vurder overensstemmelse med kvar av kildene under. For kvar kilde skriv oversikt over gap og tiltak som må utføres for å tette gapet.
Tilgjengeliggjøring av åpne daga: https://data.norge.no/guide/veileder-apne-data*

Beskrivelse av kvalitet på datasett - kvantifiserbar kvalitet: https://data.norge.no/guide/veileder-kvantifiserbar-kvalitet*

Veileder for beskrivelse av informasjonsmodeller: https://data.norge.no/guide/veileder-modelldcat-ap-no*

Standard for beskrivelse av datasett, datatjenester og datakataloger: https://data.norge.no/specification/dcat-ap-no/*

Forvaltningsstandard for begrepsbeskrivelser: https://www.digdir.no/standarder/forvaltningsstandard-omgrepsbeskrivingar-skos-ap-no-begrep/1682*

Termlosen: standard for begrepsanalyse og terminologiarbeid: https://www.digdir.no/standarder/termlosen/1733
Forvaltningsstandard for begrepsharmonisering og begrepsdifferensiering: https://data.norge.no/specification/forvaltningsstandard-begrepskoordinering*

Retningslinjer ved tilgjengeliggjøring av offentlige data: https://www.regjeringen.no/no/dokumenter/retningslinjer-ved-tilgjengeliggjoring-av-offentlige-data/id2536870/*

Spesifikasjon for beskrivelse av kvalitet på datasett: https://data.norge.no/specification/dqv-ap-no/*

Spesifikasjon for beskrivelse av informasjonsmodeller: https://data.norge.no/specification/modelldcat-ap-no/*

Los - Felles vokabular for klassifisering av offentlige tjenester og ressurser: https://www.digdir.no/informasjonsforvaltning/los-felles-vokabular-klassifisering-av-offentlige-tjenester-og-ressurser/2434*

Pekere til offentlige ressurser på nett: https://www.digdir.no/standarder/peikarar-til-offentlege-ressursar-pa-nett/1492*

Spesifikasjon for klassifikasjonsbeskrivelser: https://informasjonsforvaltning.github.io/xkos-ap-no/*

Prinsipper for informasjonsmodeller: https://www.digdir.no/informasjonsforvaltning/prinsipper-informasjonsmodeller/3030*

Felles modelleringsregler: https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029*



lage mermaid diagram som viser oversikt over alle dei vesentlige delane av dette repoet og korleis det er meint å fungere sammen med andre offentlige tjenester


juster generering av plantuml og er diagram 

opprette slack kanal under digdir samarbeid?

lage ein sturktur for å ta vare på output fra valideringer knytta til kvar modell


lag ein job som tester alle URL og URIer i repoet og logg html returkoden. 

lag ein job som identifiserer alle klasser med liknande navn på tvers av modellar.

lag ein job som identifiserar alle slots med liknande navn på tvers av modellar.

lag ein job som sjekker om alle mermaid diagram faktisk rendrer

alle linkml modellane er uoffisielle eksempelmodeller for å POCe modellering i LinkML. Evaluer om eg burde endra katalogstrukturen eller på ein anna måte dokumentert dette.

verifiser at manifest.yaml filene har flag for alle tilgjengelige artifakttypar og at README.md dokumenter alle.


evaluer gap mot https://www.digdir.no/datadeling/nasjonale-grunndata/7575 skriv til ./specs

evaluer gap mot https://www.digdir.no/datadeling/slik-kommer-du-i-gang-med-bruke-data-fra-andre/2255 skriv til ./specs

evaluer gap mot https://www.digdir.no/datadeling/slik-blir-du-en-god-datatilbyder/2248 skriv til ./specs

evaluer gap mot https://data.norge.no/nb/docs skriv til ./specs

evaluer gap mot https://www.digdir.no/informasjonsforvaltning/veileder-orden-i-eget-hus/2716 skriv til ./specs

lag plan for å oppdatere mkdocs/docs/ap-no-arkitektur.md eg ønsker å fjærne alle lukka avvik fra fila. Det er kun gjeldande avvik som er interessant å dokumentere skriv til ./specs


vær veldig kritisk og gjer ein full gjennomgang av dette repoet for å avdekke om det er noko vi bør handtere før vi inviterer andre brukere inn.