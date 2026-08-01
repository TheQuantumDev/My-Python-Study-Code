import requests

# API key
base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemonData = response.json() # convert to json format
        return pokemonData
    else:
        print(f"{response.status_code} Failed to retrieve data")

name = input("Enter a pokemon name: ")

pokemonInfo = get_pokemon_info(name)

if pokemonInfo:
    print(f"Name: {pokemonInfo["name"].capitalize()}")
    print(f"Id: {pokemonInfo["id"]}")
    print(f"Height: {pokemonInfo["height"]}")
    print(f"Weight: {pokemonInfo["weight"]}")