import pygame
from settings import *
from player import Player
import math
from map import world_map
from ray_casting import ray_casting
from drawing import Drwing

pygame.init()
sc = pygame.display.set_mode((width,height))
sc_map = pygame.Surface((width // map_scale, height // map_scale))
clock = pygame.time.Clock()
player = Player()
drawing = Drwing(sc, sc_map)
jump = 1 #значение растояния от земли (выше на 1/jump)
anti_fly = True #True - подпрыгиваешь или на земле, а False - в наивысшей точке прыжка или падаеш
nitro = 1000 #очки нитро (максимум)
nitro_voz = True #можно ли активировать нитро

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    jump, anti_fly = player.jump(jump, anti_fly)
    player_speed, nitro, nitro_voz = player.shift(nitro, nitro_voz)
    player.movement(player_speed)
    sc.fill(black)

    drawing.background()
    drawing.world(player.pos, player.angle, jump)
    drawing.fps(clock)
    drawing.mini_map(player)

    pygame.display.flip()
    clock.tick(FPS)
