import pygame, sys
import numpy as np
from math import pi
from cmath import exp

workingShape = sys.argv[1]

lines = []
with open ("fourierSeries/{}.fsd".format(workingShape), "r") as file:
    lines = file.readlines()

span = int((len(lines)/2 - 1)/2)
cValues = [None for i in range(span * 2 + 1)]

for i in range(span * 2 + 1):
    cValues[i] = complex(float(lines[2 * i]), float(lines[2 * i + 1]))

dT = 0.1
WIDTH = 900
HEIGHT = 900
SCL = 20

def calcFromT(t):
    V = 0 + 0j

    for i in range(span * 2 + 1):
        n = i - span
        c = cValues[i] * exp(1j * n * 2 * pi * t)
        #print(i, n, "|", c)

        V += c

    #print("\n\n\n")
    return V

def main():
    pygame.init()
    pygame.display.set_caption("Fourier Test Program")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    t = 0

    while True:
        dTime = clock.tick()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pass
        
        V = calcFromT(t)
        pygame.draw.circle(screen, (255, 255, 255), (SCL * V.real + WIDTH/2, -SCL * -V.imag + HEIGHT/2), 1)
        #screen.fill((0, 0, 0, 0))

        t += dT * dTime/1000.0
        pygame.display.update()

if __name__ == "__main__":
    main()