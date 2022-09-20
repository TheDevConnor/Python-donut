import pygame as pg
import const as c

import colorsys
import math

# Import everythiong from const.py
WIDTH = c.SCREEN_WIDTH
HEIGHT = c.SCREEN_HEIGHT

chars = c.chars

screen = c.screen
white = c.white
black = c.black
hue = c.hue

theta_spacing = c.theta_spacing
phi_spacing = c.phi_spacing

x_start, y_start = c.x_start, c.y_start
x_separator = c.x_separator
y_separator = c.y_separator

bg = c.bg

fps = c.fps

fps_clock = pg.time.Clock()

pg.init()
pg.font.init()

rows = HEIGHT // y_separator
cols = WIDTH // x_separator
screen_size = rows * cols

x_offset = cols / 2
y_offset = rows / 2

A, B = 0, 0

# This screen function is done over in the const.py file
screen

display_surface = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Spining Donut")
font = pg.font.Font('freesansbold.ttf', 18, bold=True)

def hsv_two_rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v)) 

def text_display(letter, x_start, y_start):
    text = font.render(str(letter), True, hsv_two_rgb(hue, 1, 1))
    display_surface.blit(text, (x_start, y_start))

running = True
while running:
    fps_clock.tick(fps)
    pg.display.update()

    screen.fill(black)
    # screen.blit(pg.image.load(bg), (0, 0))

    z = [0] * screen_size # Donut. Fills donut space
    b = [''] * screen_size # Background. Fills empty space

    for j in range(0, 628, theta_spacing): # From 0 to 2pi
        for i in range(0, 628, phi_spacing): # From 0 to 2pi
            c = math.sin(i) # Sin of i
            d = math.cos(j) # Cos of j 
            e = math.sin(A) # Sin of A
            f = math.sin(j) # Sin of j
            g = math.cos(A) # Cos of A

            h = d + 2 
            D = 1 / (c * h * e + f * g + 5)

            l = math.cos(i) # Cos of i
            m = math.cos(B) # Cos of B
            n = math.sin(B) # Sin of B

            t = c * h * g - f * e

            x = int(x_offset + 40 * D * (l * h * m - t * n)) # 3D x coordinate after roatation
            y = int(y_offset + 20 * D * (l * h * n + t * m)) # 3D y coordinate after roatation
            o = int(x + cols * y) # 1D coordinate
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n)) # 3D z coordinate after rotation

            if rows > y and y > 0 and x > 0 and cols > x and D > z[o]:
                z[o] = D
                b[o] = chars[N if N > 0 else 0]

        if y_start == rows * y_separator - y_separator:
            y_start = 0

        for i in range(len(b)):
            A += 0.000002 # for the faster roataion change to bigger number
            B += 0.000001 # for the faster roataion change to bigger number

            if i == 0 or i % cols:
                text_display(b[i], x_start, y_start)
                x_start += x_separator
            else:
                y_start += y_separator
                x_start = 0
                text_display(b[i], x_start, y_start)
                x_start += x_separator

        hue += 0.005

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False