from typing import Callable, Union

from int_cleaner import parse_str_to_number

test_values = ['0.6m', '1.5m']

def get_meter_value(value: str) -> float:
    strip_value_from_unit(value=value)
    return parse_str_to_number(value=value[:-1], format=float)


def strip_value_from_unit(value: str, format: Callable[[str], Union[int, float]])-> str:
    end = len(value)
    has_found_number = False
    while not has_found_number:
        if value[end - 1].isnumeric():
            has_found_number = True
            break
        end -= 1
    return format(value[:end])


if __name__ == '__main__':
    for _ in test_values:
        print(strip_value_from_unit(_, float))