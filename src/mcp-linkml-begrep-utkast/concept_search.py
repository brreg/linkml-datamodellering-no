"""
Søk i Felles Begrepskatalog (nasjonal konseptkatalog på data.norge.no) etter
eit eksisterande, registrert begrep som matchar eit klassenamn/omgrep.

Brukast til å finne kandidatar for annotations.begrepsidentifikator FØR ein
vurderer å registrere eit nytt begrep — sjå
specs/backlog/plan-konsekvent-begrepsidentifikator.md (Fase 1).

To offentlege, uautentiserte lese-endepunkt vert brukte:
- SPARQL (https://sparql.fellesdatakatalog.digdir.no) for eksakt oppslag på
  skos:prefLabel/skos:altLabel. Verifisert vesentleg meir treffsikkert enn
  fritekstsøket for å stadfeste/avkrefte eit presist namnetreff (sjå
  "Prioritet 1 utført"-avsnittet i planen over — fritekstsøket rangerte
  IKKJE sjølve "kommune"-konseptet blant dei 10 øvste treffa for query
  "kommune", sjølv om konseptet finst).
- Fritekstsøk (https://search.api.fellesdatakatalog.digdir.no/search/concepts)
  som fallback når eksakt oppslag ikkje gir treff — breiare, mindre presise
  kandidatar for menneskeleg vurdering.

Ingen eksterne avhengigheiter utover stdlib urllib (same mønster som
src/assets/scripts/makefile/check-iri-resolution.py).

**Vel ALDRI ein kandidat automatisk** — semantisk presisjon i eit nasjonalt
register krev menneskeleg stadfesting, same prinsipp som vart brukt i
class_uri-gjennomgangen (specs/done/undersokelse-class-uri-kryssreferansar.md).
"""

import json
import urllib.error
import urllib.parse
import urllib.request

SPARQL_ENDPOINT = "https://sparql.fellesdatakatalog.digdir.no"
SEARCH_ENDPOINT = "https://search.api.fellesdatakatalog.digdir.no/search/concepts"
TIMEOUT = 10
USER_AGENT = "linkml-datamodellering-no-begrep-sok/1.0"

NETWORK_ERRORS = (urllib.error.URLError, TimeoutError, OSError, ValueError)


def _sparql_query(query: str) -> list:
    url = SPARQL_ENDPOINT + "?" + urllib.parse.urlencode({"query": query})
    req = urllib.request.Request(
        url,
        headers={"Accept": "application/sparql-results+json", "User-Agent": USER_AGENT},
    )
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        data = json.load(resp)
    return data.get("results", {}).get("bindings", [])


def _fetch_definition(uri: str) -> str:
    """Hent norsk (eller språknøytral) definisjonstekst for eit konsept-URI, om det finst."""
    uid = uri.rsplit("/", 1)[-1]
    query = (
        "PREFIX euvoc: <http://publications.europa.eu/ontology/euvoc#>\n"
        "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n"
        "SELECT ?def WHERE {\n"
        "  ?s euvoc:xlDefinition ?bn .\n"
        "  ?bn rdf:value ?def .\n"
        f'  FILTER(CONTAINS(STR(?s), "{uid}"))\n'
        '  FILTER(LANG(?def) = "" || LANG(?def) = "nb" || LANG(?def) = "nn")\n'
        "} LIMIT 1"
    )
    try:
        bindings = _sparql_query(query)
    except NETWORK_ERRORS:
        return None
    return bindings[0]["def"]["value"] if bindings else None


