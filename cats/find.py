from dataclasses import dataclass, field
from typing import Set

from base import BaseCategoriesExtracter


@dataclass
class FindCategoriesExtractor(BaseCategoriesExtracter):
    stat_name = 'where_to_find'
    unique_places: Set[str] = field(init=False, default_factory=set)
    unique_games: Set[str] = field(init=False, default_factory=set)

    def populate_unique_dict(self) -> None:
        self.unique_stats_categories['games'] = list(self.unique_games)
        self.unique_stats_categories['places'] = list(self.unique_places)


    def append_stats_to_sets(self, stat: dict):
        
        for places in stat.values():
            for place in places:
                self.unique_places.add(place.strip())
        
        for game in stat.keys():
            self.unique_games.add(game)


if __name__ == '__main__':
    find = FindCategoriesExtractor()
    find.save_unique_stats_categories()

