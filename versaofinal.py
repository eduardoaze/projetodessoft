#IMPORTANDO BIBLIOTECAS NESCESSÁRIAS
import pygame, sys
import random
from pygame.locals import *
#CONFIGURAÇÕES
mainclock = pygame.time.Clock()
pygame.init ()
pygame.mixer.init()
pygame.display.set_caption ('game base')
#TELAS E OUTROS PARÂMETROS
screen = pygame.display.set_mode((500, 500), 0, 32)
tela = pygame.image.load('imagens/inicio.png').convert()
WIDTH = 620 #-------Largura da tela
HEIGHT = 310 #------Altura da tela
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Luigi Run')
obstaculo_WIDTH = 50 #------Parâmetros dos bixos
obstaculo_HEIGHT = 38 #-----Parâmetros dos bixos
luigi_WIDTH = 50 #----------Parâmetros do Luigi
luigi_HEIGHT = 38 #---------Parâmetros do Luigi
font = pygame.font.SysFont(None, 48)
# CARREGA O SOM DE FUNDO
pygame.mixer.music.load('sons\musicaprincipal.wav')
pygame.mixer.music.set_volume(0.2)
#DEFINE QUE O JOGO INCIA COM SOM LIGADO
volumes = True
#INICIA OS ASSETS
assets = {}
assets['vida_perde'] = pygame.mixer.Sound('sons/Nope (Construction Worker TF2) - Gaming Sound Effect (HD) (1).wav')
assets['vida_ganha'] = pygame.mixer.Sound('sons/Mario Coin Sound - Sound Effect (HD).wav')
assets['menu'] = pygame.mixer.Sound('sons\menu.wav')
assets['menu'].set_volume(0.2)
assets['fim'] = pygame.mixer.Sound('sons\Super Mario Dies Sound Effect.wav')
assets['morre'] = pygame.mixer.Sound('sons\Splat - Gaming Sound Effect (HD).wav')
assets['pulo'] = pygame.mixer.Sound('sons\Mario Jump - Gaming Sound Effect (HD).wav')
assets['background'] = pygame.image.load('imagens/ofundo.jpg').convert()
assets['luigi_img'] = pygame.image.load('imagens/luigi00.png').convert_alpha()
assets['luigi_img'] = pygame.transform.scale(assets['luigi_img'], (luigi_WIDTH, luigi_HEIGHT))
assets['luigidireita_img'] = pygame.image.load('imagens/luigi02.png').convert()
assets['luigidireita_img'] = pygame.image.load('imagens/luigi02.png').convert_alpha()
assets['luigidireita_img'] = pygame.transform.scale(assets['luigidireita_img'], (luigi_WIDTH, luigi_HEIGHT))
assets['luigi_pulando_direita'] = pygame.image.load('imagens\luigi_voando.png').convert_alpha()
assets['luigi_pulando_direita'] = pygame.transform.scale(assets['luigi_pulando_direita'], (luigi_WIDTH, luigi_HEIGHT))
assets['luigi_pulando_esquerda'] = pygame.image.load('imagens\luigi_voando2.png').convert_alpha()
assets['luigi_pulando_esquerda'] = pygame.transform.scale(assets['luigi_pulando_esquerda'], (luigi_WIDTH+13, luigi_HEIGHT+13)) #As imagens não estavam do mesmo tamanho
#LISTA DE ANIMAÇÃO DO BIXO
bixo = []
for i in range(0,2):
    filename = 'imagens/bixo0{}.png'.format(i)
    img = pygame.image.load(filename).convert_alpha()
    img = pygame.transform.scale(img, (50,38))
    bixo.append(img)
assets['bixo'] = bixo
#LISTA DE ANIMAÇÃO DE ANDAR PARA A ESQUERDA
luigi_esquerda_anim = []
for i in range(3, 5):
    filename = 'imagens/luigi0{}.png'.format(i)
    img = pygame.image.load(filename).convert_alpha()
    img = pygame.transform.scale(img, (50,38))
    luigi_esquerda_anim.append(img)

#LISTA DE ANIMAÇÃO PARA ANDAR E FICAR PARADO

luigi_direita_anim = []
for i in range(0, 3):
    filename = 'imagens/luigi0{}.png'.format(i)
    img = pygame.image.load(filename).convert_alpha()
    img = pygame.transform.scale(img, (50,38))
    luigi_direita_anim.append(img)

#LISTA DE ANIMAÇÃO DA TARTARUGA

tartaruga_anim = []
for i in range(1, 4):
    filename = 'imagens/tartaruga0{}.png'.format(i)
    img = pygame.image.load(filename).convert_alpha()
    img = pygame.transform.scale(img, (50,38))
    tartaruga_anim.append(img)
