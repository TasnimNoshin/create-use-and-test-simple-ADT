## @file
# @details
from CircleADT import *
from Statistics import *

## @brief main: calls testCirclT and testStatistics to run the test

def main():
    testCircleT()
    testStatistics()
## @brief testCircleT: tests all the functions in  CircleT() and prints whether they pass or fail.    
def testCircleT():
    c = CircleT(0,0,4)
    d = CircleT(1,2,0)
    e = CircleT(10,10,2)
    f = CircleT(4,-1,3)
    g = CircleT(0,9,5)

    if(c.xcoord() == 0.0): print("Test1 for xcoord passed.")
    else: print("Test1 for xcoord failed.")
    if(d.xcoord() == 1.0): print("Test2 for xcoord passed.")
    else: print("Test2 for xcoord failed.")
    if(e.xcoord() == 10.0): print("Test3 for xcoord passed.")
    else: print("Test3 for xcoord failed.")
    if(f.xcoord() == 4.0): print("Test4 for xcoord passed.")
    else: print("Test4 for xcoord failed.")
    if(g.xcoord() == 0.0): print("Test5 for xcoord passed.")
    else: print("Test5 for xcoord failed.")

    if(c.ycoord() == 0.0): print("Test1 for ycoord passed.")
    else: print("Test1 for ycoord failed.")
    if(d.ycoord() == 2.0): print("Test2 for ycoord passed.")
    else: print("Test2 for ycoord failed.")
    if(e.ycoord() == 10.0): print("Test3 for ycoord passed.")
    else: print("Test3 for ycoord failed.")
    if(f.ycoord() == -1.0): print("Test4 for ycoord passed.")
    else: print("Test4 for ycoord failed.")
    if(g.ycoord() == 9.0): print("Test5 for ycoord passed.")
    else: print("Test5 for ycoord failed.")

    if(c.radius() == 4.0): print("Test1 for radius passed.")
    else: print("Test1 for radius failed.")
    if(d.radius() == 0.0): print("Test2 for radius passed.")
    else: print("Test2 for radius failed.")
    if(e.radius() == 2.0): print("Test3 for radius passed.")
    else: print("Test3 for radius failed.")
    if(f.radius() == 3.0): print("Test4 for radius passed.")
    else: print("Test4 for radius failed.")
    if(g.radius() == 5.0): print("Test5 for radius passed.")
    else: print("Test5 for radius failed.")

    if(c.area() == 50.26548245743669): print("Test1 for area passed.")
    else: print("Test1 for area failed.")
    if(d.area() == 0.0): print("Test2 for area passed.")
    else: print("Test2 for area failed.")
    if(e.area() == 12.566370614359172): print("Test3 for area passed.")
    else: print("Test3 for area failed.")
    if(f.area() == 28.274333882308138): print("Test4 for area passed.")
    else: print("Test4 for area failed.")
    if(g.area() == 78.53981633974483): print("Test5 for area passed.")
    else: print("Test5 for area failed.")

    if(c.circumference() == 25.132741228718345): print("Test1 for circumference passed.")
    else: print("Test1 for circumference failed.")
    if(d.circumference() == 0.0): print("Test2 for circumference passed.")
    else: print("Test2 for circumference failed.")
    if(e.circumference() == 12.566370614359172): print("Test3 for circumference passed.")
    else: print("Test3 for circumference failed.")
    if(f.circumference() == 18.84955592153876): print("Test4 for circumference passed.")
    else: print("Test4 for circumference failed.")
    if(g.circumference() == 31.41592653589793): print("Test5 for circumference passed.")
    else: print("Test5 for circumference failed.")

    if(c.insideBox(1,2,5,6) == True): print("Circle Test1 is inside the box")
    else: print("Circle Test1 is not inside the box")
    if(d.insideBox(1,2,5,6) == True): print("Circle Test2 is inside the box")
    else: print("Circle Test2 is not inside the box")
    if(e.insideBox(1,2,5,6) == True): print("Circle Test3 is inside the box")
    else: print("Circle Test3 is not inside the box")
    if(f.insideBox(1,2,6,6) == True): print("Circle Test4 is inside the box")
    else: print("Circle Test4 is not inside the box")
    if(g.insideBox(1,2,6,6) == True): print("Circle Test5 is inside the box")
    else: print("Circle Test5 is not inside the box")

    if(c.intersect(d) == True): print ("Circle Test1 intersects with Test2.")
    else:print ("Circle Test1 does not intersect with Test2.")
    if(d.intersect(e) == True): print ("Circle Test2 intersects with Test3.")
    else:print ("Circle Test2 does not intersect with Test3.")
    if(e.intersect(f) == True): print ("Circle Test3 intersects with Test4.")
    else:print ("Circle Test3 does not intersect with Test4.")
    if(f.intersect(g) == True): print ("Circle Test4 intersects with Test5.")
    else:print ("Circle Test4 does not intersect with Test5.")
    if(g.intersect(c) == True): print ("Circle Test5 intersects with Test1.")
    else:print ("Circle Test5 does not intersect with Test1.")
    
    c.scale(5)
    if(c.radius() == 20.0): print("Test1 for scale passed.")
    else:("Test1 for scale failed.")
    d.scale(5)
    if(d.radius() == 0.0): print("Test2 for scale passed.")
    else:("Test2 for scale failed.")
    e.scale(5)
    if(e.radius() == 10.0): print("Test3 for scale passed.")
    else:("Test3 for scale failed.")
    f.scale(5)
    if(f.radius() == 15.0): print("Test4 for scale passed.")
    else:("Test4 for scale failed.")
    g.scale(5)
    if(g.radius() == 45.0): print("Test5 for scale passed.")
    else:("Test5 for scale failed.")

    c.translate(2,3)
    if(c.xcoord() == 2.0 and c.ycoord() == 3.0): print("Test1 for translate passed.")
    else:("Test1 for translate failed.")
    d.translate(2,3)
    if(d.xcoord() == 3.0 and d.ycoord() == 5.0): print("Test2 for translate passed.")
    else:("Test2 for translate failed.")
    e.translate(2,3)
    if(e.xcoord() == 12.0 and e.ycoord() == 13.0): print("Test3 for translate passed.")
    else:("Test3 for translate failed.")
    f.translate(2,3)
    if(f.xcoord() == 6.0 and f.ycoord() == 2.0): print("Test4 for translate passed.")
    else:("Test4 for translate failed.")
    g.translate(2,3)
    if(g.xcoord() == 2.0 and g.ycoord() == 12.0): print("Test5 for translate passed.")
    else:("Test5 for translate failed.")

## @brief testStatistics: tests all the functions in  Statistics() and prints whether they pass or fail
def testStatistics():
    a = CircleT(0,0,4)
    b = CircleT(1,2,0)
    c = CircleT(10,10,2)
    d = CircleT(6,5,2)
    e = CircleT(0,9,5)
    circles=[a,b,c,d,e]

    if(average(circles) == 2.6000000000000001):print("Test for average passed.")
    else:print("Test for average failed.")

    if(stdDev(circles) == 1.7435595774162693):print("Test for stdDev passed.")
    else:print("Test for stdDev failed.")

    if(rank(circles) == [5, 3, 2, 1, 4]): print("Test for rank passed.")
    else:print("Test for rank failed.")
    

main()



















    
    

    