def _exact_label_match(term: str) -> list:
    term_escaped = term.lower().replace('"', '\\"').replace("\\", "\\\\")
    query = (
        "PREFIX skos: <http://www.w3.org/2004/02/skos/core#>\n"
        "SELECT DISTINCT ?s ?label WHERE {\n"
        "  { ?s skos:prefLabel ?label } UNION { ?s skos:altLabel ?label }\n"
        '  FILTER(LANG(?label) = "nb")\n'
        f'  FILTER(LCASE(STR(?label)) = "{term_escaped}")\n'
        # Avgrens til Felles Begrepskatalog sine faktiske konsept-URI-ar.
        # Den harvesta grafen inneheld òg andre ressursar med skos:prefLabel
        # (LOS-ord under psi.norge.no/los/ord/, "subjects"-taggar under
        # catalog-admin-service.fellesdatakatalog.digdir.no) som IKKJE er
        # gyldige begrepsidentifikator-mål.
        '  FILTER(STRSTARTS(STR(?s), "https://concept-catalog.fellesdatakatalog.digdir.no/"))\n'
        "} LIMIT 10"
    )
    bindings = _sparql_query(query)
    results = []
    seen = set()
    for b in bindings:
        uri = b["s"]["value"]
        if uri in seen:
            continue
        seen.add(uri)
        results.append(
            {
                "uri": uri,
                "term": b["label"]["value"],
                "definisjon": _fetch_definition(uri),
                "match_type": "eksakt",
            }
        )
    return results


def _first_lang(d: dict):
    if not d:
        return None
    return d.get("nb") or d.get("nn") or d.get("no") or next(iter(d.values()), None)


def _free_text_search(term: str, size: int) -> list:
    body = json.dumps({"query": term, "pagination": {"size": size, "page": 1}}).encode("utf-8")
    req = urllib.request.Request(
        SEARCH_ENDPOINT,
        data=body,
        headers={"Content-Type": "application/json", "User-Agent": USER_AGENT},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        data = json.load(resp)
    results = []
    for hit in data.get("hits", []):
        results.append(
            {
                "uri": hit.get("uri"),
                "term": _first_lang(hit.get("title")),
                "definisjon": _first_lang(hit.get("description")),
                "organisasjon": (hit.get("organization") or {}).get("name"),
                "match_type": "fritekst",
            }
        )
    return results


def sok_begrep(term: str, maks_treff: int = 5) -> dict:
    """Søk etter eit begrep i Felles Begrepskatalog.

    Prøver først eksakt namnetreff (skos:prefLabel/altLabel). Fell tilbake
    til breiare fritekstsøk berre dersom ingen eksakt treff finst.
    """
    if not term or not term.strip():
        return {"feil": "term er påkravd"}
    term = term.strip()
    maks_treff = maks_treff or 5

    eksakt_feil = None
    try:
        eksakte = _exact_label_match(term)
    except NETWORK_ERRORS as e:
        eksakte = []
        eksakt_feil = str(e)

    if eksakte:
        return {
            "term_sokt": term,
            "metode": "eksakt",
            "kandidatar": eksakte[:maks_treff],
            "merknad": (
                "Presist namnetreff funne (skos:prefLabel/altLabel). Stadfest "
                "likevel definisjonen mot klassen si eiga skildring før bruk "
                "som begrepsidentifikator — vel aldri automatisk."
            ),
        }

    try:
        fritekst = _free_text_search(term, size=maks_treff)
    except NETWORK_ERRORS as e:
        feilmelding = f"Fritekstsøk feila: {e}"
        if eksakt_feil:
            feilmelding += f" (eksakt-søk feila òg: {eksakt_feil})"
        return {"term_sokt": term, "metode": "ingen", "kandidatar": [], "feil": feilmelding}

    return {
        "term_sokt": term,
        "metode": "fritekst",
        "kandidatar": fritekst,
        "merknad": (
            "Ingen eksakt namnetreff funne — dette er breiare, mindre presise "
            "kandidatar frå fritekstsøk. Vurder nøye mot klassen si eiga "
            "skildring, eller registrer nytt begrep dersom ingen passar "
            "(krev ID-porten-innlogging hjå organisasjonen si samling — "
            "sjå plan-konsekvent-begrepsidentifikator.md Fase 4)."
        ),
    }
