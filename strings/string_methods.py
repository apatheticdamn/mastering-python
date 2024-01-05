

'''
Python has a set of built-in methods that you can use on strings.
Note: All string methods returns new values. They do not change the original string.
'''

first_name = "kush"
last_name = "kumar yadav"
full_name = first_name + " " + last_name
age = 15
gpa = 3.9
print(full_name)
print(len(full_name)) # length method
print(full_name.find('yadav')) # find method '''it returns the index of the character'''
print(full_name.capitalize()) # capitalize method
print(full_name.upper()) # upper method
print(full_name.isdigit()) # checking if full name is a digit or not
#print(age.isdigit())  this code will give an error because isdigit method is only for strings

print(str(age).isdigit()) # that's why we have typecasted it

print(full_name.isalpha()) # for checking if a variable is alpahbetical or not. it will give use False because there is whitespace between them

print(full_name.count("a")) # for counting a character
print(full_name.count("f")) # this will return 0 because there is no f charater in full_name

print(full_name.replace("k", "p")) # his will replace every k character from the variable to p

print(full_name * 3) # very useful method