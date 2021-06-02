import pygame, sys

mainclock = pygame.time.Clock()
from pygame.locals import *
pygame.init ()
pygame.display.set_caption ('game base')
screen = pygame.display.set_mode((500, 500), 0, 32)

font = pygame.font.SysFont (None, 20)
fundo = pygame.image.load('imagens/inicio.jpg').convert()
def draw_text (text, font, color, surface, x, y):
    textobj = font.render (text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit (textobj, textrect)

click = False

def main_menu ():
    while True:
        screen.blit ((fundo),(0,0))
        draw_text ('Luigi run', font, (255, 255, 255), screen, 20, 20)
        
        mx, my = pygame.mouse.get_pos()
        
        button_1 = pygame.Rect (50, 250, 150, 40)
        button_2 = pygame.Rect (275, 250, 150, 40)
        if button_1.collidepoint (mx,my):
            if click:
                game()
        if button_2.collidepoint (mx,my):
            if click :
                options()
        pygame.draw.rect(screen, (0,150,0), button_1)
        pygame.draw.rect(screen, (0,150,0), button_2)

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

def game ():
    running = True
    while running:
        screen.fill ((0,0,0))

        draw_text ('game', font, (255, 255, 255), screen, 20, 20)
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
                    running = False
        pygame.display.update()
        mainclock.tick (60)

def options ():
    running = True
    while running:
        screen.fill ((0,0,0))

        draw_text ('options', font, (255, 255, 255), screen, 20, 20)
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
                    running = False
        pygame.display.update()
        mainclock.tick (60)
        



main_menu ()              