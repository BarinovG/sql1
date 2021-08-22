import sqlalchemy

engine = sqlalchemy.create_engine('postgresql+psycopg2://postgres:****@localhost:5432/homework v2')
connection = engine.connect()


# part 1
# Функции для "Домашнее задание к лекции «Select-запросы, выборки из одной таблицы»"

# Пользовательский ввод
def insert_genre(i=0):
    x = int(input('Какое количество жанров нужно будет добавить? '))
    for i in range(x):
        names = input(f'Введите название жанра №{i + 1}: ')
        connection.execute("""INSERT INTO genre(name_genre)
                   VALUES(%s)""", names)
        i += 1


def insert_singer(i=0):
    x = int(input('Какое количество певцов нужно будет добавить? '))
    for i in range(x):
        names = input(f'Введите имя певца №{i + 1}: ')
        connection.execute("""INSERT INTO singer(name_singer)
                   VALUES(%s)""", names)
        i += 1


def insert_albums(i=0):
    x = int(input('Какое количество альбомов нужно будет добавить? '))
    for i in range(x):
        names = input(f'Введите название альбома №{i + 1}: ')
        years = int(input(f'Введите год выпуска альбома №{i + 1}: '))
        connection.execute("""INSERT INTO album(name_album, year_album)
                   VALUES(%s, %s)""", (names, years))
        i += 1


def insert_track(i=0):
    x = int(input('Какое количество песен нужно будет добавить? '))
    for i in range(x):
        names = input(f'Введите название песни №{i + 1}: ')
        times = int(input(f'Введите длительность песни №{i + 1}: '))
        album_ids = int(input(f'Введите номер альбома, которому принадлежит песня №{i + 1}: '))
        connection.execute("""INSERT INTO song(name_album, time_song, album_id)
                   VALUES(%s, %s, %s)""", (names, times, album_ids))
        i += 1


def insert_mixtapes(i=0):
    x = int(input('Какое количество сборников нужно будет добавить? '))
    for i in range(x):
        names = input(f'Введите название сборника №{i + 1}: ')
        years = int(input(f'Введите год выпуска сборника №{i + 1}: '))
        connection.execute("""INSERT INTO mixtape(name_mixtape, year_mixtape)
                   VALUES(%s, %s)""", (names, years))
        i += 1


def album_by_year():
    years = int(input('Введите интересующий вас год выпуска альбомов, чтобы посмотреть, какие вышли в этом году: '))
    res = connection.execute("""SELECT name_album, year_album
    FROM album
    WHERE year_album=(%s)""", years).fetchmany(10)
    print(res)


def show_longer():
    res = connection.execute("""SELECT name_song, time_song
    FROM song 
    ORDER BY time_song DESC;""").fetchone()
    print(f'Самый длинный трек в нашей базе:{res}')


def track_by_time():
    sec = input('Введите минимальную продолжительность треков(в секундах), которые вам показать: ')
    res = connection.execute("""SELECT name_song
    FROM song
    WHERE time_song >= (%s)""", sec).fetchall()
    print(res)


def mixtape_by_year():
    print('Введите начальный и конечный год, за которые вы хотите посмотреть вышедшие сборники: ', end="")
    year1, year2 = input(), input()
    res = connection.execute("""SELECT name_mixtape
    FROM mixtape
    WHERE year_mixtape BETWEEN (%s) and (%s)""", (year1, year2)).fetchall()
    print(res)


def show_singer_onename():
    res = connection.execute("""SELECT name_singer 
    FROM singer
    WHERE name_singer NOT LIKE '%% %%' ;""").fetchall()
    print(res)


def find_song_with_my():
    res = connection.execute("""SELECT name_song
    FROM song
    WHERE name_song ILIKE '%%my%%' or name_song ILIKE '%%мой%%'; """).fetchall()
    print(res)


# part 2.
# Функции для "Домашнее задание к лекции «Группировки, выборки из нескольких таблиц»"

def amount_singer_in_genre():
    res = connection.execute("""SELECT g.name_genre AS Жанр, COUNT(s.name_singer) AS Количество_исполнителей
    FROM singer s 
	JOIN genresinger gs ON s.id = gs.singer_id
	JOIN genre g ON g.id = gs.genre_id
    GROUP BY g.name_genre;""").fetchall()
    print(res)


def amount_song_in_year():
    year1, year2 = input('Введите год начала: '), input('Введите конечный год: ')
    res = connection.execute("""SELECT year_album AS Год_выпуска, COUNT(name_song) AS Количество_песен 
	FROM song s JOIN album a ON s.album_id = a.id
    GROUP BY year_album
    HAVING year_album BETWEEN (%s) and (%s)""", (year1, year2)).fetchall()
    print(res)


def avg_timesong_by_album():
    res = connection.execute("""SELECT name_album AS Название_альбома, ROUND(AVG(time_song), 2) AS Средняя_продолжительность_песен 
    FROM song s JOIN album a ON s.album_id = a.id GROUP BY name_album ORDER BY 
    AVG(time_song) DESC, name_album;""").fetchall()
    print(res)


def find_noworking_singer_byyear():
    year = input('Введите год по которому надо посмотреть, всех кто не выпустил альбомы ')
    res = connection.execute("""SELECT name_singer, year_album
    FROM singer s
    JOIN albumsinger ac ON s.id = ac.singer_id 
    JOIN album a ON a.id = ac.album_id
    WHERE name_singer NOT IN (SELECT name_singer FROM singer s
                              JOIN albumsinger ac ON s.id = ac.singer_id 
                              JOIN album a ON a.id = ac.album_id
                              WHERE year_album = (%s))""", year).fetchall()
    print(res)


