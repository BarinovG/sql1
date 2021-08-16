CREATE TABLE IF NOT EXISTS Singer (
	id SERIAL PRIMARY KEY,
	name VARCHAR(40) NOT NULL unique
);

CREATE TABLE IF NOT EXISTS Genre (
	id SERIAL PRIMARY KEY,
	name VARCHAR(40) NOT NULL
);

CREATE TABLE IF NOT EXISTS GenreSinger (
  id SERIAL PRIMARY KEY,
  genre_id integer references genre(id) not null,
  singer_id integer references singer(id) not null
);

CREATE TABLE IF NOT EXISTS Album (
	id SERIAL PRIMARY KEY,
	name VARCHAR(40) NOT NULL,
	year integer NOT NULL
);

CREATE TABLE IF NOT EXISTS AlbumSinger (
  id SERIAL PRIMARY KEY,
  album_id integer references album(id) not null,
  singer_id integer references singer(id) not null
);

CREATE TABLE IF NOT EXISTS Song (
	id SERIAL PRIMARY KEY,
	name VARCHAR(40) NOT NULL,
	time integer NOT NULL,
	album_id integer references album(id) not null
);

CREATE TABLE IF NOT EXISTS Mixtape (
	id SERIAL PRIMARY KEY,
	name VARCHAR(40) NOT NULL,
	year integer NOT NULL
);

CREATE TABLE IF NOT EXISTS SongMixtape (
  id SERIAL PRIMARY KEY,
  song_id integer references song(id) not null,
  mixtape_id integer references mixtape(id) not null
);