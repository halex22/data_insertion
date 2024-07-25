from typing import Dict, Union

from str_cleaner import strip_value_from_unit

test = [" 1 Sp. Atk, 1 Speed ", " 1 Atk, 1 Speed ", " 1 Speed "]
two = [" 50 (normal) ", "20 (4,884–5,140 steps) "]

def clean_name_end(value: str) -> str:
    current_index = -1
    max_index = (- len(value))
    while current_index > max_index:
        if value[current_index].isalpha():
            break
        current_index -= 1
    return value[max_index : current_index + 1 ]


def clean_name_start(value: str) -> str:
    start = 0
    max_index =  len(value)
    while start < max_index:
        if value[start].isalpha():
            break
        start += 1

    return value[start:]


def get_mame(value: str, start_index: int) -> str:
    start = start_index
    max_index = (- len(value)) if start < 0 else len(value)
    if start < 0:
        while start > max_index:
            if value[start].isalpha():
                break
            start -= 1
        return value[max_index : start +1 ]
    else:
        while start < max_index:
            if value[start].isalpha():
                break
            start += 1

        return value[start:]


def format_name(value: str) -> str:
    if value[-1] == ' ':
        value = value[:-1]
    return value.replace('.', '').replace(' ', '_')


def ev_cleaner(value: str) -> Dict[str, int]:
    improvements = value.split(',')
    return_dict: dict = {}
    for improve in improvements:
        key_name = format_name(get_mame(improve, 0))
        return_dict[key_name.lower()] = strip_value_from_unit(improve, int)
    return return_dict


def dict_with_cats(value: str) -> Dict[str, Union[int, str]]:
    """To clean base_friendship and egg clycles"""
    result = value.split('(')
    cat_name = result[1]
    return clean_name_end(cat_name)


if __name__ == '__main__':
    # for _ in test:
    #     print(ev_cleaner(_))
    for _ in two:
        print(dict_with_cats(_))
