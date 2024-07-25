from typing import Dict, Union

# add point
from str_cleaner import (clean_name_end, clean_name_start, format_name,
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
    result['category'] = clean_name_end(value.split('(')[1])
    result['value'] = int(value.split('(')[0])
    return result


def clean_gender(value: str) -> Dict[str, Union[int, str]]:
    values = value.split(',')
    result = {}
    for v in values:
        value, gender = [_ for _ in v.split(' ') if _]
        result[gender.lower()] = strip_value_from_unit(
            value=value, format=float)
    return result


def cath_rate(value: str) -> Dict[str, Union[int, str]]:
    result = {}
    values = value.split('(')
    result['pokemon_index'] = int(values[0])
    result['percentage'] = strip_value_from_unit(
        value=values[1].split(' ')[0], format=float
    )
    return result


if __name__ == '__main__':

    print(cath_rate(' 60 (7.8% with PokéBall, full HP) '))
