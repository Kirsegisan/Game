from settings import *

text_map = [
    'wwwwwwwwwwwwww',
    'w..w........ww',
    'w..w....w....w',
    'w............w',
    'ww........wwww',
    'w....w.......w',
    'wwwwwwwwwwwwww'
]

world_map = set()
mini_map = set()

for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'w':
            world_map.add((i * tile, j * tile))
            mini_map.add((i * map_tile, j * map_tile))
