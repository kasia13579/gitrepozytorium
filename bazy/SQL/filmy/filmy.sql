DROP TABLE IF EXISTS filmy;
CREATE TABLE filmy (
	id INTEGER PRIMARY KEY,
	name TEXT not null,
	genre TEXT DEFAULT '',
	year INTEGER,
	rating DECIMAL
);
