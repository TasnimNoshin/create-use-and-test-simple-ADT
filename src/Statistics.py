## @file
# @details 
import numpy
from CircleADT import *

## @brief average: computes the average radius of a given list of circles
# @param circles: list of circles
# @return the average radius 
def average(circles):
    radii = []
    for i in range(len(circles)):
        radii += [circles[i].radius()]
    return numpy.average(radii)

## @brief stdDev: computes the standard deviation of a given list of circles
# @param circles: list of circles
# @return standard deviation 
def stdDev(circles):
    radii = []
    for i in range(len(circles)):
        radii += [circles[i].radius()]
    return numpy.std(radii)

## @brief rank: computes a list ranked by radius from a given list of circles
# @param circles: list of circles
# @return a list ranked by radius 
def rank(circles):
    radii = []
    for i in range(len(circles)):
        radii += [circles[i].radius()]

    index = list(range(len(radii)))
    index.sorted(key=lambda x: radii[x])
    ranks = [0] * len(index)
    for i, x in enumerate(index):
        ranks[x] = i+1
    ranks.reverse()
    return ranks
    
