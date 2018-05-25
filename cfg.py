# -*- coding: utf-8 -*-
import pygame as pg
import os

#configurações de resolução de tela, cores e taxa de quadros
largura = 1280
altura = 720
RESOLUCAO = (largura,altura)
FRAMERATE = 60
screen = pg.display.set_mode(RESOLUCAO)
pg.display.set_caption("Megaman X Pygame")
clock = pg.time.Clock()
tempo = pg.time.get_ticks()
pg.mouse.set_visible(0)
key = pg.key.get_pressed()
gameloop = True
hp = 100

#carrega imagens
title = pg.image.load(os.path.join("tex","title.jpg")).convert()
lvlbg = pg.image.load(os.path.join("tex","dystopia.jpg")).convert()
pausescr = pg.image.load(os.path.join("tex","pause.jpg")).convert()
initX = pg.image.load(os.path.join("tex","X","idlexR.png")).convert()
linitX = pg.image.load(os.path.join("tex","X","idlexL.png")).convert()
rdashX = pg.image.load(os.path.join("tex","X","RdashX.png")).convert()
ldashX = pg.image.load(os.path.join("tex","X","LdashX.png")).convert()
rcrouchX = pg.image.load(os.path.join("tex","X","Rcrouch.png")).convert()
lcrouchX = pg.image.load(os.path.join("tex","X","Lcrouch.png")).convert()
rwalkstart = pg.image.load(os.path.join("tex","X","rwalkSX.png")).convert()
lwalkstart = pg.image.load(os.path.join("tex","X","lwalkSX.png")).convert()
lwalkX1 = pg.image.load(os.path.join("tex","X","lwalkX1.png")).convert()
lwalkX2 = pg.image.load(os.path.join("tex","X","lwalkX2.png")).convert()
lwalkX3 = pg.image.load(os.path.join("tex","X","lwalkX3.png")).convert()
lwalkX4 = pg.image.load(os.path.join("tex","X","lwalkX4.png")).convert()
lwalkX5 = pg.image.load(os.path.join("tex","X","lwalkX5.png")).convert()
lwalkX6 = pg.image.load(os.path.join("tex","X","lwalkX6.png")).convert()
rwalkX1 = pg.image.load(os.path.join("tex","X","rwalkX1.png")).convert()
rwalkX2 = pg.image.load(os.path.join("tex","X","rwalkX2.png")).convert()
rwalkX3 = pg.image.load(os.path.join("tex","X","rwalkX3.png")).convert()
rwalkX4 = pg.image.load(os.path.join("tex","X","rwalkX4.png")).convert()
rwalkX5 = pg.image.load(os.path.join("tex","X","rwalkX5.png")).convert()
rwalkX6 = pg.image.load(os.path.join("tex","X","rwalkX6.png")).convert()
rshootingX = pg.image.load(os.path.join("tex","X","shootxR.png")).convert()
lshootingX = pg.image.load(os.path.join("tex","X","shootxL.png")).convert()
spawn1 = pg.image.load(os.path.join("tex","X","spawn1.png")).convert()
spawn2 = pg.image.load(os.path.join("tex","X","spawn2.png")).convert()
spawn3 = pg.image.load(os.path.join("tex","X","spawn3.png")).convert()
spawn4 = pg.image.load(os.path.join("tex","X","spawn4.png")).convert()
lwalkloopX = [lwalkstart,lwalkX1,lwalkX2,lwalkX3,lwalkX4,lwalkX5,lwalkX6]
rwalkloopX = [rwalkstart,rwalkX1,rwalkX2,rwalkX3,rwalkX4,rwalkX5,rwalkX6]
spawnX = [spawn1,spawn2,spawn3,spawn4,initX]

#variáveis de posicionamento do personagem e câmera
x = 5
y = 10

#tuplas de cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
