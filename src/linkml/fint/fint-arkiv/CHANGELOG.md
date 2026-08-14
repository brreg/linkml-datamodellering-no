# Changelog

## [4.6.0](https://github.com/brreg/linkml-datamodellering-no/compare/fint-arkiv-v4.5.0...fint-arkiv-v4.6.0) (2026-08-14)


### Features

* **generatorar:** legg til gen-graphql for GraphQL SDL-generering ([cb0a7bd](https://github.com/brreg/linkml-datamodellering-no/commit/cb0a7bd4c220dbee889df488bed0eaeb25960ce4))
* **make:** batch linkml-validate for validate-examples per domene ([a38f603](https://github.com/brreg/linkml-datamodellering-no/commit/a38f6030b61a6bf6c1230303112d148d2788281d))


### Bug Fixes

* **make:** rett stdin-konsumering i validate-bronze (BUG-10) ([91795ac](https://github.com/brreg/linkml-datamodellering-no/commit/91795ace2400341ba3ef052e4bb84cefe6e38215))
* **make:** valider ap-no-eksempelfiler via fixture, rett stdin-konsumerings-bug ([27c3979](https://github.com/brreg/linkml-datamodellering-no/commit/27c3979820230b8161e31aaf645917733745a5d6))
* **mkdocs:** aktiver plantuml-diagram for FINT, Begrepskatalog og Modellkatalog ([31881d6](https://github.com/brreg/linkml-datamodellering-no/commit/31881d6bdbb1660c29b9baaa4b14f7839e5f3364))


### Performance Improvements

* **mcp-linkml-validator:** parallelliser validate-examples, regenerer valideringsloggar ([fc67279](https://github.com/brreg/linkml-datamodellering-no/commit/fc672798d9b85870590a1bf7ea33fbca4181bf51))

## [4.5.0](https://github.com/brreg/linkml-datamodellering-no/compare/fint-arkiv-v4.4.0...fint-arkiv-v4.5.0) (2026-07-30)


### Features

* **metadata:** dynamisk README-generering frå skjema-metadata ([53def55](https://github.com/brreg/linkml-datamodellering-no/commit/53def559d46e92c604ff429b46be90381f907eaf))

## [4.4.0](https://github.com/brreg/linkml-datamodellering-no/compare/fint-arkiv-v4.3.0...fint-arkiv-v4.4.0) (2026-07-10)


### Features

* **ci:** legg til XSD-generering via avrotize-pipeline ([22b585b](https://github.com/brreg/linkml-datamodellering-no/commit/22b585b91e357a8280ad2c9c914407e8a0b1057a))
* legg til flag for publisering av kvar enkelt modell i manifest.yaml som er omdøpt fra generate.yaml. Flytter data og examples katalogane inn under src/linkml/domene slik at alle relaterte filer ligg i samme struktur. ([a4cccbd](https://github.com/brreg/linkml-datamodellering-no/commit/a4cccbdfb8e327d0a9bb1874b34ec21bd9c374d0))
* legg til OpenAPI 3.1 og AsyncAPI 3.0-generering ([7be7ef8](https://github.com/brreg/linkml-datamodellering-no/commit/7be7ef8ad6e4cda9fb2a08bbc336e1c782d5d794))
* **mkdocs:** konfigurerbar lenke-tekst for offisiell referanse og description.md for alle modellar ([20d8bf8](https://github.com/brreg/linkml-datamodellering-no/commit/20d8bf8c0e3d5ed31c608ece6bf5d64d7802b9af))
* **validate-capture:** parallelliser validering av alle skjema ([7d9a0a2](https://github.com/brreg/linkml-datamodellering-no/commit/7d9a0a28797a918d887b6ff22303ac6d56204655))
* **validering:** komplett valideringssystem med auto-detect og visuell rapportering ([f0607bc](https://github.com/brreg/linkml-datamodellering-no/commit/f0607bc510640fa8c85b989b995e0162385eb06e))


### Bug Fixes

* **ap-no:** fjern tvetydig type for lisens og hardkod generator-flagg ([e7029d7](https://github.com/brreg/linkml-datamodellering-no/commit/e7029d735d66bc9a0ae4b1918dd7c431b6a0c7ef))
* **release:** synk schema-versjon med release-nummer automatisk ([1d20298](https://github.com/brreg/linkml-datamodellering-no/commit/1d20298b932da0e876795152aab61baf99611daf))
* **schemas,mcp-validator:** etterlevingsopprett mot Digdir felles modelleringsreglar (regel 6-11, 15) ([93a25e7](https://github.com/brreg/linkml-datamodellering-no/commit/93a25e79c2eacdfa5d7548d176370200efc79279))

## [4.3.0](https://github.com/brreg/linkml-datamodellering-no/compare/fint-arkiv-v4.2.0...fint-arkiv-v4.3.0) (2026-07-09)


### Features

* **mkdocs:** konfigurerbar lenke-tekst for offisiell referanse og description.md for alle modellar ([97dacce](https://github.com/brreg/linkml-datamodellering-no/commit/97dacce159f02236196c9daa686e375e503f15ef))

## [4.2.0](https://github.com/brreg/linkml-datamodellering-no/compare/fint-arkiv-v4.1.2...fint-arkiv-v4.2.0) (2026-07-04)


### Features

* **validate-capture:** parallelliser validering av alle skjema ([6267587](https://github.com/brreg/linkml-datamodellering-no/commit/6267587223de8b03fe459c0d6458c492aa5dd279))

## [4.1.2](https://github.com/brreg/linkml-datamodellering-no/compare/fint-arkiv-v4.1.1...fint-arkiv-v4.1.2) (2026-07-04)


### Bug Fixes

* **release:** synk schema-versjon med release-nummer automatisk ([6dbb358](https://github.com/brreg/linkml-datamodellering-no/commit/6dbb358b6929bfbd73ef9c5fde8f1a0c24cb56e2))

## [4.1.1](https://github.com/brreg/linkml-datamodellering-no/compare/fint-arkiv-v4.1.0...fint-arkiv-v4.1.1) (2026-07-04)


### Bug Fixes

* **ap-no:** fjern tvetydig type for lisens og hardkod generator-flagg ([c6514ca](https://github.com/brreg/linkml-datamodellering-no/commit/c6514ca76cfaa3c85753a3515b9481f726997a8f))

## [4.1.0](https://github.com/brreg/linkml-datamodellering-no/compare/fint-arkiv-v4.0.21...fint-arkiv-v4.1.0) (2026-07-03)


### Features

* **validering:** komplett valideringssystem med auto-detect og visuell rapportering ([20caed0](https://github.com/brreg/linkml-datamodellering-no/commit/20caed0d1764e27864f377fcaea212506f3a6fab))

## [4.0.21](https://github.com/brreg/linkml-datamodellering-no/compare/fint-arkiv-v4.0.20...fint-arkiv-v4.0.21) (2026-06-19)


### Bug Fixes

* **schemas,mcp-validator:** etterlevingsopprett mot Digdir felles modelleringsreglar (regel 6-11, 15) ([72aaaf2](https://github.com/brreg/linkml-datamodellering-no/commit/72aaaf2990834bf37a84cd514798141559e1ffef))
