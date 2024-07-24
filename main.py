import json
import os
from pathlib import Path

from data_clening import (get_abilities_list, get_types_list,
                          parse_str_to_number, strip_value_from_unit)
from utils import PokedexData, PokemonDict
from utils.enums import BaseStats

DATA_DIR = Path("./json_data")
NEW_DATA_DIR = Path("./clean json")
# get the first file to test the code:
test_file = next(os.scandir(DATA_DIR))
new_data = {}

with open(test_file, mode="r", encoding="utf8") as file:
    cleaned_info: PokemonDict = {}
    data: dict = json.load(file)
    first_pok_name = next(data.keys().__iter__())
    print(first_pok_name)
    pokemon_data: PokemonDict = data[first_pok_name]
    # print(pokemon_data)

    # clean podex info
    raw_pokedex_data: PokedexData = pokemon_data.get("pokedex_data")
    cleaned_podex_data: PokedexData = {}
    cleaned_podex_data["species"] = raw_pokedex_data["species"]
    cleaned_podex_data["national"] = parse_str_to_number(
        raw_pokedex_data.get("national"), int
    )
    cleaned_podex_data["type"] = get_types_list(value=raw_pokedex_data["type"])
    cleaned_podex_data["height"] = strip_value_from_unit(
        value=raw_pokedex_data["height"].split(" ")[0], format=float
    )

    cleaned_podex_data["weight"] = strip_value_from_unit(
        value=raw_pokedex_data["weight"], format=float)

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

    print(cleaned_info)
