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

def blinker(text):
    for char in text:
        if char == ".":
            surface.fill(screenOn)
            pg.display.update()
            sleep(1)
            surface.fill(screenOff)
            pg.display.update()
        elif char == "-":
            pg.display.update()
            surface.fill(screenOn)
            sleep(3)
            surface.fill(screenOff)
            pg.display.update()
        elif char == " ": #extra on top of wait at bottom
            sleep(1)
        elif char == "/": #extra on top of wait at bottom and from spaces around /
            sleep(1)

        sleep(1) #space between . and -

        
while True: 
    surface.fill(screenOff)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

    english = translateMorse(input("Input Message: "))
    #print(english)
    #blinker(english)
    pg.display.update()

