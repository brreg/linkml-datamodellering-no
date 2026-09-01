```mermaid
erDiagram
DigitalAdresse {
    uriorcurie digital_adresse_id  
    string digital_adresse_type  
    string identifikator  
}
EPostadresse {
    string brukernavn  
    string domenenavn  
    uriorcurie digital_adresse_id  
    string digital_adresse_type  
    string identifikator  
}
IPAdresse {
    string ip_nummer  
    uriorcurie digital_adresse_id  
    string digital_adresse_type  
    string identifikator  
}
Meldingsboks {
    string meldingsbokstype  
    uriorcurie digital_adresse_id  
    string digital_adresse_type  
    string identifikator  
}
Mobiltelefonnummer {
    NasjonaltNummer nasjonalt_nummer  
    PrefiksMedNasjonalKode prefiks_med_nasjonal_kode  
    uriorcurie digital_adresse_id  
    string digital_adresse_type  
    string identifikator  
}
Nettadresse {
    string domenenavn  
    string filsti  
    string protokoll  
    uriorcurie digital_adresse_id  
    string digital_adresse_type  
    string identifikator  
}
Telefonnummer {
    NasjonaltNummer nasjonalt_nummer  
    PrefiksMedNasjonalKode prefiks_med_nasjonal_kode  
    uriorcurie digital_adresse_id  
    string digital_adresse_type  
    string identifikator  
}




```
