import pygame

class button:
    """GUI"""

    def DrawButton(x1,y1,width,height,Text,Screen):
        knappfan = 0
        pressed = False
        font = pygame.font.Font("Fonts/fontSH.ttf",24,bold=True)
        buttonText = font.render(Text,True,(0,0,0),None)
        center = ((2*x1 + width)/2,(2*y1+height)/2)

        pygame.draw.rect(Screen,(128,128,128),[x1+2,y1+2,width-2,height-2],0)
        pygame.draw.line(Screen,(200,200,200),[x1,y1],[x1,y1+height],2)
        pygame.draw.line(Screen,(200,200,200),[x1,y1],[x1+width,y1],2)
        pygame.draw.line(Screen,(60,60,60),[x1+width,y1],[x1+width,y1+height],2)
        pygame.draw.line(Screen,(60,60,60),[x1,y1+height],[x1+width,y1+height],2)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if mouse[0]>x1 and mouse[0]<x1+width and mouse[1]>y1 and mouse[1]<y1+height:
            pygame.draw.rect(Screen,(140,140,140),[x1+2,y1+2,width-2,height-2],0)
            if click[0] == 1:
                knappfan = 1
                pygame.draw.rect(Screen,(90,90,90),[x1+2,y1+2,width-2,height-2],0)
                pygame.draw.line(Screen,(60,60,60),[x1,y1],[x1,y1+height],2)
                pygame.draw.line(Screen,(60,60,60),[x1,y1],[x1+width,y1],2)
                pygame.draw.line(Screen,(200,200,200),[x1+width,y1],[x1+width,y1+height],2)
                pygame.draw.line(Screen,(200,200,200),[x1,y1+height],[x1+width,y1+height],2)
                pressed = True

        Screen.blit(buttonText,[center[0]-buttonText.get_width()/2+knappfan,center[1]-buttonText.get_height()/2+knappfan])
        return pressed

class victory:

    def DrawVictory(Type,Screen,width,height):
        Screen.blit(Type,[width/2-Type.get_width()/2,height/2-Type.get_height()/2])
        pygame.display.flip()
        pygame.time.wait(2000)
        Screen.fill((100,100,100))
        return 0

class Law:
    def drawLaw(inderCard,Law,room_width,room_height,fasCardWidth,fasCardHeight):
        pressed = False
        for i in range(0,len(indexCard)):
            if indexCard[i]==1:
                screen.blit(Law,(int(room_width-(i+1)*fasCardWidth),int(room_height-2*fasCardHeight/3)))
                if mousePos[1]>int(room_height-2*fasCardHeight/3) and mousePos[0]>int(room_width-(i+1)*fasCardWidth) and mousePos[0]<int(room_width-(i+1)*fasCardWidth+fasCardWidth):
                    screen.blit(Law,(int(room_width-(i+1)*fasCardWidth),int(room_height-fasCardHeight*0.8)))
                    if mousePressed[0]==1:
                        pressed = True
        return pressed