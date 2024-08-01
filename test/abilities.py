import json
from pathlib import Path

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


def get_abilities(data: str):
    abilities = data.split('.')[1:]
    if len(abilities) > 1:
        abilities = handle_multi_abilities(abilities)
    if abilities[0][-1] == ")":
        abilities = strip_hidden(ability=abilities[0].strip())
    return abilities


if test_batch:
    ...

else:
    test_gen = next(path_test.iterdir())
    with open(test_gen, mode='r', encoding='utf8') as file:
        data: dict = json.load(file)

    for pokemon_name in data.keys():
        pokemon_data = data[pokemon_name]
        print(get_abilities(pokemon_data['pokedex_data']['abilities']))
