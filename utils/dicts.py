from typing import Dict, List, TypedDict, Union


class PokedexData(TypedDict):
    national: str
    type: str
    species: str
    height: str
    weight: str
    abilities: str
    local: str


class CleanedPokedexData(TypedDict):
    national: int
    type: List[Union[str, None]]
    species: str
    height: float
    weight: float
    abilities: List[str]
    local: str


class Training(TypedDict):
    ev_yield: str
    catch_rate: str
    base_friendship: str
    base_exp: str
    growth_rate: str


class CleanedTraining(TypedDict):
    ev_yield: Dict[str, int]
    catch_rate: str
    base_friendship: int
    base_exp: int
    growth_rate: str


class Breeding(TypedDict):
    egg_groups: str
    gender: str
    egg_cycles: str


class CleanedBreeding(TypedDict):
    egg_groups: List[str]
    gender: List[float]
    egg_cycles: str


class PokemonDict(TypedDict):
    pokedex_data: PokedexData
    base_stats: str
    training: Training
    breeding: Breeding
    pokedex_entries: str


class CleanedPokemonDict(TypedDict):
    pokedex_data: CleanedPokedexData
    base_stats: str
    trainig: CleanedTraining
    breeding: CleanedBreeding
    pokedex_entries: str
