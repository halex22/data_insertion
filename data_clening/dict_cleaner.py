from typing import Dict, Union

# add point
from .str_cleaner import (clean_name_end, clean_name_start, format_name,
                          strip_value_from_unit)


def ev_cleaner(value: str) -> Dict[str, int]:
    improvements = value.split(',')
    return_dict: dict = {}
    for improve in improvements:
        key_name = format_name(clean_name_start(improve))
        return_dict[key_name.lower()] = strip_value_from_unit(improve, int)
    return return_dict


def dict_with_cats(value: str) -> Dict[str, Union[int, str]]:
    """To clean base_friendship and egg clycles"""
    result = {}
    try:
        result['category'] = clean_name_end(value.split('(')[1])
        result['value'] = int(value.split('(')[0])
    except IndexError:
        result['category'] = None
    return result


def clean_gender(value: str) -> Dict[str, Union[int, str]]:
    values = value.split(',')
    result = {}
    for v in values:
        try:
            value, gender = [_ for _ in v.split(' ') if _]
            result[gender.lower()] = strip_value_from_unit(
                value=value, format=float)
        except ValueError:
            result['genderless'] = 100
    return result


def cath_rate(value: str) -> Dict[str, Union[int, str]]:
    result = {}
    values = value.split('(')
    result['pokemon_index'] = int(values[0])
    result['percentage'] = strip_value_from_unit(
        value=values[1].split(' ')[0], format=float
    )
    return result


def local_pokedex_cleaner(value: str) -> Dict[str, int]:
    result = {}
    values = value.split(')')[:-1]
    for _ in values:
        pokemon_index, keys = _.split('(')
        separated_kyes = [_ for _ in keys.split('/')]
        for key in separated_kyes:
            if ' — ' in key:
                parts = key.split(' — ')
                for part in parts:
                    result[part.strip()] = int(pokemon_index)
            else:
                result[key.strip()] = int(pokemon_index)
    return result


def pokedex_entry_cleaner(value: str) -> Dict[str, str]:
    ...


if __name__ == '__main__':
    local = "0144 (Red/Blue/Yellow)0235 (Gold/Silver/Crystal)0144 (FireRed/LeafGreen)0240 (HeartGold/SoulSilver)0151 (X/Y — Coastal Kalos)0144 (Let's Go Pikachu/Let's Go Eevee)0202 (The Crown Tundra)"
    # print(cath_rate(' 60 (7.8% with PokéBall, full HP) '))
    print(local_pokedex_cleaner(local))
