from pathlib import Path
import pygame

#Constants
SQR_SIZE = 64
BOARD_LEN = 8
WIDTH = 640
HEIGTH = 640
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#Initialization
pygame.init()
pygame.mixer.init()

#caption
pygame.display.set_caption("Online Chess")

#Global Variables
screen = pygame.display.set_mode((WIDTH, HEIGTH))
                                 
black_pawn = pygame.image.load(Path('src/pieces/black/p.png'))
black_knight = pygame.image.load(Path('src/pieces/black/n.png'))
black_bishop = pygame.image.load(Path('src/pieces/black/b.png'))
black_rook = pygame.image.load(Path('src/pieces/black/r.png'))
black_queen = pygame.image.load(Path('src/pieces/black/q.png'))
black_king = pygame.image.load(Path('src/pieces/black/k.png'))


white_pawn = pygame.image.load(Path('src/pieces/white/p.png'))
white_knight = pygame.image.load(Path('src/pieces/white/n.png'))
white_bishop = pygame.image.load(Path('src/pieces/white/b.png'))
white_rook = pygame.image.load(Path('src/pieces/white/r.png'))
white_queen = pygame.image.load(Path('src/pieces/white/q.png'))
white_king = pygame.image.load(Path('src/pieces/white/k.png'))

check_sound = pygame.mixer.Sound(Path('src/sound/checked.wav'))
# check_mate_sound = pygame.mixer.music.load(Path('src/sound/check_mate.wav'))
move_sound = pygame.mixer.Sound(Path('src/sound/move.wav'))
take_sound = pygame.mixer.Sound(Path('src/sound/take.wav'))

#Game Logic Functions
def board_draw():
    cnt = 0
    for i in range(1, BOARD_LEN+1):
        for z in range(1, BOARD_LEN+1):
            if cnt % 2 == 0:
                pygame.draw.rect(screen, WHITE, (SQR_SIZE*z,SQR_SIZE*i,SQR_SIZE,SQR_SIZE))
            else:
                pygame.draw.rect(screen, BLACK, (SQR_SIZE*z,SQR_SIZE*i,SQR_SIZE,SQR_SIZE))
            cnt +=1
        cnt -= 1
    pygame.draw.rect(screen,BLACK,(64, 64, BOARD_LEN*64, BOARD_LEN*64), 1)
#Screen drawing Function
def draw():
    screen.fill((200,200,200))
    board_draw()
    pygame.display.update()

#Game main loop
def main():
    #Main Local Variables
    run = True
    clock = pygame.time.Clock()
    #The Game Loop
    while run:
        clock.tick(FPS)
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                run = False
            if ev.type == pygame.KEYDOWN:
                pass
        draw()
    
    pygame.quit()

main()

