from functools import lru_cache
from typing import Callable, Union


def strip_value_from_unit(value: str, format: Callable[[str], Union[int, float]]) -> str:
    end = len(value)
    has_found_number = False
    while not has_found_number:
        if value[end - 1].isnumeric():
            has_found_number = True
            break
        end -= 1
    return format(value[:end])


def clean_name_end(value: str) -> str:
    """Removes not alpha character at the end"""
    current_index = -1
    max_index = (- len(value))
    while current_index > max_index:
        if value[current_index].isalpha():
            break
        current_index -= 1
    return value[max_index: current_index + 1]


def clean_name_start(value: str) -> str:
    """Removes non alpha characters at the beggining"""
    start = 0
    max_index = len(value)
    while start < max_index:
        if value[start].isalpha():
            break
        start += 1

    return value[start:]


def format_name(value: str) -> str:
    """Simple function to remove blank ppaces and dots"""
    if value[-1] == ' ':
        value = value[:-1]
    return value.replace('.', '').replace(' ', '_')


@lru_cache
def clean_name_egg_group(value: str) -> str:
    if not value[-1].isalpha():
        return value[:-1]
    return value


if __name__ == '__main__':
    print(clean_name_egg_group('bug,'))
