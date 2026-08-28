# Changelog

## [1.9.1](https://github.com/brreg/linkml-datamodellering-no/compare/register-over-aksjeeiere-v1.9.0...register-over-aksjeeiere-v1.9.1) (2026-08-28)


### Bug Fixes

* **class-uri:** rett 24 klassar til eksterne vokabularekvivalentar ([2becb35](https://github.com/brreg/linkml-datamodellering-no/commit/2becb35defec6f9024a75bf1168c175ae36000be))

## [1.9.0](https://github.com/brreg/linkml-datamodellering-no/compare/register-over-aksjeeiere-v1.8.2...register-over-aksjeeiere-v1.9.0) (2026-08-25)


### Features

* **gen-java:** legg til make gen-java og Java-bruk-seksjon i Kom i gang ([74396fc](https://github.com/brreg/linkml-datamodellering-no/commit/74396fcfb1531244e32d27599bf09353381e3fb1))

## [1.8.2](https://github.com/brreg/linkml-datamodellering-no/compare/register-over-aksjeeiere-v1.8.1...register-over-aksjeeiere-v1.8.2) (2026-08-20)


### Bug Fixes

* **inlining:** gjer container-inlining ufravikeleg, lenk Klasse/Part/Korrespondansepart ([f3ee148](https://github.com/brreg/linkml-datamodellering-no/commit/f3ee1488225021811e131672a4701101a1759244))

## [1.8.1](https://github.com/brreg/linkml-datamodellering-no/compare/register-over-aksjeeiere-v1.8.0...register-over-aksjeeiere-v1.8.1) (2026-08-17)


### Bug Fixes

* **lenkjesjekk:** rett resterande brotne lenkjer og ekskluder stadfesta upubliserte vokabular ([6cb82bf](https://github.com/brreg/linkml-datamodellering-no/commit/6cb82bfa54ceafaeaab625aae5dcfbaa8241eb2d))
* **scaffolding:** kollisjonsfri kontaktinformasjon-slot + dynamisk dcat-ap-no-versjon i new-modell ([f291dac](https://github.com/brreg/linkml-datamodellering-no/commit/f291dacd1ce17bffc8327cfabd571e3d3845af83))

## [1.8.0](https://github.com/brreg/linkml-datamodellering-no/compare/register-over-aksjeeiere-v1.7.0...register-over-aksjeeiere-v1.8.0) (2026-08-14)


### Features

* **generatorar:** legg til gen-graphql for GraphQL SDL-generering ([cb0a7bd](https://github.com/brreg/linkml-datamodellering-no/commit/cb0a7bd4c220dbee889df488bed0eaeb25960ce4))
* **make:** batch linkml-validate for validate-examples per domene ([a38f603](https://github.com/brreg/linkml-datamodellering-no/commit/a38f6030b61a6bf6c1230303112d148d2788281d))


### Bug Fixes

* **oreg,mcp-validator:** rett generate-workflow-feil for blomsterregisteret ([1bd6f61](https://github.com/brreg/linkml-datamodellering-no/commit/1bd6f6183d0586fc13e21ccb81f9affce4e54992))


### Performance Improvements

* **mcp-linkml-validator:** parallelliser validate-examples, regenerer valideringsloggar ([fc67279](https://github.com/brreg/linkml-datamodellering-no/commit/fc672798d9b85870590a1bf7ea33fbca4181bf51))

## [1.7.0](https://github.com/brreg/linkml-datamodellering-no/compare/register-over-aksjeeiere-v1.6.0...register-over-aksjeeiere-v1.7.0) (2026-08-02)


### Features

* **asyncapi:** reduser image-storleik frå 4.43 GB til 296 MB ([0b61fa2](https://github.com/brreg/linkml-datamodellering-no/commit/0b61fa2c813b89f1fef0357e5fe119f75b6c1ccb))


### Bug Fixes

* **ci:** ekskluder begrepssamling-katalogar og legg til validation_policy i modellkatalog ([fe7dce0](https://github.com/brreg/linkml-datamodellering-no/commit/fe7dce05a14fcf7736372248e1d551188415624f))

## [1.6.0](https://github.com/brreg/linkml-datamodellering-no/compare/register-over-aksjeeiere-v1.5.0...register-over-aksjeeiere-v1.6.0) (2026-07-30)


### Features

* **metadata:** dynamisk README-generering frå skjema-metadata ([53def55](https://github.com/brreg/linkml-datamodellering-no/commit/53def559d46e92c604ff429b46be90381f907eaf))

## [1.5.0](https://github.com/brreg/linkml-datamodellering-no/compare/register-over-aksjeeiere-v1.4.0...register-over-aksjeeiere-v1.5.0) (2026-07-10)


### Features

* **ci:** legg til XSD-generering via avrotize-pipeline ([22b585b](https://github.com/brreg/linkml-datamodellering-no/commit/22b585b91e357a8280ad2c9c914407e8a0b1057a))
* innfør conventional commits med release-please, commitlint og semver-versjonering per modell ([ea5a19b](https://github.com/brreg/linkml-datamodellering-no/commit/ea5a19bffa8dc8bc6e6d7b96b77bb2b7f6732142))
* legg til flag for publisering av kvar enkelt modell i manifest.yaml som er omdøpt fra generate.yaml. Flytter data og examples katalogane inn under src/linkml/domene slik at alle relaterte filer ligg i samme struktur. ([a4cccbd](https://github.com/brreg/linkml-datamodellering-no/commit/a4cccbdfb8e327d0a9bb1874b34ec21bd9c374d0))
* legg til OpenAPI 3.1 og AsyncAPI 3.0-generering ([7be7ef8](https://github.com/brreg/linkml-datamodellering-no/commit/7be7ef8ad6e4cda9fb2a08bbc336e1c782d5d794))
* **mkdocs:** konfigurerbar lenke-tekst for offisiell referanse og description.md for alle modellar ([20d8bf8](https://github.com/brreg/linkml-datamodellering-no/commit/20d8bf8c0e3d5ed31c608ece6bf5d64d7802b9af))
* **modellkatalog:** rull ut per-org-modellkatalogar og fyll metadata (MD2-MD4, MD6) ([48019b0](https://github.com/brreg/linkml-datamodellering-no/commit/48019b0822cd1a50a60d41fdb070071a3db2eadf))
* **validate-capture:** parallelliser validering av alle skjema ([7d9a0a2](https://github.com/brreg/linkml-datamodellering-no/commit/7d9a0a28797a918d887b6ff22303ac6d56204655))
* **validering:** komplett valideringssystem med auto-detect og visuell rapportering ([f0607bc](https://github.com/brreg/linkml-datamodellering-no/commit/f0607bc510640fa8c85b989b995e0162385eb06e))


### Bug Fixes

* **ap-no:** fjern tvetydig type for lisens og hardkod generator-flagg ([e7029d7](https://github.com/brreg/linkml-datamodellering-no/commit/e7029d735d66bc9a0ae4b1918dd7c431b6a0c7ef))
* **mkdocs:** URL-encode policy-namn i valideringsbadge ([57c6a70](https://github.com/brreg/linkml-datamodellering-no/commit/57c6a704e60563a906ffdb3a4912ee04493883cf))
* **release:** synk schema-versjon med release-nummer automatisk ([1d20298](https://github.com/brreg/linkml-datamodellering-no/commit/1d20298b932da0e876795152aab61baf99611daf))
* **schemas,mcp-validator:** etterlevingsopprett mot Digdir felles modelleringsreglar (regel 6-11, 15) ([93a25e7](https://github.com/brreg/linkml-datamodellering-no/commit/93a25e79c2eacdfa5d7548d176370200efc79279))

## [1.4.0](https://github.com/brreg/linkml-datamodellering-no/compare/register-over-aksjeeiere-v1.3.1...register-over-aksjeeiere-v1.4.0) (2026-07-09)


### Features

* **mkdocs:** konfigurerbar lenke-tekst for offisiell referanse og description.md for alle modellar ([97dacce](https://github.com/brreg/linkml-datamodellering-no/commit/97dacce159f02236196c9daa686e375e503f15ef))

## [1.3.1](https://github.com/brreg/linkml-datamodellering-no/compare/register-over-aksjeeiere-v1.3.0...register-over-aksjeeiere-v1.3.1) (2026-07-04)


### Bug Fixes

* **mkdocs:** URL-encode policy-namn i valideringsbadge ([c783b94](https://github.com/brreg/linkml-datamodellering-no/commit/c783b94e695a4cd97f3df1ea6da9ea1d567512b1))

## [1.3.0](https://github.com/brreg/linkml-datamodellering-no/compare/register-over-aksjeeiere-v1.2.2...register-over-aksjeeiere-v1.3.0) (2026-07-04)


### Features

* **validate-capture:** parallelliser validering av alle skjema ([6267587](https://github.com/brreg/linkml-datamodellering-no/commit/6267587223de8b03fe459c0d6458c492aa5dd279))

## [1.2.2](https://github.com/brreg/linkml-datamodellering-no/compare/register-over-aksjeeiere-v1.2.1...register-over-aksjeeiere-v1.2.2) (2026-07-04)


### Bug Fixes

* **release:** synk schema-versjon med release-nummer automatisk ([6dbb358](https://github.com/brreg/linkml-datamodellering-no/commit/6dbb358b6929bfbd73ef9c5fde8f1a0c24cb56e2))

## [1.2.1](https://github.com/brreg/linkml-datamodellering-no/compare/register-over-aksjeeiere-v1.2.0...register-over-aksjeeiere-v1.2.1) (2026-07-04)


### Bug Fixes

* **ap-no:** fjern tvetydig type for lisens og hardkod generator-flagg ([c6514ca](https://github.com/brreg/linkml-datamodellering-no/commit/c6514ca76cfaa3c85753a3515b9481f726997a8f))

## [1.2.0](https://github.com/brreg/linkml-datamodellering-no/compare/register-over-aksjeeiere-v1.1.0...register-over-aksjeeiere-v1.2.0) (2026-07-03)


### Features

* **validering:** komplett valideringssystem med auto-detect og visuell rapportering ([20caed0](https://github.com/brreg/linkml-datamodellering-no/commit/20caed0d1764e27864f377fcaea212506f3a6fab))

## [1.1.0](https://github.com/brreg/linkml-datamodellering-no/compare/register-over-aksjeeiere-v1.0.1...register-over-aksjeeiere-v1.1.0) (2026-07-01)


### Features

* **modellkatalog:** rull ut per-org-modellkatalogar og fyll metadata (MD2-MD4, MD6) ([7ee7b0e](https://github.com/brreg/linkml-datamodellering-no/commit/7ee7b0e0e71af5b62cadacf611e7c3b71b908f5c))

## [1.0.1](https://github.com/brreg/linkml-datamodellering-no/compare/register-over-aksjeeiere-v1.0.0...register-over-aksjeeiere-v1.0.1) (2026-06-19)


### Bug Fixes

* **schemas,mcp-validator:** etterlevingsopprett mot Digdir felles modelleringsreglar (regel 6-11, 15) ([72aaaf2](https://github.com/brreg/linkml-datamodellering-no/commit/72aaaf2990834bf37a84cd514798141559e1ffef))
