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


def _build_langstring_array(nb_texts: list, nn_texts: list, en_texts: list, interleaved: bool = False) -> list:
    """
    Genererer LangString-streng-array i YAML-format.
    For multivalued LangString-slots i LinkML: ei liste av strenger der språk
    ikkje er eksplisitt tagga (språk avleiast ved RDF-serialisering).

    Args:
        nb_texts: liste av tekstar på bokmål
        nn_texts: liste av tekstar på nynorsk (fallback til nb dersom tom)
        en_texts: liste av tekstar på engelsk
        interleaved: dersom True, vekselinterleave språk per element (nb1, nn1, nb2, nn2, ...)
                     dersom False, flat liste (nb1, nb2, ..., nn1, nn2, ...)

    Returns:
        liste av strenger (LangString-YAML-format)
    """
    if not interleaved:
        # Flat liste: alle nb først, så nn, så en
        result = []
        result.extend(nb_texts)
        for i in range(len(nb_texts)):
            nn_text = nn_texts[i] if i < len(nn_texts) and nn_texts[i] else nb_texts[i]
            result.append(nn_text)
        if en_texts:
            result.extend(en_texts)
        return result
    else:
        # Interleaved: nb1, nn1, en1, nb2, nn2, en2, ...
        result = []
        for i in range(len(nb_texts)):
            result.append(nb_texts[i])
            nn_text = nn_texts[i] if i < len(nn_texts) and nn_texts[i] else nb_texts[i]
            result.append(nn_text)
            if i < len(en_texts) and en_texts[i]:
                result.append(en_texts[i])
        return result


