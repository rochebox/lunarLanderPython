import pygame
import sys
import time

#basic variables
sWidth = 450
sHeight = 750
lWidth = 110
gravity = 4 # in pixels per cycle
cycleTime = 0.05 #in seconds

#group of tuples
cBlack = (27, 2, 79)
pygame.init()

sSize = (450, 750)
s = pygame.display.set_mode(sSize)
pygame.display.set_caption("Lunar Lander")

#load images
lander = pygame.image.load('images/lunar110.png')

#set lander values
landerX = int((sWidth/2) - (lWidth/2))
landerY = 0
landerDX = 0
landerDY = gravity

#do this first then test
#s.fill(cBlack)
#pygame.display.update()

def moveLander():
    global landerX, landerY
    landerX += landerDX
    landerY += landerDY

while(True):
    #this is to manage mouseclicks and keys
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("We are quitting")
            pygame.quit()
            sys.exit()

    s.fill(cBlack)
    s.blit(lander,(landerX,landerY))
    pygame.display.update()
    time.sleep(cycleTime)
    moveLander()
    



