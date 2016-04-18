# blokovi_automatika

Automatsko ubacivanje kartografskih znakova prema specifikaciji DGU-a:

Potrebna je ulazna datoteka formata: 
br. E N H kod

Prema kodu se kreira .scr datoteka koja se učitava u autocad. Koordinate točke ubacuju blok na insertion point.
Prije učitavanja .scr, potrebno je ubaciti blok s simbolima.

Ukoliko nedostaje neki blok, potrebno je dodati kod s vrstom bloka.
Naziv bloka jednak je nazivu iz kartografskog ključa.
Ekstenzije .txt prije učitavanja u ACAD, promijeniti u .scr.