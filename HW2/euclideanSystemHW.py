"""
@author: Enrique Ayuso
Assignment 2.B: Euclidean System
"""

import pygame

# These variables serves as the X,Y dimensions of the screen/console
width = 800
height = 800
pygame.init()
screen = pygame.display.set_mode((width, height), 0 , 32)
pygame.display.set_caption("Euclidean System Assignment")

# Defining colors that'll be used in this program
BLACK = (   0,   0,   0)
BLUE =  (   0,   0, 255)
WHITE = ( 255, 255, 255)

# Setting white background of screen/console
screen.fill(WHITE)

# Necessary variables and their respective values
clock = pygame.time.Clock()
oldPoint = None
done = False # Ends loop and console upon exit

while not done:
    time_passed = clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos() # gets x,y values from console
            print ("Clicked at:  X - " + repr(x) + "  Y - " + repr(y)) # Displays coordinates in Terminal
            pygame.draw.circle(screen, BLUE, (x,y), 6) # Draws 'point'

            if oldPoint is not None: # Initially has no values / Null
                xIncrement = 1 if x > oldPoint[0] else -1

                for xPoint in range(oldPoint[0], x, xIncrement): # Using Euclidean System 'Formula'
                    yPoint = int(((x - xPoint) / (x - oldPoint[0]) * oldPoint[1]) + (((xPoint - oldPoint[0]) / (x - oldPoint[0])) * y))
                    # pygame.draw.line(screen, BLACK, oldPoint, (xPoint, yPoint), 1)
                    screen.set_at((xPoint, yPoint), BLACK) # Recently learnt this! set_at() accesses pixels of console
            oldPoint = (x,y) # Updates x,y of 'old' point

        elif event.type == pygame.QUIT:
            done = True
            
    pygame.display.update()

pygame.quit()