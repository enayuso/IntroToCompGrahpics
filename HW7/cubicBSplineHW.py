"""
@author: Enrique Ayuso
Assignment 7: Cubic B-Spline Assignment
"""

import pygame
import numpy as np

arrKnots = []

# defining required knot function first
def base(knot, degree, v):
    if degree == 0:
        if arrKnots[knot] <= v < arrKnots[knot + 1]:
            return 1
        else:
            return 0
    return (base(knot, degree - 1, v) * ((v - arrKnots[knot]) / (arrKnots[knot + degree] - arrKnots[knot]))) + (base(knot + 1, degree - 1, v) * ((arrKnots[knot + degree + 1] - v) / (arrKnots[knot + degree + 1] - arrKnots[knot + 1])))

width = 800
height = 800
screen = pygame.display.set_mode((width,height), 0, 32)
pygame.display.set_caption("Cubic B-Spline Assignment")

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
                #vertices.append((x,y))
                print ("Clicked at:  X - " + repr(x) + "  Y - " + repr(y))
                
                if len(vertices) > 0:
                    pygame.draw.line(screen, BLACK, (vertices[-1][0], vertices[-1][1]), (x,y))
                vertices.append((x,y))
            
            if len(vertices) == 4:
                arrKnots = np.linspace(vertices[0][0], vertices[3][0], num = 8) # np.linspace() returns evenly spaced numbers over a specific interval

                for i in np.arange(vertices[0][0], vertices[3][0], 0.05):
                    xPoint, yPoint = 0, 0
                    dNum = 0
                    for j in range(0, len(vertices)):
                        bValue = base(j, 3, i)
                        xPoint = xPoint + (vertices[j][0] * bValue)
                        yPoint = yPoint + (vertices[j][1] * bValue)
                        dNum += bValue # dNum acts as the denominator
                    xPoint /= dNum
                    yPoint /= dNum
                    pygame.draw.circle(screen, PURPLE, (xPoint, yPoint), 1)
                    pygame.display.update() # adds the animation of the line creation. without this, the result would just suddenly pop up 

        elif event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()

pygame.quit()