import csv
from tabulate import tabulate

CSV_FILE = "movies.csv"  # Global constant

def search_movie(target_movie, csv_file=CSV_FILE):

    """Function to search for a movie entered by a user"""

    with open(csv_file, mode="r", encoding="utf-8", newline="") as file:
        
        reader = csv.DictReader(file)
        rows = list(reader)
        
        for movie in rows :
            if movie["Title"].lower().strip() == target_movie.lower().strip() : # case-insensitive match
                return movie
            
# Bloc de test uniquement si le fichier est lancé directement
if __name__ == "__main__":

    target_movie = input("What movie are you looking for ? ")
    movie = search_movie(target_movie)
    if movie:
        print(f"\n🎬 Here are the details of the movie '{target_movie}' :\n")
        print(tabulate([movie], headers="keys", tablefmt="grid"))
    else:
        print(f"The movie'{target_movie}' was not found in the file !")





