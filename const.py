# coding=utf-8
import pygame
import os
# Файл констант


LENGTH_ENEMY = 52
WIDTH_ENEMY = 35

LENGTH_ENEMY_SHOOTING = 51
WIDTH_ENEMY_SHOOTING = 61

LENGTH_SHOOTING_ENEMY = 15
WIDTH_SHOOTING_ENEMY = 25


LENGTH_PLAYER = 95
WIDTH_PLAYER = 89


LENGTH_SHOOTING = 17
WIDTH_SHOOTING = 12


LENGTH_EXPLOSION = 64
WIDTH_EXPLOSION = 60


WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 750

INIT_ENERGY = 100

DISPLAYMODE = (WINDOW_WIDTH, WINDOW_HEIGHT)
FPS = 40
RATE_ENEMY_SPEED = 2
DELAY_EXPLOSION = 5
MAX_NUMBER_ENEMY = 5
RATE_PLAYER_SPEED = 3

COUNT_SHOOTING = 50
COUNT_ENEMY = 10
window = pygame.display.set_mode(DISPLAYMODE)

