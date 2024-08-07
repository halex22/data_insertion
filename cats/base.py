import json
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class BaseCategoriesExtracter(ABC):
    stat_name: str = field(init=False)
    _root_dir = Path('./cleaned pokemon json')
    outpit_dir = Path('./cats/categories')
    unique_stats_categories: dict = field(init= False, default_factory=dict) 


    def __post_init__(self):
        self.iterate_dirs()


    def read_file(self, pokemon_file_path: Path) -> dict:
        """Reads the stat info for the pokemon at the fiven path

        Args:
            pokemon_file_path (Path): Path where the stat are located

        Returns:
            dict: dictionary from the json loaded data
        """
        pokemons_stat_file = pokemon_file_path / f'{self.stat_name}.json'
        with open(pokemons_stat_file, mode='r', encoding='utf8') as stat_file:
            return json.load(stat_file)


    @abstractmethod
    def append_stats_to_sets(self, stat):
        raise NotImplementedError
    

    def save_unique_stats_categories(self) -> None:
        """Saves the uniques categories for the stat into a json file"""
        destination_file_path = self.outpit_dir / f'{self.stat_name}.json'
        self.populate_unique_dict()
        print(self.unique_stats_categories)
        with open(destination_file_path, mode='w', encoding='utf8') as output_file:
            json.dump(self.unique_stats_categories, output_file, ensure_ascii=False)
        

    @abstractmethod
    def populate_unique_dict(self) -> None:
        raise NotImplementedError
    

    def iterate_dirs(self) -> None:
        """Processes the reading and population of the unique categories stats"""
        for generation in self._root_dir.iterdir():
            for pokemon in generation.iterdir():
                pokemon_stats = self.read_file(pokemon)
                self.append_stats_to_sets(stat=pokemon_stats)

