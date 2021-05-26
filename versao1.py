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
background = pygame.image.load('imagens/ofundo.jpg').convert()
#obstaculo_img = pygame.image.load('').convert_alpha()
#obstaculo_img = pygame.transform.scale(obstaculo_img, (obstaculo_WIDTH, obstaculo_HEIGHT))
luigi_img = pygame.image.load('imagens/parado_direita.png').convert_alpha()
luigi_img = pygame.transform.scale(luigi_img, (luigi_WIDTH, luigi_HEIGHT))
# luigiparadopoder_img = pygame.image.load('imagens/paradopoder.jpg').convert_alpha()
# luigiparadopoder_img = pygame.transform.scale(luigi_img, (luigi_WIDTH, luigi_HEIGHT))
# luigiesquerda_img = pygame.image.load('imagens/esquerda.jpg').convert_alpha()
# luigiesquerda_img = pygame.transform.scale(luigi_img, (luigi_WIDTH, luigi_HEIGHT))
luigidireita_img = pygame.image.load('imagens/correndo_direita.png').convert()
luigidireita_img = pygame.image.load('imagens/correndo_direita.png').convert_alpha()
luigidireita_img = pygame.transform.scale(luigidireita_img, (luigi_WIDTH, luigi_HEIGHT))
tartaruga_img = pygame.image.load('imagens/tartaruga_direita.png').convert_alpha()
tartaruga_img = pygame.transform.scale(tartaruga_img, (50, 38))
class Bullet(pygame.sprite.Sprite):
    def __init__(self, img, bottom, centerx):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()

        self.rect.centerx = centerx + 15
        self.rect.bottom = bottom + 30
        self.speedx = 10

    def update(self):
        self.rect.x += self.speedx

        if self.rect.right > WIDTH:
            self.kill()

class Luigi(pygame.sprite.Sprite):
    def __init__(self, img, all_sprites, all_bullets, bullet_img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 10
        self.all_sprites = all_sprites
        self.all_bullets = all_bullets
        self.bullet_img = bullet_img

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
        new_bullet = Bullet(self.bullet_img, self.rect.top, self.rect.centerx)
        self.all_sprites.add(new_bullet)
        self.all_bullets.add(new_bullet)


game = True
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30
#Criando os grupos
all_sprites = pygame.sprite.Group()
all_bullets = pygame.sprite.Group()

luigi = Luigi(luigidireita_img, all_sprites, all_bullets, tartaruga_img)
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
                luigi.speedy -= 17
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
                luigi.speedy +=17

    # ----- Atualiza estado do jogo
    all_sprites.update()
    # ----- Gera saídas
    window.fill((255,255,255))  # Preenche com a cor branca
    window.blit(background,(0,0))


    #Desenha o Luigi
    all_sprites.draw(window)
    pygame.display.update() # Mostra o novo frame para o jogador
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados