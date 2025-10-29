import csv
import os

CSV_FILE = "movies.csv"  # Global constant

def add_movie(new_movie, fields, csv_file=CSV_FILE):

    """Function to add an movie in the list of movies"""

    # Check if the file is missing or empty to decide whether to write the header
    write_header = not os.path.exists(csv_file) or os.path.getsize(csv_file) == 0

    # Check if the movie already exists in the file (case-insensitive match)
    with open(csv_file, mode="r", encoding="utf-8", newline="") as file:
        
        reader = csv.DictReader(file)
        for film in reader:
            if film["Title"].strip().lower() == new_movie["Title"].strip().lower():
                return False  # Film already exists

    with open(csv_file, mode="a", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        if write_header:
            writer.writeheader()
        writer.writerow(new_movie)

    return True  # Film successfully added

# Bloc de test uniquement si le fichier est lancé directement
if __name__ == "__main__":
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