import random
import pygame
# from assets import bixo, tartaruga_anim, luigi_direita_anim, assets, luigi_esquerda_anim
from config import WIDTH, HEIGHT, GRAVITY, FALLING, GROUND, STILL, JUMP_SIZE, JUMPING

class Meteor(pygame.sprite.Sprite):
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

        def update(self):
            # Atualizando a posição do meteoro
            self.rect.x += self.speedx
            self.rect.y += self.speedy

            if self.rect.top > 270:
                self.speedy = random.randint(-3, -1)
            elif self.rect.bottom < 200:
                self.speedy = random.randint(1, 3) 
            # Se o meteoro passar do final da tela, volta para cima e sorteia
            if self.i == 2:
                self.i = 0
                self.image = bixo[self.i]
            else:
                self.image = bixo[self.i]
                self.i += 1
            # novas posições e velocidades
            if  self.rect.right < 0:
                self.rect.x = random.randint(630, 670)
                self.rect.y = random.randint(200, 270)
                self.speedx = random.randint(-7, -5)
                self.speedy = random.randint(-3, 3)
                

class Bullet(pygame.sprite.Sprite):
    def __init__(self, assets, bottom, centerx, true_right):
        pygame.sprite.Sprite.__init__(self)

        tartaruga_anim = assets['tartaruga_anim']
        self.image = tartaruga_anim[0]
        self.rect = self.image.get_rect()

        self.rect.centerx = centerx + 15
        self.rect.bottom = bottom + 45
        if true_right:
            self.speedx = 15
        else:
            self.speedx = -15
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
        self.speedy = 0
        self.groups = groups
        self.assets = assets
        self.i = 1

        #Limita o numero de tiros
        self.last_shot = pygame.time.get_ticks()
        self.shoot_ticks = 500

    def update(self):
        self.rect.x += self.speedx
        self.speedy += GRAVITY

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

        #Matem na tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 175:
            self.rect.top = 175
        if self.rect.bottom > HEIGHT - 10:
            self.rect.bottom = HEIGHT - 10

    def jump(self):
        if self.state == STILL:
            self.speedy -= JUMP_SIZE
            self.state = JUMPING
            assets['pulo'].play()

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