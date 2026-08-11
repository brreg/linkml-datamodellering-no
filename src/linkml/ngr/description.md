NGR-domenet (Nasjonale grunndata) inneheld fire fullstendige domenemodellar for sentrale norske grunndataregister: `ngr-adresse` (Adresseregisteret), `ngr-eiendom` (Matrikkelen), `ngr-person` (Folkeregisteret) og `ngr-virksomhet` (Enhetsregisteret). Desse svarar til dei fire registera som per [Rammeverk for Nasjonale grunndata](https://www.digdir.no/datadeling/nasjonale-grunndata/7575) har status som nasjonale grunndata i Noreg.

Modellane brukar `_ref`-suffiks på referanse-slots som held ein URI til ein annan ressurs (t.d. `kommune_ref`, `adressenavn_ref`) — sjå CONVENTIONS.md.

**Typisk brukar:** Offentlege verksemder som arbeider med grunndata frå Kartverket, Skatteetaten eller Brønnøysundregistrene, og utviklarar som implementerer API-ar baserte på Nasjonale grunndata.
