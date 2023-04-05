"""
@author: Enrique Ayuso
Assignment 4.B: Cubic Bezier Assignment
"""

import pygame
import numpy as np

width = 800
height = 800
# pygame.init()
screen = pygame.display.set_mode((width, height), 0 , 32)
pygame.display.set_caption("Bezier Assignment")

BLACK =  (   0,   0,   0)
BLUE =   (   0,   0, 255)
WHITE =  ( 255, 255, 255)
PURPLE = ( 128,   0, 128)

screen.fill(WHITE)

# Necessary variables and their respective values
clock = pygame.time.Clock()
# oldPoint = None
vertices = [] # Since Barycentric involves 2D/3D space
running = True # When console is active 

while running:
    time_passed = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if len(vertices) < 3:
                x, y = pygame.mouse.get_pos()
                pygame.draw.circle(screen, BLUE, (x,y), 6)
                vertices.append((x,y))
                print ("Clicked at:  X - " + repr(x) + "  Y - " + repr(y)) 

                if len(vertices) == 3:
                    for i in range(2): # used to make a straight line to connect the points together
                        pygame.draw.line(screen, BLACK, vertices[i], vertices[i+1])

                    for j in np.arange(0, 1.001, 0.001): # used to draw the 'bezier' curve 
                        # from Bezier formula:
                        # B(t) = (1 - t)[(1 - t)P0 + tP1] + t[(1- t)P1 + tP2], 0 <= t <= 1
                        xPoint = (1 - j) * ((1 - j) * vertices[0][0] + j * vertices[1][0]) + j * ((1 - j) * vertices[1][0] + j * vertices[2][0])
                        yPoint = (1 - j) * ((1 - j) * vertices[0][1] + j * vertices[1][1]) + j * ((1 - j) * vertices[1][1] + j * vertices[2][1])
                        pygame.draw.circle(screen, PURPLE, (xPoint, yPoint), 2)

        elif event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()

pygame.quit()