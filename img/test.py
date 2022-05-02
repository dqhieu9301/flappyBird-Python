
import pygame, sys, random
from pygame.locals import *

WINDOWWIDTH = 400
WINDOWHEIGHT = 600

BIRDWIDTH = 60
BIRDHEIGHT = 45
G = 0.5
SPEEDFLY = -8
BIRDIMG = pygame.image.load('./BTL/img/bird.png')

COLUMNWIDTH = 60
COLUMNHEIGHT = 500
BLANK = 160
DISTANCE = 200
COLUMNSPEED = 2
COLUMNIMG = pygame.image.load('./BTL/img/column.png')

BACKGROUND = pygame.image.load('./BTL/img/background.png')

LASERWIDTH = 27
LASERHEIGHT = 7
LASERSPEED = 2
LASERIMG = pygame.image.load('./BTL/img/laser.png')
pygame.init()
FPS = 60
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Flappy Bird')
class Laser():
    def __init__(self , Bird):
        self.width = LASERWIDTH
        self.height = LASERHEIGHT
        self.x = Bird.x
        self.y = Bird.y
        self.speed = LASERSPEED
        self.suface = LASERIMG
    def draw(self):
        DISPLAYSURF.blit(self.suface , (int(self.x) ,int(self.y)))
    def update(self):
        self.x += self.speed
class Bird():
    def __init__(self):
        self.width = BIRDWIDTH
        self.height = BIRDHEIGHT
        self.x = (WINDOWWIDTH - self.width)/2
        self.y = (WINDOWHEIGHT- self.height)/2
        self.speed = 0
        self.suface = BIRDIMG

    def draw(self):
        DISPLAYSURF.blit(self.suface, (int(self.x), int(self.y)))
    
    def update(self, mouseClick):
        self.y += self.speed + 0.5*G
        self.speed += G
        if mouseClick == True:
            self.speed = SPEEDFLY


def gameStart(bird):
    bird.__init__()

    font = pygame.font.SysFont('consolas', 60)
    headingSuface = font.render('FLAPPY BIRD', True, (255, 0, 0))
    headingSize = headingSuface.get_size()
    
    font = pygame.font.SysFont('consolas', 20)
    commentSuface = font.render('Click to start', True, (0, 0, 0))
    commentSize = commentSuface.get_size()
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                return

        DISPLAYSURF.blit(BACKGROUND, (0, 0))
        bird.draw()
        DISPLAYSURF.blit(headingSuface, (int((WINDOWWIDTH - headingSize[0])/2), 100))
        DISPLAYSURF.blit(commentSuface, (int((WINDOWWIDTH - commentSize[0])/2), 500))

        pygame.display.update()
        fpsClock.tick(FPS)

def gamePlay(bird, laser):
    bird.__init__()
    bird.speed = SPEEDFLY
    laser.__init__(bird)
    CheckLaser = False
    while True:
        mouseClick = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                mouseClick = True
            if event.type == KEYDOWN:
                if(event.key == pygame.K_RIGHT):
                    CheckLaser = True
        DISPLAYSURF.blit(BACKGROUND, (0, 0))
    
        bird.draw()
        bird.update(mouseClick)
      
        if CheckLaser :
            laser.draw()
            laser.update()
            if laser.x > WINDOWWIDTH: 
                laser.__init__(bird)
                CheckLaser = False

        pygame.display.update()
        fpsClock.tick(FPS)


def main():
    bird = Bird()

    laser = Laser(bird)
    while True:
        gameStart(bird)
        gamePlay(bird, laser)
      

if __name__ == '__main__':
    main()