# Write a Python program to calculate the area of a trapezoid.
  #Area of trapezoid = (a + b)/2 * h

height = float(input("Height of trapezoid: "))
base_1 = float(input('Base one value: '))
base_2 = float(input('Base two value: '))
area = ((base_1 + base_2) / 2) * height
print("Area of trapezoid:", area)