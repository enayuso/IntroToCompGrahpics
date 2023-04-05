"""
@author: Enrique Ayuso
Assignment 4.A: Lagrange Interpolation Assignment
"""

import pygame
import numpy as np

width = 800
height = 800
# pygame.init()
screen = pygame.display.set_mode((width, height), 0 , 32)
pygame.display.set_caption("Lagrange Interpolation Assignment")

BLACK =  (   0,   0,   0)
BLUE =   (   0,   0, 255)
WHITE =  ( 255, 255, 255)

screen.fill(WHITE)

# Necessary variables and their respective values
clock = pygame.time.Clock()
# oldPoint = None
vertices = [] 
running = True # When console is active 

while running:
    time_passed = clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if len(vertices) < 3:
                x, y = pygame.mouse.get_pos()
                print ("Clicked at:  X - " + repr(x) + "  Y - " + repr(y))  
                pygame.draw.circle(screen, BLUE, (x,y), 6)
                vertices.append((x,y))

                if len(vertices) == 3: # Occurs after 3rd point is entered and coords are saved in 'vertices'
                    for t in np.arange(0.001, (len(vertices)- 1) + 0.001, 0.001): # calculates 'u' and 'v' points of the curve line, needed in order to have it displayed in the screen
                        xPoint = int(-(t - 1) * -0.5 * (t - 2) * vertices[0][0] + t * -(t - 2) * vertices[1][0] + 0.5 * t * (t - 1) * vertices[2][0])
                        yPoint = int(-(t - 1) * -0.5 * (t - 2) * vertices[0][1] + t * -(t - 2) * vertices[1][1] + 0.5 * t * (t - 1) * vertices[2][1])
                        pygame.draw.circle(screen, BLACK, (xPoint, yPoint), 1) # draws curve line as expected with lagrange polynomial formula
        elif event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()