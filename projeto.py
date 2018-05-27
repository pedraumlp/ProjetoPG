# -*- coding: utf-8 -*-
#importação de biblotecas e classes
import pygame as pg
from pygame import *
import time
from pygame.locals import *
import os
import random
from objetos import *
from cfg import *

#inicializa o pygame
try:
    pg.init()
except:
    print("Ocorreu um erro ao iniciar o jogo")

mainMenu = True
pg.mixer.music.load(os.path.join('sound','dystopia.mp3'))
pg.mixer.music.play(-1,0.0)
pg.mixer.music.pause
gameloop = True
asura = False

#início do loop do jogo
while gameloop:
  #rotina do jogo
  #while mainMenu:
    # screen.blit(title, (0,0))
    screen.blit(lvlbg, (0,0))
    pg.mixer.music.unpause
    clock.tick(FRAMERATE)
    pg.display.flip()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gameloop = False
        if event.type == KEYDOWN and event.key == ((K_LALT or K_RALT) and K_F4):
            mainMenu = False
            gameloop = False
            pg.quit()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            screen.blit(pausescr, (0,0))
            pg.display.flip
        if event.type == KEYDOWN and event.key == K_x:
            up = True
        if event.type == KEYDOWN and event.key == K_DOWN:
            down = True
        if event.type == KEYDOWN and event.key == K_LEFT:
            left = True
        if event.type == KEYDOWN and event.key == K_RIGHT:
            right = True
        if event.type == KEYDOWN and event.key == K_c:
            charging = True
        if event.type ==KEYDOWN and event.key == K_x:
            jump = True
        if event.type == KEYDOWN and event.key == K_v:
            asura = True
        if event.type == KEYUP and event.key == K_x or K_SPACE:
            up = False
        if event.type == KEYUP and event.key == K_DOWN:
            down = False
        if event.type == KEYUP and event.key == K_RIGHT:
            right = False
        if event.type == KEYUP and event.key == K_LEFT:
            left = False
        if event.type == KEYUP and event.key == K_c:
            charging = False
        if event.type == KEYUP and event.key == K_x:
            if wallslide == True or not jump():
                jump = True
        if event.type == KEYUP and event.key == K_v:
            asura = False
    pg.time.wait(60)
    asuraF = True

pg.display.update
pg.quit()
