# -*- coding: utf-8 -*-
import pygame as pg
from cfg import *
import os
import projeto
import time

class gameStuff():
    class Player(pg.sprite.Sprite):
        def __init__(self):
            self.mmX = Surface((largura/4,altura/8,53),pg.SRCALPHA)
            self.pos = (x,y)
            self.hp = 50
            self.dmg = 5
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
                screen.blit(gameover)
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
                x += 1
                pg.display.flip
                pg.time.wait(1/10)
                if left == True:
                    for img in range (lwalkstart,lwalkx6):
                        lwalkloopX = lwalkloopX[img]
                        self.sprite = img
                        pg.display.flip()
                        img += 1
            if right == False and left == False:
                self.sprite = linitX(x,y)
            pg.display.flip()

        def Rwalk(self):
            while right:
                x += 1
                pg.time.wait(1/10)
                if right == True:
                    for img in range (rwalkstart,rwalkx6):
                        rwalkloopX = rwalkloopX[img]
                        self.sprite = img,(x,y)
                        pg.display.flip()
                        img += 1
                if right == False and left == False:
                    self.sprite = initX(x,y)
                    pg.display.flip()


        def Ldash(self):
            while dash and left:
                x += 5
                self.sprite = rdashX(x,y)
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
                self.x += 0
                self.y += 0
                if right or self.sprite == initX:
                    self.sprite = rcrouchX,(x,y)
                    screen.blit(self.sprite(self.x,self.y))
                    pg.display.flip()
                elif left or self.sprite == linitX:
                    self.sprite = lcrouchX,(x,y)
                    screen.blit(self.sprite(self.x,self.y))
                    pg.display.flip()

        def fire(self):
            if jump:
                if left:
                    for img in range (ljumpfire1,ljumpfire2,1):
                        ljumpfireloop = ljumpfireloop[img]
                        self.sprite = ljumpfireloop(x,y)
                        screen.blit(self.sprite(self.x,self.y))
                        pg.display.flip()
                    self.sprite = initX(x,y)
                    screen.blit(self.sprite(self.x,self.y))
                    pg.display.flip()
                if right:
                    for img in range (rjumpfire1,rjumpfire2,1):
                        rjumpfireloop = rjumpfireloop[img]
                        self.sprite = rjumpfireloop
                        screen.blit(self.sprite(self.x,self.y))
                        pg.display.flip()
                    self.sprite = initX
                    screen.blit(self.sprite(self.x,self.y))
                    pg.display.flip()
            if dash:
                if left:
                    self.sprite = ldashshot
                    screen.blit(self.sprite(self.x,self.y))
                    pg.display.flip()
                    pg.time.wait(2)
                    self.sprite = linitX
                    screen.blit(self.sprite(self.x,self.y))
                    pg.display.flip()
                if right:
                    self.sprite = rdashshot
                    pg.display.flip()
                    pg.time.wait(2)
                    self.sprite = initX
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
                for img in range (lwalkShootX1,lwalkShootX6):
                    lwalkloopX = lwalkloopX[img]
                    self.sprite = lwalkloopX
                    screen.blit(self.sprite(self.x,self.y))
                    pg.display.flip()

                self.sprite = linitX
                screen.blit(self.sprite(self.x,self.y))
                pg.display.flip()
            if right:
                for img in range (rwalkShootX1,rwalkShootX6,1)
                    rwalkloopX = rwalkloopX[img]
                    self.sprite = rwalkloopX
                    screen.blit(self.sprite(self.x,self.y))
                    pg.display.flip()
                pg.time.wait(2)
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
            if self.sprite == linitX(x,y):
                self.sprite = lshootingX(x,y)
                pg.display.flip()
                self.sprite = initX(x,y)
                pg.display.flip()
            enemy.hp -= dmg


        def jump(self):
            while jump:
                self.sprite = jump1
                screen.blit(self.sprite(self.x,self.y))
                pg.display.flip()
                self.y += 10
                if right:
                    self.x += 2
                if left:
                    self.x -= 2
                pg.display.flip()
                pg.time.wait(2)
                jump = False

            #if not wallslide:
                self.sprite = jump2
                screen.blit(self.sprite(self.x,self.y))
                y -= 10
                pg.display.update

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


    class enemy(pg.sprite.Sprite):
        def __init__(self):
            self.sigmaClone = Surface((largura/3.83,altura/8.53),pg.SRCALPHA)
            self.sigmaClone.hp = 10
            self.sigmaClone.status = True

        def die(self):
            if self.hp > 0 or self.y < altura:
                self.status = False
            #if self.status == False
                #destrua o objeto ou tire da tela
                #pass

    class ranking():
        pass

    class Camera(object):
        def __init__(self, camera_func, largura, height):
            self.camera_func = camera_func
            self.state = Rect(0, 0, largura, altura)

        def apply(self, target):
            return target.rect.move(self.state.topleft)

        def update(self, target):
            self.state = self.camera_func(self.state, target.rect)
