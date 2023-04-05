"""
@author: Enrique Ayuso
Assignment 3: Barycentric Coordinates Assignment
"""

import pygame
import numpy as np

width = 800
height = 800
pygame.init()
screen = pygame.display.set_mode((width, height), 0 , 32)
pygame.display.set_caption("Barycentric Coordinates Assignment")

BLACK =  (   0,   0,   0)
BLUE =   (   0,   0, 255)
WHITE =  ( 255, 255, 255)
PURPLE = ( 128,   0, 128)

screen.fill(WHITE)

# Necessary variables and their respective values
clock = pygame.time.Clock()
oldPoint = None
vertices = [] # Store x,y of each point
# done = False
running = True # When console is active 

while running:
    time_passed = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if len(vertices) < 3: # len() returns the length of an object - in this case, 'vertices'
                x, y = pygame.mouse.get_pos() # retrieves x,y coords/values
                pygame.draw.circle(screen, BLUE, (x,y), 4)
                if oldPoint is not None:
                    pygame.draw.line(screen, BLACK, oldPoint, (x,y)) # Draws line between last two points
                oldPoint = (x,y)
                vertices.append((x,y)) # append() adds to an existing list ('vertices')
                print ("Clicked at:  X - " + repr(x) + "  Y - " + repr(y)) 
                if len(vertices) == 3: # occurs when 3 'points' are made
                    pygame.draw.line(screen, BLACK, (vertices[0][0], vertices[0][1]), (x,y)) # connects first point with third point
            elif len(vertices) == 3:
                x, y = pygame.mouse.get_pos() # retreives x,y coords after 'triangle' is made and coords are set
                pygame.draw.circle(screen, PURPLE, (x,y), 4)
                # u and v function is essentially:
                # u = [(y2 - y3) * (x - x3) + (x3 - x2) * y - y3] / [(y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3)]
                # v = [(y3 - y1) * (x - x3) + (x1 - x3) * y - y3] / [(y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3)]
                u = ((vertices[1][1] - vertices[2][1]) * (x - vertices[2][0]) + (vertices[2][0] - vertices[1][0]) * (y - vertices[2][1])) / ((vertices[1][1] - vertices[2][1]) * (vertices[0][0] - vertices[2][0]) + (vertices[2][0] - vertices[1][0]) * (vertices[0][1] - vertices[2][1]))
                v = ((vertices[2][1] - vertices[0][1]) * (x - vertices[2][0]) + (vertices[0][0] - vertices[2][0]) * (y - vertices[2][1])) / ((vertices[1][1] - vertices[2][1]) * (vertices[0][0] - vertices[2][0]) + (vertices[2][0] - vertices[1][0]) * (vertices[0][1] - vertices[2][1]))
                print ("Bary. Coords: " + repr(u) + "  " + repr(v) + "  " + repr(1-u-v)) 

        elif event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()
        

