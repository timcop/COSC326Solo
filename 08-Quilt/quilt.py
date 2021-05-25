import pygame
pygame.init()

#COLOURS
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

#SCREEN
scWidth = 600
scHeight = 400
mainSc = pygame.display.set_mode((scWidth, scHeight))
pygame.display.set_caption("Quilt")

mainSc.fill(black)