def _generate_begrep_dict(
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
    merknad_nb: list | None = None,
    merknad_nn: list | None = None,
    merknad_en: list | None = None,
    tillate_term_nb: list | None = None,
    tillate_term_nn: list | None = None,
    tillate_term_en: list | None = None,
    eksempel_nb: list | None = None,
    eksempel_nn: list | None = None,
    eksempel_en: list | None = None,
    forkasta_term_nb: list | None = None,
    forkasta_term_nn: list | None = None,
    forkasta_term_en: list | None = None,
    verdiomrade_nb: list | None = None,
    verdiomrade_nn: list | None = None,
    verdiomrade_en: list | None = None,
    kjelde_tekst_nb: list | None = None,
    kjelde_tekst_nn: list | None = None,
    kjelde_tekst_en: list | None = None,
    sja_ogsa_omgrep: list | None = None,
) -> tuple[dict, list, str, str, str]:
    """
    Genererer begreps-dict, definisjoner, URI-ar og metadata.

    Returns:
        (begrep_dict, definisjoner, begrep_uri, kontaktpunkt_uri, utgjevar_uri)
    """
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
    # Alltid inkluder nn-versjon, med fallback til nb dersom anbefalt_term_nn manglar
    if anbefalt_term_nb:
        langs_with_terms.append(("nn", anbefalt_term_nn or anbefalt_term_nb, definisjon_nn or definisjon_nb))
    if anbefalt_term_en:
        langs_with_terms.append(("en", anbefalt_term_en, definisjon_en or definisjon_nb))

    def_uris = [
        definisjon_pattern.format(base_uri=base_uri, slug=slug, lang=lang)
        for lang, _, _ in langs_with_terms
    ]

    # Bygg anbefalt_term som streng-array (nb, nn, eventuelt en)
    anbefalt_term_list = [term for _, term, _ in langs_with_terms]

    begrep_dict: dict = {
        "id": begrep_uri,
        "anbefalt_term": anbefalt_term_list,
        "har_definisjon": def_uris,
        "identifikator_literal": begrep_uri,
        "kontaktpunkt_vcard": [kontaktpunkt_uri],
        "utgjevar": utgjevar_uri,
        "fagomrade": [fagomrade_uri],
    }

    # LangString-array-slots
    if merknad_nb:
        begrep_dict["merknad"] = _build_langstring_array(
            merknad_nb or [],
            merknad_nn or [],
            merknad_en or []
        )

    if tillate_term_nb:
        begrep_dict["tillate_term"] = _build_langstring_array(
            tillate_term_nb or [],
            tillate_term_nn or [],
            tillate_term_en or []
        )

    if eksempel_nb:
        begrep_dict["eksempel"] = _build_langstring_array(
            eksempel_nb or [],
            eksempel_nn or [],
            eksempel_en or []
        )

    if forkasta_term_nb:
        begrep_dict["forkasta_term"] = _build_langstring_array(
            forkasta_term_nb or [],
            forkasta_term_nn or [],
            forkasta_term_en or []
        )

    if verdiomrade_nb:
        begrep_dict["verdiomrade"] = _build_langstring_array(
            verdiomrade_nb or [],
            verdiomrade_nn or [],
            verdiomrade_en or []
        )

    if sja_ogsa_omgrep:
        begrep_dict["sja_ogsa_omgrep"] = sja_ogsa_omgrep

    definisjoner = []
    for lang, _, tekst in langs_with_terms:
        if tekst:
            def_uri = definisjon_pattern.format(base_uri=base_uri, slug=slug, lang=lang)
            def_obj = {
                "id": def_uri,
                "tekst": tekst,
                "kjelde_relasjon": kjelde_uri,
            }
            # Legg til kjelde_tekst dersom oppgjeve
            if kjelde_tekst_nb:
                def_obj["kjelde_tekst"] = _build_langstring_array(
                    kjelde_tekst_nb or [],
                    kjelde_tekst_nn or [],
                    kjelde_tekst_en or []
                )
            definisjoner.append(def_obj)

    return begrep_dict, definisjoner, begrep_uri, kontaktpunkt_uri, utgjevar_uri


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
    merknad_nb: list | None = None,
    merknad_nn: list | None = None,
    merknad_en: list | None = None,
    tillate_term_nb: list | None = None,
    tillate_term_nn: list | None = None,
    tillate_term_en: list | None = None,
    eksempel_nb: list | None = None,
    eksempel_nn: list | None = None,
    eksempel_en: list | None = None,
    forkasta_term_nb: list | None = None,
    forkasta_term_nn: list | None = None,
    forkasta_term_en: list | None = None,
    verdiomrade_nb: list | None = None,
    verdiomrade_nn: list | None = None,
    verdiomrade_en: list | None = None,
    kjelde_tekst_nb: list | None = None,
    kjelde_tekst_nn: list | None = None,
    kjelde_tekst_en: list | None = None,
    sja_ogsa_omgrep: list | None = None,
) -> str:
    """Returnerer ein YAML-streng med BegrepContainer-innhald for eitt begrep."""
    begrep_dict, definisjoner, begrep_uri, kontaktpunkt_uri, utgjevar_uri = _generate_begrep_dict(
        profile=profile,
        slug=slug,
        anbefalt_term_nb=anbefalt_term_nb,
        definisjon_nb=definisjon_nb,
        fagomrade_uri=fagomrade_uri,
        base_uri=base_uri,
        kjelde_relasjon=kjelde_relasjon,
        utgjevar_uri=utgjevar_uri,
        anbefalt_term_nn=anbefalt_term_nn,
        anbefalt_term_en=anbefalt_term_en,
        definisjon_nn=definisjon_nn,
        definisjon_en=definisjon_en,
        kontaktpunkt_uri=kontaktpunkt_uri,
        merknad_nb=merknad_nb,
        merknad_nn=merknad_nn,
        merknad_en=merknad_en,
        tillate_term_nb=tillate_term_nb,
        tillate_term_nn=tillate_term_nn,
        tillate_term_en=tillate_term_en,
        eksempel_nb=eksempel_nb,
        eksempel_nn=eksempel_nn,
        eksempel_en=eksempel_en,
        forkasta_term_nb=forkasta_term_nb,
        forkasta_term_nn=forkasta_term_nn,
        forkasta_term_en=forkasta_term_en,
        verdiomrade_nb=verdiomrade_nb,
        verdiomrade_nn=verdiomrade_nn,
        verdiomrade_en=verdiomrade_en,
        kjelde_tekst_nb=kjelde_tekst_nb,
        kjelde_tekst_nn=kjelde_tekst_nn,
        kjelde_tekst_en=kjelde_tekst_en,
        sja_ogsa_omgrep=sja_ogsa_omgrep,
    )

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
            f"# Generert av mcp-linkml-begrep-utkast — legg til i instansfila di\n"
            f"# Begrep: {begrep_uri}\n\n"
            + yaml_str
        )

    return yaml_str


