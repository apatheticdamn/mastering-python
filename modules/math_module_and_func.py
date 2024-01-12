'''
The math module is a standard module in Python and is always available. To use mathematical functions under this module, you have to import the module using import math . It gives access to the underlying C library functions. For example, # Square root calculation import math math.sqrt(4)
'''

import math

pi = 3.14

print(round(pi))

print(math.ceil(pi)) #for rounding up

print(math.floor(pi)) #for rounding down

print(abs(pi)) #for printing the absoulute value, The use of the abs() function has converted the negative numbers into positive ones.


print(pow(pi, 2)) #for adding power or exponent to a value

print(math.sqrt(4)) #for printing the square root of 4

x = 39
y = 78
z = 100

print(max(x, y, z)) #for printing the maximum value

print(min(x,y,z, pi)) #for printing the minimum value

print(math.pi) #for printing the value of pi