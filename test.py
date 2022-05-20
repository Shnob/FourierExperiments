import pygame, sys
import numpy as np
from math import pi
from cmath import exp

#cValues = [0 + 0j for i in range(51)]#[0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j]
#span = int((len(cValues) - 1)/2)

cValues = [(0.13707804431093182+0.008830467426359267j), (0.06769104096130701+0.10552202611890608j), 
(-0.011264817428754533+0.02944414518778491j), (0.07480661820505627-0.02065281788323221j), 
(0.05789731689935344+0.04555714041605078j), (0.00607995384040694-0.18859152825484693j), (0.5689382380256233-0.3913804708392418j), (1.3741254776553382+0.475988091600184j), (0.6511227461907686+2.095140234671938j), (-1.531949331471553+2.080271724379073j), (5.195488483877853e-14-3.199431830580579e-13j), (9.997135135331128+13.575489243827507j), (1.079578284479468-3.4740998499131712j), (1.8106950609653507-0.6272699899359387j), (0.6781302536570404+0.46651531925032363j), (0.005155031223442581+0.15896193671791983j), (0.08056871768403073-0.0634017611272864j), (0.11967959246927064+0.03301169612040799j), (-0.011063966183971692-0.028857136323330913j), (0.07436714695688118-0.11591181524886018j), (0.15119093221602173-0.009744377515070514j)]
span = 10

dT = 0.1
WIDTH = 900
HEIGHT = 900
SCL = 10

#for i in range(span * 2 + 1):
#    n = i - span
#
#    if (n > 0 and n % 2 == 1):
#        cValues[i] = 1/n * (-1 if ((n + 1) % 4 == 0) else 1)

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
        pygame.draw.circle(screen, (255, 255, 255), (SCL * V.real + WIDTH/2, -SCL * V.imag + HEIGHT/2), 1)
        #screen.fill((0, 0, 0, 0))

        t += dT * dTime/1000.0
        pygame.display.update()

if __name__ == "__main__":
    main()