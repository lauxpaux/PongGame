#tutorial
#https://www.101computing.net/pong-tutorial-using-pygame-getting-started/



# Import the pygame library and initialise the game engine
import pygame
import random
pygame.init()

#Define some colors
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
BLUE=(0,0,255)
GOLD=(255,215,0)

#Key variables
difficulties=['Joke','Easy','Normal','Hard','Perfect']
inaccuracyranges=[10,7,5,3,1]
inaccuratecalcs=[450,400,350,300,0]
accuratecalcs=[600,600,550,500,200]
difficulty=0
gamestop=False
testingAI=False
calcsmade=0
inplace=False
endy=-1
streak=0

hbounces=[0.7,0.8,0.9,1,1,1.1,1.1,1.2,1.2,1.3]
vbounces=[1.3,1.2,1.1,1,1,0.9,0.9,0.8,0.8,0.7]

#Open a new window
arenawidth=690
arenaheight=540

size=(arenawidth,arenaheight)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

p1score=0
p2score=0
movespeed=30

ballx=350
bally=250
ballhspeed=20
ballvspeed=20
ballsize=30
startspeed=20
ph=90

starty=0
p1x=50
p1y=0

p2x=arenawidth-50
p2y=arenaheight-ph

def calculatefinalposition():
    global ballx
    global bally
    global ballhspeed
    global ballvspeed
    global ballsize
    tempx=ballx
    tempy=bally
    tempvspeed=ballvspeed
    temphspeed=ballhspeed
    while(tempx<arenawidth-50):
        if(tempy>arenaheight-ballsize or tempy<ballsize):
            tempvspeed*=-1
        tempx+=temphspeed
        tempy+=tempvspeed
    return tempy,tempvspeed

def makecalc(inaccuracyrange):
    global ballx
    global bally
    global ballhspeed
    global ballvspeed
    global ballsize
    global movespeed

    inplace=False
    endy,endvspeed=calculatefinalposition()
    if(inaccuracyrange>0):
        endy=endy+movespeed*random.randrange(1,(inaccuracyrange*2)+1)-inaccuracyrange*movespeed
    if(endy>arenaheight-ph):
        endy=arenaheight-ph
    print('Actual endy=',endy)
    print(endy)
    val=arenaheight
    if(endvspeed>0):
        while(val+endvspeed>endy):
            val-=movespeed
        endy=val
    else:
        while(val+endvspeed>endy):
            val-=movespeed
        endy=val
    print(endy,endvspeed)
    return endy
    
def resetball(playerscoring):
    global ballx
    global bally
    global ballhspeed
    global ballvspeed
    global ballsize
    global startspeed
    global p1y
    global p2y
    global starty
    global ph
    global inplace
    global calcsmade
    global streak
    global p1score
    global p2score

    if(playerscoring==1):
        ballhspeed=-startspeed
        ballvspeed=-startspeed
        ballx=350
        bally=250
        p1y=starty
        p2y=arenaheight-ph
        endy=-1
        inplace=False
        calcsmade=0
        streak=0
        p1score+=1
    else:
        ballhspeed=startspeed
        ballvspeed=startspeed
        ballx=350
        bally=250
        p1y=starty
        p2y=arenaheight-ph
        endy=-1
        inplace=False
        calcsmade=0
        streak=0
        if(playerscoring==2):
            p2score+=1



