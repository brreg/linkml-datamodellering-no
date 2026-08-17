# Changelog

## [1.1.0](https://github.com/brreg/linkml-datamodellering-no/compare/skatteetaten-modellkatalog-v1.0.0...skatteetaten-modellkatalog-v1.1.0) (2026-08-17)


### Features

* **generatorar:** legg til gen-graphql for GraphQL SDL-generering ([cb0a7bd](https://github.com/brreg/linkml-datamodellering-no/commit/cb0a7bd4c220dbee889df488bed0eaeb25960ce4))


### Bug Fixes

* **ap-no,modellkatalog:** fullfør manglande badge-metadata (utgiver, lisens, endringsdato, utgivelsesdato) ([d9a700c](https://github.com/brreg/linkml-datamodellering-no/commit/d9a700ca64c8b7cd690832e2e5b8bc9e3ed6c4c6))
* **build-manifest:** legg til manglande generator-flagg i 11 build.yaml ([916d9df](https://github.com/brreg/linkml-datamodellering-no/commit/916d9df3205e7b1cb322eb8bdc8a59ce4d692a5b))
* **ci:** ekskluder begrepssamling-katalogar og legg til validation_policy i modellkatalog ([fe7dce0](https://github.com/brreg/linkml-datamodellering-no/commit/fe7dce05a14fcf7736372248e1d551188415624f))
* **fint,codeowners:** fjern owlgen-tvitydigheit i fint og CODEOWNERS-gap ([8319f57](https://github.com/brreg/linkml-datamodellering-no/commit/8319f57a65884a172e877c0b0a260efbbd0f9054))
* **make:** rett stdin-konsumering i validate-bronze (BUG-10) ([91795ac](https://github.com/brreg/linkml-datamodellering-no/commit/91795ace2400341ba3ef052e4bb84cefe6e38215))
* **mkdocs:** aktiver plantuml-diagram for FINT, Begrepskatalog og Modellkatalog ([31881d6](https://github.com/brreg/linkml-datamodellering-no/commit/31881d6bdbb1660c29b9baaa4b14f7839e5f3364))


### Performance Improvements

* **mcp-linkml-validator:** parallelliser validate-examples, regenerer valideringsloggar ([fc67279](https://github.com/brreg/linkml-datamodellering-no/commit/fc672798d9b85870590a1bf7ea33fbca4181bf51))
