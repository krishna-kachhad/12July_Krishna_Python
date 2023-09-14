# Write a Python program to convert degree to radian.

#-------------------Using formula--------------------------

pi=22/7
degree = float(input("Input degrees: "))
radian = degree*(pi/180)
print(radian)

#----------------------Using math module----------------------

import math
d = float(input("Input degrees: "))
print(math.radians(d))