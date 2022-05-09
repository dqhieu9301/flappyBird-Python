import pygame, sys
from pygame.locals import *
pygame.init()
FPS = 60
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((400, 400))

def rectCollision(rect1, rect2):
    if rect1[0] <= rect2[0]+rect2[2] and rect2[0] <= rect1[0]+rect1[2] and rect1[1] < rect2[1]+rect2[3] and rect2[1] < rect1[1]+rect1[3]:
        return True
    return False

rect1 = [0, 0, 80, 50] # Hình chữ nhật di chuyển
rect2 = [150, 150, 90, 60] # Hình chữ nhật đứng yên

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.fill((0, 0, 0))

    rect1[0], rect1[1] = pygame.mouse.get_pos() # Lấy vị trí của chuột

    pygame.draw.rect(DISPLAYSURF, (255, 255, 0), rect2)
    if rectCollision(rect1, rect2) == True:
        pygame.draw.rect(DISPLAYSURF, (255, 0, 0), rect1)
    else:
        pygame.draw.rect(DISPLAYSURF, (0, 255, 0), rect1)

    pygame.display.update()
    fpsClock.tick(FPS)