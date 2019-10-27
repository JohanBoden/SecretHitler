import pygame
import random
from class_GUI import *

import Client
import time
pygame.init()


# Define some colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREY = (100,100,100)
BLUE = ( 0, 0, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

print("IS CLIENT")
Client.connect()

room_width = 1280
room_height = 720

#fascist board/law size
fasBoardWidth = room_width-450
fasBoardHeight = 260
fasBoardX = room_width-fasBoardWidth
fasBoardY = 0
fasCardX = fasBoardWidth*0.06987952
fasCardY = fasBoardHeight*0.21153846
fasCardWidth = fasBoardWidth*0.1253012
fasCardHeight = fasBoardHeight*0.58461538
offsetFas = fasBoardWidth*0.146988

#liberal board/law size
libBoardWidth = room_width-450
libBoardHeight = 260
libBoardX = room_width-libBoardWidth
libBoardY = 260
libCardX = libBoardWidth*0.144578
libCardY = libBoardHeight*0.211538
libCardWidth = libBoardWidth*0.1253012
libCardHeight = libBoardHeight*0.58461538
offsetLib = libBoardWidth*0.146988

size = (room_width, room_height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Secret Hitler XD")
fascistBoard = pygame.image.load("sprites\sprFasSpelplan.png")
liberalBoard = pygame.image.load("sprites\sprLibSpelplan.png")
fascistBoard = pygame.transform.scale(fascistBoard, (fasBoardWidth,fasBoardHeight))
liberalBoard = pygame.transform.scale(liberalBoard, (libBoardWidth,libBoardHeight))
fascistLaw = pygame.image.load("sprites\sprFasRegel.png")
liberalLaw = pygame.image.load("sprites\sprLibRegel.png")
fascistLaw = pygame.transform.scale(fascistLaw, (int(fasCardWidth),int(fasCardHeight)))
liberalLaw = pygame.transform.scale(liberalLaw, (int(libCardWidth),int(libCardHeight)))
logo = pygame.image.load("sprites\sprLogo.png")
logo = pygame.transform.scale(logo, (300,200))
libLaw = 0
fasLaw = 0
libPressed = 0
fasPressed = 0
cardPressed = 0
randCard = 0
picking = 0
indexCard = [0,0,0]
drawCard = False
discarded = 0

victoryFont = pygame.font.Font("Fonts/fontSH.ttf",64,bold=True)
libVictoryText = victoryFont.render("Liberals won!",True,(0,0,0),None)
fasVictoryText = victoryFont.render("Fascists won!",True,(0,0,0),None)

# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop 
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            carryOn = False # Flag that we are done so we exit this loop
    
    randCard = [random.randint(0,2),random.randint(0,2),random.randint(0,2)]
    # --- Game logic should go here
    # --- Drawing code should go here
    # First, clear the screen to white. 
    screen.fill(GREY)
    
    if libLaw > 4:
        libLaw = fasLaw = victory.DrawVictory(libVictoryText,screen,room_width,room_height)
    if fasLaw > 5:
        libLaw = fasLaw = victory.DrawVictory(fasVictoryText,screen,room_width,room_height)

    screen.blit(fascistBoard, (fasBoardX, fasBoardY))
    screen.blit(liberalBoard, (libBoardX, libBoardY))
    #The you can draw different shapes and lines or add text to your background stage.

    button.DrawButton(10,10,100,100,"Ready!",screen)
    endGame = button.DrawButton(10,120,100,100,"Exit",screen)
    addLib = button.DrawButton(20,room_height-80,240,60,"Add liberal law {0}".format(libLaw),screen)
    addFas = button.DrawButton(280,room_height-80,240,60,"Add fascist law {0}".format(fasLaw),screen)
    drawCard = button.DrawButton(20,room_height-330,200,200,"Draw three laws!",screen)
    mousePos = pygame.mouse.get_pos()
    mousePressed = pygame.mouse.get_pressed()

    if picking == 1:
        for i in range(0,len(indexCard)):
            if indexCard[i]==1:
                screen.blit(liberalLaw,(int(room_width-(i+1)*fasCardWidth),int(room_height-2*fasCardHeight/3)))
                if mousePos[1]>int(room_height-2*fasCardHeight/3) and mousePos[0]>int(room_width-(i+1)*fasCardWidth) and mousePos[0]<int(room_width-(i+1)*fasCardWidth+fasCardWidth):
                    screen.blit(liberalLaw,(int(room_width-(i+1)*fasCardWidth),int(room_height-fasCardHeight*0.8)))
                    if mousePressed[0]==1:
                        if discarded==0:
                            indexCard[i]=2
                            discarded = discarded + 1
                        elif discarded==1:
                            indexCard[i]=2
                            if sum(indexCard)==5:
                                libLaw = libLaw + 1
                                picking = 0
                                indexCard = [0,0,0]
                                discarded = 0
                            else:
                                fasLaw = fasLaw + 1
                                picking = 0
                                indexCard = [0,0,0]
                                discarded = 0
            elif indexCard[i]==0:
                screen.blit(fascistLaw,(int(room_width-(i+1)*fasCardWidth),int(room_height-2*fasCardHeight/3)))
                if mousePos[1]>int(room_height-2*fasCardHeight/3) and mousePos[0]>int(room_width-(i+1)*fasCardWidth) and mousePos[0]<int(room_width-(i+1)*fasCardWidth+fasCardWidth):
                    screen.blit(fascistLaw,(int(room_width-(i+1)*fasCardWidth),int(room_height-fasCardHeight*0.8)))
                    if mousePressed[0]==1:
                        if discarded==0:
                            indexCard[i]=2
                            discarded = discarded + 1
                        elif discarded==1:
                            indexCard[i]=2
                            if sum(indexCard)==5:
                                libLaw = libLaw + 1
                                picking = 0
                                indexCard = [0,0,0]
                                discarded = 0
                            else:
                                fasLaw = fasLaw + 1
                                picking = 0
                                indexCard = [0,0,0]
                                discarded = 0

    if (drawCard == True and picking == 0):
        if cardPressed == 0:
            picking = 1
            for i in range(0,2):
                if randCard[i]==2:
                    indexCard[i] = 1
                else:
                    indexCard[i] = 0
        cardPressed = 1
    else:
        cardPressed = 0

    if addLib:
        if libPressed == 0:
            libLaw = libLaw + 1
        libPressed = 1
    else:
        libPressed = 0

    if addFas:
        if fasPressed == 0:
            fasLaw = fasLaw + 1
        fasPressed = 1
    else:
        fasPressed = 0

    for i in range(0,fasLaw):
        screen.blit(fascistLaw, (int(fasCardX+fasBoardX+offsetFas*(i)),int(fasCardY+fasBoardY)))
    for i in range(0,libLaw):
        screen.blit(liberalLaw, (int(libCardX+libBoardX+offsetLib*(i)),int(libCardY+libBoardY)))
    # --- Go ahead and update the screen with what we've drawn.

    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)

    if endGame:
        break
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()