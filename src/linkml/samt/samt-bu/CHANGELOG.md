# Changelog

## [1.11.0](https://github.com/brreg/linkml-datamodellering-no/compare/samt-bu-v1.10.1...samt-bu-v1.11.0) (2026-08-25)


### Features

* **gen-java:** legg til make gen-java og Java-bruk-seksjon i Kom i gang ([74396fc](https://github.com/brreg/linkml-datamodellering-no/commit/74396fcfb1531244e32d27599bf09353381e3fb1))

## [1.10.1](https://github.com/brreg/linkml-datamodellering-no/compare/samt-bu-v1.10.0...samt-bu-v1.10.1) (2026-08-17)


### Bug Fixes

* **scaffolding:** kollisjonsfri kontaktinformasjon-slot + dynamisk dcat-ap-no-versjon i new-modell ([f291dac](https://github.com/brreg/linkml-datamodellering-no/commit/f291dacd1ce17bffc8327cfabd571e3d3845af83))

## [1.10.0](https://github.com/brreg/linkml-datamodellering-no/compare/samt-bu-v1.9.0...samt-bu-v1.10.0) (2026-08-14)


### Features

* **generatorar:** legg til gen-graphql for GraphQL SDL-generering ([cb0a7bd](https://github.com/brreg/linkml-datamodellering-no/commit/cb0a7bd4c220dbee889df488bed0eaeb25960ce4))
* **make,ci:** fullført logging-rammeverk med DEBUG/INFO/ERROR-nivå ([9b72abe](https://github.com/brreg/linkml-datamodellering-no/commit/9b72abefbbe4747d120b3ef8681d0cc420f69740))


### Bug Fixes

* **build-manifest:** legg til manglande generator-flagg i 11 build.yaml ([916d9df](https://github.com/brreg/linkml-datamodellering-no/commit/916d9df3205e7b1cb322eb8bdc8a59ce4d692a5b))
* **mcp-linkml-validator:** vis reelle MCP-feil + patch relativ-import-bug for versjonslåste ([4773c74](https://github.com/brreg/linkml-datamodellering-no/commit/4773c7437e2ec01c649fba3890358f13d657a8b1))
* **mkdocs:** rett inkonsistent valideringsbadge og -resultat ([9cb9fbb](https://github.com/brreg/linkml-datamodellering-no/commit/9cb9fbb7f5d2a82038a79a34e095a63e5c40d389))
* **samt-bu:** description endring for å trigge release-please og generate workflowane. ([42ddec7](https://github.com/brreg/linkml-datamodellering-no/commit/42ddec7ed50d6729d8548cf21ea14c607a36d014))
* **samt-bu:** rett ugyldig format/spraak-verdiar i eksempelfil ([982bbd1](https://github.com/brreg/linkml-datamodellering-no/commit/982bbd19e4e25e98291a6d881efa17d0959c564f))
* **samt-bu:** trigger ny release-please køyring for å verifisere om det kun er samt-bu som får trigga ny versjon. ([6624bf8](https://github.com/brreg/linkml-datamodellering-no/commit/6624bf8d9168711d9b8da077c90b2c197366d845))
* **validering:** bruk validation_policy konsekvent, fjern bronze-fallback, kopier validation-loggar ([cb816aa](https://github.com/brreg/linkml-datamodellering-no/commit/cb816aa383a4d89c9e21f7fe4696e674d535da01))


### Performance Improvements

* **mcp-linkml-validator:** parallelliser validate-examples, regenerer valideringsloggar ([fc67279](https://github.com/brreg/linkml-datamodellering-no/commit/fc672798d9b85870590a1bf7ea33fbca4181bf51))

## [1.9.0](https://github.com/brreg/linkml-datamodellering-no/compare/samt-bu-v1.8.0...samt-bu-v1.9.0) (2026-08-02)


### Features

* **asyncapi:** reduser image-storleik frå 4.43 GB til 296 MB ([0b61fa2](https://github.com/brreg/linkml-datamodellering-no/commit/0b61fa2c813b89f1fef0357e5fe119f75b6c1ccb))


### Bug Fixes

* **docgen:** endre Metadata til Modellmetadata og flytt anker til metadata.sh ([a83174b](https://github.com/brreg/linkml-datamodellering-no/commit/a83174bb6cd3d4a9b01603e5aac09444bfdfd606))
* **samt-bu:** Endrer description for ein attributt for å trigge revalidering av samt-bu modellen i CI pipeline ([e09fa5a](https://github.com/brreg/linkml-datamodellering-no/commit/e09fa5a65e3107a53338959a5e90b09cd3bd1b97))

## [1.8.0](https://github.com/brreg/linkml-datamodellering-no/compare/samt-bu-v1.7.0...samt-bu-v1.8.0) (2026-07-30)


### Features

* **makefile:** containeriser alle Python-kall ([a1833a2](https://github.com/brreg/linkml-datamodellering-no/commit/a1833a2dfd3fc0b3363f7fc43192115d66dc9ac5))
* **metadata:** dynamisk README-generering frå skjema-metadata ([53def55](https://github.com/brreg/linkml-datamodellering-no/commit/53def559d46e92c604ff429b46be90381f907eaf))

## [1.7.0](https://github.com/brreg/linkml-datamodellering-no/compare/samt-bu-v1.6.0...samt-bu-v1.7.0) (2026-07-27)


### Features

* **docgen:** fullstendig tabellradteljing, versjonerte imports og Subsets-kolonne ([de26c53](https://github.com/brreg/linkml-datamodellering-no/commit/de26c537241776f6ba6de670da52f1c6f6e8f6f8))

## [1.6.0](https://github.com/brreg/linkml-datamodellering-no/compare/samt-bu-v1.5.0...samt-bu-v1.6.0) (2026-07-10)


### Features

* **ap-no:** publiser common-ap-no i nav-meny og omdøp katalog ([9653abf](https://github.com/brreg/linkml-datamodellering-no/commit/9653abf7a46a7714b216e3d0f6e3ebb97efeabc9))
* **ci:** legg til XSD-generering via avrotize-pipeline ([22b585b](https://github.com/brreg/linkml-datamodellering-no/commit/22b585b91e357a8280ad2c9c914407e8a0b1057a))
* **docgen:** vis alle brukte typar/enums inkl. importerte i index.md ([cdb0480](https://github.com/brreg/linkml-datamodellering-no/commit/cdb04802ccd9d6d982018e163029397c4ac70d5e))
* legg til flag for publisering av kvar enkelt modell i manifest.yaml som er omdøpt fra generate.yaml. Flytter data og examples katalogane inn under src/linkml/domene slik at alle relaterte filer ligg i samme struktur. ([a4cccbd](https://github.com/brreg/linkml-datamodellering-no/commit/a4cccbdfb8e327d0a9bb1874b34ec21bd9c374d0))
* legg til OpenAPI 3.1 og AsyncAPI 3.0-generering ([7be7ef8](https://github.com/brreg/linkml-datamodellering-no/commit/7be7ef8ad6e4cda9fb2a08bbc336e1c782d5d794))
* **makefile:** legg til timing og stille logging for gen-xsd og gen-informasjonsmodell-instance ([0d00e6f](https://github.com/brreg/linkml-datamodellering-no/commit/0d00e6fa35ef1c87af1c32572416107dbc4b2d55))
* **mkdocs:** konfigurerbar lenke-tekst for offisiell referanse og description.md for alle modellar ([20d8bf8](https://github.com/brreg/linkml-datamodellering-no/commit/20d8bf8c0e3d5ed31c608ece6bf5d64d7802b9af))
* **mkdocs:** konfigurerbare seksjons-kjelder i index.md ([122c704](https://github.com/brreg/linkml-datamodellering-no/commit/122c7047e78c3a54952d9c91910d62f53da682a3))
* **validate-capture:** parallelliser validering av alle skjema ([7d9a0a2](https://github.com/brreg/linkml-datamodellering-no/commit/7d9a0a28797a918d887b6ff22303ac6d56204655))


### Bug Fixes

* **ap-no:** fjern tvetydig type for lisens og hardkod generator-flagg ([e7029d7](https://github.com/brreg/linkml-datamodellering-no/commit/e7029d735d66bc9a0ae4b1918dd7c431b6a0c7ef))
* **los:** rett alle Los-URI-avvik og legg til rettleiing (LO1–LO5) ([05df4cc](https://github.com/brreg/linkml-datamodellering-no/commit/05df4ccd0f7b1565bd34b5fe039e238d3427bb63))
* løys valideringsfeil i samt-bu og rotårsak i dqv-ap-no (BUG-6) ([cc5f104](https://github.com/brreg/linkml-datamodellering-no/commit/cc5f104abc70530c6dbd2a2b97cdb76a1e25bcec))
* **mkdocs:** flytt horisontal linje frå badges til etter description og fjern støymeldingar ([3389d3d](https://github.com/brreg/linkml-datamodellering-no/commit/3389d3d4d83bee7c19e51e469b265183959a10e9))
* **release:** synk schema-versjon med release-nummer automatisk ([1d20298](https://github.com/brreg/linkml-datamodellering-no/commit/1d20298b932da0e876795152aab61baf99611daf))
* **samt-bu,asyncapi:** fjern overflødige åtvaringar frå make samt ([1dfd071](https://github.com/brreg/linkml-datamodellering-no/commit/1dfd071f00a5fae8444b362699334de9115b95c2))
* **samt-bu:** legg på begrepsidentifikator på person klassen ([ef615b2](https://github.com/brreg/linkml-datamodellering-no/commit/ef615b215c470ff06a8eb7d418706212ceb9ac6b))
* **samt-bu:** legg til begrepesidentifikator for Kontaktlaerer klassen ([86a44b2](https://github.com/brreg/linkml-datamodellering-no/commit/86a44b228bf2e8c95430ff94bf7f602645531cfc))
* **samt-bu:** legg til begrepsidentifikator for skole klassen ([a779825](https://github.com/brreg/linkml-datamodellering-no/commit/a7798250a9c4b541a05c3ce54a64d7d5deb3425a))
* **samt-bu:** legg til begrepsidentifikator for skoleeier ([7406526](https://github.com/brreg/linkml-datamodellering-no/commit/7406526fb4903e66f06cb66bf96679ad760e5933))
* **samt-bu:** legg til begrpsidentifikator for kommune klassen ([baf0bd4](https://github.com/brreg/linkml-datamodellering-no/commit/baf0bd4336786a9ae7a29e014718a7a9bc0bc688))
* **samt-bu:** rett stale slotnamn på Kvalitetsdimensjon-instans i eksempel ([dbda72a](https://github.com/brreg/linkml-datamodellering-no/commit/dbda72ac21c417c8e31e97fa7832fbc993242f76))
* **schemas,mcp-validator:** etterlevingsopprett mot Digdir felles modelleringsreglar (regel 6-11, 15) ([93a25e7](https://github.com/brreg/linkml-datamodellering-no/commit/93a25e79c2eacdfa5d7548d176370200efc79279))
* **validation:** Viser valideringsresultat for siste validering i index.md for kvar modell i mkdocs portal ([3b3baa3](https://github.com/brreg/linkml-datamodellering-no/commit/3b3baa30f84fe8cbf7c4bf9128eb2680dd979c72))

## [1.5.0](https://github.com/brreg/linkml-datamodellering-no/compare/samt-bu-v1.4.0...samt-bu-v1.5.0) (2026-07-10)


### Features

* **makefile:** legg til timing og stille logging for gen-xsd og gen-informasjonsmodell-instance ([4791036](https://github.com/brreg/linkml-datamodellering-no/commit/4791036318f9a52355a4e69dba8b9aac3734ebc4))

## [1.4.0](https://github.com/brreg/linkml-datamodellering-no/compare/samt-bu-v1.3.0...samt-bu-v1.4.0) (2026-07-09)


### Features

* **ap-no:** publiser common-ap-no i nav-meny og omdøp katalog ([35da103](https://github.com/brreg/linkml-datamodellering-no/commit/35da103f75e856685bf01e255b732241792964fa))
* **mkdocs:** konfigurerbar lenke-tekst for offisiell referanse og description.md for alle modellar ([97dacce](https://github.com/brreg/linkml-datamodellering-no/commit/97dacce159f02236196c9daa686e375e503f15ef))


### Bug Fixes

* **mkdocs:** flytt horisontal linje frå badges til etter description og fjern støymeldingar ([f5969b3](https://github.com/brreg/linkml-datamodellering-no/commit/f5969b325255479a2059c2679975c9177cb3de9e))

## [1.3.0](https://github.com/brreg/linkml-datamodellering-no/compare/samt-bu-v1.2.0...samt-bu-v1.3.0) (2026-07-06)


### Features

* **mkdocs:** konfigurerbare seksjons-kjelder i index.md ([94c2efb](https://github.com/brreg/linkml-datamodellering-no/commit/94c2efb8c90571a03efa5108a869e5204544bcbf))

## [1.2.0](https://github.com/brreg/linkml-datamodellering-no/compare/samt-bu-v1.1.0...samt-bu-v1.2.0) (2026-07-04)


### Features

* **validate-capture:** parallelliser validering av alle skjema ([6267587](https://github.com/brreg/linkml-datamodellering-no/commit/6267587223de8b03fe459c0d6458c492aa5dd279))

## [1.1.0](https://github.com/brreg/linkml-datamodellering-no/compare/samt-bu-v1.0.6...samt-bu-v1.1.0) (2026-07-04)


### Features

* **docgen:** vis alle brukte typar/enums inkl. importerte i index.md ([9d8b13e](https://github.com/brreg/linkml-datamodellering-no/commit/9d8b13e6eb8befd9d3e89b7d7aca9a2b9af06089))


### Bug Fixes

* **release:** synk schema-versjon med release-nummer automatisk ([6dbb358](https://github.com/brreg/linkml-datamodellering-no/commit/6dbb358b6929bfbd73ef9c5fde8f1a0c24cb56e2))

## [1.0.6](https://github.com/brreg/linkml-datamodellering-no/compare/samt-bu-v1.0.5...samt-bu-v1.0.6) (2026-07-04)


### Bug Fixes

* **ap-no:** fjern tvetydig type for lisens og hardkod generator-flagg ([c6514ca](https://github.com/brreg/linkml-datamodellering-no/commit/c6514ca76cfaa3c85753a3515b9481f726997a8f))

## [1.0.5](https://github.com/brreg/linkml-datamodellering-no/compare/samt-bu-v1.0.4...samt-bu-v1.0.5) (2026-07-03)


### Bug Fixes

* løys valideringsfeil i samt-bu og rotårsak i dqv-ap-no (BUG-6) ([49a093a](https://github.com/brreg/linkml-datamodellering-no/commit/49a093a19d2799ecdf606e0379dc19bc8b154126))
* **samt-bu,asyncapi:** fjern overflødige åtvaringar frå make samt ([76132b4](https://github.com/brreg/linkml-datamodellering-no/commit/76132b434d7941102d9d88bf586ea3003391dc0c))
* **samt-bu:** legg på begrepsidentifikator på person klassen ([efd8019](https://github.com/brreg/linkml-datamodellering-no/commit/efd80190a3fb0c84e5f07208d496d29e3a9ef5e3))
* **samt-bu:** legg til begrepesidentifikator for Kontaktlaerer klassen ([3dab033](https://github.com/brreg/linkml-datamodellering-no/commit/3dab0335740d467e4fd7db52d993b2a544caf83f))
* **samt-bu:** legg til begrepsidentifikator for skole klassen ([7e949f8](https://github.com/brreg/linkml-datamodellering-no/commit/7e949f89ae17acb089b7c21e8d3407b734405ba8))
* **samt-bu:** legg til begrepsidentifikator for skoleeier ([68c79d4](https://github.com/brreg/linkml-datamodellering-no/commit/68c79d4389ad80b3d555ff2bdd41d82fe2ea8354))
* **samt-bu:** legg til begrpsidentifikator for kommune klassen ([999e79a](https://github.com/brreg/linkml-datamodellering-no/commit/999e79a588d61f2cb46390c3342800c8674a96e5))
* **samt-bu:** rett stale slotnamn på Kvalitetsdimensjon-instans i eksempel ([6e4d623](https://github.com/brreg/linkml-datamodellering-no/commit/6e4d623d1a5f91b472748d45942e8a4fb05ad53b))
* **validation:** Viser valideringsresultat for siste validering i index.md for kvar modell i mkdocs portal ([723e61c](https://github.com/brreg/linkml-datamodellering-no/commit/723e61c410cda2763a62879a7728f02000812be4))

## [1.0.4](https://github.com/brreg/linkml-datamodellering-no/compare/samt-bu-v1.0.3...samt-bu-v1.0.4) (2026-07-02)


### Bug Fixes

* **samt-bu:** legg på begrepsidentifikator på person klassen ([efd8019](https://github.com/brreg/linkml-datamodellering-no/commit/efd80190a3fb0c84e5f07208d496d29e3a9ef5e3))
* **samt-bu:** legg til begrepesidentifikator for Kontaktlaerer klassen ([3dab033](https://github.com/brreg/linkml-datamodellering-no/commit/3dab0335740d467e4fd7db52d993b2a544caf83f))
* **samt-bu:** legg til begrepsidentifikator for skole klassen ([7e949f8](https://github.com/brreg/linkml-datamodellering-no/commit/7e949f89ae17acb089b7c21e8d3407b734405ba8))
* **samt-bu:** legg til begrepsidentifikator for skoleeier ([68c79d4](https://github.com/brreg/linkml-datamodellering-no/commit/68c79d4389ad80b3d555ff2bdd41d82fe2ea8354))
* **samt-bu:** legg til begrpsidentifikator for kommune klassen ([999e79a](https://github.com/brreg/linkml-datamodellering-no/commit/999e79a588d61f2cb46390c3342800c8674a96e5))

## [1.0.3](https://github.com/brreg/linkml-datamodellering-no/compare/samt-bu-v1.0.2...samt-bu-v1.0.3) (2026-07-01)


### Bug Fixes

* **samt-bu,asyncapi:** fjern overflødige åtvaringar frå make samt ([76132b4](https://github.com/brreg/linkml-datamodellering-no/commit/76132b434d7941102d9d88bf586ea3003391dc0c))
* **samt-bu:** rett stale slotnamn på Kvalitetsdimensjon-instans i eksempel ([6e4d623](https://github.com/brreg/linkml-datamodellering-no/commit/6e4d623d1a5f91b472748d45942e8a4fb05ad53b))

## [1.0.2](https://github.com/brreg/linkml-datamodellering-no/compare/samt-bu-v1.0.1...samt-bu-v1.0.2) (2026-06-20)


### Bug Fixes

* løys valideringsfeil i samt-bu og rotårsak i dqv-ap-no (BUG-6) ([49a093a](https://github.com/brreg/linkml-datamodellering-no/commit/49a093a19d2799ecdf606e0379dc19bc8b154126))

## [1.0.1](https://github.com/brreg/linkml-datamodellering-no/compare/samt-bu-v1.0.0...samt-bu-v1.0.1) (2026-06-19)


### Bug Fixes

* **los:** rett alle Los-URI-avvik og legg til rettleiing (LO1-LO5) ([7673852](https://github.com/brreg/linkml-datamodellering-no/commit/7673852bf911b8b8d0935aae6a471e9d1e79c485))
* **schemas,mcp-validator:** etterlevingsopprett mot Digdir felles modelleringsreglar (regel 6-11, 15) ([72aaaf2](https://github.com/brreg/linkml-datamodellering-no/commit/72aaaf2990834bf37a84cd514798141559e1ffef))
