import pygame
import math
import random

pygame.init()


width = 150
height = 70

multiplier = 10


screen = pygame.display.set_mode((width*multiplier, height*multiplier))
pixelArray = pygame.PixelArray(screen)
screen.fill((255,255,255))
grid = [[0 for y in range(height)] for x in range(width)]
for i in range(width):
    for j in range(height):
        grid[i][j] = random.randint(0,1)

def countNeighbourhood(x,y,grid):
    count = 0
    for i in range(3):
        for j in range(3):
            xmodifier = 0
            if x+i > width:
                xmodifier -= width
            ymodifier = 0
            if y+j > height:
                ymodifier -= height
            if grid[x+i-1+xmodifier][y+j-1+ymodifier] == 1:
                count += 1
    if grid[x][y] == 1:
        count -= 1
    return count

n = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    tempgrid = [[0 for y in range(height)] for x in range(width)]
    for x in range(0, width):
        for y in range(0, height):
            colour = pygame.Color(255,255,255)
            if grid[x][y] == 0 and countNeighbourhood(x,y,grid) == 3:
                tempgrid[x][y] = 1
                colour = pygame.Color(0,0,0)
            if grid[x][y] == 1:
                if countNeighbourhood(x,y,grid) == 2 or countNeighbourhood(x,y,grid) == 3:
                    tempgrid[x][y] = 1
                    colour = pygame.Color(0,0,0)
                else:
                    tempgrid[x][y] = 0
            if pixelArray[x,y] != colour:
                pygame.draw.rect(screen, colour, pygame.Rect(multiplier*x, multiplier*y, multiplier, multiplier))
    grid = tempgrid
    n += 1
    pygame.display.update()