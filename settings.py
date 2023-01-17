import math

# game
width = 1400
height = 700
half_width = width // 2
half_height = height // 2
FPS = 120
tile = 100
fps_pos = (width - 65, 5)

# ray casting
fov = math.pi / 3
half_fov = fov / 2
num_rays = 700
max_depth = 700
delta_angle = fov / num_rays
dist = num_rays / (2 * math.tan(half_fov))
proj_coeff = dist * tile
scale = width // num_rays

# player
player_pos = (half_width, half_height)
player_angle = 0

# color
white = (255, 255, 255)
black = (0, 0, 0)
red = (220, 0, 0)
green = (70, 120, 50)
blue = (0, 0, 220)
darkgray = (110, 110, 110)
purple = (120, 0, 120)
skyblue = (0, 50, 155)
yellow = (220, 220, 0)

# mini_map
map_scale = 5
map_tile = tile // map_scale
map_pos = (0, height // map_scale - height // map_scale)
