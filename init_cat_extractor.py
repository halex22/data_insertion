from pathlib import Path

INPUT_DIR = Path('./cleaned pokemon json')

egg_group = []

print(INPUT_DIR)

if __name__ == '__main__':
    
    for generation in INPUT_DIR.iterdir():
        print(generation)
