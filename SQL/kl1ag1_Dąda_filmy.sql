DROP TABLE IF EXISTS filmy;
CREATE TABLE Filmy (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    genre TEXT DEFAULT '',
    year INTEGER,
    imbd_rating DECIMAL
);

