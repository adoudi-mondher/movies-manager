"""
Movies Manager v2.0
Interface utilisateur améliorée avec inquirer et rich
"""

# Imports des fonctions métier (logique inchangée)
from functions.display import display_movies
from functions.search import search_movie
from functions.seen import mark_movie_as_seen
from functions.add import add_movie
from functions.remove import remove_movie

# Imports des nouveaux modules UI
from functions.ui.prompts import (
    show_main_menu,
    prompt_movie_search,
    prompt_select_movie,
    prompt_movie_title,
    prompt_new_movie,
    prompt_search_method,
    confirm_action,
    prompt_filter_seen
)

from functions.ui.display import (
    display_movies_rich,
    display_movie_details,
    display_filtered_movies,
    display_statistics,
    print_success,
    print_error,
    print_warning,
    print_info,
    show_welcome,
    show_goodbye,
    console
)


def menu():
    """Menu principal de l'application Movies Manager v2.0"""
    
    # Afficher l'écran de bienvenue
    show_welcome()
    
    while True:
        # Afficher le menu principal et récupérer le choix
        choice = show_main_menu()
        
        # Si l'utilisateur annule (Ctrl+C), sortir
        if not choice:
            show_goodbye()
            break
        
        # 1. Afficher tous les films
        if choice == "1":
            movies = display_movies()
            if movies:
                # Demander si l'utilisateur veut filtrer
                filter_choice = prompt_filter_seen()
                if filter_choice == 'all':
                    display_movies_rich(movies)
                else:
                    display_filtered_movies(movies, filter_choice)
                
                # Afficher les statistiques
                display_statistics(movies)
            else:
                print_error("No movies found in the file!")
        
        # 2. Rechercher un film
        elif choice == "2":
            target_movie = prompt_movie_search()
            if target_movie:
                movie = search_movie(target_movie)
                if movie:
                    display_movie_details(movie, target_movie)
                else:
                    print_error(f"The movie '{target_movie}' was not found!")
        
        # 3. Marquer un film comme vu
        elif choice == "3":
            # Demander la méthode de sélection
            method = prompt_search_method()
            
            if method == 'select':
                # Sélection depuis la liste
                movies = display_movies()
                if movies:
                    target_movie = prompt_select_movie(movies)
                else:
                    print_error("No movies available to select!")
                    target_movie = None
            else:
                # Saisie manuelle
                target_movie = prompt_movie_title("Which movie do you want to mark as seen?")
            
            # Marquer le film
            if target_movie:
                if mark_movie_as_seen(target_movie):
                    print_success(f"'{target_movie}' marked as seen!")
                else:
                    print_error(f"'{target_movie}' not found!")
        
        # 4. Ajouter un film
        elif choice == "4":
            new_movie = prompt_new_movie()
            
            if new_movie:
                fields = ["Title", "Genre", "Premiere", "Runtime", "Language", "Watch"]
                if add_movie(new_movie, fields):
                    print_success(f"Movie '{new_movie['Title']}' added successfully!")
                else:
                    print_error(f"Movie '{new_movie['Title']}' already exists!")
            else:
                print_warning("Movie addition cancelled.")
        
        # 5. Supprimer un film
        elif choice == "5":
            # Demander la méthode de sélection
            method = prompt_search_method()
            
            if method == 'select':
                # Sélection depuis la liste
                movies = display_movies()
                if movies:
                    target_movie = prompt_select_movie(movies)
                else:
                    print_error("No movies available to delete!")
                    target_movie = None
            else:
                # Saisie manuelle
                target_movie = prompt_movie_title("Which movie do you want to delete?")
            
            # Supprimer le film avec confirmation
            if target_movie:
                if confirm_action(f"Are you sure you want to delete '{target_movie}'?"):
                    if remove_movie(target_movie):
                        print_success(f"Movie '{target_movie}' deleted!")
                    else:
                        print_error(f"Movie '{target_movie}' not found!")
                else:
                    print_info("Deletion cancelled.")
        
        # 6. Quitter
        elif choice == "6":
            show_goodbye()
            break
        
        # Choix invalide (normalement impossible avec inquirer)
        else:
            print_error("Invalid choice! Try again.")


if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        # Gérer Ctrl+C proprement
        console.print("\n")
        show_goodbye()
    except Exception as e:
        # Gérer les erreurs inattendues
        print_error(f"An unexpected error occurred: {e}")
        console.print("\n")
        show_goodbye()