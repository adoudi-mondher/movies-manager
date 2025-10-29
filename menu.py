from functions.display import display_movies
from functions.search import search_movie
from functions.seen import mark_movie_as_seen
from functions.add import add_movie
from functions.remove import remove_movie
from tabulate import tabulate

def menu():
    while True:
        print("\n=== Main MENU ===")
        print("1. Show all movies")
        print("2. Search for a movie")
        print("3. Mark a movie as seen")
        print("4. Add a movie")
        print("5. Delete a movie")
        print("6. Exit")

        choice = input("Choose an option between 1 and 6 : ")

        if choice == "1":
            movies = display_movies()
            if movies:
                print("\n🎬 List of available movies :\n")
                print(tabulate(movies, headers="keys", tablefmt="grid"))
            else:
                print("No movies found in the file !")
        elif choice == "2":
            target_movie = input("Enter the title of the movie to search: ")
            movie = search_movie(target_movie)
            if movie:
                print(f"\n🎬 Here are the details of the movie '{target_movie}' :\n")
                print(tabulate([movie], headers="keys", tablefmt="grid"))
            else:
                print(f"The movie '{target_movie}' was not found in the file!")
        elif choice == "3":
            target_movie = input("Which movie do you want to mark as seen ? ")
            if mark_movie_as_seen(target_movie):
                print(f"'{target_movie}' marked as successfully viewed!")
            else:
                print(f"'{target_movie}' not found in the file!")
        elif choice == "4":
            new_movie = {
                "Title": input("Enter a movie name: "),
                "Genre": input("Enter a movie genre: "),
                "Premiere": input("Enter movie release date: "),
                "Runtime": input("Enter the duration of the movie: "),
                "Language": input("Enter the language of the movie: "),
                "Watch": input("Have you seen the movie, Yes or No ?: ")
            }
            fields = ["Title", "Genre", "Premiere", "Runtime", "Language", "Watch"]
            if add_movie(new_movie, fields):
                print(f"'{new_movie["Title"]}' movie added successfully !")
            else:
                print(f"'{new_movie["Title"]}' movie already exists !")
        elif choice == "5":
            target_movie = input("Which movie do you want deleted ? ")
            if remove_movie(target_movie):
                print(f"The movie '{target_movie}' was deleted !")
            else:
                print(f"No movies found with the title '{target_movie}' !")
        elif choice == "6":
            print("Goodbye !")
            break
        else:
            print("Invalid choice ! Try again.")

if __name__ == "__main__":
    menu()

