DROP TABLE IF EXISTS nazwiska;
CREATE TABLE nazwiska
(
    numer_ucznia INTEGER PRIMARY KEY,
    nazwisko TEXT(20),
    pierwsze_imie TEXT(10),
    drugie_imie TEXT(10)
);
DROP TABLE IF EXISTS dane_osobowe;
CREATE TABLE dane_osobowe
(
    numer_ucznia INTEGER PRIMARY KEY,
    dzien_urodzenia INTEGER(2),
    miesiac_urodzenia INTEGER(2),
    ostatnie_diwe_cyfry_roku_urodzenia INTEGER(2),
    miejsce_urodzenia TEXT,
    wojewodztwo TEXT
);
DROP TABLE IF EXISTS oceny;
CREATE TABLE oceny
(
    numer_ucznia INTEGER PRIMARY KEY AUTOINCREMENT,
    zach INTEGER,
    rel INTEGER,
    ety INTEGER,
    jpol INTEGER,
    jang INTEGER,
    jniem INTEGER,
    mat INTEGER,
    hist INTEGER,
    geog INTEGER,
    biol INTEGER,
    fiz INTEGER,
    che INTEGER,
    tech INTEGER,
    info INTEGER,
    plas INTEGER,
    PO INTEGER,
    WF TEXT
);
