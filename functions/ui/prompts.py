import inquirer
from rich.console import Console

console = Console()

def show_main_menu():
    """Menu principal avec inquirer"""
    questions = [
        inquirer.List('choice',
                     message="What do you want to do?",
                     choices=[
                         ('🎬 Show all movies', '1'),
                         ('🔍 Search for a movie', '2'),
                         ('✅ Mark a movie as seen', '3'),
                         ('➕ Add a movie', '4'),
                         ('🗑️  Delete a movie', '5'),
                         ('👋 Exit', '6')
                     ],
                     carousel=True
                     )
    ]
    
    try:
        answers = inquirer.prompt(questions)
        return answers['choice'] if answers else None
    except (KeyboardInterrupt, TypeError):
        return '6'


def prompt_movie_search():
    """Prompt pour rechercher un film par titre"""
    questions = [
        inquirer.Text('title',
                     message="Enter the movie title to search")
    ]
    try:
        answers = inquirer.prompt(questions)
        return answers['title'] if answers else None
    except (KeyboardInterrupt, TypeError):
        return None


def prompt_select_movie(movies):
    """Permet de sélectionner un film dans une liste"""
    if not movies:
        return None
    
    # Créer une liste de choix (affichage, valeur)
    choices = [(f"{movie.get('Title', 'Unknown')} ({movie.get('Premiere', 'N/A')})", 
                movie.get('Title', '')) 
               for movie in movies]
    
    questions = [
        inquirer.List('movie',
                     message="Select a movie",
                     choices=choices,
                     carousel=True)
    ]
    
    try:
        answers = inquirer.prompt(questions)
        return answers['movie'] if answers else None
    except (KeyboardInterrupt, TypeError):
        return None


def prompt_movie_title(message="Enter the movie title"):
    """Prompt générique pour entrer un titre de film"""
    questions = [
        inquirer.Text('title', message=message)
    ]
    try:
        answers = inquirer.prompt(questions)
        return answers['title'] if answers else None
    except (KeyboardInterrupt, TypeError):
        return None


def prompt_new_movie():
    """Prompt pour ajouter un nouveau film"""
    questions = [
        inquirer.Text('Title', 
                     message="Movie title",
                     validate=lambda _, x: len(x) > 0),
        inquirer.Text('Genre', 
                     message="Genre",
                     validate=lambda _, x: len(x) > 0),
        inquirer.Text('Premiere', 
                     message="Release date (e.g., February 2, 2022)",
                     validate=lambda _, x: len(x) > 0),
        inquirer.Text('Runtime', 
                     message="Duration (e.g., 120 min)",
                     validate=lambda _, x: len(x) > 0),
        inquirer.Text('Language', 
                     message="Language",
                     validate=lambda _, x: len(x) > 0),
        inquirer.List('Watch',
                     message="Have you seen it?",
                     choices=['Yes', 'No'],
                     default='No')
    ]
    
    try:
        return inquirer.prompt(questions)
    except (KeyboardInterrupt, TypeError):
        return None


def prompt_search_method():
    """Choisir entre recherche manuelle ou sélection dans la liste"""
    questions = [
        inquirer.List('method',
                     message="How do you want to find the movie?",
                     choices=[
                         ('📋 Select from list', 'select'),
                         ('⌨️  Type movie title', 'type')
                     ])
    ]
    
    try:
        answers = inquirer.prompt(questions)
        return answers['method'] if answers else None
    except (KeyboardInterrupt, TypeError):
        return None


def confirm_action(message):
    """Demande de confirmation pour une action"""
    questions = [
        inquirer.Confirm('confirmed',
                        message=message,
                        default=False)
    ]
    
    try:
        answers = inquirer.prompt(questions)
        return answers['confirmed'] if answers else False
    except (KeyboardInterrupt, TypeError):
        return False


def prompt_filter_seen():
    """Filtrer les films par statut vu/non vu"""
    questions = [
        inquirer.List('filter',
                     message="Filter movies",
                     choices=[
                         ('All movies', 'all'),
                         ('Seen movies only', 'seen'),
                         ('Unseen movies only', 'unseen')
                     ],
                     default='all')
    ]
    
    try:
        answers = inquirer.prompt(questions)
        return answers['filter'] if answers else 'all'
    except (KeyboardInterrupt, TypeError):
        return 'all'