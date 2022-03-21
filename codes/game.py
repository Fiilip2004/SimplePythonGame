import pygame


pygame.init()

win = pygame.display.set_mode((500,480))

pygame.display.set_caption("MY Game")

char1 = pygame.image.load('box.png') #BOX
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')
clock = pygame.time.Clock()

class box(object): #trieda ktora mi das box
    def __init__(self,x,y,width,height): # def na pozicie boxu
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def draw(self,win):    #def na nakreslenie boxu
        win.blit(char1, (self.x, self.y))

    
class player(object):
    def __init__(self,x,y,width,height):
        self.x = x                
        self.y = y
        self.width = width  #ŠIRKA
        self.height = height #VÝŠKA
        self.vel = 5
        self.jumpCount = 10
        self.walkCount = 1
        self.isJump = False
        self.left = False
        self.right = False
        self.leftstop = False
        self.rightMove = False

    def draw(self,win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        
        if self.left:  
            self.x = round(self.x)
            self.y = round(self.y)
            win.blit(walkLeft[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            self.x = round(self.x)
            self.y = round(self.y)
            win.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
            
        elif self.rightMove:
            win.blit(walkRight[self.walkCount//3], (self.x,self.y))
            
        else:
            self.x = round(self.x)
            self.y = round(self.y)
            win.blit(char, (self.x, self.y))
              

        

def redrawGameWindow():    
    win.blit(bg, (0,0))
    box.draw(win) # --> tu mam kod ktory z def mi bude kreslit box ale 
    man.draw(win) # --> musim ho ešte aj nazvat box.___
    pygame.display.update()

    

box = box(300, 300, 64 ,64)  # --> tu menujem box box čo potom plati pri box.draw
run = True
man = player(200, 410, 64 ,64)

while run:
    
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    #LEFT MOVE
    if keys[pygame.K_LEFT] and man.x > -10:
        if man.x > box.x + 50 and man.y < box.y:  # musim dat (aby sa mohol hybat pri skoku) a ked mie je viec ako x + x +100...
            man.left = False
            man.right = False          
        else:
            man.x -= man.vel
            man.left = True
            man.right = False

        
        
        
    #IF KEYS LEFT PRESSED AND LEFT == FALSE
    elif keys[pygame.K_LEFT] and man.x <= man.vel - 5:
        man.left = True
        man.right = False


    #RIGHT MOVE
    elif keys[pygame.K_RIGHT] and man.x < 450:
        print(man.x , man.y, box.x, box.y)
        if man.x + 50 > box.x and man.y < box.y:
            man.left = False
            man.right = False
        else:
            man.x += man.vel
            man.left = False
            man.right = True
        

    #elif keys[pygame.K_RIGHT] and man.right == False:
     #   man.rightMove = True
      #  man.walkCount += 1
       # man.right = False
        #man.left = False

       
    #IF KEYS RIGHT PRESSED AND RIGHT == FALSE        
    elif keys[pygame.K_RIGHT] and man.x <= 450:
        man.left = False
        man.right = True

    else:
        man.left = False
        man.right = False
        man.walkCount = 0
        man.rightMove = False
    
    if not(man.isJump):
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            man.isJump = True
            man.left = False
            man.right = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            man.y -= (man.jumpCount * abs(man.jumpCount)) * 0.5
            man.jumpCount -= 1
        else: 
            man.jumpCount = 10
            man.isJump = False

    redrawGameWindow()

    
    
pygame.quit()





