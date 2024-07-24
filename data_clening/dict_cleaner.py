from typing import Dict, TypeAlias

from str_cleaner import strip_value_from_unit

test = [" 1 Sp. Atk, 1 Speed ", " 1 Atk, 1 Speed ", " 1 Speed "]


def get_mame(value: str) -> str:
    start = 0
    max_index = len(value)
    while start < max_index:
        if value[start].isalpha():
            break
        start += 1

    return value[start:]


def ev_cleaner(value: str) -> Dict[str, int]:
    improvements = value.split(',')
    return_dict: dict = {}
    for improve in improvements:
        return_dict[get_mame(improve)] = strip_value_from_unit(improve, int)
    return return_dict


if __name__ == '__main__':
    for _ in test:
        print(ev_cleaner(_))
