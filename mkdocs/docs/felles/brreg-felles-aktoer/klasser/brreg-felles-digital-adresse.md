# brreg-felles-digital-adresse 

Gjenbrukbare digitale adresseklassar utleia frå Brønnøysundregistrene (BR) sin interne BRReferansemodell_v3 (MagicDraw/XMI), pakken "Adresse" (DigitalAdresse-hierarkiet). Sjå specs/done/felles-typar-enhetsregisteret-fra-br-katalogar.md for bakgrunn, metode og avklaringane denne modellen byggjer på.
BR sin eigen `Nettadresse`-undertype "Aksesspunkt" er medvite utelaten her: feltet `aksesspunktoperatoer` peikar til `Virksomhet` (definert i brreg-felles-aktoer, som importerer denne modellen) og ville gjort importgrafen sirkulær. Sjå nemnde spec § Funn 4.

URI: https://data.norge.no/felles/brreg-felles-digital-adresse