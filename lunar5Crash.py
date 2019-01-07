import pygame
import sys
import time

#def area for game
def moveLander():
    global landerX, landerY, landerDX, landerDY, crashed

    if landerY < sHeight - int(lWidth*1.05):
        landerX += landerDX
        landerY += landerDY
        landerDY += gravity
    else:
        crashed = True
    

def setFlameXY():
    global flameX, flameY, flamePic
    flameX = landerX + int(lWidth/2 - fWidth/2)
    flameY = landerY + int(fWidth * 2.25)
    flamePic += 1
    if flamePic >= len(flame):
        flamePic = 0

def thrusterUp():
    global landerDY
    landerDY -= 5
    
def cycleCrashedLander():
    global cLanderPic
    cLanderPic +=1
    if cLanderPic >= len(lCrashed):
        cLanderPic = 0

#basic variables
sWidth = 450
sHeight = 750
lWidth = 110
fWidth = 30
gravity = 1 # in pixels per cycle
cycleTime = 0.05 #in seconds

#group of tuples
cBlack = (27, 2, 79)
pygame.init()

sSize = (450, 750)
s = pygame.display.set_mode(sSize)
pygame.display.set_caption("Lunar Lander")

#load images
lander = pygame.image.load('images/lunar110.png')

flame = [ ]
for i in range(3):
    flame.append(pygame.image.load('images/flame/flame' + str(i) + '.gif'))

crashed = False
lCrashed = []
for i in range(50):
    if(i <= 9):
        lCrashed.append(pygame.image.load('images/lunarB/frame_0' + str(i) + '_delay-0.04s.gif'))
    
#set lander values
landerX = int((sWidth/2) - (lWidth/2))
landerY = 0
landerDX = 0
landerDY = gravity
#set flame values
flamePic = 0
flameX = 0
flameY = 0
setFlameXY()
#set crashed Lander Values
cLanderPic = 0

#do this first then test
#s.fill(cBlack)
#pygame.display.update()


while(True):
    #this is to manage mouseclicks and keys
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("We are quitting")
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                #print("You pressed the up arrow")
                thrusterUp()
##            if event.key == pygame.K_RIGHT:
##                location += 1
##            if event.type == pygame.key(pygame.K_UP):
##                print("You pressed the up arrow")

    s.fill(cBlack)
    if not crashed:
        s.blit(lander,(landerX,landerY))
        s.blit(flame[flamePic],(flameX,flameY))
    else:
        s.blit(lCrashed[cLanderPic],(landerX,landerY))
        cycleCrashedLander()
        
    pygame.display.update()
    time.sleep(cycleTime)
    moveLander()
    setFlameXY()
    



