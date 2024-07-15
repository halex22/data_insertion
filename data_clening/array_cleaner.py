from typing import List, Union

test_values = ['Poison ', ' Ice Flying ', ' Psychic ']

def get_types_list(value: str) -> Union[List[str], List[Union[str, None]]]:
    splited_values = [_ for _ in value.split(' ') if _ != '']
    if splited_values.__len__() < 2:
        splited_values.append(None)
    print(splited_values)

for _ in test_values:
    get_types_list(_)
