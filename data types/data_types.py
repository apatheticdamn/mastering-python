'''
Python has six standard Data Types:
Numbers.
String.
List.
Tuple.
Set.
Dictionary.
'''

name = "Kush"
age = 15
gpa = 3.9
is_attractive = True
print("is", name, "attractive?\n" + str(is_attractive))
print("The gpa of " + name + " is " + str(gpa))
print(name, "is", age, "years old")
print(name, "is the best programmer in the world")
print(name, "likes mai sakurajima")
print(name + " is " + str(age) + " years old") # we can concatenate int to str by typecasting.

'''
we can also store multiple variable with multiple values in just one line by seperating them with comma
'''

name, age, gpa, is_attractive = "Kush", 15, 3.9, True
print(name, age, gpa, is_attractive)

'''
we can also store multiple variable with just one value without writing them in seperate lines
'''

rating = views = likes = 5
print(rating)
print(likes)
print(views)