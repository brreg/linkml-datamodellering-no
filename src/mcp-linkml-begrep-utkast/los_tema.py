"""Statisk liste over gyldige LOS-tema URI-ar og norske navn.

Henta frå https://psi.norge.no/los/ontologi/tema.
Slugar nyttar ASCII: æ→a, ø→o, å→a, mellomrom→-.
"""

LOS_TEMA: list[dict] = [
    # Næringsliv og næring
    {"uri": "https://psi.norge.no/los/tema/naringsliv",              "navn": "Næringsliv"},
    {"uri": "https://psi.norge.no/los/tema/naring",                  "navn": "Næring"},
    {"uri": "https://psi.norge.no/los/tema/naringsutvikling",        "navn": "Næringsutvikling"},
    {"uri": "https://psi.norge.no/los/tema/innovasjon",              "navn": "Innovasjon"},
    {"uri": "https://psi.norge.no/los/tema/handel",                  "navn": "Handel"},
    {"uri": "https://psi.norge.no/los/tema/reiseliv",                "navn": "Reiseliv"},
    {"uri": "https://psi.norge.no/los/tema/konkurranse",             "navn": "Konkurranse"},
    # Arbeidsliv
    {"uri": "https://psi.norge.no/los/tema/arbeid",                  "navn": "Arbeid"},
    {"uri": "https://psi.norge.no/los/tema/arbeidsliv",              "navn": "Arbeidsliv"},
    {"uri": "https://psi.norge.no/los/tema/arbeidsmarked",           "navn": "Arbeidsmarked"},
    {"uri": "https://psi.norge.no/los/tema/yrkesopplaring",          "navn": "Yrkesopplæring"},
    # Helse og omsorg
    {"uri": "https://psi.norge.no/los/tema/helse",                   "navn": "Helse"},
    {"uri": "https://psi.norge.no/los/tema/helse-og-omsorg",        "navn": "Helse og omsorg"},
    {"uri": "https://psi.norge.no/los/tema/omsorg",                  "navn": "Omsorg"},
    {"uri": "https://psi.norge.no/los/tema/psykisk-helse",          "navn": "Psykisk helse"},
    {"uri": "https://psi.norge.no/los/tema/folkehelse",              "navn": "Folkehelse"},
    {"uri": "https://psi.norge.no/los/tema/legemidler",             "navn": "Legemidler"},
    {"uri": "https://psi.norge.no/los/tema/rehabilitering",          "navn": "Rehabilitering"},
    # Utdanning og barnehage
    {"uri": "https://psi.norge.no/los/tema/utdanning",              "navn": "Utdanning"},
    {"uri": "https://psi.norge.no/los/tema/barnehage",              "navn": "Barnehage"},
    {"uri": "https://psi.norge.no/los/tema/grunnskole",             "navn": "Grunnskole"},
    {"uri": "https://psi.norge.no/los/tema/videregaende-opplaring", "navn": "Videregående opplæring"},
    {"uri": "https://psi.norge.no/los/tema/hoyere-utdanning",       "navn": "Høyere utdanning"},
    {"uri": "https://psi.norge.no/los/tema/voksenopplaring",        "navn": "Voksenopplæring"},
    # Kultur og fritid
    {"uri": "https://psi.norge.no/los/tema/kultur",                 "navn": "Kultur"},
    {"uri": "https://psi.norge.no/los/tema/idrett",                 "navn": "Idrett"},
    {"uri": "https://psi.norge.no/los/tema/fritid",                 "navn": "Fritid"},
    {"uri": "https://psi.norge.no/los/tema/kulturarv",              "navn": "Kulturarv"},
    {"uri": "https://psi.norge.no/los/tema/bibliotek",              "navn": "Bibliotek"},
    {"uri": "https://psi.norge.no/los/tema/medier",                 "navn": "Medier"},
    # Samferdsel og infrastruktur
    {"uri": "https://psi.norge.no/los/tema/samferdsel",             "navn": "Samferdsel"},
    {"uri": "https://psi.norge.no/los/tema/transport",              "navn": "Transport"},
    {"uri": "https://psi.norge.no/los/tema/kollektivtransport",     "navn": "Kollektivtransport"},
    {"uri": "https://psi.norge.no/los/tema/luftfart",               "navn": "Luftfart"},
    {"uri": "https://psi.norge.no/los/tema/sjofart",                "navn": "Sjøfart"},
    {"uri": "https://psi.norge.no/los/tema/vei",                    "navn": "Vei"},
    {"uri": "https://psi.norge.no/los/tema/trafikk",                "navn": "Trafikk"},
    # Miljø og klima
    {"uri": "https://psi.norge.no/los/tema/miljo",                  "navn": "Miljø"},
    {"uri": "https://psi.norge.no/los/tema/klima",                  "navn": "Klima"},
    {"uri": "https://psi.norge.no/los/tema/energi",                 "navn": "Energi"},
    {"uri": "https://psi.norge.no/los/tema/natur",                  "navn": "Natur"},
    {"uri": "https://psi.norge.no/los/tema/avfall",                 "navn": "Avfall"},
    {"uri": "https://psi.norge.no/los/tema/forurensning",           "navn": "Forurensning"},
    {"uri": "https://psi.norge.no/los/tema/naturressurser",         "navn": "Naturressurser"},
    {"uri": "https://psi.norge.no/los/tema/friluftsliv",            "navn": "Friluftsliv"},
    # Demokrati og styring
    {"uri": "https://psi.norge.no/los/tema/demokrati",              "navn": "Demokrati"},
    {"uri": "https://psi.norge.no/los/tema/valg",                   "navn": "Valg"},
    {"uri": "https://psi.norge.no/los/tema/politikk",               "navn": "Politikk"},
    # Offentleg forvaltning
    {"uri": "https://psi.norge.no/los/tema/offentlig-forvaltning",  "navn": "Offentlig forvaltning"},
    {"uri": "https://psi.norge.no/los/tema/digitalisering",         "navn": "Digitalisering"},
    {"uri": "https://psi.norge.no/los/tema/rettigheter",            "navn": "Rettigheter"},
    {"uri": "https://psi.norge.no/los/tema/personvern",             "navn": "Personvern"},
    {"uri": "https://psi.norge.no/los/tema/anskaffelser",           "navn": "Anskaffelser"},
    # Økonomi og finans
    {"uri": "https://psi.norge.no/los/tema/okonomi",                "navn": "Økonomi"},
    {"uri": "https://psi.norge.no/los/tema/skatt",                  "navn": "Skatt"},
    {"uri": "https://psi.norge.no/los/tema/avgift",                 "navn": "Avgift"},
    {"uri": "https://psi.norge.no/los/tema/bank-og-finans",         "navn": "Bank og finans"},
    {"uri": "https://psi.norge.no/los/tema/trygd",                  "navn": "Trygd"},
    {"uri": "https://psi.norge.no/los/tema/sosialhjelp",            "navn": "Sosialhjelp"},
    {"uri": "https://psi.norge.no/los/tema/regnskap",               "navn": "Regnskap"},
    # Bygg, eiendom og plan
    {"uri": "https://psi.norge.no/los/tema/bygg",                   "navn": "Bygg"},
    {"uri": "https://psi.norge.no/los/tema/eiendom",                "navn": "Eiendom"},
    {"uri": "https://psi.norge.no/los/tema/bolig",                  "navn": "Bolig"},
    {"uri": "https://psi.norge.no/los/tema/plan-og-areal",          "navn": "Plan og areal"},
    {"uri": "https://psi.norge.no/los/tema/geodata",                "navn": "Geodata"},
    # Familie og individ
    {"uri": "https://psi.norge.no/los/tema/familie",                "navn": "Familie"},
    {"uri": "https://psi.norge.no/los/tema/barn",                   "navn": "Barn"},
    {"uri": "https://psi.norge.no/los/tema/ekteskap",               "navn": "Ekteskap"},
    # Justis og sikkerhet
    {"uri": "https://psi.norge.no/los/tema/justis",                 "navn": "Justis"},
    {"uri": "https://psi.norge.no/los/tema/politi",                 "navn": "Politi"},
    {"uri": "https://psi.norge.no/los/tema/forsvar",                "navn": "Forsvar"},
    {"uri": "https://psi.norge.no/los/tema/beredskap",              "navn": "Beredskap"},
    # Innvandring og integrering
    {"uri": "https://psi.norge.no/los/tema/innvandring",            "navn": "Innvandring"},
    {"uri": "https://psi.norge.no/los/tema/integrering",            "navn": "Integrering"},
    {"uri": "https://psi.norge.no/los/tema/asyl",                   "navn": "Asyl"},
    # Landbruk og matproduksjon
    {"uri": "https://psi.norge.no/los/tema/landbruk",               "navn": "Landbruk"},
    {"uri": "https://psi.norge.no/los/tema/matproduksjon",          "navn": "Matproduksjon"},
    {"uri": "https://psi.norge.no/los/tema/fiske",                  "navn": "Fiske"},
    {"uri": "https://psi.norge.no/los/tema/havbruk",                "navn": "Havbruk"},
    # Religion og livssyn
    {"uri": "https://psi.norge.no/los/tema/religion",               "navn": "Religion"},
    {"uri": "https://psi.norge.no/los/tema/livssyn",                "navn": "Livssyn"},
]
