from settings import *
import pygame
import math


class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle

    @property
    def pos(self):
        return self.x, self.y

    @staticmethod
    def shift(nitro, nitro_voz):
        nitro_zarad = nitro
        activat = nitro_voz
        keys = pygame.key.get_pressed()
        if keys[pygame.K_TAB] and activat and nitro_zarad >= 500:
            return 5, nitro_zarad - 5, False
        if not activat:
            if nitro_zarad <= 0:
                return 1, 0, True
            return 5, nitro_zarad - 5, False

        if nitro_zarad < 1000:
            return 1, nitro_zarad + 2, activat
        if nitro_zarad >= 1000:
            return 1, 1000, activat

    def movement(self, player_speed):
        keys = pygame.key.get_pressed()
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        if keys[pygame.K_w]:
            self.x += player_speed * cos_a
            self.y += player_speed * sin_a
            print('w')
        if keys[pygame.K_s]:
            self.x += -player_speed * cos_a
            self.y += -player_speed * sin_a
            print('s')
        if keys[pygame.K_a]:
            self.x += player_speed * sin_a
            self.y += -player_speed * cos_a
            print('a')
        if keys[pygame.K_d]:
            self.x += -player_speed * sin_a
            self.y += player_speed * cos_a
            print('d')
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02

    def jump(self, jump, anti_fly):
        jump_0 = 1
        jump_max = 10
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e] and anti_fly:
            if jump < jump_max:
                jump += 0.1
            if jump >= jump_max:
                anti_fly = False

        if not keys[pygame.K_e] or not anti_fly:
            if jump > jump_0:
                jump -= 0.1
                anti_fly = False
            else:
                jump = jump_0
                anti_fly = True
        return (jump, anti_fly)
