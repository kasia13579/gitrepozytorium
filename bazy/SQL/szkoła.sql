DROP TABLE IF EXISTS tbUczniowie;
DROP TABLE IF EXISTS tbKlasy;
CREATE TABLE tbUczniowie
(
	id INTEGER PRIMARY KEY AUTOINCREMENT;
	imie TEXT,
	nazwisko TEXT,
	PLEC INTEGER,
	id_klasa INTEGER,
	egzHum NUMERIC NOT NULL DEFAULT 0,
	egzMat NUMERIC NOT NULL DEFAULT 0,
	egzJez NUMERIC NOT NULL DEFAULT 0,
	FOREIGN KEY (id_klasa) REFERENCES  tbKlasy(id)
);

CREATE TABLE tbKlasy
(
id INTEGER PRIMARY KEY AUTOINCREMENT;
klasa TEXT,
rokNaboru INTEGER,
rokMatury INTEGER
);
INSERT INTO tbKlasy ( id, klasa, rokNaboru, rokMatury) VALUES ( NULL, '1A', 2017, 2020);
INSERT INTO tbKlasy ( id, klasa, rokNaboru, rokMatury) VALUES ( NULL, '1B', 2017, 2020);
INSERT INTO tbKlasy ( id, klasa, rokNaboru, rokMatury) VALUES ( NULL, '2A', 2016, 2019);

INSERT INTO tbUczniowie VALUES (NULL, 'Adam', 'Sodowy', 0 , 2 , 50 , 60, 69);
INSERT INTO tbUczniowie VALUES (NULL, 'Katarzyna', 'Dada', 1 , 1 , 70 , 65, 79);
INSERT INTO tbUczniowie VALUES (NULL, 'Adam', 'Sodowy', 0 , 2 , 50 , 60, 69);

