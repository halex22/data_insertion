from additional_data import get_abilities
from data_clening import (cath_rate, clean_gender, dict_with_cats, ev_cleaner,
                          get_abilities_list, get_types_list,
                          local_pokedex_cleaner, parse_str_to_number,
                          strip_value_from_unit)
from utils import (Breeding, CleanedBreeding, CleanedPokedexData,
                   CleanedTraining, PokedexData, Training)
from utils.enums import BaseStats


def clean_pokedex_data(raw_pokedex_data: PokedexData) -> CleanedPokedexData:
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
    cleaned_podex_data["local"] = local_pokedex_cleaner(
        raw_pokedex_data["local"]
    )
    
    return cleaned_podex_data


def clean_base_stats(raw_data: dict ) -> dict:
    cleaned_base_stats = {}
    for stat in BaseStats._member_names_:
        cleaned_base_stats[stat] = parse_str_to_number(
            raw_data[stat], format=int)
    return cleaned_base_stats


def clean_breed_stats(raw_data: Breeding) -> CleanedBreeding:
    cleaned_breeding_stats: CleanedBreeding = {}
    cleaned_breeding_stats["egg_groups"] = get_types_list(
        value=raw_data['egg_groups']
    )
    cleaned_breeding_stats["egg_cycles"] = dict_with_cats(
        raw_data["egg_cycles"]
    )
    cleaned_breeding_stats["gender"] = clean_gender(
        raw_data["gender"]
    )
    return cleaned_breeding_stats


def clean_training_stats(raw_data: Training) -> CleanedTraining:
    cleaned_training_data: CleanedTraining = {} 
    cleaned_training_data["base_exp"] = (
        lambda val: val if isinstance(val, int) else 0
    )(raw_data["base_exp"])
    # cleaned_training_data["base_exp"] = int(raw_data["base_exp"])
    cleaned_training_data['base_friendship'] = dict_with_cats(
        raw_data["base_friendship"]
    )
    cleaned_training_data["growth_rate"] = raw_data['growth_rate']
    cleaned_training_data["ev_yield"] = ev_cleaner(
        raw_data["ev_yield"]
    )
    cleaned_training_data["catch_rate"] = cath_rate(
        value=raw_data["catch_rate"]
    )
    return cleaned_training_data

