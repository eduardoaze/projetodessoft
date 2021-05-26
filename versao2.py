#imports
import pygame
import random
import time

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
WIDTH = 620
HEIGHT = 310
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Luigi Run')
screen = pygame.display.set_mode((620, 310),0,32)


# ----- Inicia assets
obstaculo_WIDTH = 50
obstaculo_HEIGHT = 38
luigi_WIDTH = 50
luigi_HEIGHT = 38
font = pygame.font.SysFont(None, 48)
assets = {}
assets['background'] = pygame.image.load('imagens/ofundo.jpg').convert()
assets['luigi_img'] = pygame.image.load('imagens/luigi00.png').convert_alpha()
assets['luigi_img'] = pygame.transform.scale(assets['luigi_img'], (luigi_WIDTH, luigi_HEIGHT))
assets['luigidireita_img'] = pygame.image.load('imagens/luigi02.png').convert()
assets['luigidireita_img'] = pygame.image.load('imagens/luigi02.png').convert_alpha()
assets['luigidireita_img'] = pygame.transform.scale(assets['luigidireita_img'], (luigi_WIDTH, luigi_HEIGHT))

#Lista para a animação de andar para a esquerda

luigi_esquerda_anim = []
for i in range(3, 5):
    filename = 'imagens/luigi0{}.png'.format(i)
    img = pygame.image.load(filename).convert_alpha()
    img = pygame.transform.scale(img, (50,38))
    luigi_esquerda_anim.append(img)

#Lista para a animação de andar para a direita e ficar parado

luigi_direita_anim = []
for i in range(0, 3):
    filename = 'imagens/luigi0{}.png'.format(i)
    img = pygame.image.load(filename).convert_alpha()
    img = pygame.transform.scale(img, (50,38))
    luigi_direita_anim.append(img)

#Lista para a animação da tartaruga

tartaruga_anim = []
for i in range(1, 4):
    filename = 'imagens/tartaruga0{}.png'.format(i)
    img = pygame.image.load(filename).convert_alpha()
    img = pygame.transform.scale(img, (50,38))
    tartaruga_anim.append(img)
assets['tartaruga_anim'] = tartaruga_anim

#Classe do tiro = tartaruga

class Bullet(pygame.sprite.Sprite):
    def __init__(self, assets, bottom, centerx):
        pygame.sprite.Sprite.__init__(self)

        tartaruga_anim = assets['tartaruga_anim']
        self.image = tartaruga_anim[0]
        self.rect = self.image.get_rect()

        self.rect.centerx = centerx + 15
        self.rect.bottom = bottom + 45
        self.speedx = 10
        self.i = 0

    def update(self):
        self.rect.x += self.speedx
        if self.i == 3:
            self.i = 0
            self.image = tartaruga_anim[self.i]
        else:
            self.image = tartaruga_anim[self.i]
            self.i += 1

        
        if self.rect.right > WIDTH:
            self.kill()

#Classe do player = Luigi

class Luigi(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['luigidireita_img']
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 10
        self.groups = groups
        self.assets = assets
        self.i = 1
    def update(self):
        self.rect.x += self.speedx

        #Fazendo as animações
        if self.speedx>0:
            if self.i>2:
                self.i=1
                self.image = luigi_direita_anim[self.i]
            else:
                self.image = luigi_direita_anim[self.i]
                self.i+=1
        elif self.speedx <0:
            if self.i>1:
                self.i=0
                self.image = luigi_esquerda_anim[self.i]
            else:
                self.image = luigi_esquerda_anim[self.i]
                self.i+=1
        else:
            self.image = luigi_direita_anim[0]
        self.rect.y += self.speedy

        #Matem na tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 175:
            self.rect.top = 175
        if self.rect.bottom > HEIGHT - 10:
            self.rect.bottom = HEIGHT - 10

    def shoot(self):
        # A nova bala vai ser criada logo acima e no centro horizontal da nave
        new_bullet = Bullet(self.assets, self.rect.top, self.rect.centerx)
        self.groups['all_sprites'].add(new_bullet)
        self.groups['all_bullets'].add(new_bullet)

game = True
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30
#Criando os grupos
all_sprites = pygame.sprite.Group()
all_bullets = pygame.sprite.Group()
groups = {}
groups['all_sprites'] = all_sprites
groups['all_bullets'] = all_bullets

luigi = Luigi(groups, assets)
all_sprites.add(luigi)

# ===== Loop principal =====

while game:
    clock.tick(FPS)

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                luigi.speedx -= 8
            if event.key == pygame.K_RIGHT:
                luigi.speedx += 8
            if event.key == pygame.K_UP:
                luigi.speedy -= 25
            if event.key == pygame.K_SPACE:
                luigi.shoot()
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                luigi.speedx += 8
            if event.key == pygame.K_RIGHT:
                luigi.speedx -= 8
            if event.key == pygame.K_UP:
                luigi.speedy +=25

    # ----- Atualiza estado do jogo
    all_sprites.update()
    # ----- Gera saídas
    window.fill((255,255,255))  # Preenche com a cor branca
    window.blit(assets['background'],(0,0))


    #Desenha o Luigi
    all_sprites.draw(window)
    pygame.display.update() # Mostra o novo frame para o jogador
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados