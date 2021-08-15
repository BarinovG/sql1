import sqlalchemy

engine = sqlalchemy.create_engine('postgresql+psycopg2://postgres:6496@localhost:5432/homework v2')
connection = engine.connect()
i = 0

# Пользовательский ввод
def insert_genre(i=0):
    x = int(input('Какое количество жанров нужно будет добавить? '))
    for i in range(x):
        names = input(f'Введите название жанра №{i+1}: ')
        connection.execute("""INSERT INTO genre(name)
                   VALUES(%s)""", (names))
        i += 1

def insert_singer(i=0):
    x = int(input('Какое количество певцов нужно будет добавить? '))
    for i in range(x):
        names = input(f'Введите имя певца №{i+1}: ')
        connection.execute("""INSERT INTO singer(name)
                   VALUES(%s)""", (names))
        i += 1

def insert_albums(i=0):
    x = int(input('Какое количество альбомов нужно будет добавить? '))
    for i in range(x):
        names = input(f'Введите название альбома №{i+1}: ')
        years = int(input(f'Введите год выпуска альбома №{i+1}: '))
        connection.execute("""INSERT INTO album(name, year)
                   VALUES(%s, %s)""", (names, years))
        i += 1

def insert_track(i=0):
    x = int(input('Какое количество песен нужно будет добавить? '))
    for i in range(x):
        names = input(f'Введите название песни №{i+1}: ')
        times = int(input(f'Введите длительность песни №{i+1}: '))
        album_ids = int(input(f'Введите номер альбома, которому принадлежит песня №{i+1}: '))
        connection.execute("""INSERT INTO song(name, time, album_id)
                   VALUES(%s, %s, %s)""", (names, times, album_ids))
        i += 1

def insert_mixtapes(i=0):
    x = int(input('Какое количество сборников нужно будет добавить? '))
    for i in range(x):
        names = input(f'Введите название сборника №{i+1}: ')
        years = int(input(f'Введите год выпуска сборника №{i+1}: '))
        connection.execute("""INSERT INTO mixtape(name, year)
                   VALUES(%s, %s)""", (names, years))
        i += 1

def album_by_year():
    years = int(input('Введите интересующий вас год выпуска альбомов, чтобы посмотреть, какие вышли в этом году: '))
    res = connection.execute("""SELECT name, year 
    FROM album
    WHERE year=(%s)""", (years)).fetchmany(10)
    print(res)

def show_longer():
    res = connection.execute("""SELECT name, time 
    FROM song 
    ORDER BY time DESC;""").fetchone()
    print(f'Самый длинный трек в нашей базе:{res}')

def track_by_time():
    sec = input('Введите минимальную продолжительность треков(в секундах), которые вам показать: ')
    res = connection.execute("""SELECT name 
    FROM song
    WHERE time >= (%s)""", (sec)).fetchall()
    print(res)

def mixtape_by_year():
    print('Введите начальный и конечный год, за которые вы хотите посмотреть вышедшие сборники: ', end="")
    year1, year2 = input(), input()
    res = connection.execute("""SELECT name 
    FROM mixtape
    WHERE year BETWEEN (%s) and (%s)""", (year1, year2)).fetchall()
    print(res)

def show_singer_onename():
    res = connection.execute("""SELECT name 
    FROM singer
    WHERE name NOT LIKE '%% %%' ;""").fetchall()
    print(res)

# def find_song_with_my(word='my', ruword='мой'):
#     res = connection.execute("""SELECT name
#     FROM song
#     WHERE name LIKE '%%(%s)%%' or '%%(%s)%%' """, (word, ruword)).fetchall()
#     print(res)

def find_song_with_my():
    res = connection.execute("""SELECT name 
    FROM song
    WHERE name ILIKE '%%my%%' or name ILIKE '%%мой%%'; """).fetchall()
    print(res)

inputDict = {
    'ig' : insert_genre,
    'is' : insert_singer,
    'ia' : insert_albums,
    'it' : insert_track,
    'im' : insert_mixtapes,
    'aby' : album_by_year,
    'sl' : show_longer,
    'tbt' : track_by_time,
    'mby' : mixtape_by_year,
    'sso' : show_singer_onename,
    'fswm' : find_song_with_my,
    'q' : False
}

def userChoise():
    y = True
    while y:
        choise = input("ig - ввод жанров\nis - ввод певцов\nia - ввод альбомов\nit - ввод треков\nim - ввод сборников\naby - поисков альбомов по году\nsl - показать самый длинный трек\ntbt - показать треки по времени\nmby - показать сборники по году\nsso - показать певцов с одним именем\nfswm - найти песню с 'my'/'мой в названии'\nВведите нужную команду: ").lower()
        inputDict[choise]()

if __name__ == '__main__':
    userChoise()




