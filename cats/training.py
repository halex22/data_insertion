from dataclasses import dataclass, field

from base import BaseCategoriesExtracter


@dataclass
class TraningCategoriesExtractor(BaseCategoriesExtracter):
    stat_name = 'training'
    unique_base_friendship_categories: set = field(init=False, default_factory=set)
    unique_growth_rate: set = field(init=False, default_factory=set)

    def populate_unique_dict(self) -> None:
        self.unique_stats_categories['growth_rate'] = list(self.unique_growth_rate)
        self.unique_stats_categories['base_friendship'] = list(self.unique_base_friendship_categories)


    def append_stats_to_sets(self, stat):

        current_pokemon_base_friendship = stat['base_friendship']['category']
        if current_pokemon_base_friendship:
            self.unique_base_friendship_categories.add(current_pokemon_base_friendship)

        current_pokemon_growth_rate = stat['growth_rate']
        self.unique_growth_rate.add(current_pokemon_growth_rate)


if __name__ == '__main__':
    training_extractor = TraningCategoriesExtractor()
    training_extractor.save_unique_stats_categories()

