import pygame
import Client
import time
pygame.init()


# Define some colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREY = (128,128,128)
BLUE = ( 0, 0, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

print("IS CLIENT")
Client.connect()

room_width = 1280
room_height = 720
size = (room_width, room_height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Secret Hitler")
fascistBoard = pygame.image.load("sprites\FascistBoard.png")
liberalBoard = pygame.image.load("sprites\LiberalBoard.png")
fascistBoard = pygame.transform.scale(fascistBoard, (room_width-450,260))
liberalBoard = pygame.transform.scale(liberalBoard, (room_width-450,260))
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

    # --- Game logic should go here
    # --- Drawing code should go here
    # First, clear the screen to white. 
    screen.fill(GREY)
    
    screen.blit(fascistBoard, (225, 100))
    screen.blit(liberalBoard, (225, room_height-100-260))
    #The you can draw different shapes and lines or add text to your background stage.
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if mouse[0]>225 and mouse[0]<room_width-225 and mouse[1]>100 and mouse[1]<room_height-100:
        pygame.draw.rect(screen, RED, [225, 100, room_width-450, room_height-200],2)
        if click[0] == 1:
            pygame.draw.rect(screen, BLUE, [225, 100, room_width-450, room_height-200],2)
            Client.threadedFunction('isReady')
    else:
        pygame.draw.rect(screen, BLACK, [225, 100, room_width-450, room_height-200],2)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()