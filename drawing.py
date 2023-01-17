import pygame
from settings import *
from ray_casting import ray_casting
from map import mini_map

class Drwing:
    def __init__(self, sc, sc_map):
        self.sc = sc
        self.sc_map = sc_map
        self.font = pygame.font.SysFont('Arial', 36, bold=True)

    def background(self):
        pygame.draw.rect(self.sc, skyblue, (0, 0, width, half_height))
        pygame.draw.rect(self.sc, green, (0, half_height, width, half_height))

    def world(self, player_pos, player_angle, jump):
        ray_casting(self.sc, player_pos, player_angle, jump)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        renger = self.font.render(display_fps, 0, red)
        self.sc.blit(renger, fps_pos)

    def mini_map(self, player):
        self.sc_map.fill(black)
        map_x, map_y = player.x // map_scale, player.y // map_scale
        pygame.draw.circle(self.sc_map, red, (int(map_x),int(map_y)), 7)
        pygame.draw.line(self.sc_map, yellow, (map_x, map_y), (map_x + 20 * math.cos(player.angle),
                                                  map_y + 20 * math.sin(player.angle)), 2)
        for x, y in mini_map:
            pygame.draw.rect(self.sc_map, green, (x, y, map_tile, map_tile))
        self.sc.blit(self.sc_map, map_pos)