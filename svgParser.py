import numpy as np
from math import pi
from cmath import exp
from svg.path import *
import sys

workingShape = sys.argv[1]
totalN = int(sys.argv[2]) * 2 + 1

svgpath = ""
integralRes = 1000

with open ("shapes/{}.txt".format(workingShape), "r") as myfile:
    svgpath = myfile.read()

path = parse_path(svgpath)
pts = [p for p in (path.point(i/integralRes) for i in range(0, integralRes))]

avg = 0

for i in range(len(pts)):
    avg += pts[i]

avg /= len(pts)

pts = [p - avg for p in pts]

cValues = [None for i in range(totalN)]

for i in range(totalN):
    n = i - int((totalN - 1)/2)

    sum = 0

    for j in range(integralRes):
        t = j / integralRes
        expVal = exp(1j * -n * 2 * pi * t)

        tmp = pts[j] * expVal
        sum += tmp

    integral = sum / integralRes
    cValues[i] = integral

with open('fourierSeries/{}.fsd'.format(workingShape), 'a') as file:
    file.truncate(0)
    for i in range(totalN):
        file.write("{:f}\n{:f}\n".format(cValues[i].real, cValues[i].imag))