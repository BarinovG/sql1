ALTER TABLE singer RENAME COLUMN name TO name_singer;
ALTER TABLE genre RENAME COLUMN name TO name_genre;
ALTER TABLE album RENAME COLUMN name TO name_album;
ALTER TABLE song RENAME COLUMN name TO name_song;
ALTER TABLE song RENAME COLUMN time TO time_song;
ALTER TABLE mixtape RENAME COLUMN name TO name_mixtape;
ALTER TABLE album RENAME COLUMN year TO year_album;
ALTER TABLE mixtape RENAME COLUMN year TO year_mixtape;

INSERT INTO genresinger(genre_id, singer_id)
VALUES (1, 1),
(2,2),
(3,4),
(4,7),
(4,8),
(5,5),
(2,3),
(2,6);

INSERT INTO albumsinger(album_id, singer_id)
VALUES  (1,8),
		(2,1),
		(3,2),
		(4,3),
		(5,6),
		(6,7),
		(7,5),
		(8,1);

INSERT INTO albumsinger(album_id, singer_id)
VALUES  (1,8),
		(2,1),
		(3,2),
		(4,3),
		(5,6),
		(6,7),
		(7,5),
		(8,1);
	
INSERT INTO songmixtape (mixtape_id, song_id)
VALUES  (1,10), (1,4), (1,16), (1,3),
		(2,7), (2,10), (2,12), (2,16),
		(3,3), (3,2), (3,11), (3,4),
		(4,8), (4,16), (4,8), (4,13),
		(5,4), (5,8), (5,13), (5,15),
		(6,16), (6,8), (6,11), (6,1),
		(7,15), (7,1), (7,4), (7,12),
		(8,11), (8,12), (8,16), (8,4);
	
	
	
