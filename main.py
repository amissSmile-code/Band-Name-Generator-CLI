import random
from rich import print as rprint
from rich.console import Console
from rich.panel import Panel
from rich.text import Text


def _choose_adjective() -> str:
    
    adjectives = ["Electric", "Silent", "Neon", "Mystic", "Cosmic", "Golden", "Quantum", "Retro", "Turbo"]
    return random.choice(adjectives) + " " if random.random() < 0.5 else ""

def _choose_genre() -> str:
   
    genres = ["Rock", "Jazz", "Synthwave", "Lo‑Fi", "Metal", "Indie", "Chiptune", "Ambient"]
    return random.choice(genres)

def generate_band_name(city: str, pet: str) -> str:
   
    adjective = _choose_adjective()
    genre = _choose_genre()
    # Ensure no double spaces when adjective is empty
    base = f"{adjective}{city} {pet}".strip()
    return f"{base} ({genre})"

def get_nonempty_input(prompt: str) -> str:
   
    while True:
        response = input(prompt).strip()
        if response :
            return response
        rprint("[red]Input cannot be empty. Please try again.[/red]")

def main() -> None:
    console = Console()
    console.print(Panel(Text("Welcome to the Band Name Generator!", justify="center"), style="bold magenta"))
    
    while True:
        city = get_nonempty_input("What is the name of the city you grew up in?\n")
        pet = get_nonempty_input("What is your pet name?\n")
        band_name = generate_band_name(city, pet)
        console.print(f"Your band name could be: [bold green]{band_name}[/bold green]")
        
        # Ask to continue
        choice = input("\nGenerate another? (y/n): ").lower().strip()
        if choice != 'y':
            console.print("[bold blue]Rock on! 🤘[/bold blue]")
            break
        
        console.rule()

if __name__ == "__main__":
    main()
