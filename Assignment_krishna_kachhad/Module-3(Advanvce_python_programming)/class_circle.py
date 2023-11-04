# Write a Python class named Circle constructed by a radius and two methods which will compute the area 
  # and the perimeter of a circle.[area = pi*r*r] [perimeter = 2*pi*r]

class Circle():

    def radius(self,radius):
        r = radius
    def area(self,r):
        area = 3.142*r*r
        print("Area of the circle is: ",area)
    def peri(self,r):
        peri = 2*3.14*r
        print("Perimeter of the circle is: ",peri)

c = Circle()
radius = int(input("Enter the radius of circle: "))
c.area(radius)
c.peri(radius)

#------------------------------------------------------------------------------------------------------------
class Circle():
    
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14
    
    def perimeter(self):
        return 2*self.radius*3.14

NewCircle = Circle(8)
print(NewCircle.area())
print(NewCircle.perimeter())