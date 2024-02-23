import pygame

# run before any other code
# start and initiate pygame, this initiates everything involved as well
pygame.init()

# display surface - the window the player sees
# add the width and height here 
screen = pygame.display.set_mode((800, 400))

while True: # this is to keep the game running 
    #draw all the elements and update everything 
    pygame.display.update() # this updates the display