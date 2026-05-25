import sys
import requests
import colorama
from colorama import Fore as F

colorama.init(autoreset=True)

def fetch_pokemon_info(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()

        print("\n")
        print(f"{F.GREEN}Here is some information about {F.RED}{pokemon_name.capitalize()}{F.GREEN}:")
        print(f"{F.CYAN}Name: {F.LIGHTMAGENTA_EX}{pokemon_name.capitalize()}")
        print(f"{F.CYAN}ID: {F.LIGHTMAGENTA_EX}{data['id']}")
        print(f"{F.CYAN}Image Link: {F.LIGHTMAGENTA_EX}{data['sprites']['front_default']}")
        print(f"{F.CYAN}Height: {F.LIGHTMAGENTA_EX}{data['height']} " + "decameters" if data['height'] > 1 else "decameter")
        print(f"{F.CYAN}Weight: {F.LIGHTMAGENTA_EX}{data['weight']} " + "hectograms" if data['weight'] > 1 else "hectogram")
        print(f"{F.CYAN}Type(s): " + F.LIGHTMAGENTA_EX + ", ".join(t['type']['name'].capitalize() for t in data['types']))
        print("\n".join(f"{F.CYAN}{s['stat']['name'].capitalize()}: {F.LIGHTMAGENTA_EX}{s['base_stat']}" for s in data['stats']))
        print(f"{F.CYAN}Ability(s): " + F.LIGHTMAGENTA_EX + ", ".join(a['ability']['name'].capitalize() for a in data['abilities']))
        print("\n")
    
    elif response.status_code == 404: print(f"{F.RED}NO SUCH POKEMON FOUND!")
    else: print(f"{F.RED}An error occured while searching data. Please try again.")
        
def main():
    while True:
        name_input = input(f"{F.GREEN}Enter a pokemon name (type 'q' to exit): ").strip()
        if name_input.lower() == 'q':
            sys.exit()
        else:
            fetch_pokemon_info(name_input)

if __name__ == "__main__":
    main()