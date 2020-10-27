import sys, os

#Desactive les outputs de la console 

print('\x1b[1;32;40m'+'ENJOY!'+'\x1b[0m'+' See more at  : https://edenannonay.com')

sys.stdout = open(os.devnull, "w")
sys.stderr = open(os.devnull, "w")

import pygame
from PIL import Image





# Initialise pygame
pygame.init()

# Titre et icone

pygame.display.set_caption('GTFO - Green The Farmer Odyssey')

icon = pygame.image.load('images/cow.png')

pygame.display.set_icon(icon)

# creation de l'ecran
screen = pygame.display.set_mode((800,600))
screenWidth = 800
screenHeight = 600



# Fonction qui ajoute les arbres 

def ajoutObjet(nomImg,horizontal,vertical):

    arbreImg = pygame.image.load(nomImg)
    arbreImgX = horizontal
    arbreImgY = vertical
    screen.blit(arbreImg,(arbreImgX,arbreImgY))


# Fonction qui ajoute le joueur

def ajoutJoueur(nomImg,horizontal,vertical):

    playerImg = pygame.image.load(nomImg)
    playerImgX = horizontal
    playerImgY = vertical
    screen.blit(playerImg,(playerImgX,playerImgY))


# compteurs et animation

vel=5
WalkLeft = [pygame.image.load('images/main_char_LSide_walkLLeg.png'),pygame.image.load('images/main_char_LSide.png'),pygame.image.load('images/main_char_LSide_walkRLeg.png'),pygame.image.load('images/main_char_LSide.png'),pygame.image.load('images/main_char_LSide_walkLLeg.png'),pygame.image.load('images/main_char_LSide.png'),pygame.image.load('images/main_char_LSide_walkRLeg.png'),pygame.image.load('images/main_char_LSide.png'),pygame.image.load('images/main_char_LSide_walkLLeg.png'),pygame.image.load('images/main_char_LSide.png'),pygame.image.load('images/main_char_LSide_walkLLeg.png'),pygame.image.load('images/main_char_LSide.png'),pygame.image.load('images/main_char_LSide_walkRLeg.png'),pygame.image.load('images/main_char_LSide.png'),pygame.image.load('images/main_char_LSide_walkLLeg.png'),pygame.image.load('images/main_char_LSide.png'),pygame.image.load('images/main_char_LSide_walkRLeg.png'),pygame.image.load('images/main_char_LSide.png'),pygame.image.load('images/main_char_LSide_walkLLeg.png'),pygame.image.load('images/main_char_LSide.png')]
WalkRight = [pygame.image.load('images/main_char_RSide_walkLLeg.png'),pygame.image.load('images/main_char_RSide.png'),pygame.image.load('images/main_char_RSide_walkRLeg.png'),pygame.image.load('images/main_char_RSide.png'),pygame.image.load('images/main_char_RSide_walkLLeg.png'),pygame.image.load('images/main_char_RSide.png'),pygame.image.load('images/main_char_RSide_walkRLeg.png'),pygame.image.load('images/main_char_RSide.png'),pygame.image.load('images/main_char_RSide_walkLLeg.png'),pygame.image.load('images/main_char_RSide.png'),pygame.image.load('images/main_char_RSide_walkLLeg.png'),pygame.image.load('images/main_char_RSide.png'),pygame.image.load('images/main_char_RSide_walkRLeg.png'),pygame.image.load('images/main_char_RSide.png'),pygame.image.load('images/main_char_RSide_walkLLeg.png'),pygame.image.load('images/main_char_RSide.png'),pygame.image.load('images/main_char_RSide_walkRLeg.png'),pygame.image.load('images/main_char_RSide.png'),pygame.image.load('images/main_char_RSide_walkLLeg.png'),pygame.image.load('images/main_char_RSide.png')]
WalkUp = [pygame.image.load('images/main_char_back_walkLLeg.png'),pygame.image.load('images/main_char_back.png'),pygame.image.load('images/main_char_back_walkRLeg.png'),pygame.image.load('images/main_char_back.png'),pygame.image.load('images/main_char_back_walkLLeg.png'),pygame.image.load('images/main_char_back.png'),pygame.image.load('images/main_char_back_walkRLeg.png'),pygame.image.load('images/main_char_back.png'),pygame.image.load('images/main_char_back_walkLLeg.png'),pygame.image.load('images/main_char_back.png'),pygame.image.load('images/main_char_back_walkLLeg.png'),pygame.image.load('images/main_char_back.png'),pygame.image.load('images/main_char_back_walkRLeg.png'),pygame.image.load('images/main_char_back.png'),pygame.image.load('images/main_char_back_walkLLeg.png'),pygame.image.load('images/main_char_back.png'),pygame.image.load('images/main_char_back_walkRLeg.png'),pygame.image.load('images/main_char_back.png'),pygame.image.load('images/main_char_back_walkLLeg.png'),pygame.image.load('images/main_char_back.png')]
WalkDown = [pygame.image.load('images/main_char_front_walkLLeg.png'),pygame.image.load('images/main_char_front.png'),pygame.image.load('images/main_char_front_walkRLeg.png'),pygame.image.load('images/main_char_front.png'),pygame.image.load('images/main_char_front_walkLLeg.png'),pygame.image.load('images/main_char_front.png'),pygame.image.load('images/main_char_front_walkRLeg.png'),pygame.image.load('images/main_char_front.png'),pygame.image.load('images/main_char_front_walkLLeg.png'),pygame.image.load('images/main_char_front.png'),pygame.image.load('images/main_char_front_walkLLeg.png'),pygame.image.load('images/main_char_front.png'),pygame.image.load('images/main_char_front_walkRLeg.png'),pygame.image.load('images/main_char_front.png'),pygame.image.load('images/main_char_front_walkLLeg.png'),pygame.image.load('images/main_char_front.png'),pygame.image.load('images/main_char_front_walkRLeg.png'),pygame.image.load('images/main_char_front.png'),pygame.image.load('images/main_char_front_walkLLeg.png'),pygame.image.load('images/main_char_front.png')]
WalkCount = 0
WalkCount1 = 0

