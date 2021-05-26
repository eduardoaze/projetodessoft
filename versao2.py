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
assets['luigi_img'] = pygame.image.load('imagens/parado_direita.png').convert_alpha()
assets['luigi_img'] = pygame.transform.scale(assets['luigi_img'], (luigi_WIDTH, luigi_HEIGHT))
assets['luigidireita_img'] = pygame.image.load('imagens/correndo_direita.png').convert()
assets['luigidireita_img'] = pygame.image.load('imagens/correndo_direita.png').convert_alpha()
assets['luigidireita_img'] = pygame.transform.scale(assets['luigidireita_img'], (luigi_WIDTH, luigi_HEIGHT))
tartaruga_anim = []
for i in range(1, 4):
    filename = 'imagens/tartaruga0{}.png'.format(i)
    img = pygame.image.load(filename).convert_alpha()
    img = pygame.transform.scale(img, (50,38))
    tartaruga_anim.append(img)
assets['tartaruga_anim'] = tartaruga_anim

class Bullet(pygame.sprite.Sprite):
    def __init__(self, assets, bottom, centerx):
        pygame.sprite.Sprite.__init__(self)

        tartaruga_anim = assets['tartaruga_anim']
        self.image = tartaruga_anim[0]
        self.rect = self.image.get_rect()

        self.rect.centerx = centerx + 15
        self.rect.bottom = bottom + 30
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

    def update(self):
        self.rect.x += self.speedx
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

class Explosion(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, center, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Armazena a animação de explosão
        self.explosion_anim = assets['tartaruga_anim']

        # Inicia o processo de animação colocando a primeira imagem na tela.
        self.frame = 0  # Armazena o índice atual na animação
        self.image = self.explosion_anim[self.frame]  # Pega a primeira imagem
        self.rect = self.image.get_rect()
        self.rect.center = center  # Posiciona o centro da imagem

        # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        # Quando pygame.time.get_ticks() - self.last_update > self.frame_ticks a
        # próxima imagem da animação será mostrada
        self.frame_ticks = 50

    def update(self):
        # Verifica o tick atual.
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update

        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Verifica se já chegou no final da animação.
            if self.frame == len(self.explosion_anim):
                # Se sim, tchau explosão!
                self.kill()
            else:
                # Se ainda não chegou ao fim da explosão, troca de imagem.
                center = self.rect.center
                self.image = self.explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


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