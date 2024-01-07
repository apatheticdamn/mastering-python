'''
While loop statements in Python are used to repeatedly execute a certain statement as long as the condition provided in the while loop statement stays true. While loops let the program control to iterate over a block of code.
'''

name = ""

while len(name) == 0:
    name = input("Enter your name: ")

print("Hello " + name.capitalize() + "!")
