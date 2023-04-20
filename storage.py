import sqlite3


def connect_to_database(db):
    con = sqlite3.connect(db)
    return con, con.cursor()

def select_all_movies(cursor):
    cursor.execute("SELECT * FROM movie")
    lista_movies = cursor.fetchall()
    return lista_movies

def save_movie(con, cursor, movie):
    cursor.execute("""INSERT INTO movie 
                (title, year, score) VALUES 
                (?, ?, ?)
                """, (movie.title, movie.year, movie.score))
    con.commit()
    print(f"Pelicula '{movie.title}' guardada con exito")

def delete_movie(con, cursor, title):
        cursor.execute("""DELETE FROM movie
                WHERE title = ?
        """, (title, ))
        con.commit()
        print(f"Pelicula '{title}' eliminada con exito")

    


















class SQLiteStorage:
    pass