def find_mixtape_by_singer():
    name = str(input('Введите имя исполнителя, чтобы посмотреть в каких сборниках он присутствует: '))
    res = connection.execute("""SELECT name_mixtape AS Название_сборника, name_singer AS Исполнитель, name_song AS Название_песни
    FROM singer s JOIN albumsinger ac ON s.id = ac.singer_id 
    JOIN album a ON a.id = ac.album_id 
    JOIN song sg ON sg.album_id = a.id 
    JOIN songmixtape sm ON sg.id = sm.song_id 
    JOIN mixtape m ON m.id = sm.mixtape_id
    WHERE name_singer = (%s)""", name).fetchall()
    print(res)


def find_album_by_number_genres():
    amount_genre = input(
        'Введите больше какого количество исполнителей разных жанров должно пристуствовать в альбоме? ')
    res = connection.execute("""SELECT name_album AS Название_альбома, COUNT(name_genre) AS Количество_жанров
    FROM album a JOIN albumsinger ac ON a.id = ac.album_id
    JOIN singer s ON s.id = ac.singer_id
    JOIN genresinger gs ON s.id = gs.singer_id 
    JOIN genre g ON g.id = gs.genre_id
    GROUP BY name_album
    HAVING COUNT(name_genre) > (%s)""", amount_genre).fetchall()
    print(res)


def show_song_withouth_mixtapes():
    res = connection.execute("""SELECT name_singer AS Исполнитель, name_song AS Название_песни
    FROM singer s JOIN albumsinger ac ON s.id = ac.singer_id 
    JOIN album a ON a.id = ac.album_id 
    JOIN song sg ON sg.album_id = a.id 
    FULL OUTER JOIN songmixtape sm ON sg.id = sm.song_id 
    FULL OUTER JOIN mixtape m ON m.id = sm.mixtape_id
    WHERE name_mixtape IS NULL;""").fetchall()
    print(res)


def show_singer_shortest_song():
    res = connection.execute("""SELECT name_singer AS Исполнитель, name_song AS Название_песни, time_song AS Продолжинтельность_песни
    FROM singer s JOIN albumsinger ac ON s.id = ac.singer_id 
    JOIN album a ON a.id = ac.album_id 
    JOIN song sg ON sg.album_id = a.id
    WHERE time_song IN (SELECT MIN(time_song) 
                        FROM singer s JOIN albumsinger ac ON s.id = ac.singer_id 
                        JOIN album a ON a.id = ac.album_id 
                        JOIN song sg ON sg.album_id = a.id);""").fetchall()
    print(res)


def show_album_withMIN_tracks():
    res = connection.execute("""SELECT name_album, COUNT(name_song) AS amount
	FROM album a 
	JOIN song sg ON sg.album_id = a.id
    GROUP BY name_album 
    HAVING COUNT(name_song) = (
        SELECT MIN(amount) AS min_amount
        FROM 
            (
            SELECT name_album, COUNT(name_song) AS amount
            FROM album a 
            JOIN song sg ON sg.album_id = a.id
            GROUP BY name_album
            ) query_in
	)""").fetchall()
    print(res)


inputDict = {
    'ig': insert_genre,
    'is': insert_singer,
    'ia': insert_albums,
    'it': insert_track,
    'im': insert_mixtapes,
    'aby': album_by_year,
    'sl': show_longer,
    'tbt': track_by_time,
    'mby': mixtape_by_year,
    'sso': show_singer_onename,
    'fswm': find_song_with_my,
    'asig': amount_singer_in_genre,
    'asiy': amount_song_in_year,
    'atba': avg_timesong_by_album,
    'fnsb': find_noworking_singer_byyear,
    'fmbs': find_mixtape_by_singer,
    'fabng': find_album_by_number_genres,
    'sswm': show_song_withouth_mixtapes,
    'ssss': show_singer_shortest_song,
    'sawt': show_album_withMIN_tracks,
    'q': False
}


def userChoise():
    y = True
    print("ig - ввод жанров\nis - ввод певцов\nia - ввод альбомов\nit - ввод треков\nim - ввод сборников\naby - "
          "поисков альбомов по году\nsl - показать самый длинный трек\ntbt - показать треки по времени\nmby - "
          "показать сборники по году\nsso - показать певцов с одним именем\nfswm - найти песню с 'my'/'мой в "
          "названии'\nasig - количество исполнителей в каждом жанре\nasiy - количество треков, вошедших в альбомы "
          "N-N годов\natba - средняя продолжительность треков по каждому альбому\nfnsb - все исполнители, "
          "которые не выпустили альбомы в N году\nfmbs - названия сборников, в которых присутствует конкретный "
          "исполнитель\nfabng - название альбомов, в которых присутствуют исполнители более N жанра(ов)\nsswm - "
          "наименование треков, которые не входят в сборники\nssss - показать исполнителя(-ей), написавшего самый "
          "короткий по продолжительности трек\nsawt - название альбомов, содержащих наименьшее количество "
          "треков\n")
    while y:
        choise = input('Введите нужную команду: ').lower()
        inputDict[choise]()


if __name__ == '__main__':
    userChoise()
