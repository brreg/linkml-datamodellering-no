Modellere opp BR modell fra MagicDraw (bvrinn) (må testes meir)

teste ut anna publiseringsløsning enn mkdocs

automatisk publisering av modell til felles datakatalog (må testes)

(importere begreper fra felles begrepskatalog)
automatisk publisere begreper til felles begrepskatalog (må testes)

modellere generiske kodelister/kodeverk

validere br krav til metadata (har laga validering av Digdir krav til metadata)

teste fra-magicdraw-xmi til-linkml-yaml til-magicdraw-xmi for å verifisere om vi kan produsere gyldig magicdraw xmi-fil

Eit av måla med dette repoet er å realisere Digdirs Rammeverk for informasjonsforvaltning som eit nasjonalt verktøy.
Lag en spesifikasjon som kartlegger hvor godt dette repoet stemmer overens med Digdirs Rammeverk for informasjonsforvaltning:
https://www.digdir.no/informasjonsforvaltning/rammeverk-informasjonsforvaltning/3626

opprette slack kanal under digdir samarbeid?

alle linkml modellane er uoffisielle eksempelmodeller for å POCe modellering i LinkML. Evaluer om eg burde endra katalogstrukturen eller på ein anna måte dokumentert dette.

Modellere FINT Felles (mangler i dag)


Treng vi FAQ?



Korleis skal vi klassifisere informasjonsmodellar? https://data.norge.no/vocabulary/information-model-type

Kan vi klassifisere informasjonsmodellane i linkml-datamodellering-no repoet?

ngr https://informasjonsforvaltning.github.io/nasjonale-grunndata/
vs
person og enhet https://www.digdir.no/informasjonsforvaltning/person-og-enhet-felles-informasjonsmodell/2018


semic eu core vocabularies


https://semiceu.github.io/Core-Business-Vocabulary/releases/2.3.0/
https://semiceu.github.io/Core-Business-Vocabulary/releases/2.3.0/html/overview.jpg


konvertere fleire BRREG modellar


gå igjennom alle ferdiggenererte index.md filer for alle modellar og finn ut om alle modellar har alle 6 badges. Kartlegg avvik og foreslå tiltak. Skriv til /specs

badges i readme


Hei! Du gikk glipp av denne samtalen fordi det foregikk på Slack fredag:
 
Da har jeg etter flere runder med prøving og feiling sammen med Zaher funnet ut årsaken. Feilen var egentlig ikke relatert til anyof og oneof i det hele tatt. Vi har nå testet og verifisert at skjema fungerer.
Feil 1 — additionalProperties: false
"additionalProperties": false er en boolean-schema. JsonSchema.Net gir den Keywords == null. Analysatoren kaller AsWorkList() uten null-sjekk og kaster:

System.ArgumentNullException: Value cannot be null. (Parameter 'source')
   at JsonSchemaAnalyzer.IsValidSimpleTypeRestriction(JsonSchema) : line 692
Dette er en reell bug i Altinns kode (manglende null-guard, jf. at HasSingleAllOf har den). Fikset i skjemaet ved å fjerne alle 26 forekomster.
Feil 2 — egendefinerte x-nøkler


Metamodell-konverteren har en whitelist og kaster på ukjente keywords:

MetamodelConvertException: Keyword x-schema-id not processed!
   at JsonSchemaToMetamodelConverter.ProcessKeyword() : line 203
Gjaldt x-schema-id, x-major-version, x-dct-modified, x-adms-status, x-servicedomain. Skjult bak feil 1. Fikset ved å fjerne nøklene.
Resultat etter begge fikser


Kjørt mot Altinns faktiske kode: Validator: VALID og Metamodel conversion: OK. oneOf/anyOf beholdt uendret.
 
Helland, Tore
 
Er det noe vi kan legge inn som valgfritt å filtrere vekk i genereringsløsningen våre (Altinn-skjema true/false) som parateter. Uansett, burde vi få Altinn til å gjøre endringer for hva som kan godtas, men det kan ta tid.
 



  Confirmed — the earlier failure was the sandbox blocking podman's rootless namespace setup (newuidmap), not a real command failure.


  odrl standard

  Terje Sylversnes
  Kjersti Steien følger opp etteer Jim

  SIMPL prosjektet EU har lagt inn støtte for content negotiation i plattformen

  DID

   Container-verktøyet krev rettar sandboxen blokkerer (newuidmap: Operation not permitted).


   gjer ein analyse av all kildekode og identifiser bruk av inlining. Kom med forslag til konvensjon rundt inlining og forslag til korleis vi kan unngå inlining der det går utotver lesbarhet, testbarhet, logging (feilsluking) eller gjenbrukbarhet.

   hamnar -> havner

   slotsnamn -> slotnavn

Demo:  
make check-prereqs

make new-modell DOMAIN=domene NAME=modellnavn

make validate SCHEMA=src/linkml/oreg/

make analyse-similar-classes-domain DOMAIN=ap-no

make analyse-similar-slots-domain DOMAIN=ap-no

make gen-informasjonsmodell-instance SCHEMA=src/linkml/oreg/


make new-begrepssamling DOMAIN=domene NAME=begrepssamling-navn

