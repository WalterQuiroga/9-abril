import os
from storage import connect_to_database, select_all_movies, save_movie, delete_movie
from models import Movie
from dotenv import load_dotenv

load_dotenv()


DB_NAME = os.getenv('DB_NAME')

con, cursor = connect_to_database(DB_NAME)

movie_one = Movie(title = 'Super Mario Bross', year = 2023, score = 9.7)


salir = True

while salir:
    print("Seleccione una opcion...")
    print("0 - Salir del programa")
    print("1 - Seleccionar todas las peliculas")
    print("2 - Crear una nueva pelicula")
    print("3 - Eliminar una pelicula")
    option =int(input(">>>"))
    if option==1:
        all_movies = select_all_movies(cursor)
        print(all_movies)
    elif option == 2:
        movie_title = input("ingrese el nombre de la pelicula: ")
        movie_year = int(input("ingrese el año de la pelicula: "))
        movie_score = float(input("ingrese la calificacion de la pelicula: "))
        movie = Movie(title = movie_title, year = movie_year, score = movie_score)
        save_movie(con, cursor, movie)
    elif option ==3:
        all_movies = select_all_movies(cursor)
        print("Peliculas guardadas")
        for movie in all_movies:
            print(f"Tiulo: {movie[0]}")
        movie_title = input("ingrese el nombre de la pelicula que desea eliminar: ")
        delete_movie(con, cursor, movie_title)
    else:
        print("Saliendo del programa")
        salir = False