left = False
right = False
up = False
down = False
clock = pygame.time.Clock()




# Fonction qui créée les maps 

def ajoutMap(numMap):
    
    if numMap == 1 :

        
        

        # Différentes largeurs
        h1=0
        h2=0
        h3=0
        h4=0

        # Différentes longueurs
        l1=74
        l2=0

        # 1re rangee arbre vertical
        
        #  tree_1 45*58
        
        for i in range(16):
            ajoutObjet('images/tree_2.png',0,h1)
            h1=h1+36

       
        # 2e rangee arbre vertical 
        for i in range(16):
            ajoutObjet('images/tree_2.png',38,h2)
            h2=h2+36

        # 3eme rangee arbre vertical
        for i in range(15):
            ajoutObjet('images/tree_2.png',758,h3)
            h3=h3+36
        # 4eme rangee arbre vertical
        for i in range(15):
            ajoutObjet('images/tree_2.png',720,h4)
            h4=h4+36
            
        # 1re rangee arbre horizontal
        for i in range(19):
            ajoutObjet('images/tree_2.png',l1,540)
            l1=l1+38
        l1=76
        for i in range(6):
            ajoutObjet('images/tree_2.png',l1,0)
            l1=l1+38
        l1 = 492.5
        for i in range(6):
            ajoutObjet('images/tree_2.png',l1,0)
            l1=l1+38
            
# Redessine/refresh la fenetre

