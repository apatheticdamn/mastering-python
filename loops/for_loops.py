'''
The for loop in Python is used to iterate over a sequence, which could be a list, tuple, array, or string.

while loop can be iterated unlimited times while for loop can be iterated limited times

while loop = unlimited
for loop = limited 
'''
import time 

for seconds in range(10, 0, -1): #for counting from 10 to 0 [start, stop, step] = [10, 0, -1]
    print(seconds)
    time.sleep(1)

print("Happy new year!")
