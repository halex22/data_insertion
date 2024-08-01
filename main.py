import json
import os
from pathlib import Path

from additional_data import clean_types_effect, entries_cleaner
from sections_cleaner import (clean_base_stats, clean_breed_stats,
                              clean_pokedex_data, clean_training_stats)
from utils import CleanedPokemonDict, PokemonDict

DATA_DIR = Path("./json_data") # info input dir 
NEW_DATA_DIR = Path("./cleaned json") # info output dir 


for gen_file in os.scandir(DATA_DIR):
    gen_dict = {}
    gen_name = gen_file.name

    with open(gen_file, mode="r", encoding="utf8") as file:
        data: dict = json.load(file)

    for pokemon_name in data.keys():
        cleaned_info: CleanedPokemonDict = {}
        print(f'Cleaning {pokemon_name} info...')
        pokemon_data: PokemonDict = data[pokemon_name]

        cleaned_info["pokedex_data"] = clean_pokedex_data(pokemon_data["pokedex_data"])

        cleaned_info["base_stats"] = clean_base_stats(pokemon_data["base_stats"])

        cleaned_info["breeding"] = clean_breed_stats(pokemon_data['breeding'])

        cleaned_info["training"] = clean_training_stats(pokemon_data["training"])

        cleaned_info["pokedex_entries"] = entries_cleaner(pokemon_data["pokedex_entries"])

        cleaned_info["types_effect"] = clean_types_effect(pokemon_data["types_effect"])

        cleaned_info['img_link'] = pokemon_data ["img_link"]

        gen_dict[pokemon_name] = cleaned_info

    cleaned_file = NEW_DATA_DIR / gen_name

    with open(cleaned_file, mode='w', encoding='utf8') as file:
        json.dump(gen_dict, file, ensure_ascii=False)
