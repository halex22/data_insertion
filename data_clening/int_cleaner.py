from typing import List, Union


def parse_str_to_number(value: str, format: Union[int, float]) -> Union[int, float]:
    if value.isalpha():
        return 0
    return format(value)

