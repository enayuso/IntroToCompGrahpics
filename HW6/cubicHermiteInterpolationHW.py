"""
@author: Enrique Ayuso
Assignment 6: Cubic Hermite Interpolation Assignment
"""

import pygame
import numpy as np

width = 800
height = 800
screen = pygame.display.set_mode((width,height), 0, 32)
pygame.display.set_caption("Cubic Hermite Interpolation Assignment")

BLACK =  (   0,   0,   0)
BLUE =   (   0,   0, 255)
WHITE =  ( 255, 255, 255)
PURPLE = ( 128,   0, 128)

screen.fill(WHITE)
clock = pygame.time.Clock()
vertices = []
running = True

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
                    arr1 = np.array([
                        [vertices[0][0]**3, vertices[0][0]**2, vertices[0][0], 1, 0, 0, 0, 0], # [x1^3, x1^2, x1, 1, 0, 0, 0, 0]
                        [vertices[1][0]**3, vertices[1][0]**2, vertices[1][0], 1, 0, 0, 0, 0], # [x2^3, x2^2, x2, 1, 0, 0, 0, 0]
                        [0, 0, 0, 0, vertices[1][0]**3, vertices[1][0]**2, vertices[1][0], 1], # [0, 0, 0, 0, x2^3, x2^2, x2, 1]
                        [0, 0, 0, 0, vertices[2][0]**3, vertices[2][0]**2, vertices[2][0], 1], # [0, 0, 0, 0, x3^3, x3^2, x3, 1]
                        [3 * vertices[1][0]**2, 2 * vertices[1][0], 1, 0, 0, 0, 0, 0],         # [3(x2^2), 2(x2), 1, 0, 0, 0, 0, 0]
                        [0, 0, 0, 0, 3 * vertices[1][0]**2, 2 * vertices[1][0], 1, 0],         # [0, 0, 0, 0, 3(x2^2), 2(x2), 1, 0]
                        [6 * vertices[1][0], 2, 0, 0, 0, 0, 0, 0],                             # [6(x2), 2, 0, 0, 0, 0, 0, 0]
                        [0, 0, 0, 0, 6 * vertices[1][0], 2, 0, 0]                              # [0, 0, 0, 0, 6(x1), 2, 0, 0]
                    ])

                    arr2 = np.array([vertices[0][1], vertices[1][1], vertices[1][1], vertices[2][1], 0, 0, 0, 0]) # [y1, y2, y2, y3, 0, 0, 0, 0]

                    result = np.dot(np.linalg.inv(arr1), arr2) # np.linalg.inv() computes the multiplicative inverse of a matrix (being 'arr1')
                    # np.dot() computes the dot product of two arrays (being 'arr1' and 'arr2')

                    for xPoint in np.arange(vertices[0][0], vertices[1][0], 0.5):
                        yPoint = result[0] * (xPoint**3) + result[1] * (xPoint**2) + result[2] * (xPoint) + result[3]
                        # using formula for Cubic Hermite Interpolation, being: y = a * t^3 + b * t^2 + c * t + d
                        # gotten from https://blog.demofox.org/2015/08/08/cubic-hermite-interpolation/
                        pygame.draw.circle(screen, PURPLE, (xPoint, yPoint), 2)

                    for xPoint in np.arange(vertices[1][0], vertices[2][0], 0.5):
                        yPoint = result[4] * (xPoint**3) + result[5] * (xPoint**2) + result[6] * (xPoint) + result[7]
                        # likewise here, using: y = a * t^3 + b * t^2 + c * t + d
                        pygame.draw.circle(screen, PURPLE, (xPoint, yPoint), 2)

        elif event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()

pygame.quit()