"""Logikk for å byggje YAML-blokkar for SKOS-AP-NO Begrep frå strukturerte parametrar."""

import yaml
from pathlib import Path


_PROFILES_DIR = Path(__file__).parent / "profiles"

_KJELDE_BASE = "https://data.norge.no/vocabulary/relationship-with-source-type"

KJELDETYPAR = {
    "direct-from-source":  f"{_KJELDE_BASE}#direct-from-source",
    "self-composed":       f"{_KJELDE_BASE}#self-composed",
    "derived-from-source": f"{_KJELDE_BASE}#derived-from-source",
}


def load_profile(name: str) -> dict:
    """Lastar ein namngitt profil frå profiles/-katalogen."""
    path = _PROFILES_DIR / f"{name}.yaml"
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def _resolve(explicit: str, profile_key: str, profile: dict, required_name: str) -> str:
    """Returnerer eksplisitt verdi, profil-standard eller feiler."""
    if explicit:
        return explicit
    val = (profile.get("defaults") or {}).get(profile_key, "")
    if val:
        return val
    raise ValueError(f"Påkravd parameter '{required_name}' manglar og er ikkje satt i profilen.")


def opprett_begrep(
    profile: dict,
    slug: str,
    anbefalt_term_nb: str,
    definisjon_nb: str,
    fagomrade_uri: str,
    *,
    base_uri: str = "",
    kjelde_relasjon: str = "",
    utgjevar_uri: str = "",
    anbefalt_term_nn: str = "",
    anbefalt_term_en: str = "",
    definisjon_nn: str = "",
    definisjon_en: str = "",
    kontaktpunkt_uri: str = "",
    merknad: list | None = None,
    eksempel: list | None = None,
    sja_ogsa_omgrep: list | None = None,
) -> str:
    """Returnerer ein YAML-streng med BegrepContainer-innhald for eitt begrep."""
    merknad = merknad or []
    eksempel = eksempel or []
    sja_ogsa_omgrep = sja_ogsa_omgrep or []

    base_uri = _resolve(base_uri, "base_uri", profile, "base_uri")
    utgjevar_uri = _resolve(utgjevar_uri, "utgjevar_uri", profile, "utgjevar_uri")
    kjelde_relasjon = _resolve(kjelde_relasjon, "kjelde_relasjon", profile, "kjelde_relasjon")

    if kjelde_relasjon not in KJELDETYPAR:
        raise ValueError(
            f"Ugyldig kjelde_relasjon: '{kjelde_relasjon}'. "
            f"Gyldige: {list(KJELDETYPAR)}"
        )
    kjelde_uri = KJELDETYPAR[kjelde_relasjon]

    uri_cfg = profile.get("uri") or {}
    begrep_pattern      = uri_cfg.get("begrep_pattern",      "{base_uri}/{slug}")
    definisjon_pattern  = uri_cfg.get("definisjon_pattern",  "{base_uri}/def/{slug}-{lang}")
    kontaktpunkt_pattern = uri_cfg.get("kontaktpunkt_default", "{base_uri}/kontakt/begrepsansvarleg")

    begrep_uri = begrep_pattern.format(base_uri=base_uri, slug=slug)

    if not kontaktpunkt_uri:
        kontaktpunkt_uri = kontaktpunkt_pattern.format(base_uri=base_uri, slug=slug)

    # Bygg språkliste — dersom definisjon for nn/en manglar, bruk nb-tekst som fallback
    langs_with_terms = []
    if anbefalt_term_nb:
        langs_with_terms.append(("nb", anbefalt_term_nb, definisjon_nb))
    if anbefalt_term_nn:
        langs_with_terms.append(("nn", anbefalt_term_nn, definisjon_nn or definisjon_nb))
    if anbefalt_term_en:
        langs_with_terms.append(("en", anbefalt_term_en, definisjon_en or definisjon_nb))

    def_uris = [
        definisjon_pattern.format(base_uri=base_uri, slug=slug, lang=lang)
        for lang, _, _ in langs_with_terms
    ]

    begrep_dict: dict = {
        "id": begrep_uri,
        "anbefalt_term": [term for _, term, _ in langs_with_terms],
        "har_definisjon": def_uris,
        "identifikator_literal": begrep_uri,
        "kontaktpunkt_vcard": [kontaktpunkt_uri],
        "utgjevar": utgjevar_uri,
        "fagomrade": [fagomrade_uri],
    }
    if merknad:
        begrep_dict["merknad"] = merknad
    if eksempel:
        begrep_dict["eksempel"] = eksempel
    if sja_ogsa_omgrep:
        begrep_dict["sja_ogsa_omgrep"] = sja_ogsa_omgrep

    definisjoner = []
    for lang, _, tekst in langs_with_terms:
        if tekst:
            def_uri = definisjon_pattern.format(base_uri=base_uri, slug=slug, lang=lang)
            definisjoner.append({
                "id": def_uri,
                "tekst": tekst,
                "kjelde_relasjon": kjelde_uri,
            })

    container: dict = {
        "begrep": [begrep_dict],
        "definisjoner": definisjoner,
        "organisasjonar": [{"id": utgjevar_uri}],
        "kontaktpunkt": [{"id": kontaktpunkt_uri}],
    }

    add_comment = (profile.get("generation") or {}).get("add_header_comment", True)
    yaml_str = yaml.dump(
        container,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
    )

    if add_comment:
        yaml_str = (
            f"# Generert av mcp-linkml-begrep-generator — legg til i instansfila di\n"
            f"# Begrep: {begrep_uri}\n\n"
            + yaml_str
        )

    return yaml_str
