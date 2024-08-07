import json
import os
import shutil
from pathlib import Path

from additional_data import clean_pleaces, clean_types_effect
from sections_cleaner import (clean_base_stats, clean_breed_stats,
                              clean_pokedex_data, clean_training_stats)
from utils.dirs import dir_handler

DATA_DIR = Path("./pokemon json")  # info input dir
NEW_DATA_DIR = Path("./cleaned pokemon json")  # info output dir

stats_mapper = {
    'breeding': clean_breed_stats,
    'base_stats': clean_base_stats,
    'types_effect': clean_types_effect,
    'pokédex_data': clean_pokedex_data,
    'training': clean_training_stats,
    'where_to_find': clean_pleaces
}

copy_only_stats = ['pokédex_entries', 'img_link',
                   'other_languages', 'where_to_find']


if __name__ == '__main__':
    
    dir_handler(NEW_DATA_DIR)
    for generation in DATA_DIR.iterdir():
        target_gen_dir_to_populate = NEW_DATA_DIR / generation.stem
        dir_handler(target_gen_dir_to_populate)

        # iterate through the pokemons in the generation
        for pokemon in generation.iterdir():
            current_poke_name = pokemon.stem
            print(f'Cleaning {current_poke_name} info')

            target_cleaned_poke_dir = target_gen_dir_to_populate / current_poke_name

            # check if the cleaned pokemon dir exits
            dir_handler(target_cleaned_poke_dir)

            # iterate through the pokemon info
            for stat in pokemon.iterdir():
                stat_name = stat.stem

                if stat_name in copy_only_stats:
                    shutil.copy(stat, target_cleaned_poke_dir)

                if not stat_name in stats_mapper.keys():
                    continue # in case new stats are added but the cleaner is not implemented 

                cleaner = stats_mapper[stat_name]

                # read the stat json file
                with open(stat, mode='r', encoding='utf8') as input_file:
                    raw_data = json.load(input_file)

                cleaned_info = cleaner(raw_data)
                cleaned_stat_file_path = target_cleaned_poke_dir / stat.name

                # save the cleaned data 
                with open(cleaned_stat_file_path, mode='w', encoding='utf8') as output_file:
                    json.dump(cleaned_info, output_file, ensure_ascii=False)
