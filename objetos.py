# -*- coding: utf-8 -*-
import pygame as pg
from cfg import *
import os
import projeto
import time

class gameStuff():

    class ground(self):
        self.tex = ground
        self.y = 604
        self.sup = Surface(self.tex(2604,116))
        Surface.blit(self.sup(0,self.y))

    class Player(pg.sprite.Sprite):
        def __init__(self):
            self.mmX = Surface((largura/4,altura/8,53),pg.SRCALPHA)
            self.pos = (x,y)
            self.hp = 50
            self.dmg = 5
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
                screen.blit(lwalkloopX[self.deltaS//6],(self.x,self.y)))
                pg.display.flip()
            if right == False and left == False:
                self.sprite = linitX(x,y)
                screen.blit(self.sprite(self.x,self.y))
            pg.display.flip()

        def Rwalk(self):
            while right:
                x += 1
                deltaS += 2
                screen.blit(rwalkloopX[self.deltaS//6],(self.x,self.y)))
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
              if self.x > 5
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
              if self.x < 2599
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
                    screen.blit(lwalkshootloopX[self.deltaS//6],(self.x,self.y)))
                    screen.blit(self.sprite(self.x,self.y))
                    pg.display.flip()
                self.sprite = linitX
                screen.blit(self.sprite(self.x,self.y))
                pg.display.flip()
            if right:
                while right:
                    self.x += 2
                    deltaS += 2
                    screen.blit(rwalkshootloopX[self.deltaS//6],(self.x,self.y)))
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


    class enemy(pg.sprite.Sprite):
        def __init__(self):
            self.sigmaClone = Surface((132,180),pg.SRCALPHA)
            self.sigmaClone.x =
            self.sigmaClone.y = 
            self.sigmaClone.tex = sigmaidle
            self.sigmaClone.hp = 10
            self.sigmaClone.status = True
            self.hitbox = Rect(self.x,self.y, 132,180)

        def die(self):
            if self.hp > 0 or self.y < altura:
                self.status = False
            if self.status == False
                self.hitbox = Rect(self.x,self.y,0,0)
                Player.score += 100

    class ranking():
        pontuacao += Player.score
