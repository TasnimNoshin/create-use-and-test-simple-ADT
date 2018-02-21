## @file Statistics.py
#  @title Statistics
#  @author Adele Olejarz (400010177)
#  @date Jan 28th, 2017
#MacID: olejarza

import numpy as np
import CircleADT as circle

## @brief This method returns the average radius from a list of circles
#  @param circles a list of type CircleT
#  @return the average radius length in the list
def average(circles):
    ##list of radii
    radii = [circle.radius() for circle in circles]
    temp= np.average(radii)
    return temp

## @brief This method returns the standard deviation of radius from a list of circles
#  @param circles a list of type CircleT
#  @return the standard deviation of the radii ((average distance from average radius))
def stdDev(circles):
    ## list of radii
    stand = [circle.radius() for circle in circles]
    return np.std(stand)

## @brief This method takes a list of CircleT objects, and returns a list sorted by radius.
#  @param circles a list of type CircleT
#  @return A list of positions, based on rank of the corresponding circle's radius
def rank(circles):
    ##here I assume that a user will not input a negative value for a circle's radius, as this would be nonsensical
    ##a new list to store the rankings by radius
    ranklist=[]
    ##a list of just the radii, to be changed as we find the next highest radius
    radlist = [circle.radius() for circle in circles]
    ##initializing ranklist, so we can change the rank of every element as we find it.
    for x in range(0,len(radlist)): ranklist.append(0)
    
    ##the actual ranking algorithm
    for rank in range(1,len(radlist)+1):
        hi = 0       ##initialized to first element
        for i in range(0,len(radlist)):
            if (radlist[i] >=radlist[hi]):
                hi = i

        ranklist[hi] = rank
        radlist[hi] = -9991 ##this replaces it in the list, so we can find next highest element.


        
    return(ranklist)

    
    