assets['tartaruga_anim'] = tartaruga_anim
assets["score_font"] = font

#TOCA A MUSICA DO MENU
assets['menu'].play()

#MENU PRINCIPAL
def main_menu ():
    click = False
    jogando = True
    while jogando:
        #DESENHA A TELA DO MENU
        screen.blit ((tela),(0,0))
        mx, my = pygame.mouse.get_pos()
        #CRIA OS BOTÕES
        button_1 = pygame.Rect (20, 30, 200, 50)
        button_2 = pygame.Rect (400, 30, 200, 50)
        #VERIFICA SE CLICOU NO BOTÃO DE INCIAR O JOGO
        if button_1.collidepoint (mx,my):
            if click:
                game()
        #VERIFICA SE CLICOU NO BOTAO DE OPÇÕES
        if button_2.collidepoint (mx,my):
            if click :
                options()
        click = False

        #FUNCIONAMENTO DO BOTÃO
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

        #ATUALIZA A TELA
        pygame.display.update()
        mainclock.tick (60)

#CARREGA IMAGENS PARA A ANIMAÇÃO DE LIGAR E DESLIGAR O SOM
paraabrir = pygame.image.load('imagens/ofundoabertocomvoltar.png').convert()
parafechar = pygame.image.load('imagens/ofundofechadocomvoltar.png').convert()

#Opções
def options():
    click = False
    jogando = True
    global volumes
    while jogando:
        #MOSTRA SE O SOM ESTÁ LIGADO OU NÃO
        if volumes:
            screen.blit (parafechar,(0,0))
        else:
            screen.blit (paraabrir,(0,0))
        mx, my = pygame.mouse.get_pos()
        #DESENHA OS BOTÕES
        voltar = pygame.Rect (10,10,200,50)
        volume = pygame.Rect (240, 80, 140, 110)
        #MUTA E DESMUTA TODOS OS SONS
        if volume.collidepoint (mx,my):
            if click :
                if volumes:
                    volumes = False
                    assets['menu'].stop()
                else:
                    volumes = True
                    assets['menu'].play()
        #VOLTA PARA O MENU
        if voltar.collidepoint (mx,my):
            if click:
                main_menu()
        click = False

        #FUNCIONAMENTO DO BOTÃO
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

        #ATUALIZA A TELA
        pygame.display.update()
        mainclock.tick (60)

#CARREGA A IMAGEM DA TELA DE GAMEOVER
gamedown = pygame.image.load('imagens/gameover.png').convert()

#TELA DE GAMEOVER
def gameover ():
    jogando = True
    click = False
    global score
    while jogando:
        screen.blit (gamedown,(0,0))
        mx, my = pygame.mouse.get_pos()
        #DESENHA OS BOTÕES
        jogarnovamente = pygame.Rect (30, 220, 270, 50)
        menu = pygame.Rect (390, 250, 120, 50)    
        #VERIFICA SE CLICOU NO BOTÃO DE JOGAR NOVAMENTE
        if jogarnovamente.collidepoint (mx,my):
            if click:
                game()
        #VERIFICA SE CLICOU NO BOTÃO DE VOLTAR PARA O MENU  
        if menu.collidepoint (mx,my):
            if click:
                main_menu()  
        #MOSTRA A PONTUAÇÃO OBTIDA NO JOGO
        text_surface = assets['score_font'].render("{:03d}".format(score), True, (255, 255,255 ))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 3,  110)
        window.blit(text_surface, text_rect)
        click = False

        #FUNCIONAMENTO DO BOTÃO
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

        #ATUALIZA A TELA
        pygame.display.update()
        mainclock.tick (60)
                    
#JOGO
def game ():
    global score
    #SCORE DO JOGADOR
    score = 0
    #Variáveis para a função pulo:
    GRAVITY = 2
    JUMP_SIZE = 20
    GROUND = HEIGHT - 10
    #Define os estados do jogador
    STILL = 0
    JUMPING = 1
    FALLING = 2

