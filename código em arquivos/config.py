#Dados gerais
WIDTH = 620
HEIGHT = 310
FPS = 30

#Parâmetros
obstaculo_WIDTH = 50
obstaculo_HEIGHT = 38
luigi_WIDTH = 50
luigi_HEIGHT = 38

#Variáveis para a função pulo:
GRAVITY = 2
JUMP_SIZE = 20
GROUND = HEIGHT - 10
#Define os estados do jogador
STILL = 0
JUMPING = 1
FALLING = 2
#Outros estados
DONE = 3
PLAYING = 4
state = PLAYING

BIXOS = 3
score = 0
lives = 3