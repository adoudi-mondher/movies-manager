import csv
from tabulate import tabulate

CSV_FILE = "movies.csv"  # Global constant

def display_movies(csv_file=CSV_FILE):
     
     """Function to display the list of movies"""
     
     with open(csv_file, mode="r", encoding="utf-8", newline="") as file:
        
        reader = csv.DictReader(file)
        return list(reader)

# Bloc de test uniquement si le fichier est lancé directement
if __name__ == "__main__":
    movies = display_movies()
    if movies:
        print("\n🎬 List of available movies :\n")
        print(tabulate(movies, headers="keys", tablefmt="grid"))
    else:
        print("No movies found in the file !")
    
    