#CRIA AS CLASSES QUE SERÃO UTILIZADAS NO JOGO

    #CLASSE DOS INIMIGOS
    class Bixo(pygame.sprite.Sprite):
        def __init__(self, assets):
            # Construtor da classe mãe (Sprite).
            pygame.sprite.Sprite.__init__(self)

            bixo = assets['bixo']
            self.image = bixo[1]
            self.rect = self.image.get_rect()
            self.rect.x = random.randint(630, 670)
            self.rect.y = random.randint(200, 270)
            self.speedx = random.randint(-7, -5)
            self.speedy = random.randint(-3, 3)
            self.assets = assets
            self.i = 0

        #ATUALIZA A POSIÇÃO DOS BIXOS
        def update(self):
            # Atualizando a posição do bixo
            self.rect.x += self.speedx
            self.rect.y += self.speedy

            #FAZ O MOVIMENTO DE SUBIR E DESCER DOS BIXOS    
            if self.rect.top > 270:
                self.speedy = random.randint(-3, -1)
            elif self.rect.bottom < 200:
                self.speedy = random.randint(1, 3) 
            #FAZ A ANIMAÇÃO
            if self.i == 2:
                self.i = 0
                self.image = bixo[self.i]
            else:
                self.image = bixo[self.i]
                self.i += 1
            # SE PASSAR DA TELA CRIA OUTRO E SORTEIA A POSIÇÃO/VELOCIDADE
            if  self.rect.right < 0:
                self.rect.x = random.randint(630, 670)
                self.rect.y = random.randint(200, 270)
                self.speedx = random.randint(-7, -5)
                self.speedy = random.randint(-3, 3)
                
    #CLASSE DO "TIRO" -- TARTARUGA
    class Bullet(pygame.sprite.Sprite):
        def __init__(self, assets, bottom, centerx, true_right):
            pygame.sprite.Sprite.__init__(self)

            tartaruga_anim = assets['tartaruga_anim']
            self.image = tartaruga_anim[0]
            self.rect = self.image.get_rect()

            self.rect.centerx = centerx + 15
            self.rect.bottom = bottom + 45

            #VERIFICA SE ESTÁ VIRADO PARA A DIREITA OU ESQUERDA
            if true_right:
                self.speedx = 15
            else:
                self.speedx = -15
            self.i = 0

        #ATUALIZA A POSIÇÃO E ANIMA A TARTARUGA
        def update(self):
            self.rect.x += self.speedx
            if self.i == 3:
                self.i = 0
                self.image = tartaruga_anim[self.i]
            else:
                self.image = tartaruga_anim[self.i]
                self.i += 1

            #VERIFICA SE PASSOU DO LIMITE DA TELA
            if self.rect.right > WIDTH:
                self.kill()

    #CLASSE DO PLAYER

    class Luigi(pygame.sprite.Sprite):
        def __init__(self, groups, assets):
            pygame.sprite.Sprite.__init__(self)
            self.image = assets['luigidireita_img']
            self.rect = self.image.get_rect()
            self.rect.x = 10
            self.rect.bottom = HEIGHT - 10
            self.speedx = 0
            self.speedy = 0
            self.groups = groups
            self.assets = assets
            self.i = 1

            #LIMITA O NÚMERO DE TIROS
            self.last_shot = pygame.time.get_ticks()
            self.shoot_ticks = 500

        #ATUALIZA A POSIÇÃO DO JOGADOR
        def update(self):
            self.rect.x += self.speedx
            self.speedy += GRAVITY

            #VERIFICA OS ESTADOS DO JOGADOR
            #-------------------------------------------- CÓDIGO COPIADO DO GITHUB DA SALA, JUMP.PY
            if self.speedy > 0:
                self.state = FALLING
            self.rect.y += self.speedy
            # Se bater no chão, para de cair
            if self.rect.bottom > GROUND:
                # Reposiciona para a posição do chão
                self.rect.bottom = GROUND
                # Para de cair
                self.speedy = 0
                # Atualiza o estado para parado
                self.state = STILL
            #----------------------------------------------

            #Fazendo as animações
            if self.speedx>0:
                if self.state == STILL:
                    if self.i>2:
                        self.i=1
                        self.image = luigi_direita_anim[self.i]
                    else:
                        self.image = luigi_direita_anim[self.i]
                        self.i+=1
                else:
                    self.image = assets['luigi_pulando_direita']
            elif self.speedx <0:
                if self.state == STILL:
                    if self.i>1:
                        self.i=0
                        self.image = luigi_esquerda_anim[self.i]
                    else:
                        self.image = luigi_esquerda_anim[self.i]
                        self.i+=1
                else:
                    self.image = assets['luigi_pulando_esquerda']
            else:
                self.image = luigi_direita_anim[0]

            #MANTÉM O JOGADOR NA TELA
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.top < 175:
                self.rect.top = 175
            if self.rect.bottom > HEIGHT - 10:
                self.rect.bottom = HEIGHT - 10
        #FUNÇÃO DE PULO
        #------------------------------------------------- CÓDIGO COPIADO DO GITHUB DA SALA, JUMP.PY
        def jump(self):
            if self.state == STILL:
                self.speedy -= JUMP_SIZE
                self.state = JUMPING
                #TOCA O SOM DE PULO
                if volumes:
                    assets['pulo'].play()
                    assets['pulo'].set_volume(0.2)
        #-------------------------------------------------

        #FUNÇÃO DE TIRO, JOGA A TARTARUGA
        def shoot(self):
            # A nova bala vai ser criada logo acima e no centro horizontal da nave
            true_right = self.speedx>=0
                    # Verifica se pode atirar
            now = pygame.time.get_ticks()
            # Verifica quantos ticks se passaram desde o último tiro.
            elapsed_ticks = now - self.last_shot

            # Se já pode atirar novamente...
            if elapsed_ticks > self.shoot_ticks:
                # Marca o tick da nova imagem.
                self.last_shot = now
                #Posiciona a bala no chão
                new_bullet = Bullet(self.assets, self.rect.top, self.rect.centerx, true_right)
                self.groups['all_sprites'].add(new_bullet)
                self.groups['all_bullets'].add(new_bullet) 

    #DEFINE ESTADOS E PARÂMETROS QUE SERÃO UTILIZADOS DURANTE O JOGO
    DONE = 3
    PLAYING = 4
    state = PLAYING
    BIXOS = 3
    lives = 3
    keys_down = {}
    clock = pygame.time.Clock()

    # Variável para o ajuste de velocidade  (FPS)
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
        inimigo = Bixo(assets)
        all_sprites.add(inimigo)
        all_bixos.add(inimigo)
    luigi = Luigi(groups, assets)
    all_sprites.add(luigi)

    #VERIFICA SE O SOM ESTÁ LIGADO
    if volumes:
        pygame.mixer.music.play(loops=-1)
    # ===== Loop principal =====
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
            for bixos in hits: # As chaves são os elementos do primeiro grupo (bixos) que colidiram com alguma bala
                # O bixo morre e precisa ser recriado
                m = Bixo(assets)
                all_sprites.add(m)
                all_bixos.add(m)
                #VERIFICA SE O SOM ESTÁ LIGADO
                if volumes:
                    #SOM DE BIXO MORRENDO
                    assets['morre'].play()
                #ACRESCENTA 100 PONTOS AO SCORE POR MATAR UM BIXO
                score+=100
                #A CADA 1000 PONTOS ADICIONA UMA VIDA
                if score % 1000 == 0:
                    lives += 1
                    #VERIFICA SE O SOM ESTÁ LIGADO
                    if volumes:
                        #SOM DE VIDA GANHA
                        assets['vida_ganha'].play()
                    #SE TIVER MENOS QUE 4 BIXOS ADICIONA MAIS UM, AUMENTANDO A DIFICULDADE
                    if BIXOS<4:
                        BIXOS+=1
                        m = Bixo(assets)
                        all_sprites.add(m)
                        all_bixos.add(m)
            
            # Verifica colisão com o personagem
            hits = pygame.sprite.spritecollide(luigi, all_bixos, True)
            if len(hits) > 0:
                #VERIFICA O NÚMERO DE VIDAS
                if lives==1:
                    #VERIFICA SE O SOM ESTÁ LIGADO
                    if volumes:
                        #TOCA O SOM DE GAMEOVER
                        assets['fim'].play()
                    pygame.mixer.music.stop()
                    state = DONE
                    #INICIA A TELA DE GAMEOVER
                    gameover()
                else:
                    lives-=1
                    #VERIFICA SE O SOM ESTÁ LIGADO
                    if volumes:
                        #TOCA O SOM DE VIA PERDIDA
                        assets['vida_perde'].play()
                    #MATA O LUIGI
                    luigi.kill()
                    keys_down = {}
                    #CRIA OUTRO LUIGI NA POSIÇÃO INCIAL
                    luigi = Luigi(groups, assets) 
                    all_sprites.add(luigi)
                    #RECRIA O BIXO QUE MATOU O LUIGI
                    m = Bixo(assets)
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

        #DESENHA AS VIDAS
        assets['vidas'] = pygame.image.load('imagens/vidas.png').convert_alpha()
        assets['vidas'] = pygame.transform.scale(assets['vidas'], (25, 20))
        for a in range (0, lives):
            img = assets['vidas']
            img_rect = img.get_rect()
            img_rect.bottomleft = (10 + 25*a, HEIGHT - 10)
            window.blit(img, img_rect)

    


        pygame.display.update() # Mostra o novo frame para o jogador

#VOLTA PARA O MENU
main_menu ()





