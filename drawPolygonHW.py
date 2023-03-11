"""
@author: Enrique Ayuso
Assignment 1: Implement drawPolygon
Deadline: March 11, 2023
"""

import pygame
from sys import exit
from pygame.locals import *
import numpy as np
# a libary in Python; does support for large, multidimensional arrays and matrices,
# along with a large collection of high-level math functions to operate on such arrays.

# These variables serves as the X,Y dimension of the screen
width = 800
height = 800
pygame.init() # initializes all imported pygame modules
screen = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption("drawPolygon Assignment")

# Defining the colors that'll be used in this program
BLACK = (   0,   0,   0)
BLUE =  (   0,   0, 255)
WHITE = ( 255, 255, 255)

# Using a white background for the screen
screen.fill(WHITE)

# Necessary variables and their respective value
clock =pygame.time.Clock() # Clock will be used on the following conditional statement
done = False; # Ends loop (and console) upon exit
margin = 5 # Sizes up of rectangge generated upon mouse-click
pressed = -1 # used to record coordinates and display rectangle upon click
oldPoint = np.array([0,0]) 
currentPoint = np.array([0,0])

# Function to record mouse input and update 'pressed' variable
while not done:
    time_passed = clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: # when mouse button is pressed down
            pressed = 1
            x, y = pygame.mouse.get_pos()
            currentPoint = np.array((x, y))
            but1, but2, but3 = pygame.mouse.get_pressed()
            if but1 == 1 or but2 == 1 or but3 == 1: # displays same point icon regardless of which mouse button was pressed
                pygame.draw.rect(screen, BLUE, (currentPoint[0], currentPoint[1], 2.5 * margin, 2.5 * margin), 5)
        elif event.type == pygame.MOUSEMOTION: # no mouse button being pressed
            pressed = 0
        elif event.type == pygame.MOUSEBUTTONUP: # draws line between last 2 points upon release of mouse button
            pressed = 2
            currentPoint = pygame.mouse.get_pos()
            if oldPoint[0] != 0 and oldPoint[1] != 0: #will not draw random line at start since both initial X and Y are 0
                pygame.draw.polygon(screen, BLACK, [oldPoint, currentPoint], 2) # previously drawLine, without []
            oldPoint = currentPoint # updates X and Y after new point is made
        elif event.type == pygame.QUIT: # terminates console upon exit
            done = True
        else:
            pressed = -1
    
    # Used to display X, Y Coordinates and Value of Pressed and Tick on Terminal
    x, y = pygame.mouse.get_pos()
    currentPoint = np.array((x,y))
    print("Mouse X: " + repr(x) + " Y: " + repr(y) + " Pressed: " + repr(pressed) + " Tick: " + repr(time_passed))

    pygame.display.update() # Updates display

pygame.quit()

                     

