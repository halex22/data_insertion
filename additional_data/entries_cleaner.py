import json
from pathlib import Path


def format_pokemon_entries(data:dict) -> dict:
    """split the games and adds the corresponding entry"""
    formated_entries = {}
    for games, entry in data.items():
        for game in games.split('-'):
            formated_entries[game.strip()] = entry
    return formated_entries


if __name__ == '__main__':

    test_path = Path('./json_data/gen_1.json')

    test_batch = False

    with open (test_path, mode='r', encoding='utf8') as file:
        data:dict = json.load(file)



    if test_batch:
        for pokemon_name in data.keys():
            pokemon = data[pokemon_name]['pokedex_entries']
            format_pokemon_entries(data=pokemon)

    else:
        pokemon_name = next(data.keys().__iter__())
        pokemon = data[pokemon_name]['pokedex_entries']
        format_pokemon_entries(data=pokemon)

