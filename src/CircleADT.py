## @brief
# @details 
import math
class CircleT:
    
    ## @brief __init__:initializes CircleT
    # @param x: x coordinate of the centre of the circle
    # @param y: y coordinate of the centre of the circle
    # @param r: the radius of the circle

    def __init__(self, x, y, r):
        self.x = float(x)
        self.y = float(y)
        self.r = float(r)
    ## @brief xcoord: a getter for x coordinate of the centre of the circle
    # @return x coordinate
    def xcoord(self):
        return self.x
    
    ## @brief ycoord: a getter for y coordinate of the centre of the circle
    # @return y coordinate    
    def ycoord(self):
        return self.y

    ## @brief radius: a getter for the radius of the circle
    # @return radius of the circle   
    def radius(self):
        return self.r

    ## @brief area: computes the area 
    # @return area of the circle    
    def area(self):
        return math.pi*(self.r**2)
    
    ## @brief circumference: computes the circumference
    # @return circumference of the circle    
    def circumference(self):
        return 2*math.pi*self.r

    ## @brief insideBox:checks to see if the circle is inside a given box
    # @param x0: x coordinate of the upper left corner of the box
    # @param y0: y coordinate of the upper left corner of the box
    # @param w:  the width of the box
    # @param h:  the height of the box
    # @return true if the circle is inside the box and otherwise false    
    def insideBox(self, x0, y0, w, h):
        if (((self.x + self.r) <= (x0+w)) and (x0 <= (self.x - self.r)) and (((self.y + self.r) <= y0) and ((y0-h) <= (self.y - self.r)))):
            return True
        else:
            return False

    ## @brief intersect:checks to see if the new circle intersects with the given circle
    # @param c: a new circle
    # @return true if the new circle intersects with the given circle and otherwise false 
    def intersect(self, c):
        if (((self.x - c.x)**2) + ((self.y - c.y)**2) <= ((c.r + self.r)**2)):
            return True
        else:
            return False

    ## @brief scale: changes radius of the given circle k times
    # @param k: a float number; changes the radius k times 
    def scale(self, k):
        self.r = float(k) * self.r

    ## @brief translate: changes x and y coordinate of the given circle 
    # @param dx: a float number; changes the centre of the circle by dx in the x direction
    # @param dy: a float number; changes the centre of the circle by dy in the y direction
    def translate(self, dx, dy):
        self.x = float(dx) + self.x
        self.y = float(dy) + self.y
        
        
