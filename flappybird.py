#This is the FlappyBird game developed in Python

import pygame
from random import randint

pygame.init()

gameDisplay = pygame.display.set_mode((600,400))
pygame.display.set_caption("Flippy Bird")

size = [600,400];
screen = pygame.display.set_mode(size)
basicfont = pygame.font.SysFont(None, 48)



clock = pygame.time.Clock()
y_change =0
crashed = False

green = (0,102,102)
#loading images
background = pygame.image.load('background-night1.png')
base = pygame.image.load('base.png')
bird = pygame.image.load('bird.png')
pipe = pygame.image.load('pipe-green.png')
ReversedPipe=pygame.image.load('Reversed_pipe.png')
play=pygame.image.load('play.png').convert()
black = (0,0,0)
ground = 315

#setting variables
interiorSpace = randint(10,250);
exteriorSpace = randint(300,450);
x=0
y=1
a=0 #base x
b=350 #base y

 #Bird
c=150 #bird x
d=200 # bird y

 #Pipes
x1=300 #pipe down 1 x
y1=randint(250,350)  #pipe down 1 y

x2=300 # pipe up 1 x
y2= 0 - randint(0, 80) # pipe up 1 y


x3= x1 + exteriorSpace
y3 = y1

x4 = x2 + exteriorSpace
y4=y2

p1 = 250
p2 = 150

o=250
p=150

started = False
gameOn= True

#displaying images
def square(x,y):
    gameDisplay.blit(background,(x,y))
    gameDisplay.blit(bird,(c,d))
    gameDisplay.blit(pipe,(x1,y1))   #Pipe 1
    gameDisplay.blit(ReversedPipe,(x2,y2)) #pipe 2
    gameDisplay.blit(pipe, (x3, y3))  # Pipe 5
    gameDisplay.blit(ReversedPipe, (x4, y4))  # pipe 6
    gameDisplay.blit(base, (a, b))
    gameDisplay.blit(play, (p1, p2))

#redraw after clicked play
def redraw(x,y):
    gameDisplay.blit(background,(x,y))
    gameDisplay.blit(bird,(c,d))
    gameDisplay.blit(pipe,(x1,y1))   #Pipe 1
    gameDisplay.blit(ReversedPipe,(x2,y2)) #pipe 2
    gameDisplay.blit(pipe, (x3, y3))  # Pipe 5
    gameDisplay.blit(ReversedPipe, (x4, y4))  # pipe 6
    gameDisplay.blit(base, (a, b))

score = 0
test = True

#When bird hits the pipes
def collisionDetection():
    global score, test
    game = True
    if d >= ground:
        game = False
    if((((c+20)>=x1-(50/2) and (c)<= x1+50 and d >= (y1-25))) or ((c+20) >= x3-(50/2) and (c) <= x3 + 50 and d >=(y3-25))):
        game = False
    if(((c+20)>=x2-(50/2) and (c)<= x2+50 and d <= y2+190 ) or ((c+20) >= x4-(50/2) and (c) <= x4 + 50 and d <= y4+190)):
        game = False
    if(c > (x1+50) and test == True):
        score += 1
        test = False
    if(c > (x3+50) and test == False):
        score += 1
        test = True

    return game


def displayScore(score):
    if(gameOn == False):
        gameover()
    else:
        text_disp ="Score - {}".format(score)
        font = pygame.font.SysFont(None, 25)
        text = font.render(text_disp, True, black)
        gameDisplay.blit(text, [10, 10])

def gameover():
    font = pygame.font.SysFont(None, 25)
    text = font.render('GAME OVER', True, black)
    gameDisplay.blit(text, [250 , 200])

while not crashed:
        displayScore(score)
        gameDisplay.blit(bird, (c, d))
        folowing_space = randint(150, 250);
        if (gameOn):
            if (started):
                d += 2
                x1 -= 2
                x2 -= 2
                x3 -= 2
                x4 -= 2
            if(x1 <= 0 - randint(0,folowing_space)):
                x1 = 599
                y1= randint(220,300)
                x2 = x1
                y2 = 0 - randint(5, 85)

            if (x3 <= 0 - randint(0, folowing_space)):
                x3 = x1 + folowing_space
                y3 = randint(220, 350)
                x4 = x3
                y4 = 0 - randint(5, 70)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if(gameOn):
                square(x, y)
                if event.type == pygame.MOUSEBUTTONDOWN:
                   pos = pygame.mouse.get_pos()
                   if gameDisplay.blit(play, (p1, p2)).collidepoint(pos):
                     started = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        incr = d / 2;
                        if d - incr > 0:
                            d -= d / 100 + 60
                        else:
                            d = 0

                if event.type == pygame.KEYUP:
                    started = True
        gameOn = collisionDetection()
        gameDisplay.fill(green)
        if(gameOn):
            square(x,y)
        if(started == True):
            redraw(x, y)
        clock.tick(60)
        displayScore(score)
        pygame.display.update()
pygame.quit()
quit()