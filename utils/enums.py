from enum import StrEnum, auto


class PokedexData(StrEnum):
    national = auto()
    type = auto()
    species = auto()
    height = auto()
    weight = auto()
    abilities = auto()
    local = auto()


class BaseStats(StrEnum):
    hp = auto()
    attack = auto()
    defense = auto()
    sp_atk = auto()
    sp_def = auto()
    speed = auto()
