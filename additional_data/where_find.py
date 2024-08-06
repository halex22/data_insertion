
def append_route_prefix(place: str) -> str:
    """Appends the `Route` prefix to the number

    Args:
        place (str): place to find the pokemon

    Returns:
        str: Place with the prefixed if needed
    """
    try:
        return f'Route {int(place)}'
    except ValueError:
        return place


def clean_game_info(value: str) -> dict:
    places = value.split(',')
    return [append_route_prefix(_) for _ in places]


def clean_pleaces(data: dict) -> dict:
    cleaned_data = {}
    for pokemon_game, info in data.items():
        cleaned_data[pokemon_game] = clean_game_info(value=info)
    return cleaned_data
