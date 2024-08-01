import json
from pathlib import Path


def get_local_pokedex_dict(data: str) -> dict:
    local_dex_dict = {}
    data = data.replace('—' , '/')
    sections = data.split(')')[:-1]
    for section in sections:
        pokedex_index, games = section.split('(')
        for game in games.split('/'):
            local_dex_dict[game.strip()] = int(pokedex_index)
    return local_dex_dict



if __name__ == '__main__':
    test_path = Path('./json_data/gen_1.json')

    test_batch = True

    with open (test_path, mode='r', encoding='utf8') as file:
        data:dict = json.load(file)

    if test_batch:
        for pokemon_name in data.keys():
            pokemon = data[pokemon_name]['pokedex_data']['local']
            print(get_local_pokedex_dict(pokemon))

    else:
        pokemon_name = next(data.keys().__iter__())

        pokemon = data[pokemon_name]['pokedex_data']['local']
        print(get_local_pokedex_dict(pokemon))