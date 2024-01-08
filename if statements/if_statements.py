''''
The if statement is a conditional statement in python, that is used to determine whether a block of code will be executed or not. Meaning if the program finds the condition defined in the if statement to be true, it will go ahead and execute the code block inside the if statement.
'''

age = int(input("How old are you?: "))

if age >= 18 and age < 100:
    print("You are an adult you can watch anything")
elif age >= 100:
    print("You are a century old obviously you can watch anything")
elif age < 0:
    print("You haven't been born yet") #hahahahaha
else:
    print("You cannot watch any adult content")

