from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich import box
from rich.prompt import Prompt, Confirm

console = Console()


def display_movies_rich(movies):
    """Affiche tous les films avec Rich dans un tableau stylé"""
    if not movies:
        console.print("[yellow]⚠️  No movies found![/yellow]")
        return
    
    table = Table(
        title="🎬 Movie Collection", 
        box=box.ROUNDED,
        show_header=True,
        header_style="bold magenta",
        title_style="bold cyan"
    )
    
    # Ajouter les colonnes avec style
    table.add_column("Title", style="cyan", no_wrap=False)
    table.add_column("Genre", style="green")
    table.add_column("Premiere", style="yellow", justify="center")
    table.add_column("Runtime", style="blue", justify="center")
    table.add_column("Language", style="magenta")
    table.add_column("Watch", style="bold", justify="center")
    
    # Ajouter les lignes avec code couleur pour Watch
    for movie in movies:
        watch_status = movie.get('Watch', 'No')
        watch_style = "[green]✓ Yes[/green]" if watch_status == "Yes" else "[red]✗ No[/red]"
        
        table.add_row(
            movie.get('Title', ''),
            movie.get('Genre', ''),
            movie.get('Premiere', ''),
            movie.get('Runtime', ''),
            movie.get('Language', ''),
            watch_style
        )
    
    console.print("\n")
    console.print(table)
    console.print("\n")


def display_movie_details(movie, title):
    """Affiche les détails d'un film dans un panel élégant"""
    if not movie:
        print_error("Movie details not available")
        return
    
    # Créer le contenu avec formatage
    watch_emoji = "✅" if movie.get('Watch') == 'Yes' else "⏳"
    
    details = f"""
[bold cyan]Title:[/bold cyan] {movie.get('Title', 'N/A')}
[bold green]Genre:[/bold green] {movie.get('Genre', 'N/A')}
[bold yellow]Release:[/bold yellow] {movie.get('Premiere', 'N/A')}
[bold blue]Runtime:[/bold blue] {movie.get('Runtime', 'N/A')}
[bold magenta]Language:[/bold magenta] {movie.get('Language', 'N/A')}
[bold white]Watched:[/bold white] {watch_emoji} {movie.get('Watch', 'No')}
    """.strip()
    
    panel = Panel(
        details,
        title=f"🎬 {title}",
        border_style="green",
        box=box.DOUBLE,
        padding=(1, 2)
    )
    
    console.print("\n")
    console.print(panel)
    console.print("\n")


def display_filtered_movies(movies, filter_type='all'):
    """Affiche les films filtrés selon leur statut"""
    if filter_type == 'seen':
        filtered = [m for m in movies if m.get('Watch') == 'Yes']
        title = "🎬 Seen Movies"
    elif filter_type == 'unseen':
        filtered = [m for m in movies if m.get('Watch') == 'No']
        title = "🎬 Unseen Movies"
    else:
        filtered = movies
        title = "🎬 All Movies"
    
    if not filtered:
        console.print(f"[yellow]No {filter_type} movies found![/yellow]")
        return
    
    table = Table(
        title=title,
        box=box.ROUNDED,
        show_header=True,
        header_style="bold magenta"
    )
    
    table.add_column("Title", style="cyan")
    table.add_column("Genre", style="green")
    table.add_column("Premiere", style="yellow", justify="center")
    table.add_column("Runtime", style="blue", justify="center")
    
    for movie in filtered:
        table.add_row(
            movie.get('Title', ''),
            movie.get('Genre', ''),
            movie.get('Premiere', ''),
            movie.get('Runtime', '')
        )
    
    console.print("\n")
    console.print(table)
    console.print(f"\n[dim]Total: {len(filtered)} movie(s)[/dim]\n")


def print_success(message):
    """Affiche un message de succès avec style"""
    console.print(f"[bold green]✓ {message}[/bold green]")


def print_error(message):
    """Affiche un message d'erreur avec style"""
    console.print(f"[bold red]✗ {message}[/bold red]")


def print_info(message):
    """Affiche un message d'information avec style"""
    console.print(f"[blue]ℹ {message}[/blue]")


def print_warning(message):
    """Affiche un message d'avertissement avec style"""
    console.print(f"[yellow]⚠️  {message}[/yellow]")


def show_welcome():
    """Affiche un message de bienvenue stylé"""
    welcome_text = Text()
    welcome_text.append("🎬 ", style="bold yellow")
    welcome_text.append("Movies Manager", style="bold cyan")
    welcome_text.append(" v2.0", style="dim")
    
    panel = Panel(
        welcome_text,
        box=box.DOUBLE,
        border_style="cyan",
        padding=(1, 2)
    )
    
    console.print("\n")
    console.print(panel)
    console.print("\n")


def show_goodbye():
    """Affiche un message d'au revoir"""
    console.print("\n[bold green]👋 Goodbye! Thanks for using Movies Manager![/bold green]\n")


def print_separator():
    """Affiche une ligne de séparation"""
    console.print("\n" + "─" * 60 + "\n", style="dim")


def display_statistics(movies):
    """Affiche des statistiques sur la collection"""
    if not movies:
        print_warning("No movies to analyze")
        return
    
    total = len(movies)
    seen = len([m for m in movies if m.get('Watch') == 'Yes'])
    unseen = total - seen
    
    # Calcul du pourcentage
    seen_percent = (seen / total * 100) if total > 0 else 0
    
    stats = f"""
[bold]Total Movies:[/bold] {total}
[green]✓ Seen:[/green] {seen} ({seen_percent:.1f}%)
[red]✗ Unseen:[/red] {unseen} ({100-seen_percent:.1f}%)
    """.strip()
    
    panel = Panel(
        stats,
        title="📊 Collection Statistics",
        border_style="blue",
        box=box.ROUNDED,
        padding=(1, 2)
    )
    
    console.print("\n")
    console.print(panel)
    console.print("\n")