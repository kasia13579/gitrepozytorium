DROP TABLE IF EXISTS uzytkownicy;
CREATE TABLE uzytkownicy (
id_uzytkownika INTEGER PRIMARY KEY,
imie VARCHAR(30) NOT NULL CHECK (imie <> ''),
nazwisko VARCHAR(30) NOT NULL CHECK (nazwisko <> ''),
kraj VARCHAR(40) NOT NULL CHECK (kraj <> ''),
plec BOOLEAN
);

DROP TABLE IF EXISTS znajomosci;
CREATE TABLE znajomosci (
znajomy_1 INTEGER NOT NULL REFERENCES UZYTKOWNICY(id_uzytkownika) ON DELETE CASCADE,
znajomy_2 INTEGER NOT NULL REFERENCES UZYTKOWNICY(id_uzytkownika) ON DELETE CASCADE,
data DATE,
PRIMARY KEY (znajomy_1, znajomy_2)
);


DROP TABLE IF EXISTS zdjecia;
CREATE TABLE zdjecia (
id_zdjecia INTEGER PRIMARY KEY,
data_dodania DATE NOT NULL,
id_uzytkownika CHAR(2),
szerokosc CHAR(4),
wysokosc CHAR(4),
FOREIGN KEY (id_uzytkownika) REFERENCES uzytkownicy(id_uzytkownika)
ON DELETE CASCADE
);
