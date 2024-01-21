'''
An exception is an event, which occurs during the execution of a program that disrupts the normal flow of the program's instructions. In general, when a Python script encounters a situation that it cannot cope with, it raises an exception. An exception is a Python object that represents an error.
'''


'''
example:

if we divide something from 0 our program will be interrupted with an error
and if someone is entering anything other than number then error will occur

'''
numerator = int(input("Enter a number to divide: "))
denominator = int(input("Enter a number to divide by: "))
result = numerator / denominator
print(result)


#exception handling

try:
	numerator = float(input("Enter a number to divide: "))
	denominator = float(input("Enter a number to divide by: "))
	result = numerator / denominator
except ZeroDivisionError:
	print("You can not divide something from 0")
except ValueError:
	print("Enter numbers only")
except Exception as e:
	print(e)
	print("Enter numbers only")

#we can also use else statement
else:
	print(result)

#this block of code will always execute even if an error occurs
finally:
	print("This line will always execute")