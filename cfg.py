# -*- coding: utf-8 -*-
import pygame as pg
import os
import objetos
from objetos import *

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

#carrega imagens
title = pg.image.load(os.path.join("tex","title.jpg")).convert()
lvlbg = pg.image.load(os.path.join("tex","centralhighway.jpg")).convert()
ground = pg.image.load(os.path.join("tex","surface.jpg")).convert()
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
gameover = pg.image.load(os.path.join("tex","gameover.jpg")).convert()
rshootingX = pg.image.load(os.path.join("tex","X","shootxR.png")).convert()
lshootingX = pg.image.load(os.path.join("tex","X","shootxL.png")).convert()
lwalkShootX1 = pg.image.load(os.path.join("tex","X","walkshootL1.png")).convert()
ldashshot = pg.image.load(os.path.join("tex","X","Lshootdash.png")).convert()
rdashshot = pg.image.load(os.path.join("tex","X","Rshootdash.png")).convert()
lwalkShootX2 = pg.image.load(os.path.join("tex","X","walkshootL2.png")).convert()
lwalkShootX3 = pg.image.load(os.path.join("tex","X","walkshootL3.png")).convert()
lwalkShootX4 = pg.image.load(os.path.join("tex","X","walkshootL4.png")).convert()
lwalkShootX5 = pg.image.load(os.path.join("tex","X","walkshootL5.png")).convert()
lwalkShootX6 = pg.image.load(os.path.join("tex","X","walkshootL6.png")).convert()
rwalkShootX1 = pg.image.load(os.path.join("tex","X","walkshootR1.png")).convert()
rwalkShootX2 = pg.image.load(os.path.join("tex","X","walkshootR2.png")).convert()
rwalkShootX3 = pg.image.load(os.path.join("tex","X","walkshootR3.png")).convert()
rwalkShootX4 = pg.image.load(os.path.join("tex","X","walkshootR4.png")).convert()
rwalkShootX5 = pg.image.load(os.path.join("tex","X","walkshootR5.png")).convert()
rwalkShootX6 = pg.image.load(os.path.join("tex","X","walkshootR6.png")).convert()
spawn1 = pg.image.load(os.path.join("tex","X","spawn1.png")).convert()
spawn2 = pg.image.load(os.path.join("tex","X","spawn2.png")).convert()
spawn3 = pg.image.load(os.path.join("tex","X","spawn3.png")).convert()
spawn4 = pg.image.load(os.path.join("tex","X","spawn4.png")).convert()
ljump1 = pg.image.load(os.path.join("tex","X","ljump1.png")).convert()
ljump2 = pg.image.load(os.path.join("tex","X","ljump2.png")).convert()
rjump1 = pg.image.load(os.path.join("tex","X","rjump1.png")).convert()
rjump2 = pg.image.load(os.path.join("tex","X","rjump2.png")).convert()
ljumpfire1 = pg.image.load(os.path.join("tex","X","ljumpfire1.png")).convert()
ljumpfire2 = pg.image.load(os.path.join("tex","X","ljumpfire2.png")).convert()
rjumpfire1 = pg.image.load(os.path.join("tex","X","rjumpfire1.png")).convert()
rjumpfire2 = pg.image.load(os.path.join("tex","X","rjumpfire2.png")).convert()
asuraRight = pg.image.load(os.path.join("tex","X","asuraFistR.png")).convert()
asuraLeft = pg.image.load(os.path.join("tex","X","asuraFistL.png")).convert()
asuraFireLeft = pg.image.load(os.path.join("tex","X","asuraFireL.png")).convert()
asuraFireRight = pg.image.load(os.path.join("tex","X","asuraFireR.png")).convert()
rvictory = pg.image.load(os.path.join("tex","X","Rvictory.png")).convert()
lvictory = pg.image.load(os.path.join("tex","X","Lvictory.png")).convert()
lwalkloopX = [lwalkstart,lwalkX1,lwalkX2,lwalkX3,lwalkX4,lwalkX5,lwalkX6]
rwalkloopX = [rwalkstart,rwalkX1,rwalkX2,rwalkX3,rwalkX4,rwalkX5,rwalkX6]
lsigmaidle = pg.image.load(os.path.join("tex","enemies","Lsigmaidle.png")).convert()
rsigmaidle = pg.image.load(os.path.join("tex","enemies","Rsigmaidle.png")).convert()
lwalkshootloopX = [lwalkShootX1, lwalkShootX2, lwalkShootX3, lwalkShootX4, lwalkShootX5, lwalkShootX6]
rwalkshootloopX = [rwalkShootX1, rwalkShootX2, rwalkShootX3, rwalkShootX4, rwalkShootX5, rwalkShootX6]
spawnX = [spawn1, spawn2, spawn3, spawn4, initX]
#gravidade

#tuplas de cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
