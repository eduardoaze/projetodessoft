# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
from config import PLAYING, WIDTH, HEIGHT, DONE
from telas import main_menu
from game_screen import game

pygame.init()
pygame.mixer.init()

# GERA A TELA
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Luigi Run')

state = PLAYING
while state != DONE:
    if state == PLAYING:
        state = main_menu(window)
    else:
        state = DONE
