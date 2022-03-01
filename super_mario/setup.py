import os
import pygame as pg
import tools

pg.init()
pg.display.set_caption('super mario')
SCREEN=pg.display.set_mode((600,800))
SCREEN_RECT=SCREEN.get_rect()

GFX=tools.load_all_gfx('resources/graphics')
