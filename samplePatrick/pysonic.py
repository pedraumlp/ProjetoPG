import pygame
import random
import time
pygame.init

tela = pygame.display.set_mode((900,500))

sonic_parado = pygame.image.load('parado.png')

corrida_right = [pygame.image.load('corrida.png'),pygame.image.load('corrida1.png'),
                 pygame.image.load('corrida2.png'),
                 pygame.image.load('corrida3.png')]

corrida_left = [pygame.image.load('corridaleft.png'),pygame.image.load('corrida1left.png'),
                 pygame.image.load('corrida2left.png'),
                 pygame.image.load('corrida3left.png')]

pulo = [pygame.image.load('puloright.png'),pygame.image.load('pulo1right.png'),
              pygame.image.load('pulo2right.png'),pygame.image.load('pulo3right.png'),
              pygame.image.load('pulo4right.png'),pygame.image.load('pulo5right.png'),
              pygame.image.load('pulo6right.png'),pygame.image.load('pulo7right.png'),
              pygame.image.load('pulo8right.png')]

clock = pygame.time.Clock()


class sonic(object):
    def __init__(self,x_sonic,y_sonic,width,height):
        self.x_sonic = x_sonic
        self.y_sonic = y_sonic
        self.width = width
        self.height = height
        self.velo = 12
        self.pulando = False
        self.left =False
        self.right = False
        self.cont_anda = 0
        self.cont_pulei = 0
        self.cont_pulo = 10
        self.hitbox = (self.x_sonic, self.y_sonic,self.width,self.height)
        
    def desenhar(self, tela):
        if self.cont_anda +1 >= 12:
            self.cont_anda = 0
        if self.left and self.pulando == False:
            tela.blit(corrida_left[self.cont_anda//3],(self.x_sonic,self.y_sonic))
            self.cont_anda +=1
        elif self.right and self.pulando == False:
            tela.blit(corrida_right[self.cont_anda//3],(self.x_sonic,self.y_sonic))
            self.cont_anda +=1
        elif self.cont_pulei +1 >= 12:
            self.cont_pulei = 0
        elif self.pulando:
            tela.blit(pulo[self.cont_pulei//3], (self.x_sonic,self.y_sonic))
            self.cont_pulei += 1
        else:
            tela.blit(sonic_parado,(self.x_sonic,self.y_sonic))
        self.hitbox = (self.x_sonic, self.y_sonic,self.width, self.height)
        pygame.draw.rect(tela, (255,0,0), self.hitbox,2)
        
class inimigos(object):
    car = [pygame.image.load('car1.png'),pygame.image.load('car2.png'),pygame.image.load('car3.png'),pygame.image.load('car4.png')]
    macaco = [pygame.image.load('macaco1.png'),pygame.image.load('macaco2.png'),pygame.image.load('macaco3.png'),pygame.image.load('macaco4.png'),
              pygame.image.load('macaco5.png'),
              pygame.image.load('macaco6.png')]
    boss1 = pygame.image.load('boss1.png')
    boss2 = pygame.image.load('boss2.png')
    boss3 = pygame.image.load('boss3.png')
    boss4 = pygame.image.load('boss4.png')
    boss5 = pygame.image.load('boss5.png')
    boss6 = pygame.image.load('boss6.png')
    boss7 = pygame.image.load('boss7.png')
    boss8 = pygame.image.load('boss8.png')
    
    def __init__(self):
        self.x_inimigo = 925
        self.x_inimigo2 = 1125
        self.cont_car = 0
        self.cont_macaco = 0
        self.atak = 3
        self.macaco_hitbox = (self.x_inimigo,355, 58, 75)
        
    def mover(self, tela):
        self.x_inimigo += ambiente.velo
        self.x_inimigo2 +=ambiente.velo
        
        if self.cont_macaco + 1 > 24:
            self.cont_macaco = 0
            
        if self.cont_car +1 > 12:
            self.cont_car = 0
            
        if self.x_inimigo <= -100 and self.x_inimigo2 <= -32:
            self.atak = random.randrange(0,11)
            self.x_inimigo = 925
            self.x_inimigo2 = 1125
            
        elif self.atak == 0:
            print(self.cont_macaco//3)
            tela.blit(self.macaco[self.cont_macaco//4],(self.x_inimigo, 355))
            self.cont_macaco +=1
            
        elif self.atak == 1:
            tela.blit(self.car[self.cont_car//3],(self.x_inimigo, 396))
            self.cont_car +=1
            
        elif self.atak == 2:
            tela.blit(self.car[self.cont_car//3],(self.x_inimigo, 396))
            tela.blit(self.car[self.cont_car//3],(self.x_inimigo2, 396))
            self.cont_car +=1
            
        elif self.atak == 3:
            tela.blit(self.boss1,(self.x_inimigo, 358))
        elif self.atak == 4:
            tela.blit(self.boss2,(self.x_inimigo, 359))
        elif self.atak == 5:
            tela.blit(self.boss3,(self.x_inimigo, 371))
        elif self.atak == 6:
            tela.blit(self.boss4,(self.x_inimigo, 364))
        elif self.atak == 7:
            tela.blit(self.boss5,(self.x_inimigo, 354))
        elif self.atak == 8:
            tela.blit(self.boss6,(self.x_inimigo, 364))
        elif self.atak == 9:
            tela.blit(self.boss7,(self.x_inimigo, 366))
        elif self.atak == 10:
            tela.blit(self.boss5,(self.x_inimigo, 370))

        
class mapa():
    def __init__(self):
        self.largura = 0
        self.largura0 = 1000
        self.velo = -5
        self.pontos = 0
        self.fase = 10
        
    def mapa_movimento(self,tela):
        mapa = pygame.image.load('mapa_chao1.png')
        self.largura += self.velo
        self.largura0 += self.velo
        
        tela.blit(mapa,(self.largura,0))
        tela.blit(mapa,(self.largura0,0))
        jogador.x_sonic += self.velo
        if self.largura <=-1000 and self.largura0 <=0:
            self.largura=1000
            self.largura0 = 0
            self.pontos +=10
            
        if self.largura0 <=-1000 and self.largura <= 0:
            self.largura0=1000
            self.largura=0
            self.pontos +=10
            
        if self.pontos > self.fase:
            jogador.velo +=2
            self.velo += -2
            self.fase +=self.fase


def buttons(img,img0,x,y,img_w,img_h,action=None):
    
    #pega a posicao do mouse
    mouse = pygame.mouse.get_pos()
    

    #pega a action do mouse
    click = pygame.mouse.get_pressed()

    img = pygame.image.load(img)
    img0 = pygame.image.load(img0)
            
    if x+img_w > mouse[0] > x and y+img_h > mouse[1] > y:
        tela.blit(img,(x,y))
        if click[0] == 1 and action != None:
            if action == 'jogar':
                jogador.x_sonic = 300
                jogador.y_sonic = 390
                jogador.velo = 12
                jogador.pulando = False
                jogador.cont_pulo = 10
                #inimigo
                inimigo.x_inimigo = 925
                #mapa
                ambiente.largura = 0
                ambiente.largura0 = 1000
                ambiente.velo = -5
                ambiente.pontos = 0
                ambiente.fase = 10
                game()
            elif action == 'sair':
                pygame.quit()
                quit()
            elif action == 'menu':
                game_intro()
            elif action == 'jogar novamente':
                #sonic
                jogador.x_sonic = 300
                jogador.y_sonic = 390
                jogador.velo = 12
                jogador.pulando = False
                jogador.cont_pulo = 10
                #inimigo
                inimigo.x_inimigo = 925
                #mapa
                ambiente.largura = 0
                ambiente.largura0 = 1000
                ambiente.velo = -5
                ambiente.pontos = 0
                ambiente.fase = 10
                game()
                
                
    else:
        tela.blit(img0,(x,y))
        
def game_over():
    game_over = pygame.image.load('game_over1.png')
    mapa = pygame.image.load('mapa_chao1.png')
    
    intro = True

    while intro:
        tela.blit(mapa,(ambiente.largura,0))
        tela.blit(mapa,(ambiente.largura0,0))
        tela.blit(game_over,(200,100))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        buttons('jogar0.png','jogar.png',405,440,76,16,'jogar novamente')
        buttons('sair0.png','sair.png',650,440,61,16,'sair')
        buttons('menu0.png','menu.png',160,440,60,16,'menu')
        
        clock.tick(30)
        pygame.display.update()

def game_intro():
    capa = pygame.image.load('intro_foto.png')
    
    
    

    intro = True

    while intro:
        clock.tick(60)
        tela.blit(capa,(0,0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        buttons('jogar0.png','jogar.png',405,440,76,16,'jogar')
        buttons('sair0.png','sair.png',650,440,61,16,'sair')
        buttons('tutorial0.png','tutorial.png',160,440,114,16,'tutorial')
        
        clock.tick(30)
        pygame.display.update()


def desenhar_na_tela():
    tela.fill((255,255,255))
    ambiente.mapa_movimento(tela)
    inimigo.mover(tela)
    jogador.desenhar(tela)
    
    pygame.display.update()
                  
inimigo = inimigos()
ambiente = mapa()
jogador = sonic(300,390,32,36)

def game():
    run=True
    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] and jogador.x_sonic > jogador.velo:
            jogador.x_sonic -= jogador.velo
            jogador.left = True
            jogador.right = False
        elif keys[pygame.K_RIGHT] and jogador.x_sonic < 900 - jogador.width - jogador.velo:
            jogador.x_sonic += jogador.velo
            jogador.right = True
            jogador.left = False
        else:
            jogador.left = False
            jogador.right = False
            jogador.cont_anda = 0
            
        if not(jogador.pulando):
            if keys[pygame.K_SPACE]:
                jogador.pulando = True
                jogador.right = False
                jogador.left = False
                jogador.cont_anda = 0
        else:
            if jogador.cont_pulo >= -10:
                neg = 1
                if jogador.cont_pulo < 0:
                    neg= -1
                jogador.y_sonic -= (jogador.cont_pulo ** 2) * 0.4 * neg
                jogador.cont_pulo -= 1
            else:
                jogador.pulando = False
                jogador.cont_pulo = 10
         
        
        #self.macaco_hitbox = (self.x_inimigo,355, 60, 75)
        #(self.x_sonic, self.y_sonic,self.width,self.height)
        if  inimigo.x_inimigo < jogador.x_sonic+32 and inimigo.x_inimigo+58 > jogador.x_sonic and 355 < jogador.y_sonic+36 < 430 and inimigo.atak == 0:
            game_over()
        if inimigo.x_inimigo < jogador.x_sonic+32 and inimigo.x_inimigo+32 > jogador.x_sonic and 396 < jogador.y_sonic+31 < 430 and inimigo.atak == 1:
            game_over()
        if inimigo.x_inimigo < jogador.x_sonic+32 and inimigo.x_inimigo+32 > jogador.x_sonic and 396 < jogador.y_sonic+31 < 430 and inimigo.atak == 2 or inimigo.x_inimigo2 < jogador.x_sonic+32 and inimigo.x_inimigo2+32 > jogador.x_sonic and 396 < jogador.y_sonic+31 < 430 and inimigo.atak == 2:
            game_over()
        if inimigo.x_inimigo < jogador.x_sonic+32 and inimigo.x_inimigo+82 > jogador.x_sonic and 358 < jogador.y_sonic+31 < 430 and inimigo.atak == 3:
            game_over()
        if inimigo.x_inimigo < jogador.x_sonic+32 and inimigo.x_inimigo+72 > jogador.x_sonic and 359 < jogador.y_sonic+31 < 430 and inimigo.atak == 4:
            game_over()
        if inimigo.x_inimigo < jogador.x_sonic+32 and inimigo.x_inimigo+76 > jogador.x_sonic and 371 < jogador.y_sonic+31 < 430 and inimigo.atak == 5:
            game_over()
        if if inimigo.x_inimigo < jogador.x_sonic+32 and inimigo.x_inimigo+55 > jogador.x_sonic and 364 < jogador.y_sonic+31 < 430 and inimigo.atak == 6:
            game_over()
        if if inimigo.x_inimigo < jogador.x_sonic+32 and inimigo.x_inimigo+64 > jogador.x_sonic and 354 < jogador.y_sonic+31 < 430 and inimigo.atak == 7:
            game_over()
        if inimigo.x_inimigo < jogador.x_sonic+32 and inimigo.x_inimigo+55 > jogador.x_sonic and 364 < jogador.y_sonic+31 < 430 and inimigo.atak == 8:
            game_over()
        if inimigo.x_inimigo < jogador.x_sonic+32 and inimigo.x_inimigo+66 > jogador.x_sonic and 366 < jogador.y_sonic+31 < 430 and inimigo.atak == 9:
            game_over()
        if if inimigo.x_inimigo < jogador.x_sonic+32 and inimigo.x_inimigo+64 > jogador.x_sonic and 370 < jogador.y_sonic+31 < 430 and inimigo.atak == 10:
            game_over()
                                                                                                                                                                                         
            
        desenhar_na_tela()

game_intro()
game()
pygame.quit()




















