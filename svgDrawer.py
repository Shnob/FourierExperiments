import pygame, sys
import numpy as np
from math import pi
from cmath import exp
from svg.path import *

workingShape = sys.argv[1]

WIDTH = 900
HEIGHT = 900

svgpath = ""
n = 10000
scl = 20

with open ("shapes/{}.txt".format(workingShape), "r") as myfile:
    svgpath = myfile.read()

path = parse_path(svgpath)
pts = [(p.real * scl, p.imag * scl) for p in (path.point(i/n) for i in range(0, n+1))]

avgX = 0
avgY = 0

for i in range(len(pts)):
    avgX += pts[i][0]
    avgY += pts[i][1]

avgX /= len(pts)
avgY /= len(pts)

pts = [(p[0] - avgX, p[1] - avgY) for p in pts]
ptsCtr = [(p[0] + WIDTH/2, p[1] + HEIGHT/2) for p in pts]

def drawEntirePath(screen):
    pygame.draw.aalines(screen, (255, 255, 255), False, ptsCtr)


def main():
    pygame.init()
    pygame.display.set_caption("svgParser")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pass


        screen.fill( (0, 0, 0) )
        drawEntirePath(screen)

        pygame.display.update()

if __name__ == "__main__":
    main()