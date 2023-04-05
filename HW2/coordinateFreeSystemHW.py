"""
@author: Enrique Ayuso
Assignment 2.A: Coordinate Free System
"""

import pygame
# from sys import exit
# from pygame.locals import *
import numpy as np

# These variables serves as the X,Y dimensions of the screen/console
width = 800
height = 800
pygame.init()
screen = pygame.display.set_mode((width, height), 0 , 32)
pygame.display.set_caption("Coordinate-Free System Assignment")

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

# Function to record point locations and draws point and line between points
while not done:
    time_passed = clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print ("Clicked at:  X - " + repr(x) + "  Y - " + repr(y)) # Displays coordinates in Terminal
            pygame.draw.circle(screen, BLUE, (x,y), 6) # Creates circle (point) when clicked

            if oldPoint is not None: # Initially, oldPoint contains no values/null
                for i in range(1000): 
                    i *= 0.001
                    # Setting up latest x and y values
                    xPoint = int(((1 - i) * oldPoint[0]) + (i * x))
                    yPoint = int(((1 - i) * oldPoint[1]) + (i * y))
                    pygame.draw.line(screen, BLACK, oldPoint, (xPoint, yPoint), 2) # Draws line between last 2 points
            oldPoint = (x, y) # 'updates' old x,y with recent x,y
            
        elif event.type == pygame.QUIT: # Terminates console upon exit
            done = True
    
    pygame.display.update()
    
pygame.quit()

