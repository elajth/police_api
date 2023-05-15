API över polisens händelser

Datamängden innehåller 500 aktuella händelsenotiser från polisen som ger kortfattad information om ett urval av de utryckningar som polisen gör.

Observera att det är inledande uppgifter om händelser som ligger till grund för notiserna. Det betyder att uppgifterna kan komma att ändras.

Notiserna brukar publiceras inom de närmsta timmarna efter det att händelsen har inträffat, men det kan variera beroende på situationen. Ibland uppdateras notiserna, när och hur ofta det sker varierar också beroende på situationen.

Informationsresursen innehåller inte personuppgifter.

Anrop till /api/events utan argument returnerar samtliga händelsenotiser som publiceras på polisen.se.

API:et finns här:
https://polisen.se/api/events
Om de olika delarna i API:et
Tid för händelsen

I API:et anges datum och tid för händelsen.

Filtrering på händelsetid/datum (t.ex. viss månad/dag/timme):

/api/events?DateTime=2018-03

/api/events?DateTime=2018-03-05

/api/events?DateTime=2018-03-05%2021
Plats för händelsen

Den geografiska plats som anges för händelsen är det län eller den kommun där händelsen har inträffat. I api:et skickar vi även med en koordinat. Det är en mittkoordinat för det område där händelsen har inträffat, alltså för kommunen eller länet. Det är inte den plats där själva händelsen har inträffat.

Filtrering på plats (flera platser kan separeras med semikolon):

/api/events?locationname=Stockholm;Järfälla
Händelsetyp

Den händelsetyp som anges i händelsen är en av ett antal bestämda kategorier.

Filtrering på händelsetyp (flera händelsetyper kan separeras med semikolon):

/api/events?type=Misshandel;R%C3%A5n

Den händelsetyp som anges är en av typerna i listan här nedan. Sammanfattningarna används bland annat för att sammanfatta vad som hänt i ett län under till exempel en natt.

    Alkohollagen
    Anträffad död
    Anträffat gods
    Arbetsplatsolycka
    Bedrägeri
    Bombhot
    Brand
    Brand automatlarm
    Bråk
    Detonation
    Djur skadat/omhändertaget
    Ekobrott
    Farligt föremål, misstänkt
    Fjällräddning
    Fylleri/LOB
    Förfalskningsbrott
    Försvunnen person
    Gränskontroll
    Häleri
    Inbrott
    Inbrott, försök
    Knivlagen
    Kontroll person/fordon
    Lagen om hundar och katter
    Larm inbrott
    Larm överfall
    Miljöbrott
    Missbruk av urkund
    Misshandel
    Misshandel, grov
    Mord/dråp
    Mord/dråp, försök
    Motorfordon, anträffat stulet
    Motorfordon, stöld
    Narkotikabrott
    Naturkatastrof
    Ofog barn/ungdom
    Ofredande/förargelse
    Olaga frihetsberövande
    Olaga hot
    Olaga intrång/hemfridsbrott
    Olovlig körning
    Ordningslagen
    Polisinsats/kommendering
    Rattfylleri
    Rån
    Rån väpnat
    Rån övrigt
    Rån, försök
    Räddningsinsats
    Sammanfattning dag
    Sammanfattning dygn
    Sammanfattning eftermiddag
    Sammanfattning förmiddag
    Sammanfattning helg
    Sammanfattning kväll
    Sammanfattning kväll och natt
    Sammanfattning natt
    Sammanfattning vecka
    Sedlighetsbrott
    Sjukdom/olycksfall
    Sjölagen
    Skadegörelse
    Skottlossning
    Skottlossning, misstänkt
    Spridning smittsamma kemikalier
    Stöld
    Stöld, försök
    Stöld, ringa
    Stöld/inbrott
    Tillfälligt obemannat
    Trafikbrott
    Trafikhinder
    Trafikkontroll
    Trafikolycka
    Trafikolycka, personskada
    Trafikolycka, singel
    Trafikolycka, smitning från
    Trafikolycka, vilt
    Uppdatering
    Utlänningslagen
    Vapenlagen
    Varningslarm/haveri
    Våld/hot mot tjänsteman
    Våldtäkt
    Våldtäkt, försök
    Vållande till kroppsskada

 
Granskad 31 mars 2021 