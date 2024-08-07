import json
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class BaseCategoriesExtracter(ABC):
    pokemon_file_path: Path
    stat_name: str = field(init=False)
    root_dir = Path('./cleaned pokemon json')


    def __post_init__(self):
        self.iterate_dirs()


    def read_file(self, pokemon_file_path):
        pokemons_stat_file = pokemon_file_path / f'{self.stat_name}.json'
        with open(pokemons_stat_file, mode='r', encoding='utf8') as stat_file:
            return json.load(stat_file)


    @abstractmethod
    def append_stats_to_sets(self, stat):
        pass
    

    def iterate_dirs(self):
        for generation in self.root_dir.iterdir():
            for pokemon in generation.iterdir():
                pokemon_stats = self.read_file(pokemon)
                self.append_stats_to_sets(stat=pokemon_stats)
                break


@dataclass
class BreedingCategoriesExtractor(BaseCategoriesExtracter):
    unique_egg_group: set =  field(init=False, default_factory=set)
    unique_egg_cycles: set =  field(init=False, default_factory=set)
    stat_name = 'breeding'


    def __post_init__(self):
        super().__post_init__()



    def append_stats_to_sets(self, stat):
        current_pokemon_egg_groups = stat['egg_groups']
        for egg_group in current_pokemon_egg_groups:
            if egg_group:
                self.unique_egg_group.add(egg_group)

        current_pokemon_egg_cycles_category = stat['egg_cycles']['category']
        if current_pokemon_egg_cycles_category:
            cleaned_egg_cycles = ''.join(char for char in current_pokemon_egg_cycles_category if char.isalpha())
            self.unique_egg_cycles.add(current_pokemon_egg_cycles_category)


        print(self.unique_egg_cycles, self.unique_egg_group)

if __name__ == '__main__':
    test_path = Path('./cleaned pokemon json/gen_1/abra')
    breeding_extractor = BreedingCategoriesExtractor(pokemon_file_path=test_path)