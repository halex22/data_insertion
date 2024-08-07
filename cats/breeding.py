import json
from abc import ABC
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class BaseCategoriesExtracter(ABC):
    pokemon_file_path: Path
    stat_name: str = field(init=False)
    stats: dict = field(init=False, default_factory=dict)

    def __post_init__(self):
        print('parent')
        self.read_file()


    def read_file(self):
        pokemons_stat_file = self.pokemon_file_path / f'{self.stat_name}.json'
        with open(pokemons_stat_file, mode='r', encoding='utf8') as stat_file:
            self.stats = json.load(stat_file)


@dataclass
class BreedingCategoriesExtractor(BaseCategoriesExtracter):
    unique_egg_group: set =  field(init=False, default_factory=set)
    unique_egg_cycles: set =  field(init=False, default_factory=set)
    stat_name = 'breeding'

    def __post_init__(self):
        super().__post_init__()


    def extract_unique_egg_group(self):
        ...


if __name__ == '__main__':
    test_path = Path('./cleaned pokemon json/gen_1/abra')
    breeding_extractor = BreedingCategoriesExtractor(pokemon_file_path=test_path)