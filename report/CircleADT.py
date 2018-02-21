## @file CircleADT.py
# @title CircleADT
# @author Adele Olejarz (400010177)
# @date Jan 28th, 2017
#MacID: olejarza

##want to use math.pi
import math


## @brief This class represents a circle
# @details This class represents a circle as a triple (x,y,r)
class CircleT(object):

    ##@brief Constructor for CircleT
    # @details Constructor accepts three real number parameters; x, y and r; where x and y define the origin of the circle, and r the radius.
    # @param x The x coordinate of the circle's origin
    # @param y The y coordinate of the circle's origin
    # @param r the radius of the circle
    # assume the user will not enter a 0 or negative radius
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r

    ## @brief Returns the x coordinate of the circle's origin
    #  @return a real number for the x coordinate
    def xcoord(self):
        return self.x


    ## @brief Returns the y coordinate of the circle's origin
    #  @return a real number for the y coordinate
    def ycoord(self):
        return self.y

    ## @brief Returns the radius of the circle
    #  @return a real number for the radius
    def radius(self):
        return self.r

    ## @brief Returns the area of the circle
    #  @return the area of the circle
    def area(self):
        return math.pi*(self.r**2)

    ## @brief Returns the circumference of the circle
    #  @return the circumference of the circle
    def circumference(self):
        return 2*math.pi*self.r

    ## @brief Returns a boolean regarding wether or not the circle is contained in a box
    #  @details insideBox accepts 4 inputs, x,y,w,h where x is the x coordinate of the left side of a box, y is the y coordinate of the top of the box, w is the width of the box, and h is the height of the box. The function will return true if the circle is within the box, and false if it is not.
    #  @param x The x coordinate of the box's left side
    #  @param y The y coordinate of the box's top
    #  @param w the width of the box
    #  @param h the height of the box
    #  @return a boolean, which is true if the circle is within the box, false otherwise
    def insideBox(self,x,y,w,h):
        ##here i assume that the edges of the box count as "in the box" so that a circle with diameter equal to the side length of a box will fit in the box if and only if they share the same origin (centre point)
        if ((self.x + self.r) <= (x+w) and (self.x - self.r) >= x):
            if((self.y + self.r)<= y and (self.y - self.r) >= y - h):
              return True ##if the points on the circle farthest up down left and right are within the box, the whole circle must be
            else: return False 
        else: return False
          
    ## @brief Returns a boolean regarding whether or not the circle shares any points in common with an additional input circle, c.
    #  @details If the combined radii are >= the distance, the circles MUST at least touch. By this logic, they intersect eachother as I consider the circumference a part of the circle
    #  @param c The circle to which the calling circle will be compared.
    #  @return a boolean, true if the circle shares any points with the input circle
    def intersect(self,c):
        ## originDist is the distance between the two circles' origins. Will be compared to radii to determine intersection 
        originDist = (math.sqrt((self.x - c.x)**2 + (self.y - c.y)**2))
        if ((c.r+self.r)>=originDist): return True
        else: return False

    ## @brief Multiplies the circle's radius by the input provided by the user
    #  @details Takes the absolute value of the input. In theory a negative value would invert the radius, but since this is a circle, and the origin won't change, the effect would not be noticable. as such i take the absolute value of the scale.
    #  @param k the float which to multiply the radius by
    def scale(self,k):
        self.r = self.r *abs(k);

    ## @brief Translates the origin of the circle, dx in the x direction, and dy in the y direction
    #  @param dx the amount to move the circle in the x direction
    #  @param dy the amount to move the circle in the y direction
    def translate(self,dx,dy):
        self.x += dx
        self.y += dy

    
    
        
