import json
from pathlib import Path

effect_mapper = {
    '': 1.0,
    '½': 0.5,
    '¼': 0.25,
    '1½': 1.5
}


def clean_types_effect(data: dict):
    for type in data.values():
        for key, value in type.items():
            try:
                type[key] = float(value)
            except ValueError:
                type[key] = effect_mapper[value]
    return data


if __name__ == '__main__':
    test_path = Path('./json_data/gen_1.json')

    test_batch = True

    with open (test_path, mode='r', encoding='utf8') as file:
        data:dict = json.load(file)

    if test_batch:
        for pokemon_name in data.keys():
            pokemon = data[pokemon_name]['types_effect']
            print(clean_types_effect(pokemon))

    else:
        pokemon_name = next(data.keys().__iter__())

        pokemon = data[pokemon_name]['types_effect']
        print(clean_types_effect(pokemon))
