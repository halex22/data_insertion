from int_cleaner import parse_str_to_number

test_values = ['0.6m', '1.5m']

def get_meter_value(value: str) -> float:
    return parse_str_to_number(value=value[:-1], format=float)

if __name__ == '__main__':
    for _ in test_values:
        print(get_meter_value(_))