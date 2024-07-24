import json
import os
from pathlib import Path

from utils import PokemonDict

DATA_DIR = Path('./json_data')

# get the first file to test the code:
test_file = next(os.scandir(DATA_DIR))

with open(test_file, mode='r', encoding='utf8') as file:
    data: dict = json.load(file)

    first_pokemon : PokemonDict = data[next(data.__iter__())]
    print(first_pokemon.get('pokedex_data'))
    # for key in data.keys():
    #     print('\n')
        # for value in data[key]:
        #     print(value)
