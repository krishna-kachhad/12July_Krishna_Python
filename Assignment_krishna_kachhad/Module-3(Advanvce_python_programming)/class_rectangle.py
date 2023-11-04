# Write a Python class named Rectangle constructed by a length and width and a method 
  # which will compute the area of a rectangle

class rectangle():
    def __init__(self,width,length):
        self.width=width
        self.length=length
    def area(self):
        return self.width * self.length
a=int(input("Enter length of rectangle: "))
b=int(input("Enter width of rectangle: "))
obj=rectangle(a,b)
print("Area of rectangle:",obj.area())
 