import csv
import os

CSV_FILE = "movies.csv"  # Global constant

def remove_movie(target_movie, csv_file=CSV_FILE):

    """Function delete movie entered by user"""

    found = False
    temp_file = CSV_FILE+ ".temp"

    with open(CSV_FILE, newline="", encoding="utf-8") as in_file, \
        open(temp_file, "w", newline="", encoding="utf-8") as out_file:

        reader = csv.DictReader(in_file)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(out_file, fieldnames=fieldnames)
        writer.writeheader()

        for movie in reader:
            if movie["Title"].lower().strip() != target_movie.lower().strip() :
                writer.writerow(movie)
            else:
                found = True

    os.replace(temp_file, CSV_FILE)
    return found

# Bloc de test uniquement si le fichier est lancé directement
if __name__ == "__main__":
    target_movie = input("Which movie do you want deleted ? ")
    if remove_movie(target_movie):
        print(f"The movie '{target_movie}' was deleted !")
    else:
        print(f"No movies found with the title '{target_movie}' !")
