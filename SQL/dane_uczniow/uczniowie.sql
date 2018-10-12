DROP TABLE IF EXISTS oceny;
CREATE TABLE oceny
(
    id_ucznia INTEGER,
    ocena INTEGER,
    data DATE(10),
    ID_przedmiotu INTEGER
);
DROP TABLE IF EXISTS przedmioty;
CREATE TABLE przedmioty
(
    id_przedmiotu INTEGER,
    nazwa_przedmiotu TEXT,
    nazwisko_nauczyciela TEXT,
    imie_nauczyciela TEXT,
    FOREIGN KEY (id_przedmiotu) REFERENCES przedmioty(id_przedmiotu)
);
DROP TABLE IF EXISTS uczniowie;
CREATE TABLE uczniowie
(
    id_ucznia INTEGER PRIMARY KEY AUTOINCREMENT,
    nazwsiko TEXT,
    imie TEXT,
    ulica TEXT,
    dom INTEGER,
    id_klasy INTEGER,
    FOREIGN KEY (id_ucznia) REFERENCES uczniowie(id_ucznia)
);


