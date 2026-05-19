# ./src/mcp-linkml-validator

Dette er en mcp server for å validere LinkML skjema mot utvalgt valideringspolicy.

Policies:
- `bronze`: sjekker om skjemaet tilfredsstiller bronse-nivå i en medaljongarkitektur
- `silver`: sjekker om skjemaet tilfredsstiller sølv-nivå i en medaljongarkitektur    
- `gold`: sjekker om skjemaet tilfredsstiller gull-nivå i en medaljongarkitektur

## eksempel på bruk

`make mcp-validate SCHEMA=<sti-til-skjema> [POLICY=gold]`