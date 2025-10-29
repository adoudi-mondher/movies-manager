import csv
import os

CSV_FILE = "movies.csv"  # Global constant

def mark_movie_as_seen(target_movie, csv_file=CSV_FILE):

    """Function marked movie entered by user as seen"""

    found = False
    temp_file = CSV_FILE + ".temp"

    with open(csv_file, newline="", encoding="utf-8") as in_file, \
        open(temp_file, "w", newline="", encoding="utf-8") as out_file:
    
        reader = csv.DictReader(in_file)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(out_file, fieldnames=fieldnames)
        writer.writeheader()

        for movie in reader:
            if movie["Title"].lower().strip() == target_movie.lower().strip() :
                movie["Watch"] = "Yes"
                found = True
            writer.writerow(movie)

    # Replace the temporary file
    os.replace(temp_file, CSV_FILE)
    return found

# Bloc de test uniquement si le fichier est lancé directement
if __name__ == "__main__":
    target_movie = input("Which movie do you want to mark as seen ? ")
    if mark_movie_as_seen(target_movie):
        print(f"'{target_movie}' marked as successfully viewed!")
    else:
        print(f"'{target_movie}' not found in the file!")


