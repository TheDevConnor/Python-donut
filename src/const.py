import pygame as pg

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

white = (255, 255, 255)
black = (0, 0, 0)
hue   = 0

theta_spacing = 10
phi_spacing = 1

fps = 75

chars = ".,-~:;=!*#$@"


""" The startign position of the donut """
x_start, y_start = 0, 0

x_separator = 10
y_separator = 20

# The background
bg = '../assets/Subscribe!/bg.jpg'