def redraw():

    global WalkCount
    global WalkCount1

    ajoutObjet('images/House.png',270,134.5)


    if WalkCount + 1 >= 60:
        WalkCount = 0
    if left:  # If we are facing left
        screen.blit(WalkLeft[WalkCount//3], (playerX,playerY))  # We integer divide walkCounr by 3 to ensure each
        WalkCount += 1                           # image is shown 3 times every animation
    elif right:
        screen.blit(WalkRight[WalkCount//3], (playerX,playerY))
        WalkCount += 1
    
    
    
    elif up:  # If we are facing left
        screen.blit(WalkUp[WalkCount//3], (playerX,playerY))  # We integer divide walkCounr by 3 to ensure each
        WalkCount += 1                           # image is shown 3 times every animation
    elif down:
        screen.blit(WalkDown[WalkCount//3], (playerX,playerY))
        WalkCount += 1
    
    else :
        
        ajoutJoueur(sprite,playerX,playerY)
    
    
    playerHitbox = (playerX,playerY,width,height)
    
    

    ajoutMap(1)
    
    
    pygame.display.update()

# Variables permettant de positionner le joueur
playerX = 380
playerY = 239.5
playerX_change = 0
playerY_change = 0

    
# differents sprites 

sprite ='images/main_char_front.png'
im = Image.open(sprite)
width, height = im.size 



# Boucle permettant de faire tourner le jeu
running = True
while running:
    
    clock.tick(60)
    screen.blit(pygame.image.load('images/grass_done2.png'),(0,0))
    
    limit = screenWidth - vel - width
    

    # Rempli l'ecran avec de la couleur
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Gere les touches appuyes


    keys = pygame.key.get_pressed()

    # Code gerant les frontieres

    if (playerY < vel or playerY <= 54.5 or (playerY <= 249.5 and playerY>=84.5 and playerX>=245 and playerX<=480)) and up == True  :
        vel = 0 
        sprite='images/main_char_back.png'
    elif (playerY > screenHeight - height - vel or playerY >= 504.5 or (playerY >= 74.5 and playerY<=239.5 and playerX>=240 and playerX<=475 ))  and down == True  :
        vel = 0
        sprite='images/main_char_front.png'
    else :
        vel = 5

    if (playerX ==5 or playerX <= 70 or (playerX>=230 and playerX<=485 and playerY<=239.5 and playerY>=84.5)) and left == True  :
        vel = 0
        sprite='images/main_char_LSide.png'
    elif (playerX == limit or playerX >= 685 or (playerX>=230 and playerX<=485 and playerY>=84.5 and playerY<=239.5)) and right == True :
        vel = 0
        sprite='images/main_char_RSide.png'
    
   



    # Fin du code gerant les frontieres
        
        
    
    if keys[pygame.K_z] and playerY > vel  :
        playerY_change = -vel
        playerX_change = 0
        up = True 
        down = False
        left = False
        right =False
        
    
    elif keys[pygame.K_s] and playerY < screenHeight - height - vel   :
        playerY_change = vel
        playerX_change = 0
        up = False
        down = True 
        left = False
        right =False   
    else :
        up = False
        down = False

    if keys[pygame.K_q] and playerX > vel  :
        playerX_change = -vel
        playerY_change = 0
        left = True 
        right = False
        up = False
        down =False
    
    elif keys[pygame.K_d] and playerX < screenWidth - vel - width  :
        playerX_change = vel        
        playerY_change = 0
        left = False
        right = True   
        up = False
        down =False 
    else :
        left = False
        right = False

    if event.type == pygame.KEYUP :
        if event.type == pygame.KEYUP :
            if event.key == pygame.K_z :
                
                playerX_change = 0
                playerY_change = 0
                sprite = 'images/main_char_back.png'
                
                

            if event.key == pygame.K_s  :
                
                playerX_change = 0
                playerY_change = 0
                sprite = 'images/main_char_front.png'
                

            if event.key == pygame.K_q :
                
                playerX_change = 0
                playerY_change = 0
                sprite = 'images/main_char_LSide.png'
                

            if event.key == pygame.K_d :
                
                playerX_change = 0
                playerY_change = 0
                sprite = 'images/main_char_RSide.png'
                
                
            

    
    
      
    playerX = playerX + playerX_change   
    playerY = playerY + playerY_change
        

     

    # Refresh
    
    redraw()
