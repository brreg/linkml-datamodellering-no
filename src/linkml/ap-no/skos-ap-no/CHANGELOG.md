# Changelog

## [2.11.0](https://github.com/brreg/linkml-datamodellering-no/compare/skos-ap-no-v2.10.0...skos-ap-no-v2.11.0) (2026-07-10)


### Features

* **ap-no,begrepskatalog,modellkatalog:** legg til DQV-kvalitetsmålingar (kvantifiserbar kvalitet) ([9009b1e](https://github.com/brreg/linkml-datamodellering-no/commit/9009b1e63660f55fce18c1a9bf4dda0757a27d5e))
* **ap-no:** publiser common-ap-no i nav-meny og omdøp katalog ([9653abf](https://github.com/brreg/linkml-datamodellering-no/commit/9653abf7a46a7714b216e3d0f6e3ebb97efeabc9))
* **ci:** legg til XSD-generering via avrotize-pipeline ([22b585b](https://github.com/brreg/linkml-datamodellering-no/commit/22b585b91e357a8280ad2c9c914407e8a0b1057a))
* legg til flag for publisering av kvar enkelt modell i manifest.yaml som er omdøpt fra generate.yaml. Flytter data og examples katalogane inn under src/linkml/domene slik at alle relaterte filer ligg i samme struktur. ([a4cccbd](https://github.com/brreg/linkml-datamodellering-no/commit/a4cccbdfb8e327d0a9bb1874b34ec21bd9c374d0))
* legg til OpenAPI 3.1 og AsyncAPI 3.0-generering ([7be7ef8](https://github.com/brreg/linkml-datamodellering-no/commit/7be7ef8ad6e4cda9fb2a08bbc336e1c782d5d794))
* **mkdocs:** konfigurerbar lenke-tekst for offisiell referanse ([1d493cd](https://github.com/brreg/linkml-datamodellering-no/commit/1d493cdafb5c3991b3270b901503b7df70717f6c))
* **mkdocs:** konfigurerbare seksjons-kjelder i index.md ([122c704](https://github.com/brreg/linkml-datamodellering-no/commit/122c7047e78c3a54952d9c91910d62f53da682a3))
* **modellmanifest:** autogenerer &lt;modell&gt;-manifest.yaml i make domain-* ([97fd24d](https://github.com/brreg/linkml-datamodellering-no/commit/97fd24de6b851e1807aa43d814ef77d58ac74b2d))
* **skos-ap-no:** implementer TL1-TL3 frå avvik-termlosen.md, flytt spec til done ([d48ab8f](https://github.com/brreg/linkml-datamodellering-no/commit/d48ab8fec4fe46fa6ba3baa233dc3c200785271a))
* **validate-capture:** parallelliser validering av alle skjema ([7d9a0a2](https://github.com/brreg/linkml-datamodellering-no/commit/7d9a0a28797a918d887b6ff22303ac6d56204655))
* **validering:** komplett valideringssystem med auto-detect og visuell rapportering ([f0607bc](https://github.com/brreg/linkml-datamodellering-no/commit/f0607bc510640fa8c85b989b995e0162385eb06e))


### Bug Fixes

* **ap-no,specs:** rett avvik mot Prinsipper for informasjonsmodellar ([ce4964b](https://github.com/brreg/linkml-datamodellering-no/commit/ce4964bc4d121438606489a41dae63ac1bea672b))
* **ap-no:** fjern tvetydig type for lisens og hardkod generator-flagg ([e7029d7](https://github.com/brreg/linkml-datamodellering-no/commit/e7029d735d66bc9a0ae4b1918dd7c431b6a0c7ef))
* normaliser version-felt til tre-delt semver for release-please-kompatibilitet ([abd967b](https://github.com/brreg/linkml-datamodellering-no/commit/abd967be7c48043154a9c06c14d98c59e7154f36))
* **release:** synk schema-versjon med release-nummer automatisk ([1d20298](https://github.com/brreg/linkml-datamodellering-no/commit/1d20298b932da0e876795152aab61baf99611daf))
* **schemas,mcp-validator:** etterlevingsopprett mot Digdir felles modelleringsreglar (regel 6-11, 15) ([93a25e7](https://github.com/brreg/linkml-datamodellering-no/commit/93a25e79c2eacdfa5d7548d176370200efc79279))
* **skos-ap-no:** juster subset og range-feil per SKOS-AP-NO-Begrep-standarden ([c7fd78b](https://github.com/brreg/linkml-datamodellering-no/commit/c7fd78b40d849cee74e9dcbdf227e0b0e7a60a91))

## [2.10.0](https://github.com/brreg/linkml-datamodellering-no/compare/skos-ap-no-v2.9.0...skos-ap-no-v2.10.0) (2026-07-10)


### Features

* **ap-no,begrepskatalog,modellkatalog:** legg til DQV-kvalitetsmålingar (kvantifiserbar kvalitet) ([6fb9bad](https://github.com/brreg/linkml-datamodellering-no/commit/6fb9badce3ca37ea38fb2a6a882cad466ba8eae8))
* **ap-no:** publiser common-ap-no i nav-meny og omdøp katalog ([35da103](https://github.com/brreg/linkml-datamodellering-no/commit/35da103f75e856685bf01e255b732241792964fa))
* **ci:** legg til XSD-generering via avrotize-pipeline ([4b7478a](https://github.com/brreg/linkml-datamodellering-no/commit/4b7478a340c100db4e4d7fb5f3178bf3f0e8b4af))
* legg til flag for publisering av kvar enkelt modell i manifest.yaml som er omdøpt fra generate.yaml. Flytter data og examples katalogane inn under src/linkml/domene slik at alle relaterte filer ligg i samme struktur. ([0e1e4fb](https://github.com/brreg/linkml-datamodellering-no/commit/0e1e4fbeff55711958f0b29c74af2944302d9896))
* legg til OpenAPI 3.1 og AsyncAPI 3.0-generering ([887fe84](https://github.com/brreg/linkml-datamodellering-no/commit/887fe84fa94e08bc3616cad9aa30887740c93253))
* **mkdocs:** konfigurerbar lenke-tekst for offisiell referanse ([a41c35a](https://github.com/brreg/linkml-datamodellering-no/commit/a41c35a660445f0180b3cdc17175386b1bd730a9))
* **mkdocs:** konfigurerbare seksjons-kjelder i index.md ([94c2efb](https://github.com/brreg/linkml-datamodellering-no/commit/94c2efb8c90571a03efa5108a869e5204544bcbf))
* **modellmanifest:** autogenerer &lt;modell&gt;-manifest.yaml i make domain-* ([321b8a8](https://github.com/brreg/linkml-datamodellering-no/commit/321b8a8ea36b37531bc9512f5c90407a92389b8f))
* **skos-ap-no:** implementer TL1-TL3 frå avvik-termlosen.md, flytt spec til done ([07419b2](https://github.com/brreg/linkml-datamodellering-no/commit/07419b287f47d79bb6c99e87c69ddfebf24368e5))
* **validate-capture:** parallelliser validering av alle skjema ([6267587](https://github.com/brreg/linkml-datamodellering-no/commit/6267587223de8b03fe459c0d6458c492aa5dd279))
* **validering:** komplett valideringssystem med auto-detect og visuell rapportering ([20caed0](https://github.com/brreg/linkml-datamodellering-no/commit/20caed0d1764e27864f377fcaea212506f3a6fab))


### Bug Fixes

* **ap-no,specs:** rett avvik mot Prinsipper for informasjonsmodellar ([f93510f](https://github.com/brreg/linkml-datamodellering-no/commit/f93510f32fd44ff09cd0567d6b744bc3e661eea5))
* **ap-no:** fjern tvetydig type for lisens og hardkod generator-flagg ([c6514ca](https://github.com/brreg/linkml-datamodellering-no/commit/c6514ca76cfaa3c85753a3515b9481f726997a8f))
* normaliser version-felt til tre-delt semver for release-please-kompatibilitet ([5af2108](https://github.com/brreg/linkml-datamodellering-no/commit/5af2108f3b7749fee1537950c4abf9eebf9a4eaa))
* **release:** synk schema-versjon med release-nummer automatisk ([6dbb358](https://github.com/brreg/linkml-datamodellering-no/commit/6dbb358b6929bfbd73ef9c5fde8f1a0c24cb56e2))
* **schemas,mcp-validator:** etterlevingsopprett mot Digdir felles modelleringsreglar (regel 6-11, 15) ([72aaaf2](https://github.com/brreg/linkml-datamodellering-no/commit/72aaaf2990834bf37a84cd514798141559e1ffef))
* **skos-ap-no:** juster subset og range-feil per SKOS-AP-NO-Begrep-standarden ([73751b5](https://github.com/brreg/linkml-datamodellering-no/commit/73751b5f102a7903d909541ba8b987ae89b8f129))

## [2.9.0](https://github.com/brreg/linkml-datamodellering-no/compare/skos-ap-no-v2.8.0...skos-ap-no-v2.9.0) (2026-07-10)


### Features

* **ap-no,begrepskatalog,modellkatalog:** legg til DQV-kvalitetsmålingar (kvantifiserbar kvalitet) ([6fb9bad](https://github.com/brreg/linkml-datamodellering-no/commit/6fb9badce3ca37ea38fb2a6a882cad466ba8eae8))
* **ap-no:** publiser common-ap-no i nav-meny og omdøp katalog ([35da103](https://github.com/brreg/linkml-datamodellering-no/commit/35da103f75e856685bf01e255b732241792964fa))
* **ci:** legg til XSD-generering via avrotize-pipeline ([4b7478a](https://github.com/brreg/linkml-datamodellering-no/commit/4b7478a340c100db4e4d7fb5f3178bf3f0e8b4af))
* legg til flag for publisering av kvar enkelt modell i manifest.yaml som er omdøpt fra generate.yaml. Flytter data og examples katalogane inn under src/linkml/domene slik at alle relaterte filer ligg i samme struktur. ([0e1e4fb](https://github.com/brreg/linkml-datamodellering-no/commit/0e1e4fbeff55711958f0b29c74af2944302d9896))
* legg til OpenAPI 3.1 og AsyncAPI 3.0-generering ([887fe84](https://github.com/brreg/linkml-datamodellering-no/commit/887fe84fa94e08bc3616cad9aa30887740c93253))
* **mkdocs:** konfigurerbar lenke-tekst for offisiell referanse ([a41c35a](https://github.com/brreg/linkml-datamodellering-no/commit/a41c35a660445f0180b3cdc17175386b1bd730a9))
* **mkdocs:** konfigurerbare seksjons-kjelder i index.md ([94c2efb](https://github.com/brreg/linkml-datamodellering-no/commit/94c2efb8c90571a03efa5108a869e5204544bcbf))
* **modellmanifest:** autogenerer &lt;modell&gt;-manifest.yaml i make domain-* ([321b8a8](https://github.com/brreg/linkml-datamodellering-no/commit/321b8a8ea36b37531bc9512f5c90407a92389b8f))
* **skos-ap-no:** implementer TL1-TL3 frå avvik-termlosen.md, flytt spec til done ([07419b2](https://github.com/brreg/linkml-datamodellering-no/commit/07419b287f47d79bb6c99e87c69ddfebf24368e5))
* **validate-capture:** parallelliser validering av alle skjema ([6267587](https://github.com/brreg/linkml-datamodellering-no/commit/6267587223de8b03fe459c0d6458c492aa5dd279))
* **validering:** komplett valideringssystem med auto-detect og visuell rapportering ([20caed0](https://github.com/brreg/linkml-datamodellering-no/commit/20caed0d1764e27864f377fcaea212506f3a6fab))


### Bug Fixes

* **ap-no,specs:** rett avvik mot Prinsipper for informasjonsmodellar ([f93510f](https://github.com/brreg/linkml-datamodellering-no/commit/f93510f32fd44ff09cd0567d6b744bc3e661eea5))
* **ap-no:** fjern tvetydig type for lisens og hardkod generator-flagg ([c6514ca](https://github.com/brreg/linkml-datamodellering-no/commit/c6514ca76cfaa3c85753a3515b9481f726997a8f))
* normaliser version-felt til tre-delt semver for release-please-kompatibilitet ([5af2108](https://github.com/brreg/linkml-datamodellering-no/commit/5af2108f3b7749fee1537950c4abf9eebf9a4eaa))
* **release:** synk schema-versjon med release-nummer automatisk ([6dbb358](https://github.com/brreg/linkml-datamodellering-no/commit/6dbb358b6929bfbd73ef9c5fde8f1a0c24cb56e2))
* **schemas,mcp-validator:** etterlevingsopprett mot Digdir felles modelleringsreglar (regel 6-11, 15) ([72aaaf2](https://github.com/brreg/linkml-datamodellering-no/commit/72aaaf2990834bf37a84cd514798141559e1ffef))
* **skos-ap-no:** juster subset og range-feil per SKOS-AP-NO-Begrep-standarden ([73751b5](https://github.com/brreg/linkml-datamodellering-no/commit/73751b5f102a7903d909541ba8b987ae89b8f129))

## [2.8.0](https://github.com/brreg/linkml-datamodellering-no/compare/skos-ap-no-v2.7.0...skos-ap-no-v2.8.0) (2026-07-09)


### Features

* **ap-no,begrepskatalog,modellkatalog:** legg til DQV-kvalitetsmålingar (kvantifiserbar kvalitet) ([6fb9bad](https://github.com/brreg/linkml-datamodellering-no/commit/6fb9badce3ca37ea38fb2a6a882cad466ba8eae8))
* **ap-no:** publiser common-ap-no i nav-meny og omdøp katalog ([35da103](https://github.com/brreg/linkml-datamodellering-no/commit/35da103f75e856685bf01e255b732241792964fa))
* **ci:** legg til XSD-generering via avrotize-pipeline ([4b7478a](https://github.com/brreg/linkml-datamodellering-no/commit/4b7478a340c100db4e4d7fb5f3178bf3f0e8b4af))
* legg til flag for publisering av kvar enkelt modell i manifest.yaml som er omdøpt fra generate.yaml. Flytter data og examples katalogane inn under src/linkml/domene slik at alle relaterte filer ligg i samme struktur. ([0e1e4fb](https://github.com/brreg/linkml-datamodellering-no/commit/0e1e4fbeff55711958f0b29c74af2944302d9896))
* legg til OpenAPI 3.1 og AsyncAPI 3.0-generering ([887fe84](https://github.com/brreg/linkml-datamodellering-no/commit/887fe84fa94e08bc3616cad9aa30887740c93253))
* **mkdocs:** konfigurerbar lenke-tekst for offisiell referanse ([a41c35a](https://github.com/brreg/linkml-datamodellering-no/commit/a41c35a660445f0180b3cdc17175386b1bd730a9))
* **mkdocs:** konfigurerbare seksjons-kjelder i index.md ([94c2efb](https://github.com/brreg/linkml-datamodellering-no/commit/94c2efb8c90571a03efa5108a869e5204544bcbf))
* **modellmanifest:** autogenerer &lt;modell&gt;-manifest.yaml i make domain-* ([321b8a8](https://github.com/brreg/linkml-datamodellering-no/commit/321b8a8ea36b37531bc9512f5c90407a92389b8f))
* **skos-ap-no:** implementer TL1-TL3 frå avvik-termlosen.md, flytt spec til done ([07419b2](https://github.com/brreg/linkml-datamodellering-no/commit/07419b287f47d79bb6c99e87c69ddfebf24368e5))
* **validate-capture:** parallelliser validering av alle skjema ([6267587](https://github.com/brreg/linkml-datamodellering-no/commit/6267587223de8b03fe459c0d6458c492aa5dd279))
* **validering:** komplett valideringssystem med auto-detect og visuell rapportering ([20caed0](https://github.com/brreg/linkml-datamodellering-no/commit/20caed0d1764e27864f377fcaea212506f3a6fab))


### Bug Fixes

* **ap-no,specs:** rett avvik mot Prinsipper for informasjonsmodellar ([f93510f](https://github.com/brreg/linkml-datamodellering-no/commit/f93510f32fd44ff09cd0567d6b744bc3e661eea5))
* **ap-no:** fjern tvetydig type for lisens og hardkod generator-flagg ([c6514ca](https://github.com/brreg/linkml-datamodellering-no/commit/c6514ca76cfaa3c85753a3515b9481f726997a8f))
* normaliser version-felt til tre-delt semver for release-please-kompatibilitet ([5af2108](https://github.com/brreg/linkml-datamodellering-no/commit/5af2108f3b7749fee1537950c4abf9eebf9a4eaa))
* **release:** synk schema-versjon med release-nummer automatisk ([6dbb358](https://github.com/brreg/linkml-datamodellering-no/commit/6dbb358b6929bfbd73ef9c5fde8f1a0c24cb56e2))
* **schemas,mcp-validator:** etterlevingsopprett mot Digdir felles modelleringsreglar (regel 6-11, 15) ([72aaaf2](https://github.com/brreg/linkml-datamodellering-no/commit/72aaaf2990834bf37a84cd514798141559e1ffef))
* **skos-ap-no:** juster subset og range-feil per SKOS-AP-NO-Begrep-standarden ([73751b5](https://github.com/brreg/linkml-datamodellering-no/commit/73751b5f102a7903d909541ba8b987ae89b8f129))

## [2.7.0](https://github.com/brreg/linkml-datamodellering-no/compare/skos-ap-no-v2.6.0...skos-ap-no-v2.7.0) (2026-07-09)


### Features

* **modellmanifest:** autogenerer &lt;modell&gt;-manifest.yaml i make domain-* ([321b8a8](https://github.com/brreg/linkml-datamodellering-no/commit/321b8a8ea36b37531bc9512f5c90407a92389b8f))

## [2.6.0](https://github.com/brreg/linkml-datamodellering-no/compare/skos-ap-no-v2.5.0...skos-ap-no-v2.6.0) (2026-07-09)


### Features

* **ap-no:** publiser common-ap-no i nav-meny og omdøp katalog ([35da103](https://github.com/brreg/linkml-datamodellering-no/commit/35da103f75e856685bf01e255b732241792964fa))
* **mkdocs:** konfigurerbar lenke-tekst for offisiell referanse ([a41c35a](https://github.com/brreg/linkml-datamodellering-no/commit/a41c35a660445f0180b3cdc17175386b1bd730a9))

## [2.5.0](https://github.com/brreg/linkml-datamodellering-no/compare/skos-ap-no-v2.4.0...skos-ap-no-v2.5.0) (2026-07-06)


### Features

* **mkdocs:** konfigurerbare seksjons-kjelder i index.md ([94c2efb](https://github.com/brreg/linkml-datamodellering-no/commit/94c2efb8c90571a03efa5108a869e5204544bcbf))

## [2.4.0](https://github.com/brreg/linkml-datamodellering-no/compare/skos-ap-no-v2.3.2...skos-ap-no-v2.4.0) (2026-07-04)


### Features

* **validate-capture:** parallelliser validering av alle skjema ([6267587](https://github.com/brreg/linkml-datamodellering-no/commit/6267587223de8b03fe459c0d6458c492aa5dd279))

## [2.3.2](https://github.com/brreg/linkml-datamodellering-no/compare/skos-ap-no-v2.3.1...skos-ap-no-v2.3.2) (2026-07-04)


### Bug Fixes

* **release:** synk schema-versjon med release-nummer automatisk ([6dbb358](https://github.com/brreg/linkml-datamodellering-no/commit/6dbb358b6929bfbd73ef9c5fde8f1a0c24cb56e2))

## [2.3.1](https://github.com/brreg/linkml-datamodellering-no/compare/skos-ap-no-v2.3.0...skos-ap-no-v2.3.1) (2026-07-04)


### Bug Fixes

* **ap-no:** fjern tvetydig type for lisens og hardkod generator-flagg ([c6514ca](https://github.com/brreg/linkml-datamodellering-no/commit/c6514ca76cfaa3c85753a3515b9481f726997a8f))

## [2.3.0](https://github.com/brreg/linkml-datamodellering-no/compare/skos-ap-no-v2.2.0...skos-ap-no-v2.3.0) (2026-07-03)


### Features

* **validering:** komplett valideringssystem med auto-detect og visuell rapportering ([20caed0](https://github.com/brreg/linkml-datamodellering-no/commit/20caed0d1764e27864f377fcaea212506f3a6fab))

## [2.2.0](https://github.com/brreg/linkml-datamodellering-no/compare/skos-ap-no-v2.1.0...skos-ap-no-v2.2.0) (2026-07-01)


### Features

* **ap-no,begrepskatalog,modellkatalog:** legg til DQV-kvalitetsmålingar (kvantifiserbar kvalitet) ([6fb9bad](https://github.com/brreg/linkml-datamodellering-no/commit/6fb9badce3ca37ea38fb2a6a882cad466ba8eae8))

## [2.1.0](https://github.com/brreg/linkml-datamodellering-no/compare/skos-ap-no-v2.0.2...skos-ap-no-v2.1.0) (2026-06-20)


### Features

* **skos-ap-no:** implementer TL1-TL3 frå avvik-termlosen.md, flytt spec til done ([07419b2](https://github.com/brreg/linkml-datamodellering-no/commit/07419b287f47d79bb6c99e87c69ddfebf24368e5))


### Bug Fixes

* **skos-ap-no:** juster subset og range-feil per SKOS-AP-NO-Begrep-standarden ([73751b5](https://github.com/brreg/linkml-datamodellering-no/commit/73751b5f102a7903d909541ba8b987ae89b8f129))

## [2.0.2](https://github.com/brreg/linkml-datamodellering-no/compare/skos-ap-no-v2.0.1...skos-ap-no-v2.0.2) (2026-06-20)


### Bug Fixes

* **ap-no,specs:** rett avvik mot Prinsipper for informasjonsmodellar ([f93510f](https://github.com/brreg/linkml-datamodellering-no/commit/f93510f32fd44ff09cd0567d6b744bc3e661eea5))

## [2.0.1](https://github.com/brreg/linkml-datamodellering-no/compare/skos-ap-no-v2.0.0...skos-ap-no-v2.0.1) (2026-06-19)


### Bug Fixes

* **schemas,mcp-validator:** etterlevingsopprett mot Digdir felles modelleringsreglar (regel 6-11, 15) ([72aaaf2](https://github.com/brreg/linkml-datamodellering-no/commit/72aaaf2990834bf37a84cd514798141559e1ffef))
