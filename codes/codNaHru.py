import pygame
import random

pygame.init()

win_x, win_y = 500,480
win = pygame.display.set_mode((win_x, win_y))

pygame.display.set_caption("MY Game")

char1 = pygame.image.load('box.png')
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

x = 400
y = 400
width = 64
height = 64
vel = 5
walkCount = 0
jumpCount = 10


clock = pygame.time.Clock()
isJump = False
left = False
right = False

#BOX
x1 = 100
y1 = 350
width1 = 100
height1 = 35

class MovingPlayer(pygame.Rect):

    def __init__(self, x, y, w, h, vel):
        # Calling the __init__ method of the parent class
        super().__init__(x, y, w, h)
        self.vel = vel

    def update(self):

        self.y += self.vel
        if self.y >= 480:     # If it's not in this area
            global missed
            self.y = 0
            self.x = random.randint(1,470)
            missed += 1

def redrawGameWindow():
    global walkCount

    win.blit(bg, (0,0))
    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount//3], (x,y))     #TO JE KED BUDE CHODIT ABY SA OBRAZKY STREIDALI
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x, y))
        walkCount = 0

    pygame.display.update()

def box():
    win.blit(char1, (x1, y1))
    pygame.display.update()
    
run = True
player = pygame.Rect(x, y, width, height)

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x + vel >= 0:
        left = True
        right = False
        x -= vel

    else:
        if keys[pygame.K_RIGHT] and x + width - vel <= win_x:
            left = False
            right = True
            x += vel
        else:
            left = False
            right = False


    if not(isJump):
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            print(jumpCount)
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False

    redrawGameWindow()
    box()    
    pygame.display.update()

pygame.quit()







