# Changelog

## [1.6.0](https://github.com/brreg/linkml-datamodellering-no/compare/cpsv-ap-no-v1.5.0...cpsv-ap-no-v1.6.0) (2026-07-10)


### Features

* **ap-no:** publiser common-ap-no i nav-meny og omdøp katalog ([9653abf](https://github.com/brreg/linkml-datamodellering-no/commit/9653abf7a46a7714b216e3d0f6e3ebb97efeabc9))
* **ci:** legg til XSD-generering via avrotize-pipeline ([22b585b](https://github.com/brreg/linkml-datamodellering-no/commit/22b585b91e357a8280ad2c9c914407e8a0b1057a))
* legg til flag for publisering av kvar enkelt modell i manifest.yaml som er omdøpt fra generate.yaml. Flytter data og examples katalogane inn under src/linkml/domene slik at alle relaterte filer ligg i samme struktur. ([a4cccbd](https://github.com/brreg/linkml-datamodellering-no/commit/a4cccbdfb8e327d0a9bb1874b34ec21bd9c374d0))
* legg til OpenAPI 3.1 og AsyncAPI 3.0-generering ([7be7ef8](https://github.com/brreg/linkml-datamodellering-no/commit/7be7ef8ad6e4cda9fb2a08bbc336e1c782d5d794))
* **mkdocs:** konfigurerbar lenke-tekst for offisiell referanse ([1d493cd](https://github.com/brreg/linkml-datamodellering-no/commit/1d493cdafb5c3991b3270b901503b7df70717f6c))
* **mkdocs:** konfigurerbar lenke-tekst for offisiell referanse og description.md for alle modellar ([20d8bf8](https://github.com/brreg/linkml-datamodellering-no/commit/20d8bf8c0e3d5ed31c608ece6bf5d64d7802b9af))
* **mkdocs:** konfigurerbare seksjons-kjelder i index.md ([122c704](https://github.com/brreg/linkml-datamodellering-no/commit/122c7047e78c3a54952d9c91910d62f53da682a3))
* **modellmanifest:** autogenerer &lt;modell&gt;-manifest.yaml i make domain-* ([97fd24d](https://github.com/brreg/linkml-datamodellering-no/commit/97fd24de6b851e1807aa43d814ef77d58ac74b2d))
* **validate-capture:** parallelliser validering av alle skjema ([7d9a0a2](https://github.com/brreg/linkml-datamodellering-no/commit/7d9a0a28797a918d887b6ff22303ac6d56204655))
* **validering:** komplett valideringssystem med auto-detect og visuell rapportering ([f0607bc](https://github.com/brreg/linkml-datamodellering-no/commit/f0607bc510640fa8c85b989b995e0162385eb06e))


### Bug Fixes

* **ap-no:** fjern tvetydig type for lisens og hardkod generator-flagg ([e7029d7](https://github.com/brreg/linkml-datamodellering-no/commit/e7029d735d66bc9a0ae4b1918dd7c431b6a0c7ef))
* **ap-no:** løys URI-konflikt i xkos-ap-no og endre merge-imports-namn ([834abab](https://github.com/brreg/linkml-datamodellering-no/commit/834abab9976890216fca522326429edf7f9b4933))
* **cpsv-ap-no:** fjern duplikat lisens-slot som kolliderer med common-ap-no ([34a012e](https://github.com/brreg/linkml-datamodellering-no/commit/34a012e4a51a57cee06f217446aae6b8a5d520ca))
* normaliser version-felt til tre-delt semver for release-please-kompatibilitet ([abd967b](https://github.com/brreg/linkml-datamodellering-no/commit/abd967be7c48043154a9c06c14d98c59e7154f36))
* **release:** synk schema-versjon med release-nummer automatisk ([1d20298](https://github.com/brreg/linkml-datamodellering-no/commit/1d20298b932da0e876795152aab61baf99611daf))
* **schemas,mcp-validator:** etterlevingsopprett mot Digdir felles modelleringsreglar (regel 6-11, 15) ([93a25e7](https://github.com/brreg/linkml-datamodellering-no/commit/93a25e79c2eacdfa5d7548d176370200efc79279))

## [1.5.0](https://github.com/brreg/linkml-datamodellering-no/compare/cpsv-ap-no-v1.4.0...cpsv-ap-no-v1.5.0) (2026-07-09)


### Features

* **modellmanifest:** autogenerer &lt;modell&gt;-manifest.yaml i make domain-* ([321b8a8](https://github.com/brreg/linkml-datamodellering-no/commit/321b8a8ea36b37531bc9512f5c90407a92389b8f))

## [1.4.0](https://github.com/brreg/linkml-datamodellering-no/compare/cpsv-ap-no-v1.3.0...cpsv-ap-no-v1.4.0) (2026-07-09)


### Features

* **ap-no:** publiser common-ap-no i nav-meny og omdøp katalog ([35da103](https://github.com/brreg/linkml-datamodellering-no/commit/35da103f75e856685bf01e255b732241792964fa))
* **mkdocs:** konfigurerbar lenke-tekst for offisiell referanse ([a41c35a](https://github.com/brreg/linkml-datamodellering-no/commit/a41c35a660445f0180b3cdc17175386b1bd730a9))
* **mkdocs:** konfigurerbar lenke-tekst for offisiell referanse og description.md for alle modellar ([97dacce](https://github.com/brreg/linkml-datamodellering-no/commit/97dacce159f02236196c9daa686e375e503f15ef))

## [1.3.0](https://github.com/brreg/linkml-datamodellering-no/compare/cpsv-ap-no-v1.2.2...cpsv-ap-no-v1.3.0) (2026-07-06)


### Features

* **mkdocs:** konfigurerbare seksjons-kjelder i index.md ([94c2efb](https://github.com/brreg/linkml-datamodellering-no/commit/94c2efb8c90571a03efa5108a869e5204544bcbf))

## [1.2.2](https://github.com/brreg/linkml-datamodellering-no/compare/cpsv-ap-no-v1.2.1...cpsv-ap-no-v1.2.2) (2026-07-05)


### Bug Fixes

* **ap-no:** løys URI-konflikt i xkos-ap-no og endre merge-imports-namn ([55f73ab](https://github.com/brreg/linkml-datamodellering-no/commit/55f73ab0d0203e510c9b3d2c9a2ca33b5d7ef633))

## [1.2.1](https://github.com/brreg/linkml-datamodellering-no/compare/cpsv-ap-no-v1.2.0...cpsv-ap-no-v1.2.1) (2026-07-04)


### Bug Fixes

* **cpsv-ap-no:** fjern duplikat lisens-slot som kolliderer med common-ap-no ([52889d1](https://github.com/brreg/linkml-datamodellering-no/commit/52889d12d5646d6dc56703b015c7958e0603b0b4))

## [1.2.0](https://github.com/brreg/linkml-datamodellering-no/compare/cpsv-ap-no-v1.1.2...cpsv-ap-no-v1.2.0) (2026-07-04)


### Features

* **validate-capture:** parallelliser validering av alle skjema ([6267587](https://github.com/brreg/linkml-datamodellering-no/commit/6267587223de8b03fe459c0d6458c492aa5dd279))

## [1.1.2](https://github.com/brreg/linkml-datamodellering-no/compare/cpsv-ap-no-v1.1.1...cpsv-ap-no-v1.1.2) (2026-07-04)


### Bug Fixes

* **release:** synk schema-versjon med release-nummer automatisk ([6dbb358](https://github.com/brreg/linkml-datamodellering-no/commit/6dbb358b6929bfbd73ef9c5fde8f1a0c24cb56e2))

## [1.1.1](https://github.com/brreg/linkml-datamodellering-no/compare/cpsv-ap-no-v1.1.0...cpsv-ap-no-v1.1.1) (2026-07-04)


### Bug Fixes

* **ap-no:** fjern tvetydig type for lisens og hardkod generator-flagg ([c6514ca](https://github.com/brreg/linkml-datamodellering-no/commit/c6514ca76cfaa3c85753a3515b9481f726997a8f))

## [1.1.0](https://github.com/brreg/linkml-datamodellering-no/compare/cpsv-ap-no-v1.0.1...cpsv-ap-no-v1.1.0) (2026-07-03)


### Features

* **validering:** komplett valideringssystem med auto-detect og visuell rapportering ([20caed0](https://github.com/brreg/linkml-datamodellering-no/commit/20caed0d1764e27864f377fcaea212506f3a6fab))

## [1.0.1](https://github.com/brreg/linkml-datamodellering-no/compare/cpsv-ap-no-v1.0.0...cpsv-ap-no-v1.0.1) (2026-06-19)


### Bug Fixes

* **schemas,mcp-validator:** etterlevingsopprett mot Digdir felles modelleringsreglar (regel 6-11, 15) ([72aaaf2](https://github.com/brreg/linkml-datamodellering-no/commit/72aaaf2990834bf37a84cd514798141559e1ffef))
