"""Statisk liste over gyldige LOS-tema URI-ar og norske namn.

Henta frå https://psi.norge.no/los/ontologi/tema.
Slugar nyttar ASCII: æ→a, ø→o, å→a, mellomrom→-.
"""

LOS_TEMA: list[dict] = [
    # Næringsliv og næring
    {"uri": "https://psi.norge.no/los/tema/naringsliv",              "namn": "Næringsliv"},
    {"uri": "https://psi.norge.no/los/tema/naring",                  "namn": "Næring"},
    {"uri": "https://psi.norge.no/los/tema/naringsutvikling",        "namn": "Næringsutvikling"},
    {"uri": "https://psi.norge.no/los/tema/innovasjon",              "namn": "Innovasjon"},
    {"uri": "https://psi.norge.no/los/tema/handel",                  "namn": "Handel"},
    {"uri": "https://psi.norge.no/los/tema/reiseliv",                "namn": "Reiseliv"},
    {"uri": "https://psi.norge.no/los/tema/konkurranse",             "namn": "Konkurranse"},
    # Arbeidsliv
    {"uri": "https://psi.norge.no/los/tema/arbeid",                  "namn": "Arbeid"},
    {"uri": "https://psi.norge.no/los/tema/arbeidsliv",              "namn": "Arbeidsliv"},
    {"uri": "https://psi.norge.no/los/tema/arbeidsmarked",           "namn": "Arbeidsmarked"},
    {"uri": "https://psi.norge.no/los/tema/yrkesopplaring",          "namn": "Yrkesopplæring"},
    # Helse og omsorg
    {"uri": "https://psi.norge.no/los/tema/helse",                   "namn": "Helse"},
    {"uri": "https://psi.norge.no/los/tema/helse-og-omsorg",        "namn": "Helse og omsorg"},
    {"uri": "https://psi.norge.no/los/tema/omsorg",                  "namn": "Omsorg"},
    {"uri": "https://psi.norge.no/los/tema/psykisk-helse",          "namn": "Psykisk helse"},
    {"uri": "https://psi.norge.no/los/tema/folkehelse",              "namn": "Folkehelse"},
    {"uri": "https://psi.norge.no/los/tema/legemidler",             "namn": "Legemidler"},
    {"uri": "https://psi.norge.no/los/tema/rehabilitering",          "namn": "Rehabilitering"},
    # Utdanning og barnehage
    {"uri": "https://psi.norge.no/los/tema/utdanning",              "namn": "Utdanning"},
    {"uri": "https://psi.norge.no/los/tema/barnehage",              "namn": "Barnehage"},
    {"uri": "https://psi.norge.no/los/tema/grunnskole",             "namn": "Grunnskole"},
    {"uri": "https://psi.norge.no/los/tema/videregaende-opplaring", "namn": "Videregående opplæring"},
    {"uri": "https://psi.norge.no/los/tema/hoyere-utdanning",       "namn": "Høyere utdanning"},
    {"uri": "https://psi.norge.no/los/tema/voksenopplaring",        "namn": "Voksenopplæring"},
    # Kultur og fritid
    {"uri": "https://psi.norge.no/los/tema/kultur",                 "namn": "Kultur"},
    {"uri": "https://psi.norge.no/los/tema/idrett",                 "namn": "Idrett"},
    {"uri": "https://psi.norge.no/los/tema/fritid",                 "namn": "Fritid"},
    {"uri": "https://psi.norge.no/los/tema/kulturarv",              "namn": "Kulturarv"},
    {"uri": "https://psi.norge.no/los/tema/bibliotek",              "namn": "Bibliotek"},
    {"uri": "https://psi.norge.no/los/tema/medier",                 "namn": "Medier"},
    # Samferdsel og infrastruktur
    {"uri": "https://psi.norge.no/los/tema/samferdsel",             "namn": "Samferdsel"},
    {"uri": "https://psi.norge.no/los/tema/transport",              "namn": "Transport"},
    {"uri": "https://psi.norge.no/los/tema/kollektivtransport",     "namn": "Kollektivtransport"},
    {"uri": "https://psi.norge.no/los/tema/luftfart",               "namn": "Luftfart"},
    {"uri": "https://psi.norge.no/los/tema/sjofart",                "namn": "Sjøfart"},
    {"uri": "https://psi.norge.no/los/tema/vei",                    "namn": "Vei"},
    {"uri": "https://psi.norge.no/los/tema/trafikk",                "namn": "Trafikk"},
    # Miljø og klima
    {"uri": "https://psi.norge.no/los/tema/miljo",                  "namn": "Miljø"},
    {"uri": "https://psi.norge.no/los/tema/klima",                  "namn": "Klima"},
    {"uri": "https://psi.norge.no/los/tema/energi",                 "namn": "Energi"},
    {"uri": "https://psi.norge.no/los/tema/natur",                  "namn": "Natur"},
    {"uri": "https://psi.norge.no/los/tema/avfall",                 "namn": "Avfall"},
    {"uri": "https://psi.norge.no/los/tema/forurensning",           "namn": "Forurensning"},
    {"uri": "https://psi.norge.no/los/tema/naturressurser",         "namn": "Naturressurser"},
    {"uri": "https://psi.norge.no/los/tema/friluftsliv",            "namn": "Friluftsliv"},
    # Demokrati og styring
    {"uri": "https://psi.norge.no/los/tema/demokrati",              "namn": "Demokrati"},
    {"uri": "https://psi.norge.no/los/tema/valg",                   "namn": "Valg"},
    {"uri": "https://psi.norge.no/los/tema/politikk",               "namn": "Politikk"},
    # Offentleg forvaltning
    {"uri": "https://psi.norge.no/los/tema/offentlig-forvaltning",  "namn": "Offentlig forvaltning"},
    {"uri": "https://psi.norge.no/los/tema/digitalisering",         "namn": "Digitalisering"},
    {"uri": "https://psi.norge.no/los/tema/rettigheter",            "namn": "Rettigheter"},
    {"uri": "https://psi.norge.no/los/tema/personvern",             "namn": "Personvern"},
    {"uri": "https://psi.norge.no/los/tema/anskaffelser",           "namn": "Anskaffelser"},
    # Økonomi og finans
    {"uri": "https://psi.norge.no/los/tema/okonomi",                "namn": "Økonomi"},
    {"uri": "https://psi.norge.no/los/tema/skatt",                  "namn": "Skatt"},
    {"uri": "https://psi.norge.no/los/tema/avgift",                 "namn": "Avgift"},
    {"uri": "https://psi.norge.no/los/tema/bank-og-finans",         "namn": "Bank og finans"},
    {"uri": "https://psi.norge.no/los/tema/trygd",                  "namn": "Trygd"},
    {"uri": "https://psi.norge.no/los/tema/sosialhjelp",            "namn": "Sosialhjelp"},
    {"uri": "https://psi.norge.no/los/tema/regnskap",               "namn": "Regnskap"},
    # Bygg, eiendom og plan
    {"uri": "https://psi.norge.no/los/tema/bygg",                   "namn": "Bygg"},
    {"uri": "https://psi.norge.no/los/tema/eiendom",                "namn": "Eiendom"},
    {"uri": "https://psi.norge.no/los/tema/bolig",                  "namn": "Bolig"},
    {"uri": "https://psi.norge.no/los/tema/plan-og-areal",          "namn": "Plan og areal"},
    {"uri": "https://psi.norge.no/los/tema/geodata",                "namn": "Geodata"},
    # Familie og individ
    {"uri": "https://psi.norge.no/los/tema/familie",                "namn": "Familie"},
    {"uri": "https://psi.norge.no/los/tema/barn",                   "namn": "Barn"},
    {"uri": "https://psi.norge.no/los/tema/ekteskap",               "namn": "Ekteskap"},
    # Justis og sikkerhet
    {"uri": "https://psi.norge.no/los/tema/justis",                 "namn": "Justis"},
    {"uri": "https://psi.norge.no/los/tema/politi",                 "namn": "Politi"},
    {"uri": "https://psi.norge.no/los/tema/forsvar",                "namn": "Forsvar"},
    {"uri": "https://psi.norge.no/los/tema/beredskap",              "namn": "Beredskap"},
    # Innvandring og integrering
    {"uri": "https://psi.norge.no/los/tema/innvandring",            "namn": "Innvandring"},
    {"uri": "https://psi.norge.no/los/tema/integrering",            "namn": "Integrering"},
    {"uri": "https://psi.norge.no/los/tema/asyl",                   "namn": "Asyl"},
    # Landbruk og matproduksjon
    {"uri": "https://psi.norge.no/los/tema/landbruk",               "namn": "Landbruk"},
    {"uri": "https://psi.norge.no/los/tema/matproduksjon",          "namn": "Matproduksjon"},
    {"uri": "https://psi.norge.no/los/tema/fiske",                  "namn": "Fiske"},
    {"uri": "https://psi.norge.no/los/tema/havbruk",                "namn": "Havbruk"},
    # Religion og livssyn
    {"uri": "https://psi.norge.no/los/tema/religion",               "namn": "Religion"},
    {"uri": "https://psi.norge.no/los/tema/livssyn",                "namn": "Livssyn"},
]
