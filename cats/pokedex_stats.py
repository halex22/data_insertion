from dataclasses import dataclass, field
from typing import Dict, List, Union

from base import BaseCategoriesExtracter


@dataclass
class PokedexDataExtractor(BaseCategoriesExtracter):
    stat_name = 'pokédex_data'
    unique_species: set = field(init=False, default_factory=set)
    unique_abilities: set = field(init=False, default_factory=set)
    unique_local_pokedex_name: set = field(init=False, default_factory=set)
    unique_types: set = field(init=False, default_factory=set)


    def populate_unique_dict(self) -> None:
        self.unique_stats_categories['types'] = list(self.unique_types)
        self.unique_stats_categories['abilities'] = list(self.unique_abilities)
        self.unique_stats_categories['local_pokedex'] = list(self.unique_local_pokedex_name)
        self.unique_stats_categories['species'] = list(self.unique_species)


    def append_stats_to_sets(self, stat):

        current_pokemon_types = stat['type']
        for type in current_pokemon_types:
            if type:
                self.unique_types.add(type.lower())


        current_pokemon_abilities: Dict[str, Union[List[str], str]] = stat['abilities']
        for ability in current_pokemon_abilities['normal']:
            if ability:
                self.unique_abilities.add(ability.strip())
        self.unique_abilities.add(current_pokemon_abilities['hidden'].strip())

        current_pokemon_species = stat['species']
        self.unique_species.add(current_pokemon_species)

        current_pokemon_local_pokedex: dict = stat['local']
        for game in current_pokemon_local_pokedex.keys():
            self.unique_local_pokedex_name.add(game)
    

if __name__ == '__main__':
    pokedex_data_cleaner = PokedexDataExtractor()
    pokedex_data_cleaner.save_unique_stats_categories()