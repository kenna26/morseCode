from time import sleep
import pygame as pg
from pygame import *
import sys
import morseCode
from morseCode import translateMorse
pg.init()

screenOn = (225, 225, 225)
screenOff = (0, 0, 0)

surface = pg.display.set_mode((400, 400))
surface.fill(screenOff)


#first value in list is always on

def blinker(text):
    blinkerList = []
    for char in text:
        if char == ".":
            blinkerList.append(1)
        elif char == "-":
            pg.display.update()
            surface.fill(screenOn)
            clock.tick(FPS)
            surface.fill(screenOff)
            pg.display.update()
        elif char == " ": #extra on top of wait at bottom
            clock.tick(FPS)
        elif char == "/": #extra on top of wait at bottom and from spaces around /
            clock.tick(FPS)

    clock.tick(FPS) #space between . and -


clock = pg.time.Clock()

FPS = 3
    
running = True


while running: 
    pg.display.update()
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

pg.quit()


