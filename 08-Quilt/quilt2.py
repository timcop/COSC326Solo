import pygame
import sys
from copy import deepcopy

# Rectangle class
class Rectangle:
    def __init__(self, scale, colour):
        self.scale = scale
        self.colour = colour
        self.length
        self.x
        self.y

    def setCoords(self, x, y):
        self.x = x
        self.y = y

    # Draw method
    def drawRectangle(self, screen):
        pygame.draw.rect(screen, r.colour, [r.x, r.y, r.length, r.length])

# Input
rectangles = []
for line in sys.stdin:
    line = line.split()
    scale = line[0]
    colour = (line[1], line[2], line[3])
    rectangles.append(Rectangle(scale, colour))

#Screen
pygame.init()
WHITE = (255,255,255)
scWidth = 512
scHeight = scWidth
screen = pygame.display.set_mode([scWidth, scHeight])

# Find length of each rectangle
sum = 0
for r in rectangles:
    sum += r.scale
length = scWidth/sum
# Set each length
for r in rectangles:
    r.length = r.scale*length

## Draw each rectangle
drawn = []
pygame.display.set_caption("Quilts")
done = False
clock = pygame.time.Clock()
while not done:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)
    for r in rectangles:
        if len(drawn) == 0:
            ## Draw r in center
            r.x = scWidth/2 - r.length/2
            r.y = r.x
            r.drawRectangle(screen)
            drawn.append(r)
        else:
            temp = []
            for d in drawn:
                ## Draw 4 of r on each corner of d
                r1 = deepcopy(r)
                r1.setCoords(d.x - r.length/2, d.y - r.length/2)
                # Draw r1
                temp.append(r1)

                r2 = deepcopy(r)
                r2.setCoords(d.x + d.length - r.length/2, d.y - r.length/2)
                # Draw
                temp.append(r2)

                r3 = deepcopy(r)
                r3.setCoords(d.x + d.length - r.length/2, d.y + d.length - r.length/2)
                # Draw
                temp.append(r2)

                r2 = deepcopy(r)
                r2.setCoords(d.x - r2.length/2, d.y + d.length - r1.length/2)
                # Draw
                temp.append(r2)
            drawn = temp.copy()
    pygame.display.flip()
pygame.quit()
