from abc import ABC,abstractmethod
class polygon:
    def area(self):
        pass
    def perimeter(self):
        pass

class square(polygon):
    def area(self):
        print("The area of square is side*side")
    def perimeter(self):
        print("The perimeter of square is 4*side")

class triangle(polygon):
    def area(self):
        print("The area of triangle is 1/2(l+b)")
    def perimeter(self):
        print("The perimeter of triangle is the sum of all three sides")
 
class rectangle(polygon):
    def area(self):
        print("The area of rectangle is length*breadth")
    def perimeter(self):
        print("The perimeter of rectangle is 2*(l+b)")  

class circle(polygon):
    def area(self):
        print("The area of circle is 3.14*r**2")
    def perimeter(self):
        print("The circumference of circle is 2*3.14*r")

class parallelogram(polygon):
    def area(self):
        print("The area of parallelogram is breadth*height")
    def perimeter(self):
        print("The perimeter of parallelogram is 2*(a+b)")

objectsquare=square()
objectsquare.area()
objectsquare.perimeter()

objecttriangle=triangle()
objecttriangle.area()
objecttriangle.perimeter()

objectrectangle=rectangle()
objectrectangle.area()
objectrectangle.perimeter()

objectcircle=circle()
objectcircle.area()
objectcircle.perimeter()

objectparallelogram=parallelogram()
objectparallelogram.area()
objectparallelogram.perimeter()