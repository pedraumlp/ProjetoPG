# -*- coding: utf-8 -*-
#importação de biblotecas e classes
import pygame as pg
from pygame import *
import time
from pygame.locals import *
import os
import random

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


class ground(object):
    self.tex = ground
    self.y = 604
    self.sup = Surface(self.tex(2604,116))
    Surface.blit(self.sup(0,self.y))

class Player(object):
    def __init__(self):
        self.mmX = Surface((largura/4,altura/8,53),pg.SRCALPHA)
        self.x = 5
        self.y = ground.y
        self.hp = 50
        self.dmg = 5
        Player.score += pg.time.get_ticks()/10**3
        self.hitbox = Rect(self.x,self.y, largura/4,altura/8,53)
        self.score = 0
        self.deltaS = 0
        self.facing = "right"
        for img in range (spawn1,initX,1):
            spawnX = spawnX[img]
            self.sprite = img
            screen.blit(img(self.x,self.y))
            pg.display.flip()

    #def asuraBlink(self):
    #    if asuraF == True
    #        if left:
    #            self.sprite = asuraLeft
    #            screen.blit(self.sprite(self.x,self.y))
    #            pg.display.flip()
    #            pg.time.wait(1/2)
    #            self.sprite = linitX
    #            pg.display.flip()
    #        if right:
    #            self.sprite = asuraRight
    #            screen.blit(self.sprite(self.x,self.y))
    #            pg.display.flip()
    #            pg.time.wait(1/2)
    #            self.sprite = initX
    #            screen.blit(self.sprite(self.x,self.y))
    #            pg.display.flip()
    def die(self):
        if self.hp > 0 or self.y < altura:
            screen.blit(gameover, (0,0))
            pg.time.wait(5)
            mainMenu = True

    #def wallkick(self):
    #    if wallslide == True:
    #        y -= 2

    #def asuraFist(self):
    #    if asuraF == True:
    #        if asura == True:
    #            if left:
    #                self.sprite = asuraLeft
    #                screen.blit(self.sprite(self.x,self.y))
    #                pg.display.flip()
    #            if right:
    #                 self.sprite = asuraRight
    #                 pg.display.flip()
    #    asura = False

    def standRight(self):
        self.sprite = initX
        screen.blit(self.sprite(self.x,self.y))
        pg.display.flip()

    def standRight(self):
        self.sprite = linitX
        screen.blit(self.sprite(self.x,self.y))
        pg.display.flip()

    def standDefault(self):
        if left and right:
            standRight()

    def Lwalk(self):
        while left:
            x -= 2
            deltaS += 2
            screen.blit(lwalkloopX[self.deltaS//6],(self.x,self.y))
            pg.display.flip()
        if right == False and left == False:
            self.sprite = linitX(x,y)
            screen.blit(self.sprite(self.x,self.y))
        pg.display.flip()

    def Rwalk(self):
        while right:
            x += 1
            deltaS += 2
            screen.blit(rwalkloopX[self.deltaS//6],(self.x,self.y))
            pg.display.flip()
        if right == False and left == False:
            self.sprite = initX(x,y)
            screen.blit(self.sprite(self.x,self.y))
        pg.display.flip()

    def jump(self):
        while jump:
            self.sprite = jump1
            screen.blit(self.sprite(self.x,self.y))
            pg.display.flip()
            self.y += 10
            pg.display.flip()
            if right:
                self.x += 2
                self.facing = "right"
            if left:
                self.x -= 2
                self.facing = "left"
            pg.display.flip()
            pg.time.wait(2)
            jump = False

        #if not wallslide:
        self.sprite = jump2
        screen.blit(self.sprite(self.x,self.y))
        pg.display.update


    def Ldash(self):
        while dash and left:
          if self.x > 5:
            x -= 5
            self.sprite = ldashX
            screen.blit(self.sprite(self.x,self.y))
            pg.display.flip()
            pg.time.wait(2)
            dash = False
        if left and right == False:
            self.sprite = linitX
            screen.blit(self.sprite(self.x,self.y))
            pg.display.flip()
        else:
            if left:
                Lwalk()
            if right:
                Rwalk()

    def Rdash(self):
        while dash and right:
          if self.x < 2599:
            x += 5
            self.sprite = ldashX
            screen.blit(self.sprite(self.x,self.y))
            pg.display.flip()
            pg.time.wait(2)
            dash = False
        if left and right == False:
            self.sprite = initX
            screen.blit(self.sprite(self.x,self.y))
            pg.display.flip()
        else:
            if left:
                Lwalk()
            if right:
                Rwalk()

    def crouch (self):
        while down:
            left = False
            right = False
            jump = False
            if self.sprite == initX:
                self.sprite = rcrouchX
                screen.blit(self.sprite(self.x,self.y))
                pg.display.flip()
            elif left or self.sprite == linitX:
                self.sprite = lcrouchX,(x,y)
                screen.blit(self.sprite(self.x,self.y))
                pg.display.flip()

    def fire(self):
        if jump:
            if left:
                self.sprite = ljumpfire1
                screen.blit(self.sprite(self.x,self.y))
                pg.display.flip()
                if jump == False:
                    self.sprite = ljumpfire2
                    screen.blit(self.sprite(self.x,self.y))
                    pg.display.flip()
                    if self.y == ground.y:
                        self.sprite = linitX
                        screen.blit(self.sprite(self.x,self.y))
                        pg.display.flip()
            if right:
                self.sprite = rjumpfireloop
                screen.blit(self.sprite(self.x,self.y))
                pg.display.flip()
                if jump == False:
                    self.sprite = rjumpfire2
                    screen.blit(self.sprite(self.x,self.y))
                    pg.display.flip()
                if self.y == ground.y:
                    self.sprite = initX
                    screen.blit(self.sprite(self.x,self.y))
                    pg.display.flip()
        if dash:
            if left:
                self.sprite = ldashshot
                screen.blit(self.sprite(self.x,self.y))
                self.x -= 5
                pg.display.flip()
                pg.time.wait(2)
                self.sprite = linitX
                screen.blit(self.sprite(self.x,self.y))
                pg.display.flip()
            if right:
                self.sprite = rdashshot
                screen.blit(self.sprite(self.x,self.y))
                self.x += 5
                pg.display.flip()
                pg.time.wait(2)
                self.sprite = initX
                screen.blit(self.sprite(self.x,self.y))
                pg.display.flip()

        #if wallkick:
        #    if left:
        #        self.sprite = rshootingX
        #        screen.blit(self.sprite(self.x,self.y))
        #        pg.display.flip()
        #         pg.time.wait(1)
        #    if not wallkick
        #        self.sprite = linitX
        #        screen.blit(self.sprite(self.x,self.y))
        #        pg.display.flip()
        #    if right:
        #        self.sprite = rshootingX
        #        screen.blit(self.sprite(self.x,self.y))
        #        pg.display.flip()
        #        self.sprite = initX
        #        screen.blit(self.sprite(self.x,self.y))
        #        pg.display.flip()

        if left:
            while left:
                self.x -= 2
                deltaS += 2
                screen.blit(lwalkshootloopX[self.deltaS//6],(self.x,self.y))
                screen.blit(self.sprite(self.x,self.y))
                pg.display.flip()
            self.sprite = linitX
            screen.blit(self.sprite(self.x,self.y))
            pg.display.flip()
        if right:
            while right:
                self.x += 2
                deltaS += 2
                screen.blit(rwalkshootloopX[self.deltaS//6],(self.x,self.y))
                screen.blit(self.sprite(self.x,self.y))
                pg.display.flip()
            self.sprite = initX
            screen.blit(self.sprite(self.x,self.y))
            pg.display.flip()

        #standingPose
        if self.sprite == initX:
            self.sprite = rshootingX
            screen.blit(self.sprite(self.x,self.y))
            pg.display.flip()
            self.sprite = initX
            screen.blit(self.sprite(self.x,self.y))
            pg.display.flip()
        if self.sprite == linitX:
            self.sprite = lshootingX
            screen.blit(self.sprite(self.x,self.y))
            pg.display.flip()
            self.sprite = initX
            screen.blit(self.sprite(self.x,self.y))
            pg.display.flip()
        enemy.hp -= dmg

    #def charge(self):
    #    while charging:
    #        if self.dmg < 5:
    #            pg.time.wait(2)
    #            self.dmg += 4
    #        if self.dmg < 10:
    #            pg.time.wait(2)
    #            self.dmg += 5
    #        if charging = False:
    #            pg.time.wait(1/2)
    #            dmg = 1


#class enemy(pg.sprite.Sprite):
#    def __init__(self):
#        self.sigmaClone = Surface((132,180),pg.SRCALPHA)
#        self.sigmaClone.x =
#        self.sigmaClone.y =
#        self.sigmaClone.tex = sigmaidle
#        self.sigmaClone.hp = 10
#        self.sigmaClone.status = True
#        self.hitbox = Rect(self.x,self.y, 132,180)

#    def die(self):
#        if self.hp > 0 or self.y < altura:
#            self.status = False
#        if self.status == False
#            self.hitbox = Rect(self.x,self.y,0,0)
#            Player.score += 100

if Player.x == ground.x:
    left = False
if Player.x == 2599:
    pg.mixer.music.stop
    left = False
    right = False
    dash = False
    if Player.facing == "left":
        Player.sprite = rvictory
        pg.display.flip()
        Player.sprite = spawn4
        pg.display.flip()
        Player.sprite = spawn3
        pg.display.flip()
        Player.sprite = spawn2
        pg.display.flip()
        Player.sprite = spawn1
        pg.display.flip()
        Player.y += 2
        pg.display.flip()
        while Player.y < 0:
            Player.y += 2
            pg.display.flip()
        pg.time.wait(5)
        pg.QUIT

    if Player.facing == "right":
        Player.sprite = lvictory
        pg.display.flip()
        Player.sprite = spawn4
        pg.display.flip()
        Player.sprite = spawn3
        pg.display.flip()
        Player.sprite = spawn2
        pg.display.flip()
        Player.sprite = spawn1
        Player.y += 2
        pg.display.flip()
        while Player.y < 0:
            Player.y += 2
            pg.display.flip()
        pg.time.wait(5)
        pg.QUIT

while Player.y > ground.y:#and not wallslide:
    jump = False
    if jump == False:
        y -= 5
        Player.sprite = jump2
        if fire == True:
            Player.sprite = jumpfire2
if Player.facing == "left" and Player.y == ground.y:
    Player.sprite == initX
    screen.blit(Player.sprite(Player.x,Player.y))
if Player.facing == "right" and Player.y == ground.y:
    Player.sprite == linitX

#colisão
if Player.projectile.x == enemy.x and Player.projectile.y == enemy.y:
    if event.type == KEYUP and event.key == K_DOWN:
        enemy.hp -= Player.dmg

if enemy.x == Player.x and enemy.y == enemy.y:
    Player.hp -= enemy.dmg

if enemy.projectile.x == Player.x and enemy.projectile.y == Player.y:
    Player.hp -= enemy.dmg

class ranking():
    pontuacao += Player.score

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
#asura = False
#asuraF = False



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
        if event.type == KEYDOWN and event.key == K_F4:
            gameloop = False
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            screen.blit(pausescr, (0,0))
            pg.display.flip
        if event.type == KEYDOWN and event.key == K_UP:
            up = True
        if event.type == KEYDOWN and event.key == K_DOWN:
            down = True
        if event.type == KEYDOWN and event.key == K_LEFT:
                left = True
        if event.type == KEYDOWN and event.key == K_RIGHT:
            right = True
        if event.type == KEYDOWN and event.key == K_c:
            charging = True
            if event.type == KEYUP and event.key == K_c:
                fire = True
                charging = False

        if event.type ==KEYDOWN and event.key == K_x:
            jump = True
        #if event.type == KEYDOWN and event.key == K_v:
        #    asura = True
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
        #if event.type == KEYUP and event.key == K_v:
        #    asura = False
        if event.type == KEYUP and event.key == K_ESCAPE:
            pass
        screen.blit(Player.sprite(Player.x,Player.y))
        pg.display.flip()
    #pg.time.wait(60)
    #asuraF = True

pg.display.update()
pg.quit()