def playgame():
    global ballx
    global bally
    global ballhspeed
    global ballvspeed
    global ballsize
    global movespeed
    global startspeed
    global p1y
    global p2y
    global starty
    global ph
    global inplace
    global calcsmade
    global streak
    global p1score
    global p2score
    global gamestop
    global difficulty

    gameover=False

    p1_maxticker=2
    p1_moveticker=p1_maxticker

    styledirection=1

    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 64)
    while(not gamestop):
        #Draw Paddles
        screen.fill(BLACK)
        pygame.draw.circle(screen,WHITE,[ballx,bally],ballsize//2)
        pygame.draw.rect(screen,BLUE,[p1x,p1y,10,ph])
        if(difficulty<4):
            pygame.draw.rect(screen,RED,[p2x,p2y,10,ph])
        else:
            pygame.draw.rect(screen,GOLD,[p2x,p2y,10,ph])

        #Draw Text
        text = font.render(str(p1score), 1, BLUE)
        screen.blit(text, (75,10))

        if(difficulty<4):
            text = font.render(str(p2score), 1, RED)
            screen.blit(text, (575,10))
        else:
            text = font.render(str(p2score), 1, GOLD)
            screen.blit(text, (575,10))

        text = font.render(str(streak), 1, WHITE)
        screen.blit(text, (350,60))

        font = pygame.font.Font(None, 64)
        if(difficulty<4):
            text = font.render('Difficulty: '+difficulties[difficulty], 1, RED)
            screen.blit(text, (150,10))
        else:
            text = font.render('Difficulty: '+difficulties[difficulty], 1, GOLD)
            screen.blit(text, (150,10))

        if(not gameover):
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    gamestop = True # Flag that we are done so we exit this loop

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]:
                if(p1y>0):
                    p1y-=movespeed

            if pressed[pygame.K_DOWN]:
                if(p1y<arenaheight-ph):
                    p1y+=movespeed

            if pressed[pygame.K_w]:
                if(p12>0):
                    p2y-=movespeed
            if pressed[pygame.K_s]:
                if(p2y<arenaheight-ph):
                    p2y+=movespeed

            if(pressed[pygame.K_n]):
                if(p1_moveticker==0):
                    p1_moveticker=p1_maxticker
                    if(difficulty<4):
                        difficulty+=1
                        p1score=0
                        p2score=0
                        if(difficulty>4):
                            gamestop=True
                        else:
                            resetball(0)

            if(pressed[pygame.K_p]):
                if(p1_moveticker==0):
                    p1_moveticker=p1_maxticker
                    if(difficulty>0):
                        difficulty-=1
                        p1score=0
                        p2score=0
                        resetball(0)
            
            if(pressed[pygame.K_c]):
                p2score=3

            if(bally>arenaheight-ballsize and ballvspeed>0):
                ballvspeed*=-1
            elif(bally<ballsize and ballvspeed<0):
                ballvspeed*=-1

            #Move Ball
            ballx+=ballhspeed
            bally+=ballvspeed

            #player hits ball back
            if(bally>=p1y and bally<=p1y+ph and ballx<=p1x+abs(ballhspeed) and ballx>=p1x and ballhspeed<0):
                ballhspeed*=-1
                ballhspeed+=1
                if(ballvspeed>0):
                    ballvspeed+=1
                else:
                    ballvspeed-=1

                roll=random.randrange(0,len(hbounces)-1)
                ballhspeed=int(ballhspeed*hbounces[roll])
                ballvspeed=int(ballvspeed*vbounces[roll])
                calcsmade=0
                endy=-1
                streak+=1
            
            #When testing AI, ball is automatically hit back for player
            if(testingAI):
                if(ballx<50):
                    ballhspeed*=-1
                    ballhspeed+=1
                    if(ballvspeed>0):
                        ballvspeed+=1
                    else:
                        ballvspeed-=1
                    
                    roll=random.randrange(0,len(hbounces)-1)
                    ballhspeed=int(ballhspeed*hbounces[roll])
                    ballvspeed=int(ballvspeed*vbounces[roll])

                    calcsmade=0
                    endy=-1
                    streak+=1

            #AI hits ball back
            if(bally>=p2y and bally<=p2y+ph and ballx+abs(ballhspeed)>=p2x and ballx<=p2x and ballhspeed>0):
                ballhspeed*=-1
                ballhspeed-=1
                if(ballvspeed>0):
                    ballvspeed+=1
                else:
                    ballvspeed-=1
                
                #Top of paddle
                if(bally>=p2y and bally<p2y+30):
                    ballhspeed=int(ballhspeed*0.8)
                    ballvspeed=int(ballvspeed*1.1)
                #Middle of paddle
                elif(bally>=p2y+30 and bally<p2y+60):
                    q=1
                #Bottom of paddle
                else:
                    ballhspeed=int(ballhspeed*1.1)
                    ballvspeed=int(ballvspeed*0.8)

                calcsmade=0
                streak+=1

            #Inaccurate calc
            if(ballx>inaccuratecalcs[difficulty] and ballhspeed>0):
                if(calcsmade==0):
                    print('Calc 1')
                    endy=makecalc(inaccuracyranges[difficulty])
                    calcsmade+=1

            #Accurate calc
            if(ballx>accuratecalcs[difficulty] and ballhspeed>0):
                if(calcsmade==1):
                    print('Calc 2')
                    endy=makecalc(0)
                    calcsmade+=1

            if(ballx>inaccuratecalcs[difficulty] and ballhspeed>0):
                if(p2y-endy<movespeed and p2y-endy>-movespeed):
                    if(not inplace):
                        inplace=True
                        print('p2y=',p2y,'endy=',endy)
                if(p2y<endy):
                    p2y+=movespeed
                #ball is above
                elif(p2y>endy):
                    p2y-=movespeed

            #Reset to middle
            if(ballhspeed<0):
                if(difficulty>2):
                    #Stylish Movement
                    if(difficulty>3):
                        if(p2y==300):
                            styledirection=0
                        elif(p2y==180):
                            styledirection=1
                        if(p2y>180 and styledirection==0):
                            p2y-=movespeed
                        elif(p2y<300 and styledirection==1):
                            p2y+=movespeed
                        elif(p2y>300):
                            p2y-=movespeed
                        elif(p2y<180):
                            p2y+=movespeed
                    #Vanilla Movement
                    else:
                        if(p2y>240):
                            p2y-=movespeed
                        elif(p2y<240):
                            p2y+=movespeed
                

            #Ball gets past player
            if(ballx<0-ballsize):
                resetball(2)

            #Ball gets past AI
            elif(ballx>arenawidth+ballsize):
                resetball(1)
            
            #Player Wins. Next level or end game.
            if(p1score>2):
                difficulty+=1
                p1score=0
                p2score=0
                if(difficulty>4):
                    p1score=3
                    gameover=True
                    print('Gameover')
                else:
                    resetball(0)
            #AI Wins
            elif(p2score>2):
                gameover=True
                print('Gameover')

            if(p1_moveticker>0):
                p1_moveticker-=1
        else:
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    gamestop = True # Flag that we are done so we exit this loop

            if(p1score>2):
                text2 = font.render('CHAMPION', 1, BLUE)
                screen.blit(text2, (180,200))
            else:
                if(difficulty<4):
                    text2 = font.render('Difficulty: '+difficulties[difficulty], 1, RED)
                else:
                    text2 = font.render('Difficulty: '+difficulties[difficulty], 1, GOLD)
                screen.blit(text2, (180,200))

        pygame.display.flip()
        clock.tick(60)
    #Once we have exited the main program loop we can stop the game engine:
    pygame.quit()
playgame()