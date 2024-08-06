import json
from pathlib import Path
from typing import List, Optional

path_test = Path('./json_data')

test_batch = False


def strip_hidden(ability: str):
    mover = 1
    while mover < len(ability):
        if ability[mover].isupper():
            if ability[mover - 1] != ' ':
                break
        mover += 1
    return [ability[:mover], ability[mover:]]


def handle_multi_abilities(abilties_array: list) -> list:
    abilties_array[0] = abilties_array[0][:-1].strip()
    if abilties_array[-1][-1] == ')':
        cleaned_abilities = strip_hidden(ability=abilties_array[-1].strip())
        abilties_array = [abilties_array[0], *cleaned_abilities]
    return abilties_array


def populate_dict(abilities: list) -> dict:
    abilities_dict = {'normal': [], 'hidden': ''}
    for ability in abilities:
        if ability[-1] == ')':
            abilities_dict['hidden'] = ability.split('(')[0].strip()
        else:
            abilities_dict['normal'].append(ability)
    return abilities_dict


def get_abilities(data: str):
    abilities = data.split('.')[1:]
    if len(abilities) > 1:
        abilities = handle_multi_abilities(abilities)
    if abilities[0][-1] == ")":
        abilities = strip_hidden(ability=abilities[0].strip())
    return populate_dict(abilities=abilities)


if __name__ == '__main__':
    if test_batch:
        ...

    else:
        test_gen = next(path_test.iterdir())
        with open(test_gen, mode='r', encoding='utf8') as file:
            data: dict = json.load(file)

        for pokemon_name in data.keys():
            pokemon_data = data[pokemon_name]
            print(get_abilities(pokemon_data['pokedex_data']['abilities']))
