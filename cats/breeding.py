from dataclasses import dataclass, field

from base import BaseCategoriesExtracter


@dataclass
class BreedingCategoriesExtractor(BaseCategoriesExtracter):
    unique_egg_group: set =  field(init=False, default_factory=set)
    unique_egg_cycles: set =  field(init=False, default_factory=set)
    stat_name = 'breeding'


    def append_stats_to_sets(self, stat):
        current_pokemon_egg_groups = stat['egg_groups']
        for egg_group in current_pokemon_egg_groups:
            if egg_group:
                self.unique_egg_group.add(egg_group)

        current_pokemon_egg_cycles_category = stat['egg_cycles']['category']
        if current_pokemon_egg_cycles_category:
            self.unique_egg_cycles.add(current_pokemon_egg_cycles_category)

    
    def populate_unique_dict(self) -> None:
        self.unique_stats_categories['egg_cycles'] = list(self.unique_egg_cycles)
        self.unique_stats_categories['egg_groups'] = list(self.unique_egg_group)


if __name__ == '__main__':
    breeding_extractor = BreedingCategoriesExtractor()
    breeding_extractor.save_unique_stats_categories()