from typing import List, Union

from .str_cleaner import clean_name_egg_group

test_values = ['Poison ', ' Ice Flying ', ' Psychic ']
abilities =  "1. Synchronize2. Inner FocusMagic Guard (hidden ability)"
eggs = ['Bug,', 'Water', '1']


def get_types_list(value: str) -> Union[List[str], List[Union[str, None]]]:
    splited_values = [_ for _ in value.split(' ') if _ != '']
    if len(splited_values) < 2:
        splited_values.append(None)
    return splited_values

def get_abilities_list(value: str) -> List[str]:
    abilities = value.split('.')[1:] # so the first number is exclued in the array
    if len(abilities) > 1:
        abilities[0] = abilities[0][:-1] # so the number at the end of the 0 index in exluced
    return abilities


def clean_egg_group(groups: List[str]) -> List[str]:
    cleaned_eggs = [clean_name_egg_group(group) for group in groups if group is not None and  len(group) > 2 ]
    return cleaned_eggs



if __name__ == '__main__':
    print(clean_egg_group(eggs))
    # print(get_abilities_list(abilities))
    # for _ in test_values:
    #     print(get_types_list(_))
