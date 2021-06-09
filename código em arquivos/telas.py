import pygame, sys

from pygame.image import load
from config import HEIGHT, WIDTH, score, DONE, PLAYING
from pygame.locals import *
from assets import loadassets
from classes import Meteor, Luigi

volumes = True

def draw_text (text, font, color, surface, x, y):
    textobj = font.render (text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit (textobj, textrect)

mainclock = pygame.time.Clock()
window = pygame.display.set_mode((WIDTH, HEIGHT))
screen = pygame.display.set_mode((500, 500), 0, 32)

def main_menu ():
    global volumes
    assets = loadassets()
    assets['menu'].play()
    font = pygame.font.SysFont (None, 20)
    tela = pygame.image.load('imagens/inicio.png').convert()
    click = False
    jogando = True
    while jogando:
        screen.blit ((tela),(0,0))
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect (20, 30, 200, 50)
        button_2 = pygame.Rect (400, 30, 200, 50)
        if button_1.collidepoint (mx,my):
            if click:
                game()
        if button_2.collidepoint (mx,my):
            if click :
                options()
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        mainclock.tick (60)
#telas com e sem som
paraabrir = pygame.image.load('imagens/ofundoabertocomvoltar.png').convert()
parafechar = pygame.image.load('imagens/ofundofechadocomvoltar.png').convert()
#Opções
jogando = True
def options():
    global volumes
    assets = loadassets()
    click = False
    jogando = True
    while jogando:
        if volumes:
            screen.blit (parafechar,(0,0))
        else:
            screen.blit (paraabrir,(0,0))
        mx, my = pygame.mouse.get_pos()
        voltar = pygame.Rect (10,10,200,50)
        volume = pygame.Rect (240, 80, 140, 110)
        #muta e desmuta
        if volume.collidepoint (mx,my):
            if click :
                if volumes:
                    volumes = False
                    assets['menu'].stop()
                else:
                    volumes = True
                    assets['menu'].play()
        #volta para o menu
        if voltar.collidepoint (mx,my):
            if click:
                main_menu()
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click= True
        pygame.display.update()
        mainclock.tick (60)


#imagem da tela de game over
gamedown = pygame.image.load('imagens/gameover.png').convert()

#Tela de gameover
def gameover ():
    assets = loadassets ()
    jogando = True
    click = False
    global score
    while jogando:
        screen.blit (gamedown,(0,0))
        mx, my = pygame.mouse.get_pos()
        jogarnovamente = pygame.Rect (30, 220, 270, 50)
        menu = pygame.Rect (390, 250, 120, 50)    
        #para o jogo
        if jogarnovamente.collidepoint (mx,my):
            if click:
                game()
        #para o menu   
        if menu.collidepoint (mx,my):
            if click:
                main_menu()  
        #pontuação da rodada
        text_surface = assets['score_font'].render("{:03d}".format(score), True, (255, 255,255 ))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 3,  110)
        window.blit(text_surface, text_rect)
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click= True
        pygame.display.update()
        mainclock.tick (60)

# def game ():
#     running = True
#     while running:
#         screen.fill ((0,0,0))

#         draw_text ('game', font, (255, 255, 255), screen, 20, 20)
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == KEYDOWN:
#                 if event.key == K_ESCAPE:
#                     pygame.quit()
#                     sys.exit()
#             if event.type == MOUSEBUTTONDOWN:
#                 if event.button == 1:
#                     running = False
#         pygame.display.update()
#         mainclock.tick (60)

def game ():
    assets = loadassets()
    global volumes
    global score
    BIXOS = 3
    score = 0
    clock = pygame.time.Clock()
    FPS = 30
    #Criando os grupos
    all_bixos = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_bullets = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_bullets'] = all_bullets
    groups['all_bixos'] = all_bixos
    for i in range(3):
        inimigo = Meteor(assets)
        all_sprites.add(inimigo)
        all_bixos.add(inimigo)


    luigi = Luigi(groups, assets)
    all_sprites.add(luigi)

    # ===== Loop principal =====
    if volumes:
        pygame.mixer.music.play(loops=-1)
    while state != DONE:
        clock.tick(FPS)
        assets['menu'].stop()
        assets['menu'].set_volume(0.2)
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
                pygame.mixer.music.stop()
            # Verifica se apertou alguma tecla.
            if state == PLAYING:
                if event.type == pygame.KEYDOWN:
                    # Dependendo da tecla, altera a velocidade.
                    keys_down[event.key] = True
                    if event.key == pygame.K_LEFT:
                        luigi.speedx -= 8
                    if event.key == pygame.K_RIGHT:
                        luigi.speedx += 8
                    if event.key == pygame.K_UP:
                        luigi.jump()
                    if event.key == pygame.K_SPACE:
                        luigi.shoot()
                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:
                    # Dependendo da tecla, altera a velocidade.
                    if event.key in keys_down and keys_down[event.key]:
                        if event.key == pygame.K_LEFT:
                            luigi.speedx += 8
                        if event.key == pygame.K_RIGHT:
                            luigi.speedx -= 8

        # ----- Atualiza estado do jogo
        all_sprites.update()

        if state == PLAYING:
            #Verifica se houve colisão entre a tartaruga e os bixos
            hits = pygame.sprite.groupcollide(all_bixos, all_bullets, True, True)
            for meteor in hits: # As chaves são os elementos do primeiro grupo (meteoros) que colidiram com alguma bala
                # O bixo morre e precisa ser recriado
                m = Meteor(assets)
                all_sprites.add(m)
                all_bixos.add(m)
                if volumes:
                    assets['morre'].play()
                score+=100
                if score % 1000 == 0:
                    lives += 1
                    if volumes:
                        assets['vida_ganha'].play()
                    if BIXOS<4:
                        BIXOS+=1
                        m = Meteor(assets)
                        all_sprites.add(m)
                        all_bixos.add(m)
            
            # Verifica colisão com o personage 
            hits = pygame.sprite.spritecollide(luigi, all_bixos, True)
            if len(hits) > 0:
                if lives==1:
                    if volumes:
                        assets['fim'].play()
                    pygame.mixer.music.stop()
                    state = DONE
                    gameover()
                else:
                    lives-=1
                    if volumes:
                        assets['vida_perde'].play()
                    # assets['morre'].play()
                    luigi.kill()
                    keys_down = {}
                    luigi = Luigi(groups, assets) 
                    all_sprites.add(luigi)
                    m = Meteor(assets)
                    all_sprites.add(m)
                    all_bixos.add(m) 
                        
                    
                
            
        # ----- Gera saídas
        window.fill((255,255,255))  # Preenche com a cor branca
        window.blit(assets['background'],(0,0))


        #Desenha o Luigi
        all_sprites.draw(window)

        # Desenhando o score
        text_surface = assets['score_font'].render("{:03d}".format(score), True, (255, 255, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        window.blit(text_surface, text_rect)
    
        assets['vidas'] = pygame.image.load('imagens/vidas.png').convert_alpha()
        assets['vidas'] = pygame.transform.scale(assets['vidas'], (25, 20))
        for a in range (0, lives):
            img = assets['vidas']
            img_rect = img.get_rect()
            img_rect.bottomleft = (10 + 25*a, HEIGHT - 10)
            window.blit(img, img_rect)

    


        pygame.display.update() # Mostra o novo frame para o jogador