def skriv_begrep_til_fil(
    output_path: Path,
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
    merknad_nb: list | None = None,
    merknad_nn: list | None = None,
    merknad_en: list | None = None,
    tillate_term_nb: list | None = None,
    tillate_term_nn: list | None = None,
    tillate_term_en: list | None = None,
    eksempel_nb: list | None = None,
    eksempel_nn: list | None = None,
    eksempel_en: list | None = None,
    forkasta_term_nb: list | None = None,
    forkasta_term_nn: list | None = None,
    forkasta_term_en: list | None = None,
    verdiomrade_nb: list | None = None,
    verdiomrade_nn: list | None = None,
    verdiomrade_en: list | None = None,
    kjelde_tekst_nb: list | None = None,
    kjelde_tekst_nn: list | None = None,
    kjelde_tekst_en: list | None = None,
    sja_ogsa_omgrep: list | None = None,
) -> Path:
    """
    Genererer og skriv begreps-YAML til fil (berre begreps-objektet, ikkje BegrepContainer).

    Returns:
        Path til den skrivne fila
    """
    begrep_dict, _, _, _, _ = _generate_begrep_dict(
        profile=profile,
        slug=slug,
        anbefalt_term_nb=anbefalt_term_nb,
        definisjon_nb=definisjon_nb,
        fagomrade_uri=fagomrade_uri,
        base_uri=base_uri,
        kjelde_relasjon=kjelde_relasjon,
        utgjevar_uri=utgjevar_uri,
        anbefalt_term_nn=anbefalt_term_nn,
        anbefalt_term_en=anbefalt_term_en,
        definisjon_nn=definisjon_nn,
        definisjon_en=definisjon_en,
        kontaktpunkt_uri=kontaktpunkt_uri,
        merknad_nb=merknad_nb,
        merknad_nn=merknad_nn,
        merknad_en=merknad_en,
        tillate_term_nb=tillate_term_nb,
        tillate_term_nn=tillate_term_nn,
        tillate_term_en=tillate_term_en,
        eksempel_nb=eksempel_nb,
        eksempel_nn=eksempel_nn,
        eksempel_en=eksempel_en,
        forkasta_term_nb=forkasta_term_nb,
        forkasta_term_nn=forkasta_term_nn,
        forkasta_term_en=forkasta_term_en,
        verdiomrade_nb=verdiomrade_nb,
        verdiomrade_nn=verdiomrade_nn,
        verdiomrade_en=verdiomrade_en,
        kjelde_tekst_nb=kjelde_tekst_nb,
        kjelde_tekst_nn=kjelde_tekst_nn,
        kjelde_tekst_en=kjelde_tekst_en,
        sja_ogsa_omgrep=sja_ogsa_omgrep,
    )

    # Skriv berre begreps-objektet til fil
    yaml_str = yaml.dump(
        begrep_dict,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
    )

    # Legg til header-kommentar
    yaml_str = f"# Generert av mcp-linkml-begrep-utkast\n" + yaml_str

    # Opprett mappe dersom den ikkje finst
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Skriv til fil
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(yaml_str)

    return output_path
