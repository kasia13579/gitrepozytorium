DROP TABLE IF EXISTS dane_customers;
CREATE TABLE dane_customers
(
    customers_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT,
    address TEXT
);

DROP TABLE IF EXISTS dane_orders;
CREATE TABLE dane_orders
(
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    purchase_date DATE,
    FOREIGN KEY (dane_customers_id) REFERENCES dane_customers(id),
    FOREIGN KEY (dane_subscriptions_id) REFERENCES dane_subscriptions(id),
);

DROP TABLE IF EXISTS dane_subscriptions;
CREATE TABLE dane_subscriptions
(
    subscription_id INTEGER PRIMARY KEY AUTOINCREMENT,
    description    TEXT,
    price_per_month INTEGER,
    subscription_length TEXT
);

DROP TABLE IF EXISTS uczniowie;
CREATE TABLE uczniowie
(
    id  INTEGER PRIMARY KEY AUTOINCREMENT, 
    imie
    nazwisko
    plec
    id_klasa
    egz_hum
    egz_mat
    egz_jez
);

DROP TABLE IF EXISTS klasy;
CREATE TABLE klasy
(
    id
    klasa
    rok_naboru
    rok_matury
);

DROP TABLE IF EXISTS przedmioty;
CREATE TABLE przedmioty
(
    id
    przedmiot
    nazwisko_naucz
    imie_naucz
    plec_naucz
);

DROP TABLE IF EXISTS oceny;
CREATE TABLE oceny
(
    id
    datad
    id_uczen
    id_przedmiot
    oceny
);

