#  area = a * b(squared)* 1 over tan(pie over 4)
#  all divided by 4
import math

a = int(input("number of sides: "))
b = int(input("the length of a side: "))
d = (a * (b*b) * (1/math.tan(math.pi/a)))/4
print( "The area of the polygon is:", int(d))