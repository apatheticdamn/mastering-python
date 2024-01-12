'''
The index operator (Python uses square brackets to enclose the index) selects a single character from a string.
'''
name = "apathetic damn"

if(name[0].islower()): # .islower() is a func for checking
    name = name.capitalize()

print(name)

first_name = name[:9] 
last_name = name[10:]

print(first_name)