"""
@author: Enrique Ayuso
Assignment 5: Cubic Bezier Assignment
"""

import pygame
import numpy as np

width = 800
height = 800
screen = pygame.display.set_mode((width,height), 0, 32)
pygame.display.set_caption("Cubic Bezier Assignment")

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
            
            if len(vertices) < 4:
                x, y = pygame.mouse.get_pos()
                pygame.draw.circle(screen, BLUE, (x,y), 6)
                vertices.append((x,y))
                print("Clicked at: X - " + repr(x) + "  Y - " + repr(y))

                if len(vertices) == 4:
                    for i in range(3):
                        pygame.draw.line(screen, BLACK, vertices[i], vertices[i+1])

                    for j in np.arange(0, 1.001, 0.001):
                        # Following the general form for a quadratic Bezier curve:
                        # P3,3(t) = (1 - t)^3 * P0 + 3 * t * (1 - t)^2 * P1 + 3 * t^2 * (1 - t) * P2 + t^3 * P3
                        # gotten from https://www.uio.no/studier/emner/matnat/ifi/nedlagte-emner/INF-MAT5340/v10/undervisningsmateriale/book.pdf
                        xPoint = (1 - j)**3 * vertices[0][0] + 3 * j * (1 - j)**2  * vertices[1][0] + 3 * j**2 * (1 - j) * vertices[2][0] + j**3 * vertices[3][0]
                        yPoint = (1 - j)**3 * vertices[0][1] + 3 * j * (1 - j)**2  * vertices[1][1] + 3 * j**2 * (1 - j) * vertices[2][1] + j**3 * vertices[3][1]
                        pygame.draw.circle(screen, PURPLE, (xPoint, yPoint), 2)

        elif event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
