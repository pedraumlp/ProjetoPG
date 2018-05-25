# -*- coding: utf-8 -*-
import pygame as pg
from cfg import *
import os
import projeto
import time

class gameStuff():
    class enemy(pg.sprite.Sprite):
        def __init__(self):
            sigmaClone = Surface((largura/3.83,altura/8.53),pg.SRCALPHA)
            hp = 10

    class Player(pg.sprite.Sprite):
        def __init__(self):
            Player.mmX = Surface((largura/4,altura/8,53),pg.SRCALPHA)
            Player.pos = (x,y)
            for img in range (spawn1,initX):
                spawnX = spawnX[img]
                Player.sprite = img
                pg.display.flip()
                img += 1
        #def die(self):
        #    if hp > 0 or y < altura:
        #        pg.quit()

        def wallkick(self):
            if wallslide == True:
                y -= 2

        def standRight(self):
            Player.sprite = initX

        def standRight(self):
            Player.sprite = linitX

        def standDefault(self):
            if left:
             if right:
                standRight()

        def Ldash(self):
            while dash and left:
                x += 5
                Player.sprite = rdashX(x,y)
                pg.display.flip()
                pg.time.wait(2)
                dash = False
            if right == False and left == False:
                Player.sprite = linitX
                pg.display.flip()

        def Rdash(self):
            while dash and right:
                x += 5
                Player.sprite = ldashX
                pg.display.flip()
                pg.time.wait(2)
                dash = False
            if right == False and left == False:
                Player.sprite = initX
                pg.display.flip()

        def Lwalk(self):
            while left:
                x += 1
                pg.display.flip
                pg.time.wait(1/10)
                if left == True:
                    for img in range (lwalkstart,lwalkx6):
                        lwalkloopX = lwalkloopX[img]
                        Player.sprite = img
                        pg.display.flip()
                        img += 1
            if right == False and left == False:
                Player.sprite = linitX(x,y)
            pg.display.flip()

        def Rwalk(self):
            while right:
                x += 1
                pg.time.wait(1/10)
                if right == True:
                    for img in range (rwalkstart,rwalkx6):
                        rwalkloopX = rwalkloopX[img]
                        Player.sprite = img,(x,y)
                        pg.display.flip()
                        img += 1
                if right == False and left == False:
                    Player.sprite = initX(x,y)
                    pg.display.flip()

        def crouch (self):
            while down:
                x += 0
                y += 0
                if right or Player.sprite == initX:
                    Player.sprite = rcrouchX,(x,y)
                elif left or Player.sprite == linitX:
                    Player.sprite = lcrouchX,(x,y)

        def charge(self):
            while charging:
                if dmg < 5:
                    pg.time.wait(2)
                    dmg += 5
                if dmg < 10:
                    pg.time.wait(2)
                    dmg+= 5

#animações de tiro
        def fire(self):
            if jump:
                if left:
                    for img in range (ljumpfire1,ljumpfire2):
                        ljumpfireloop = ljumpfireloop[img]
                        Player.sprite = ljumpfireloop(x,y)
                        pg.display.flip()
                        img += 1
                    Player.sprite = initX(x,y)
                    pg.display.flip()
                if right:
                    for img in range (rjumpfire1,rjumpfire2):
                        rjumpfireloop = rjumpfireloop[img]
                        Player.sprite = rjumpfireloop(x,y)
                        pg.display.flip()
                        img += 1
                    Player.sprite = initX(x,y)
                    pg.display.flip()
            if dash:
                if left:
                    Player.sprite = ldashshot(x,y)
                    pg.display.flip()
                    pg.time.wait(2)
                    Player.sprite = linitX(x,y)
                    pg.display.flip()
                if right:
                    Player.sprite = rdashshot(x,y)
                    pg.display.flip()
                    pg.time.wait(2)
                    Player.sprite = initX(x,y)
                    pg.display.flip()

            #if wallkick:
            #    if left:
            #        Player.sprite = rshootingX(x,y)
            #        pg.display.flip()
            #         pg.time.wait(1)
            #    if not wallkick
            #        Player.sprite = linitX(x,y)
            #        pg.display.flip()
            #    if right:
            #        Player.sprite = rshootingX(x,y)
            #        pg.display.flip()
            #        Player.sprite = initX(x,y)
            #        pg.display.flip()

            if left:
                for img in range (lwalkShootX1,lwalkShootX6):
                    lwalkloopX = lwalkloopX[img]
                    Player.sprite = lwalkloopX(x,y)
                    pg.display.flip()

                Player.sprite = linitX(x,y)
                pg.display.flip()
            if right:
                for img in range (rwalkShootX1,rwalkShootX6)
                    rwalkloopX = rwalkloopX[img]
                    Player.sprite = rwalkloopX(x,y)
                    pg.display.flip()
                pg.time.wait(2)
                Player.sprite = initX(x,y)
                pg.display.flip()

            #standingPose
            if Player.sprite == initX:
                Player.sprite = rshootingX(x,y)
                pg.display.flip()
                Player.sprite = initX(x,y)
                pg.display.flip()
            if Player.sprite == linitX(x,y):
                Player.sprite = lshootingX(x,y)
                pg.display.flip()
                Player.sprite = initX(x,y)
                pg.display.flip()
            enemy.hp -= dmg


        def jump(self):
            while jump:
                Player.sprite = jump1,(x,y)
                pg.display.flip()
                img += 1
                y += 10
                pg.display.flip()
                pg.time.wait(2)
                jump = False
            if not wallslide:
                Player.sprite = jump1,(x,y)
                y -= 10
                pg.display.update

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
