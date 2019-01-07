import pygame
import sys

#group of tuples
cBlack = (27, 2, 79)
pygame.init()

sSize = (450, 750)
s = pygame.display.set_mode(sSize)
pygame.display.set_caption("Lunar Lander")

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

    s.fill(cBlack)
    pygame.display.update()
    



