import json
import os
from pathlib import Path

from data_clening import (clean_gender, dict_with_cats, ev_cleaner,
                          get_abilities_list, get_types_list,
                          parse_str_to_number, strip_value_from_unit)
from utils import (Breeding, CleanedBreeding, CleanedPokedexData,
                   CleanedPokemonDict, CleanedTraining, PokedexData,
                   PokemonDict, Training)
from utils.enums import BaseStats

DATA_DIR = Path("./json_data")
NEW_DATA_DIR = Path("./clean json")
# get the first file to test the code:
test_file = next(os.scandir(DATA_DIR))
new_data: CleanedPokemonDict = {}

with open(test_file, mode="r", encoding="utf8") as file:
    cleaned_info: PokemonDict = {}
    data: dict = json.load(file)
    first_pok_name = next(data.keys().__iter__())
    print(f'Cleaning {first_pok_name} info...')
    pokemon_data: PokemonDict = data[first_pok_name]

    # clean podex info
    raw_pokedex_data: PokedexData = pokemon_data.get("pokedex_data")
    cleaned_podex_data: CleanedPokedexData = {}
    cleaned_podex_data["species"] = raw_pokedex_data["species"]
    cleaned_podex_data["national"] = parse_str_to_number(
        raw_pokedex_data.get("national"), int
    )
    cleaned_podex_data["type"] = get_types_list(value=raw_pokedex_data["type"])
    cleaned_podex_data["height"] = strip_value_from_unit(
        value=raw_pokedex_data["height"].split(" ")[0], format=float
    )

    cleaned_podex_data["weight"] = strip_value_from_unit(
        value=raw_pokedex_data["weight"].split(" ")[0], format=float)

    cleaned_podex_data["abilities"] = get_abilities_list(
        raw_pokedex_data["abilities"])
    cleaned_info["pokedex_data"] = cleaned_podex_data

    # Parse base_stats to integers.
    raw_base_stats = pokemon_data.get("base_stats")
    cleaned_base_stats = {}
    for stat in BaseStats._member_names_:
        cleaned_base_stats[stat] = parse_str_to_number(
            raw_base_stats[stat], format=int)
    cleaned_info["base_stats"] = cleaned_base_stats

    # clean breeding stats
    raw_breeding_stats: Breeding = pokemon_data["breeding"]
    cleaned_breeding_stats: CleanedBreeding = {}
    cleaned_breeding_stats["egg_groups"] = get_types_list(
        value=raw_breeding_stats['egg_groups']
    )
    cleaned_breeding_stats["egg_cycles"] = dict_with_cats(
        raw_breeding_stats["egg_cycles"]
    )
    cleaned_breeding_stats["gender"] = clean_gender(
        raw_breeding_stats["gender"]
    )
    cleaned_info["breeding"] = cleaned_breeding_stats

    # training data
    raw_training_data: Training = pokemon_data['training']
    cleaned_training_data: CleanedTraining = {}
    cleaned_training_data["base_exp"] = int(raw_training_data["base_exp"])
    cleaned_training_data['base_friendship'] = dict_with_cats(
        raw_training_data["base_friendship"]
    )
    cleaned_training_data["growth_rate"] = raw_training_data['growth_rate']
    cleaned_training_data["ev_yield"] = ev_cleaner(
        raw_training_data["ev_yield"]
    )

    cleaned_info["training"] = cleaned_training_data

    print(cleaned_info)
